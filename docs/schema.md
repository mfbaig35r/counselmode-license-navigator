# Data schema

All files are in `oss-license-advisor/data/`, UTF-8 JSON. `data/` is the source of truth.

## licenses.json

`{schema_version, generated, disclaimer, licenses: [...]}`. One record per SPDX ID or `LicenseRef-` (139: 129
licenses in 12 families, and 10 exceptions).

| Field | Values |
|---|---|
| `id` | SPDX ID, `LicenseRef-...`, `AdditionRef-...` (custom exceptions) or `Note-...` (a note, never part of an expression) |
| `name`, `family`, `family_tab` | Display name; family (`public_domain`, `permissive`, `weak_copyleft`, `strong_copyleft`, `network_copyleft`, `source_available`, `noncommercial`, `ethical_source`, `ai_model_licenses`, `content_data`, `hardware`, `proprietary`, `exception`); the reference doc it appears in |
| `osi_status`, `osi_note` | `approved`, `not_approved`, `withdrawn`, `pending`, `not_applicable` |
| `fsf_status`, `fsf_note` | `free`, `nonfree`, `not_reviewed` |
| `patent_grant`, `patent_note` | `express`, `none`, `excluded`, `varies` |
| `copyleft_scope` | `none`, `file_or_library`, `whole_work`, `network`, `use_restriction`, `contract`, `varies` |
| `triggers` | What sets obligations off; see "Obligations and triggers" below |
| `obligations` | Duties and restrictions; see "Obligations and triggers" below |
| `obligations_derived` | Set when obligations were derived automatically from the text: review before relying |
| `facts` | `steward_year`, `allows`, `conditions`, `copyleft_detail`, `gpl_compatibility`, `notable_projects`, `saas`, `notes` |
| `editorial_view` | CounselMode's judgment, not legal advice: `build_on`, `license_your_own`, `practical_effect`, `jurisdiction`, `attribution` |
| `provenance` | `source`, `verification_status` (`Verified (primary)`: every fact checked against a primary source; `Partially verified (primary)`: checked, with at least one detail not confirmable, named in `verification_note`; `Secondary only`; `Not re-verified`), `last_verified`, `volatile` (always true for AI model, source-available, noncommercial, ethical-source and proprietary records), `spdx_list_status`, `expression_valid_in` |
| `caveat` | True when the record should be confirmed against the official text |
| `warnings` | Record-specific cautions to show the user |

### Obligations and triggers

The only allowed values (`OBLIGATIONS` and `TRIGGERS` in `scripts/license_lookup.py`; a test enforces both lists).

| Obligation | Meaning |
|---|---|
| `attribution` | Keep copyright and license notices, or reproduce them with copies, binaries or docs |
| `notice_file` | Carry forward a NOTICE-type file |
| `state_changes` | Mark or describe modifications |
| `source_disclosure` | Make source available to recipients when distributing |
| `same_license` | Modifications or the combined work must use the same terms |
| `network_source_offer` | Offer source to users who interact over a network |
| `relinking` | Let users relink or replace the library in a combined work |
| `installation_info` | Provide installation information or keys for user products |
| `patent_retaliation` | The license or its patent grant ends if you bring a patent claim |
| `noncommercial_only` | Use limited to noncommercial purposes |
| `no_competing_service` | No competing product or service |
| `mau_revenue_cap` | Rights limited above a user-count, headcount or revenue threshold |
| `maas_gate` | Offering it as a service needs permission or extra terms |
| `naming_rule` | Naming, branding or attribution-string rules for derivatives (not "no endorsement" clauses) |
| `usage_policy` | An acceptable-use or prohibited-use policy applies and must flow down |
| `no_derivatives` | Adaptations may not be shared |
| `reference_only` | The source may be viewed for reference; other use is not licensed |
| `no_production_use` | Production use is not licensed (development, testing or evaluation only, unless a grant says otherwise) |

| Trigger | Meaning |
|---|---|
| `distribution` | Conveying copies (source or binary) to others |
| `network_interaction` | Users interacting with it remotely over a network |
| `service_offering` | Offering it, or a similar service, to third parties as a service |
| `competing_use` | Use that competes with the licensor |
| `commercial_use` | Any commercial use (sets obligations off; it is not itself a ban) |
| `threshold` | Crossing a size, revenue or user threshold |
| `prohibited_use` | Uses listed as prohibited |
| `any_use` | Obligations apply to any use at all |

**Internal-use risk.** BLOCK when `noncommercial_only` or `reference_only` applies (or the license is in the
noncommercial family and not size-bounded); REVIEW when bounded by size, revenue or production use; copyleft licenses
with `any_use` keep their base risk; otherwise as the family table says.

## compatibility.json and compat_groups.json

`compatibility.json`: a list of `{inbound, outbound, context, result, conditions, source}`. `inbound` and `outbound` are
group labels such as `"MIT / BSD-2 / BSD-3 / ISC / zlib"`. `context`: `distribution_combined_work` or
`saas_not_distributed`. `result`: `yes` (notice-only conditions), `yes_narrows` (the combined work takes the stricter
license), `conditional` (substantive terms carry over), `no`, `not_applicable`.

`compat_groups.json`: `{note, groups: {label: {members: [license IDs], note?}}}`. Every label used in
`compatibility.json` is here, and every member is a record in `licenses.json` (both tested).

The per-family docs in `references/`, plus `case-law.md`, `regulatory-overlay.md` and `model-map.md`, are generated
from these files by `scripts/build_references.py`; a test fails if they drift.

## models.json

A list of `{vendor, model, license, license_id, release_date, conditions, osi, source, last_verified,
verification_status, caveat, aliases}`, keyed by exact model and version. `aliases` lists the version names people
type ("Llama 3.1", "Gemma 4 E2B"); lookups match on them, at version boundaries, never on free text. Every record
must have them (tested). Never infer a model's license from its vendor.

## aliases.json

`{"how people write it": "SPDX ID or LicenseRef"}`, matched case- and punctuation-insensitively. Includes SPDX's
deprecated identifiers (`GPL-3.0` is `GPL-3.0-only`).

## context.json

`case_law`, `regulatory`, `relicensing` and `projects` (each project with an SPDX `license_expression` and its
`expression_verification_status`), plus `spdx_snapshot` (list version and re-keyed IDs).

## spdx_snapshot_3.29.0.json

The SPDX list facts the build relied on: confirmed-listed IDs (the relevant subset), confirmed-absent IDs and the full
exceptions list.
