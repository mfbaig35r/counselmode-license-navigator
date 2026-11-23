# Changelog

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
