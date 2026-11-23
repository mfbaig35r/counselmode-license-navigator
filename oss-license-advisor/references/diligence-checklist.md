# Diligence checklist (editorial view)

| # | Diligence / compliance item | Why it matters | Evidence to request |
|---|---|---|---|
| 1 | Software Bill of Materials (SBOM) for each product/release | Baseline inventory of all OSS components and licenses | SPDX or CycloneDX SBOM; scan reports (Black Duck, FOSSA, Snyk, Mend) |
| 2 | Copyleft components in distributed products | GPL/LGPL/AGPL can require source release of proprietary code | Component list filtered by family; architecture diagrams showing linking |
| 3 | AGPL / SSPL components in SaaS stack | Network-trigger obligations or service restrictions | Hosting architecture; modification records |
| 4 | Source-available dependencies | Vendor relicensing risk; competing-use restrictions | List of BUSL/ELv2/SSPL/RSAL dependencies and versions |
| 5 | Attribution / NOTICE compliance | Even permissive licenses require notices | Third-party notices file, About screens |
| 6 | Source-code offers and GPL compliance records | Required for GPL device distribution | Written offers, source distribution portal |
| 7 | OSS policy and approval process | Shows control environment | Written OSS policy, approval logs |
| 8 | Contributor License Agreements / DCO | Determines ability to relicense target's own OSS | CLA records, repository policies |
| 9 | Outbound OSS released by target | Confirms ownership and license choice | List of public repos and licenses |
| 10 | AI model register | Model license thresholds (MAU/revenue) may be crossed post-closing | Models, versions, licenses, uses, AUP compliance |
| 11 | AI coding assistant usage | Potential verbatim reproduction of licensed code | Tooling policies, filters enabled, vendor indemnities |
| 12 | Training data licenses | Dataset license restrictions (NC, SA) affect models | Data cards, dataset licenses, provenance |
| 13 | Open-source litigation / demand letters | Prior enforcement history | Correspondence with SFC, FSF, vendors |
| 14 | Export controls on encryption / AI | Some OSS and models subject to export rules | ECCN classifications |
| 15 | Reps & warranties and remediation | Allocate OSS risk in SPA | OSS rep, special indemnity, pre-closing remediation covenants |
