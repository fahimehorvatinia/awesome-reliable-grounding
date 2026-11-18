# Reliability slice: systematic gap search log (Stage 2)

Date of search: 2026-11-17. Slice: reliability-interpretability.

Protocol per cell: at least 4 distinct searches across at least 3 source types (WebSearch standard/extended phrasing, alphaXiv semantic search `discover_papers`, Semantic Scholar Graph API, arXiv API listing search, Google Scholar MCP where available). Every hit added to `reliability.jsonl` was verified this session against an authoritative source (arXiv abs/API, CVF/ECVA/NeurIPS/ICLR/PMLR/ACL proceedings pages, or Crossref DOI). Inclusion criterion: the paper studies the cell's condition for a grounding-type output (box, mask, temporal interval, tube, 3D box/mask, sound-source map, or evidence region). Papers that study the condition only for classification/retrieval/QA/captioning are listed as near-misses. Semantic Scholar and arXiv APIs were intermittently rate-limited (HTTP 429) during the session; where a source was unavailable this is stated in the cell's query list.

Verdict scale: **gap confirmed** (no peer-reviewed or preprint work found that addresses the cell for grounding outputs) / **partially filled** (some work exists but covers only part of the cell, or only preprints) / **filled** (peer-reviewed work directly addresses the cell).

Cells are appended below as they are completed (order may differ from the numbering).


## Cell 1: No-target / absent-target protocols for spatio-temporal video grounding (STVG) and referring video object segmentation (RVOS) (adjacent: RMOT, audio-visual RVOS)

**Mandatory check: does MeViS TPAMI (ding2025mevistpami, DOI 10.1109/TPAMI.2025.3600507, arXiv 2512.10945) contain no-target expressions?** Yes. Verified from the arXiv HTML full text (v1; arXiv journal_ref and Crossref both give IEEE TPAMI 47(12):11400-11416, 2025):
- Sec. I (Introduction): "These additions include motion reasoning expressions, which involve implicit queries requiring complex reasoning, and no-target expressions, which are deceptive motion descriptions that relate to the video but do not refer to any actual object, as shown in Fig. 3."
- Sec. III-A (Motion Expression Annotation), guideline A5: "No-target expression must also describe motion like other single-/multi-target expressions, and cannot be entirely unrelated to the video. Annotators can derive no-target expressions by modifying existing single-/multi-target expressions." Validation rule V2 discards no-target expressions that are unrelated to the video or do not describe motion.
- Sec. III-B (Dataset Analysis and Statistics): MeViSv2 adds "3,503 no-target expressions that are deceptive but do not refer to any objects in the video", and "in previous version 'no-target expression' is not considered, leading to undefined behavior when the given sentence does not match any object in the given video."
- Sec. V (Experiments, Evaluation Metrics paragraph): "for samples where no target is present, true positives are assigned J and F value of 1, whereas false negatives are given J and F value of 0. Besides, N-acc. and T-acc. [GRES] are employed to assess the model's ability to identify no-target scenarios." N-acc = TP/(TP+FN) over no-target samples; T-acc = TN/(TN+FP) over target samples.
- Sec. V-C, Table VII: top-1-mask RVOS methods (URVOS, LBDT, MTTR, ReferFormer, VLT+TC) get N-acc 0.0 / T-acc 100.0; DsHmp 21.0/84.1; LMPM++ 45.7/87.4. Sec. V-E: HOTA is adapted to HOTA* so an empty trajectory on a no-target sample scores 1 (RMOT on MeViSv2, Table X); Sec. V-F: audio-guided VOS also reports N-acc/T-acc (Table XI; MUTR N-acc 0.0).
- **ICCV 2023 MeViS (ding2023mevis, arXiv 2308.08544)** has multi-object but **no** no-target expressions: the Fig. 3 caption says the number of targets "is arbitrary, from 1 to many", the guidelines (A1-A4) and metrics (J, F only) contain no no-target case, and the TPAMI text states the earlier version did not consider them.

