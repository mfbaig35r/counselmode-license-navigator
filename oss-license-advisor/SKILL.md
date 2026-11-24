---
name: oss-license-advisor
description: Classify, explain and assess software, model and data licenses (open source, source-available, noncommercial, ethical-source, hardware, proprietary, and AI/LLM model licenses) and their obligations. Use whenever a user asks what a license allows; whether a dependency, tool or model can be used internally, in SaaS, in distributed software or on devices; which license to choose; whether licenses are compatible; how GPL/AGPL/LGPL/MPL/Apache/MIT/SSPL/BUSL/FSL/Llama/Gemma/Muse/Kimi/Mistral/OpenMDW terms apply; or needs open-source/AI license diligence for M&A, audit or compliance (SBOM triage, copyleft, revenue thresholds, maintenance risk, EU AI Act/CRA overlay). Not legal advice.
---

# OSS License Advisor (v2.13.3)

Data-backed workflow for software and model licensing, for **inbound** use (building on others' code/models) and **outbound** licensing (your own releases). Version 2.13, November 23, 2026: 144 license records in 12 families plus 12 exception records (one per SPDX ID / LicenseRef, checked against SPDX License List 3.29.0), 58 version-keyed model records, 99 software projects keyed by version (each era checked against the project's LICENSE file), 220 compatibility tuples over 25 license groups (177 verified against primary sources), 190 aliases, plus case law, regulatory overlay, relicensing log and diligence checklist.

## Package contents

| Path | Use |
|---|---|
| `data/licenses.json` | One record per SPDX ID / LicenseRef: enums (`osi_status`, `fsf_status`, `patent_grant`, `copyleft_scope`, `triggers`, `obligations`), `facts`, `editorial_view`, `provenance` (`source`, `verification_status`, `last_verified`, `volatile`, `spdx_list_status`), `caveat` |
| `data/compatibility.json` | Tuples: inbound, outbound, context, `result` (yes / yes_narrows / conditional / no / not_applicable), conditions, source |
| `data/compat_groups.json` | Each compatibility label and the license IDs it covers; `compat` matches on these IDs, never on label text |
| `data/models.json` | Model version → license (Gemma 1-3 vs 4, Llama, Muse, Kimi, Mistral, NVIDIA, etc.) |
| `data/projects.json` | Software project version → license, by era (Redis 7.2 vs 7.4 vs 8, Terraform 1.5 vs 1.6), each era checked against the LICENSE file at a tag, with forks |
| `data/spdx_snapshot_3.29.0.json` | SPDX list snapshot used by the build: confirmed-listed license IDs (relevant subset), confirmed-absent IDs, full exceptions list |
| `data/aliases.json` | How people write licenses ("ALv2", "ASL 2.0", "GPLv3") → SPDX ID |
| `data/context.json` | Case law, regulatory overlay, AI model relicensing events |
| `references/*.md` | Human-readable versions per family tab plus model map, compatibility, scenarios, choosing, projects, checklist, case law, regulation, relicensing, glossary, sources |
| `data/choosing.json` | Outbound license recommendations by goal (editorial view); `choose` checks each against code you include |
| `scripts/license_lookup.py` | `lookup`, `model`, `project [--version]`, `compat`, `obligations --scenario`, `triage <SBOM> --scenario`, `choose <goal> --includes ...` |

Load only what the question needs. Prefer `data/` for lookups; use `references/` for explanation.

## Workflow

1. **Resolve the exact license.** If the user's wording matches several licenses (`lookup` returns `candidates`), ask which one; never pick. IDs are join keys: SPDX-listed IDs as published in SPDX 3.29.0; anything not on the list is a `LicenseRef-` (old IDs and ScanCode keys resolve through `aliases.json`). Custom exceptions are `AdditionRef-` (valid in SPDX 3.0 only). For a named software project, use `projects.json` and the **version in use**: licenses change between releases (Redis, Elasticsearch, Terraform); each era's SPDX expression joins to license records. Normalize via `aliases.json` to an SPDX ID or LicenseRef. Parse SPDX expressions: `WITH` (exception; see `13-Exceptions`), `OR` (choice), `AND` (cumulative). For models, resolve the **exact model and version** in `models.json`; never infer from the vendor (e.g., Gemma 4 is Apache-2.0, but Gemma 1-3 are not; Mistral has three license regimes).

