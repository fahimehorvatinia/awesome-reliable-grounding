## Cell 4: Corruption / perturbation robustness of temporal grounding outputs

Scope: moment retrieval (MR), temporal sentence grounding (TSG), video temporal grounding (VTG) with Video-LLMs, and highlight detection (HD). Each must be evaluated on predicted temporal intervals under one of two kinds of perturbation:
- video corruptions: noise, blur, compression, frame drops, temporal shuffling;
- text perturbations: typos, paraphrase, query rewording.

Already in the slice and not re-added:
- Schiappa et al. (NeurIPS 2022 D&B): text-to-video retrieval perturbations.
- R^2-Bench (ECCV 2024).
- Otani et al. (BMVC 2020).
- Charades-CD / ActivityNet-CD (Yuan / Lan et al.).
- Moment of Untruth (WACV 2025).

**Queries** (source | exact query | number of relevant results)
1. WebSearch | robustness benchmark video moment retrieval temporal sentence grounding perturbations corruption | 1 (Jung et al. consistency). It also surfaced a near-miss: robust test-time video-text retrieval, ICLR 2026.
2. WebSearch | video temporal grounding video-LLM robustness query paraphrase consistency benchmark | 1 (Jung et al.), plus near-misses EgoExo-Con and REVEAL.
3. alphaXiv discover_papers | keywords [moment retrieval, temporal grounding, robustness, perturbation]; question: "Robustness of video moment retrieval / temporal sentence grounding / video temporal grounding to video corruptions ... or query text perturbations ..." | 1 (Jung et al.), plus near-misses REVEAL, TemRobBench, query-insensitive STVG, EgoExo-Con and robust video-text retrieval.
4. alphaXiv discover_papers | keywords [Charades-STA, QVHighlights, noise, frame drop]; question: "Evaluating temporal sentence grounding or highlight detection models under video corruptions, compression, frame dropping, temporal shuffling, or noisy/typo queries ..." | 0 (only nominal VTG methods).
5. WebSearch | "temporal sentence grounding" robustness "query perturbation" OR "noisy queries" OR "typos" | 1 (HERO), plus near-misses SpotSound (audio-only), Embracing Uncertainty (CVPR 2021) and the causal TSG preprint 2507.04958.
6. WebSearch | video LLM temporal grounding robustness frame sampling temporal perturbation shuffled frames timestamp localization 2025 | 0 interval-level. Near-misses: Trust-videoLLMs 2506.12336, VideoQA in the Era of LLMs (IJCV 2025), 2505.14321.
7. WebSearch (extended) | "moment retrieval" OR "temporal grounding" corrupted videos Gaussian noise blur compression robustness evaluation Charades-STA QVHighlights | 1 (SRAM). Near-misses: CausalVTG (NeurIPS 2025) and Denoise-then-Retrieve.
8. WebSearch | video moment retrieval degraded video low-light adverse conditions noisy video robust temporal grounding paper | 2 (NST for STVG; SRAM), plus near-misses CDNet and Denoise-then-Retrieve.
9. WebSearch | temporal grounding benchmark "rephrased queries" OR "query variations" OR "paraphrased queries" video LLM robustness IoU 2026 | 2 (Dang et al., Multimedia Systems 2026; HERO).
10. Semantic Scholar API | robustness video moment retrieval perturbation / robustness temporal sentence grounding perturbation | S2: 429 on all retries (5 retries × 10 s back-off, two sessions), not available.
11. arXiv API | all:"moment retrieval" AND all:robustness | arXiv: 429 on all retries during the cell-4 pass, not available. Later arXiv API calls in cell 6 succeeded.
12. Google Scholar MCP | robustness temporal sentence grounding video moment retrieval perturbation benchmark | returned an empty result set (tool appears non-functional).
13. Follow-up WebSearch | "Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding" accepted | 0 venue found. It surfaced DEMR (AAAI 2026) as a near-miss.

**Verified hits**
- jung2025consistency | On the Consistency of Video Large Language Models in Temporal Comprehension | CVPR 2025 | peer-reviewed | CVF page + arXiv 2411.12951 | Probes Video-LLM temporal grounding with rephrased queries and temporally shifted target moments, and measures how consistent the predicted intervals stay (Charades-CON / ActivityNet-CON). Most models are far from consistent.
- dang2026distinguishing | Distinguishing semantically similar queries in temporal video grounding via LLM-generated query | Multimedia Systems 32(2) 2026 | peer-reviewed | Crossref DOI 10.1007/s00530-025-02147-z | LLM-generated paraphrases and semantically similar hard negatives for VTG/HD, with new robustness metrics. This is query-rewording robustness on interval outputs (abstract-level evidence only; Springer full text not accessed).
- han2026hero | HERO: Hierarchical Embedding-Refinement for Open-Vocabulary Temporal Sentence Grounding in Videos | arXiv 2603.06732 | preprint | arXiv abs + HTML | Charades-OV / ActivityNet-OV rewrite the CD test queries with an LLM so that each contains novel concepts ("paraphrastic variations"). Closed-vocabulary TSG models degrade (R1@IoU).
- chen2026knowledge | Knowledge-Preserved Model Tuning in Null-Space for Robust Spatio-Temporal Video Grounding | arXiv 2606.03539 | preprint (arXiv comment "Accepted by ICME 2026"; no IEEE record found) | arXiv abs + HTML | Mixed-Quality STVG benchmark (motion/defocus blur, low light, low resolution on VidSTG/HC-STVG), evaluated with m_tIoU/m_vIoU. This is the only video-degradation robustness study found, and it covers spatio-temporal grounding, not MR/TSG.
- ma2024beyond | Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding (SRAM) | arXiv 2408.16272 | preprint ("ongoing work") | arXiv abs + HTML | Weak hit. It adds Gaussian noise to video features and token swaps to queries on QVHighlights val, but reports only the shift in epistemic uncertainty, not interval accuracy under perturbation.

