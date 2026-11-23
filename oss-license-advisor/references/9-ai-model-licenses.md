# 9-AI Model Licenses

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## Llama 4 Community License — `LicenseRef-Llama-4`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution']
- **obligations:** ['attribution', 'notice_file', 'naming_rule', 'usage_policy', 'mau_revenue_cap', 'patent_retaliation']
- steward_year: Meta / Apr 2025
- allows: Use, reproduce, distribute, copy, create derivative works of, and modify the Llama Materials (grant does not cover outputs as such)
- conditions: AUP; >700M MAU on release date requires Meta license; "Built with Llama"; models trained on Llama Materials or outputs and distributed must begin with "Llama"; include Agreement copy; Notice file; EU-domiciled individuals/companies get no s.1(a) rights for multimodal models (AUP), end users of products excepted; IP-litigation termination
- copyleft_detail: Model weights & derivatives (incl. fine-tunes)
- gpl_compatibility: N/A (not OSS)
- notable_projects: Llama 4 Scout / Maverick
- saas: Hosting allowed subject to AUP and MAU threshold
- notes: Meta has since released Muse models under different licenses (Muse Glimmer: Apache-2.0; Muse Spark Open: Muse Model License; Muse Spark: proprietary). See Model Map.
- **Editorial view – build_on:** Commercial use generally allowed below MAU threshold, subject to AUP and attribution. Flow-down obligations apply when distributing fine-tunes. Verify current text and EU restriction.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.llama.com/llama4/license/ ; https://www.llama.com/llama4/use-policy/ ; https://www.gnu.org/licenses/license-list.html ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Llama 3.x Community License (3, 3.1, 3.2, 3.3) — `LicenseRef-Llama-3.x`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution']
- **obligations:** ['attribution', 'notice_file', 'naming_rule', 'usage_policy', 'mau_revenue_cap', 'patent_retaliation']
- steward_year: Meta / 2024
- allows: As above; 3.1+ expressly allows using outputs to improve other models (with naming rule)
- conditions: 700M MAU; AUP; Llama 3: "Built with Meta Llama 3", derivative names begin "Llama 3", no use of outputs to improve other LLMs; 3.1-3.3: "Built with Llama", names begin "Llama"; Notice file; 3.2 multimodal: no s.1(a) rights for EU-domiciled individuals/companies (AUP), end users excepted
- copyleft_detail: Weights & derivatives
- gpl_compatibility: N/A
- notable_projects: Llama 3.1 8B/70B/405B, Llama 3.2, Llama 3.3 70B
- saas: Allowed subject to AUP
- notes: Version-specific: keep a register of exact model + license version.
- **Editorial view – build_on:** As above; Llama 3 (pre-3.1) prohibited using outputs to improve other LLMs.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://www.llama.com/llama3/license/ ; https://www.llama.com/llama3_1/license/ ; https://www.llama.com/llama3_2/license/ ; https://www.llama.com/llama3_3/license/ ; https://www.llama.com/llama3_2/use-policy/ ; https://www.gnu.org/licenses/license-list.html ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Llama 2 Community License — `LicenseRef-Llama-2`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution']
- **obligations:** ['attribution', 'notice_file', 'usage_policy', 'mau_revenue_cap', 'patent_retaliation']
- steward_year: Meta / Jul 2023
- allows: Use, distribute, derive
- conditions: 700M MAU threshold; AUP; no using outputs to improve other LLMs (excluding Llama derivatives)
- copyleft_detail: Weights & derivatives
- gpl_compatibility: N/A
- notable_projects: Llama 2 and many fine-tunes (e.g., early Vicuna variants)
- saas: Allowed subject to AUP
- **Editorial view – build_on:** As above; output restriction matters for distillation.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Gemma Terms of Use (models listed in its Appendix only) — `LicenseRef-Gemma`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['prohibited_use', 'distribution', 'service_offering']
- **obligations:** ['attribution', 'notice_file', 'state_changes', 'usage_policy']
- steward_year: Google / 2024 (current text last modified Apr. 1, 2026)
- allows: Use, reproduce, modify, distribute Gemma models and "Model Derivatives" (incl. distilled models)
- conditions: Gemma Prohibited Use Policy (flows down); must pass on terms; Google may restrict use it reasonably believes violates terms; notices
- copyleft_detail: Weights, derivatives, and models trained on outputs (distillation)
- gpl_compatibility: N/A
- notable_projects: Models in the ToU Appendix (Gemma 1/1.1/2/3/3n, CodeGemma, PaliGemma 1/2, ShieldGemma 1/2, RecurrentGemma, EmbeddingGemma, T5Gemma 1/2, VaultGemma, FunctionGemma, TranslateGemma, DataGemma, Gemma Scope, Gemma-APS). NOT Gemma 4 or EmbeddingGemma 2 (Apache-2.0)
- saas: Allowed; hosting counts as Distribution, so s.3.1 flow-down conditions apply (Notice file exempt for hosted)
- notes: Per-version mapping required: Gemma 4 is the first Gemma family released under OSI-approved Apache-2.0. See Model Map.
- **Editorial view – build_on:** Commercial use allowed; no MAU cap, but flow-down and remote-restriction clauses are notable diligence items.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://ai.google.dev/gemma/terms ; https://ai.google.dev/gemma/prohibited_use_policy ; https://ai.google.dev/gemma/docs/releases ; https://ai.google.dev/gemma/docs/gemma_4_license ; https://www.gnu.org/licenses/license-list.html ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## CreativeML OpenRAIL-M — `LicenseRef-CreativeML-OpenRAIL-M`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'prohibited_use']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'usage_policy']
- steward_year: RAIL / Stability AI & CompVis / 2022
- allows: Use, share, modify model; commercial use allowed
- conditions: Attachment A use-based restrictions must be included in downstream licenses; outputs owned by user
- copyleft_detail: Use restrictions flow down
- gpl_compatibility: N/A
- notable_projects: Stable Diffusion 1.x / 2.x
- saas: Allowed subject to restrictions
- **Editorial view – build_on:** Moderate: flow-down use restrictions; commercial OK.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## BigScience OpenRAIL-M / RAIL 1.0 [BigScience-OpenRAIL-M] — `LicenseRef-BigScience-OpenRAIL-M`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'prohibited_use']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'usage_policy']
- steward_year: BigScience / 2022
- allows: As OpenRAIL-M
- conditions: Use-based restrictions flow down
- copyleft_detail: Use restrictions flow down
- gpl_compatibility: N/A
- notable_projects: BLOOM, StarCoder (BigCode OpenRAIL-M)
- saas: Allowed subject to restrictions
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** RAIL family is a template for "responsible" licenses.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## BigScience OpenRAIL-M / RAIL 1.0 [BigScience-BLOOM-RAIL-1.0] — `LicenseRef-BigScience-BLOOM-RAIL-1.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'prohibited_use']
- **obligations:** ['attribution', 'state_changes', 'patent_retaliation', 'usage_policy']
- steward_year: BigScience / 2022
- allows: As OpenRAIL-M
- conditions: Use-based restrictions flow down
- copyleft_detail: Use restrictions flow down
- gpl_compatibility: N/A
- notable_projects: BLOOM, StarCoder (BigCode OpenRAIL-M)
- saas: Allowed subject to restrictions
- **Editorial view – build_on:** Moderate.
- **Editorial view – license_your_own:** RAIL family is a template for "responsible" licenses.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Stability AI Community License — `LicenseRef-Stability-Community`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution', 'service_offering', 'commercial_use']
- **obligations:** ['attribution', 'notice_file', 'state_changes', 'naming_rule', 'usage_policy', 'mau_revenue_cap', 'patent_retaliation']
- steward_year: Stability AI / 2024
- allows: Free research, noncommercial, and commercial use for orgs < US$1M annual revenue
- conditions: Enterprise license required above revenue threshold; AUP
- copyleft_detail: Revenue-based restriction
- gpl_compatibility: N/A
- notable_projects: Stable Diffusion 3/3.5, Stable Video, others
- saas: Restricted above threshold
- **Editorial view – build_on:** Size threshold = growth/M&A trigger; check acquirer revenue.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Tongyi Qianwen / earlier Qwen licenses — `LicenseRef-Qwen`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution', 'commercial_use']
- **obligations:** ['attribution', 'notice_file', 'state_changes', 'mau_revenue_cap', 'naming_rule', 'patent_retaliation']
- steward_year: Alibaba Cloud / 2023-2024
- allows: Use, modify, distribute
- conditions: Large Qwen models carry custom licenses with commercial thresholds and separate-license requirements for Model-as-a-Service (e.g., Qwen3.8-Max License, Qwen Community License 1.0); smaller models (e.g., Qwen3.8-27B) are Apache-2.0. Verify per model.
- copyleft_detail: Weights & derivatives
- gpl_compatibility: N/A
- notable_projects: Some Qwen 1.x/2.x large variants (many Qwen2.5 and Qwen3 models are Apache-2.0)
- saas: Allowed subject to terms
- notes: Per-model variance.
- **Editorial view – build_on:** Check per model card - Qwen licensing varies by size and version.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE; other Qwen licenses secondary | verification: Secondary only | last_verified: 2026-11-18 | volatile: True

