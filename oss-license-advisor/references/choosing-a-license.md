# Choosing an outbound license (editorial view)

| Your goal | Recommended license(s) | Why | Trade-offs |
|---|---|---|---|
| Maximum adoption, including by companies | MIT or Apache-2.0 | Minimal friction; Apache-2.0 adds express patent grant and contribution terms | Others can build proprietary forks without giving back |
| Maximum adoption + patent protection | Apache-2.0 | Patent grant and patent-retaliation clause | Incompatible with GPLv2-only projects |
| Keep your library improvements open, allow proprietary apps to use it | MPL-2.0 or LGPL-3.0 | File/library-level copyleft | LGPL relinking requirements can deter mobile/embedded use; MPL is simpler |
| Ensure all derivative distributions remain open | GPL-3.0-or-later | Strong copyleft with patent and anti-tivoization terms | Many companies avoid embedding GPL code |
| Prevent cloud providers from offering your software as a service without contributing | AGPL-3.0 (OSI) or source-available (SSPL/ELv2/BUSL/FSL) | AGPL stays open source; source-available gives stronger protection but is not open source | AGPL reduces enterprise adoption; source-available triggers community backlash and forks |
| Monetize with dual licensing | GPL/AGPL + commercial license (require CLA) | Copyleft pushes commercial users to buy a license | Need contributor CLAs; community friction |
| Dedicate to public domain | 0BSD, MIT-0, Unlicense, or CC0 (non-code) | Legally robust PD equivalents | No attribution; CC0 excludes patents |
| Release model weights openly | Apache-2.0 or MIT (truly open); OpenRAIL if you want use restrictions | Clear rights encourage adoption | Use-restricted licenses are not open source |
| Release a dataset | CC-BY-4.0, CDLA-Permissive-2.0, or CC0 | Clear rights for training and reuse | Share-alike data licenses (ODbL, CC-BY-SA) complicate downstream use |