**Near-misses**
- EgoExo-Con: Exploring View-Invariant Video Temporal Understanding (arXiv 2510.26113; arXiv comment: accepted to ECCV 2026). Tests cross-view (ego/exo) consistency of temporal grounding and verification, which is a viewpoint shift rather than a corruption or perturbation of the same input. It is relevant to H "temporal/cross-view consistency".
- Stress Tests REVEAL Fragile Temporal and Visual Grounding in Video-Language Models (arXiv 2602.11244). Probes are binary or six-way QA, not interval prediction.
- Investigating and Enhancing the Robustness of LMMs Against Temporal Inconsistency (TemRobBench, arXiv 2505.14405). Event-order perturbations of video and text, but all tasks are multiple-choice QA.
- VideoQA in the Era of LLMs: An Empirical Study (IJCV 2025, arXiv 2408.04223). Covers frame shuffling, question rephrasing, word shuffling and keyword removal, but robustness is reported only as QA accuracy and flip rate. Its grounding probes run on clean inputs.
- Benchmarking the Trustworthiness in Multimodal LLMs for Video Understanding (Trust-videoLLMs, arXiv 2506.12336). Includes cross-modal perturbations, but the abstract gives no evidence of interval-level grounding under perturbation.
- Breaking Down Video LLM Benchmarks (arXiv 2505.14321). Frame shuffling, QA only.
- Robust Test-time Video-Text Retrieval: Benchmarking and Adapting for Query Shifts (arXiv 2604.20851; ICLR 2026 per alphaXiv). Video-level retrieval, not moment-level.
- Robustness Analysis of Video-Language Models Against Visual and Language Perturbations (Schiappa et al., NeurIPS 2022 D&B). Already in the slice; text-to-video retrieval.
- Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding (arXiv 2610.06018; EMNLP 2026 Findings per arXiv). Uses irrelevant or missing queries, i.e. absent-target / missing modality rather than perturbation. Already a hit in cell 1 (kolodziejczyk2026investigating).
- SpotSound (arXiv 2604.13023). Paraphrase and shift robustness for audio-only temporal grounding, not video.
- Embracing Uncertainty: Decoupling and De-bias for Robust Temporal Grounding (CVPR 2021). Models query and label uncertainty; there is no perturbation evaluation (snippet-level reading).
- Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval (DEMR, arXiv 2512.00953; comment "Accepted by AAAI 2026"). The abstract describes robustness on Charades-CD/ActivityNet-CD (distribution shift), not input perturbation. Full text not checked.
- CausalVTG: Towards Robust Video Temporal Grounding via Causal Inference (NeurIPS 2025). "Robust" refers to strict-IoU accuracy and debiasing, not perturbation (search-snippet reading).
- Denoise-then-Retrieve (arXiv 2508.11313) and Disentangle and Denoise / CDNet (arXiv 2408.07600). "Noise" here means query-irrelevant clips, and evaluation is nominal.
- Spurious-correlation TSG via causal inference (arXiv 2507.04958). Bias and shortcuts, not perturbation (snippet only).

**Could not verify**
- No candidate hit was left unverified.
- NST's ICME 2026 acceptance (arXiv comment) could not be confirmed in a registry, so it is cited as a preprint.
- Venues and details of the near-misses were not verified beyond the arXiv/alphaXiv pages and are not used as citations.

**Verdict**: partially filled.
- **What exists.** Text-side perturbation of temporal grounding outputs has begun to be studied:
  - Jung et al. (CVPR 2025) test paraphrase and moment-shift consistency for Video-LLMs.
  - Dang et al. (Multimedia Systems 2026) add LLM paraphrases and hard negatives with robustness metrics for VTG/HD.
  - HERO (preprint) adds open-vocabulary query rewriting.
- **What is missing.** As of 2026-11-17, across WebSearch, alphaXiv and Google Scholar (S2 and the arXiv API were rate-limited for this cell), we found no benchmark that applies standard video corruptions to MR/TSG/HD and scores predicted intervals. Standard corruptions here means noise, blur, compression, frame drops or temporal shuffling at controlled severities. The only video-degradation study we found targets spatio-temporal grounding (NST, preprint; blur, low light, low resolution). SRAM (preprint) perturbs features but reports only uncertainty shifts.
- **Also absent.** We found no character-level (typo) query-robustness study for temporal grounding. Frame-shuffling and frame-drop robustness of Video-LLMs has been measured only on QA accuracy, not on temporal IoU.
