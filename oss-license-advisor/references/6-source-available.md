# 6-Source-Available

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## Server Side Public License v1 — `SSPL-1.0`

- **osi_status:** withdrawn
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['source_disclosure', 'same_license', 'no_competing_service']
- steward_year: MongoDB / 2018
- allows: Use, modify, distribute (AGPLv3-based)
- conditions: §13: offering the program "as a service" requires releasing source of the ENTIRE service stack (management, UI, APIs, monitoring, backup, hosting software) under SSPL
- copyleft_detail: Entire service infrastructure
- gpl_compatibility: Incompatible with GPL/AGPL
- notable_projects: MongoDB (since 2018), Elasticsearch/Kibana (2021-2024, now also AGPL option), Graylog (historic)
- saas: Core restriction
- notes: Not OSI-approved; considered source-available.
- **Editorial view – build_on:** Internal use and use as a backend for your own app are generally OK; offering the software itself as a hosted service to third parties is effectively prohibited unless you buy a commercial license. Debian, Fedora, RHEL exclude SSPL software.
- **Editorial view – license_your_own:** Vendor anti-cloud defense; not open source.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Business Source License 1.1 — `BUSL-1.1`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['source_disclosure', 'no_competing_service']
- steward_year: MariaDB / 2016-2017
- allows: Copy, modify, non-production use; vendor-defined "Additional Use Grant" may allow production use
- conditions: Production use limited by Additional Use Grant (often "not a competing offering"); each version converts to a "Change License" (GPLv2+ compatible, e.g., Apache-2.0/MPL-2.0) on Change Date (max 4 years)
- copyleft_detail: Usage restriction until Change Date
- gpl_compatibility: Not compatible until conversion
- notable_projects: MariaDB MaxScale, CockroachDB (historic), HashiCorp Terraform/Vault/Consul (since Aug 2023), Sentry (historic), Couchbase
- saas: Restricted per Additional Use Grant
- notes: Change Date mechanics: older releases become open source.
- **Editorial view – build_on:** Read the Additional Use Grant carefully - it defines what is allowed. Competing-service restrictions; forks appeared (OpenTofu from Terraform, OpenBao from Vault).
- **Editorial view – license_your_own:** Delayed open source; protects vendor monetization window.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Elastic License 2.0 — `Elastic-2.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['attribution', 'no_competing_service']
- steward_year: Elastic / 2021
- allows: Use, copy, distribute, modify, create derivatives
- conditions: No providing as hosted/managed service with substantial set of features; no circumventing license keys; no removing notices
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Elasticsearch & Kibana (alongside SSPL & AGPL since 2024), Airbyte (some), many SaaS vendors
- saas: Restricted (no managed service)
- notes: Amazon forked Elasticsearch as OpenSearch (Apache-2.0).
- **Editorial view – build_on:** Fine for internal use and embedding in your product as long as you do not offer the software itself as a managed service and do not bypass licensing functionality.
- **Editorial view – license_your_own:** Short, readable vendor-protective license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Redis Source Available License v2 — `LicenseRef-RSALv2`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service', 'noncommercial_only']
- steward_year: Redis / 2022 (core 2024)
- allows: Use, modify, distribute
- conditions: No commercializing as a database product/managed service; no circumventing license keys
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Redis 7.4 (2024); Redis 8 added AGPLv3 option (2025)
- saas: Restricted
- notes: Redis license history shows fast-changing vendor terms - re-verify.
- **Editorial view – build_on:** Avoid offering Redis as a service; consider Valkey (BSD-3, Linux Foundation fork).
- **Editorial view – license_your_own:** Vendor anti-cloud.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Functional Source License [FSL-1.1-ALv2] — `FSL-1.1-ALv2`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: Sentry / 2023
- allows: Any purpose except "Competing Use"
- conditions: No competing commercial product/service; each version converts to Apache-2.0 or MIT after 2 years
- copyleft_detail: Usage restriction; 2-year conversion
- gpl_compatibility: Not compatible until conversion
- notable_projects: Sentry, Codecov, Liquibase Community 5.0+ (FSL-1.1-ALv2 since Sept. 30, 2025)
- saas: Restricted only for competing use
- **Editorial view – build_on:** Low-moderate unless you compete with the licensor.
- **Editorial view – license_your_own:** "Fair Source" option with short conversion period.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://spdx.org/licenses ; https://www.liquibase.com/blog/liquibase-community-for-the-future-fsl | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Functional Source License [FSL-1.1-MIT] — `FSL-1.1-MIT`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: Sentry / 2023
- allows: Any purpose except "Competing Use"
- conditions: No competing commercial product/service; each version converts to Apache-2.0 or MIT after 2 years
- copyleft_detail: Usage restriction; 2-year conversion
- gpl_compatibility: Not compatible until conversion
- notable_projects: Sentry, Codecov, Liquibase Community 5.0+ (FSL-1.1-ALv2 since Sept. 30, 2025)
- saas: Restricted only for competing use
- **Editorial view – build_on:** Low-moderate unless you compete with the licensor.
- **Editorial view – license_your_own:** "Fair Source" option with short conversion period.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://spdx.org/licenses ; https://www.liquibase.com/blog/liquibase-community-for-the-future-fsl | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Commons Clause (rider) — `LicenseRef-Commons-Clause`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['source_disclosure']
- steward_year: FOSSA/Heather Meeker / 2018
- allows: Base license terms (e.g., Apache) minus right to "Sell"
- conditions: Cannot sell the software or a service whose value derives substantially from it
- copyleft_detail: Usage restriction overlay
- gpl_compatibility: Not compatible
- notable_projects: Redis modules (historic), Neo4j Enterprise 3.4-3.5 (AGPL + Commons Clause)
- saas: Restricted
- notes: Neo4j v. PureThink: the LICENSOR (Neo4j) appended the Commons Clause to the AGPL; the court rejected the argument that licensees could strip it out under AGPL §7/§10, because those sections restrict "you" (the licensee), not the licensor. 9th Cir. unpublished, non-precedential memorandum (Feb. 18, 2022). District court findings of fact July 22, 2024 (US$597,000 damages + permanent injunction); judgment entered Aug. 15, 2024 (reported to add prejudgment interest less a stipulated deduction); appeal No. 24-5538 dismissed Dec. 10, 2025; satisfaction of judgment filed Dec. 15, 2025. No appellate merits ruling on §7. See Case Law tab.
- **Editorial view – build_on:** Moderate-high; ambiguity of "substantially". A project labeled "Apache 2.0 + Commons Clause" is NOT Apache-licensed.
- **Editorial view – license_your_own:** Not recommended (ambiguous).
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: CourtListener docket 5:18-cv-07182 (N.D. Cal.); govinfo judgment Doc. 248 | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## PolyForm Shield 1.0.0 — `LicenseRef-PolyForm-Shield-1.0.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: PolyForm Project / 2019
- allows: Any purpose except providing products that compete with licensor
- conditions: Non-compete
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Various
- saas: Restricted for competitors
- **Editorial view – build_on:** Moderate if you might compete.
- **Editorial view – license_your_own:** Lawyer-drafted standardized source-available license; bars any product competing with the licensor.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## PolyForm Perimeter 1.0.0 — `LicenseRef-PolyForm-Perimeter-1.0.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: PolyForm Project / 2019
- allows: As Shield but narrower (cannot compete with the software itself)
- conditions: Non-compete
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Various
- saas: Restricted
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Use when you want to bar only direct substitutes for your software, not all competitors.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Confluent Community License 1.0 — `LicenseRef-Confluent`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: Confluent / 2018
- allows: Use, modify, distribute
- conditions: No offering as SaaS competing with Confluent (e.g., KSQL as a service)
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Confluent Schema Registry, ksqlDB
- saas: Restricted
- **Editorial view – build_on:** Moderate; Apache Kafka itself is Apache-2.0 - distinguish components.
- **Editorial view – license_your_own:** Vendor protection.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Fair Core License [FCL-1.0-ALv2] — `LicenseRef-FCL-1.0-ALv2`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- steward_year: Keygen / 2024
- allows: FSL-like plus license-key protected features
- conditions: Competing-use restriction; 2-year conversion
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Keygen
- saas: Restricted
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Open-core variant of FSL.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Fair Core License [FCL-1.0-MIT] — `LicenseRef-FCL-1.0-MIT`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- steward_year: Keygen / 2024
- allows: FSL-like plus license-key protected features
- conditions: Competing-use restriction; 2-year conversion
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: Keygen
- saas: Restricted
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Open-core variant of FSL.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Timescale License (TSL) — `LicenseRef-Timescale`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['no_competing_service']
- steward_year: Timescale / 2018
- allows: Use internally and in your own SaaS
- conditions: No offering TimescaleDB as a DBaaS
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: TimescaleDB community features (core is Apache-2.0)
- saas: Restricted for DBaaS
- **Editorial view – build_on:** Moderate; split licensing per feature.
- **Editorial view – license_your_own:** Vendor protection.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

