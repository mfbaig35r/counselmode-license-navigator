# 12-Proprietary

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## End User License Agreement (EULA) — `LicenseRef-Proprietary`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Vendor-specific
- allows: Limited right to install/use per license metric (seat, device, core)
- conditions: No reverse engineering, no redistribution, audit rights, usage limits, transfer restrictions
- copyleft_detail: N/A
- gpl_compatibility: Usually incompatible with GPL combination
- notable_projects: Windows, macOS, Adobe, Oracle Database
- saas: Hosting/outsourcing often restricted
- notes: Key M&A item: anti-assignment and change-of-control.
- **Editorial view – build_on:** Check assignment/change-of-control clauses, audit exposure, license metrics, true-up.
- **Editorial view – license_your_own:** Retain all rights; monetize via fees.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## SaaS / Terms of Service — `LicenseRef-SaaS-ToS`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- **obligations:** ['no_competing_service']
- steward_year: Vendor-specific
- allows: Access, not a copy; subscription rights
- conditions: Acceptable use, data terms, SLAs, termination
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Salesforce, OpenAI API, GitHub
- saas: N/A
- notes: API terms often restrict using outputs to build competing models.
- **Editorial view – build_on:** Check data use / AI training clauses, output ownership, indemnities (e.g., copyright indemnity for AI outputs).
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Enterprise / Master License Agreement — `LicenseRef-ELA`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Negotiated
- allows: Negotiated scope
- conditions: Negotiated
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Oracle ULA, Microsoft EA, SAP
- saas: Negotiated
- **Editorial view – build_on:** Check transferability on M&A; ULA certification timing.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## OEM / Embedded Distribution License — `LicenseRef-OEM`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** varies
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Negotiated
- allows: Bundle and redistribute vendor software in your product
- conditions: Royalties, territory, branding
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Codecs, embedded OS, fonts
- saas: N/A
- **Editorial view – build_on:** Check sublicensing scope and royalty reporting.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Freeware — `LicenseRef-Freeware`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- **obligations:** ['noncommercial_only']
- steward_year: Vendor-specific
- allows: Use at no cost
- conditions: Usually no modification, no redistribution, sometimes noncommercial only
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Many utilities
- saas: N/A
- **Editorial view – build_on:** "Free" price is not "free" license - check commercial-use restrictions.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Shareware / Trialware — `LicenseRef-Shareware`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Vendor-specific
- allows: Time- or feature-limited trial
- conditions: Payment after trial
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: WinRAR
- saas: N/A
- **Editorial view – build_on:** Compliance risk if trials used in production.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Dual licensing (GPL/AGPL + commercial) — `LicenseRef-Dual-Licensing`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** varies
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Vendor
- allows: Choose OSS terms or buy commercial terms
- conditions: Under OSS option: full copyleft; under commercial: negotiated
- copyleft_detail: Depends on option
- gpl_compatibility: Depends on option
- notable_projects: MySQL, Qt, iText, Ghostscript, MongoDB (pre-2018)
- saas: Depends
- notes: Popular open-core business model.
- **Editorial view – build_on:** Common way to avoid copyleft: buy commercial license. Verify which option you are actually using.
- **Editorial view – license_your_own:** Requires CLA/copyright assignment from contributors so vendor can relicense.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Unlicensed code (no LICENSE file) — `NOASSERTION`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: N/A
- allows: Nothing beyond viewing (and GitHub ToS forking)
- conditions: All rights reserved by default
- copyleft_detail: N/A
- gpl_compatibility: Not compatible
- notable_projects: Many public GitHub repos
- saas: N/A
- notes: Public visibility does not grant a license.
- **Editorial view – build_on:** HIGH: copying without license is infringement. Ask author to add a license.
- **Editorial view – license_your_own:** Always add a LICENSE file.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Trade secret / internal code — `LicenseRef-Trade-Secret`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: N/A
- allows: No public rights
- conditions: Confidentiality, NDAs, access controls
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Proprietary algorithms, model weights kept closed
- saas: N/A
- **Editorial view – build_on:** Diligence: confirm employee/contractor IP assignments and confidentiality.
- **Editorial view – license_your_own:** Protection lost if disclosed.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Docker Desktop Subscription Service Agreement — `LicenseRef-Docker-Desktop`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Docker, Inc. / 2021 change
- allows: Free for personal use, education, noncommercial OSS and small businesses (fewer than 250 employees AND less than US$10M annual revenue - verify current thresholds)
- conditions: Larger organizations need a paid subscription (Pro/Team/Business)
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Docker Desktop (Docker Engine/CLI itself is Apache-2.0)
- saas: N/A
- notes: Distinguish Docker Desktop (proprietary) from Docker Engine / Moby (Apache-2.0).
- **Editorial view – build_on:** Common audit finding in diligence: employee installs at larger companies; threshold measured at organization level.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: From prior knowledge; thresholds change - verify vendor terms before reliance | verification: Not re-verified | last_verified: None | volatile: True

