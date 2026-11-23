"""Tests for oss-license-advisor/scripts/license_lookup.py and the data it reads.

Run from the repository root:  uv run --with pytest pytest tests
"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

SKILL = Path(__file__).resolve().parents[1] / "oss-license-advisor"
SCRIPT = SKILL / "scripts" / "license_lookup.py"
spec = importlib.util.spec_from_file_location("license_lookup", SCRIPT)
ll = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ll)

IDS = {r["id"] for r in ll.LIC}


def cli(*args, cwd=None):
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, cwd=cwd)


# Resolution: exact first, never a silent guess.


@pytest.mark.parametrize("record", ll.LIC, ids=lambda r: r["id"])
def test_every_id_resolves_exactly_to_itself(record):
    assert ll.unique(record["id"]) is record
    assert ll.unique(record["id"].lower()) is record


@pytest.mark.parametrize("alias,target", sorted(ll.ALIASES.items()))
def test_every_alias_resolves_to_its_target(alias, target):
    assert target in IDS, f"alias {alias!r} points at {target!r}, which has no record"
    assert ll.unique(alias)["id"] == target


@pytest.mark.parametrize(
    "deprecated,current",
    [("GPL-3.0", "GPL-3.0-only"), ("GPL-3.0+", "GPL-3.0-or-later"), ("GPL-2.0", "GPL-2.0-only"),
     ("LGPL-2.1", "LGPL-2.1-only"), ("LGPL-3.0+", "LGPL-3.0-or-later"), ("AGPL-3.0", "AGPL-3.0-only")],
)
def test_deprecated_spdx_ids_mean_the_only_or_or_later_form(deprecated, current):
    assert ll.unique(deprecated)["id"] == current


def test_a_partial_name_returns_candidates_not_a_guess():
    res = ll.resolve("GPL")
    assert res["match"] == "candidates"
    assert {"GPL-3.0-only", "LGPL-3.0-only", "AGPL-3.0-only"} <= {r["id"] for r in res["records"]}
    assert ll.unique("GPL") is None
    assert "give the exact SPDX ID" in ll.lookup("GPL")["note"]


def test_unknown_resolves_to_nothing():
    assert ll.resolve("definitely-not-a-license")["match"] == "none"
    assert ll.resolve("   ")["match"] == "none"


# Obligations: the record asked about, and the risk for the scenario.


def test_gpl_3_0_obligations_are_the_gpls_not_the_lgpls():
    """Regression: v2.3 resolved "GPL-3.0" to LGPL-3.0-only by substring match."""
    out = ll.obligations("GPL-3.0", "saas")
    assert out["id"] == "GPL-3.0-only"
    assert out["risk"] == "LOW"  # the GPL triggers on distribution; SaaS alone does not
    assert ll.obligations("GPL-3.0", "distribute")["risk"] == "HIGH"


def test_agpl_is_high_for_saas():
    assert ll.obligations("AGPL-3.0-only", "saas")["risk"] == "HIGH"


def test_obligations_refuse_an_ambiguous_or_unknown_license():
    assert "ambiguous" in ll.obligations("GPL", "saas")["error"]
    assert "not in the database" in ll.obligations("nope-1.0", "saas")["error"]
    assert "scenario" in ll.obligations("MIT", "cloud")["error"]


def _old_family_risk(r, sc):
    """The v2.3 rule, kept to prove the explicit table changed no rating."""
    risk = {"public_domain": "LOW", "permissive": "LOW", "content_documentation_font_adjacent_data_licenses": "REVIEW",
            "weak_copyleft": "MEDIUM", "strong_copyleft": "HIGH", "network_copyleft": "HIGH",
            "source_available": "HIGH", "noncommercial_restricted_purpose": "BLOCK", "ethical_source": "HIGH",
            "ai_model_licenses": "REVIEW", "hardware": "REVIEW",
            "proprietary_commercial_free_but_not_for_business_unlicensed": "REVIEW"}
    f = r["family"]
    base = next((v for k, v in risk.items() if f.startswith(k.split("_")[0])), "REVIEW")
    trig = set(r.get("triggers", []))
    if sc == "internal":
        return "BLOCK" if "commercial_use" in trig else (
            "REVIEW" if base in ("REVIEW", "HIGH") and f.startswith(("ai", "ethical", "propriet")) else "LOW")
    if not (trig & ll.SCENARIOS[sc]) and base in ("MEDIUM", "HIGH"):
        return "LOW"
    if sc == "device" and "installation_info" in r.get("obligations", []):
        return "HIGH"
    return base


@pytest.mark.parametrize("scenario", list(ll.SCENARIOS))
def test_risk_table_matches_the_v2_3_rule_for_every_license(scenario):
    assert {r["id"]: ll.family_risk(r, scenario) for r in ll.LIC} == {
        r["id"]: _old_family_risk(r, scenario) for r in ll.LIC}


def test_every_family_has_an_explicit_risk():
    assert {r["family"] for r in ll.LIC} <= set(ll.FAMILY_RISK)


# Compatibility: matched on license IDs through compat_groups.json.


def test_every_compat_label_is_mapped_to_real_licenses():
    labels = {t["inbound"] for t in ll.COMP} | {t["outbound"] for t in ll.COMP}
    assert labels <= set(ll.GROUPS)
    for label, members in ll.GROUPS.items():
        assert members and members <= IDS, label


def test_compat_with_spdx_ids_finds_only_the_right_groups():
    """Regression: v2.3 found nothing for "GPL-3.0-only" and matched LGPL/AGPL groups for "GPL-3.0"."""
    out = ll.compat("MIT", "GPL-3.0-only")
    assert out["tuples"]
    assert {t["outbound"] for t in out["tuples"]} == {"GPL-3.0"}
    assert all("MIT" in ll.GROUPS[t["inbound"]] for t in out["tuples"])


def test_every_compat_tuple_is_reachable_by_license_ids():
    for t in ll.COMP:
        i, o = sorted(ll.GROUPS[t["inbound"]])[0], sorted(ll.GROUPS[t["outbound"]])[0]
        assert t in ll.compat(i, o)["tuples"], (t["inbound"], t["outbound"])


def test_compat_says_which_name_is_ambiguous_or_unknown():
    assert "ambiguous" in ll.compat("GPL", "MIT")["error"]
    assert "unknown" in ll.compat("MIT", "nope-9")["error"]


# Models.


def test_model_lookup_is_by_exact_model():
    gemma4 = ll.model("Gemma 4")
    assert gemma4 and all("4" in m["model"] for m in gemma4)
    for m in ll.MODELS:
        assert m["license_id"] in IDS or m["license_id"].startswith(("LicenseRef-", "Note-")), m["model"]
    assert ll.model("") == []


# Triage: SPDX expressions with the right precedence.


@pytest.mark.parametrize(
    "expr,scenario,risk",
    [
        ("MIT", "distribute", "LOW"),
        ("MIT OR GPL-3.0-only", "distribute", "LOW"),
        ("MIT AND GPL-3.0-only", "distribute", "HIGH"),
        # AND binds tighter than OR; v2.3 took the least risky part of any expression containing OR.
        ("GPL-3.0-only AND (MIT OR Apache-2.0)", "distribute", "HIGH"),
        ("(GPL-3.0-only AND MIT) OR Apache-2.0", "distribute", "LOW"),
        ("GPL-2.0-only WITH Classpath-exception-2.0", "distribute", "HIGH"),
        ("AGPL-3.0-only", "saas", "HIGH"),
        ("not-a-license", "distribute", "UNKNOWN"),
        ("MIT AND not-a-license", "distribute", "UNKNOWN"),
    ],
)
def test_expression_risk(expr, scenario, risk):
    assert ll.expression_risk(expr, scenario)[1] == risk


def test_a_lowercase_or_is_part_of_a_name_not_an_operator():
    assert ll._TOKEN.findall("BSD or MIT") == ["BSD", "or", "MIT"]
    assert ll.expression_risk("Apache License 2.0", "distribute")[0] == "Apache-2.0"


def test_triage_csv_and_exit_code(tmp_path):
    sbom = tmp_path / "sbom.csv"
    sbom.write_text("name,license\nleft-pad,MIT\nreadline,GPL-3.0-only\n")
    done = cli("triage", str(sbom), "--scenario", "distribute")
    assert done.returncode == 2
    assert "readline\tGPL-3.0-only\tGPL-3.0-only\tHIGH" in done.stdout
    ok = tmp_path / "ok.txt"
    ok.write_text("MIT\nApache-2.0\n")
    assert cli("triage", str(ok)).returncode == 0


# The command line and the data as shipped.


@pytest.mark.parametrize(
    "args,code",
    [(["lookup", "ALv2"], 0), (["lookup", "nope-9"], 1), (["model", "Gemma", "4"], 0),
     (["compat", "MIT", "GPL-3.0-only"], 0), (["obligations", "AGPL-3.0-only", "--scenario", "saas"], 0),
     (["obligations", "GPL", "--scenario", "saas"], 1)],
)
def test_cli_commands_end_with_the_disclaimer(args, code):
    done = cli(*args)
    assert done.returncode == code
    assert "[Disclaimer] Not legal advice." in done.stdout


def test_cli_works_from_any_directory(tmp_path):
    assert cli("lookup", "MIT", cwd=tmp_path).returncode == 0


def test_every_record_carries_provenance():
    for r in ll.LIC:
        p = r["provenance"]
        assert p.get("verification_status") and "last_verified" in p and "volatile" in p, r["id"]


def test_no_firm_attribution_anywhere():
    for path in SKILL.rglob("*"):
        if path.suffix in (".md", ".json", ".py"):
            text = path.read_text(encoding="utf-8").lower()
            for word in ("eversheds", "sutherland", "harvey", "firm view", "firm_view"):
                assert word not in text, f"{word!r} in {path.relative_to(SKILL)}"


def test_data_files_are_valid_json():
    for path in (SKILL / "data").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
