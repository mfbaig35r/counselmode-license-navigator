"""Locate the bundled skill and load its lookup module: the single copy of the data and logic.

Installed, the skill sits inside the package (`counselmode_licenses/skill`, put there by the wheel build). In a source
checkout it is `oss-license-advisor/` at the repository root.
"""

from __future__ import annotations

import importlib.util
from functools import cache
from pathlib import Path
from types import ModuleType


@cache
def skill_dir() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in (here / "skill", here.parents[1] / "oss-license-advisor"):
        if (candidate / "SKILL.md").is_file():
            return candidate
    raise RuntimeError("The license data is missing: reinstall counselmode-licenses.")


def _load(name: str, filename: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(f"counselmode_licenses.{name}", skill_dir() / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def lookup() -> ModuleType:
    """scripts/license_lookup.py: resolution, compatibility, obligations, risk, triage."""
    return _load("license_lookup", "license_lookup.py")


@cache
def references() -> ModuleType:
    """scripts/build_references.py: renders a record as readable text."""
    return _load("build_references", "build_references.py")
