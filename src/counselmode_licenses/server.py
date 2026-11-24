"""CounselMode License Navigator: an MCP server over the bundled license data. Every answer carries its provenance and
the disclaimer; nothing here is legal advice. Run over stdio with `counselmode-licenses` (or `uvx counselmode-licenses`).
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from importlib.metadata import PackageNotFoundError, version
from typing import Annotated, Literal
from urllib.parse import quote

from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError, ToolError
from mcp.types import ToolAnnotations
from pydantic import Field

from counselmode_licenses.skill import lookup, references, skill_dir

READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
MAX_COMPONENTS = 500
SITE = "https://counselmode.com"
NOT_ADVICE = "This is not legal advice."
HANDOFF = f"For a full compliance screening of these dependencies, with a report, see {SITE}."
# What each kind of claim in an answer is. One short sentence per answer, not per item.
RATING_BASIS = (
    "Ratings: CounselMode's rule (license family + what this use triggers; OR takes the least risky option, AND "
    "the most), not a legal conclusion."
)
RULINGS_BASIS = "Rulings: CounselMode's reading of the licenses and FSF/OSI positions, not a legal conclusion."
CHOOSE_BASIS = "Recommendations: CounselMode's editorial view, not legal advice."
# Answers say what is unverified (verification_gaps) and what is judgment (the basis lines and counselmode_view), so
# the closing line only needs what applies to every answer.
DISCLAIMER = (
    "Not legal advice. Confirm anything that matters against the license text, and ask a lawyer for decisions with "
    "real consequences. Jurisdiction: US (general), with an EU overlay."
)
DATA_FILES = ("licenses", "compatibility", "compat_groups", "models", "projects", "aliases", "context")
Scenario = Literal["internal", "saas", "distribute", "device"]

INSTRUCTIONS = """\
License answers for software, AI models and data, from a curated dataset keyed by SPDX ID. Not legal advice.

- Resolve the exact license first. If lookup_license returns candidates, ask the user which one; never pick.
- For AI models, use model_license with the exact model and version; never infer a license from the vendor.
- For a named software project (Redis, Terraform, Linux), use project_license with the version in use: licenses
  change between releases.
- Ask which scenario applies (internal use, SaaS, distribution, a device) before stating obligations or risk.
- Every record has provenance: say how it was verified and when, and say so plainly when it is not re-verified or
  volatile. Recommend confirming anything that matters against the license text, and a lawyer for real decisions.
- Answers separate three kinds of claim. Facts carry a source and a verification status: state them with the source.
  Ratings (`rating`, `ratings`) and compatibility rulings are CounselMode's rule-based judgments: attribute them
  ("CounselMode rates this HIGH for SaaS, because ...") and give the `because`. `counselmode_view` is editorial
  judgment: present it as CounselMode's view. Never present a rating, ruling or view as a legal conclusion.
- If an answer has `verification_gaps`, say which parts are not fully verified.
- Coverage of the whole dataset (what is verified and what is not) is the resource licenses://coverage.
The method in full is the resource licenses://skill."""


def _version() -> str:
    try:
        return version("counselmode-licenses")
    except PackageNotFoundError:
        return "dev"


def _url(record: dict) -> str:
    source = (record.get("provenance") or {}).get("source") or record.get("source") or ""
    found = re.search(r"https?://[^\s;,)]+", source)
    if found:
        return found.group(0)
    if "Listed" in str((record.get("provenance") or {}).get("spdx_list_status")):
        return f"https://spdx.org/licenses/{record['id']}.html"
    return SITE


def _coverage(ll) -> dict:
    """Counts by verification status for each part of the dataset."""

    def count(statuses):
        c = Counter("Verified (primary)" if s.startswith("Verified (primary)") else s for s in statuses)
        return dict(sorted(c.items(), key=lambda kv: -kv[1]))

    eras = [e for p in ll.PROJECTS for e in p["eras"]]
    return {
        "note": "Verified (primary): checked against a primary source. Anything else says what is missing. "
        "Ratings and compatibility rulings are CounselMode's judgment even when the facts under them are verified.",
        "licenses": {"total": len(ll.LIC), "by_status": count(r["provenance"]["verification_status"] for r in ll.LIC)},
        "compatibility_rulings": {"total": len(ll.COMP), "by_status": count(t["verification_status"] for t in ll.COMP)},
        "project_license_eras": {"total": len(eras), "by_status": count(e["verification_status"] for e in eras)},
        "models": {"total": len(ll.MODELS), "by_status": count(m.get("verification_status") or "?" for m in ll.MODELS)},
    }


