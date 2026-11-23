#!/usr/bin/env python3
"""Rebuild the per-family reference docs (references/<n>-<family>.md) from data/licenses.json.

  build_references.py           write the docs
  build_references.py --check   exit 1 if any doc differs from the data (run in tests)

data/ is the source of truth: never edit these docs by hand. Standard library only.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HEADER = "Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice)."


def render_record(r: dict) -> str:
    lines = [f"## {r['name']} — `{r['id']}`", ""]
    for key in ("base", "effect", "osi_status", "fsf_status", "patent_grant", "copyleft_scope", "triggers", "obligations"):
        if r.get(key) not in (None, [], ""):
            lines.append(f"- **{key}:** {r.get(key)}")
    for key, value in (r.get("facts") or {}).items():
        if value not in (None, ""):
            lines.append(f"- {key}: {value}")
    for key, value in (r.get("editorial_view") or {}).items():
        if key != "attribution":
            lines.append(f"- **Editorial view – {key}:** {value}")
    p = r.get("provenance") or {}
    lines.append(
        f"- provenance: {p.get('source')} | verification: {p.get('verification_status')} | "
        f"last_verified: {p.get('last_verified')} | volatile: {p.get('volatile')}"
    )
    return "\n".join(lines)


def build() -> dict[str, str]:
    with open(os.path.join(ROOT, "data", "licenses.json"), encoding="utf-8") as f:
        records = json.load(f)["licenses"]
    tabs: OrderedDict[str, list] = OrderedDict()
    for r in records:
        tabs.setdefault(r["family_tab"], []).append(r)
    docs = {}
    for tab, recs in tabs.items():
        body = "\n\n".join(render_record(r) for r in recs)
        slug = re.sub(r"[^a-z0-9]+", "-", tab.lower()).strip("-")
        docs[os.path.join(ROOT, "references", f"{slug}.md")] = f"# {tab}\n\n{HEADER}\n\n{body}\n\n"
    with open(os.path.join(ROOT, "data", "context.json"), encoding="utf-8") as f:
        context = json.load(f)
    with open(os.path.join(ROOT, "data", "models.json"), encoding="utf-8") as f:
        models = json.load(f)
    for name, title, intro, rows in TABLES(context, models):
        docs[os.path.join(ROOT, "references", name)] = f"# {title}\n\n" + (f"{intro}\n\n" if intro else "") + table(rows)
    return docs


def TABLES(context: dict, models: list) -> list[tuple[str, str, str, list[dict]]]:
    return [
        ("case-law.md", "Case law", "Verify statuses on the docket before publication.", context["case_law"]),
        ("regulatory-overlay.md", "Regulatory overlay", "", context["regulatory"]),
        ("model-map.md", "AI model \u2192 license map (keyed by model version)",
         "Always read the license shipped with the exact checkpoint.", models),
    ]


def cell(value) -> str:
    return "" if value is None else str(value).replace("|", "\\|").replace("\n", " ")


def table(rows: list[dict]) -> str:
    keys = list(rows[0])
    out = ["| " + " | ".join(keys) + " |", "|" + "---|" * len(keys)]
    out += ["| " + " | ".join(cell(r.get(k)) for k in keys) + " |" for r in rows]
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    docs = build()
    if "--check" in argv:
        stale = []
        for path, text in docs.items():
            current = open(path, encoding="utf-8").read() if os.path.exists(path) else None
            if current != text:
                stale.append(os.path.relpath(path, ROOT))
        if stale:
            print("out of date (run scripts/build_references.py): " + ", ".join(stale))
        return 1 if stale else 0
    for path, text in docs.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(docs)} reference docs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
