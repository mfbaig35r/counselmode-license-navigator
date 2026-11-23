"""Assemble exactly what the hosted deployment ships into one folder, so it can be tested as-is and deployed from.

    uv run python deploy/stage.py [--out .deploy]

Contents: api/index.py and vercel.json (from deploy/), the package wheel (built now, with the skill and data inside),
a pyproject.toml that installs only that wheel with the `hosted` extra, its uv.lock (Vercel installs from uv.lock),
and the Vercel project link if deploy/vercel-project.json exists.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEPLOY = REPO / "deploy"


def stage(out: Path) -> Path:
    if out.exists():
        shutil.rmtree(out)
    (out / "api").mkdir(parents=True)
    (out / "wheels").mkdir()
    dist = out / "_dist"
    subprocess.run(["uv", "build", "--wheel", "--out-dir", str(dist), str(REPO)], check=True, capture_output=True)
    wheel = next(dist.glob("counselmode_licenses-*.whl"))
    shutil.move(str(wheel), out / "wheels" / wheel.name)
    shutil.rmtree(dist)
    shutil.copy(DEPLOY / "api_index.py", out / "api" / "index.py")
    shutil.copy(DEPLOY / "vercel.json", out / "vercel.json")
    (out / "pyproject.toml").write_text(
        "[project]\n"
        'name = "counselmode-licenses-deploy"\n'
        'version = "0"\n'
        'requires-python = ">=3.12"\n'
        'dependencies = ["counselmode-licenses[hosted]"]\n\n'
        "[tool.uv]\npackage = false\n\n"
        f'[tool.uv.sources]\ncounselmode-licenses = {{ path = "wheels/{wheel.name}" }}\n',
        encoding="utf-8",
    )
    subprocess.run(["uv", "lock", "--project", str(out)], check=True, capture_output=True)
    link = DEPLOY / "vercel-project.json"
    if link.exists():
        (out / ".vercel").mkdir()
        shutil.copy(link, out / ".vercel" / "project.json")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default=str(REPO / ".deploy"))
    out = stage(Path(ap.parse_args().out))
    print(f"staged {out}: " + ", ".join(sorted(p.name for p in out.iterdir())))


if __name__ == "__main__":
    main()
