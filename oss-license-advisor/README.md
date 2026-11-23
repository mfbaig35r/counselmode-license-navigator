# oss-license-advisor (v2.10)

Copy `oss-license-advisor/` into your agent's skills directory. For an MCP server, expose `data/*.json` as resources and wrap `scripts/license_lookup.py` commands as tools.

    python scripts/license_lookup.py lookup ALv2
    python scripts/license_lookup.py model "Gemma 4"
    python scripts/license_lookup.py compat GPL-2.0-only GPL-2.0+
    python scripts/license_lookup.py obligations AGPL-3.0-only --scenario saas
    python scripts/license_lookup.py triage sbom.csv --scenario distribute