def _verification_gaps(answer) -> list[dict]:
    """Every record, ruling, model or project era in an answer whose verification status is not fully verified."""
    gaps, seen = [], set()

    def walk(node, owner=None):
        if isinstance(node, list):
            for item in node:
                walk(item, owner)
        elif isinstance(node, dict):
            owner = node.get("id") or node.get("name") or owner
            status = node.get("verification_status") or (node.get("provenance") or {}).get("verification_status")
            if status and not status.startswith("Verified (primary)"):
                what = node.get("id") or node.get("model") or node.get("license_expression")
                if "inbound" in node and "outbound" in node:
                    what = f"{node['inbound']} into {node['outbound']} ({node.get('context', '')})"
                elif "license_expression" in node and owner:
                    what = f"{owner}: {node['license_expression']}"
                if what and what not in seen:
                    seen.add(what)
                    gaps.append({"what": what, "status": status})
            for key, value in node.items():
                if key not in ("provenance", "change"):
                    walk(value, owner)

    walk(answer)
    return gaps


def _era_range(era: dict) -> str:
    lo, hi = era["versions"]["from"], era["versions"]["to"]
    if lo is None and hi is None:
        return "all versions"
    return f"{lo or 'up'} to {hi}" if hi else f"{lo} and later"


def _page(record: dict) -> str:
    """The license's plain-English page on counselmode.com, which links on to its sources."""
    return f"{SITE}/licenses/{quote(record['id'], safe='')}"


def _project_page(p: dict) -> str:
    return f"{SITE}/licenses/projects/{p['id']}"


def _model_id(m: dict) -> str:
    return f"model:{m['vendor']}:{m['model']}"


