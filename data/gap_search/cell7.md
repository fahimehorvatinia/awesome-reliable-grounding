## Cell 7: Calibration, uncertainty estimation, conformal prediction and risk-coverage / selective prediction for grounding OUTPUTS (boxes, masks, points, temporal intervals, 3D boxes)

Search date 2026-11-17. Already in slice, so not re-added: Whitehead et al. ECCV 2022, Padhi et al. 2025 (preprint), D3 (NeurIPS 2023), VIRO (CVPR 2026). SRAM ("Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding", arXiv 2408.16272, preprint) is a hit, but its record already exists in reliability.jsonl as `ma2024beyond`, so it is not duplicated in cell7.jsonl.

**Queries** (source | exact query | number of relevant results)
1. WebSearch | `uncertainty estimation referring expression comprehension bounding box calibration` | 1 (Deruyttere et al. 2021)
2. WebSearch | `uncertainty-aware video temporal grounding moment retrieval boundary uncertainty annotation ambiguity` | 5 (SRAM, DEMR, EMB, DTG, Shang et al.)
3. alphaXiv discover_papers | `calibration and uncertainty estimation of visual grounding outputs: calibrated confidence of open-vocabulary / phrase grounding detectors, uncertainty-aware referring expression comprehension or segmentation, conformal prediction for language-conditioned detection` | 2 (COVER, Surrogate Uncertainty), plus near-misses
4. alphaXiv discover_papers | `uncertainty estimation, calibration or selective prediction for video temporal grounding / moment retrieval, modelling boundary uncertainty or annotation ambiguity, and uncertainty-aware referring image segmentation` | 4 (COVER, DEMR, Shang et al., PROVE)
5. Semantic Scholar API | `uncertainty visual grounding referring expression` | S2: HTTP 429 after 4 retries, not available
6. Semantic Scholar API | `calibration referring expression segmentation confidence` | 0 (the hits were "calibration" used in the sense of feature calibration)
7. Semantic Scholar API | `conformal prediction grounding` | S2: HTTP 429, not available
8. arXiv API | `all:"visual grounding" AND (all:uncertainty OR all:calibration OR all:conformal)`, the same with `all:"referring expression"`, and the same with `"temporal grounding" OR "moment retrieval"` | HTTP 429 in two rounds, not available
9. Google Scholar MCP | `uncertainty calibration visual grounding referring expression comprehension` | 0 (the tool returned an empty result)
10. WebSearch | `conformal prediction visual grounding bounding box coverage guarantee referring` | 0 (generic conformal object detection only; see near-misses)
11. WebSearch | `calibration of open-vocabulary object detectors confidence miscalibration 2024 2025` | 0 verifiable (YOLO-World temperature-scaling paper could not be verified)
12. WebSearch | `Andeol conformal object detection sequential risk control; de Grancey conformal object detection 2022` | 0 (near-misses)
13. WebSearch (extended) | `confidence calibration multimodal LLM visual grounding bounding box uncertainty quantification` | 0 (VQA-level near-misses)
14. WebSearch | `Grounding DINO OWL-ViT calibration expected calibration error open-vocabulary detection confidence` | 0
15. WebSearch | `uncertainty-aware referring image segmentation OR 3D visual grounding uncertainty estimation paper` | 1 (CroBIM-U)
16. WebSearch | `GUI grounding uncertainty calibration abstention click coordinates confidence` | 2 (SafeGround, HyperClick)
17. WebSearch | `uncertainty estimation audio-visual segmentation OR sound source localization calibrated confidence` | 1 (Liu et al. CVPR 2025)
18. WebSearch | `"selective prediction" OR "risk-coverage" grounding localization referring abstain` | 0 (SIEVES is a near-miss)
19. WebSearch | `phrase grounding uncertainty probabilistic embeddings ambiguity multiple hypotheses referring expression` | 2 (uMedGround, CLUE)
20. alphaXiv discover_papers | `confidence calibration of open-vocabulary object detectors (e.g. Grounding DINO, OWL-ViT, YOLO-World, GLIP): expected calibration error, miscalibration analysis, post-hoc calibration` | 1 (Soon & Hsieh)
21. WebSearch (extended) | `"open-vocabulary" object detection "calibration" ECE study arXiv detectors overconfident novel classes` | 0
22. alphaXiv discover_papers | `uncertainty estimation, confidence calibration or conformal prediction for 3D visual grounding, spatio-temporal video grounding, referring video object segmentation, or reasoning segmentation with multimodal LLMs` | 0 new
23. WebSearch | `conformal risk control segmentation masks text-prompted OR language-conditioned OR open-vocabulary segmentation guarantee` | 0 (generic conformal segmentation only)
24. arXiv API (succeeded on retry) | `("visual grounding" OR "referring expression" OR "temporal grounding" OR "moment retrieval") AND (conformal OR calibration OR "selective prediction")`, 40 results | 4 new (Zoom Consistency, GRIT, Wang & Rambow; Surrogate, PROVE and COVER again)
25. Crossref title search (during verification) | `Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding` | 1 new (Xia et al., CVIU 2026; abstract not readable, see "Could not verify")
26. Coordinator-supplied candidate | arXiv 2610.14210 | 1 (Zakrzewski et al.)

