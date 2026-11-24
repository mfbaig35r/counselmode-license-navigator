# Changelog

## 2.13.3 (2026-11-23)

- Case law: two disputes that never reached a court, from the parties' own records (court dockets not checked).
  **HashiCorp / OpenTofu** (April 2024): a cease-and-desist and DMCA notice over OpenTofu's `removed` block, answered
  with an analysis tracing the code to pre-fork MPL-2.0 Terraform and a DMCA counter notice; no later demand found.
  **ONLYOFFICE / Euro-Office** (March to August 2026): whether an AGPLv3 Section 7 term requiring the ONLYOFFICE logo
  to be kept may be removed as a "further restriction"; the FSF said it may, and ONLYOFFICE replaced the term with
  attribution and notice terms in May 2026.

## 2.13.2 (2026-11-23)

- `search` and `fetch` link each license and project to its plain-English page on counselmode.com
  (counselmode.com/licenses/<id>, /licenses/projects/<id>), which links on to the primary sources; a license's
  primary source is in `metadata.source`, a project's repository in `metadata.repo`. Model records keep their source.

## 2.13.1 (2026-11-23)

- **Every record stands on its own.** 32 fields in 20 records only pointed at another record ("As BSD-2", "As
  GPLv2"); each now carries the text itself, with the facts unchanged.
- **Editorial views use the tool's risk scale.** Off-scale words ("Very low risk", "Moderate", "Moderate-high",
  "VERY HIGH") are replaced by the record's own computed levels (LOW, MEDIUM, HIGH, BLOCK, REVIEW) per scenario, so a
  view never contradicts the risk the tools report; the AGPL views no longer name a company or say "force".
- AGPL-3.0 records cited the SPDX page for AGPL-1.0-only; corrected.
- Tests: descriptions stand alone and use the scale; SPDX source links name the record (or an exception it explains).

## 2.13 (2026-11-23)

- **Software projects, keyed by version** (`data/projects.json`, the `project_license` MCP tool and the `project`
  command): 99 well-known projects, from operating systems and databases to frameworks and developer tools, with the
  license each version is under. Each license era cites the project's LICENSE file at a release tag (131 of 139 eras
  verified; the rest say why, for example closed-source products with no LICENSE file), and each license change cites
  its announcement and the commit that made it. Forks link to the project they came from (Valkey from Redis 7.2.4,
  OpenTofu from Terraform, Apache Pekko from Akka). `projects.json` replaces the unverified project list in
  `context.json`; `common-projects.md` and the relicensing log are now generated from it, and the log covers 40
  software license changes.
- **14 new license records**, each checked against its own text: curl, SSH-OpenSSH, OpenSSL (the pre-3.0 license),
  Ruby, Artistic-1.0-Perl, GPL-1.0-or-later, Zend-2.0, the Swift and Qt LGPL exceptions, Elastic License 1.0, the
  Facebook BSD+Patents grant React used until 2017, FSL-1.0, the n8n Sustainable Use License and the CockroachDB
  Software License. 34 records are now fully verified and 13 partially.
- Project groupings use a new rule, `expression_family`: the most open choice in an OR, the most restrictive part of
  an AND.

## 2.12 (2026-11-23)

- **Compatibility rulings checked against primary sources** (FSF compatibility pages and GPL FAQ matrix, the license
  texts, the Mozilla MPL FAQ, SPDX). Each ruling now carries `verification_status`, `last_verified` and its primary
  source URL; 177 of 220 are verified. The rest, mostly the AI model and noncommercial groups, say so.
- **SSPL-1.0, BUSL-1.1, Elastic-2.0 and RSALv2 have their own rulings.** They shared one, so SSPL-1.0 code in a
  proprietary product read "Conditional" when SSPL requires the whole work to be SSPL. Each is now ruled from its own
  text: SSPL-1.0 is "no" for every distributed destination; BUSL-1.1 is "no" until its Change Date, then follows the
  licensor's Change License; Elastic-2.0 and RSALv2 allow closed products and services only on their stated
  limitations.
- **Corrections:** MPL-2.0's source duty covers every MPL file you ship, not only modified ones; LGPL-2.1 allows static
  linking if users can relink; LGPL-3.0 terms must allow reverse engineering for debugging; EPL-2.0 code can become
  GPL, never LGPL; AGPL-3.0's source offer is triggered by modification, not by being user-facing; LGPL-2.1-only
  caveats added.
