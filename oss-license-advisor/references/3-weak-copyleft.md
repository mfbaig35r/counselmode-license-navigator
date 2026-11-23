# 3-Weak Copyleft

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## GNU LGPL v2.1 [LGPL-2.1-only] — `LGPL-2.1-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure', 'relinking']
- steward_year: FSF / 1999
- allows: Use library in any program, including proprietary
- conditions: Modifications to the library must be LGPL with source; distributed works must permit user modification of library and reverse engineering for debugging; provide relinking ability (shared library or object files)
- copyleft_detail: Library-level; triggered by distribution
- gpl_compatibility: Compatible with GPLv2/v3 (can convert to GPL)
- notable_projects: glibc, FFmpeg (default build), Qt (LGPL option), GTK
- saas: Not triggered by SaaS (no network clause)
- notes: Mobile app stores and static linking make compliance harder (iOS).
- **Editorial view – build_on:** Moderate. Prefer dynamic linking; static linking requires providing object files for relinking. Do not prohibit reverse engineering in your EULA for the combined work.
- **Editorial view – license_your_own:** For libraries you want widely used incl. by proprietary apps, while keeping library improvements open.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## GNU LGPL v2.1 [LGPL-2.1-or-later] — `LGPL-2.1-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure', 'relinking']
- steward_year: FSF / 1999
- allows: Use library in any program, including proprietary
- conditions: Modifications to the library must be LGPL with source; distributed works must permit user modification of library and reverse engineering for debugging; provide relinking ability (shared library or object files)
- copyleft_detail: Library-level; triggered by distribution
- gpl_compatibility: Compatible with GPLv2/v3 (can convert to GPL)
- notable_projects: glibc, FFmpeg (default build), Qt (LGPL option), GTK
- saas: Not triggered by SaaS (no network clause)
- notes: Mobile app stores and static linking make compliance harder (iOS).
- **Editorial view – build_on:** Moderate. Prefer dynamic linking; static linking requires providing object files for relinking. Do not prohibit reverse engineering in your EULA for the combined work.
- **Editorial view – license_your_own:** For libraries you want widely used incl. by proprietary apps, while keeping library improvements open.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## GNU LGPL v3 [LGPL-3.0-only] — `LGPL-3.0-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['installation_info']
- steward_year: FSF / 2007
- allows: As LGPL-2.1 (implemented as GPLv3 + additional permissions)
- conditions: As 2.1, plus GPLv3 Installation Information (anti-tivoization) for user products; patent provisions
- copyleft_detail: Library-level; distribution
- gpl_compatibility: Compatible with GPLv3; INCOMPATIBLE with GPLv2-only
- notable_projects: GNU libraries, some Qt modules
- saas: Not triggered by SaaS
- notes: Many embedded vendors avoid (L)GPLv3 due to anti-tivoization.
- **Editorial view – build_on:** Moderate-high for embedded/consumer devices: must allow users to install modified library (Installation Information).
- **Editorial view – license_your_own:** As 2.1, with modern patent terms.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## GNU LGPL v3 [LGPL-3.0-or-later] — `LGPL-3.0-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['installation_info']
- steward_year: FSF / 2007
- allows: As LGPL-2.1 (implemented as GPLv3 + additional permissions)
- conditions: As 2.1, plus GPLv3 Installation Information (anti-tivoization) for user products; patent provisions
- copyleft_detail: Library-level; distribution
- gpl_compatibility: Compatible with GPLv3; INCOMPATIBLE with GPLv2-only
- notable_projects: GNU libraries, some Qt modules
- saas: Not triggered by SaaS
- notes: Many embedded vendors avoid (L)GPLv3 due to anti-tivoization.
- **Editorial view – build_on:** Moderate-high for embedded/consumer devices: must allow users to install modified library (Installation Information).
- **Editorial view – license_your_own:** As 2.1, with modern patent terms.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Mozilla Public License 2.0 — `MPL-2.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'same_license']
- steward_year: Mozilla / 2012
- allows: Use and combine in "Larger Works" under any license
- conditions: Source of MPL-covered files (and modifications to them) must be available under MPL; keep notices
- copyleft_detail: FILE-level; distribution of executable form
- gpl_compatibility: Compatible with GPL/LGPL/AGPL via "Secondary License" (unless marked "Incompatible With Secondary Licenses")
- notable_projects: Firefox, Thunderbird, LibreOffice (MPL/LGPL), Terraform providers, OpenTofu
- saas: Not triggered by SaaS
- notes: Most business-friendly copyleft.
- **Editorial view – build_on:** Low-moderate: only modified MPL files must be published. Keep your proprietary code in separate files.
- **Editorial view – license_your_own:** Balanced choice: protects your files while allowing proprietary combination.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Mozilla Public License 1.1 — `MPL-1.1`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: Mozilla / 1999
- allows: As MPL-2.0
- conditions: File-level copyleft
- copyleft_detail: File-level
- gpl_compatibility: INCOMPATIBLE with GPL
- notable_projects: Legacy Mozilla code
- saas: Not triggered
- **Editorial view – build_on:** Moderate; GPL incompatibility.
- **Editorial view – license_your_own:** Superseded.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Eclipse Public License 2.0 — `EPL-2.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure']
- steward_year: Eclipse Foundation / 2017
- allows: Use, combine with separate modules under other licenses
- conditions: Modifications to EPL "Program" (module-level) must be EPL with source; commercial distributors indemnify contributors
- copyleft_detail: Module-level; distribution
- gpl_compatibility: GPL-compatible only if Secondary License (GPL-2.0) is designated
- notable_projects: Eclipse IDE, Jakarta EE, OpenJ9
- saas: Not triggered
- **Editorial view – build_on:** Moderate; check for Secondary License designation before mixing with GPL.
- **Editorial view – license_your_own:** Common in Java ecosystem.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Eclipse Public License 1.0 — `EPL-1.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: Eclipse / 2004
- allows: As EPL-2.0
- conditions: Module-level copyleft; choice-of-law (NY)
- copyleft_detail: Module-level
- gpl_compatibility: INCOMPATIBLE with GPL
- notable_projects: JUnit 4, Clojure
- saas: Not triggered
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Superseded by EPL-2.0.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Common Development and Distribution License 1.0 — `CDDL-1.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: Sun Microsystems / 2004
- allows: MPL-style
- conditions: File-level copyleft
- copyleft_detail: File-level
- gpl_compatibility: INCOMPATIBLE with GPL
- notable_projects: OpenZFS, illumos, GlassFish
- saas: Not triggered
- notes: Ubuntu ships ZFS module; legal views differ.
- **Editorial view – build_on:** Moderate; notorious ZFS-on-Linux GPL incompatibility debate.
- **Editorial view – license_your_own:** Rarely chosen today.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Common Public License 1.0 — `CPL-1.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: IBM / 2001
- allows: Predecessor to EPL
- conditions: Module-level copyleft
- copyleft_detail: Module-level
- gpl_compatibility: Incompatible with GPL
- notable_projects: Legacy IBM projects
- saas: Not triggered
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Superseded.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Microsoft Reciprocal License — `MS-RL`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: Microsoft / 2005
- allows: Use and combine
- conditions: File-level copyleft
- copyleft_detail: File-level
- gpl_compatibility: Incompatible with GPL
- notable_projects: WiX Toolset (historic)
- saas: Not triggered
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Niche.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## CeCILL-C — `CECILL-C`

- **osi_status:** not_approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- steward_year: CEA/CNRS/Inria (France) / 2006
- allows: LGPL-like for French law
- conditions: Component-level copyleft
- copyleft_detail: Component-level
- gpl_compatibility: Compatible with LGPL-style use
- notable_projects: French public-sector projects
- saas: Not triggered
- **Editorial view – build_on:** Moderate; French law governs.
- **Editorial view – license_your_own:** Used by French institutions.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Apple Public Source License 2.0 — `APSL-2.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure', 'network_source_offer']
- steward_year: Apple / 2003
- allows: Use, modify
- conditions: File-level copyleft; "external deployment" (network) triggers source obligation
- copyleft_detail: File-level; includes external deployment
- gpl_compatibility: Incompatible with GPL
- notable_projects: Darwin / XNU components
- saas: External deployment of modified covered code triggers obligations
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** Niche.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Microsoft Public License — `MS-PL`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'same_license', 'patent_retaliation']
- steward_year: Microsoft / 2005
- allows: Use, modify, distribute
- conditions: Source distributions must be under Ms-PL; binaries under a compatible license; patent termination; keep notices
- copyleft_detail: Source-distribution level
- gpl_compatibility: INCOMPATIBLE with GPL
- notable_projects: Older .NET projects, CodePlex-era libraries
- saas: Not triggered
- notes: Sibling of Ms-RL.
- **Editorial view – build_on:** Low-moderate; GPL incompatibility.
- **Editorial view – license_your_own:** Superseded in practice by MIT/Apache.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## SIL Open Font License 1.1 — `OFL-1.1`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** file_or_library
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'naming_rule']
- steward_year: SIL International / 2007
- allows: Use, embed, modify, bundle and redistribute fonts with any software
- conditions: Fonts may not be sold standalone; modified fonts must be OFL and cannot use Reserved Font Names; keep notices
- copyleft_detail: Font-level copyleft
- gpl_compatibility: Compatible for bundling with any software (fonts are separate works)
- notable_projects: Google Fonts, Noto, Fira, Source Sans
- saas: No obligations
- notes: Appears in nearly every web/app SBOM.
- **Editorial view – build_on:** Low risk; ships in most products; do not rename/sell fonts alone.
- **Editorial view – license_your_own:** Standard for open fonts.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