## DeepSeek License Agreement — `LicenseRef-DeepSeek`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['prohibited_use', 'distribution', 'service_offering']
- **obligations:** ['attribution', 'state_changes', 'usage_policy', 'patent_retaliation']
- steward_year: DeepSeek / Oct. 23, 2023 (v1.0)
- allows: Use, modify, distribute, commercial use
- conditions: Attachment A use restrictions (incl. any military use, fully automated decisions adversely affecting legal rights) flow down as enforceable terms; copy of License to recipients; modified-file notices; retain notices; DeepSeek may restrict use remotely
- copyleft_detail: Use restrictions flow down
- gpl_compatibility: N/A
- notable_projects: Original DeepSeek-V3 Base/Chat (Dec. 26, 2024), DeepSeek-V2/V2.5, Coder, Coder-V2, VL2 weights (code under MIT). DeepSeek-R1 (Jan. 20, 2025), V3-0324 (Mar. 2025) and later V3.x/V4.x weights are MIT, not this license.
- saas: Allowed
- notes: Verify each repo.
- **Editorial view – build_on:** Checkpoint-dependent: original V3 weights remain under DeepSeek License Agreement v1.0 (Oct. 23, 2023) with Attachment A use restrictions that must flow down; later checkpoints do not change that retroactively.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL ; https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README.md ; https://api-docs.deepseek.com/news/news250120 ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Mistral AI Research License (MRL-0.1) — `LicenseRef-MRL`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['commercial_use', 'distribution']
- **obligations:** ['noncommercial_only', 'notice_file', 'state_changes', 'patent_retaliation']
- steward_year: Mistral AI / 2024
- allows: Research Purposes only: personal, scientific or academic research that is non-profit and non-commercial; applies to Models, Derivatives and Outputs
- conditions: No production/commercial use without commercial license
- copyleft_detail: Purpose restriction
- gpl_compatibility: N/A
- notable_projects: MNPL: Codestral 22B v0.1 (May 29, 2024). MRL: Mistral Large 2 (2407) and 2.1 (2411), Mistral Small 2409, Ministral 8B 2410, Pixtral Large 2411. Mistral regimes now include Apache-2.0, Modified MIT, Mistral Ecosystem Open-Weight License (Mistral Large 4), MRL/MNPL, and API-only models
- saas: Restricted
- notes: "Mistral = Apache" is not a safe rule; map each model version.
- **Editorial view – build_on:** Do not ship MRL/MNPL models in products.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://mistral.ai/licenses/MRL-0.1.md ; https://docs.mistral.ai/getting-started/models/ ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Mistral AI Non-Production License (MNPL-0.1) — `LicenseRef-MNPL`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['commercial_use', 'distribution']
- **obligations:** ['noncommercial_only', 'notice_file', 'state_changes', 'patent_retaliation', 'no_production_use']
- steward_year: Mistral AI / 2024
- allows: Testing, research, Personal or evaluation purposes in Non-Production Environments; no supply in the course of commercial activity (incl. SaaS)
- conditions: No production/commercial use without commercial license
- copyleft_detail: Purpose restriction
- gpl_compatibility: N/A
- notable_projects: MNPL: Codestral 22B v0.1 (May 29, 2024). MRL: Mistral Large 2 (2407) and 2.1 (2411), Mistral Small 2409, Ministral 8B 2410, Pixtral Large 2411. Mistral regimes now include Apache-2.0, Modified MIT, Mistral Ecosystem Open-Weight License (Mistral Large 4), MRL/MNPL, and API-only models
- saas: Restricted
- notes: "Mistral = Apache" is not a safe rule; map each model version.
- **Editorial view – build_on:** Do not ship MRL/MNPL models in products.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://mistral.ai/licences/MNPL-0.1.md ; https://docs.mistral.ai/getting-started/models/ ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## Falcon / TII Falcon License — `LicenseRef-Falcon`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'prohibited_use']
- **obligations:** ['attribution', 'notice_file', 'state_changes', 'naming_rule', 'usage_policy', 'maas_gate', 'patent_retaliation']
- steward_year: TII / 2023-2024
- allows: Use and distribute
- conditions: Acceptable use policy; hosting-use restrictions for some versions (Falcon 180B)
- copyleft_detail: Varies
- gpl_compatibility: N/A
- notable_projects: Falcon 180B (Falcon 7B/40B are Apache-2.0)
- saas: Restricted for Falcon 180B hosting
- **Editorial view – build_on:** Verify version.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: Hand-compiled Nov. 2026 | verification: Not re-verified | last_verified: None | volatile: True

