# 4-Strong Copyleft

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## GNU GPL v2.0 only — `GPL-2.0-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license']
- steward_year: FSF / 1991
- allows: Run, study, modify, distribute
- conditions: Distributing the program or "work based on the program" requires licensing the whole under GPLv2 with complete corresponding source (or written offer, 3 years); no additional restrictions
- copyleft_detail: Whole derivative/combined work; triggered by distribution
- gpl_compatibility: GPLv2 only; INCOMPATIBLE with GPLv3, Apache-2.0
- notable_projects: Linux kernel (with syscall note), Git, MySQL Community (with FOSS exception), BusyBox
- saas: Not triggered by SaaS
- notes: Kernel syscall note: user-space programs are not derivative works of the kernel. Kernel modules are a gray area (EXPORT_SYMBOL_GPL).
- **Editorial view – build_on:** HIGH if you distribute: shipping proprietary code combined/linked with GPL code can require releasing your source. Internal use and SaaS do not trigger. Termination on violation is automatic (cure under GPLv3-style commitments many projects adopted).
- **Editorial view – license_your_own:** Maximizes reciprocity; deters proprietary forks; enables dual licensing (GPL + commercial).
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/gpl-2.0.txt; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/; https://spdx.org/licenses/Linux-syscall-note.html | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: False

## GNU GPL v2.0 or later — `GPL-2.0-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** varies
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license']
- steward_year: FSF / 1991
- allows: As GPLv2, recipient may choose later versions
- conditions: As GPLv2
- copyleft_detail: Whole work; distribution
- gpl_compatibility: Compatible with GPLv3 (by choosing v3)
- notable_projects: GCC (historic), many GNU programs, WordPress
- saas: Not triggered
- **Editorial view – build_on:** As above.
- **Editorial view – license_your_own:** Gives flexibility to move to GPLv3.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/gpl-2.0.txt; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/ | verification: Partially verified (primary) | last_verified: 2026-11-23 | volatile: False

## GNU GPL v3.0 [GPL-3.0-only] — `GPL-3.0-only`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'installation_info']
- steward_year: FSF / 2007
- allows: As GPLv2
- conditions: As GPLv2 plus: Installation Information for "User Products" (anti-tivoization), anti-DRM (§3), express patent license & anti-discrimination patent deal terms (§11), 30-day cure for first violation (§8)
- copyleft_detail: Whole work; "convey" (distribution)
- gpl_compatibility: Compatible with Apache-2.0, LGPLv3, AGPLv3 (combination); INCOMPATIBLE with GPLv2-only
- notable_projects: Most GNU projects (Bash, GCC, GIMP; also Ansible, Samba) are GPL-3.0-or-later, not -only: check each project's license notice
- saas: Not triggered by SaaS (the "SaaS loophole")
- **Editorial view – build_on:** HIGH for distributed products; plus consumer-device vendors must provide keys/installation info.
- **Editorial view – license_your_own:** Strongest "distribution" copyleft with modern patent terms.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/gpl-3.0.txt; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/ | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: False

## GNU GPL v3.0 [GPL-3.0-or-later] — `GPL-3.0-or-later`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'installation_info']
- steward_year: FSF / 2007
- allows: As GPLv2
- conditions: As GPLv2 plus: Installation Information for "User Products" (anti-tivoization), anti-DRM (§3), express patent license & anti-discrimination patent deal terms (§11), 30-day cure for first violation (§8)
- copyleft_detail: Whole work; "convey" (distribution)
- gpl_compatibility: Compatible with Apache-2.0, LGPLv3, AGPLv3 (combination); INCOMPATIBLE with GPLv2-only
- notable_projects: Bash, GCC, GIMP, Ansible, Samba
- saas: Not triggered by SaaS (the "SaaS loophole")
- **Editorial view – build_on:** HIGH for distributed products; plus consumer-device vendors must provide keys/installation info.
- **Editorial view – license_your_own:** Strongest "distribution" copyleft with modern patent terms.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.gnu.org/licenses/gpl-3.0.txt; https://opensource.org/licenses; https://www.gnu.org/licenses/license-list.html; https://spdx.org/licenses/ | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: False

