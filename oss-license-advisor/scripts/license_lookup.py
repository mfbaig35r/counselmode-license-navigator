#!/usr/bin/env python3
"""OSS license advisor data tool (schema 2.1).

  license_lookup.py lookup <license id, name or alias>
  license_lookup.py model <model name>
  license_lookup.py project <project name> [--version X]   (or "Redis 7.4"; keyed by version)
  license_lookup.py compat <inbound license> <outbound license>
  license_lookup.py obligations <license> --scenario internal|saas|distribute|device
  license_lookup.py triage <file> [--scenario ...]   (one license per line, or CSV/TSV with a license column)
  license_lookup.py choose <goal> [--not-open-source] [--includes LICENSE,LICENSE]   (goals: see data/choosing.json)

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


def _load(name, default=None):
    path = os.path.join(DATA, name)
    if default is not None and not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


DB = _load("licenses.json")
LIC = DB["licenses"]
ALIASES = _load("aliases.json")
COMP = _load("compatibility.json")
MODELS = _load("models.json")
PROJECTS = _load("projects.json", default=[])
GROUPS = {label: set(g["members"]) for label, g in _load("compat_groups.json")["groups"].items()}
GOALS = {g["goal"]: g for g in _load("choosing.json")["goals"]}

# The only values `obligations` and `triggers` may hold (docs/schema.md defines each). MCP tool schemas and the tests
# read them from here.
OBLIGATIONS = frozenset(
    {
        "attribution",
        "notice_file",
        "state_changes",
        "source_disclosure",
        "same_license",
        "network_source_offer",
        "relinking",
        "installation_info",
        "patent_retaliation",
        "noncommercial_only",
        "no_competing_service",
        "mau_revenue_cap",
        "maas_gate",
        "naming_rule",
        "usage_policy",
        "no_derivatives",
        "reference_only",
        "no_production_use",
    }
)
TRIGGERS = frozenset(
    {
        "distribution",
        "network_interaction",
        "service_offering",
        "competing_use",
        "commercial_use",
        "threshold",
        "prohibited_use",
        "any_use",
    }
)
SCENARIOS = {
    "internal": set(),
    "saas": {
        "network_interaction",
        "service_offering",
        "competing_use",
        "threshold",
        "prohibited_use",
        "any_use",
        "commercial_use",
    },
    "distribute": {"distribution", "competing_use", "threshold", "prohibited_use", "any_use", "commercial_use"},
    "device": {"distribution", "threshold", "prohibited_use", "any_use", "commercial_use"},
}
FAMILY_RISK = {
    "public_domain": "LOW",
    "permissive": "LOW",
    "content_data": "REVIEW",
    "weak_copyleft": "MEDIUM",
    "strong_copyleft": "HIGH",
    "network_copyleft": "HIGH",
    "source_available": "HIGH",
    "noncommercial": "BLOCK",
    "ethical_source": "HIGH",
    "ai_model_licenses": "REVIEW",
    "hardware": "REVIEW",
    "proprietary": "REVIEW",
    "exception": "REVIEW",
}
ORDER = ["LOW", "REVIEW", "MEDIUM", "HIGH", "BLOCK", "UNKNOWN"]
DISCLAIMER = (
    "\n[Caveat] Check each record's provenance.verification_status and caveat flag; Secondary-only and Not re-verified"
    " entries must be confirmed against the official text.\n[Disclaimer] "
    + DB["disclaimer"]
    + " Data generated "
    + DB["generated"]
    + "; jurisdiction: US (general) with EU overlay."
)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9.+]", "", s.lower())


def words(s: str) -> str:
    """Lowercase words with every other separator turned into one space ("Llama 3.1 8B" -> "llama 3.1 8b")."""
    return re.sub(r"[^a-z0-9.+]+", " ", s.lower()).strip()


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
    return rating(record, scenario)["level"]


# How a trigger reads inside a rating's `because`.
TRIGGER_PHRASE = {
    "distribution": "distribution",
    "network_interaction": "users interacting with it over a network",
    "service_offering": "offering it as a service",
    "competing_use": "competing use",
    "commercial_use": "commercial use",
    "threshold": "a size, revenue or user threshold",
    "prohibited_use": "uses the license prohibits",
    "any_use": "any use",
}


def _words(keys) -> str:
    return ", ".join(TRIGGER_PHRASE.get(k, k.replace("_", " ")) for k in sorted(keys))


def rating(record: dict, scenario: str) -> dict:
    """CounselMode's first-pass risk rating for one license and one use, and why: `because` names the path the rule
    took (the license family, the triggers this use hits, or the reason it drops to LOW). A derived rating, not a
    legal conclusion."""
    family = record["family"]
    kind = family.replace("_", " ")
    base = FAMILY_RISK.get(family, "REVIEW")
    triggers = set(record.get("triggers", []))
    obligations = set(record.get("obligations", []))

    def out(level, because):
        return {"level": level, "because": because}

    if scenario == "internal":
        # Internal use is blocked by an actual use restriction, not by a commercial-use trigger (which only says what
        # sets obligations off). Size-, revenue- or production-bounded licenses depend on who you are and what you do.
        bounded = "mau_revenue_cap" in obligations or "threshold" in triggers
        if blocked := obligations & {"noncommercial_only", "reference_only"}:
            return out("BLOCK", f"the license allows only {_words(blocked).replace(' only', '')} use")
        if family == "noncommercial" and not bounded:
            return out("BLOCK", "a noncommercial license; internal use at a business is commercial use")
        if bounded:
            return out("REVIEW", "rights depend on a size, revenue or user threshold; check where you stand")
        if "no_production_use" in obligations:
            return out("REVIEW", "production use is not licensed unless a grant allows it")
        if "any_use" in triggers and family.endswith("copyleft"):
            return out(base, f"{kind}, with duties that apply to any use, internal use included")
        if base in ("REVIEW", "HIGH") and family.startswith(("ai", "ethical", "propriet")):
            return out("REVIEW", f"{kind}: its use terms apply even to internal use; read them")
        return out("LOW", "internal use triggers none of its obligations")
    hit = triggers & SCENARIOS[scenario]
    if not hit and base in ("MEDIUM", "HIGH"):
        return out("LOW", f"{kind}, but this use triggers none of its obligations")
    if scenario == "device" and "installation_info" in obligations:
        return out("HIGH", f"{kind}; shipping it on a device triggers the installation-information duty")
    if base == "LOW":
        return out("LOW", f"{kind}: notice-type obligations only")
    return out(base, kind + (f"; this use triggers {_words(hit)}" if hit else ""))


VIEW_LABEL = "CounselMode's view: judgment, not fact or legal advice."


def labelled(record: dict) -> dict:
    """A record for an answer: its editorial view under `counselmode_view`, labelled, apart from the facts."""
    out = {k: v for k, v in record.items() if k != "editorial_view"}
    view = record.get("editorial_view") or {}
    if isinstance(view, str):  # a project's one-sentence view
        view = {"view": view}
    view = {k: v for k, v in view.items() if k != "attribution"}
    if view:
        out["counselmode_view"] = {"label": VIEW_LABEL, **view}
    return out


def lookup(query: str) -> dict:
    """Exact matches return the full record. A partial name returns a short list of candidates (ID, name, family) to
    choose from; exceptions appear only when the query asks for one."""
    res = resolve(query)
    if res["match"] != "candidates":
        return {"query": query, "match": res["match"], "results": [labelled(r) for r in res["records"][:5]]}
    records = res["records"]
    if "exception" not in query.lower():
        records = [r for r in records if r.get("record_type") != "exception"] or records
    if len(records) == 1:
        return {"query": query, "match": "candidates", "results": [labelled(records[0])]}
    return {
        "query": query,
        "match": "candidates",
        "results": [{"id": r["id"], "name": r["name"], "family": r["family"]} for r in records[:12]],
        "note": f"{len(records)} licenses match; ask which one is meant and look it up by its exact SPDX ID.",
    }


def model(query: str) -> list[dict]:
    """Model records for a query, matched on each record's `aliases` (the version names people type), never on free
    text: "Gemma" finds every Gemma record, "Llama 3.1 8B Instruct" finds Llama 3.x, but "Mistral Large 2.1" does not
    match "Mistral Large 2" (a version boundary). A vendor name returns that vendor's records."""
    q = norm(query)
    if not q:
        return []
    return [
        m
        for m in MODELS
        if any(_alias_hit(query, a) for a in m.get("aliases") or [m["model"]]) or norm(m["vendor"]).startswith(q)
    ]