def create_server() -> FastMCP:
    ll = lookup()
    disclaimer = DISCLAIMER
    mcp = FastMCP("CounselMode License Navigator", instructions=INSTRUCTIONS, version=_version(), website_url=SITE)

    def done(result: dict) -> dict:
        if gaps := _verification_gaps(result):
            result["verification_gaps"] = gaps
        result["disclaimer"] = disclaimer
        return result

    @mcp.tool(annotations=READ_ONLY)
    def lookup_license(
        license: Annotated[str, Field(description='An SPDX ID ("Apache-2.0"), a name, or an alias ("ALv2", "GPLv3").')],
    ) -> dict:
        """What a software, model or data license allows and requires: OSI and FSF status, patent grant, copyleft scope,
        obligations, facts, CounselMode's editorial view and provenance. A partial name returns `candidates`, a short list
        of IDs: ask the user which one they mean, then look that one up."""
        out = ll.lookup(license)
        if not out["results"]:
            raise ToolError(
                f"{license!r} is not in the database. Classify it against the license text itself. {NOT_ADVICE}"
            )
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def model_license(
        model: Annotated[
            str, Field(description='The exact model and version, e.g. "Gemma 4", "Llama 3.1", "DeepSeek-R1".')
        ],
    ) -> dict:
        """The license an AI model is released under, keyed by exact model and version (licenses differ between versions
        of the same family). Returns the matching model records with their conditions and provenance."""
        hits = ll.model(model)
        if not hits:
            raise ToolError(
                f"{model!r} is not mapped. Read the license shipped with the exact checkpoint. {NOT_ADVICE}"
            )
        out = {"query": model, "results": hits}
        if others := ll.other_versions(hits):
            out["other_versions"] = others
            out["other_versions_note"] = "Other versions of this model family are under different terms; say so."
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def project_license(
        project: Annotated[
            str, Field(description='The software project, e.g. "Redis", "Terraform", "Linux kernel", "Next.js".')
        ],
        version: Annotated[
            str | None,
            Field(description='The version in use, e.g. "7.4" or "1.5.7". Omit to get every license era.'),
        ] = None,
    ) -> dict:
        """The license a well-known software project is released under, keyed by version: projects change licenses
        (Redis, Elasticsearch, Terraform), so the answer depends on the release. Returns each matching project's license
        eras with the LICENSE file each was checked against; with a version, only the era covering it, with CounselMode's
        rating for internal use, SaaS and distribution (each with its `because`)."""
        hits = ll.project(project, version)
        if not hits:
            raise ToolError(
                f"{project!r} is not mapped. Read the LICENSE file in the exact release you use. {NOT_ADVICE}"
            )
        out = {"query": project, "results": hits}
        if version:
            out["rating_basis"] = RATING_BASIS
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def check_compatibility(
        inbound: Annotated[str, Field(description="The license of the code or component you want to use.")],
        outbound: Annotated[str, Field(description="The license of your project, or 'proprietary'.")],
    ) -> dict:
        """Whether code under `inbound` can go into a work under `outbound`, for a distributed combined work and for
        SaaS. `yes` means notice-only conditions, `yes_narrows` that the combined work takes the stricter license,
        `conditional` that substantive terms carry over."""
        out = ll.compat(inbound, outbound)
        if "error" in out:
            raise ToolError(out["error"] + ". Ask the user for the exact license.")
        if not out["tuples"]:
            out["note"] = "No ruling for this pair in the dataset: analyze the two license texts directly."
        else:
            out["rulings_basis"] = RULINGS_BASIS
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def license_obligations(
        license: Annotated[str, Field(description="An SPDX ID, name or alias.")],
        scenario: Annotated[Scenario, Field(description="How the software is used.")],
    ) -> dict:
        """What a license requires for one use (internal, SaaS, distribution or a device), with CounselMode's rating:
        LOW, MEDIUM, HIGH, BLOCK or REVIEW (depends on facts the data cannot know), and `because`, the reason. The
        rating is a rule-based first pass, not a legal conclusion: attribute it."""
        out = ll.obligations(license, scenario)
        if "error" in out:
            raise ToolError(out["error"] + ". Ask the user for the exact license.")
        out["rating_basis"] = RATING_BASIS
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def triage_dependencies(
        components: Annotated[
            str,
            Field(
                description="One license or SPDX expression per line, or CSV/TSV text with a license column "
                f"(and optionally name or component). At most {MAX_COMPONENTS} rows."
            ),
        ],
        scenario: Annotated[Scenario, Field(description="How the product is used.")] = "distribute",
    ) -> dict:
        """A first pass over a dependency list: each component's license resolved and rated for the scenario (SPDX
        expressions: OR takes the least risky choice, AND the most). `gate` is "fail" if anything is HIGH, BLOCK or
        UNKNOWN. A first pass only, not a compliance review."""
        rows = ll.parse_components(components.splitlines())
        if not rows:
            raise ToolError("No components given.")
        if len(rows) > MAX_COMPONENTS:
            raise ToolError(f"{len(rows)} rows: send at most {MAX_COMPONENTS} per call.")
        result = ll.triage(rows, scenario)
        counts = Counter(r["rating"]["level"] for r in result)
        failed = any(ll.ORDER.index(r["rating"]["level"]) >= ll.ORDER.index("HIGH") for r in result)
        out = {
            "scenario": scenario,
            "rows": result,
            "summary": {k: counts[k] for k in ll.ORDER if counts[k]},
            "gate": "fail" if failed else "pass",
            "rating_basis": RATING_BASIS,
        }
        if failed:
            out["next_step"] = HANDOFF
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def choose_license(
        goal: Annotated[
            Literal[
                "max_adoption",
                "adoption_with_patents",
                "library_open_apps_free",
                "all_derivatives_open",
                "stop_cloud_resale",
                "dual_licensing",
                "public_domain",
                "open_model_weights",
                "open_dataset",
            ],
            Field(description="What the user wants from their license. Ask them; do not infer it."),
        ],
        must_be_open_source: Annotated[
            bool, Field(description="False only if the user accepts source-available or use-restricted licenses.")
        ] = True,
        includes: Annotated[
            list[str] | None,
            Field(description="Licenses of code the project includes or combines with (SPDX IDs or names)."),
        ] = None,
    ) -> dict:
        """Which license to release your own software, model weights or dataset under, for a stated goal. Each
        recommendation is checked against the licenses of code you include; one that cannot take that code is
        excluded with the reason. CounselMode's editorial view, not legal advice."""
        out = ll.choose(goal, must_be_open_source, includes)
        if "error" in out:
            raise ToolError(out["error"] + ". Ask the user for the exact license.")
        out["basis"] = CHOOSE_BASIS
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def search(query: Annotated[str, Field(description="Words to search license and model records for.")]) -> dict:
        """Search license and AI model records. Returns ids to pass to `fetch`."""
        return {"results": _search(ll, query)}

    @mcp.tool(annotations=READ_ONLY)
    def fetch(id: Annotated[str, Field(description="An id returned by `search`.")]) -> dict:
        """The full text of one license or model record, with its source URL and verification status."""
        return _fetch(ll, id, disclaimer)

    @mcp.resource("licenses://skill", mime_type="text/markdown")
    def skill() -> str:
        """The method: how to resolve, scope and answer a license question (SKILL.md)."""
        return (skill_dir() / "SKILL.md").read_text(encoding="utf-8")

    @mcp.resource("licenses://coverage", mime_type="application/json")
    def coverage() -> str:
        """How much of the dataset is verified against primary sources, and what is not."""
        return json.dumps(_coverage(ll), indent=1, ensure_ascii=False)

    @mcp.resource("licenses://data/{name}", mime_type="application/json")
    def data(name: str) -> str:
        """A data file: licenses, compatibility, compat_groups, models, aliases or context (CC BY 4.0)."""
        if name not in DATA_FILES:
            raise ResourceError(f"No data file {name!r}. Available: {', '.join(DATA_FILES)}.")
        return (skill_dir() / "data" / f"{name}.json").read_text(encoding="utf-8")

    return mcp


