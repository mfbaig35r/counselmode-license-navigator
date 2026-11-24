"""Tests for oss-license-advisor/scripts/license_lookup.py and the data it reads.

Run from the repository root:  uv run --with pytest pytest tests
"""

import importlib.util
import json
import re
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
    return subprocess.run([sys.executable, str(SCRIPT), *args], check=False, capture_output=True, text=True, cwd=cwd)


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
    [
        ("GPL-3.0", "GPL-3.0-only"),
        ("GPL-3.0+", "GPL-3.0-or-later"),
        ("GPL-2.0", "GPL-2.0-only"),
        ("LGPL-2.1", "LGPL-2.1-only"),
        ("LGPL-3.0+", "LGPL-3.0-or-later"),
        ("AGPL-3.0", "AGPL-3.0-only"),
    ],
)
def test_deprecated_spdx_ids_mean_the_only_or_or_later_form(deprecated, current):
    assert ll.unique(deprecated)["id"] == current


def test_a_partial_name_returns_candidates_not_a_guess():
    res = ll.resolve("GPL")
    assert res["match"] == "candidates"
    assert {"GPL-3.0-only", "LGPL-3.0-only", "AGPL-3.0-only"} <= {r["id"] for r in res["records"]}
    assert ll.unique("GPL") is None
    assert "exact SPDX ID" in ll.lookup("GPL")["note"]


def test_unknown_resolves_to_nothing():
    assert ll.resolve("definitely-not-a-license")["match"] == "none"
    assert ll.resolve("   ")["match"] == "none"


# Obligations: the record asked about, and the risk for the scenario.


def test_gpl_3_0_obligations_are_the_gpls_not_the_lgpls():
    """Regression: v2.3 resolved "GPL-3.0" to LGPL-3.0-only by substring match."""
    out = ll.obligations("GPL-3.0", "saas")
    assert out["id"] == "GPL-3.0-only"
    assert out["rating"]["level"] == "LOW"  # the GPL triggers on distribution; SaaS alone does not
    assert ll.obligations("GPL-3.0", "distribute")["rating"]["level"] == "HIGH"


def test_agpl_is_high_for_saas():
    assert ll.obligations("AGPL-3.0-only", "saas")["rating"]["level"] == "HIGH"


def test_obligations_refuse_an_ambiguous_or_unknown_license():
    assert "ambiguous" in ll.obligations("GPL", "saas")["error"]
    assert "not in the database" in ll.obligations("nope-1.0", "saas")["error"]
    assert "scenario" in ll.obligations("MIT", "cloud")["error"]


def _old_family_risk(r, sc):
    """The v2.3 rule, kept to prove the explicit table changed no rating."""
    risk = {
        "public_domain": "LOW",
        "permissive": "LOW",
        "content_documentation_font_adjacent_data_licenses": "REVIEW",
        "weak_copyleft": "MEDIUM",
        "strong_copyleft": "HIGH",
        "network_copyleft": "HIGH",
        "source_available": "HIGH",
        "noncommercial_restricted_purpose": "BLOCK",
        "ethical_source": "HIGH",
        "ai_model_licenses": "REVIEW",
        "hardware": "REVIEW",
        "proprietary_commercial_free_but_not_for_business_unlicensed": "REVIEW",
    }
    f = r["family"]
    base = next((v for k, v in risk.items() if f.startswith(k.split("_")[0])), "REVIEW")
    trig = set(r.get("triggers", []))
    if sc == "internal":
        return (
            "BLOCK"
            if "commercial_use" in trig
            else ("REVIEW" if base in ("REVIEW", "HIGH") and f.startswith(("ai", "ethical", "propriet")) else "LOW")
        )
    if not (trig & ll.SCENARIOS[sc]) and base in ("MEDIUM", "HIGH"):
        return "LOW"
    if sc == "device" and "installation_info" in r.get("obligations", []):
        return "HIGH"
    return base


@pytest.mark.parametrize("scenario", ["saas", "distribute", "device"])
def test_risk_table_matches_the_v2_3_rule_for_every_license(scenario):
    assert {r["id"]: ll.family_risk(r, scenario) for r in ll.LIC} == {
        r["id"]: _old_family_risk(r, scenario) for r in ll.LIC
    }


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
        i, o = min(ll.GROUPS[t["inbound"]]), min(ll.GROUPS[t["outbound"]])
        assert t in ll.compat(i, o)["tuples"], (t["inbound"], t["outbound"])