## Anaconda Terms of Service — `LicenseRef-Anaconda-ToS`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Anaconda, Inc. / 2020, revised 2024
- allows: Free use of Anaconda Distribution and default package channels for individuals and small organizations (threshold: fewer than 200 employees - verify)
- conditions: Larger organizations need a paid license; applies to default repository access, not to conda-forge packages
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Anaconda Distribution, repo.anaconda.com defaults channel
- saas: N/A
- notes: Package licenses (mostly OSS) differ from repository ToS.
- **Editorial view – build_on:** Audit exposure; Anaconda has pursued enterprise compliance. Mitigate by using conda-forge / Miniforge.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: From prior knowledge; thresholds change - verify vendor terms before reliance | verification: Not re-verified | last_verified: None | volatile: True

## Oracle Java SE (OTN / Java SE Universal Subscription) [LicenseRef-Oracle-OTN] — `LicenseRef-Oracle-OTN`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Oracle / 2019 OTN; 2021 NFTC; 2023 per-employee pricing
- allows: Oracle JDK free for development/personal use under OTN; NFTC allows free production use of recent LTS releases for a limited period (verify per version)
- conditions: Commercial production use of Oracle JDK builds outside NFTC requires Java SE Universal Subscription, priced per total employee count (since Jan. 2023)
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Oracle JDK 8/11/17/21 builds
- saas: N/A
- notes: OpenJDK itself is GPL-2.0 WITH Classpath-exception-2.0.
- **Editorial view – build_on:** HIGH audit exposure: Oracle actively audits; per-employee metric scales with acquirer headcount. Mitigate by using OpenJDK builds (Temurin, Corretto, Zulu).
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: From prior knowledge; thresholds change - verify vendor terms before reliance | verification: Not re-verified | last_verified: None | volatile: True

## Oracle Java SE (OTN / Java SE Universal Subscription) [LicenseRef-Oracle-NFTC] — `LicenseRef-Oracle-NFTC`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** contract
- **triggers:** ['any_use']
- steward_year: Oracle / 2019 OTN; 2021 NFTC; 2023 per-employee pricing
- allows: Oracle JDK free for development/personal use under OTN; NFTC allows free production use of recent LTS releases for a limited period (verify per version)
- conditions: Commercial production use of Oracle JDK builds outside NFTC requires Java SE Universal Subscription, priced per total employee count (since Jan. 2023)
- copyleft_detail: N/A
- gpl_compatibility: N/A
- notable_projects: Oracle JDK 8/11/17/21 builds
- saas: N/A
- notes: OpenJDK itself is GPL-2.0 WITH Classpath-exception-2.0.
- **Editorial view – build_on:** HIGH audit exposure: Oracle actively audits; per-employee metric scales with acquirer headcount. Mitigate by using OpenJDK builds (Temurin, Corretto, Zulu).
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: From prior knowledge; thresholds change - verify vendor terms before reliance | verification: Not re-verified | last_verified: None | volatile: True

