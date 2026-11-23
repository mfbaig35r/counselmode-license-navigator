# 6-Source-Available

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## Server Side Public License v1 — `SSPL-1.0`

- **osi_status:** withdrawn
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** network
- **triggers:** ['distribution', 'service_offering']
- **obligations:** ['source_disclosure', 'same_license', 'installation_info']
- steward_year: MongoDB / 2018
- allows: Use, modify, distribute (GPLv3-based per MongoDB; s.13 replaced)
- conditions: §13: offering the program "as a service" requires releasing source of the ENTIRE service stack (management, UI, APIs, monitoring, backup, hosting software) under SSPL
- copyleft_detail: Entire service infrastructure
- gpl_compatibility: Incompatible with GPL/AGPL
- notable_projects: MongoDB (since Oct. 16, 2018), Elasticsearch/Kibana (since 2021; SSPL still offered alongside AGPL-3.0 and ELv2), Graylog (current)
- saas: Core condition: s.13 Service Source Code release
- notes: Not OSI-approved; considered source-available.
- **Editorial view – build_on:** Internal use and use as a backend for your own app are generally OK; offering the software itself as a hosted service to third parties is effectively prohibited unless you buy a commercial license. Debian, Fedora, RHEL exclude SSPL software.
- **Editorial view – license_your_own:** Vendor anti-cloud defense; not open source.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.mongodb.com/legal/licensing/server-side-public-license ; https://www.mongodb.com/legal/licensing/server-side-public-license/faq ; https://opensource.org/blog/the-sspl-is-not-an-open-source-license ; https://www.gnu.org/licenses/license-list.html ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Business Source License 1.1 — `BUSL-1.1`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['attribution', 'same_license', 'no_competing_service', 'no_production_use']
- steward_year: MariaDB / 2016-2017
- allows: Copy, modify, non-production use; vendor-defined "Additional Use Grant" may allow production use
- conditions: Production use limited by Additional Use Grant (often "not a competing offering"); each version converts to a "Change License" (GPLv2+ compatible, e.g., Apache-2.0/MPL-2.0) on Change Date (max 4 years)
- copyleft_detail: Usage restriction until Change Date
- gpl_compatibility: Not compatible until conversion
- notable_projects: MariaDB MaxScale, CockroachDB (historic; now CockroachDB Software License), HashiCorp Terraform/Vault/Consul (BUSL; Licensor now IBM), Sentry (historic; now FSL), Couchbase Server components
- saas: Restricted per Additional Use Grant
- notes: Change Date mechanics: older releases become open source.
- **Editorial view – build_on:** Read the Additional Use Grant carefully - it defines what is allowed. Competing-service restrictions; forks appeared (OpenTofu from Terraform, OpenBao from Vault).
- **Editorial view – license_your_own:** Delayed open source; protects vendor monetization window.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://mariadb.com/bsl11/ ; https://opensource.org/api/licenses ; https://www.gnu.org/licenses/license-list.html ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: True

## Elastic License 2.0 — `Elastic-2.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['service_offering', 'distribution']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'no_competing_service']
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
- **triggers:** ['service_offering', 'competing_use', 'distribution']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'no_competing_service']
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
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['attribution', 'no_competing_service', 'patent_retaliation']
- steward_year: Sentry / 2023
- allows: Any purpose except "Competing Use"
- conditions: No Competing Use (commercial product/service that substitutes for the Software or a licensor product existing at release, or offers substantially similar functionality); each version additionally licensed under Apache License, Version 2.0 on the second anniversary of its release
- copyleft_detail: Usage restriction; 2-year conversion
- gpl_compatibility: Not compatible until conversion
- notable_projects: Sentry, Codecov, Liquibase Community 5.0+ (FSL-1.1-ALv2 since Sept. 30, 2025)
- saas: Restricted only for competing use
- **Editorial view – build_on:** Low-moderate unless you compete with the licensor.
- **Editorial view – license_your_own:** "Fair Source" option with short conversion period.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://github.com/getsentry/fsl.software/blob/main/FSL-1.1-ALv2.template.md ; https://fsl.software/ ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) ; https://opensource.org/api/licenses ; https://www.gnu.org/licenses/license-list.html | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: True

## Functional Source License [FSL-1.1-MIT] — `FSL-1.1-MIT`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering']
- **obligations:** ['attribution', 'no_competing_service', 'patent_retaliation']
- steward_year: Sentry / 2023
- allows: Any purpose except "Competing Use"
- conditions: No Competing Use (commercial product/service that substitutes for the Software or a licensor product existing at release, or offers substantially similar functionality); each version additionally licensed under MIT license on the second anniversary of its release
- copyleft_detail: Usage restriction; 2-year conversion
- gpl_compatibility: Not compatible until conversion
- notable_projects: None verified for the MIT variant (Sentry, Codecov and Liquibase use FSL-1.1-ALv2)
- saas: Restricted only for competing use
- **Editorial view – build_on:** Low-moderate unless you compete with the licensor.
- **Editorial view – license_your_own:** "Fair Source" option with short conversion period.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://github.com/getsentry/fsl.software/blob/main/FSL-1.1-MIT.template.md ; https://fsl.software/ ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) ; https://opensource.org/api/licenses ; https://www.gnu.org/licenses/license-list.html | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: True