def test_every_compat_tuple_says_whether_it_was_verified():
    for t in ll.COMP:
        assert t["verification_status"] in ("Verified (primary)", "Not re-verified"), t
        if t["verification_status"] == "Verified (primary)":
            assert t["source"].startswith("https://") and t["last_verified"], t
        else:
            assert t["last_verified"] is None, t


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
    [
        (["lookup", "ALv2"], 0),
        (["lookup", "nope-9"], 1),
        (["model", "Gemma", "4"], 0),
        (["compat", "MIT", "GPL-3.0-only"], 0),
        (["obligations", "AGPL-3.0-only", "--scenario", "saas"], 0),
        (["obligations", "GPL", "--scenario", "saas"], 1),
    ],
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


def test_reference_docs_are_generated_from_the_data():
    """The per-family docs, case law, regulatory overlay and model map are built from data/: never hand-edited."""
    done = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "build_references.py"), "--check"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert done.returncode == 0, done.stdout


def test_verification_statuses_use_the_known_values():
    known = (
        "Verified (primary)",
        "Partially verified (primary)",
        "Secondary only",
        "Not re-verified",
        "Note only",
        "Not on SPDX exceptions list",
    )
    for r in ll.LIC:
        assert r["provenance"]["verification_status"].startswith(known), (
            r["id"],
            r["provenance"]["verification_status"],
        )


@pytest.mark.parametrize(
    "license_id,risk",
    [
        ("MIT", "LOW"),
        ("GPL-3.0-only", "LOW"),
        ("PolyForm-Noncommercial-1.0.0", "BLOCK"),
        ("CC-BY-NC-4.0", "BLOCK"),
        ("LicenseRef-MS-RSL", "BLOCK"),  # reference_only
        ("LicenseRef-MRL", "BLOCK"),  # research only
        ("PolyForm-Small-Business-1.0.0", "REVIEW"),  # depends on the user's size
        ("LicenseRef-Llama-4", "REVIEW"),
        ("LicenseRef-Commons-Clause", "LOW"),  # restricts selling, not internal use
        ("LicenseRef-Moonshot-Modified-MIT", "REVIEW"),  # name display above a threshold
        ("BUSL-1.1", "REVIEW"),  # no_production_use: production use only through the Additional Use Grant
        ("LicenseRef-Oracle-OTN", "REVIEW"),  # no_production_use: development use is free
        ("LicenseRef-MNPL", "BLOCK"),  # non-production and noncommercial
        ("RPL-1.5", "HIGH"),  # duties attach to internal "Deploy"
        ("AGPL-3.0-only", "LOW"),  # network copyleft, but internal use alone triggers nothing
    ],
)
def test_internal_use_is_blocked_by_a_use_restriction_not_a_commercial_trigger(license_id, risk):
    assert ll.family_risk(ll.unique(license_id), "internal") == risk


def test_obligations_and_triggers_use_only_the_vocabulary():
    for r in ll.LIC:
        assert set(r.get("obligations") or []) <= ll.OBLIGATIONS, (r["id"], set(r["obligations"]) - ll.OBLIGATIONS)
        assert set(r.get("triggers") or []) <= ll.TRIGGERS, (r["id"], set(r["triggers"]) - ll.TRIGGERS)


def test_the_schema_doc_defines_every_vocabulary_value():
    doc = (SKILL.parent / "docs" / "schema.md").read_text(encoding="utf-8")
    for value in ll.OBLIGATIONS | ll.TRIGGERS:
        assert f"`{value}`" in doc, value


@pytest.mark.parametrize(
    "license_id,value",
    [
        ("CC-BY-ND-4.0", "no_derivatives"),
        ("CC-BY-NC-ND-4.0", "no_derivatives"),
        ("LicenseRef-MS-RSL", "reference_only"),
        ("BUSL-1.1", "no_production_use"),
    ],
)
def test_restrictions_are_recorded(license_id, value):
    assert value in ll.unique(license_id)["obligations"]


@pytest.mark.parametrize(
    "query,expected",
    [
        ("Gemma 4", {"Apache-2.0"}),  # not the Gemma 1-3 record, whose note mentions Gemma 4
        ("Gemma 3 27B", {"LicenseRef-Gemma"}),
        ("Llama 3.1", {"LicenseRef-Llama-3.x"}),
        ("Llama 3.1 8B Instruct", {"LicenseRef-Llama-3.x"}),
        ("llama-3.1-70b", {"LicenseRef-Llama-3.x"}),
        ("DeepSeek-V3.1", {"MIT"}),  # not the original V3 checkpoint's license
        ("DeepSeek-V3", {"LicenseRef-DeepSeek", "MIT"}),  # both: the license depends on the checkpoint
        ("Mistral Large 2", {"LicenseRef-MRL"}),
    ],
)
def test_model_matching_respects_versions(query, expected):
    assert {m["license_id"] for m in ll.model(query)} == expected