def model_family(m: dict) -> tuple[str, str]:
    """(vendor, family): the words of the first alias before its first version number ("Gemma 4 E2B" -> "gemma")."""
    first = (m.get("aliases") or [m["model"]])[0]
    return m["vendor"], re.split(r"\s*\d", first, maxsplit=1)[0].strip().lower()


def other_versions(hits: list[dict]) -> list[dict]:
    """Versions in the same families as `hits` that are under a different license (Gemma 1 to 3 for Gemma 4), so an
    answer about one version can say the others differ."""
    families = {model_family(m) for m in hits}
    licenses = {m["license_id"] for m in hits}
    return [
        {"model": m["model"], "license": m["license"], "license_id": m["license_id"]}
        for m in MODELS
        if model_family(m) in families and m not in hits and m["license_id"] not in licenses
    ]


def _alias_hit(query: str, alias: str) -> bool:
    """Same name or broader ("Gemma" for "Gemma 4"), or more specific at a word break ("Llama 3.1 8B" for "Llama 3.1",
    but not "Mistral Large 2.1" for "Mistral Large 2")."""
    q, q_words = norm(query), words(query)
    a, a_words = norm(alias), words(alias)
    return bool(q) and (a.startswith(q) or (q_words.startswith(a_words) and q_words[len(a_words) :][:1] in ("", " ")))


