"""The hosted app (http.py): the GET guard, the about page, no files served, and a full MCP exchange over HTTP."""

import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from counselmode_licenses.http import create_app

INIT = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}},
}
HEADERS = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json"}


@pytest.fixture(scope="module")
def http():
    with TestClient(create_app()) as client:
        yield client


def test_get_and_head_on_the_endpoint_are_405(http):
    assert http.get("/mcp").status_code == 405
    assert http.head("/mcp").status_code == 405
    assert http.get("/mcp").headers["allow"] == "POST"


def test_about_page(http):
    body = http.get("/").json()
    assert body["mcp"] == "/mcp" and "Not legal advice" in body["about"]


@pytest.mark.parametrize("host", ["licenses.counselmode.com", "counselmode-licenses.vercel.app"])
def test_initialize_works_on_any_host(http, host):
    assert http.post("/mcp", json=INIT, headers={**HEADERS, "Host": host}).status_code == 200


@pytest.mark.parametrize(
    "path",
    [
        "/pyproject.toml",
        "/src/counselmode_licenses/server.py",
        "/oss-license-advisor/data/licenses.json",
        "/uv.lock",
        "/.env",
    ],
)
def test_no_file_is_served(http, path):
    assert http.get(path).status_code == 404


def test_a_tool_call_over_http(http):
    """A stateless server answers a tools/call POST on its own, as remote clients send it."""
    call = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": "lookup_license", "arguments": {"license": "MIT"}},
    }
    http.post("/mcp", json=INIT, headers=HEADERS)
    response = http.post("/mcp", json=call, headers=HEADERS)
    assert response.status_code == 200
    result = response.json()["result"]
    assert not result.get("isError")
    assert result["structuredContent"]["results"][0]["id"] == "MIT"
