# Changelog

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

Known state: 29 records verified against primary sources, 11 partially, 2 secondary only, 95 not re-verified beyond
their obligations. Editorial views for the 26 most-asked records await owner review.

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

## 2.3 (2026-11-18)

Earlier history is in the workbook's Change Log tab (`oss-license-advisor/assets/`).
