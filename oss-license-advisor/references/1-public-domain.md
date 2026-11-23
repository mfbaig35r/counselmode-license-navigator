# 1-Public Domain

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## Public domain (true dedication / statutory) — `LicenseRef-Public-Domain`

- **osi_status:** not_applicable
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** none
- steward_year: N/A; e.g., U.S. federal government works (17 U.S.C. §105)
- allows: Any use without permission
- conditions: None; but no warranty disclaimer and moral rights may persist outside U.S.
- copyleft_detail: None
- gpl_compatibility: Compatible with everything
- notable_projects: SQLite (author dedication), many U.S. government codebases
- saas: No obligations
- notes: Patents are NOT waived. Some companies require a separate license (e.g., SQLite sells a "warranty of title").
- **Editorial view – build_on:** Lowest risk. Confirm the dedication is valid in your jurisdiction (some civil-law countries do not allow full waiver). Third-party contributions may not be PD.
- **Editorial view – license_your_own:** Not recommended for new projects: use CC0/Unlicense/0BSD for a legally robust fallback.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## Creative Commons Zero 1.0 — `CC0-1.0`

- **osi_status:** withdrawn
- **fsf_status:** free
- **patent_grant:** excluded
- **copyleft_scope:** none
- steward_year: Creative Commons / 2009
- allows: Waives all copyright and related rights to extent possible; fallback permissive license
- conditions: None
- copyleft_detail: None
- gpl_compatibility: Compatible with GPL
- notable_projects: Many datasets, Wikidata, some libraries
- saas: No obligations
- notes: Widely used for data/metadata. Not OSI-approved because of patent exclusion.
- **Editorial view – build_on:** Low risk, but no patent license - weigh for code from patent-holding companies. Fedora disallows CC0 for new code due to patent clause.
- **Editorial view – license_your_own:** Good for data, docs, samples; less ideal for code (prefer 0BSD/MIT-0/Unlicense).
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## The Unlicense — `Unlicense`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** none
- steward_year: unlicense.org / 2010
- allows: PD dedication + permissive fallback
- conditions: None
- copyleft_detail: None
- gpl_compatibility: Compatible with GPL
- notable_projects: youtube-dl / yt-dlp, many small utilities
- saas: No obligations
- notes: Drafting criticized by some lawyers; works in practice.
- **Editorial view – build_on:** Low risk; some corporate policies still disfavor it due to drafting ambiguity.
- **Editorial view – license_your_own:** Simple PD option; some legal teams prefer 0BSD for clarity.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## BSD Zero Clause — `0BSD`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** none
- **obligations:** ['attribution']
- steward_year: Rob Landley / 2013 (toybox)
- allows: Use, copy, modify, distribute for any purpose, with or without fee
- conditions: None (no attribution required)
- copyleft_detail: None
- gpl_compatibility: Compatible with GPL
- notable_projects: toybox, many npm micro-packages
- saas: No obligations
- notes: Text is ISC minus the attribution requirement.
- **Editorial view – build_on:** Lowest friction permissive option.
- **Editorial view – license_your_own:** Excellent "PD-equivalent" choice for code.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## MIT No Attribution — `MIT-0`

- **osi_status:** approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** none
- steward_year: AWS & others / 2018
- allows: Same as MIT without attribution requirement
- conditions: None
- copyleft_detail: None
- gpl_compatibility: Compatible with GPL
- notable_projects: AWS code samples, SDK snippets
- saas: No obligations
- notes: Popular for documentation code.
- **Editorial view – build_on:** Lowest friction.
- **Editorial view – license_your_own:** Good for samples/snippets meant to be copy-pasted.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

## WTFPL — `WTFPL`

- **osi_status:** not_approved
- **fsf_status:** free
- **patent_grant:** none
- **copyleft_scope:** none
- steward_year: Sam Hocevar / 2004
- allows: Do anything
- conditions: None
- copyleft_detail: None
- gpl_compatibility: Compatible with GPL
- notable_projects: Assorted hobby projects
- saas: No obligations
- notes: Some enterprises ban it on policy grounds.
- **Editorial view – build_on:** Often flagged by corporate OSS policies for informality and profanity; legally permissive.
- **Editorial view – license_your_own:** Avoid for professional projects.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: False