- **What "no" means, stated:** the combined work cannot be released under the project's license (or a later version
  it allows). GPL code in an LGPL, MIT or Apache project is "no", and the conditions name the only route: moving the
  whole project to GPL. Under that rule three results changed: LGPL-3.0 into an LGPL-2.1-or-later project, and
  AGPL-3.0 into a GPL-2.0-or-later or GPL-3.0 project, are now "yes_narrows".
- `references/compatibility-matrix.md` is now generated from the data; it had drifted from it.

## 2.11 (2026-11-23)

- **The workbook is no longer distributed.** It was a v2.3 snapshot that predated every correction since; shipping it
  would contradict the data. Its Change Log tab is preserved below under "2.0 to 2.3". The reference docs in
  `references/` are the human-readable view, generated from `data/`.
- NOTICE names CounselMode LLC; package metadata lists it as author.
- The hosted endpoint's permanent address: https://licenses.counselmode.com/mcp.

## 2.10 (2026-11-23)

- **`choose_license`** (MCP tool and `choose` command): which license to release your own software, model weights or
  dataset under, for one of nine goals, with each recommendation checked against the licenses of code you include.
  A license that cannot take that code is excluded with the reason (for example, GPL-2.0-only code rules out MIT,
  Apache-2.0 and GPL-3.0-or-later). Source-available and use-restricted options appear only when open source is not
  required, marked as such. CounselMode editorial view.
- NOTICE states the SPDX License List's terms (part of the SPDX Specification: Community Specification License 1.0,
  earlier portions CC BY 3.0; Linux Foundation site content CC BY 3.0) and that we use a subset; attribution as both
  require: name, version, source.
- The goals live in `data/choosing.json` with exact IDs (`-or-later` for the GPL family; BigScience OpenRAIL-M for
  use-restricted weights); `choosing-a-license.md` is generated from it.

## 2.9 (2026-11-23)

- **Relicensing log checked against primary sources** (project announcements, license-file history, fork
  announcements): 7 confirmed with exact dates, 5 corrected. MinIO's fork is now pgsty/silo; Sentry moved to FSL-1.0 in
  Nov. 2023 and FSL-1.1 in Feb. 2024; Cal.com's dates fixed; Gemma 4's announcement date; Meta's Muse Spark Open is an
  open-weights release under its own license, not "proprietary". `relicensing-log.md` is now generated from the data.
- **Vizio:** the Aug. 10, 2026 trial did not go ahead; per SFC's own case page (a party statement, not the court
  docket, which could not be read) it is now expected in late 2026, with no verdict, judgment or settlement reported.
- **Hosted endpoint live** at https://counselmode-licenses.vercel.app/mcp (no sign-in), behind a per-IP flood limit.

## 2.8 (2026-11-23)

- **New AI records from primary sources:** three licenses, `LicenseRef-Mistral-Ecosystem-Open-Weight` (Mistral Large 4:
  MIT-style with a model-as-a-service gate, no revenue threshold), `LicenseRef-HAI-DEF` (Google's terms for MedGemma)
  and `LicenseRef-Meta-SAM` (SAM 3.1, partially verified: the Hugging Face file is gated); and 31 model records,
  including Mistral Large 3 and 4, Ministral 3, Magistral, MRL-era Mistral releases, EmbeddingGemma 2, MedGemma,
  Gemma 4 assistant variants, DeepSeek V2 to V3.2 releases, OCR and Math models, and Meta's hosted Muse models (API
  terms only). Now 132 licenses, 10 exceptions and 58 model records.
- Unconfirmed and left out or flagged: DeepSeek-Prover-V2 (model card and repo say the DeepSeek License, the Hugging
  Face file says MIT; the stricter one is recorded), Gemma Scope 2's terms, some DeepSeek release dates (repository
  creation dates only).
- Model aliases are unique within and across records (tested).

## 2.7 (2026-11-23)