**v2.3 rules:** Keys starting `Note-` are notes, not SPDX expressions; never place them in an expression. `Hippocratic-3.0-core` matches only the HL3 core text with no modules; if a project uses modules, use `LicenseRef-Hippocratic-3.0-<MODULES>` (or `LicenseRef-Hippocratic-3.0-modules` when unread) and warn the user. Surface each record's `warnings` list and each project's `expression_verification_status`. DeepSeek licenses are checkpoint-specific: original V3 (Dec. 2024) weights are `LicenseRef-DeepSeek`; R1 and V3-0324 onward are MIT. In the compatibility matrix, `yes` means notice-only conditions; `conditional` means substantive terms carry over.

2. **Check provenance and always return it.** Every answer must state `verification_status` (Verified (primary) / Secondary only / Not re-verified) and `last_verified`. If `caveat` is true, say so and recommend confirming against the official text. `volatile` is rule-based: AI model, source-available, noncommercial, ethical-source and proprietary/vendor-ToS records are always volatile. Treat maintenance status "Unknown (not verified)" as unknown, never as active.
3. **Pin down the scenario**: internal, SaaS (not distributed), distribution, device, modification, linking (static/dynamic), containers, fine-tuning/distillation, or acquisition. Run `obligations <id> --scenario`.
4. **Check combinations** with `compat` / `compatibility.json` (matched on license IDs through `compat_groups.json`); `yes_narrows` means the combined work must use the stricter license.
5. **Overlay context**: thresholds measured on the group (revenue, MAU, headcount) at closing; maintenance status (archived projects get no security fixes); EU AI Act open-source exemption limits; CRA reporting; relicensing history.
6. **Recommend actions** (process separation, dynamic linking, permissive forks such as OpenSearch/OpenTofu/Valkey, commercial license, OpenJDK builds, conda-forge, model swap) and **flag for counsel**: derivative-work scope, dynamic linking under the GPL, AGPL "interacting remotely," kernel modules, ambiguous "noncommercial," MaaS definitions, AI output/training restrictions, pending cases.

## Output rules

- Lead with the bottom line and the assumed scenario.
- Separate **facts** (with source and verification date) from **editorial view** (label it "CounselMode editorial view").
- Risk levels: LOW / MEDIUM / HIGH / BLOCK / REVIEW / UNKNOWN.
- Diligence findings: component, license ID, scenario, risk, evidence, remediation, SPA treatment (rep, special indemnity, pre-closing covenant).
- Always end with: not legal advice; jurisdiction assumed (U.S. general, EU overlay where relevant); verify volatile items.

## Rules of thumb

- No LICENSE file means all rights reserved.
- Permissive licenses still require notices; Apache-2.0 adds NOTICE and change-marking and is GPLv2-only-incompatible.
- GPL triggers on distribution; SaaS alone does not (AGPL and CAL close that gap). A Vizio pretrial order (Dec. 2025, Cal. Super. Ct.; not precedential, and SFC calls it irrelevant) read GPLv2 not to require keeping devices functional after reinstallation; GPLv3 Installation Information is a separate express duty.
- Doe v. GitHub (9th Cir. Sept. 16, 2026): AI-generated code lacking attribution is not, by itself, CMI removal under DMCA §1202(b); the training-data theory was not decided; the court expressed no view on copyright infringement, and breach-of-license (contract) claims remain pending in the district court.
- Source-available, noncommercial and ethical-source licenses are not open source.
- "Open-weight" ≠ open source; read MaaS gates (Kimi K3, Muse Spark Open), group-revenue bars (Mistral Modified MIT), MAU caps (Llama) and attribution/naming rules.
- Licensors can add restrictions to their own AGPL releases; licensees cannot strip them (Neo4j v. PureThink, non-precedential).

## Maintenance

`data/` is the source of truth from v2.4: edit it directly, run the tests (`tests/` at the repository root), refresh `last_verified`, and log changes in `CHANGELOG.md`. For full SPDX coverage, seed from the SPDX license-list JSON and ScanCode LicenseDB when available.
