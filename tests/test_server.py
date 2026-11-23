"""The MCP server, exercised through FastMCP's in-memory client (the real protocol path)."""

import asyncio
import json

import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from counselmode_licenses.server import MAX_COMPONENTS, create_server

SERVER = create_server()


def call(tool, **args):
    async def run():
        async with Client(SERVER) as c:
            return (await c.call_tool(tool, args)).structured_content

    return asyncio.run(run())


def read(uri):
    async def run():
        async with Client(SERVER) as c:
            return (await c.read_resource(uri))[0].text

    return asyncio.run(run())


def test_tools_are_the_expected_read_only_set():
    async def run():
        async with Client(SERVER) as c:
            return await c.list_tools()

    tools = {t.name: t for t in asyncio.run(run())}
    assert set(tools) == {
        "choose_license",
        "lookup_license",
        "model_license",
        "check_compatibility",
        "license_obligations",
        "triage_dependencies",
        "search",
        "fetch",
    }
    for t in tools.values():
        assert t.annotations.read_only_hint and not t.annotations.destructive_hint, t.name
        assert t.description and len(t.description) > 40, t.name


def test_lookup_by_alias_carries_provenance_and_disclaimer():
    out = call("lookup_license", license="ALv2")
    assert out["match"] == "alias" and out["results"][0]["id"] == "Apache-2.0"
    assert out["results"][0]["provenance"]["verification_status"]
    assert out["disclaimer"].startswith("[Caveat]") and "Not legal advice." in out["disclaimer"]


def test_a_partial_name_returns_candidates():
    out = call("lookup_license", license="GPL")
    assert out["match"] == "candidates" and "give the exact SPDX ID" in out["note"]


def test_unknown_license_is_an_error_not_an_empty_answer():
    with pytest.raises(ToolError, match="not in the database"):
        call("lookup_license", license="definitely-not-a-license-9")


def test_model_license_by_exact_version():
    out = call("model_license", model="Gemma 4")
    assert out["results"] and all(m["license_id"] == "Apache-2.0" for m in out["results"])
    with pytest.raises(ToolError, match="not mapped"):
        call("model_license", model="no-such-model-xyz")


def test_compatibility_on_license_ids():
    out = call("check_compatibility", inbound="MIT", outbound="GPL-3.0-only")
    assert out["tuples"] and {t["outbound"] for t in out["tuples"]} == {"GPL-3.0"}
    with pytest.raises(ToolError, match="ambiguous"):
        call("check_compatibility", inbound="GPL", outbound="MIT")


def test_obligations_by_scenario():
    assert call("license_obligations", license="GPL-3.0", scenario="saas")["id"] == "GPL-3.0-only"
    assert call("license_obligations", license="GPL-3.0", scenario="saas")["risk"] == "LOW"
    assert call("license_obligations", license="AGPL-3.0-only", scenario="saas")["risk"] == "HIGH"
    with pytest.raises(ToolError):
        call("license_obligations", license="MIT", scenario="cloud")


def test_triage_gates_and_hands_off():
    out = call("triage_dependencies", components="name,license\nleft-pad,MIT\nreadline,GPL-3.0-only\n")
    assert out["gate"] == "fail" and out["summary"] == {"LOW": 1, "HIGH": 1}
    assert "counselmode.com" in out["next_step"]
    ok = call("triage_dependencies", components="MIT\nApache-2.0\n", scenario="saas")
    assert ok["gate"] == "pass" and "next_step" not in ok


def test_triage_rejects_empty_and_oversized_input():
    with pytest.raises(ToolError, match="No components"):
        call("triage_dependencies", components="\n\n")
    with pytest.raises(ToolError, match=f"at most {MAX_COMPONENTS}"):
        call("triage_dependencies", components="MIT\n" * (MAX_COMPONENTS + 1))


def test_search_then_fetch_for_chatgpt():
    hits = call("search", query="GPLv3")["results"]
    assert hits[0]["id"] == "GPL-3.0-only" and hits[0]["url"].startswith("http")
    doc = call("fetch", id=hits[0]["id"])
    assert doc["title"] and "Not legal advice." in doc["text"] and doc["url"].startswith("http")
    assert doc["metadata"]["verification_status"]
    models = [h for h in call("search", query="Gemma")["results"] if h["id"].startswith("model:")]
    assert models
    assert "license_id" in call("fetch", id=models[0]["id"])["metadata"]
    with pytest.raises(ToolError, match="Use an id from"):
        call("fetch", id="nope")


def test_resources_serve_the_method_and_the_data():
    assert "OSS License Advisor" in read("licenses://skill")
    assert len(json.loads(read("licenses://data/licenses"))["licenses"]) >= 139
    with pytest.raises(Exception, match="No data file"):
        read("licenses://data/secrets")


def test_choose_license_checks_included_code():
    plain = call("choose_license", goal="max_adoption")
    assert [r["id"] for r in plain["recommendations"]] == ["MIT", "Apache-2.0"]
    assert plain["attribution"] == "CounselMode editorial view; not legal advice" and plain["disclaimer"]
    blocked = call("choose_license", goal="max_adoption", includes=["GPL-2.0-only"])
    assert blocked["recommendations"] == [] and {e["id"] for e in blocked["excluded"]} == {"MIT", "Apache-2.0"}
    assert "check_compatibility" in blocked["note"]
    with pytest.raises(ToolError, match="ambiguous"):
        call("choose_license", goal="max_adoption", includes=["GPL"])