_VERSION = re.compile(r"^(.*?)[\s-]+v?(\d+(?:\.\d+)*)\+?$")


def _version(v: str | None) -> tuple[int, ...] | None:
    nums = re.findall(r"\d+", v or "")
    return tuple(int(n) for n in nums) if nums else None


def _in_era(v: tuple[int, ...], era: dict) -> bool:
    """A version is in an era when it falls within its release lines: "7.2" as an upper bound covers every 7.2.x."""
    lo, hi = _version(era["versions"]["from"]), _version(era["versions"]["to"])
    return (lo is None or v[: len(lo)] >= lo) and (hi is None or v[: len(hi)] <= hi)


def project(query: str, version: str | None = None) -> list[dict]:
    """Project records for a query, matched on name, id and `aliases` like model(); each carries its license eras. With a
    version (given, or trailing the query as in "Redis 7.4"), only the era covering that version is kept, with its risk
    per scenario."""

    def names(p):
        return [p["name"], p["id"], *p.get("aliases", [])]

    # A trailing version ("Redis 7.4") is a version, unless it is part of a name ("Python 3" as an alias).
    m = _VERSION.match(query.strip())
    if version is None and m and not any(norm(query) == norm(a) for p in PROJECTS for a in names(p)):
        query, version = m.group(1), m.group(2)
    hits = [p for p in PROJECTS if any(_alias_hit(query, a) for a in names(p))]
    v = _version(version)
    out = []
    for p in hits:
        eras = [e for e in p["eras"] if v is None or _in_era(v, e)]
        if v is not None:
            eras = [
                {
                    **e,
                    "ratings": {
                        s: expression_rating(e["license_expression"], s) for s in ("internal", "saas", "distribute")
                    },
                }
                for e in eras
            ]
        out.append(labelled({**p, "eras": eras, **({"version": version} if version else {})}))
    return out


def compat(inbound: str, outbound: str) -> dict:
    """Compatibility tuples for putting `inbound` code into a work under `outbound`, matched on license IDs."""
    ri, ro = unique(inbound), unique(outbound)
    if ri is None or ro is None:
        bad = [(q, resolve(q)) for q, r in ((inbound, ri), (outbound, ro)) if r is None]
        return {
            "error": "; ".join(
                f"{q!r} is {'ambiguous: ' + ', '.join(x['id'] for x in res['records'][:8]) if res['records'] else 'unknown'}"
                for q, res in bad
            )
        }
    tuples = [t for t in COMP if ri["id"] in GROUPS.get(t["inbound"], ()) and ro["id"] in GROUPS.get(t["outbound"], ())]
    return {"inbound": ri["id"], "outbound": ro["id"], "tuples": tuples}


def combine(inbound_id: str, outbound_id: str) -> str:
    """Can code under `inbound_id` go into a distributed work under `outbound_id`? yes, conditional, no or unknown."""
    results = {
        t["result"]
        for t in COMP
        if t["context"] == "distribution_combined_work"
        and t["result"] != "not_applicable"
        and inbound_id in GROUPS.get(t["inbound"], ())
        and outbound_id in GROUPS.get(t["outbound"], ())
    }
    if not results:
        return "unknown"
    if "no" in results:
        return "no"
    return "conditional" if results & {"conditional", "yes_narrows"} else "yes"


