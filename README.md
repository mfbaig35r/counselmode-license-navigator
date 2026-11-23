# CounselMode License Navigator

Free, open-source answers to software, model and data license questions, inside the AI assistant you already use.

- **What a license allows and requires**: 129 licenses in 12 families (permissive, copyleft, network copyleft,
  source-available, noncommercial, ethical-source, AI model, content and data, hardware, proprietary) and 10 exceptions,
  keyed by SPDX ID.
- **Whether two licenses combine**: 187 compatibility rulings, for distributed works and for SaaS.
- **What your use triggers**: obligations and a risk level for internal use, SaaS, distribution and devices.
- **Which license an AI model is under**: 27 records keyed by exact model and version (Gemma 4 is Apache-2.0; Gemma 1
  to 3 are not).
- **A first pass over a dependency list**: one license or SPDX expression per line, or a CSV with a license column.

Every answer carries its source, when it was last verified, and whether it is volatile. **This is not legal advice.**
For a full compliance screening with a report, see [CounselMode](https://counselmode.com).

## Use it

**As an agent skill.** Copy `oss-license-advisor/` into your assistant's skills folder (for Claude Code,
`~/.claude/skills/`). The assistant reads `SKILL.md` and uses the data and script as needed.

**From the command line** (Python 3, standard library only):

```
python oss-license-advisor/scripts/license_lookup.py lookup ALv2
python oss-license-advisor/scripts/license_lookup.py model "Gemma 4"
python oss-license-advisor/scripts/license_lookup.py compat MIT GPL-3.0-only
python oss-license-advisor/scripts/license_lookup.py obligations AGPL-3.0-only --scenario saas
python oss-license-advisor/scripts/license_lookup.py triage sbom.csv --scenario distribute
```

`triage` exits with 2 if anything is HIGH, BLOCK or UNKNOWN, so it can gate a build.

An MCP server, local and hosted, is in progress.

## How much to trust it

Each record says how it was checked (`provenance.verification_status`). Today 20 of 139 records are verified against
primary sources and the rest are not yet re-verified; obligations on most records were derived automatically from the
license text. The answers show this. Confirm anything that matters against the license text and, for decisions with
real consequences, with a lawyer.

## Layout

| Path | What |
|---|---|
| `oss-license-advisor/SKILL.md` | The procedure an assistant follows |
| `oss-license-advisor/data/` | The data (source of truth); see `docs/schema.md` |
| `oss-license-advisor/references/` | Human-readable write-ups per license family, plus case law, regulation, choosing a license |
| `oss-license-advisor/scripts/license_lookup.py` | Lookup, model, compatibility, obligations and triage |
| `oss-license-advisor/assets/` | A shareable workbook (a v2.3 snapshot) |
| `tests/` | `uv run --with pytest pytest tests` |

## License

Code: [Apache-2.0](LICENSE). Data, references and workbook: [CC BY 4.0](DATA-LICENSE). See [NOTICE](NOTICE).
