#!/usr/bin/env python3
"""Monthly re-check: has any project's license changed since we verified it?

For each project's current license era, compares the LICENSE file at the tag we checked against the same file at the
project's HEAD today, ignoring copyright lines (years change every January). Also checks whether the SPDX License List
has moved past our snapshot. Prints a markdown report; `--out FILE` writes it too and sets `changed=N` for GitHub
Actions. A changed file is a prompt to re-verify, not proof the license changed. Standard library only.
"""

from __future__ import annotations

import difflib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "oss-license-advisor" / "data"
GITHUB_BLOB = re.compile(r"https://github\.com/([^/]+)/([^/]+)/blob/(.+)$")
RAW = "https://raw.githubusercontent.com"
LICENSE_FILES = [
    "LICENSE",
    "LICENSE.txt",
    "LICENSE.md",
    "COPYING",
    "LICENSES/README.md",
    "LICENSE-APACHE",
    "LICENSE-MIT",
]
SIMILAR = 0.97  # below this, the file changed enough to read again


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": "counselmode-license-recheck"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def normalize(text: str) -> str:
    lines = [line for line in text.splitlines() if "copyright" not in line.lower()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip().lower()


def split_ref(owner: str, repo: str, rest: str) -> tuple[str, str]:
    """Split "<ref>/<path>" where the ref may itself contain slashes ("release/15.1.0"): ask git which candidate is a
    real tag or branch, longest first. A commit hash is never ambiguous."""
    parts = rest.split("/")
    if re.fullmatch(r"[0-9a-f]{40}", parts[0]):
        return parts[0], "/".join(parts[1:])
    for i in range(len(parts) - 1, 0, -1):
        ref = "/".join(parts[:i])
        found = subprocess.run(
            [
                "git",
                "ls-remote",
                "--tags",
                "--heads",
                f"https://github.com/{owner}/{repo}",
                f"refs/tags/{ref}",
                f"refs/heads/{ref}",
            ],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        ).stdout.strip()
        if found:
            return ref, "/".join(parts[i:])
    return parts[0], "/".join(parts[1:])


def check_project(p: dict) -> dict:
    era = p["eras"][-1]
    m = GITHUB_BLOB.match(era.get("source") or "")
    if not m:
        return {"id": p["id"], "status": "skipped", "why": "source is not a GitHub file"}
    owner, repo, rest = m.groups()
    pinned = fetch(f"https://raw.githubusercontent.com/{owner}/{repo}/{rest}")
    if pinned is None:
        return {"id": p["id"], "status": "error", "why": "the verified file no longer loads at its tag"}
    ref, path = split_ref(owner, repo, rest)
    head = fetch(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{path}")
    if head is None:
        for alt in LICENSE_FILES:
            if alt != path and (text := fetch(f"{RAW}/{owner}/{repo}/HEAD/{alt}")):
                ratio = difflib.SequenceMatcher(None, normalize(pinned), normalize(text)).ratio()
                if ratio >= SIMILAR:  # renamed, same text: worth knowing, not worth an alert
                    return {"id": p["id"], "status": "renamed", "why": f"{path} is now {alt} at HEAD, same text"}
                return {"id": p["id"], "status": "changed", "why": f"{path} is gone at HEAD; {alt} differs"}
        return {"id": p["id"], "status": "changed", "why": f"{path} is gone at HEAD"}
    # A source file under REUSE (Qt) declares its license in an SPDX line; compare that, not the code around it.
    declared = re.compile(r"SPDX-License-Identifier:\s*(.+)")
    if (was := declared.search(pinned)) and not path.upper().startswith(("LICENSE", "COPYING", "LICENSES/")):
        now = declared.search(head)
        if not now or now.group(1).strip() != was.group(1).strip():
            return {"id": p["id"], "status": "changed", "why": f"the SPDX line in {path} changed at HEAD"}
        return {"id": p["id"], "status": "same"}
    ratio = difflib.SequenceMatcher(None, normalize(pinned), normalize(head)).ratio()
    if ratio < SIMILAR:
        return {
            "id": p["id"],
            "status": "changed",
            "why": f"{path} at HEAD differs from {ref} (similarity {ratio:.2f})",
        }
    return {"id": p["id"], "status": "same"}


def check_spdx() -> str | None:
    snapshot = next(DATA.glob("spdx_snapshot_*.json")).stem.removeprefix("spdx_snapshot_")
    latest = json.loads(fetch("https://spdx.org/licenses/licenses.json") or "{}").get("licenseListVersion")
    if latest and latest != snapshot:
        return f"The SPDX License List is at {latest}; our snapshot is {snapshot}."
    return None


def main(argv: list[str]) -> int:
    projects = json.loads((DATA / "projects.json").read_text())
    names = {p["id"]: p["name"] for p in projects}
    results = []
    for p in projects:
        try:
            results.append(check_project(p))
        except (OSError, ValueError) as e:  # network or decode errors: one bad host should not stop the run
            results.append({"id": p["id"], "status": "error", "why": str(e)[:120]})
    spdx = check_spdx()
    changed = [r for r in results if r["status"] == "changed"]
    errors = [r for r in results if r["status"] == "error"]
    skipped = [r for r in results if r["status"] == "skipped"]
    renamed = [r for r in results if r["status"] == "renamed"]

    lines = [
        "## License re-check",
        "",
        (
            f"{len(projects)} projects: {len(changed)} changed, {len(errors)} could not be checked, "
            f"{len(skipped)} skipped (no GitHub LICENSE file), "
            f"{len(renamed)} renamed, {len(projects) - len(changed) - len(errors) - len(skipped) - len(renamed)} unchanged."
        ),
        "",
    ]
    if spdx:
        lines += [f"**SPDX:** {spdx}", ""]
    if changed:
        lines += ["**Changed since verified** (re-read the license and update `data/projects.json`):", ""]
        lines += [f"- {names[r['id']]} (`{r['id']}`): {r['why']}" for r in changed] + [""]
    if renamed:
        lines += ["**Renamed, same text** (update the source path at the next release):", ""]
        lines += [f"- {names[r['id']]} (`{r['id']}`): {r['why']}" for r in renamed] + [""]
    if errors:
        lines += ["**Could not be checked:**", ""]
        lines += [f"- {names[r['id']]} (`{r['id']}`): {r['why']}" for r in errors] + [""]
    report = "\n".join(lines)
    print(report)
    if "--out" in argv:
        Path(argv[argv.index("--out") + 1]).write_text(report)
        if out := os.environ.get("GITHUB_OUTPUT"):
            with open(out, "a") as f:
                f.write(f"changed={len(changed) + len(errors) + (1 if spdx else 0)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