## Muse Model License (Muse Spark Open) — `LicenseRef-Meta-Muse-Model-License`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'prohibited_use', 'distribution', 'service_offering']
- **obligations:** ['attribution', 'naming_rule', 'usage_policy', 'maas_gate', 'mau_revenue_cap']
- steward_year: Meta / Oct. 15, 2026
- allows: MIT-style grant: use, copy, modify (incl. fine-tune), create derivatives, distill, merge, distribute, sublicense, sell
- conditions: Include notice, license and Usage Policy; comply with Usage Policy; display "Built with Muse Spark Open"; Model-as-a-Service operators whose licensee + affiliates aggregate gross revenue exceeds US$20M in any 12 months must notify Meta and sign a separate agreement; Meta claims no ownership of outputs
- copyleft_detail: Weights & Derivatives (defined to include models trained or distilled on outputs)
- gpl_compatibility: N/A (not OSS)
- notable_projects: Muse Spark Open 816B-A42B
- saas: MaaS above US$20M revenue requires Meta agreement
- notes: "Derivatives" includes models improved using outputs: distillation is caught.
- **Editorial view – build_on:** Internal use, research and use as a component of your own (non-MaaS) product are carved out of the MaaS clause; attribution applies broadly.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/blob/main/LICENSE.md | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Kimi K2 Modified MIT License — `LicenseRef-Moonshot-Modified-MIT`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'threshold', 'commercial_use']
- **obligations:** ['attribution', 'naming_rule']
- steward_year: Moonshot AI / 2025
- allows: Standard MIT grant
- conditions: MIT notice; if used in commercial products/services with >100M MAU or >US$20M monthly revenue, prominently display "Kimi K2" in the UI
- copyleft_detail: None (attribution only)
- gpl_compatibility: N/A
- notable_projects: Kimi K2, K2-Instruct-0905, K2-Thinking, K2.5
- saas: Attribution at scale
- notes: Template ("modified MIT") copied by other vendors with different conditions - always read the appended paragraph.
- **Editorial view – build_on:** Attribution-only modification; MIT grant continues at any scale.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Kimi K3 License — `LicenseRef-Moonshot-Kimi-K3`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'threshold', 'commercial_use']
- **obligations:** ['attribution', 'maas_gate', 'mau_revenue_cap', 'naming_rule']
- steward_year: Moonshot AI / July 2026
- allows: Broad MIT-style grant over weights, code and docs
- conditions: Notice + compliance with law as a condition; MaaS operators (licensee + affiliates) above US$20M aggregate revenue in any 12 months need a separate Moonshot agreement before any commercial use; "Kimi K3" display above 100M MAU or US$20M monthly revenue; exemptions for internal use and use via Moonshot official products/certified partners
- copyleft_detail: Commercial-use gate for MaaS
- gpl_compatibility: N/A
- notable_projects: Kimi K3
- saas: MaaS gate
- notes: Group-level (affiliate) revenue test - M&A trigger.
- **Editorial view – build_on:** Not MIT despite early reporting. SaaS products embedding the model in features are outside the MaaS definition; inference hosts are inside.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Mistral Modified MIT License — `LicenseRef-Mistral-Modified-MIT`

