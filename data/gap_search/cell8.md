## Cell 8: Causal / interventional interpretability of grounding outputs (and interpretability of REC/RES, 3D-LLM and AV-LLM grounding)

Search date 2026-11-17.

**Already in slice, not re-added:** Kang et al. CVPR 2025, Neo et al. ICLR 2025, Zhang et al. CVPR 2025, Basu et al. NeurIPS 2024, Golovanevsky NAACL 2025, Jiang et al. ICLR 2025, Pach et al. NeurIPS 2025, Gandelsman ICLR 2024, Chefer ICCV 2021, Kaduri CVPR 2025, Nikankin NeurIPS 2025, SegCompass CVPR 2026, AdaptVis ICML 2025, "MLLMs know where to look" ICLR 2025, Palit ICCV-W 2023.

**Hit rule used:**
- (a) An activation-level or token/head-level intervention whose measured outcome is a grounding output (box, mask, heatmap, REC/RES accuracy). Or:
- (b) An interpretability method or analysis that is evaluated on, or explains, a grounding output.
- Interpretable-by-design grounding architectures, and mechanistic studies whose outcome is text (VQA, captions), are near-misses.

**Queries** (source | exact query | number of relevant results)
1. alphaXiv discover_papers | `mechanistic or causal interpretability of visual grounding in multimodal LLMs: activation patching, attention knockout, ablating attention heads or visual tokens and measuring referring expression comprehension accuracy or box/coordinate output; how MLLMs produce bounding box coordinates` | 3 (Visual Retrieval Heads, Grounding Isn't Knowing, Angular Relevance), plus near-misses (Gaze Heads, causal tracing of vision encoders, attention faithfulness)
2. WebSearch | `Cao "Emergent Pixel Grounding in Large Multimodal Models Without Grounding Supervision" conference` | 1 (Cao et al.; venue check)
3. WebSearch | `explainability referring expression comprehension OR referring image segmentation model explanation attribution analysis TransVG LAVT what do grounding models attend` | 0 hits (near-misses only: AMC, LGRAN)
4. WebSearch (extended) | `interpretability 3D large language model grounding attention analysis OR audio-visual LLM interpretability sound source localization attention heads` | 0 hits (AV-LLM mechanistic studies measure text outputs)
5. alphaXiv discover_papers | `interpretability or attention analysis of 3D large language models for 3D visual grounding, or of audio-visual LLMs / audio-visual models for sound source localization and segmentation; also explanation methods for referring image segmentation models` | 2 (Mechanisms of Object Localization, Drop-off to Recovery), plus AV-LLM near-misses
6. Google Scholar MCP | `activation patching visual grounding referring expression attention heads causal` | 0 (the tool returned an empty result)
7. Semantic Scholar API | `mechanistic interpretability visual grounding localization heads ablation` | S2: HTTP 429 after 4 retries, not available
8. WebSearch | `3D-LLM interpretability probing point cloud tokens 3D visual grounding attention knockout OR ablation analysis "3D" multimodal LLM mechanistic` | 0 hits (3D-LLM attention and logit-lens studies on QA only)
9. arXiv API | `all:"attention knockout" AND (all:grounding OR all:localization)` (25 results) | 2 (Grounding Isn't Knowing and Mechanisms of Object Localization, already found; confirms them)
10. arXiv API | `all:"referring" AND (all:"activation patching" OR all:"causal mediation" OR all:"mechanistic")` (25 results) | 0
11. Verification: WebSearch `"Mechanisms of Object Localization in Vision-Language Models" CVPR 2026 openaccess`, plus CVF pages fetched with curl (CVPR 2026 paper page; ICCV 2025 Findings workshop listing).

**Verified hits** (key | title | venue | status | verified via | why it fills the cell)

*(a) Causal, with a grounding outcome*
- `schaumloffel2026mechanisms` | Mechanisms of Object Localization in Vision-Language Models | CVPR 2026 | peer-reviewed | CVF open-access page (pp. 31356-31365) plus arXiv 2605.19792
  - Token ablation, attention knockout and causal mediation in LLaVA-1.5 and InternVL-3.5, with the predicted box as the outcome.
  - Localisation is driven by a "containerization" mechanism over object-aligned tokens, and a very small set of heads mediates the causal effect.
  - The only peer-reviewed causal study with a box outcome found.
- `park2026retrieval` | Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information | arXiv 2608.27417 | preprint | arXiv abs
  - Visual Retrieval Heads (about 1.7–2.6% of heads) are causally responsible for referring grounding.
  - Masking the top 20 "reduces grounding accuracy by up to 80 percentage points" across 11 VLMs and 5 REC benchmarks, while random heads have little effect (abstract claims).
  - Supplies the causal test that Kang et al. (CVPR 2025) did not run.
- `liu2026grounding` | Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning? | arXiv 2608.23074 | preprint | arXiv abs
  - Token ablation, probing, attention knockout and causal mediation in LLaVA-1.5 and Qwen2.5-VL.
  - A small set of heads mediates both the localisation and spatial-relation outputs, and precise box boundaries are not needed for relation prediction.
- `wu2026dropoff` | From Drop-off to Recovery: A Mechanistic Analysis of Segmentation in MLLMs | arXiv 2603.17228 | preprint | arXiv abs
  - **Borderline:** attention knockout with a mask-level outcome (linear segmentation probes on MLLM tokens), but the outcome is semantic segmentation, not a referring output.
  - Finds an adapter "drop-off" and attention-mediated recovery in the LLM layers.

*(b) Interpretability evaluated as grounding output (correlational, not causal)*
- `cao2024emergent` | Emergent Visual Grounding in Large Multimodal Models Without Grounding Supervision | arXiv 2410.08209 | preprint | arXiv abs (comment "ICCV 2025 Findings", but not among the 31 papers in the CVF ICCV 2025 Findings proceedings) | "Attend-and-segment" reads pixel masks out of the attention maps of LMMs trained without grounding supervision.
- `esmaeilkhani2026angular` | Angular Supervision for Visual Object Grounding in Autoregressive Vision-Language Models | arXiv 2610.32220 | preprint | arXiv abs | Proposes a norm-invariant explanation measure (Angular Relevance). It argues that attention maps and Logit Lens give poor spatial explanations, and evaluates the new maps as training-free RES.

**Near-misses** (title (venue/arXiv id) | why excluded)

*Causal studies of VLMs with text outcomes*
- Gaze Heads: How VLMs Look at What They Describe (Gandikota and Bau, arXiv 2606.14703) | Attention-mask intervention on "gaze heads" redirects which region is described (83.1% panel steering, abstract). The outcome is caption content, not a box or mask. The closest causal analogue for region selection.
- Where To Look? Causal Tracing of Vision Encoders in VLM (arXiv 2608.10758) | Causal tracing on answers. Finds highly causal vision tokens "often lie outside the target region", which is relevant evidence, but the outcome is text.
- Visual Attention Faithfulness in VLMs is Heterogeneous (arXiv 2609.00830; EMNLP 2026 per comment) | Causal perturbation of attention-ranked tokens on VQAv2, VRDU and ChartQA. Not grounding outputs.
- Pathways of Visual Information Flow in VLMs (arXiv 2607.03358) and From Vision to Language: Causal Information Flow in Multimodal Decision-Making (arXiv 2609.05149) | Causal patching for answer/decision outputs (alphaXiv listing). Not grounding.
- Mechanistic Insights into Functional Sparsity in MLLMs via CoRe Heads (arXiv 2606.05843) | Query-relevant visual extraction for answers. Seen in listing only.

*Audio-visual LLMs: mechanistic, but text outputs and no localisation*
- Do Audio-Visual Large Language Models Really See and Hear? (arXiv 2604.02605; "CVPR Findings" per comment) | "First mechanistic interpretability study of AVLLMs". Probing and attention knockout show deeper layers privilege vision and suppress audio. Outcome is text generation, not sound-source localisation.
- Probing Cross-modal Information Hubs in Audio-Visual LLMs (arXiv 2605.10815; ICML 2026 per comment) | Cross-modal sink tokens; hallucination mitigation. No grounding output.
- From Senses to Decisions: The Information Flow of Auditory and Visual Perception in MLLMs (arXiv 2606.10147) | AV information flow for answers (listing only).
- Are Audio-Language Models Listening? Audio-Specialist Heads (arXiv 2603.06854) and Causal Tracing of Audio-Text Fusion in LALMs (arXiv 2603.13768) | Audio-language only.
- Unlocking Spatial Grounding in Large Audio-Visual Retrieval Models (LAIP, arXiv 2607.24786) | Shows intermediate visual tokens of AV retrieval models retain spatial information usable for sound-source localisation. It is a method paper, not an interpretability study.

*3D-LLMs: attention or probing on QA*
- The Point, the Vision and the Text: Does Point Cloud Boost Spatial Reasoning of LLMs? (arXiv 2504.04540) | Attention visualisation, logit lens and modality masking in 3D-LLMs (point-cloud attention sinks). Outcome is spatial-reasoning QA, not 3D boxes. Details from a search summary.
- Do 3D Large Language Models Really Understand 3D Spatial Relationships? (arXiv 2603.23523) | Attention-based reliance on point-cloud tokens for QA (search summary).

*REC/RES explanation-adjacent*
- Improving Visual Grounding by Encouraging Consistent Gradient-based Explanations (AMC, arXiv 2206.15462) | Uses Grad-CAM explanations as a training signal for grounding. Does not analyse a grounding model's mechanism.
- Neighbourhood Watch: REC via Language-guided Graph Attention Networks (arXiv 1812.04794), and MAttNet (already in bib) | Interpretable by design (attention or graph modules), not post-hoc or causal analysis.
- CLUE (arXiv 2602.08999; cell 7 hit) | Uses cross-modal attention maps as an ambiguity signal for interactive grounding, with no causal analysis.

**Could not verify**
- Venue of Cao et al. (arXiv comment "ICCV 2025 Findings"). Not in the CVF ICCV 2025 Findings proceedings listing, so cited as preprint.
- Code link for `schaumloffel2026mechanisms` (github.com/t9s9/vlm-loc-mechanisms). Reported only by a search summary, so not recorded as code_url.
- 3D-LLM near-misses (arXiv 2504.04540, 2603.23523). Seen only through search summaries; abstracts not read.

**Verdict: partially filled.** As of 2026-11-17 (sources: alphaXiv, WebSearch, the arXiv API; S2 and Google Scholar were unavailable or empty), one peer-reviewed paper and three preprints apply causal interventions with a grounding outcome:
- Schaumlöffel et al. (CVPR 2026) use token ablation, attention knockout and causal mediation on the predicted box.
- Visual Retrieval Heads (preprint): head masking collapses REC accuracy by up to 80 pp across 11 VLMs.
- "Grounding Isn't Knowing" (preprint).
- "Drop-off to Recovery" (preprint, borderline): segmentation probes.

These complement the attention-based localisation-heads line (Kang et al., CVPR 2025) and attention-based emergent-grounding readouts (Cao et al.; Angular Relevance), which remain correlational.

Still missing, as far as these sources show: causal analyses of mask-producing grounders ([SEG]/LISA-style MLLMs or classic RES models such as LAVT), and post-hoc explanation studies of classic REC/RES models (MAttNet, TransVG, LAVT). Also missing is any interpretability work whose outcome is a grounding output in:
- temporal or spatio-temporal grounding
- 3D-LLM grounding (3D-LLM analyses found concern QA only)
- audio-visual LLM grounding (AV-LLM mechanistic studies exist, but measure text outputs, not sound-source localisation)
