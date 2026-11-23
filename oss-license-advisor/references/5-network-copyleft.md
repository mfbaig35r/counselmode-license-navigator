# 5-Network Copyleft

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## GNU Affero GPL v3.0 [AGPL-3.0-only] — `AGPL-3.0-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer', 'installation_info']
- steward_year: FSF / 2007 (Affero v1: 2002)
- allows: Run, study, modify, distribute
- conditions: Conveying the program or a work based on it requires licensing the whole under AGPLv3 with complete corresponding source, with GPLv3's Installation Information for "User Products" (anti-tivoization), anti-DRM (§3), express patent license and anti-discrimination patent deal terms (§11), 30-day cure for first violation (§8); plus §13: if you MODIFY the program and users interact with it remotely over a network, you must offer those users the Corresponding Source of your version
- copyleft_detail: Whole work; distribution AND remote network interaction with modified version
- gpl_compatibility: Compatible with GPLv3: combination permitted by GPLv3 §13 and AGPLv3 §13; the AGPL part keeps its network clause
- notable_projects: Grafana, Elasticsearch & Kibana (AGPL option alongside SSPL and ELv2), Redis 8 (AGPLv3 option alongside RSALv2 and SSPLv1), MinIO (repository no longer maintained)
- saas: Triggered when a modified version is offered to users interacting with it over a network (§13)
- notes: Scope of "interacting remotely" and what counts as the "Program" in a microservice architecture is debated.
- **Editorial view – build_on:** HIGH for SaaS and distribution; LOW for internal use. Many companies ban AGPL dependencies outright. Unmodified internal use is generally safe; modifying it and exposing it over a network triggers the source offer.
- **Editorial view – license_your_own:** Used by open-core vendors to require cloud providers to share their changes or buy a commercial license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/agpl-3.0.txt; https://spdx.org/licenses/AGPL-3.0-only.html; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/ | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: False

## GNU Affero GPL v3.0 [AGPL-3.0-or-later] — `AGPL-3.0-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer', 'installation_info']
- steward_year: FSF / 2007 (Affero v1: 2002)
- allows: Run, study, modify, distribute
- conditions: Conveying the program or a work based on it requires licensing the whole under AGPLv3 with complete corresponding source, with GPLv3's Installation Information for "User Products" (anti-tivoization), anti-DRM (§3), express patent license and anti-discrimination patent deal terms (§11), 30-day cure for first violation (§8); plus §13: if you MODIFY the program and users interact with it remotely over a network, you must offer those users the Corresponding Source of your version
- copyleft_detail: Whole work; distribution AND remote network interaction with modified version
- gpl_compatibility: Compatible with GPLv3: combination permitted by GPLv3 §13 and AGPLv3 §13; the AGPL part keeps its network clause
- notable_projects: Mastodon, iText, Ghostscript, Nextcloud (mixed; some files AGPL-3.0-only)
- saas: Triggered when a modified version is offered to users interacting with it over a network (§13)
- notes: Scope of "interacting remotely" and what counts as the "Program" in a microservice architecture is debated.
- **Editorial view – build_on:** HIGH for SaaS and distribution; LOW for internal use. Many companies ban AGPL dependencies outright. Unmodified internal use is generally safe; modifying it and exposing it over a network triggers the source offer.
- **Editorial view – license_your_own:** Used by open-core vendors to require cloud providers to share their changes or buy a commercial license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/agpl-3.0.txt; https://spdx.org/licenses/AGPL-3.0-or-later.html; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/ | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: False

## Reciprocal Public License 1.5 — `RPL-1.5`

- **osi_status:** approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction', 'any_use']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer', 'patent_retaliation', 'naming_rule']
- steward_year: Technical Pursuit / 2007
- allows: Use, modify
- conditions: Must publish source of modifications even for internal/private deployment
- copyleft_detail: Extends to internal use
- gpl_compatibility: Incompatible with GPL
- notable_projects: Rare
- saas: Triggered even internally
- **Editorial view – build_on:** HIGH for any use, including internal use; avoid.
- **Editorial view – license_your_own:** Avoid.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Common Public Attribution License 1.0 — `CPAL-1.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer', 'patent_retaliation', 'naming_rule']
- steward_year: Socialtext / 2007
- allows: MPL-1.1 based
- conditions: Network use counts as distribution; prominent attribution (logo) display requirement
- copyleft_detail: File-level + network
- gpl_compatibility: Incompatible with GPL
- notable_projects: Historic web apps
- saas: TRIGGERED
- **Editorial view – build_on:** LOW for internal use; HIGH for SaaS and distribution. Attribution display in UI.
- **Editorial view – license_your_own:** Rare.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Cryptographic Autonomy License 1.0 — `CAL-1.0`

- **osi_status:** approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'source_disclosure', 'same_license', 'network_source_offer', 'installation_info', 'patent_retaliation']
- steward_year: Holochain / 2019
- allows: Use, modify, distribute
- conditions: Copyleft triggered by distribution AND by providing use to third parties over a network; must also give users access to their own data (user-data autonomy)
- copyleft_detail: Whole work; distribution + network use
- gpl_compatibility: Incompatible with GPL (generally treated so)
- notable_projects: Holochain
- saas: TRIGGERED
- notes: OSI-approved network copyleft beyond AGPL.
- **Editorial view – build_on:** HIGH; network trigger plus data-portability duties.
- **Editorial view – license_your_own:** Rare.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