- **osi_status:** not_approved
- **fsf_status:** not_reviewed
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['threshold', 'distribution']
- **obligations:** ['attribution', 'mau_revenue_cap']
- steward_year: Mistral AI / Dec. 2025
- allows: MIT-style grant
- conditions: No rights at all if global consolidated monthly revenue of your company (or your employer) exceeds US$20M for the preceding month; applies to derivatives and combined works; above threshold use Mistral commercial license or hosted service
- copyleft_detail: Revenue-based bar on all use (incl. internal)
- gpl_compatibility: N/A
- notable_projects: Devstral 2 123B (API deprecated May 22, 2026, retired Jul. 31, 2026; weights remain), Mistral Medium 3.5 (API deprecated Oct. 31, 2026, retires Apr. 30, 2027), Timestral 1.0 (5M-209M)
- saas: Barred above threshold
- notes: Unlike Kimi/Muse thresholds, this is not limited to MaaS.
- **Editorial view – build_on:** HIGH for larger groups: the bar covers internal use and is measured on consolidated group revenue - an acquisition can terminate rights overnight.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512/blob/main/LICENSE ; https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE ; https://docs.mistral.ai/getting-started/models/ ; https://help.mistral.ai/en/articles/347393 ; https://spdx.org/licenses/ (list 3.29.0, 2026-09-16) | verification: Verified (primary) | last_verified: 2026-11-23 | volatile: True

