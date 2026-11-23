#!/usr/bin/env python3
"""OSS license advisor data tool (schema 2.1).

  license_lookup.py lookup <license id, name or alias>
  license_lookup.py model <model name>
  license_lookup.py compat <inbound license> <outbound license>
  license_lookup.py obligations <license> --scenario internal|saas|distribute|device
  license_lookup.py triage <file> [--scenario ...]   (one license per line, or CSV/TSV with a license column)

Names resolve exactly (alias, SPDX ID, then name); a partial name returns candidates instead of a guess.
Every output ends with the disclaimer. Exit 2 from triage if any HIGH, BLOCK or UNKNOWN. Standard library only.
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def _load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


DB = _load("licenses.json")
LIC = DB["licenses"]
ALIASES = _load("aliases.json")
COMP = _load("compatibility.json")
MODELS = _load("models.json")
GROUPS = {label: set(g["members"]) for label, g in _load("compat_groups.json")["groups"].items()}

# The only values `obligations` and `triggers` may hold (docs/schema.md defines each). MCP tool schemas and the tests
# read them from here.
OBLIGATIONS = frozenset({
    "attribution", "notice_file", "state_changes", "source_disclosure", "same_license", "network_source_offer",
    "relinking", "installation_info", "patent_retaliation", "noncommercial_only", "no_competing_service",
    "mau_revenue_cap", "maas_gate", "naming_rule", "usage_policy", "no_derivatives", "reference_only",
    "no_production_use",
})
TRIGGERS = frozenset({
    "distribution", "network_interaction", "service_offering", "competing_use", "commercial_use", "threshold",
    "prohibited_use", "any_use",
})
SCENARIOS = {
    "internal": set(),
    "saas": {"network_interaction", "service_offering", "competing_use", "threshold", "prohibited_use", "any_use",
             "commercial_use"},
    "distribute": {"distribution", "competing_use", "threshold", "prohibited_use", "any_use", "commercial_use"},
    "device": {"distribution", "threshold", "prohibited_use", "any_use", "commercial_use"},
}
FAMILY_RISK = {
    "public_domain": "LOW", "permissive": "LOW", "content_data": "REVIEW", "weak_copyleft": "MEDIUM",
    "strong_copyleft": "HIGH", "network_copyleft": "HIGH", "source_available": "HIGH", "noncommercial": "BLOCK",
    "ethical_source": "HIGH", "ai_model_licenses": "REVIEW", "hardware": "REVIEW", "proprietary": "REVIEW",
    "exception": "REVIEW",
}
ORDER = ["LOW", "REVIEW", "MEDIUM", "HIGH", "BLOCK", "UNKNOWN"]
DISCLAIMER = (
    "\n[Caveat] Check each record's provenance.verification_status and caveat flag; Secondary-only and Not re-verified"
    " entries must be confirmed against the official text.\n[Disclaimer] " + DB["disclaimer"] + " Data generated "
    + DB["generated"] + "; jurisdiction: US (general) with EU overlay."
)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9.+]", "", s.lower())


_BY_ID = {norm(r["id"]): r for r in LIC}
_BY_NAME = {norm(r["name"]): r for r in LIC}
_ALIAS = {norm(k): v for k, v in ALIASES.items()}


def resolve(query: str) -> dict:
    """{"match": alias|id|name|candidates|none, "records": [...]}. Only alias, id and name are exact."""
    q = norm(query)
    if not q:
        return {"match": "none", "records": []}
    if q in _ALIAS and norm(_ALIAS[q]) in _BY_ID:
        return {"match": "alias", "records": [_BY_ID[norm(_ALIAS[q])]]}
    if q in _BY_ID:
        return {"match": "id", "records": [_BY_ID[q]]}
    if q in _BY_NAME:
        return {"match": "name", "records": [_BY_NAME[q]]}
    hits = [r for r in LIC if q in norm(r["id"]) or q in norm(r["name"])]
    hits.sort(key=lambda r: (not norm(r["id"]).startswith(q), len(r["id"]), r["id"]))
    return {"match": "candidates" if hits else "none", "records": hits}


def unique(query: str) -> dict | None:
    """The one record a query names, or None when it names none or several."""
    res = resolve(query)
    if res["match"] in ("alias", "id", "name") or len(res["records"]) == 1:
        return res["records"][0]
    return None


def family_risk(record: dict, scenario: str) -> str:
    family = record["family"]
    base = FAMILY_RISK.get(family, "REVIEW")
    triggers = set(record.get("triggers", []))
    if scenario == "internal":
        # Internal use is blocked by an actual use restriction, not by a commercial-use trigger (which only says what
        # sets obligations off). Size-, revenue- or production-bounded licenses depend on who you are and what you do.
        obligations = set(record.get("obligations", []))
        bounded = "mau_revenue_cap" in obligations or "threshold" in triggers
        if obligations & {"noncommercial_only", "reference_only"} or (family == "noncommercial" and not bounded):
            return "BLOCK"
        if bounded or "no_production_use" in obligations:
            return "REVIEW"
        if "any_use" in triggers and family.endswith("copyleft"):
            return base  # copyleft duties that apply to any use, internal included (e.g. RPL-1.5's "Deploy")
        if base in ("REVIEW", "HIGH") and family.startswith(("ai", "ethical", "propriet")):
            return "REVIEW"
        return "LOW"
    if not (triggers & SCENARIOS[scenario]) and base in ("MEDIUM", "HIGH"):
        return "LOW"
    if scenario == "device" and "installation_info" in record.get("obligations", []):
        return "HIGH"
    return base


def lookup(query: str) -> dict:
    res = resolve(query)
    out = {"query": query, "match": res["match"], "results": res["records"][:5]}
    if res["match"] == "candidates" and len(res["records"]) > 1:
        out["note"] = f"{len(res['records'])} licenses match; give the exact SPDX ID: " + ", ".join(
            r["id"] for r in res["records"][:12])
    return out


def model(query: str) -> list[dict]:
    q = norm(query)
    return [m for m in MODELS if q and (q in norm(m["model"]) or q in norm(m["vendor"]))]


def compat(inbound: str, outbound: str) -> dict:
    """Compatibility tuples for putting `inbound` code into a work under `outbound`, matched on license IDs."""
    ri, ro = unique(inbound), unique(outbound)
    if ri is None or ro is None:
        bad = [(q, resolve(q)) for q, r in ((inbound, ri), (outbound, ro)) if r is None]
        return {"error": "; ".join(
            f"{q!r} is {'ambiguous: ' + ', '.join(x['id'] for x in res['records'][:8]) if res['records'] else 'unknown'}"
            for q, res in bad)}
    tuples = [t for t in COMP if ri["id"] in GROUPS.get(t["inbound"], ()) and ro["id"] in GROUPS.get(t["outbound"], ())]
    return {"inbound": ri["id"], "outbound": ro["id"], "tuples": tuples}


def obligations(query: str, scenario: str) -> dict:
    if scenario not in SCENARIOS:
        return {"error": f"scenario must be one of {', '.join(SCENARIOS)}"}
    r = unique(query)
    if r is None:
        res = resolve(query)
        return {"error": f"{query!r} is " + (
            "ambiguous: " + ", ".join(x["id"] for x in res["records"][:8]) if res["records"] else "not in the database")}
    return {
        "id": r["id"], "scenario": scenario,
        "triggers_hit": sorted(set(r.get("triggers", [])) & SCENARIOS[scenario]),
        "obligations": r.get("obligations", []), "risk": family_risk(r, scenario),
        "editorial_view": r.get("editorial_view"), "provenance": r["provenance"],
    }


# SPDX operators are case-sensitive: "or" inside a license name is part of the name.
_TOKEN = re.compile(r"\(|\)|[^\s()]+")
OPS = ("AND", "OR", "WITH")


def expression_risk(expr: str, scenario: str) -> tuple[str, str, object]:
    """(license ID or text, risk, volatile) for an SPDX expression. OR takes the least risky choice, AND the most;
    AND binds tighter than OR; WITH keeps the license and drops the exception. Unknown or ambiguous parts are UNKNOWN."""
    tokens = _TOKEN.findall(expr)
    pos = 0

    def leaf(text):
        r = unique(text)
        return (r["id"], family_risk(r, scenario), r["provenance"].get("volatile")) if r else (text, "UNKNOWN", None)

    def primary():
        nonlocal pos
        if pos < len(tokens) and tokens[pos] == "(":
            pos += 1
            v = disjunction()
            pos += 1 if pos < len(tokens) and tokens[pos] == ")" else 0
        else:
            words = []
            while pos < len(tokens) and tokens[pos] not in ("(", ")") and tokens[pos] not in OPS:
                words.append(tokens[pos])
                pos += 1
            v = leaf(" ".join(words))
        if pos < len(tokens) and tokens[pos] == "WITH":
            pos += 1
            while pos < len(tokens) and tokens[pos] not in ("(", ")") and tokens[pos] not in ("AND", "OR"):
                pos += 1
        return v

    def conjunction():
        nonlocal pos
        parts = [primary()]
        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            parts.append(primary())
        return max(parts, key=lambda x: ORDER.index(x[1]))

    def disjunction():
        nonlocal pos
        parts = [conjunction()]
        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            parts.append(conjunction())
        return min(parts, key=lambda x: ORDER.index(x[1]))

    return disjunction() if tokens else (expr, "UNKNOWN", None)


def read_components(path: str) -> list[tuple[str, str]]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    if lines and ("," in lines[0] or "\t" in lines[0]):
        rows = csv.DictReader(lines, delimiter="\t" if "\t" in lines[0] else ",")
        key = next((x for x in rows.fieldnames if "licen" in x.lower()), rows.fieldnames[0])
        return [(row.get("name") or row.get("component") or "", row[key] or "") for row in rows]
    return [("", line.strip()) for line in lines if line.strip()]


def triage(components: list[tuple[str, str]], scenario: str) -> list[dict]:
    return [
        dict(zip(("component", "license", "id", "risk", "volatile"), (comp, expr, *expression_risk(expr, scenario))))
        for comp, expr in components
    ]


def _print(obj) -> None:
    print(json.dumps(obj, indent=1, ensure_ascii=False))


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[0]
    scenario = argv[argv.index("--scenario") + 1] if "--scenario" in argv else "distribute"
    args = [a for i, a in enumerate(argv[1:], 1) if not a.startswith("--") and argv[i - 1] != "--scenario"]
    if cmd == "lookup":
        out = lookup(" ".join(args))
        _print(out if out["results"] else "Not in database - classify manually against references/ and the official text.")
        print(DISCLAIMER)
        return 0 if out["results"] else 1
    if cmd == "model":
        hits = model(" ".join(args))
        _print(hits or "Model not mapped - read the license shipped with the checkpoint.")
        print(DISCLAIMER)
        return 0
    if cmd == "compat" and len(args) >= 2:
        out = compat(args[0], args[1])
        _print(out if "error" in out or out["tuples"] else {**out, "note": "No tuple - analyze manually."})
        print(DISCLAIMER)
        return 1 if "error" in out else 0
    if cmd == "obligations":
        out = obligations(args[0], scenario)
        _print(out)
        print(DISCLAIMER)
        return 1 if "error" in out else 0
    if cmd == "triage":
        if scenario not in SCENARIOS:
            print(f"scenario must be one of {', '.join(SCENARIOS)}")
            return 1
        rows = triage(read_components(args[0]), scenario)
        print(f"scenario: {scenario}\ncomponent\tlicense\tid\trisk\tvolatile")
        for r in rows:
            print(f"{r['component']}\t{r['license']}\t{r['id']}\t{r['risk']}\t{r['volatile']}")
        print("(OR = least risky alternative; AND = most risky; AND binds tighter than OR; review)" + DISCLAIMER)
        return 2 if any(ORDER.index(r["risk"]) >= ORDER.index("HIGH") for r in rows) else 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
