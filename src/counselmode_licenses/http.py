"""The hosted License Navigator: the same server over stateless streamable HTTP, with no sign-in.

`create_app()` returns a FastAPI app for Vercel's FastAPI preset, which routes every path to the function and serves
no files (the default preset would serve the source and data as static downloads). Install with the `hosted` extra.

Two rules keep a serverless host cheap and predictable:
- Stateless: every POST is a complete JSON-RPC exchange; nothing is held between requests.
- `GET /mcp` is answered with 405 before anything else runs. A stateless server has no server-initiated stream to
  offer, and an idle SSE stream would hold a function open until the platform timeout, then the client reconnects.
"""

from __future__ import annotations

import json

from starlette.types import ASGIApp, Receive, Scope, Send

from counselmode_licenses.server import SITE, _version, create_server

MCP_PATH = "/mcp"
_NO_STREAM = json.dumps(
    {
        "jsonrpc": "2.0",
        "error": {"code": -32000, "message": "Method Not Allowed: this server is stateless. Send JSON-RPC over POST."},
        "id": None,
    }
).encode()


class RejectListeningStream:
    """ASGI middleware: answer GET and HEAD on the MCP endpoint with 405 instead of opening an idle stream."""

    def __init__(self, app: ASGIApp, path: str = MCP_PATH) -> None:
        self.app = app
        self.paths = {path, path.rstrip("/") + "/"}

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http" and scope["method"] in ("GET", "HEAD") and scope["path"] in self.paths:
            headers = [
                (b"content-type", b"application/json"),
                (b"allow", b"POST"),
                (b"content-length", str(len(_NO_STREAM)).encode()),
            ]
            await send({"type": "http.response.start", "status": 405, "headers": headers})
            await send({"type": "http.response.body", "body": b"" if scope["method"] == "HEAD" else _NO_STREAM})
            return
        await self.app(scope, receive, send)


def create_app():
    from fastapi import FastAPI

    mcp_app = create_server().http_app(path=MCP_PATH, stateless_http=True, json_response=True)
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None, lifespan=mcp_app.lifespan)

    @app.get("/")
    def about() -> dict:
        return {
            "name": "CounselMode License Navigator",
            "version": _version(),
            "mcp": MCP_PATH,
            "about": "Software, model and data license answers for AI assistants. No sign-in. Not legal advice.",
            "site": SITE,
        }

    app.mount("/", mcp_app)
    app.add_middleware(RejectListeningStream, path=MCP_PATH)
    return app
