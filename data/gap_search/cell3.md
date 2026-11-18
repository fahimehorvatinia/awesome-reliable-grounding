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
