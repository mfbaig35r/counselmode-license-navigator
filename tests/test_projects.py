"""Tests for data/projects.json (software projects keyed by version) and the project lookup."""

import importlib.util
import itertools
import re
from datetime import date
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "oss-license-advisor" / "scripts" / "license_lookup.py"
spec = importlib.util.spec_from_file_location("license_lookup", SCRIPT)
ll = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ll)

IDS = {r["id"] for r in ll.LIC}
BY_ID = {p["id"]: p for p in ll.PROJECTS}
CATEGORIES = {
    "operating-system",
    "language-runtime",
    "compiler",
    "c-library",
    "framework",
    "database",
    "search",
    "infrastructure",
    "observability",
    "storage",
    "dev-tool",
    "media",
    "crypto",
    "ml-framework",
    "application",
}
# A LICENSE file on a branch can change under us; a verified era must point at a tag or commit.
BRANCH = re.compile(r"/(blob|raw|tree)/(main|master|trunk|develop)/|githubusercontent\.com/[^/]+/[^/]+/(main|master)/")


def test_there_are_projects():
    assert len(ll.PROJECTS) >= 60


def test_ids_are_unique_slugs():
    assert len(BY_ID) == len(ll.PROJECTS)
    assert all(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", i) for i in BY_ID)


@pytest.mark.parametrize("p", ll.PROJECTS, ids=lambda p: p["id"])
def test_project_record_is_well_formed(p):
    assert p["category"] in CATEGORIES
    assert p["name"] and p["steward"] and p["editorial_view"]
    # The steward is a name shown as a heading; detail belongs in notes.
    assert len(p["steward"]) <= 45 and not any(c in p["steward"] for c in ";:"), p["steward"]
    assert p["repo"] is None or p["repo"].startswith("https://")  # None: proprietary, no public source
    assert p.get("edition_of") in (None, *BY_ID)
    for f in p.get("forks", []):
        assert f["id"] in BY_ID, f
    for text in (p["editorial_view"], p.get("notes") or ""):
        assert "—" not in text


@pytest.mark.parametrize("p", ll.PROJECTS, ids=lambda p: p["id"])
def test_eras_are_ordered_and_only_the_last_is_open(p):
    eras = p["eras"]
    assert eras
    assert eras[-1]["versions"]["to"] is None
    for prev, nxt in itertools.pairwise(eras):
        hi, lo = ll._version(prev["versions"]["to"]), ll._version(nxt["versions"]["from"])
        assert hi and lo and hi < lo, (prev["versions"], nxt["versions"])
        assert nxt.get("change", {}).get("announcement") or nxt.get("change", {}).get("commit"), nxt
        assert nxt["since"] and (prev["since"] is None or prev["since"] < nxt["since"])
    for e in eras:
        if e["since"]:
            date.fromisoformat(e["since"])


@pytest.mark.parametrize("p", ll.PROJECTS, ids=lambda p: p["id"])
def test_every_expression_uses_known_ids(p):
    for e in p["eras"]:
        tokens = [t for t in re.findall(r"[^\s()]+", e["license_expression"]) if t not in ll.OPS]
        assert tokens and set(tokens) <= IDS, (e["license_expression"], set(tokens) - IDS)


@pytest.mark.parametrize("p", ll.PROJECTS, ids=lambda p: p["id"])
def test_verified_eras_cite_a_pinned_license_file(p):
    for e in p["eras"]:
        assert e["verification_status"] in ("Verified (primary)", "Not re-verified"), e
        if e["verification_status"] == "Verified (primary)":
            assert e["source"].startswith("https://") and not BRANCH.search(e["source"]), e["source"]
            assert e["last_verified"], e
        else:
            assert e["last_verified"] is None, e


def family(p):
    return p.get("edition_of") or p["id"]


def test_aliases_are_unambiguous_across_projects_and_models():
    """A name may be shared only by editions of one project ("VS Code" is both the MIT source and Microsoft's build),
    so a lookup returns all of them rather than one silently."""
    seen = {}
    for p in ll.PROJECTS:
        for a in {ll.norm(x) for x in [p["name"], p["id"], *p.get("aliases", [])]}:
            assert a not in seen or seen[a] == family(p), f"{a!r} names both {seen[a]} and {p['id']}"
            seen[a] = family(p)
    model_names = {ll.norm(a) for m in ll.MODELS for a in m.get("aliases") or [m["model"]]}
    assert not set(seen) & model_names


@pytest.mark.parametrize(
    "query,version,expected",
    [
        ("Redis", "7.2.4", "BSD-3-Clause"),
        ("Redis 7.4", None, "LicenseRef-RSALv2 OR SSPL-1.0"),
        ("redis", "8.0.2", "LicenseRef-RSALv2 OR SSPL-1.0 OR AGPL-3.0-only"),
        ("Terraform", "1.5.7", "MPL-2.0"),
        ("Terraform 1.6", None, "BUSL-1.1"),
    ],
)
def test_a_version_selects_the_era_that_covers_it(query, version, expected):
    hits = ll.project(query, version)
    assert len(hits) == 1, [h["id"] for h in hits]
    assert [e["license_expression"] for e in hits[0]["eras"]] == [expected]
    assert set(hits[0]["eras"][0]["risk"]) == {"internal", "saas", "distribute"}


def test_without_a_version_every_era_is_returned_and_unknown_names_find_nothing():
    (redis,) = ll.project("Redis")
    assert len(redis["eras"]) == 3 and "risk" not in redis["eras"][0]
    assert ll.project("no-such-project-xyz") == []


@pytest.mark.parametrize(
    "expr,family",
    [
        ("MIT OR Apache-2.0", "permissive"),
        ("LicenseRef-RSALv2 OR SSPL-1.0 OR AGPL-3.0-only", "network_copyleft"),
        ("(AGPL-3.0-only OR SSPL-1.0 OR Elastic-2.0) AND Elastic-2.0", "source_available"),
        ("Apache-2.0 AND GPL-2.0-only WITH Linux-syscall-note", "strong_copyleft"),
        ("not-a-license-9", "unknown"),
    ],
)
def test_expression_family_takes_the_most_open_choice_and_the_most_restrictive_part(expr, family):
    assert ll.expression_family(expr) == family
