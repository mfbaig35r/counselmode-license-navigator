"""Smoke-test a running License Navigator over HTTP: the endpoint, the tools, and that no file is reachable.

uv run python deploy/smoke.py https://licenses.counselmode.com
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

HEADERS = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json"}
INIT = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "smoke", "version": "0"}},
}
FILES = [
    "/pyproject.toml",
    "/uv.lock",
    "/api/index.py",
    "/vercel.json",
    "/.vercel/project.json",
    "/counselmode_licenses/server.py",
    "/counselmode_licenses/skill/data/licenses.json",
    "/oss-license-advisor/data/licenses.json",
    "/wheels/",
]
TOOLS = {
    "choose_license",
    "lookup_license",
    "model_license",
    "check_compatibility",
    "license_obligations",
    "triage_dependencies",
    "search",
    "fetch",
}


def request(method: str, url: str, body: dict | None = None) -> tuple[int, bytes]:
    """(status, body) without raising on HTTP errors and without following redirects."""

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None

    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS if body is not None else {})
    try:
        with urllib.request.build_opener(NoRedirect).open(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def rpc(base: str, method: str, params: dict, id_: int) -> dict:
    status, body = request("POST", f"{base}/mcp", {"jsonrpc": "2.0", "id": id_, "method": method, "params": params})
    if status != 200:
        raise SystemExit(f"{method}: HTTP {status}")
    return json.loads(body)["result"]


def smoke(base: str) -> list[str]:
    base = base.rstrip("/")
    failures = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        print(f"{'PASS' if ok else 'FAIL'}  {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    status, body = request("GET", f"{base}/")
    check("about page", status == 200 and json.loads(body or b"{}").get("mcp") == "/mcp", str(status))
    check("GET /mcp is 405", request("GET", f"{base}/mcp")[0] == 405)
    check("initialize", request("POST", f"{base}/mcp", INIT)[0] == 200)
    names = {t["name"] for t in rpc(base, "tools/list", {}, 2)["tools"]}
    check("tools/list", names == TOOLS, str(sorted(names ^ TOOLS)) if names != TOOLS else "")
    args = {"license": "GPL-3.0", "scenario": "saas"}
    sc = rpc(base, "tools/call", {"name": "license_obligations", "arguments": args}, 3).get("structuredContent") or {}
    check("obligations GPL-3.0 saas", sc.get("id") == "GPL-3.0-only" and sc.get("risk") == "LOW", str(sc.get("id")))
    r = rpc(base, "tools/call", {"name": "model_license", "arguments": {"model": "Gemma 4"}}, 4)
    ids = {m["license_id"] for m in (r.get("structuredContent") or {}).get("results", [])}
    check("model Gemma 4", ids == {"Apache-2.0"}, str(ids))
    exposed = [f for f in FILES if request("GET", f"{base}{f}")[0] != 404]
    check("no file reachable", not exposed, ", ".join(exposed))
    return failures


if __name__ == "__main__":
    sys.exit(1 if smoke(sys.argv[1]) else 0)
