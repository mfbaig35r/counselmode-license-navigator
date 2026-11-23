# 5-Network Copyleft

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## GNU Affero GPL v3.0 [AGPL-3.0-only] — `AGPL-3.0-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['network_source_offer']
- steward_year: FSF / 2007 (Affero v1: 2002)
- allows: As GPLv3
- conditions: As GPLv3 plus §13: if you MODIFY the program and users interact with it remotely over a network, you must offer those users the Corresponding Source of your version
- copyleft_detail: Whole work; distribution AND remote network interaction with modified version
- gpl_compatibility: Compatible with GPLv3: combination permitted by GPLv3 §13 and AGPLv3 §13; the AGPL part keeps its network clause
- notable_projects: Mastodon, Nextcloud, Grafana (since 2021), MinIO, Elasticsearch & Kibana (AGPL option since 2024), Redis 8 (AGPL option 2025), iText, Ghostscript
- saas: TRIGGERED
- notes: Scope of "interacting remotely" and what counts as the "Program" in a microservice architecture is debated.
- **Editorial view – build_on:** VERY HIGH for SaaS/cloud products. Many companies ban AGPL dependencies outright (e.g., Google policy). Unmodified internal use is generally safe; modifying and exposing over a network triggers source release.
- **Editorial view – license_your_own:** Used by open-core vendors to force cloud providers to share or buy commercial license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## GNU Affero GPL v3.0 [AGPL-3.0-or-later] — `AGPL-3.0-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['network_source_offer']
- steward_year: FSF / 2007 (Affero v1: 2002)
- allows: As GPLv3
- conditions: As GPLv3 plus §13: if you MODIFY the program and users interact with it remotely over a network, you must offer those users the Corresponding Source of your version
- copyleft_detail: Whole work; distribution AND remote network interaction with modified version
- gpl_compatibility: Compatible with GPLv3: combination permitted by GPLv3 §13 and AGPLv3 §13; the AGPL part keeps its network clause
- notable_projects: Mastodon, Nextcloud, Grafana (since 2021), MinIO, Elasticsearch & Kibana (AGPL option since 2024), Redis 8 (AGPL option 2025), iText, Ghostscript
- saas: TRIGGERED
- notes: Scope of "interacting remotely" and what counts as the "Program" in a microservice architecture is debated.
- **Editorial view – build_on:** VERY HIGH for SaaS/cloud products. Many companies ban AGPL dependencies outright (e.g., Google policy). Unmodified internal use is generally safe; modifying and exposing over a network triggers source release.
- **Editorial view – license_your_own:** Used by open-core vendors to force cloud providers to share or buy commercial license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Reciprocal Public License 1.5 — `RPL-1.5`

- **osi_status:** approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['source_disclosure']
- steward_year: Technical Pursuit / 2007
- allows: Use, modify
- conditions: Must publish source of modifications even for internal/private deployment
- copyleft_detail: Extends to internal use
- gpl_compatibility: Incompatible with GPL
- notable_projects: Rare
- saas: Triggered even internally
- **Editorial view – build_on:** VERY HIGH; avoid.
- **Editorial view – license_your_own:** Avoid.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Common Public Attribution License 1.0 — `CPAL-1.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution']
- steward_year: Socialtext / 2007
- allows: MPL-1.1 based
- conditions: Network use counts as distribution; prominent attribution (logo) display requirement
- copyleft_detail: File-level + network
- gpl_compatibility: Incompatible with GPL
- notable_projects: Historic web apps
- saas: TRIGGERED
- **Editorial view – build_on:** Moderate-high: attribution display in UI.
- **Editorial view – license_your_own:** Rare.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Cryptographic Autonomy License 1.0 — `CAL-1.0`

- **osi_status:** approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['network_source_offer']
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

