# CounselMode License Navigator

Free, open-source answers to software, model and data license questions, inside the AI assistant you already use.

- **What a license allows and requires**: 156 records (144 licenses in 12 families, from permissive and copyleft to
  source-available, noncommercial, ethical-source, AI model, content and data, hardware and proprietary, plus 12
  exceptions), keyed by SPDX ID.
- **Whether two licenses combine**: 220 compatibility rulings, for distributed works and for SaaS, 177 of them
  checked against primary sources.
- **What your use triggers**: obligations and a risk level for internal use, SaaS, distribution and devices.
- **Which license an AI model is under**: 58 records keyed by exact model and version (Gemma 4 is Apache-2.0; Gemma 1
  to 3 are not).
- **Which license a software project is under**: 99 well-known projects keyed by version, each checked against the
  project's LICENSE file at a release tag (Redis 7.2 is BSD-3-Clause; 7.4 is RSALv2 or SSPL; 8 adds AGPL-3.0).
- **Which license to choose for your own project**, for a stated goal, checked against the licenses of code you
  include.
- **A first pass over a dependency list**: one license or SPDX expression per line, or a CSV with a license column.

Every answer carries its source, when it was last verified, and whether it is volatile. **This is not legal advice.**
For a full compliance screening with a report, see [CounselMode](https://counselmode.com).

## Use it

**Hosted, nothing to install.** Add this MCP server URL, with no authentication, as a custom connector in Claude.ai,
ChatGPT or Grok:

```
https://licenses.counselmode.com/mcp
```

**As a local MCP server** (Python 3.11+), for Claude Code, Claude Desktop, Cursor and any other MCP client:

```
claude mcp add licenses -- uvx counselmode-licenses        # Claude Code
uvx counselmode-licenses                                   # any client: run it as a stdio server
```

Tools: `lookup_license`, `model_license`, `project_license`, `check_compatibility`, `license_obligations`,
`choose_license`, `triage_dependencies`, and `search` and `fetch` (for ChatGPT's deep research). The method is the
resource `licenses://skill`; the data files are `licenses://data/<name>`.

**As an agent skill.** Copy `oss-license-advisor/` into your assistant's skills folder (for Claude Code,
`~/.claude/skills/`). The assistant reads `SKILL.md` and uses the data and script as needed.

**From the command line** (Python 3.9+, standard library only):

```
python oss-license-advisor/scripts/license_lookup.py lookup ALv2
python oss-license-advisor/scripts/license_lookup.py model "Gemma 4"
python oss-license-advisor/scripts/license_lookup.py compat MIT GPL-3.0-only
python oss-license-advisor/scripts/license_lookup.py obligations AGPL-3.0-only --scenario saas
python oss-license-advisor/scripts/license_lookup.py choose all_derivatives_open --includes Apache-2.0,MIT
python oss-license-advisor/scripts/license_lookup.py triage sbom.csv --scenario distribute
```

`triage` exits with 2 if anything is HIGH, BLOCK or UNKNOWN, so it can gate a build.

## How much to trust it

Each record says how it was checked (`provenance.verification_status`). Today 34 of the 156 records, including the
most-asked licenses, are fully verified against primary sources and 13 partially. Every record's obligations were
checked against its license text; the other fields of the remaining records are not yet re-verified. The answers show
this. Confirm anything that matters against the license text and, for decisions with real consequences, with a lawyer.

**Found a wrong answer?** Open an issue with the license or model, what the tool said, and a link to the primary source
(the license text, the vendor's own page, or a court record).

## Layout

| Path | What |
|---|---|
| `oss-license-advisor/SKILL.md` | The method an assistant follows |
| `oss-license-advisor/data/` | The data, and the only place it is edited; see `docs/schema.md` |
| `oss-license-advisor/references/` | Readable views per license family, plus case law, regulation and choosing a license (generated from the data) |
| `oss-license-advisor/scripts/` | `license_lookup.py` (lookup, model, compatibility, obligations, choose, triage) and `build_references.py` |
| `src/counselmode_licenses/` | The MCP server (`server.py`) and its hosted HTTP app (`http.py`) |
| `deploy/` | Hosting on Vercel: staging, entry point, and a smoke test that also checks no file is served |
| `tests/` | `uv run pytest` |

## License

Code: [Apache-2.0](LICENSE). Data and references: [CC BY 4.0](DATA-LICENSE). See [NOTICE](NOTICE) for third-party
material, including the SPDX License List.