def test_a_different_version_is_not_matched():
    assert ll.model("Mistral Large 2.1") == []
    assert ll.model("Llama 5") == []


def test_every_model_record_has_aliases():
    for m in ll.MODELS:
        assert m.get("aliases"), m["model"]


def test_aliases_are_unique_within_and_across_model_records():
    owner = {}
    for i, m in enumerate(ll.MODELS):
        normed = [ll.norm(a) for a in m["aliases"]]
        assert len(normed) == len(set(normed)), ("duplicate alias in", m["model"])
        for a in normed:
            assert owner.setdefault(a, i) == i, (a, "is on two records")


def test_every_goal_names_real_licenses():
    for g in ll.GOALS.values():
        for c in g["candidates"] + g.get("not_open_source", []):
            assert c["id"] in IDS, (g["goal"], c["id"])


def test_choose_offers_source_available_only_when_open_source_is_not_required():
    open_only = {r["id"] for r in ll.choose("stop_cloud_resale")["recommendations"]}
    assert open_only == {"AGPL-3.0-or-later"}
    allowed = ll.choose("stop_cloud_resale", must_be_open_source=False)["recommendations"]
    assert {r["id"] for r in allowed if r["not_open_source"]} == {"SSPL-1.0", "Elastic-2.0", "BUSL-1.1", "FSL-1.1-ALv2"}


@pytest.mark.parametrize(
    "goal,includes,kept,dropped",
    [
        ("all_derivatives_open", ["Apache-2.0", "MIT"], {"GPL-3.0-or-later"}, set()),
        ("all_derivatives_open", ["GPL-2.0-only"], set(), {"GPL-3.0-or-later"}),  # GPLv2-only cannot go into GPLv3
        ("max_adoption", ["GPL-2.0-only"], set(), {"MIT", "Apache-2.0"}),
        ("library_open_apps_free", ["MIT"], {"MPL-2.0", "LGPL-3.0-or-later"}, set()),
    ],
)
def test_choose_excludes_licenses_that_cannot_take_included_code(goal, includes, kept, dropped):
    out = ll.choose(goal, includes=includes)
    assert {r["id"] for r in out["recommendations"]} == kept
    assert {e["id"] for e in out["excluded"]} == dropped


def test_choose_rejects_unknown_goals_and_unclear_licenses():
    assert "goal must be one of" in ll.choose("world_domination")["error"]
    assert "ambiguous" in ll.choose("max_adoption", includes=["GPL"])["error"]
    assert "not in the database" in ll.choose("max_adoption", includes=["nope-9"])["error"]


def test_cli_choose():
    done = cli("choose", "all_derivatives_open", "--includes", "Apache-2.0,MIT")
    assert done.returncode == 0 and "GPL-3.0-or-later" in done.stdout and "[Disclaimer]" in done.stdout


DESCRIBED = [("facts", k) for k in ("allows", "conditions", "copyleft_detail", "saas")] + [
    ("editorial_view", k) for k in ("build_on", "license_your_own")
]


@pytest.mark.parametrize("record", ll.LIC, ids=lambda r: r["id"])
def test_descriptions_stand_alone_and_use_the_risk_scale(record):
    """Each record is shown on its own (a license page, one MCP answer): no "As BSD-2" pointers, and risk words only
    from the tool's own scale."""
    for part, key in DESCRIBED:
        text = (record.get(part) or {}).get(key) or ""
        assert not re.search(r"^\s*(As |Same as|See )|\bAs above\b", text), (record["id"], key, text)
        assert not re.search(r"\b(VERY HIGH|Very low risk|Moderate-high|Low-moderate|Moderate)\b", text), (
            record["id"],
            key,
            text,
        )


@pytest.mark.parametrize("record", ll.LIC, ids=lambda r: r["id"])
def test_spdx_source_links_name_the_record_or_an_exception_it_explains(record):
    """Regression: AGPL-3.0 records cited the SPDX page for AGPL-1.0-only."""
    exceptions = {r["id"] for r in ll.LIC if r.get("record_type") == "exception"}
    for cited in re.findall(r"spdx\.org/licenses/([A-Za-z0-9.+-]+)\.html", record["provenance"].get("source") or ""):
        assert cited in ({record["id"], "exceptions-index"} | exceptions), (record["id"], cited)