**Queries** (source | exact query | #relevant results)
1. WebSearch (standard) | `referring video object segmentation "no-target" expressions benchmark N-acc T-acc` | 6 (MeViS TPAMI; 8th LSVOS MeViS-Text winner report; GREx; three 5th PVUW MeViS reports)
2. WebSearch (standard) | `spatio-temporal video grounding target absent "does not exist" query rejection benchmark` | 1 (Soccer-GMR, temporal only). OmniGround, OmniSTVG/BOSTVG, SVAG-Bench and VUE-STG were checked and assume the target is present.
3. alphaXiv discover_papers | keywords ["referring video object segmentation","no-target","spatio-temporal video grounding","nonexistent object"]; question "Referring video object segmentation or spatio-temporal video grounding benchmarks/methods that handle expressions referring to no object in the video (no-target, absent target, semantic mismatch, hallucination)" | 5 (arXiv 2610.06018, 2610.02946, 2608.11458, 2609.06078, 2603.14300)
4. WebSearch (standard) | `"Described Spatial-Temporal Video Detection" arXiv zero targets` | 1 (DSTVD / DVD-ST)
5. WebSearch (standard) | `referring multi-object tracking expressions with no target "zero" objects negative expressions dataset Refer-KITTI false positive` | 2 (Refer-KITTI-V2, YesTrack)
6. Semantic Scholar Graph API | `referring video object segmentation no-target nonexistent object robustness` and `spatio-temporal video grounding irrelevant query negative absent target` | S2: 429, not available (5 retries with 10 s back-off)
7. Google Scholar MCP | `referring video object segmentation expressions referring to nonexistent objects no-target hallucination` | 0 (tool returned an empty list)
8. arXiv API | `abs:"referring video" AND (abs:"no-target" OR abs:"nonexistent" OR abs:"non-existent" OR abs:"absent")` | arXiv API: HTTP 429, not available (arXiv abs/HTML pages were used for verification instead)
9. WebSearch (extended) | `"referring video" segmentation hallucination "non-existent" OR "nonexistent" objects benchmark robustness score 2025` | 3 (ReVOS hallucination subset; PVUW 2026 report on "forced mapping"; R2-Bench, already in slice)
10. alphaXiv discover_papers | keywords ["spatio-temporal video grounding","referring multi-object tracking","no target","rejection","hallucination"]; question "Video grounding (spatio-temporal tubes, referring tracking, MLLM video grounding) where the queried object may be absent and the model must reject or output nothing" | 3 (2610.06018 again; 2511.23151 already in slice; YesTrack). Near-miss: 2606.31187.

Candidate-specific full-text checks: R2-VOS (arXiv 2207.01203v3), VISA/ReVOS (arXiv 2407.11325v1), Ref-AVS (arXiv 2407.10957v1), OmniAVS (arXiv 2507.22886v2), DSTVD (arXiv HTML 2407.05610v1), Refer-KITTI-V2 (arXiv HTML 2406.05039v3), and the query-insensitive STVG study (arXiv 2610.06018v1).

**Verified hits**
- ding2025mevistpami | MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation | IEEE TPAMI 2025 | peer-reviewed | Crossref DOI + arXiv journal_ref + full text | 3,503 human-written deceptive no-target motion expressions, scored with N-acc/T-acc (RVOS, audio-guided VOS) and a no-target-aware HOTA* (RMOT). This is the largest no-target video referring benchmark found.
- li2023robust | Robust Referring Video Object Segmentation with Cyclic Structural Consensus (R2-VOS) | ICCV 2023 | peer-reviewed | Crossref DOI 10.1109/ICCV51070.2023.02032 + arXiv comment | First RVOS work to drop the "referred object must appear" assumption. Its R2-Youtube-VOS has ~10 negative expressions per video, plus the robustness score R and alignment accuracy A.
- yan2024visa | VISA: Reasoning Video Object Segmentation via Large Language Model(s) (ReVOS) | ECCV 2024 | peer-reviewed | ECVA page + DOI | ReVOS has 325 nonexistent-object queries for "hallucination evaluation", scored with R from R2-VOS. All methods stay at R <= 15.5.
- kolodziejczyk2026investigating | Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding | Findings of EMNLP 2026 | peer-reviewed | Crossref DOI 10.18653/2026.findings-emnlp.2423 (resolves to ACL Anthology) + arXiv 2610.06018 | The only STVG (tube) study of absent targets. TubeDETR and TA-STVG still output plausible tubes for irrelevant or empty queries (e.g. TA-STVG on HCSTVG-v2 keeps m_tIoU 0.476 vs 0.548). The authors call for negative-aware STVG protocols but propose no benchmark.
- ji2024described | Described Spatial-Temporal Video Detection (DSTVD / DVD-ST) | arXiv | preprint | arXiv abs; no peer-reviewed version found | Reformulates STVG so that a query can refer to zero, one or many objects. Its baselines add a three-state "exists and referenced / exists not referenced / does not exist" classifier.
- lee2026multiagent | Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026 | arXiv | preprint (challenge report) | arXiv abs | Shows that MeViSv2 no-target negatives are hard. Rejecting all of them on validation did not transfer to test, and an independent multi-agent existence audit "recovers most of the residual no-target errors".

**Existing-bibliography evidence (no new record written; keys already in existing_keys.tsv)**
- wang2024refavs (Ref-AVS, ECCV 2024; arXiv 2407.10957) **does** have a Null test subset. Sec. 3.6 (Dataset Split): "A 'null reference problem' arises when an expression refers to an object that either does not exist or is not visible in the given context ... the true masks for this subset are empty". Table 2 gives 257 videos and 1,028 expressions. Sec. 5.2 scores it with S, "the square root of the ratio between the predicted mask area and the background area" (lower is better). EEMC gets S = 0.007.
- ying2025omniavs (OmniAVS, ICCV 2025; arXiv 2507.22886): annotation rule "Expressions can refer to any number of objects, from none to many" (Sec. 3.2). Under Evaluation Metrics, "for no-target expressions ... J&F is set to 1 if the prediction is empty; otherwise, it is 0". OmniAVS also reports Ref-AVS Null S (OISA-1B 9.8, which the authors attribute to MLLM hallucination) and ReVOS R. A JSONL record could be added if the slice wants it.
- Already in slice (temporal-only analogues): flanagan2025moment (NA-VMR) and lee2026refuse (HI-VTG).

**Near-misses**
- MeViS (ICCV 2023; ding2023mevis) | multi-target only, no no-target expressions (see mandatory check).
- Referring Multi-Object Tracking with Diverse Dynamic Expressions / Refer-KITTI-V2 + TempRMOT (arXiv 2406.05039v3) | Sec. III-B: "we have included expressions unrelated to the video content to increase the benchmark difficulty". However, these are scored only with standard HOTA (Sec. V-A), with no no-target metric or analysis. Per MeViS TPAMI Sec. V-E, standard HOTA scores no-target samples as 0. Refer-Dance (iKUN, CVPR 2024) is described there as "94.86% of expressions are null"; not independently verified.
- YoURVOS: "Show Me When and Where: Towards Referring Video Object Segmentation in the Wild" (arXiv 2603.14300) | target-absent *frames* in untrimmed videos ("when" the object appears). The referred object always exists somewhere, so these are not no-target queries.
- FaVOS: "When Predicting Nothing Beats SAM 3" (arXiv 2610.02946; comment: NeurIPS 2026 E&D) | mask-prompted VOS, not language grounding. Relevant to metric design: on target-absent frames J&F rewards empty predictions, so "a trivial empty-mask predictor can outperform strong models such as SAM 3". The paper proposes Volumetric J&F.
- Soccer-GMR / Generalized Moment Retrieval (arXiv 2605.02623) | null-set rejection for temporal moments only (no spatial output). Verified on its arXiv abs, which resolves the slice's earlier "could not verify" entry.
- Temporal Sentence Grounding with Relevance Feedback (NeurIPS 2024, Dong et al.) | temporal-only absent-segment detection. Seen only as a reference in arXiv 2610.06018 and not independently verified.
- OmniSTVG/BOSTVG (arXiv 2503.10500) and OmniGround (arXiv 2511.16937) | multi-target or complex-query STVG with 1-10 targets per query, no absent targets.
- YesTrack (arXiv 2609.02318; comment: ECCV 2026) | per-candidate MLLM yes/no verification for RMOT on Refer-KITTI(-V2), with no no-target protocol.
- 2026 MeViS challenge reports (SaSaSaSa2VA arXiv 2603.27241; VIRST-Audio arXiv 2603.23126; AgentRVOS arXiv 2604.22836; 8th LSVOS report arXiv 2609.06078) | existence-aware gating or "target-presence judgment" on MeViSv2 no-target expressions. These are short technical reports that inherit the MeViSv2 protocol, so they serve as supporting evidence rather than separate protocols. VIRST-Audio swaps the N-acc/T-acc definitions, per a search snippet that was not checked in the paper.
- Learning to Deny / UCF101-AD (arXiv 2606.31187; comment: ECCV 2026) | action-denial benchmark for MLLM classification, not grounding.

**Could not verify**
- None of the hits. Semantic Scholar and the arXiv API were rate-limited for this cell, so the search relies on WebSearch, alphaXiv and full-text reads.
- Refer-Dance "94.86% null expressions" (second-hand from the Refer-KITTI-V2 text) and the VIRST-Audio metric-definition swap (search snippet) were not checked against the original papers.

**Verdict**: **partially filled.**
- **RVOS, including audio-visual RVOS:** this side is now filled by peer-reviewed protocols. These are R2-VOS (ICCV 2023, negative video-text pairs, robustness score R), ReVOS (ECCV 2024, 325 nonexistent-object queries, R), Ref-AVS Null (ECCV 2024, metric S), OmniAVS (ICCV 2025, binary J&F on no-target) and MeViSv2 (TPAMI 2025, 3,503 deceptive no-target expressions, N-acc/T-acc, and a no-target-aware HOTA* for RMOT). MeViSv2 is now a challenge track (PVUW/LSVOS 2026) whose winning entries rely on explicit existence verification.
- **Box/tube STVG:** as of 2026-11-17, the only peer-reviewed work is a diagnostic short paper (Findings of EMNLP 2026). It shows that TubeDETR and TA-STVG ground irrelevant or empty queries almost as confidently as real ones, but it releases no benchmark or rejection metric. The only zero-target STVG dataset (DSTVD/DVD-ST) is a 2024 preprint. No STVG benchmark with negative queries and a rejection metric, and no calibrated abstention for tubes, was found.
- **Metrics across RVOS benchmarks:** each benchmark scores no-target differently (R, S, N-acc/T-acc, binary J&F, HOTA*). No comparison or calibration analysis across these metrics was found.

## Cell 2: Missing modality in temporal grounding (missing audio / subtitles / ASR / speech at test time for moment retrieval, video temporal grounding, audio-visual event localisation, highlight detection) and in audio-visual LLM grounding

**Queries** (source | exact query | #relevant results)
1. WebSearch (standard) | `missing modality video temporal grounding moment retrieval audio absent at test time` | 2 (IMG arXiv 2508.04273; TriSense arXiv 2505.18110)
2. WebSearch (standard) | `audio-visual event localization missing modality robust incomplete audio visual` | 0 hits; 4 near-misses (Prompt the Missing CVPRW 2025; Retrieving to Recover AVQA; GLDTracker speaker tracking; PreFM event parsing)
3. alphaXiv discover_papers | "Moment retrieval, video temporal grounding or highlight detection evaluated when the audio, speech, ASR or subtitle modality is missing at test time (missing modality robustness)" | 2 (TSMD 2609.39051, borderline; AVTrace 2609.19991)
4. arXiv API | `all:"missing modality" AND (all:"moment retrieval" OR all:"temporal grounding" OR all:"highlight detection")` and `all:"missing audio" AND (all:localization OR all:grounding OR all:retrieval)` | first attempt HTTP 429 x5, failed; retried later as `all:"missing modality" AND (all:"moment retrieval" OR all:"temporal grounding" OR all:"event localization" OR all:"highlight detection")` | 0 results (total 0)
5. Semantic Scholar API | `missing modality moment retrieval` | 1 (IMG, ACM MM 2025); others not grounding
6. Semantic Scholar API | `missing audio audio-visual event localization` / `modality dropout audio-visual temporal grounding` / `missing subtitle video corpus moment retrieval` / `audio-visual large language model temporal grounding missing audio` | all HTTP 429 after 5 retries, not available
7. Semantic Scholar API | `incomplete modality video temporal grounding` | 0 relevant (20 generic VTG papers)
8. Semantic Scholar API | `audio-visual event localization missing modality` | 1 (Both-or-Neither, ACM MM 2026 workshop)
9. Google Scholar MCP | `missing modality moment retrieval audio absent inference`; `audio-visual event localization missing modality` | 0 (tool returned empty lists; not functional)
10. alphaXiv discover_papers | "Audio-visual event localization or audio-visual video parsing evaluated with a missing or absent modality (missing audio or missing visual frames) at test time" | 1 (Fang et al. 2605.27894 = AAAI 2026); near-misses MiDl, AVQA-missing, UWAV
11. alphaXiv discover_papers | "Audio-visual large language models that perform temporal or spatial grounding, evaluated with the audio stream removed or one modality missing" | 1 (AVTrace); near-misses TiTok, RVG-Bench, OmniGround, OmniCompass
12. WebSearch (standard) | `TVR video subtitle moment retrieval "subtitle only" "video only" ablation missing subtitles robustness` | 0 hits (TVR / SQuiDNet design ablations only)
13. WebSearch (extended) | `modality dropout audio-visual temporal grounding robustness missing audio video LLM 2025` | 1 (TriSense = NeurIPS 2025); near-misses Multifaceted AV eval (EMNLP Findings 2025), PU-VALOR
14. WebSearch (extended) | `"audio-visual event localization" "missing modality" OR "modality missing" OR "incomplete modalities"` | 0 hits (Segment Beyond View AAAI 2024 as adjacent)
15. WebSearch (standard) | `egocentric moment localization missing audio modality test-time Ego4D natural language query audio` | 0 hits (MiDl ICLR 2025 = action recognition only)
Also checked full text (arXiv HTML) of Meerkat (2407.01851), TiTok (2610.09408), RVG-Bench (2610.32268), OmniGround (2610.25929) for audio-removed grounding results.

**Verified hits**
- lin2025audio | Audio Does Matter: Importance-Aware Multi-Granularity Fusion for Video Moment Retrieval | ACM MM 2025 | peer-reviewed | Crossref DOI 10.1145/3746027.3754982 + arXiv abs 2508.04273 | VMR with audio-visual-text fusion; cross-modal knowledge distillation so the visual branch works "when audio modality is missing during inference"; Table 3 reports Charades-STA with audio missing (visual branch) vs fused.
- li2025watch | Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM (TriSense) | NeurIPS 2025 | peer-reviewed | NeurIPS proceedings page (DOI 10.52202/085713-4307) + arXiv abs 2505.18110 | AV-LLM for moment retrieval and segment captioning trained with modality dropout; evaluates MR under four modality settings (audio-visual-speech, visual-speech, audio-visual, visual-only).
- fang2026towards | Towards Unified Vision-Language Models with Incomplete Multi-Modal Inputs | AAAI 2026 | peer-reviewed | Crossref DOI 10.1609/aaai.v40i5.37387 + arXiv abs 2605.27894 | Plug-in completion module for video-language models evaluated on video sentence grounding (Charades-STA, ActivityNet Captions, TACoS) with 30% missing video frames and query text at train and test time.
- tynchenko2026both | Both-or-Neither: Counterfactual Joint-Evidence Auditing for Reliable Audio-Visual Event Localization | Proc. 1st Int. Workshop on Joint Audio-Video Comprehension and Generation (ACM MM 2026 workshop) | workshop | Crossref DOI 10.1145/3840475.3841438 (abstract via Semantic Scholar record) | Audits AVE event localisation under "modality removal, same-class and cross-class replacement, and temporal audio shifts"; reports "unimodal leakage".
- zhang2026avtrace | AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models | arXiv | preprint | arXiv abs 2609.19991 (no venue in comments) | Omni-model temporal grounding benchmark (onset/span grounding, cross-modal localisation); development-set perturbations remove input streams and show drops on span grounding, largest with text alone (Qwen3-Omni-30B only; figure, no table).

**Near-misses**
- TSMD: Temporal-Stream Modality Dropout for Robust Video Highlight Detection (arXiv 2609.39051, preprint) | Studies temporal and whole-stream missingness of visual/audio/text streams, but for *query-free* highlight scoring / summarisation (MoSu, Mr. HiSum); no language-conditioned grounding output. Closest adjacent work for "highlight detection".
- TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding (arXiv 2610.09408, ACCV 2026 per comment) | type (b): "w/o audio" is a training-time ablation (UnAV-100 mIoU drops), not a test-time missing-audio evaluation.
- TVR: A Large-Scale Dataset for Video-Subtitle Moment Retrieval (ECCV 2020, arXiv 2001.09099) and SQuiDNet (arXiv 2210.08714) | type (b): video-only vs subtitle-only model variants trained separately; not robustness to subtitles missing at test time (seen via search snippets; not re-opened).
- RVG-Bench (arXiv 2610.32268) | compares audio-visual vs visual-only *models*, no within-model modality removal.
- MEERKAT (ECCV 2024, key chowdhury2024meerkat) | audio removal is reported only for AVQA (appendix Table 16), not for its grounding tasks (type c).
- MissRAG (ICCV 2025) | already in slice; AV-QA / captioning only (type c).
- Test-Time Adaptation for Combating Missing Modalities in Egocentric Videos / MiDl (ICLR 2025, arXiv 2404.15161) | missing audio/video at test time, but evaluated only on action recognition (Epic-Kitchens, Epic-Sounds, Ego4D-AR); abstract mentions moment localisation only as motivation (type c).
- Exploring Missing Modality in Multimodal Egocentric Datasets (arXiv 2401.11470) | action recognition only (type c).
- Learning Trimodal Relation for AVQA with Missing Modality (arXiv 2407.16171) and Retrieving to Recover (arXiv 2604.10695) | AVQA only (type c).
- Prompt the Missing (CVPR 2025 Workshops) | AV classification only (type c).
- Multifaceted Evaluation of Audio-Visual Capability for MLLMs (Findings of EMNLP 2025) | missing/shifted video for AV-QA, not grounding (snippet only).
- Segment Beyond View (AAAI 2024, arXiv 2312.08673) | partially missing visual field of view for audio-visual *semantic segmentation* (spatial masks), outside the temporal / AV-LLM scope of this cell; relevant to an AV-segmentation missing-modality cell.
- GLDTracker (arXiv 2408.14585) | AV speaker tracking with incomplete modalities; spatial tracking, not language/temporal grounding.
- UWAV (arXiv 2505.09615) | audio-visual video parsing method; its abstract reports no missing-modality test.
- PreFM (streaming audio-visual event parsing) | seen only in a WebSearch snippet ("modality-agnostic robust representation"); abstract not read, so not assessed.
- OmniGround (arXiv 2610.25929) | omni-modal temporal grounding, no modality-removal evaluation found in full text.

**Could not verify**
- None of the hits. Semantic Scholar and arXiv APIs were rate-limited for several queries (logged above), so coverage relies more on WebSearch and alphaXiv.

**Verdict**: partially filled. Peer-reviewed work now evaluates temporal grounding with a modality missing at inference: IMG (ACM MM 2025) for missing audio in moment retrieval, TriSense (NeurIPS 2025) for moment retrieval under audio/speech dropout in an AV-LLM, and Fang et al. (AAAI 2026) for partially missing video/query input in sentence grounding. A workshop paper (ACM MM 2026 workshop) audits AVE localisation under modality removal, and one preprint (AVTrace) probes omni-model temporal grounding with input streams removed. Still missing as of 2026-11-17 (searched with WebSearch, alphaXiv, Semantic Scholar, arXiv API): any study of missing subtitles / ASR at test time for video-subtitle moment retrieval (TVR-style), a standard missing-modality protocol or benchmark for AV temporal grounding (each paper uses its own setting), and AV-LLM *spatial* or spatio-temporal grounding with audio absent. Meerkat-style AV-LLMs report audio removal only for QA.

## Cell 5: Conflicting modalities in 3D grounding (point cloud vs multi-view images vs text disagree) and in temporal grounding (speech / subtitles / audio disagree with the visual stream)

**Queries** (source | exact query | #relevant results)
1. alphaXiv discover_papers | "3D visual grounding or 3D-LLMs under modality conflict: point cloud and multi-view images disagree, or the text description contradicts the 3D scene (false premise)" | 0 hits; near-misses MCM-VG (2604.26261), Talk2Sensors (2608.04568), counterfactual-caption anisotropy study (2605.09090), Senses Wide Shut (2605.13737), PVFH-Bench (2610.14635), FPCO-Dialog (2609.03331)
2. alphaXiv discover_papers | "Audio-visual temporal grounding or video moment retrieval when audio, speech or subtitles conflict with or are misaligned with the visual stream (counterfactual or mismatched audio)" | 0 grounding hits; near-misses Thud / "When Vision Speaks for Sound" (2605.16403), Compositional Failure (2608.27785), Tri-PvP (2609.06011), Local Evidence Global Failure (2610.25352), One Waveform Two Stories (2611.00325), Beyond Text Following (2606.05161)
3. Semantic Scholar API | `3D visual grounding modality conflict point cloud image`; `audio-visual conflict temporal grounding misaligned audio`; `false premise 3D visual grounding`; `subtitle visual conflict video grounding` | all HTTP 429 after 5 retries, not available
4. Semantic Scholar API (cell-2 query, cross-cell) | `audio-visual event localization missing modality` | 1 (Both-or-Neither, which also tests cross-class replacement = conflict)
5. WebSearch (extended) | `3D visual grounding false premise nonexistent object misleading description 3D-LLM hallucination benchmark point cloud` | 0 hits; 3D-POPE / 3D-GRAND (already in slice), 3DVerifierBench (2610.22360), 3D-VCD, an aggregator-only 3D-VLM hallucination study
6. WebSearch (standard) | `audio-visual misalignment counterfactual audio swap temporal grounding moment retrieval robustness mismatched audio video LLM` | 0 hits (Thud only)
7. WebSearch (standard) | `subtitles contradict visual content video grounding OR moment retrieval "subtitle" misleading OR inconsistent OR conflicting benchmark` | 0 (TVR, HERO, VERIFIED: subtitles assumed helpful)
8. arXiv API | `all:"3D visual grounding" AND (all:conflict OR all:"false premise" OR all:inconsistent OR all:contradict)` | 1 result (ViewSRD), 0 relevant
9. arXiv API | `all:"audio-visual" AND (all:"temporal grounding" OR all:"moment retrieval" OR all:"event localization") AND (all:conflict OR all:mismatched OR all:misaligned OR all:counterfactual)` | 4 results, 1 relevant (AVID 2604.13593)
10. arXiv API | `(all:"visual grounding" OR all:"referring") AND all:LiDAR AND (all:conflict OR all:"sensor failure" OR all:corruption OR all:robustness)` | 85 results, 0 conflict studies (Talk2Sensors adjacent)
Google Scholar MCP returned empty lists in cell 2 and was not used further. Full text (arXiv HTML) checked for Thud (2605.16403), Talk2Sensors (2608.04568) and AVID (2604.13593).

**Verified hits**
- tynchenko2026both | Both-or-Neither: Counterfactual Joint-Evidence Auditing for Reliable Audio-Visual Event Localization | Proc. 1st Int. Workshop on Joint Audio-Video Comprehension and Generation (ACM MM 2026 workshop) | workshop | Crossref DOI 10.1145/3840475.3841438 (abstract via Semantic Scholar record) | AVE event localisation audited under "same-class and cross-class replacement, and temporal audio shifts"; reports and reduces "cross-modal conflict acceptance" (also cell 2).
- chen2026avid | AVID: A Benchmark for Omni-Modal Audio-Visual Inconsistency Understanding via Agent-Driven Construction | arXiv | preprint | arXiv abs 2604.13593 (v2, no venue) | Injects audio-visual conflicts into long videos (39.4K inconsistency events, 8 categories) and evaluates omni-models on temporally grounding the inconsistent segments (R@IoU, mIoU) as well as detection, classification and reasoning.

**Near-misses**
- When Vision Speaks for Sound / Thud (arXiv 2605.16403, preprint) | counterfactual audio Shift / Mute / Swap for video MLLMs; output is a synchronisation/consistency judgement with self-reported timestamps, scored as QA, not grounding IoU. Closest temporal-conflict probe.
- Senses Wide Shut / IMAVB (arXiv 2605.13737) | textual premise contradicts what the omni-model sees or hears; QA rejection, not grounding.
- Compositional Failure in Audio-Visual LLMs (arXiv 2608.27785, ICML 2026 Compositional Learning workshop per comment) | AV conflict as yes/no matching on AVHBench; no grounding output.
- Tri-PvP (arXiv 2609.06011, EMNLP 2026 Findings per comment) | vision-audio-text conflict benchmark; QA only.
- Local Evidence, Global Failure (arXiv 2610.25352) | speech-vision temporal composition on SVHalluc; QA accuracy.
- One Waveform, Two Stories (arXiv 2611.00325) and Beyond Text Following (arXiv 2606.05161) | speech-vs-acoustic or text-vs-audio conflict in audio-language models; no visual grounding.
- AVTrace (arXiv 2609.19991; cell-2 hit) | Cat3 A/V synchronisation verification is yes/no, not grounding under conflict.
- AVHBench, Seeing Sound Hearing Sight, Words or Vision, MMMC, AVSBench-Robust | already in slice (not re-added).
- 3D-GRAND / 3D-POPE (CVPR 2025) | already in slice; existence polling, not point-cloud vs image conflict.
- Grounding Generative Verification in 3D Content / 3DVerifierBench (arXiv 2610.22360) | verifies generated 3D assets against specifications (multi-view, contradiction explanations); not scene grounding.
- Multiple Consistent 2D-3D Mappings (MCM-VG, arXiv 2604.26261) | enforces 2D-3D consistency to fix noisy 3D proposals in zero-shot 3DVG; no evaluation under conflicting inputs.
- Talk2Sensors (arXiv 2608.04568) | camera/LiDAR/4D-radar 3DVG for driving with inference-time *sensor dropout* (Fig. 8b); missing modality, not conflicting sensors. Adjacent; relevant to a 3D/driving missing-modality cell.
- Investigating Anisotropy in Visual Grounding under Controlled Counterfactual Perturbations (arXiv 2605.09090, CVPR 2026 XAI4CV workshop per comment) | mismatched captions for 2D REC (TransVG, SwimVG); 2D, not 3D or temporal.
- PVFH-Bench (arXiv 2610.14635), FPCO-Dialog (arXiv 2609.03331) | 2D false-premise hallucination / dialogue, not grounding outputs in 3D or video (abstract snippets only).

**Could not verify**
- "Understanding and Evaluating Hallucinations in 3D Visual Language Models" (random point-cloud/question pairing, "visual neglect"): seen only on an aggregator (Lacuna); no arXiv or proceedings page found. Not recorded.
- 3D-VCD: Hallucination Mitigation in 3D-LLM Embodied Agents through Visual Contrastive Decoding (arXiv 2604.08645; "CVPR 2026" claimed by a search summary): venue not checked. Near-miss in any case (HEAL distractor injection for embodied planning, not grounding).

**Verdict**: partially filled (3D half: gap confirmed; temporal half: partially filled). **3D:** no work found as of 2026-11-17 (sources: alphaXiv, WebSearch, arXiv API; Semantic Scholar rate-limited) that tests 3D visual grounding when point clouds, multi-view images and text disagree, or that evaluates false-premise 3D referring expressions with a rejection/no-box output. 3D-POPE probes object existence only. Multi-sensor driving grounding (Talk2Sensors) tests sensor dropout, not sensor disagreement. **Temporal:** two works localise in time under audio-visual conflict. One is a workshop audit of AVE localisation under cross-class audio/visual replacement and audio shifts (Both-or-Neither, ACM MM 2026 workshop). The other is a preprint benchmark that asks omni-models to temporally ground injected AV inconsistencies (AVID; best mIoU 26.2 for Gemini 3.1 Pro before fine-tuning). Counterfactual-audio and premise-conflict studies of AV-LLMs (Thud, IMAVB, Tri-PvP, AVHBench) score QA rather than grounding. No work was found on query-conditioned moment retrieval when subtitles/ASR contradict the visual stream.

## Cell 3: Missing or degraded inputs in 3D visual grounding (3D-VG, 3D-RES, 3D-LLM grounding)

Scope searched: missing RGB/colour, missing depth, sparse or few views, partial scans, point-cloud corruption/noise/occlusion, sensor degradation (incl. LiDAR/radar grounding under adverse weather as adjacent). Searches run 2026-11-17.

Inclusion policy used: a hit either (a) evaluates a grounding-type 3D output (3D box/mask, affordance mask) under a controlled test-time removal or corruption of an input, or (b) defines a grounding task/benchmark whose stated challenge is an incomplete observation (partial scan, sparse views, no depth). Papers that only use a different sensor regime (e.g. image-only zero-shot 3D-VG) without studying degradation are near-misses. Training-time input-feature ablations (e.g. ScanRefer xyz vs. xyz+rgb) are near-misses: they are design ablations, not test-time missing-input studies.

**Queries** (source | exact query | #relevant results)
1. WebSearch | `3D visual grounding robustness point cloud corruption benchmark` | 1 (HAMMER, which led to GEAL's corruption protocol; ModelNet40-C is classification only)
2. alphaXiv discover | "3D visual grounding under missing or degraded inputs: point cloud corruption, missing RGB colour, sparse views, partial scans, robustness of 3D referring segmentation and 3D-LLM grounding" (keywords: 3D visual grounding, robustness, point cloud corruption, ScanRefer) | 0 hits (SpaceDG is a near-miss; the rest are nominal 3D-VG methods)
3. arXiv API | `all:"visual grounding" AND all:3D AND all:robustness` | 3 (Talk2Sensors, SpeechRefer, plus near-misses Cross3DVG, MCM-VG, camera-robust 3D localisation)
4. arXiv API | `abs:"3D visual grounding" AND abs:corruption`; `... AND abs:"partial"`; `... AND abs:"without point cloud"` | not available (HTTP 429 every attempt)
5. Semantic Scholar API | `3D visual grounding robustness corrupted point clouds` | not available (HTTP 429, 5 retries with 10 s back-off)
6. Google Scholar MCP | `3D visual grounding robustness noisy point cloud missing color sparse views` | 0 (empty result)
7. WebSearch | `GEAL generalizable 3D affordance learning cross-modal consistency corruption benchmark` | 1 (GEAL)
8. WebSearch | `3D visual grounding from RGB images only without point cloud zero-shot VLM-Grounder` | 0 hits (VLM-Grounder is a near-miss)
9. WebSearch (extended) | `"3D visual grounding" "point cloud" noise OR occlusion OR "missing color" robustness evaluation ScanRefer Nr3D 2025` | 0 (InstanceRefer and others mention noise/occlusion only as motivation)
10. WebSearch | `online 3D visual grounding partial observation streaming RGB-D incremental reconstruction embodied agent` | 1 (Refer-It-in-RGBD; OnlineSI is a near-miss)
11. alphaXiv discover | "Do 3D LLMs or 3D VG models stay robust when point clouds are noisy, occluded, partially scanned, or when colour/depth is missing? ..." | 1 (Talk2Sensors; UNICORNS is a near-miss)
12. WebSearch | `LiDAR language grounding adverse weather robustness 3D referring expression autonomous driving fog rain` | 0 with a weather evaluation (Talk2PC, Talk2Radar, 3EED, LiDAR Grounding)
13. alphaXiv discover | "Language-guided 3D object grounding with LiDAR, 4D radar or camera under adverse weather, night, sensor failure or missing sensor modality" | 0 grounding hits (results were detection, occupancy and MCQ benchmarks)
14. alphaXiv discover | "3D visual grounding or 3D referring segmentation from sparse views, few images, or single view without full scene reconstruction or depth" | 2 (MVGGT, SeqAlign3DVG; Z3D is a near-miss)
15. alphaXiv discover | "robustness benchmark for 3D LLMs or point cloud language models under point cloud corruptions, perturbations, noise, dropout, occlusion" | 0 (classification benchmarks; one adversarial 3D-VLM study)
16. WebSearch | `WaterVG waterway visual grounding mmWave radar adverse weather night evaluation` | 0 (NanoMVG "harsh environments" claim only)
17. CVF Open Access title scan (regex over all CVPR 2024, CVPR 2025, ICCV 2025 and CVPR 2026 titles for 3D/point/LiDAR/radar together with grounding/referring/segmentation words) | 3 (LangRef3DGS, Affostruction; HAMMER and MVGGT confirmed)

**Verified hits**
- liu2021referitinrgbd | Refer-It-in-RGBD: A Bottom-Up Approach for 3D Visual Grounding in RGBD Images | CVPR 2021 | peer-reviewed | CVF page + arXiv 2103.07894 | 3D-VG in single-view RGB-D where referents are "often only partially scanned due to occlusion". The method is designed for partial geometry.
- lu2025geal | GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency | CVPR 2025 | peer-reviewed | CVF page + arXiv HTML 2412.09511 | Introduces the PIAD-C and LASO-C corruption benchmarks: 7 point-cloud corruptions × 5 severities, covering both question-conditioned (LASO) and image-conditioned (PIAD) 3D affordance grounding.
- yao2026hammer | HAMMER: Harnessing MLLMs via Cross-Modal Integration for Intention-Driven 3D Affordance Grounding | CVPR 2026 | peer-reviewed | CVF page + arXiv 2603.02329 | Constructs a corrupted benchmark ("noise-infused point clouds") for MLLM-based, image-conditioned 3D affordance grounding.
- wu2026mvggt | MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation | CVPR 2026 | peer-reviewed | CVF page + arXiv 2601.06874 | Defines 3D-RES from a few sparse RGB views without a dense point cloud (MVRefer benchmark). It notes that reconstruct-then-segment pipelines yield "degraded target regions".
- ye2026langref3dgs | LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting | CVPR 2026 | peer-reviewed | CVF page | Language-guided 3D segmentation from "sparse and occluded" RGB-D views. Reports "robustness to partial inputs". Prompts appear to be category-level.
- park2026affostruction | Affostruction: 3D Affordance Grounding with Generative Reconstruction | CVPR 2026 | peer-reviewed | CVF page (arXiv 2601.09211) | Grounds text-described affordances from partial RGB-D, including unobserved surfaces, via generative reconstruction.
- guan2026talk2sensors | Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching | arXiv | preprint | arXiv abs + HTML | The only verified 3D-VG work with an inference-time missing-sensor test. Removing the camera, radar or LiDAR costs TSFormer −5.17 mAP (camera) and −4.34 mAP (radar); FUTR3D loses −7.64 and −4.56; both collapse without LiDAR. Adverse weather and night are explicitly left as future work.
- qi2025speak | I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs | arXiv | preprint | arXiv abs | 3D-VG under noisy speech-to-text transcripts. This is query-side degradation, so it is an adjacent hit.
- zhang2026seqalign3dvg | SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding | arXiv (comment: ACM MM 2026, not confirmed) | preprint | arXiv abs | Image-based 3D-VG under a depth-free protocol, with expressions strictly aligned to the partial RGB observations provided.

**Near-misses**
- ScanRefer (existing key chen2020scanrefer; arXiv 1912.08830 Sec. 6.4) | Training-time input-feature ablation, with separately trained models, not a test-time missing input. Overall val Acc@0.25/0.5 is 36.01/23.76 for xyz only, 36.50/23.61 for xyz+rgb, and 40.84/26.23 for xyz+multiview (ar5iv table). So raw colour adds almost nothing, while multi-view image features help.
- VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding (CoRL 2024; arXiv 2410.13860) | Uses image sequences plus depth and poses instead of a reconstructed point cloud. This is an input-regime choice for zero-shot grounding. The only degradation discussion is noisy camera parameters and depth, given as the reason for its Acc@0.25/0.5 gap; no controlled degradation study.
- Z3D: Zero-Shot 3D Visual Grounding from Images (arXiv 2602.03361) | Images-only regime, with optional poses and depth. No degradation study in the abstract.
- SeeGround (existing key li2025seeground, CVPR 2025) | Renders query-aligned views from the full point cloud. No missing-input evaluation.
- Mono3DVG (existing key zhan2024mono3dvg) | Monocular, depth-free outdoor 3D-VG. Input regime, not a degradation study.
- Cross3DVG: Cross-Dataset 3D Visual Grounding on Different RGB-D Scans (3DV 2024, DOI 10.1109/3dv62453.2024.00033) | Cross-sensor and cross-reconstruction domain shift (ScanNet→3RScan). This is G = domain/sensor shift, not missing or degraded input.
- Towards Camera-Robust 3D Localization: Equation-Anchored Tool-Use for MLLMs (arXiv 2605.19528) | MLLM 3D detection and grounding under rescaled camera intrinsics (0.5×–1.5×). Sensor-parameter shift, not missing or degraded data.
- Multiple Consistent 2D-3D Mappings for Robust Zero-Shot 3D Visual Grounding (MCM-VG, arXiv 2604.26261) | "Robust" refers to noisy open-vocabulary 3D proposals, not degraded inputs.
- OnlineSI: Taming Large Language Model for Online 3D Understanding and Grounding (arXiv 2601.16538) | Online grounding from a video stream with bounded memory. Partial observation is inherent, but the abstract states no controlled missing or degraded input evaluation.
- 3EED: Ground Everything Everywhere in 3D (NeurIPS 2025 D&B; arXiv 2511.01755) | Outdoor LiDAR+RGB grounding with cross-platform shift. No weather or sensor-degradation evaluation in the abstract.
- Talk2Radar (existing key guan2025talk2radar) | The text calls radar "immune to adverse weather conditions" (arXiv 2405.12821 HTML), but no weather-stratified evaluation.
- Talk2PC: Enhancing 3D Visual Grounding through LiDAR and Radar Point Clouds Fusion for Autonomous Driving (arXiv 2503.08336) | LiDAR+radar fusion. No degradation or weather evaluation in the abstract.
- WaterVG (arXiv 2403.12686) and NanoMVG (arXiv 2408.17207) | Camera + 4D radar 2D grounding (adjacent). NanoMVG claims performance "particularly in harsh environments", but I found no weather-stratified protocol in the paper text.
- SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation (arXiv 2605.22536) | Nine rendered degradations, but QA only.
- ObsDriveBench (arXiv 2607.23537) | Adverse-weather camera/LiDAR/radar benchmark. Multiple-choice QA only.
- Do 3D Large Language Models Really Use 3D Evidence? (UNICORNS, arXiv 2610.24447) | "Insufficient scene evidence" condition, but 3D-QA only.
- On the Adversarial Robustness of 3D Large Vision-Language Models (arXiv 2601.06464) | Adversarial attack (not corruption) on PointLLM/GPT4Point captioning and classification.
- Benchmarking Robustness of 3D Point Cloud Recognition Against Common Corruptions (ModelNet40-C, arXiv 2201.12296) | Corruption benchmark for classification only.
- Partially Matching Submap Helps: Uncertainty Modeling and Propagation for Text to Point Cloud Localization (ICCV 2025, title seen in CVF listing) | Text-to-point-cloud localisation of the agent's own position from partial submaps. Not object grounding, and only the title was checked.
- R²-Bench (existing key li2024r2bench) | Already in slice. Covers perturbations across referring tasks.

**Could not verify**
- SeqAlign3DVG's ACM MM 2026 acceptance: arXiv comment only, and the Crossref lookup was rate-limited. It is recorded as a preprint.
- Peer-reviewed versions of Talk2Sensors, SpeechRefer and OnlineSI: Crossref returned HTTP 429. No venue is stated on arXiv.

**Verdict**: partially filled.
- **What exists.**
  - Controlled test-time degradation of the 3D input has been studied for object-level 3D affordance grounding: point-cloud corruption benchmarks PIAD-C/LASO-C (GEAL, CVPR 2025) and HAMMER's corrupted benchmark (CVPR 2026).
  - For outdoor multi-sensor 3D-VG there is one preprint (Talk2Sensors, 2026) with inference-time modality dropout.
  - Partial or sparse observation has been addressed as a task formulation: single-view partial RGB-D (Refer-It-in-RGBD, CVPR 2021), sparse-view 3D-RES (MVGGT, CVPR 2026), partial-view 3DGS referential segmentation (LangRef3DGS, CVPR 2026), affordance grounding on unobserved surfaces (Affostruction, CVPR 2026), and a depth-free image-based benchmark (SeqAlign3DVG, preprint).
  - Query-side degradation (noisy speech) has one preprint (SpeechRefer).
- **What is still missing.** As of 2026-11-17, in the sources listed above, we found no study of scene-level referring 3D-VG, 3D-RES or 3D-LLM grounding (ScanRefer / ReferIt3D / Multi3DRefer family) under:
  - test-time point-cloud corruption or noise;
  - removal of colour or RGB features;
  - depth noise;
  - controlled reduction of scan coverage against a full-scan reference.

  Missing colour has been examined only as a training-time feature ablation (ScanRefer). We also found no LiDAR/radar 3D grounding evaluation under real or simulated adverse weather: Talk2Sensors explicitly defers it, and Talk2Radar only asserts radar's weather robustness.

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

## Cell 9: Evidence verification / traceable evidence for video, audio-visual, or 3D grounding (answers that cite temporal, spatio-temporal or 3D evidence that is checked against ground truth)

**Queries** (source | exact query | #relevant results)
1. WebSearch (standard) | `grounded video question answering temporal evidence benchmark answer-grounding consistency NExT-GQA CG-Bench ReXTime V-STaR` | 7 (NExT-GQA, ReXTime, CG-Bench, V-STaR, VideoZeroBench, LOVER, Zoom-Zero)
2. alphaXiv discover_papers | keywords ["grounded video question answering","temporal evidence","spatio-temporal evidence","evidence grounding reward"]; question "Video reasoning models or benchmarks where answers must cite temporal or spatio-temporal evidence (timestamps, boxes, tubes) and the cited evidence is scored or verified against ground truth" | 12 (Open-o3-Video-v2, EG-VQA, LOVER, GroundFormer, Evidence-Backed VideoQA, VideoZeroBench, VideoLVR, multi-agent RL, ASSEMBLE, TRACE, STSG-VQA, Video-HolmesV2)
3. alphaXiv discover_papers | keywords ["3D question answering","grounded reasoning","3D visual grounding","audio-visual question answering","evidence"]; question "3D scene or audio-visual question answering / reasoning where the model must also localize the supporting evidence (3D boxes of answer-related objects, sounding regions, temporal segments) and that evidence is evaluated" | 6 (EvaOmni, ANCHOR, Inter-3D VQA, LOVER, Evidence-Backed VideoQA, TEMA (audio only)); others were spatial-audio benchmarks without evidence scoring
4. WebSearch (standard) | `3D question answering grounded answer objects bounding box evidence evaluated ScanQA "answer grounding" OR "grounded reasoning" 3D-LLM chain-of-thought boxes benchmark 2025` | 2 (ScanQA, FE-3DGQA)
5. alphaXiv discover_papers | keywords ["3D scene","grounded chain-of-thought","3D question answering","3D-LLM","evidence boxes"]; question "3D scene reasoning or 3D question answering methods/benchmarks that require explicit grounded evidence (3D boxes/objects per reasoning step) and evaluate answer-evidence consistency or grounding of the rationale" | 4 (SceneCOT, UNICORNS, Scene-R1, Inter-3D VQA)
6. Google Scholar MCP | `grounded video question answering temporal evidence verification benchmark` | 0 (tool returned an empty list)
7. Semantic Scholar Graph API | `audio-visual question answering grounded evidence temporal localization benchmark` | S2: 429, not available (5 retries with 10 s back-off)

Venue checks: CVF pages (NExT-GQA, ScanQA, V-STaR); the ICLR 2025 and 2026 proceedings (CG-Bench, SceneCOT); the NeurIPS 2024 D&B proceedings (ReXTime); the ICML 2026 virtual poster page (Open-o3-Video); Crossref (FE-3DGQA). The ECVA listing has no ECCV 2026 papers yet.

**Verified hits**
- xiao2024can | Can I Trust Your Answer? Visually Grounded Video Question Answering (NExT-GQA) | CVPR 2024 | peer-reviewed | CVF page | Answers must come with temporal evidence, scored by Acc@GQA (correct and IoP>=0.5). The best method reaches only 17.5 Acc@GQA vs 70.8 QA accuracy (human 82.1). Sampling frames outside the ground-truth evidence barely changes QA accuracy.
- chen2025cgbench | CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding | ICLR 2025 | peer-reviewed | ICLR proceedings page | White-box clue-interval grounding (mIoU, acc.@IoU) plus a black-box Clue Recovery Rate. GPT-4o drops from 45.2 MCQ accuracy to 4.38 acc.@IoU.
- chen2024rextime | ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos | NeurIPS 2024 D&B | peer-reviewed | NeurIPS proceedings page + DOI | Models must output the answer's time span, scored by Accuracy@IoU>=0.5. GPT-4o gets 73.67 VQA accuracy but 28.67 joint (human 58.51).
- cheng2026vstar | V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning | CVPR 2026 Findings | peer-reviewed | CVF page | Scores what/when/where chains jointly. Video-LLMs answer "what" well but fail the "when" and "where" grounding steps.
- meng2026openo3 | Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence | ICML 2026 | peer-reviewed | ICML virtual poster page + arXiv | RL with temporal and spatial evidence rewards makes reasoning traces "traceable and verifiable" (timestamps plus boxes). The traces are also used for confidence-aware test-time scaling.
- meng2026videozerobench | VideoZeroBench: Probing the Limits of Video MLLMs with Spatio-Temporal Evidence Verification | arXiv | preprint | arXiv abs | A five-level protocol with evidence hints. No model exceeds 1.8% when the answer and the spatio-temporal evidence must both be correct.
- seo2026what | What You Ask is What You Ground (GroundFormer) | arXiv (comment: accepted at ECCV 2026) | preprint | arXiv abs | Shows "question-invariant grounding": models cite nearly the same segment for different questions about one video, which IoP/IoU evidence scores can miss.
- julin2026anchor | ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark | arXiv (comment: accepted at NeurIPS 2026 E&D) | preprint | arXiv abs | AV-QA with rationale traces checked against temporal intervals, boxes and audio cues. Models with similar accuracy differ markedly in evidence support.
- hu2026evaomni | EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning | arXiv | preprint | arXiv abs | Omni-LLMs must return per-modality evidence intervals, scored with the Coverage Grounded (C.G.) and Bottleneck Grounded (B.G.) scores folded into accuracy.
- wei2026videoholmesv2 | Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos? | arXiv (comment: accepted by ECCV 2026) | preprint | arXiv abs | Evidence-based evaluation with a spatio-temporal, evidence-aware metric for audio-visual answers.
- azuma2022scanqa | ScanQA: 3D Question Answering for Spatial Scene Understanding | CVPR 2022 | peer-reviewed | CVF page | 3D-QA where the question-related object box is scored (Acc@0.25/0.5) alongside the answer. These are separate metrics, not a joint one.
- zhao2023toward | Toward Explainable 3D Grounded Visual Question Answering: A New Benchmark and Strong Baseline (FE-3DGQA) | IEEE TCSVT 2023 | peer-reviewed | Crossref DOI | Dense boxes for answer-grounded and contextual objects, aimed at "completely visually grounded and explainable" 3D answers.
- linghu2026scenecot | SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes | ICLR 2026 | peer-reviewed | ICLR proceedings page | Grounded CoT for 3D-LLMs, evaluated for "grounding-QA coherence".

**Already in slice (not re-added)**: luo2025thinking ("When Thinking Drifts", NeurIPS 2025, a video Visual Evidence Reward), wang2026treebench (TreeBench/TreeVGR), wu2026gcot (GCoT), shao2024visual (Visual CoT), zheng2026deepeyes, wu2024vstar. All are image-level except luo2025thinking.

**Near-misses**
- Do 3D Large Language Models Really Use 3D Evidence? (UNICORNS; arXiv 2610.24447) | 3D-LLM responses under insufficient evidence, referential ambiguity and false presuppositions. These are scored on text responses ("no scene claim unsupported by the available evidence"), not on localised evidence. Also relevant to a 3D absent-target or false-premise cell.
- Inter-3D VQA (arXiv 2608.28762; comment: EMNLP 2026) | "3D spatiotemporally grounded VQA" on roadside LiDAR plus multi-view data. The metrics are textual consistency, numerical accuracy and semantic correctness, with no scoring of evidence regions.
- Scene-R1 (arXiv 2506.17545) | RL 3D reasoning with interpretable temporal and 2D-to-3D grounding steps. Here grounding is the task output, not evidence checked for a separate answer.
- ScanReason (zhu2024scanreason, ECCV 2024; key exists in spatial.jsonl) | reasoning 3D grounding whose output is the answer box. It does not verify evidence for a separate answer.
- Meerkat (chowdhury2024meerkat; existing key) | AV-LLM grounding in space and time as a task, not evidence verification for QA (not re-read this session).
- TEMA (arXiv 2609.30029) | evidence-grounded temporal QA over multi-audio dialogs; audio only, with no visual grounding.

**Could not verify (seen only in alphaXiv or search listings; not recorded)**
- Further 2026 video preprints in the same line: EG-VQA (arXiv 2606.24797; abstract read: EG-F1 over temporally localised textual evidence); LOVER (arXiv 2609.15224; uses NExT-GQA IoP as an RL reward per a search snippet); Evidence-Backed Video Question Answering (arXiv 2607.11862); VideoLVR (arXiv 2610.37613); ASSEMBLE (arXiv 2609.32466); TRACE (arXiv 2608.22516); multi-agent self-improving RL (arXiv 2608.28675); Open-o3-Video-v2 (arXiv 2610.17656); VITED (arXiv 2503.12855); Zoom-Zero (arXiv 2512.14273). Only listing-level abstracts were seen and venues were not checked.
- Venue status of seo2026what and wei2026videoholmesv2 (ECCV 2026) and julin2026anchor (NeurIPS 2026 E&D) rests on arXiv comments only; proceedings were not yet online on 2026-11-17. Open-o3-Video is confirmed on the ICML 2026 site, but no PMLR page was located.

**Verdict**: **partially filled.**
- **Video:** filled by peer-reviewed benchmarks that score cited temporal or spatio-temporal evidence jointly with the answer: NExT-GQA (CVPR 2024), ReXTime (NeurIPS 2024 D&B), CG-Bench (ICLR 2025) and V-STaR (CVPR 2026 Findings). An RL method that rewards verifiable spatio-temporal evidence (Open-o3-Video, ICML 2026) also exists. All of them report a large answer-evidence gap, e.g. GPT-4o on CG-Bench drops from 45.2 MCQ accuracy to 4.38 acc.@IoU, and VideoZeroBench reports <=1.8% joint accuracy.
- **3D:** grounded QA scores evidence boxes. ScanQA (CVPR 2022) and FE-3DGQA (TCSVT 2023) score them separately from the answer, and SceneCOT (ICLR 2026) adds a grounding-QA coherence measure.
- **Audio-visual:** evidence verification exists only in 2026 preprints (ANCHOR, EvaOmni, Video-HolmesV2), two of them accepted per their arXiv comments.
- **Still missing (in the papers we read):**
  - Evidence is checked against human annotations, or by feeding ground-truth clue segments as input (NExT-GQA PosQA/NegQA, CG-Bench clue-only MCQ, VideoZeroBench evidence hints). No work tests whether the model's own cited interval, box or 3D object causally drives its answer, e.g. by ablating the cited evidence.
  - No work combines evidence verification with abstention or no-evidence conditions for localised outputs. The closest are a 3D text-level study (UNICORNS, preprint) and CG-Bench's hallucination questions.

## Post-review corrections (coordinator, 2026-11-17)
- Cell 9: Open-o3-Video (meng2026openo3) **is** in PMLR v306 (https://proceedings.mlr.press/v306/meng26e.html, title and authors checked). The JSONL record was updated to venue "ICML 2026 (PMLR 306)" with a pmlr bib_source.
- Spot-checks re-run by the coordinator, all confirmed:
  - kolodziejczyk2026investigating: Crossref DOI and arXiv 2610.06018.
  - tynchenko2026both, fang2026towards, lin2025audio: Crossref DOIs.
  - yao2026hammer, ye2026langref3dgs, wu2026mvggt, park2026affostruction (CVPR 2026 listing) and lu2025geal (CVPR 2025 listing).
  - juanola2025critical: Crossref DOI.
  - halacheva2026p3vlm: arXiv comment "NeurIPS 2026, Spotlight".
  - cheng2026vstar: CVF CVPR 2026 Findings page.
  - linghu2026scenecot (ICLR 2026) and chen2025cgbench (ICLR 2025): proceedings listings.

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

## Cell 6: Adversarial or backdoor attacks on (a) 3D visual grounding / 3D-LLM grounding, (b) audio-visual grounding (sound-source localisation, AVS), (c) temporal grounding (moment retrieval, Video-LLM temporal grounding)

Already in the slice and not re-added:
- Gao et al. 2024 (ICLR-W; adversarial attacks on MLLM REC)
- IAG (CVPR 2026; 2D backdoor on VLM grounding)
- Xu et al. (CVPR 2018)
- Typographic attacks (ECCV 2024)
- AVTrustBench (AV-LLM QA, incl. adversarial)

**Queries** (source | exact query | sub-field | number of relevant results)
1. WebSearch | adversarial attack video moment retrieval temporal sentence grounding | (c) | 0. Results were adversarial *learning* methods for TSG/VMR.
2. WebSearch | adversarial attack 3D visual grounding point cloud language | (a) | 1 lead (UAO², via a ChatPaper summary). Near-misses: 2601.06464 and Inflate3D.
3. WebSearch | adversarial attack audio-visual segmentation sound source localization | (b) | 1 (Tian & Xu, CVPR 2021). Near-miss: 2502.11858.
4. alphaXiv discover_papers | keywords [3D visual grounding, adversarial attack, backdoor, 3D-LLM] | (a) | 0 new. Near-misses: 3D-LVLM attack 2601.06464, PI3D 2602.07104, point-cloud classifier backdoors. IAG and Gao et al. are already in the slice.
5. alphaXiv discover_papers | keywords [audio-visual segmentation, sound source localization, adversarial attack, backdoor] | (b) | 1 (Tian & Xu). Near-misses: 2502.11858, SoundBreak 2601.16231, SAM2-video backdoor 2512.22046.
6. WebSearch | universal adversarial object 3D scene grounding mislocalization attack ScanRefer | (a) | 1 (UAO², CVPR 2025).
7. WebSearch | backdoor attack 3D visual grounding OR "3D vision-language" OR "3D LLM" trigger point cloud | (a) | 0 new. Results were point-cloud classifier backdoors.
8. WebSearch | "audio-visual segmentation" adversarial robustness attack AVSBench | (b) | 0. AVSBench-Robust is already in the slice and covers negative audio, not attacks.
9. WebSearch | Daizong Liu adversarial attack temporal sentence grounding video | (c) | 0.
10. alphaXiv discover_papers | keywords [temporal sentence grounding, video moment retrieval, adversarial attack, backdoor] | (c) | 0. Near-miss: TVA (2511.07049).
11. Google Scholar MCP | adversarial attack video moment retrieval temporal sentence grounding | (c) | the tool returned an empty result (non-functional).
12. arXiv API, eight separate queries | (a), (b), (c) | 0 relevant:
    - abs:adversarial AND abs:"temporal grounding" → 1 irrelevant result
    - all:adversarial AND all:"moment retrieval" → 0
    - all:"moment retrieval" AND all:attack → 0
    - abs:attack AND abs:"temporal sentence grounding" → 0
    - all:adversarial AND all:"3D visual grounding" → 0
    - all:"3D visual grounding" AND all:attack → 0
    - abs:adversarial AND abs:"audio-visual segmentation" → 0
    - abs:adversarial AND abs:"sound source localization" → 5 irrelevant (acoustic-array localisation)

    Caveat: the arXiv API phrase search covers title, abstract and comments only.
13. Semantic Scholar API | adversarial attack temporal sentence grounding / backdoor attack video moment retrieval / adversarial attack audio-visual segmentation | (b), (c) | S2 returned 429 on all retries, so it was not available for search. The S2 title-match endpoint succeeded once and was used only to verify a hit.
14. WebSearch (extended) | adversarial perturbation attack on video temporal grounding model OR video-LLM timestamp localization OR moment retrieval vulnerability 2025 2026 | (c), (a) | 2 leads: SNEAK (cited in a TSG survey) and the IJCNN 2025 3D-VG backdoor.
15. WebSearch (extended) | adversarial attack 3D large language model grounding Chat-3D LL3DA LEO 3D-VisTA robustness bounding box | (a) | 0 for 3D-LLM grounders.
16. WebSearch (extended) | backdoor attacks on 3D visual grounding models multimodal controlled trigger bounding box 2025 | (a) | 1 (IJCNN 2025, IEEE Xplore 11229253).
17. WebSearch | backdoor OR adversarial attack "sound source localization" OR "audio-visual localization" OR "audio-visual segmentation" model fooled localization map | (b) | 1 (Tian & Xu again). Near-misses: AV-attack survey 2506.11521, SED attack 2510.02158.
18. WebSearch | adversarial attack natural language video localization OR "video grounding" OR "spatio-temporal video grounding" robustness attack query video | (c) | 1 (SNEAK). Near-misses: CAVALRY-V, PoisonVID, OV-VIS attack.
19. Lookups used for verification only: WebSearch for the SNEAK title, WebSearch for the "Manipulating the Bounding Box" title, Crossref/arXiv via verify.py, and the CVF pages.

**Verified hits**
- (a) liu2025seeing | Seeing is Not Believing: Adversarial Natural Object Optimization for Hard-Label 3D Scene Attacks | CVPR 2025 | peer-reviewed | CVF page + CVF PDF
  - The attack is hard-label, universal and inserts a natural-looking adversarial object.
  - Its victims are 7 3D-VG models (ScanRefer, ReferIt3D, SAT, 3DTrans., 3D-SPS, ViL3DRel, EDA), evaluated on ScanRefer, Nr3D and Sr3D.
  - Example: EDA ScanRefer Unique Acc@0.25 drops from 85.76 to 20.61 (Table 1).
- (a) zhang2025manipulating | Manipulating the Bounding Box: Multimodal Controlled Backdoor Attacks on 3D Visual Grounding Models | IJCNN 2025 | peer-reviewed | Crossref DOI 10.1109/IJCNN64981.2025.11229253 + Semantic Scholar abstract
  - Point-cloud and text triggers shift the position and size of the predicted 3D box.
  - The abstract says this has negligible effect on clean accuracy.
- (b) tian2021can | Can Audio-Visual Integration Strengthen Robustness Under Multimodal Attacks? | CVPR 2021 | peer-reviewed | CVF page + arXiv 2104.02000
  - It studies adversarial attacks on AV event recognition (classification).
  - It also shows that a weakly-supervised sound-source localisation model "can be successfully fooled". This is the only attack result on an AV localisation output that we found.
- (c) gou2021sneak | SNEAK: Synonymous Sentences-Aware Adversarial Attack on Natural Language Video Localization | arXiv 2112.04154 | preprint (no peer-reviewed version found) | arXiv abs + PDF
  - It runs video-side, query-side and joint adversarial attacks on VSLNet (TACoS, Charades-STA; mIoU).
  - The perturbation is optimised to work across synonymous queries.

**Near-misses**
- (a) On the Adversarial Robustness of 3D Large Vision-Language Models (arXiv 2601.06464). Attacks PointLLM and GPT4Point on captioning and classification-style outputs, not grounding.
- (a) Inflate3D (ACL 2026 Findings, aclanthology 2026.findings-acl.259; seen in search results only). A resource-exhaustion attack on 3D-VLMs, not grounding.
- (a) Extended to Reality: Prompt Injection in 3D Environments (PI3D; arXiv 2602.07104; COLM 2026 per arXiv). Task-hijacking prompt injection against MLLMs in 3D scenes; the abstract gives no evidence that grounding outputs are evaluated.
- (a) Point-cloud backdoor and adversarial attacks on classifiers, with no language query: IRBA 2208.08052, SRBA 2412.07511, SPBA 2503.09336, STONE 2511.11210, hard-label 3D attack 2412.00404.
- (a) LiDAR/fusion 3D-detection backdoors with no language query: BadFusion (IJCAI 2024), MOBA 2511.09999, Mirage 2606.20752.
- (b) Rethinking Audio-Visual Adversarial Vulnerability from Temporal and Modality Perspectives (arXiv 2502.11858; ICLR 2025 per arXiv). AV classification on Kinetics-Sounds.
- (b) SoundBreak (arXiv 2601.16231). Audio-only attacks on trimodal reasoning and generation models.
- (b) Mirage Fools the Ear, Mute Hides the Truth (arXiv 2510.02158). Attacks audio-only sound event detection (temporal), with no visual grounding.
- (b) Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models (arXiv 2512.22046). SAM2 with visual prompts, no audio or language.
- (b) AVRobustBench (arXiv 2506.00358). Corruptions, not attacks, on AV recognition. AVSBench-Robust (already in the slice) covers negative or irrelevant audio, not adversarial input.
- (b) Investigating Vulnerabilities and Defenses Against Audio-Visual Attacks (survey, arXiv 2506.11521). Its examples are classification and speech.
- (c) From Pretrain to Pain: Adversarial Vulnerability of Video Foundation Models Without Task Knowledge (TVA; arXiv 2511.07049; AAAI 2026 per arXiv). Of its 24 tasks, the temporal one is action detection with category-defined intervals and no language query (THUMOS14, Charades). MVBench "Action Localization" is multiple-choice. No language-queried temporal grounding.
- (c) CAVALRY-V (arXiv 2507.00817). Adversarial attacks on video MLLMs evaluated on QA benchmarks.
- (c) PoisonVID (arXiv 2509.20851, seen in search snippet). Poisons prompt-guided frame sampling in VideoLLMs; output is not interval grounding (not verified further).
- (c) Open-vocabulary video instance segmentation attack (IJCAI 2026 proceedings paper 0180, seen in a search snippet). Category-name queries, not temporal grounding; title not verified.
- (c) Adversarial *training* for TSG/VMR is not an attack: BSSARD (AAAI 2024, arXiv 2401.07567), ATSG, and "Moment is Important: Language-Based Video Moment Retrieval via Adversarial Learning".
- (c) Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box VLMs for Autonomous Driving (arXiv 2610.08331). VLM QA and decisions, not grounding.

**Could not verify**
- None among the hits.
- The near-misses Inflate3D, PoisonVID and the IJCAI 2026 OV-VIS attack were seen only in search snippets. Their titles and venues were not verified, so they are not used as citations.

**Verdict**: partially filled overall. The coverage is very uneven across sub-fields, and all three lack attacks on LLM-based grounders.

- **(a) 3D visual grounding: partially filled.** Two peer-reviewed papers exist, both from the same group (Daizong Liu et al.):
  - a hard-label universal adversarial-object attack on seven classic 3D-VG models (CVPR 2025);
  - a multimodal point-cloud plus text backdoor that manipulates 3D boxes (IJCNN 2025).

  We found no adversarial or backdoor attack on 3D-LLM grounders that emit boxes or object IDs (e.g. Chat-3D, LL3DA, LEO). The one 3D-LVLM attack study we found (2601.06464) targets captioning and classification.
- **(b) Audio-visual grounding: gap essentially confirmed.** The only result is a 2021 analysis (Tian & Xu, CVPR 2021) showing that a weakly-supervised sound-source localisation model can be fooled while studying AV event recognition. As of 2026-11-17 we found no adversarial or backdoor attack on audio-visual segmentation (AVSBench), Ref-AVS or AV-LLM grounding. AV attack papers address classification, and AVSBench-Robust studies negative audio, not attacks.
- **(c) Temporal grounding: gap confirmed for peer-reviewed work.** A single 2021 arXiv preprint (SNEAK) attacks a TSG model (VSLNet). We found nothing on attacks against Video-LLM temporal grounding, highlight detection or spatio-temporal grounding. Video-foundation-model attacks such as TVA (AAAI 2026) cover action detection and QA, not language-queried intervals.

Sources searched: WebSearch, alphaXiv and the arXiv API. Semantic Scholar was rate-limited and Google Scholar returned nothing.

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