def _search(ll, query: str, limit: int = 10) -> list[dict]:
    resolved = ll.resolve(query)
    results, seen = [], set()

    def add(id_, title, url):
        if id_ not in seen and len(results) < limit:
            seen.add(id_)
            results.append({"id": id_, "title": title, "url": url})

    for r in resolved["records"] if resolved["match"] != "candidates" else []:
        add(r["id"], r["name"], _page(r))
    for m in ll.model(query):
        add(_model_id(m), f"{m['vendor']} {m['model']}: {m['license']}", _url(m))
    for p in ll.project(query):
        add(f"project:{p['id']}", f"{p['name']}: {p['eras'][-1]['license_expression']}", _project_page(p))
    words = [w for w in re.findall(r"[a-z0-9.+-]+", query.lower()) if len(w) > 1]
    scored = []
    for r in ll.LIC:
        text = json.dumps([r["id"], r["name"], r["family"], r.get("facts"), r.get("obligations")]).lower()
        score = sum(w in text for w in words) + 2 * any(w in r["id"].lower() for w in words)
        if score:
            scored.append((-score, len(r["id"]), r))
    for _, _, r in sorted(scored, key=lambda x: (x[0], x[1])):
        add(r["id"], r["name"], _page(r))
    return results


def _fetch(ll, id_: str, disclaimer: str) -> dict:
    if id_.startswith("project:"):
        p = next((p for p in ll.PROJECTS if f"project:{p['id']}" == id_), None)
        if p is None:
            raise ToolError(f"No record {id_!r}. Use an id from `search`.")
        eras = "\n".join(
            f"- {_era_range(e)}: {e['license_expression']} ({e['verification_status']}; {e['source']})"
            for e in p["eras"]
        )
        return {
            "id": id_,
            "title": p["name"],
            "text": f"{p['name']} (steward: {p['steward']})\n\nLicense by version:\n{eras}\n\n"
            f"Editorial view: {p['editorial_view']}\n\n{disclaimer}",
            "url": _project_page(p),
            "metadata": {
                "category": p["category"],
                "current_license": p["eras"][-1]["license_expression"],
                "repo": p["repo"],
            },
        }
    if id_.startswith("model:"):
        m = next((m for m in ll.MODELS if _model_id(m) == id_), None)
        if m is None:
            raise ToolError(f"No record {id_!r}. Use an id from `search`.")
        text = "\n".join(f"- {k}: {v}" for k, v in m.items() if v not in (None, ""))
        return {
            "id": id_,
            "title": f"{m['vendor']} {m['model']}",
            "text": f"{text}\n\n{disclaimer}",
            "url": _url(m),
            "metadata": {
                "license_id": m["license_id"],
                "verification_status": m.get("verification_status"),
                "last_verified": m.get("last_verified"),
            },
        }
    record = next((r for r in ll.LIC if r["id"] == id_), None)
    if record is None:
        raise ToolError(f"No record {id_!r}. Use an id from `search`.")
    p = record.get("provenance") or {}
    return {
        "id": record["id"],
        "title": record["name"],
        "text": references().render_record(record) + f"\n\n{disclaimer}",
        "url": _page(record),
        "metadata": {
            "source": _url(record),
            "family": record["family"],
            "verification_status": p.get("verification_status"),
            "last_verified": p.get("last_verified"),
            "volatile": p.get("volatile"),
        },
    }


def main() -> None:
    if "--version" in sys.argv[1:]:
        print(_version())
        return
    create_server().run(show_banner=False)


if __name__ == "__main__":
    main()