def choose(goal: str, must_be_open_source: bool = True, includes: list[str] | None = None) -> dict:
    """Outbound licenses for a goal (data/choosing.json, CounselMode editorial view), each checked against the licenses
    of code you include. A candidate that cannot take one of them is excluded, with the reason."""
    if goal not in GOALS:
        return {"error": f"goal must be one of {', '.join(GOALS)}"}
    deps = []
    for q in includes or []:
        r = unique(q)
        if r is None:
            res = resolve(q)
            return {
                "error": f"{q!r} is "
                + (
                    "ambiguous: " + ", ".join(x["id"] for x in res["records"][:8])
                    if res["records"]
                    else "not in the database"
                )
            }
        deps.append(r["id"])
    g = GOALS[goal]
    pool = [dict(c, not_open_source=False) for c in g["candidates"]]
    if not must_be_open_source:
        pool += [dict(c, not_open_source=True) for c in g.get("not_open_source", [])]
    recommendations, excluded = [], []
    for c in pool:
        r = _BY_ID[norm(c["id"])]
        checks = {d: combine(d, r["id"]) for d in deps}
        blocked = [d for d, v in checks.items() if v == "no"]
        if blocked:
            excluded.append({"id": r["id"], "because": f"cannot include {', '.join(blocked)} in a distributed work"})
            continue
        recommendations.append(
            {
                "id": r["id"],
                "name": r["name"],
                "note": c.get("note"),
                "not_open_source": c["not_open_source"],
                "osi_status": r.get("osi_status"),
                "patent_grant": r.get("patent_grant"),
                "with_your_code": checks,
                "provenance": r["provenance"],
            }
        )
    out = {
        "goal": goal,
        "title": g["title"],
        "for": g["for"],
        "why": g["why"],
        "trade_offs": g["trade_offs"],
        "recommendations": recommendations,
        "excluded": excluded,
        "attribution": "CounselMode editorial view; not legal advice",
    }
    if not must_be_open_source and g.get("not_open_source"):
        out["note_not_open_source"] = (
            "Entries marked not_open_source are source-available or use-restricted, not open source."
        )
    if deps and not recommendations:
        out["note"] = (
            "None of the recommended licenses can include " + ", ".join(deps) + ". The included code's license "
            "usually decides the outbound license: check_compatibility shows what can take it."
        )
    elif any(v in ("unknown", "conditional") for r in recommendations for v in r["with_your_code"].values()):
        out["note"] = (
            "Some combinations are conditional or not covered by the data: check them against the license texts."
        )
    return out


def obligations(query: str, scenario: str) -> dict:
    if scenario not in SCENARIOS:
        return {"error": f"scenario must be one of {', '.join(SCENARIOS)}"}
    r = unique(query)
    if r is None:
        res = resolve(query)
        return {
            "error": f"{query!r} is "
            + (
                "ambiguous: " + ", ".join(x["id"] for x in res["records"][:8])
                if res["records"]
                else "not in the database"
            )
        }
    return {
        "id": r["id"],
        "scenario": scenario,
        "triggers_hit": sorted(set(r.get("triggers", [])) & SCENARIOS[scenario]),
        "obligations": r.get("obligations", []),
        "rating": rating(r, scenario),
        "counselmode_view": labelled(r).get("counselmode_view"),
        "provenance": r["provenance"],
    }


# SPDX operators are case-sensitive: "or" inside a license name is part of the name.
_TOKEN = re.compile(r"\(|\)|[^\s()]+")
OPS = ("AND", "OR", "WITH")


def _fold(expr: str, leaf, rank):
    """Evaluate an SPDX expression: OR keeps the part with the lowest rank, AND the highest; AND binds tighter than OR;
    WITH keeps the license and drops the exception. `leaf` maps a license name to a value, `rank` orders values."""
    tokens = _TOKEN.findall(expr)
    pos = 0

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
        return max(parts, key=rank)

    def disjunction():
        nonlocal pos
        parts = [conjunction()]
        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            parts.append(conjunction())
        return min(parts, key=rank)

    return disjunction() if tokens else None