- **MCP server** (`counselmode-licenses`, FastMCP 4, Python 3.11+): `lookup_license`, `model_license`,
  `check_compatibility`, `license_obligations`, `triage_dependencies` (up to 500 rows; a failing gate points to
  CounselMode's full screening), plus `search` and `fetch` for ChatGPT's deep research. All read-only; every result
  carries provenance and the disclaimer. The wheel bundles the skill folder, so the data and logic exist once.
- **Fixed: model lookups matched free text.** "Gemma 4" also returned the Gemma 1-3 record (its note mentions Gemma 4)
  and "Llama 3.1" found nothing. Model records now carry `aliases`, matched at version boundaries: "Llama 3.1 8B
  Instruct" finds Llama 3.x, "Mistral Large 2.1" does not match "Mistral Large 2", "DeepSeek-V3" returns both the
  original checkpoint's license and the later MIT one.

## 2.6 (2026-11-23)

- **Three new obligation values** for restrictions the vocabulary could not express: `no_derivatives` (CC BY-ND, CC
  BY-NC-ND), `reference_only` (MS-RSL) and `no_production_use` (BUSL-1.1, Oracle OTN, Mistral's non-production license).
  The allowed values now live in `scripts/license_lookup.py` (`OBLIGATIONS`, `TRIGGERS`); tests enforce them and require
  each to be defined in `docs/schema.md`, which now defines every value.
- **Internal-use risk** now also sees production limits and internal-use copyleft: BUSL-1.1 internal LOW to REVIEW
  (production use depends on the Additional Use Grant); RPL-1.5 internal LOW to HIGH (its duties attach to internal
  "Deploy"). No other rating changed.
- MS-RSL no longer needs a `commercial_use` trigger to be blocked for internal use: `reference_only` says why.

## 2.5 (2026-11-23)

Content gate (phase 1): primary-source research on the most-asked records, and every record's obligations checked
against its license text.

- **Obligations and triggers checked for all 139 records** against the license texts (spdx.org, stewards' own pages,
  official legal codes). None remain auto-derived. Common errors fixed: copyleft licenses missing attribution,
  change-marking, same-license and source duties (eight had none at all); permissive, content and hardware licenses
  with no triggers; `source_disclosure` wrongly added where a text only mentions source distributions (BSD-2-Clause,
  Zlib, BSL-1.0); `threshold` and `prohibited_use` stamped on AI licenses without such terms; network triggers missing
  from EUPL-1.2, OSL-3.0 and APSL-2.0.
- **26 most-asked records re-verified field by field** (GPL, LGPL and AGPL families, MIT, Apache-2.0, BSD, MPL-2.0,
  BUSL, SSPL, FSL, Llama, Gemma, Mistral, DeepSeek) and 18 AI model records. DeepSeek's license has an express patent
  grant; SSPL is GPLv3-based with no competing-use bar; Mistral's Modified MIT is a US$20M monthly-revenue bar; project
  examples sorted between `-only` and `-or-later` records.
- **Case law and regulation checked against court records and the Official Journal.** Corrected: Vizio (trial was
  scheduled, not held), Artifex (pleading-stage rulings), Entr'ouvert (EUR 800,000; secondary copies only), Versata
  (2012 to 2014); AI Act and CRA deadlines and steward duties completed. `SKILL.md`'s Doe v. GitHub line no longer
  says license and copyright claims are unaffected.
- **Internal-use risk rule fixed.** Internal use is blocked by an actual use restriction (`noncommercial_only`, or a
  noncommercial-family license), not by a commercial-use trigger, and licenses bounded by size or revenue rate REVIEW.
  Changes from 2.4: PolyForm Small Business BLOCK to REVIEW; Mistral's research and non-production licenses REVIEW to
  BLOCK. Other ratings that changed follow from corrected triggers (for example EUPL-1.2 and OSL-3.0 are now HIGH for
  SaaS).
- Oracle NFTC has its own record (it duplicated OTN); Oracle, Docker and Anaconda terms updated to their current
  dates. New verification status `Partially verified (primary)` with a `verification_note`.
- Reference docs (`references/`) are generated from `data/` by `scripts/build_references.py`; a test fails on drift.

Known state: 21 license records fully verified against primary sources, 11 partially, 2 secondary only (8 exception
records carry an earlier "verified" status that confirms only their SPDX listing); the rest not re-verified beyond
their obligations. (Corrected in 2.8: this line first said 29 by counting those 8 exceptions.) Editorial views for the 26 most-asked records await owner review.

## 2.4 (2026-11-23)

First version prepared for open release as the CounselMode License Navigator.

- **Fixed: wrong license resolved by partial match.** `obligations GPL-3.0` answered for `LGPL-3.0-only`, because
  lookups fell back to the first record whose name contained the query. Resolution is now exact first (alias, SPDX ID,
  name); a partial name returns candidates and `obligations`, `compat` and `triage` refuse to guess.
- **Fixed: compatibility matched label text.** `compat MIT GPL-3.0-only` found nothing and "GPL-3.0" also matched the
  LGPL and AGPL groups. New `data/compat_groups.json` lists the license IDs each compatibility label covers; `compat`
  matches on IDs.
- **Fixed: triage ignored operator precedence.** Any expression containing OR took its least risky part, so
  `GPL-3.0-only AND (MIT OR Apache-2.0)` came out LOW. SPDX expressions are now parsed (AND binds tighter than OR,
  parentheses, WITH; operators case-sensitive as the spec requires).
- Added SPDX deprecated identifiers as aliases (`GPL-3.0` is `GPL-3.0-only`, `GPL-3.0+` is `GPL-3.0-or-later`, and the
  LGPL, AGPL and GFDL equivalents), plus `proprietary` and `closed source`.
- Risk ratings unchanged: the family-to-risk rule is now an explicit table, tested to give the v2.3 result for every
  license and scenario.
- Tests (`tests/`), Apache-2.0 for code, CC BY 4.0 for data, NOTICE, schema documentation.
- Opinions are labelled "editorial view" (`editorial_view`), attributed to CounselMode.
- `data/` is now the source of truth; the workbook is a v2.3 snapshot until regenerated.

Known state of the data: 115 of 139 license records are "Not re-verified" and 129 have obligations auto-derived from
the license text. Every answer reports a record's verification status; treat unverified records accordingly.

## 2.0 to 2.3 (2026-11-18 and earlier)

From the workbook's Change Log tab (the workbook is no longer distributed; see 2.11).

1. Neo4j v. PureThink note corrected (licensor added Commons Clause; licensees cannot strip it); dates and appeal dismissal added (6-Source-Available; Case Law)
2. FSL SPDX IDs corrected to FSL-1.1-ALv2 / FSL-1.1-MIT (6-Source-Available)
3. Gemma mapped per version (Gemma 4 = Apache-2.0) (9-AI Model Licenses; Model Map; Common Projects)
4. Meta Muse models added (Glimmer Apache-2.0; Spark Open Muse Model License; Spark proprietary) (9-AI; Model Map)
5. MinIO maintenance/abandonment documented; maintenance-status column added (Common Projects; Use-Case; Relicensing Log)
6. Vizio nuance added (Dec. 23, 2025 ruling; trial status) (Use-Case; Case Law)
7. Compatibility matrix: GPL narrowing labels harmonized; LGPL split into 2.1 and 3.0; model row filled; Apache/MIT/OpenMDW model row added (Compatibility Matrix)
8. Artistic-2.0 patent grant corrected to express (2-Permissive)
9. AGPL "§13/§13" typo fixed (5-Network Copyleft)
10. Double-counted OSL-3.0 and non-license rows removed from license counts (moved to Model Map) (5-Network; 9-AI)
11. Blank outbound cells filled (Perimeter, Shield, Prosperity, CDLA-Sharing) (6; 7; 10)
12. Added Unicode-3.0, BSD-2-Clause-Patent, PHP-3.01, Ms-PL, OFL-1.1, CAL-1.0, CC-BY-NC-SA/ND, GFDL-1.3, ODC-By, PDDL, CERN-OHL P/W/S (Various)
13. New families: Ethical Source; Hardware; Exceptions tab (WITH expressions) (8; 11; 13)
14. Added Kimi K2/K3, Mistral Modified MIT, OpenMDW-1.1, Muse Model License (9-AI)
15. Added Docker Desktop, Anaconda, Oracle Java SE (12-Proprietary)
16. New tabs: Model Map, Case Law, Regulatory Overlay, Relicensing Log, Change Log (New)
17. Provenance and volatility columns; "Editorial view" labels on judgment columns (All family tabs)
18. Cal.com corrected: commercial edition went closed source; community code relaunched as Cal.diy (MIT) (Relicensing Log)
19. Glossary and diligence checklist expanded (Glossary; Checklist)
20. Structured data (licenses.json, compatibility.json, models.json, aliases.json) generated for agent use (Skill package)
21. v2.1: Doe v. GitHub updated to 9th Cir. decision (Sept. 16, 2026); AI coding-assistant scenario revised (Case Law; Use-Case)
22. v2.1: Gemma 4 12B Unified split out (June 3, 2026) (Model Map)
23. v2.1: Neo4j judgment date corrected (findings July 22, 2024; judgment Aug. 15, 2024) (6-Source-Available; Case Law)
24. v2.1: Vizio wording softened to a trial-court pretrial order SFC calls irrelevant (Use-Case; Case Law)
25. v2.1: Volatile flag made rule-based (AI, source-available, noncommercial, ethical, proprietary/vendor ToS always Yes) (All family tabs)
26. v2.1: Provenance split into Source / Verification status / Last verified; SPDX list status column added (All family tabs)
27. v2.1: Maintenance status defaults changed from "Active" to "Unknown (not verified)" (Common Projects)
28. v2.1: One row per SPDX ID; compound and non-ID values replaced with clean IDs or LicenseRefs; MS-PL casing fixed (All family tabs)
29. v2.1: Compatibility matrix: Apache->MIT now Conditional; Apache->LGPL-2.1+ uses narrowing wording; model rows made consistent (N/A for code-license columns) (Compatibility Matrix)
30. v2.1: Hippocratic 3.0 outbound filled; Overview OpenMDW wording fixed (8-Ethical Source; Overview)
31. v2.1: ID and verification columns added to Exceptions, Case Law, Regulatory, Model Map (Reference tabs)
32. v2.1: Model Map verified against primary sources for Llama 4, gpt-oss, DeepSeek V4, Qwen3.8-Max, Mistral Medium 3.5; remaining secondary rows flagged with caveat (Model Map)
33. v2.2: All non-LicenseRef IDs checked against SPDX License List 3.29.0 (2026-09-16); 10 IDs not on the list re-keyed to LicenseRef- (PolyForm Shield/Perimeter, Prosperity-3.0, FCL-1.0-ALv2/MIT, OpenMDW-1.1, BigScience RAIL x2, CreativeML-OpenRAIL-M, MS-RSL); old IDs and ScanCode keys kept as aliases (All family tabs; aliases.json)
34. v2.2: Hippocratic 3.0 keyed to listed ID Hippocratic-3.0-core (modules not expressible) (8-Ethical Source)
35. v2.2: "Assumed listed" replaced by Listed / Not on SPDX list status tied to the snapshot; build fails on any ID neither confirmed listed nor confirmed absent (All family tabs)
36. v2.2: Custom exceptions use AdditionRef- (SPDX 3.0); OpenSSL exception treated as a note; listed exceptions verified against SPDX exceptions list 3.29.0 (13-Exceptions)
37. v2.2: Model Map: Codestral / Mistral Large 2 split; Muse Spark keyed to LicenseRef-SaaS-ToS; OSAID moved to Glossary; OpenMDW-1.1 keyed to LicenseRef-OpenMDW-1.1; Qwen3.8-Max and Qwen Community 1.0 records added so all model IDs join (Model Map; 9-AI)
38. v2.2: Common Projects: SPDX expression column added; multi-product rows split; build fails if any expression token does not join to a license record or listed exception (Common Projects)
39. v2.2: Compatibility: Apache-2.0 into proprietary distributed now Conditional; MPL-2.0 rows use "combined work becomes" wording (Compatibility Matrix)
40. v2.2: Blank "Last verified" exported as null in all JSON files (Data export)
41. v2.3: Hippocratic 3.0 split: Hippocratic-3.0-core only for core text with no modules; LicenseRef-Hippocratic-3.0-modules (generic) and LicenseRef-Hippocratic-3.0-FULL added; MCP warning on core ID (8-Ethical Source; licenses.json)
42. v2.3: CreativeML-OpenRAIL-M re-confirmed absent from SPDX 3.29.0 (no RAIL license listed); old ID and Hugging Face key kept as aliases with warning (9-AI; aliases.json)
43. v2.3: FFmpeg split into default (LGPL-2.1-or-later) and --enable-gpl (GPL-2.0-or-later) build rows; Android kernel expression now uses WITH Linux-syscall-note (Common Projects)
44. v2.3: Split project rows (Redis 7.4/8, Valkey, Elasticsearch, OpenSearch, Terraform, OpenTofu) given row-specific descriptions; per-row expression verification status added (Common Projects; context.json)
45. v2.3: DeepSeek split by checkpoint: original V3 (Dec. 2024) under DeepSeek License Agreement v1.0; R1 / V3-0324 onward MIT; verified against model cards (Model Map; 9-AI)
46. v2.3: OpenSSL linking note re-keyed Note- (not AdditionRef-); note records carry record_type=note and null expression (13-Exceptions; licenses.json)
48. v2.3.1: Model-weights matrix row split into Apache-2.0 / OpenMDW-1.1 (Conditional, both carry termination terms) and MIT (Yes); no mixed-value cells (Compatibility Matrix)
49. v2.3.1: Hippocratic-3.0-core row rewritten to describe core terms only; module language kept on the modules / FULL rows (8-Ethical Source)
47. v2.3: Matrix legend defines "Yes" as notice-only conditions and "Conditional" as substantive terms; Apache-2.0 model weights into proprietary now Conditional (Compatibility Matrix)