## OpenMDW License Agreement 1.1 — `LicenseRef-OpenMDW-1.1`

- **osi_status:** pending
- **fsf_status:** nonfree
- **patent_grant:** express
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution']
- **obligations:** ['attribution', 'patent_retaliation']
- steward_year: Linux Foundation / May 28, 2026 (1.0: 2025)
- allows: Permission to deal in "Model Materials" (models, parameters, code, data, docs) without restriction under copyright, patent, database and trade-secret rights
- conditions: Retain agreement copy and notices on distribution; defensive termination provision (under discussion at OSI); no conditions on outputs
- copyleft_detail: None
- gpl_compatibility: Expected compatible as permissive (not FSF-reviewed)
- notable_projects: NVIDIA Cosmos, Isaac GR00T, Ising, Nemotron (19+ models); Arcee Trinity; Poolside Laguna S 2.1; ByteDance Seed-X (1.0)
- saas: No obligations
- notes: Likely to become a standard row; track OSI decision.
- **Editorial view – build_on:** Low risk; designed for full model releases.
- **Editorial view – license_your_own:** Strong candidate for releasing your own model + data + code under one license.
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://openmdw.ai/license/1-1 ; OSI license-review list Aug. 2026 | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Qwen3.8-Max License — `LicenseRef-Qwen3.8-Max`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'threshold', 'commercial_use']
- **obligations:** ['attribution', 'naming_rule', 'maas_gate', 'mau_revenue_cap']
- steward_year: Alibaba (Qwen) / 2026
- allows: MIT-style grant over the model and derivatives
- conditions: Display model name above 100M MAU or US$20M monthly revenue; MaaS or AI Work Assistant businesses with licensee + affiliates revenue above US$50M in any 12 months need a separate Qwen license before commercial use; internal use exempt
- copyleft_detail: Commercial-use gate for MaaS / AI work assistants
- gpl_compatibility: N/A
- notable_projects: Qwen3.8-2.4T-A95B
- saas: MaaS / AI work-assistant gate
- notes: Group-level revenue test - M&A trigger.
- **Editorial view – build_on:** Check product category (MaaS, AI work assistant) as well as group revenue.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE | verification: Verified (primary) | last_verified: 2026-11-18 | volatile: True

## Qwen Community License 1.0 — `LicenseRef-Qwen-Community-1.0`

- **osi_status:** not_approved
- **fsf_status:** nonfree
- **patent_grant:** none
- **copyleft_scope:** use_restriction
- **triggers:** ['distribution', 'service_offering', 'threshold', 'commercial_use']
- **obligations:** ['attribution', 'naming_rule', 'maas_gate']
- steward_year: Alibaba (Qwen) / 2026
- allows: Use, modify, distribute
- conditions: Separate license required for MaaS and AI work-assistant products (reported: no revenue floor); attribution clause
- copyleft_detail: Use restriction
- gpl_compatibility: N/A
- notable_projects: Qwen3.8-Flash-Next
- saas: Restricted for MaaS
- **Editorial view – build_on:** Secondary sources only - confirm the license file before relying.
- **Editorial view – license_your_own:** N/A
- **Editorial view – jurisdiction:** US (general); verify locally
- provenance: https://13k.eu/en/policy/open-weight-licenses/ (secondary) | verification: Secondary only | last_verified: 2026-11-18 | volatile: True