## Commons Clause (rider) — `LicenseRef-Commons-Clause`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** use_restriction
- **triggers:** ['service_offering', 'commercial_use', 'competing_use', 'distribution']
- **obligations:** ['attribution', 'no_competing_service']
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
- **triggers:** ['competing_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'patent_retaliation', 'no_competing_service']
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
- **triggers:** ['competing_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'patent_retaliation', 'no_competing_service']
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
- **triggers:** ['service_offering', 'competing_use', 'distribution']
- **obligations:** ['attribution', 'state_changes', 'no_competing_service']
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
- **triggers:** ['competing_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'same_license', 'patent_retaliation', 'no_competing_service']
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
- **triggers:** ['competing_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'same_license', 'patent_retaliation', 'no_competing_service']
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
- **triggers:** ['service_offering', 'competing_use', 'distribution']
- **obligations:** ['attribution', 'no_competing_service']
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

## Elastic License 1.0 (Elastic License Agreement, Posted Date April 20, 2018) — `LicenseRef-Elastic-1.0`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'no_production_use', 'maas_gate']
- steward_year: Elasticsearch BV (Elastic) / 2018 (Posted Date April 20, 2018)
- allows: No-charge license to use the Basic Features and Functions of the object code, solely for your internal business operations; prepare Derivative Works of the Commercial Software source for testing; keep a public copy of the repository with the Agreement included
- conditions: No reverse engineering of object code; no redistribution, sale, sublicensing or other transfer to third parties; no Prohibited SaaS Offering; no circumventing License Keys; no removing Marks and Notices; derivative works of Commercial Software may not be used in production; ends automatically on breach
- copyleft_detail: Contract terms; no source-sharing duty
- gpl_compatibility: Not compatible: the Agreement bars redistribution
- notable_projects: Elasticsearch and Kibana x-pack code, 6.3 to 7.10 (alongside Apache-2.0 for the rest of each repository)
- saas: Restricted: no SaaS where access to the Elastic Software or its features is a primary reason or substantial motivation for users
- notes: "Commercial Software" is source in files with an Elastic License header or in the x-pack folder. Elastic may modify the Agreement, effective on the new Posted Date. Elasticsearch and Kibana 7.11 and later moved to SSPL-1.0 OR Elastic-2.0.
- **Editorial view – build_on:** Fine for running the Basic features internally. Do not redistribute it, run modified x-pack code in production, or offer it as a hosted service without Elastic's permission. The OSS builds ("-oss" artifacts, Apache-2.0) avoid these terms.
- **Editorial view – license_your_own:** Not a model to copy: it is a vendor agreement with Dutch governing law and no redistribution rights.
- **Editorial view – jurisdiction:** Netherlands: Dutch law; Amsterdam courts (section 5); verify locally
- provenance: https://github.com/elastic/elasticsearch/blob/v7.10.2/licenses/ELASTIC-LICENSE.txt ; https://github.com/elastic/elasticsearch/blob/v6.3.0/LICENSE.txt ; https://github.com/elastic/elasticsearch/blob/v7.11.0/LICENSE.txt ; https://github.com/elastic/kibana/blob/v6.3.0/LICENSE.txt ; https://github.com/elastic/kibana/blob/v7.10.2/licenses/ELASTIC-LICENSE.txt ; https://opensource.org/api/licenses ; https://web.archive.org/web/20261118021016/https://www.gnu.org/licenses/license-list.html (Wayback capture, Nov. 18, 2026; gnu.org timed out) ; https://spdx.org/licenses/ (list 3.29.0; no Elastic-1.0 ID) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Functional Source License, Version 1.0, Apache 2.0 Change License — `LicenseRef-FSL-1.0-Apache-2.0`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['competing_use', 'service_offering', 'distribution']
- **obligations:** ['attribution', 'no_competing_service', 'patent_retaliation']
- steward_year: Functional Software, Inc. dba Sentry / 2023 (first in Sentry 23.11.1, Nov. 2023)
- allows: Use, copy, modify, create derivative works, publicly perform and display, and redistribute for any Permitted Purpose
- conditions: No Competing Use: use in or for a commercial product or service that competes with the Software or another licensor product, including as a substitute, in a way that exposes the Software's APIs, or with substantially similar functionality. Internal use, non-commercial education and research, and development or managed services for a licensee are permitted. Redistributions must include a copy of or link to the terms and keep copyright notices. On the second anniversary of release the Software becomes available under Apache-2.0
- copyleft_detail: Usage restriction; 2-year change to Apache-2.0
- gpl_compatibility: Not compatible until the change date; Apache-2.0 is then compatible with GPLv3 (FSF)
- notable_projects: Sentry 23.11.1 to 24.2.0 (24.3.0 moved to FSL 1.1)
- saas: Restricted only for competing use; managed services for a licensee are a Permitted Purpose
- notes: Differs from FSL-1.1-ALv2: 1.0 names exposing the Software's APIs as a Competing Use, and its change clause says the Software "will become available" under Apache-2.0, while 1.1 grants an irrevocable future Apache-2.0 license.
- **Editorial view – build_on:** Low to moderate unless your product competes with Sentry. Each release becomes Apache-2.0 two years after it was made available.
- **Editorial view – license_your_own:** Use FSL-1.1-ALv2 instead; 1.0 is superseded and its change clause is a statement rather than an express grant.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://github.com/getsentry/sentry/blob/23.11.1/LICENSE.md ; https://github.com/getsentry/sentry/blob/24.2.0/LICENSE.md ; https://github.com/getsentry/sentry/blob/24.3.0/LICENSE.md ; https://opensource.org/api/licenses ; https://web.archive.org/web/20261118021016/https://www.gnu.org/licenses/license-list.html (Wayback capture, Nov. 18, 2026; gnu.org timed out) ; https://spdx.org/licenses/ (list 3.29.0; lists FSL-1.1-ALv2 and FSL-1.1-MIT, not FSL 1.0) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## n8n Sustainable Use License 1.0 — `LicenseRef-n8n-Sustainable-Use-1.0`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'commercial_use']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'maas_gate']
- steward_year: n8n / 2022 (commit 521cf51e, Mar. 17, 2022; first in n8n 0.169.0)
- allows: Use, copy, distribute, make available and prepare derivative works, within the limitations
- conditions: Use or modify only for your own internal business purposes or for non-commercial or personal use; distribute or provide it to others only free of charge for non-commercial purposes; keep all notices; give recipients a copy of the terms; mark modified copies
- copyleft_detail: Usage restriction
- gpl_compatibility: Not compatible
- notable_projects: n8n (0.169 and later)
- saas: Restricted: providing n8n to others is allowed only free of charge for non-commercial purposes
- notes: Internal business use, including commercial companies running workflows for themselves, is within the grant. Before 0.169 n8n used Apache-2.0 with the Commons Clause.
- **Editorial view – build_on:** Fine for running n8n inside your own business. Offering it to customers, hosting it for others commercially, or reselling it needs a separate license from n8n.
- **Editorial view – license_your_own:** A short vendor-protective license; not open source.
- **Editorial view – jurisdiction:** No governing-law clause in the text; verify locally
- provenance: https://github.com/n8n-io/n8n/blob/n8n@3.3.0/LICENSE.md ; https://github.com/n8n-io/n8n/blob/n8n@0.169.0/LICENSE.md ; https://github.com/n8n-io/n8n/blob/n8n@0.168.0/LICENSE.md ; https://github.com/n8n-io/n8n/commit/521cf51e7cfb73ad60650b72206083d4c2666d29 ; https://opensource.org/api/licenses ; https://web.archive.org/web/20261118021016/https://www.gnu.org/licenses/license-list.html (Wayback capture, Nov. 18, 2026; gnu.org timed out) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## CockroachDB Software License — `LicenseRef-CockroachDB-Software-License`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** contract
- **triggers:** ['any_use', 'distribution']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'no_production_use']
- steward_year: Cockroach Labs, Inc. / 2024 (first in v24.3.0, Nov. 2024; v24.2.0 was BUSL-1.1)
- allows: Use, copy and distribute the Software and create Modified Versions (not other derivative works), for operating, evaluating, testing, fixing, integrating with and improving CockroachDB
- conditions: No operation without a License Key except Limited Non-Production Use (single node, or an introductory period, in development or testing); Telemetry must be shared unless your License Key allows disabling it; do not circumvent Protective Measures and keep them in Modified Versions; keep notices, pass on the Agreement and mark modifications; benchmark disclosures must include replication details, and Cockroach Labs may benchmark your products; 15-day cure period, otherwise termination
- copyleft_detail: Contract terms; Modified Versions keep the Protective Measures
- gpl_compatibility: Not compatible
- notable_projects: CockroachDB 24.3 and later
- saas: Production use, including services built on it, needs a License Key from Cockroach Labs
- notes: The License Key terms (who qualifies, on what conditions) are set outside this text.
- **Editorial view – build_on:** Treat it like a commercial license: production use depends on a License Key and on Telemetry rules that sit outside the open text. Development on a single node is allowed. Releases through 24.2 remain under BUSL-1.1 and convert on their Change Dates.
- **Editorial view – license_your_own:** Not a model to copy: key-gated and telemetry-dependent.
- **Editorial view – jurisdiction:** New York law; state and federal courts in New York County, New York (exclusive); verify locally
- provenance: https://github.com/cockroachdb/cockroach/blob/v26.2.12/LICENSE ; https://github.com/cockroachdb/cockroach/blob/v24.3.0/LICENSE ; https://github.com/cockroachdb/cockroach/blob/v24.2.0/LICENSE ; https://opensource.org/api/licenses ; https://web.archive.org/web/20261118021016/https://www.gnu.org/licenses/license-list.html (Wayback capture, Nov. 18, 2026; gnu.org timed out) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