**Verified hits** (key | title | venue | status | verified via | why it fills the cell)

*Formal guarantees, calibration metrics, selective prediction*
- `mohamed2026conformal` | Conformal Coverage Guarantees for Any Video Temporal Grounder | arXiv 2608.07434 | preprint (submitted to AAAI 2027) | arXiv abs | Post-hoc split-conformal wrapper that turns any temporal grounder into one whose temporal region covers the true moment with probability ≥1−α. Motivated by annotator disagreement on boundaries.
- `zhang2026surrogate` | Surrogate Uncertainty for Black-box Visual Grounding | arXiv 2610.39798 | preprint | arXiv abs | Bayesian surrogate estimates per-query aleatoric and epistemic uncertainty for a black-box VLM grounder. Combined with conformal prediction or ask-or-act planning on a robot, it "improves both calibration and task performance".
- `nautiyal2026prove` | PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models | arXiv 2610.32440 | preprint | arXiv abs | Evidential per-patch Beta grounding maps from frozen CLIP. Its uncertainty "tracks localisation error and supports selective prediction under abstention", and it detects absent referents.
- `zakrzewski2026agreement` | Agreement versus Softmax under Spatial Disambiguation | arXiv 2610.14210 | preprint (NeurIPS 2026 workshop, non-archival, per arXiv comment) | arXiv abs | Object-level ECE for 3D grounding on ScanRefer, split into Unique and Multiple queries. The only box-level calibration study for 3D-VG found.
- `wang2026safeground` | SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration | ICLR 2026 Workshop and ICML 2026 Workshop | workshop | arXiv abs plus iclr.cc and icml.cc "Poster in Workshop" pages | Sampling-dispersion uncertainty for click coordinates, with a calibrated threshold that gives statistically guaranteed FDR control and abstain-or-cascade.
- `zhang2025enhancing` | Enhancing Trustworthy GUI Grounding via Self-Critiqued Reinforcement Learning (HyperClick) | arXiv 2510.27266 | preprint | arXiv abs | Reports that GUI-grounding confidence is misaligned with correctness, and trains explicit click confidence by RL to support abstention.
- `kim2026zoom` | Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines | arXiv 2604.15376 | preprint | arXiv abs | A geometric confidence signal for GUI point grounding (AUC 0.60, an abstract claim) used for routing.
- `soon2026confidence` | Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics | arXiv 2607.10993 | preprint (ICPR 2026 workshop claimed in arXiv comment) | arXiv abs | Shows that GroundingDINO, OWL-ViT and YOLO-World scores "are not reliable localization probability estimates" because of scale and semantic bias. Temperature-scaling correction.
- `gupta2022grit` | GRIT: General Robust Image Task Benchmark | arXiv 2204.13653 | preprint | arXiv abs; Semantic Scholar venue is arXiv.org | Benchmark that evaluates "performance, robustness, and calibration" over seven tasks, including referring expression grounding and localisation.
- `wang2026seeing` | When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs | arXiv 2608.23978 | preprint (EMNLP 2026 claimed in arXiv comment, not confirmed) | arXiv abs | Finds that LVLMs in interactive visual grounding are "poorly calibrated, often reporting confidence that exceeds their empirical accuracy".

