"""Every answer says what kind of claim each part is: facts with their verification, ratings with their reason,
CounselMode's view labelled as such. Enforced here rather than left to the prompt."""

import asyncio
import json

import pytest
from fastmcp import Client

from counselmode_licenses.server import create_server

SERVER = create_server()

CALLS = [
    ("lookup_license", {"license": "AGPL-3.0-only"}),
    ("lookup_license", {"license": "GPL"}),
    ("lookup_license", {"license": "LicenseRef-Llama-3.x"}),
    ("license_obligations", {"license": "AGPL-3.0-only", "scenario": "saas"}),
    ("license_obligations", {"license": "MIT", "scenario": "distribute"}),
    ("project_license", {"project": "Redis", "version": "7.4.1"}),
    ("project_license", {"project": "Cal.com"}),
    ("model_license", {"model": "Gemma 4"}),
    ("check_compatibility", {"inbound": "SSPL-1.0", "outbound": "MIT"}),
    ("check_compatibility", {"inbound": "LicenseRef-Llama-3.x", "outbound": "MIT"}),
    (
        "triage_dependencies",
        {"components": "MIT\nGPL-3.0-only\nSSPL-1.0\nMIT OR Apache-2.0\nFooBar-1.0", "scenario": "saas"},
    ),
    ("choose_license", {"goal": "library_open_apps_free", "includes": ["MIT"]}),
    ("fetch", {"id": "Apache-2.0"}),
]


def call(tool, args):
    async def run():
        async with Client(SERVER) as c:
            return (await c.call_tool(tool, args)).structured_content

    return asyncio.run(run())


ANSWERS = {f"{tool}:{json.dumps(args)}": (tool, call(tool, args)) for tool, args in CALLS}


def nodes(value, path="$"):
    """Every dict in an answer, with its path."""
    if isinstance(value, dict):
        yield path, value
        for k, v in value.items():
            yield from nodes(v, f"{path}.{k}")
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from nodes(v, f"{path}[{i}]")


@pytest.mark.parametrize("key", ANSWERS)
def test_no_bare_risk_or_unlabelled_view(key):
    _, answer = ANSWERS[key]
    for path, node in nodes(answer):
        assert "risk" not in node, f"bare risk at {path}"
        assert "editorial_view" not in node, f"unlabelled editorial view at {path}"
        if "counselmode_view" in node:
            assert node["counselmode_view"]["label"].startswith("CounselMode's view"), path


@pytest.mark.parametrize("key", ANSWERS)
def test_every_rating_gives_its_reason_and_the_answer_says_what_ratings_are(key):
    _, answer = ANSWERS[key]
    ratings = [(p, n) for p, n in nodes(answer) if "level" in n]
    for path, node in ratings:
        assert node.get("because"), f"rating without a reason at {path}"
    if ratings:
        assert "CounselMode's rule" in answer.get("rating_basis", ""), key


def test_rulings_and_recommendations_say_whose_judgment_they_are():
    compat = ANSWERS['check_compatibility:{"inbound": "SSPL-1.0", "outbound": "MIT"}'][1]
    assert "CounselMode's reading" in compat["rulings_basis"]
    choose = ANSWERS['choose_license:{"goal": "library_open_apps_free", "includes": ["MIT"]}'][1]
    assert "editorial view" in choose["basis"]


def test_answers_that_rest_on_unverified_records_flag_them():
    """The Llama compatibility rulings and the Cal.com v6.4 era are not re-verified; Apache-2.0 is partially."""
    llama = ANSWERS['check_compatibility:{"inbound": "LicenseRef-Llama-3.x", "outbound": "MIT"}'][1]
    assert llama["verification_gaps"] and all({"what", "status"} <= set(g) for g in llama["verification_gaps"])
    calcom = ANSWERS['project_license:{"project": "Cal.com"}'][1]
    assert any("LicenseRef-Proprietary" in g["what"] for g in calcom["verification_gaps"])
    redis = ANSWERS['project_license:{"project": "Redis", "version": "7.4.1"}'][1]
    assert "verification_gaps" not in redis  # the 7.4 era is verified


def test_coverage_resource_counts_every_part_of_the_dataset():
    async def run():
        async with Client(SERVER) as c:
            return json.loads((await c.read_resource("licenses://coverage"))[0].text)

    cov = asyncio.run(run())
    for part in ("licenses", "compatibility_rulings", "project_license_eras", "models"):
        assert cov[part]["total"] == sum(cov[part]["by_status"].values()) > 0, part
    assert cov["licenses"]["total"] == 156 and cov["compatibility_rulings"]["total"] == 220
