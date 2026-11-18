## Cell 10: Benchmark-validity audits: (a) 3D grounding datasets; (b) sound-source localisation beyond those already in slice

Scope: (a) blind or language-only baselines, view-dependence bias, annotation noise or ambiguity, and evaluation flaws in ScanRefer / ReferIt3D (Nr3D, Sr3D) / Multi3DRefer and 3D-VL benchmarks; (b) sound-source localisation (SSL/AVS) benchmark audits beyond Mo & Morgado 2022, Chen et al. ECCV-W 2024, Sun et al. ACM MM 2024, AVSBench-Robust and Seeing Sound/Hearing Sight (all already in slice). Searches were run on 2026-11-17.

**Queries** (source | exact query | #relevant results)
1. alphaXiv discover | "Do 3D vision-language benchmarks like ScanRefer, ReferIt3D Nr3D/Sr3D allow language-only or blind baselines to succeed? Shortcuts, view-dependence bias, annotation noise, evaluation flaws, 3D-LLMs performing similarly without 3D input" (keywords: ScanRefer, Nr3D, Sr3D, blind baseline, 3D-LLM, evaluation) | 1 hit (P³-VLM). Near-misses: Real-3DQA, UNICORNS, two NeurIPS-2026 workshop papers.
2. WebSearch | `3D visual grounding benchmark language-only baseline bias Nr3D Sr3D ScanRefer shortcut analysis` | 2 (EDA, ViGiL3D)
3. CVF Open Access title scan (regex `mist|3D.*(evaluat|benchmark|bias|shortcut|blind|diagnos|rethink|revisit|hallucinat)|(sound|audio).*(locali[sz]|bias|benchmark|segment)` over all CVPR 2024, CVPR 2025, ICCV 2025 and CVPR 2026 titles) | 3 (Beacon3D, AVATAR, Chen et al. CVPR 2024). Near-miss: Senocak et al. CVPR 2026.
4. WebSearch | `"P$^3$-VLM" OR "P3-VLM" point-based alternative grounded 3D vision-language models NeurIPS 2026` | verification only (NeurIPS 2026 poster page)
5. WebSearch | `Juanola Haro Fuentes ICASSP 2025 visual sound source localization negative audio critical assessment` | 2 (Juanola et al. ICASSP 2025; SSL-SaN, BMVC 2025)
6. WebSearch | `LanguageRefer spatial-language model 3D visual grounding CoRL 2021 viewpoint annotation language-only` | 1 (LanguageRefer)
7. WebSearch | `"Does Your 3D Encoder Really Work" 2D VLMs meets 3D VLMs` | 0 hits. Near-misses: 3D-encoder idling paper, "Revisiting 3D LLM Benchmarks".
8. Crossref API | `ViGiL3D Linguistically Diverse Dataset 3D Visual Grounding` | verification only (ACL 2025 DOI)
- Semantic Scholar API was unavailable today (HTTP 429, see cell 3). The Crossref API returned 429 intermittently, so DOIs were checked when it responded.

**Verified hits**

*(a) 3D grounding benchmarks*
- **huang2025beacon3d** | Unveiling the Mist over 3D Vision-Language Understanding: Object-centric Evaluation with Chain-of-Analysis (Beacon3D) | CVPR 2025 | peer-reviewed | verified via CVF page.
  - Explicit validity audit of 3D-VL benchmarks: "flawed test data, like ambiguous referential text in the grounding task, can yield incorrect and unreliable test results".
  - Introduces object-centric re-evaluation and finds that adding LLMs "hinders grounding capabilities".
- **halacheva2026p3vlm** | P³-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models | NeurIPS 2026 (poster page; arXiv says Spotlight) | peer-reviewed | verified via the neurips.cc virtual page and arXiv HTML 2610.28018.
  - A blind LLM given only box coordinates reaches 36.4% class accuracy on Nr3D and 38.1% on ScanRefer. With a single-point prompt this falls to 18.0% and 18.4% (Table 2). Table 1 is headed "Object-centric VLMs do not utilize their 3D encoder".
  - Caveat: the audited task is location-prompted captioning/identification, not localisation output.
- **wang2025vigil3d** | ViGiL3D: A Linguistically Diverse Dataset for 3D Visual Grounding | ACL 2025 | peer-reviewed | verified via Crossref DOI 10.18653/v1/2025.acl-long.1470 and the ACL Anthology.
  - Linguistic-coverage audit of 3D-VG datasets plus a diagnostic OOD prompt set. Open-vocabulary 3D-VG methods fail on these prompts.
- **wu2023eda** | EDA: Explicit Text-Decoupling and Dense Alignment for 3D Visual Grounding | CVPR 2023 | peer-reviewed | verified via CVF page.
  - Partial hit: diagnoses the object-name shortcut on ScanRefer/ReferIt3D and adds the evaluation task "locating objects without object names".
- **roh2022languagerefer** | LanguageRefer: Spatial-Language Model for 3D Visual Grounding | CoRL 2021 (PMLR 164, 2022) | peer-reviewed | verified via PMLR page and ar5iv.
  - Partial hit: analyses view-dependent utterances in ReferIt3D. Reports that "some VD utterances lack information to guess the valid orientation" because annotators "can freely rotate the scene". Provides viewpoint annotations.
  - The model uses box geometry, class labels and language only, with no dense visual features.

*(b) Sound-source localisation*
- **juanola2025critical** | A Critical Assessment of Visual Sound Source Localization Models Including Negative Audio | ICASSP 2025 | peer-reviewed | verified via Crossref DOI 10.1109/ICASSP49660.2025.10890384 and arXiv 2410.01020.
  - Names three evaluation flaws: visible-only sources, assumed object size, and no universal threshold.
  - Adds a negative-audio test set (silence, noise, off-screen). Many SOTA models "fail to appropriately adjust their predictions based on audio input".
- **juanola2025learning** | Learning from Silence and Noise for Visual Sound Source Localization | BMVC 2025 | peer-reviewed | verified via BMVC proceedings page and arXiv 2508.21761.
  - Argues prior evaluations are "limited to positive cases". Adds a new alignment–separability metric and IS3+ with negative audio.
- **choi2025avatar** | What's Making That Sound Right Now? Video-centric Audio-Visual Localization | ICCV 2025 | peer-reviewed | verified via CVF page.
  - Critiques image-level AVL benchmarks that "assume ... sound sources are always visible and involve only a single object".
  - The new AVATAR benchmark has Single-sound, Mixed-sound, Multi-entity and Off-screen scenarios.
- **chen2024unraveling** | Unraveling Instance Associations: A Closer Look for Audio-Visual Segmentation | CVPR 2024 | peer-reviewed | verified via CVF page.
  - Identifies "biased audio-visual data" in AVS training sets and proposes a strategy to build "relatively unbiased" AVS benchmarks.
- **senocak2023sound** (existing key, no new record) | Sound Source Localization is All about Cross-Modal Alignment, ICCV 2023 | relevant.
  - The CVF abstract states that "existing benchmarks do not account for ... cross-modal semantic understanding" (silent objects, off-screen sounds). It adds a cross-modal retrieval evaluation.

**Near-misses**
- Do 3D Large Language Models Really Understand 3D Spatial Relationships? (Real-3DQA; ICLR 2026 per arXiv 2603.23523 comment, venue not re-checked) | A text-only fine-tuned LM "can perform comparably or even surpass" 3D-LLMs on SQA3D. Strong blind-baseline evidence, but for QA only.
- Does Your 3D Encoder Really Work? When Pretrain-SFT from 2D VLMs Meets 3D VLMs (arXiv 2506.05318, preprint) | Zeroing the 3D scene-encoder features leaves performance "largely unaffected" ("3D encoder idling"). The evidence is reported on QA and captioning metrics, and it proposes a 3D-RDVG grounding variant as training data. Not a grounding audit.
- Revisiting 3D LLM Benchmarks: Are We Really Testing 3D Capabilities? (arXiv 2502.08503; comment: ACL 2025 Findings) | "2D-Cheating" with rendered images. The paper text has no grounding benchmark (checked arXiv HTML).
- Do 3D Large Language Models Really Use 3D Evidence? (UNICORNS, arXiv 2610.24447) | Referential ambiguity and insufficient evidence conditions, but QA responses only.
- Token-Budgeted Candidate Retrieval for 3D Scene-Grounded VLMs: Category Names vs. Pairwise Geometry (arXiv 2610.14207; NeurIPS 2026 workshop, non-archival) | Category-name matching beats geometry for candidate retrieval on ScanRefer/Nr3D (R@10 0.864 vs 0.626 on ScanRefer, abstract). This is indirect evidence of a name shortcut, framed as context selection rather than a benchmark audit.
- Agreement versus Softmax under Spatial Disambiguation (arXiv 2610.14210; NeurIPS 2026 workshop, non-archival) | Reports object-level ECE on ScanRefer Unique/Multiple and an error decomposition (45.6% of Multiple errors are same-class wrong-instance). This concerns calibration, not benchmark validity. **Flag for the calibration/abstention cell:** it is the only box-level calibration analysis for 3D grounding seen in this search (non-archival preprint).
- ORD: Object-Relation Decoupling for Generalized 3D Visual Grounding (CVPR 2026, CVF page read) | A method that suppresses the "semantic shortcuts from entity names". It is not an audit.
- SeqAlign3DVG (arXiv 2608.30451; recorded in cell 3) | Critiques image-based 3D-VG benchmarks for "loose text-observation alignment". Recorded under cell 3 to avoid duplication.
- How Far Can We Go With Synthetic Data for Audio-Visual Sound Source Localization? (CVPR 2026, CVF page read) | Mentions "semantic misalignment" in real SSL datasets, but this is a training-data study, not an evaluation audit.
- Already in slice, not re-added: Multi3DRefer (zero-target descriptions), 3D-GRAND/3D-POPE (3D-LLM hallucination), Mo & Morgado 2022, Chen et al. ECCV-W 2024, Sun et al. ACM MM 2024, AVSBench-Robust, Seeing Sound/Hearing Sight.

**Could not verify**
- None of the hits are unverified.
- Not examined beyond the title (CVPR 2024 listing): "Viewpoint-Aware Visual Grounding in 3D Scenes". It may analyse view-dependent descriptions; check before claiming absence of a view-dependence audit.
- Not found: a peer-reviewed blind/text-only *grounding* baseline on ScanRefer or Nr3D/Sr3D (as opposed to QA). Also not found: an annotation-noise or label-error audit that quantifies erroneous ScanRefer/Nr3D descriptions. Beacon3D is the closest; it re-annotates test data and names ambiguous referential text as a flaw.

**Verdict**: partially filled.

(a) 3D grounding. Benchmark-validity work now exists:
- Beacon3D (CVPR 2025) audits flawed and ambiguous grounding test data and averaging metrics.
- P³-VLM (NeurIPS 2026) gives the first verified blind-LLM baseline on Nr3D/ScanRefer, showing box-coordinate "semantic leakage" in location-prompted 3D-VLM evaluation.
- ViGiL3D (ACL 2025) audits linguistic coverage.
- Earlier method papers document the object-name shortcut (EDA, CVPR 2023) and view-dependence annotation ambiguity in ReferIt3D (LanguageRefer, CoRL 2021).

What is still missing, as of 2026-11-17 in the sources listed:
- a language-only or blind baseline for the localisation task itself on ScanRefer, Nr3D/Sr3D or Multi3DRefer;
- a quantitative label-noise audit of ScanRefer/ReferIt3D descriptions.

"3D-LLMs perform similarly without 3D input" is documented only for QA and captioning (Real-3DQA, ICLR 2026; 3D-encoder-idling preprint).

(b) Sound-source localisation. Four further audits complement the slice:
- negative-audio evaluation flaws (Juanola et al., ICASSP 2025);
- a positive-only evaluation critique with a new metric (BMVC 2025);
- visible/single-source assumptions (AVATAR, ICCV 2025);
- AVS dataset bias (Chen et al., CVPR 2024).

This part of the cell is now well covered.