def expression_risk(expr: str, scenario: str) -> tuple[str, str, object]:
    """(license ID or text, risk, volatile) for an SPDX expression. OR takes the least risky choice, AND the most.
    Unknown or ambiguous parts are UNKNOWN."""

    def leaf(text):
        r = unique(text)
        return (r["id"], family_risk(r, scenario), r["provenance"].get("volatile")) if r else (text, "UNKNOWN", None)

    return _fold(expr, leaf, lambda x: ORDER.index(x[1])) or (expr, "UNKNOWN", None)


# From most open to most closed: how a project is grouped by license.
OPENNESS = [
    "public_domain",
    "permissive",
    "weak_copyleft",
    "strong_copyleft",
    "network_copyleft",
    "content_data",
    "hardware",
    "ethical_source",
    "source_available",
    "noncommercial",
    "ai_model_licenses",
    "proprietary",
    "unknown",
]


def expression_family(expr: str) -> str:
    """The family of an SPDX expression: the most open choice in an OR, the most restrictive part of an AND."""

    def leaf(text):
        r = unique(text)
        return r["family"] if r and r["family"] in OPENNESS else "unknown"

    return _fold(expr, leaf, OPENNESS.index) or "unknown"


def expression_rating(expr: str, scenario: str) -> dict:
    """A rating object for an SPDX expression: the level from expression_risk, and why, naming the license that
    decided it when the expression offers a choice (OR) or combines licenses (AND)."""
    chosen, level, _ = expression_risk(expr, scenario)
    record = unique(chosen) if level != "UNKNOWN" else None
    because = rating(record, scenario)["because"] if record else "the license is not recognised; read it directly"
    if record and re.search(r"\b(OR|AND)\b", expr):
        because = f"via {chosen}: {because}"
    return {"level": level, "because": because}


def read_components(path: str) -> list[tuple[str, str]]:
    with open(path, encoding="utf-8") as f:
        return parse_components(f.read().splitlines())


def parse_components(lines: list[str]) -> list[tuple[str, str]]:
    """(component, license) pairs from one license or SPDX expression per line, or CSV/TSV with a license column."""
    lines = [line for line in lines if line.strip()]
    if lines and ("," in lines[0] or "\t" in lines[0]):
        rows = csv.DictReader(lines, delimiter="\t" if "\t" in lines[0] else ",")
        key = next((x for x in rows.fieldnames if "licen" in x.lower()), rows.fieldnames[0])
        return [(row.get("name") or row.get("component") or "", row[key] or "") for row in rows]
    return [("", line.strip()) for line in lines if line.strip()]


def triage(components: list[tuple[str, str]], scenario: str) -> list[dict]:
    rows = []
    for comp, expr in components:
        chosen, _, volatile = expression_risk(expr, scenario)
        rows.append(
            {
                "component": comp,
                "license": expr,
                "id": chosen,
                "rating": expression_rating(expr, scenario),
                "volatile": volatile,
            }
        )
    return rows


def _print(obj) -> None:
    print(json.dumps(obj, indent=1, ensure_ascii=False))


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[0]
    scenario = argv[argv.index("--scenario") + 1] if "--scenario" in argv else "distribute"
    args = [
        a
        for i, a in enumerate(argv[1:], 1)
        if not a.startswith("--") and argv[i - 1] not in ("--scenario", "--includes", "--version")
    ]
    if cmd == "lookup":
        out = lookup(" ".join(args))
        _print(
            out if out["results"] else "Not in database - classify manually against references/ and the official text."
        )
        print(DISCLAIMER)
        return 0 if out["results"] else 1
    if cmd == "model":
        hits = model(" ".join(args))
        _print(hits or "Model not mapped - read the license shipped with the checkpoint.")
        print(DISCLAIMER)
        return 0
    if cmd == "project":
        version = argv[argv.index("--version") + 1] if "--version" in argv else None
        hits = project(" ".join(a for a in args if a != version), version)
        _print(hits or "Project not mapped - read the LICENSE file in the exact release you use.")
        print(DISCLAIMER)
        return 0 if hits else 1
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
    if cmd == "choose":
        includes = argv[argv.index("--includes") + 1].split(",") if "--includes" in argv else []
        out = choose(args[0], must_be_open_source="--not-open-source" not in argv, includes=includes)
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
            print(f"{r['component']}\t{r['license']}\t{r['id']}\t{r['rating']['level']}\t{r['volatile']}")
        print("(OR = least risky alternative; AND = most risky; AND binds tighter than OR; review)" + DISCLAIMER)
        return 2 if any(ORDER.index(r["rating"]["level"]) >= ORDER.index("HIGH") for r in rows) else 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