## European Union Public Licence 1.2 — `EUPL-1.2`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** whole_work
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer']
- steward_year: European Commission / 2017
- allows: Use, modify, distribute, communicate to public
- conditions: Derivatives under EUPL or a listed compatible license; source must be provided; covers "communication to the public" (arguably network use)
- copyleft_detail: Whole work; distribution and communication
- gpl_compatibility: Explicit compatibility list incl. GPLv2/v3, AGPLv3, MPL-2.0, EPL, LGPL, CeCILL, OSL
- notable_projects: EU public-sector software (Joinup)
- saas: Possibly triggered via "communication to the public" - interpretation varies
- notes: Some treat it as weak copyleft due to compatibility clause.
- **Editorial view – build_on:** Moderate-high; compatibility clause allows relicensing to listed licenses for combined works.
- **Editorial view – license_your_own:** Available in all 23 EU languages; designed for EU law.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Open Software License 3.0 — `OSL-3.0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** whole_work
- **triggers:** ['distribution', 'network_interaction']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license', 'network_source_offer', 'patent_retaliation']
- steward_year: L. Rosen / 2005
- allows: Use, modify, distribute
- conditions: Derivatives under OSL; "External Deployment" (network use) counts as distribution
- copyleft_detail: Whole work; distribution + network deployment
- gpl_compatibility: INCOMPATIBLE with GPL
- notable_projects: Magento 1 (historic)
- saas: TRIGGERED by external deployment
- **Editorial view – build_on:** HIGH; network trigger.
- **Editorial view – license_your_own:** Rarely chosen.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## CeCILL 2.1 — `CECILL-2.1`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** express
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'source_disclosure', 'same_license']
- steward_year: CEA/CNRS/Inria / 2013
- allows: GPL-like under French law
- conditions: Whole-work copyleft
- copyleft_detail: Whole work
- gpl_compatibility: Compatible with GPL (explicit)
- notable_projects: French research software
- saas: Not triggered
- **Editorial view – build_on:** HIGH similar to GPL.
- **Editorial view – license_your_own:** For French institutions.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Sleepycat License — `Sleepycat`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'source_disclosure']
- steward_year: Sleepycat / Oracle
- allows: Use Berkeley DB
- conditions: Source of software using Berkeley DB must be made available on distribution
- copyleft_detail: Whole application
- gpl_compatibility: Compatible with GPL
- notable_projects: Berkeley DB (pre-2013)
- saas: Not triggered
- **Editorial view – build_on:** HIGH; legacy.
- **Editorial view – license_your_own:** Superseded (BDB moved to AGPL in 2013).
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## GNU General Public License v1.0 or later — `GPL-1.0-or-later`

- **osi_status:** approved
- **fsf_status:** not_reviewed
- **patent_grant:** varies
- **copyleft_scope:** whole_work
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'state_changes', 'source_disclosure', 'same_license']
- steward_year: FSF / February 1989
- allows: Copy, distribute and modify; under section 7 a recipient may follow version 1 or any later version published by the FSF
- conditions: Keep notices and give recipients a copy of the license; mark modified files with what changed and the date; any work you distribute or publish that contains the Program must be licensed to all third parties under this license; object-code distribution must come with source, a three-year written offer, or (noncommercial only) the source information you received; interactive programs must show a copyright and no-warranty notice
- copyleft_detail: Whole work; distribution or publication
- gpl_compatibility: Compatible with GPLv2 and GPLv3 by choosing the later version (section 7)
- notable_projects: Perl 5 (as the alternative to Artistic-1.0-Perl)
- saas: Not triggered
- **Editorial view – build_on:** Treat it as strong copyleft on distribution. Because of the or-later option you can follow GPL-2.0 or GPL-3.0 instead, which is how it combines with modern GPL code. For Perl, the Artistic alternative is also available.
- **Editorial view – license_your_own:** Do not use for new work; choose GPL-3.0-or-later.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://github.com/Perl/perl5/blob/v5.44.0/Copying ; https://github.com/Perl/perl5/blob/v5.44.0/README ; https://opensource.org/license/gpl-1-0 ; https://opensource.org/api/licenses ; https://web.archive.org/web/20261118021016/https://www.gnu.org/licenses/license-list.html (Wayback capture, Nov. 18, 2026; gnu.org timed out) ; https://spdx.org/licenses/GPL-1.0-or-later.html (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: False

