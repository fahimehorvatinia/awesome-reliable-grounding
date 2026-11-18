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