*Uncertainty-aware grounding models (no formal calibration)*
- `huang2026adaptive` | Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval (DEMR) | AAAI 2026 | peer-reviewed | Crossref DOI 10.1609/aaai.v40i7.37414 plus arXiv | Debiased deep evidential regression for moment-retrieval uncertainty, evaluated on Charades-CD and ActivityNet-CD.
- `huang2022video` | Video Activity Localisation with Uncertainties in Temporal Boundary (EMB) | ECCV 2022 | peer-reviewed | ECVA page | Models annotation uncertainty of temporal boundaries during training.
- `zhou2022thinking` | Thinking Inside Uncertainty: Interest Moment Perception for Diverse Temporal Grounding (DTG) | IEEE TCSVT 2022 | peer-reviewed | Crossref DOI 10.1109/tcsvt.2022.3179314; abstract via OpenAlex | Addresses label uncertainty (several valid moments) with multi-output prediction and new metrics.
- `shang2026llm` | LLM-Powered Query Expansion for Enhancing Boundary Prediction in Language-Driven Action Localization | IJCV 2026 | peer-reviewed | Crossref DOI 10.1007/s11263-026-03083-9 | Uses probabilistic boundary targets to tolerate boundary-annotation uncertainty.
- `deruyttere2021giving` | Giving Commands to a Self-Driving Car: How to Deal with Uncertain Situations? | Engineering Applications of AI 2021 | peer-reviewed | Crossref DOI 10.1016/j.engappai.2021.104257 | Detects uncertain grounding situations on Talk2Car and generates clarifying questions.
- `zou2025uncertainty` | Uncertainty-Aware Medical Diagnostic Phrase Identification and Grounding (uMedGround) | IEEE TPAMI 2025 | peer-reviewed | Crossref DOI 10.1109/tpami.2025.3596878 | Medical phrase grounding to boxes with an uncertainty-aware prediction model.
- `liu2025robust` | Robust Audio-Visual Segmentation via Audio-Guided Visual Convergent Alignment | CVPR 2025 | peer-reviewed | CVF page | Uncertainty-estimation head for AVS masks that lowers confidence where sound state changes. The only audio-visual grounding uncertainty model found.
- `sun2026crobimu` | CroBIM-U: Uncertainty-Driven Referring Remote Sensing Image Segmentation | arXiv 2601.03490 | preprint | arXiv abs | Pixel-wise referring-uncertainty map for RES, used internally for gating and refinement rather than reported as confidence.
- `abrini2026clue` | CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion | arXiv 2602.08999 | preprint | arXiv abs | An ambiguity detector on cross-modal attention decides when an interactive grounder should ask instead of answer.
- (`ma2024beyond`, SRAM, arXiv 2408.16272, preprint: hit, already in reliability.jsonl.)

**Near-misses** (title (venue/arXiv id) | why excluded)

*Generic, not language-conditioned. Useful for the "transfer" argument.*
- Multivariate Confidence Calibration for Object Detection (Küppers et al., CVPR 2020 Workshops, CVF page found by search) | Box-position- and scale-aware calibration (D-ECE) for class-label detectors. Not language-conditioned.
- On Calibration of Object Detectors: Pitfalls, Evaluation and Baselines (Kuzucu et al., arXiv 2405.20459) | Localisation-aware ECE and post-hoc calibrators for generic detectors. A natural template for REC calibration metrics.
- Uncertainty Quantification in Detection Transformers: Object-Level Calibration and Image-Level Reliability (arXiv 2412.01782) | Generic DETR. Seen in alphaXiv listing only.
- Object Detection with Probabilistic Guarantees: A Conformal Prediction Approach (de Grancey et al., SAFECOMP 2022 workshops, per search snippet) | Generic conformal object detection.
- Confident Object Detection via Conformal Prediction and Conformal Risk Control: an Application to Railway Signaling (Andéol et al., PMLR v204, COPA 2023) | Generic conformal object detection.
- Conformal Object Detection by Sequential Risk Control (Andéol et al., arXiv 2505.24038) | Formalises conformal object detection (SeqCRC). Not language-conditioned.
- Sequential Conformal Risk Control for Safe Railway Signaling Detection (Andéol and Masséna, PMLR v266, per search snippet) | Generic.
- Adaptive Bounding Box Uncertainties via Two-Step Conformal Prediction (Timans et al., arXiv 2403.07263; ECCV 2024 per arXiv comment) | Class-conditional box intervals. Generic.
- Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty (Mossina et al., CVPR 2024 Workshops) | Conformal risk control for closed-set segmentation.
- Controlling False Positives in Image Segmentation via Conformal Prediction (arXiv 2511.15406) and conformal promptable segmentation (arXiv 2602.10045, search snippet only) | Medical, or pixel-prompted SAM, not text-prompted.
- UncertainSAM (arXiv 2505.05049) | SAM uncertainty with visual prompts.
- Query2Uncertainty (arXiv 2605.05328) | Calibration for 3D object detection, not language-conditioned.
- Calibrating Probabilistic Object Detectors with Annotator Disagreement (arXiv 2605.24722) and Object Detection Benchmarks are Incomplete (arXiv 2609.21822) | Annotation uncertainty for generic detection.

*Open-vocabulary detection where "calibration" means something else*
- ProCal: Inference-Time Proposal Calibration for OVOD (arXiv 2607.01759) | Localisation-aware reranking of proposals against "ranking miscalibration". No confidence-calibration analysis.
- CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object Detection (arXiv 2608.27214, ACM MM 2026 per comment) | Known/unknown score adjustment, not probability calibration.
- Exploring Hierarchical Consistency and Unbiased Objectness for OVOD (arXiv 2604.23344) | Calibrates pseudo-labels for training.
- Open-Vocabulary Calibration for Fine-tuned CLIP (arXiv 2402.04655) | Classification only.
- Correlation-Guided Query-Dependency Calibration for Video Temporal Grounding (arXiv 2311.08835) | "Calibration" of attention or query dependency, not confidence.

