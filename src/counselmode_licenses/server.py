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

from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError, ToolError
from mcp.types import ToolAnnotations
from pydantic import Field

from counselmode_licenses.skill import lookup, references, skill_dir

READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
MAX_COMPONENTS = 500
SITE = "https://counselmode.com"
HANDOFF = f"For a full compliance screening of these dependencies, with a report, see {SITE}."
DATA_FILES = ("licenses", "compatibility", "compat_groups", "models", "aliases", "context")
Scenario = Literal["internal", "saas", "distribute", "device"]

INSTRUCTIONS = """\
License answers for software, AI models and data, from a curated dataset keyed by SPDX ID. Not legal advice.

- Resolve the exact license first. If lookup_license returns candidates, ask the user which one; never pick.
- For AI models, use model_license with the exact model and version; never infer a license from the vendor.
- Ask which scenario applies (internal use, SaaS, distribution, a device) before stating obligations or risk.
- Every record has provenance: say how it was verified and when, and say so plainly when it is not re-verified or
  volatile. Recommend confirming anything that matters against the license text, and a lawyer for real decisions.
- Editorial views are CounselMode's judgment; label them as such.
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


def _model_id(m: dict) -> str:
    return f"model:{m['vendor']}:{m['model']}"


def create_server() -> FastMCP:
    ll = lookup()
    disclaimer = ll.DISCLAIMER.strip()
    mcp = FastMCP("CounselMode License Navigator", instructions=INSTRUCTIONS, version=_version(), website_url=SITE)

    def done(result: dict) -> dict:
        result["disclaimer"] = disclaimer
        return result

    @mcp.tool(annotations=READ_ONLY)
    def lookup_license(
        license: Annotated[str, Field(description='An SPDX ID ("Apache-2.0"), a name, or an alias ("ALv2", "GPLv3").')],
    ) -> dict:
        """What a software, model or data license allows and requires: OSI and FSF status, patent grant, copyleft scope,
        obligations, facts, CounselMode's editorial view and provenance. A partial name returns `candidates`: ask the
        user which one they mean."""
        out = ll.lookup(license)
        if not out["results"]:
            raise ToolError(f"{license!r} is not in the database. Classify it against the license text itself.")
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
            raise ToolError(f"{model!r} is not mapped. Read the license shipped with the exact checkpoint.")
        return done({"query": model, "results": hits})

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
        return done(out)

    @mcp.tool(annotations=READ_ONLY)
    def license_obligations(
        license: Annotated[str, Field(description="An SPDX ID, name or alias.")],
        scenario: Annotated[Scenario, Field(description="How the software is used.")],
    ) -> dict:
        """What a license requires for one use (internal, SaaS, distribution or a device), with a risk level: LOW,
        MEDIUM, HIGH, BLOCK or REVIEW (depends on facts the data cannot know)."""
        out = ll.obligations(license, scenario)
        if "error" in out:
            raise ToolError(out["error"] + ". Ask the user for the exact license.")
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
        counts = Counter(r["risk"] for r in result)
        failed = any(ll.ORDER.index(r["risk"]) >= ll.ORDER.index("HIGH") for r in result)
        out = {
            "scenario": scenario,
            "rows": result,
            "summary": {k: counts[k] for k in ll.ORDER if counts[k]},
            "gate": "fail" if failed else "pass",
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
        add(r["id"], r["name"], _url(r))
    for m in ll.model(query):
        add(_model_id(m), f"{m['vendor']} {m['model']}: {m['license']}", _url(m))
    words = [w for w in re.findall(r"[a-z0-9.+-]+", query.lower()) if len(w) > 1]
    scored = []
    for r in ll.LIC:
        text = json.dumps([r["id"], r["name"], r["family"], r.get("facts"), r.get("obligations")]).lower()
        score = sum(w in text for w in words) + 2 * any(w in r["id"].lower() for w in words)
        if score:
            scored.append((-score, len(r["id"]), r))
    for _, _, r in sorted(scored, key=lambda x: (x[0], x[1])):
        add(r["id"], r["name"], _url(r))
    return results


def _fetch(ll, id_: str, disclaimer: str) -> dict:
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
        "url": _url(record),
        "metadata": {
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
