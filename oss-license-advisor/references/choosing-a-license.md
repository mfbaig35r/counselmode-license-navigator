# Choosing an outbound license (editorial view)

Generated from data/choosing.json; the choose_license tool also checks each one against code you include.

| Your goal | Recommended license(s) | Why | Trade-offs |
|---|---|---|---|
| Maximum adoption, including by companies | MIT or Apache-2.0 | Minimal friction; Apache-2.0 adds an express patent grant and contribution terms | Others can build proprietary forks without giving back |
| Maximum adoption + patent protection | Apache-2.0 | Patent grant and patent-retaliation clause | Incompatible with GPLv2-only projects |
| Keep your library improvements open, allow proprietary apps to use it | MPL-2.0 or LGPL-3.0-or-later | File/library-level copyleft | LGPL relinking requirements can deter mobile/embedded use; MPL is simpler |
| Ensure all derivative distributions remain open | GPL-3.0-or-later | Strong copyleft with patent and anti-tivoization terms | Many companies avoid embedding GPL code |
| Prevent cloud providers from offering your software as a service without contributing | AGPL-3.0-or-later; not open source: SSPL-1.0, Elastic-2.0, BUSL-1.1, FSL-1.1-ALv2 | AGPL stays open source; source-available gives stronger protection but is not open source | AGPL reduces enterprise adoption; source-available triggers community backlash and forks |
| Monetize with dual licensing | GPL-3.0-or-later or AGPL-3.0-or-later | Copyleft pushes commercial users to buy a license | Contributors must sign a CLA so you can relicense their work; community friction |
| Dedicate to public domain | 0BSD or MIT-0 or Unlicense or CC0-1.0 | Legally robust public-domain equivalents | No attribution; CC0 excludes patents |
| Release model weights openly | Apache-2.0 or MIT; not open source: LicenseRef-BigScience-OpenRAIL-M | Clear rights encourage adoption | Use-restricted licenses are not open source |
| Release a dataset | CC-BY-4.0 or CDLA-Permissive-2.0 or CC0-1.0 | Clear rights for training and reuse | Share-alike data licenses (ODbL, CC-BY-SA) complicate downstream use |