*Grounding used as a signal for VQA or answer confidence (same status as Padhi et al.)*
- SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring (arXiv 2604.25855; neurips.cc 2026 poster page seen) | Risk–coverage for VQA answers. Localisation quality is a selector feature, not the certified output.
- SRICE: Seeing and Reasoning with Confidence (arXiv 2503.08308) | Conformally calibrates external detector outputs inside a VQA agent. The output is a VQA answer.
- Object-Level Verbalized Confidence Calibration in VLMs via Semantic Perturbation (arXiv 2504.14848) | Verbalized confidence on object-centric QA.
- SAVOR (arXiv 2609.16601; ICONIP 2026 per comment) | Calibrated confidence for hallucination QA.
- VL-Calibration (arXiv 2604.09529) and "Seeing is Believing, but How Much?" (EMNLP 2025) | Answer-level LVLM calibration.
- Uncertainty-Aware Decision Making in MLLMs, a survey (arXiv 2608.17084) | Survey, not grounding-output calibration.

*Grounding papers without uncertainty or calibration of the output*
- OpenRef / Multi-task Consistency Checker (arXiv 2605.25706) | Rejection metric (N3R) and consistency self-verification, with no calibration. Belongs to the absent-target and verification cells.
- ReGround-Surg (arXiv 2608.24671; PRCV 2026 per comment) | The "reliability map" is an attention weighting, not output uncertainty.
- Bayesian Self-Training for Semi-Supervised 3D Segmentation (arXiv 2409.08102; ECCV 2024 per search snippet) | Uncertainty filters pseudo-labels (including for dense 3D-VG), not the output.
- Uncertainty Estimation for Sound Source Localization with Deep Learning (IEEE TIM, PolyU repository page) | Microphone-array audio SSL, no visual grounding.
- ENCP: conformal prediction for VLN (arXiv 2609.17499) and Confidence Calibration in VLA Models (arXiv 2507.17383) | Navigation and actions, not grounding outputs.

**Could not verify**
- "Evidential learning for Uncertainty-Aware Video Temporal Grounding and Rejection" (Xia, Su, Zhou et al., Computer Vision and Image Understanding vol. 273, art. 104967, 2026, DOI 10.1016/j.cviu.2026.104967; SSRN preprint 10.2139/ssrn.6463182). The bibliographic record is verified via Crossref, but no abstract was readable: Crossref has none, OpenAlex has none, and SSRN is bot-walled. By its title it is very likely a peer-reviewed hit (evidential uncertainty plus rejection for VTG). No JSONL record was written. **Check before citing.**
- YOLO-World temperature-scaling calibration study (ICAIIT 2025, opendata.uni-halle.de PDF). The page is bot-walled (Anubis), so the title and authors were not confirmed.
- Venue claims taken from arXiv comments only: ICPR 2026 Workshop (`soon2026confidence`), EMNLP 2026 (`wang2026seeing`), NeurIPS 2026 workshop, non-archival (`zakrzewski2026agreement`). All three are cited as preprints.

**Verdict: partially filled.** As of 2026-11-17 (sources: WebSearch, alphaXiv, the arXiv API, Crossref/OpenAlex for verification; S2 and Google Scholar were unavailable or empty), work on grounding-output uncertainty exists in two layers.

- **Peer-reviewed uncertainty-aware models, all without formal calibration evaluation:**
  - temporal-boundary and label-uncertainty modelling for temporal grounding: EMB (ECCV 2022), DTG (TCSVT 2022), DEMR (AAAI 2026), Shang et al. (IJCV 2026)
  - uncertainty heads for medical box grounding (TPAMI 2025) and AVS masks (CVPR 2025)
  - uncertainty-triggered clarification on Talk2Car (EAAI 2021)
- **Formal calibration or guarantees on grounding outputs, all preprints or workshop papers from 2026:**
  - conformal coverage for temporal intervals (COVER)
  - FDR-controlled abstention for GUI point grounding (SafeGround, workshop)
  - surrogate-Bayesian and conformal uncertainty for black-box robot grounding
  - evidential selective prediction for CLIP grounding maps (PROVE)
  - object-level ECE on ScanRefer (non-archival workshop)
  - an analysis of OV-detector score bias

No peer-reviewed work was found that reports localisation-aware calibration (for example ECE or risk–coverage over IoU) or conformal guarantees for standard REC/RES/GRES with MLLM grounders, for spatio-temporal video grounding or RVOS, for 3D grounding beyond the workshop note, or for audio-visual grounding beyond one uncertainty head. Generic conformal object detection (de Grancey 2022; Andéol 2023 and 2025; Timans, ECCV 2024) and box-aware calibration (Küppers, CVPRW 2020) could transfer, but none of them is language-conditioned.
