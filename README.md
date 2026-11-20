<div align="center">

# 🎯 Awesome Reliable Multimodal Grounding

**A curated, verified list of multimodal grounding research — organised around reliability.**

![papers](https://img.shields.io/badge/papers-373-blue) ![surveys](https://img.shields.io/badge/surveys-41-blueviolet) ![benchmark values](https://img.shields.io/badge/benchmark%20values-1%2C109-orange) ![license](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)

</div>

> **Multimodal grounding** = localising, inside one signal, the referent described by a query in another: a box for a referring expression, a mask for a sound, a time interval for a sentence, a 3D region for an instruction. This list focuses on **reliability**: what happens with missing, noisy or conflicting modalities, ambiguous or absent targets and distribution shift, and how a model's output can be verified.

Companion repository of the survey *Reliable Multimodal Grounding: A Survey* (F. Orvati Nia, in preparation).

## 📌 At a glance

| | |
|---|---|
| 📚 Primary works | **373** (314 peer-reviewed · 50 preprints ⚠️ · 9 workshop (W)) |
| 📖 Surveys | **41** |
| 💻 Works with verified code links | **202** |
| 📊 Benchmark values (with source table) | **1,109** |
| 🔍 Method papers with no coded verification or evidence-support mechanism (facet H) | **213 of 284** |
| ✅ Every entry | checked against the publisher, the official proceedings page or arXiv |

## 🗂️ Contents

| Papers by modality | Reliability | Resources |
|---|---|---|
| [🖼️ Image](#image) | [⚖️ Reliability conditions](#reliability-conditions) | [📖 Surveys](#surveys) |
| [🎬 Video](#video) | [✔️ Verification mechanisms](#verification-mechanisms) | [🧭 Taxonomy](#taxonomy) |
| [🔊 Audio and audio-visual](#audio-and-audio-visual) | [🧪 Benchmarks](#benchmarks) | [📦 Data & scripts](#data-and-scripts) |
| [🧊 3D and spatial](#3d-and-spatial) |  | [📝 Citation](#citation) |
| [🛰️ Other sensors and domains](#other-sensors-and-domains) |  |  |

**Legend:** ⚠️ preprint · (W) workshop paper · *Type* = architecture paradigm in the survey's taxonomy.

<a id="taxonomy"></a>

## 🧭 Taxonomy

Every paper is coded on eight facets ([full codebook](data/codebook.md)).

| Facet | What it records | Values |
|---|---|---|
| **A** Query | how the target is specified | expression · instruction · phrase · speech · sound · exemplar · visual prompt · gesture |
| **B** Target | where it is found | image · video · audio-visual video · audio · RGB-D · point cloud · 3DGS · LiDAR/radar/thermal · remote sensing · medical |
| **C** Referent | what is found | object · part · region · set of 0..K · event · sound source · relation · affordance |
| **D** Output | how it is returned | point/heatmap · box · rotated box · mask · interval · tube/track · 3D box · 3D mask · grounded text |
| **E** Architecture | how the model is built | E1 proposal & rank → E9 training-free (see *Type* column) |
| **F** Supervision | how it is trained | full · weak · self-supervised · semi-supervised · zero-shot · synthetic/LLM · RL |
| **G** Reliability condition 🆕 | what stress it is tested under | missing · degraded · conflicting · ambiguity · absent target · multi-target · shift · novel · adversarial · long-horizon |
| **H** Verification 🆕 | how its output is checked | abstention head · confidence · cycle consistency · temporal consistency · self-verification · external verifier · traceable evidence · clarification |

<a id="image"></a>

## 🖼️ Image

**146 papers** · Analysis / audit 31 · Dense fusion 19 · MLLM · coords as text 16 · Dataset / benchmark 16 · Training-free 13

<details open>
<summary><b>Datasets & benchmarks</b> (16)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Exposing and Evaluating Hallucinations for GUI Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html) | CVPR 2026 | — |
| [Grounded Chain-of-Thought for Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Grounded_Chain-of-Thought_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html) | CVPR 2026 | — |
| [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978) | arXiv ⚠️ | — |
| [Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination](https://arxiv.org/abs/2506.21546) | arXiv ⚠️ | [code](https://github.com/plan-lab/HalluSegBench) |
| [Revisiting Referring Expression Comprehension Evaluation in the Era of Large Multimodal Models](https://doi.org/10.1109/CVPRW67362.2025.00056) | CVPR 2025 Workshops (W) | [code](https://github.com/JierunChen/Ref-L4) |
| [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.01363) | CVPR 2024 | — |
| [Unveiling Typographic Deceptions: Insights of the Typographic Vulnerability in Large Vision-Language Models](https://doi.org/10.1007/978-3-031-73202-7_11) | ECCV 2024 | — |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 | [code](https://github.com/shikras/d-cube) |
| [Evaluating Object Hallucination in Large Vision-Language Models](https://doi.org/10.18653/v1/2023.emnlp-main.20) | EMNLP 2023 | [code](https://github.com/RUCAIBox/POPE) |
| [GREC: Generalized Referring Expression Comprehension](https://arxiv.org/abs/2308.16182) | arXiv ⚠️ | [code](https://github.com/henghuiding/gRefCOCO) |
| [GRIT: General Robust Image Task Benchmark](https://arxiv.org/abs/2204.13653) | arXiv ⚠️ | — |
| [Cops-Ref: A New Dataset and Task on Compositional Referring Expression Comprehension](https://doi.org/10.1109/CVPR42600.2020.01010) | CVPR 2020 | — |
| [CLEVR-Ref+: Diagnosing Visual Reasoning With Referring Expressions](https://doi.org/10.1109/CVPR.2019.00431) | CVPR 2019 | — |
| [Talk2Car: Taking Control of Your Self-Driving Car](https://doi.org/10.18653/v1/d19-1215) | EMNLP-IJCNLP 2019 | — |
| [Flickr30k Entities: Collecting Region-to-Phrase Correspondences for Richer Image-to-Sentence Models](https://doi.org/10.1007/s11263-016-0965-7) | IJCV 2017 | — |
| [ReferItGame: Referring to Objects in Photographs of Natural Scenes](https://doi.org/10.3115/v1/D14-1086) | EMNLP 2014 | — |

</details>

<details>
<summary><b>Methods</b> (99)</summary>

| Paper | Venue | Type | Code |
|---|---|---|---|
| [Angular Supervision for Visual Object Grounding in Autoregressive Vision-Language Models](https://arxiv.org/abs/2610.32220) | arXiv ⚠️ | Training-free | — |
| [CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion](https://arxiv.org/abs/2602.08999) | arXiv ⚠️ | MLLM · coords as text | — |
| [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cdb347d7516d52a9280ea9d6708911f6-Abstract-Conference.html) | ICLR 2026 | Agentic / RL reasoning | [code](https://github.com/Visual-Agent/DeepEyes) |
| [IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Li_IAG_Input-aware_Backdoor_Attack_on_VLM-based_Visual_Grounding_CVPR_2026_paper.html) | CVPR 2026 | MLLM · coords as text | — |
| [MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_MVGGT_Multimodal_Visual_Geometry_Grounded_Transformer_for_Multiview_3D_Referring_CVPR_2026_paper.html) | CVPR 2026 | Dense fusion | [code](https://mvggt.github.io/) |
| [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440) | arXiv ⚠️ | Open-set pre-training | — |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 | Agentic / RL reasoning | [code](https://github.com/IDEA-Research/Rex-Thinker) |
| [SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419) | ICLR 2026 Workshop (W) | MLLM · coords as text | — |
| [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_SegCompass_Exploring_Interpretable_Alignment_with_Sparse_Autoencoders_for_Enhanced_Reasoning_CVPR_2026_paper.html) | CVPR 2026 | Agentic / RL reasoning | [code](https://github.com/ZhenyuLU-Heliodore/SegCompass) |
| [Surrogate Uncertainty for Black-box Visual Grounding](https://arxiv.org/abs/2610.39798) | arXiv ⚠️ | Training-free | — |
| [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](https://arxiv.org/abs/2608.04698) | arXiv ⚠️ | Agentic / RL reasoning | — |
| [Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Method](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f09ab24aa37ae2664b3d923cdb0319b5-Abstract-Conference.html) | ICLR 2026 | Agentic / RL reasoning | [code](https://github.com/Haochen-Wang409/TreeVGR) |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 | Training-free | — |
| [Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines](https://arxiv.org/abs/2604.15376) | arXiv ⚠️ | Training-free | [code](https://github.com/omxyz/zoom-consistency-routing) |
| [Advancing Visual Large Language Model for Multi-granular Versatile Perception](https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Advancing_Visual_Large_Language_Model_for_Multi-granular_Versatile_Perception_ICCV_2025_paper.html) | ICCV 2025 | Query-based (DETR) | [code](https://github.com/xiangwentao666/MVP-LM) |
| [DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy](https://doi.org/10.1109/ICCV51701.2025.01854) | ICCV 2025 | Query-based (DETR) | [code](https://github.com/Dmmm1997/DeRIS) |
| [Detect Anything via Next Point Prediction](https://arxiv.org/abs/2510.12798) | arXiv ⚠️ | Agentic / RL reasoning | [code](https://github.com/IDEA-Research/Rex-Omni) |
| [Enhancing Trustworthy GUI Grounding via Self-Critiqued Reinforcement Learning](https://arxiv.org/abs/2510.27266) | arXiv ⚠️ | Agentic / RL reasoning | — |
| [Hierarchical Alignment-enhanced Adaptive Grounding Network for Generalized Referring Expression Comprehension](https://doi.org/10.1609/aaai.v39i8.32867) | AAAI 2025 | Query-based (DETR) | — |
| [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/aaa0ac4253da75faf9b0dc0dda062612-Abstract-Conference.html) | ICLR 2025 | Training-free | [code](https://github.com/saccharomycetes/mllms_know) |
| [POPEN: Preference-Based Optimization and Ensemble for LVLM-Based Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_POPEN_Preference-Based_Optimization_and_Ensemble_for_LVLM-Based_Reasoning_Segmentation_CVPR_2025_paper.html) | CVPR 2025 | MLLM · mask token | — |
| [Reasoning to Attend: Try to Understand How <SEG> Token Works](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_Reasoning_to_Attend_Try_to_Understand_How_SEG_Token_Works_CVPR_2025_paper.html) | CVPR 2025 | MLLM · mask token | [code](https://github.com/rui-qian/READ) |
| [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b4008025c2182bfe16fcc8566ee14d64-Abstract-Conference.html) | ICLR 2025 | Training-free | [code](https://github.com/shengliu66/VTI) |
| [Robust Multimodal Large Language Models Against Modality Conflict](https://proceedings.mlr.press/v267/zhang25dq.html) | ICML 2025 | Agentic / RL reasoning | [code](https://github.com/zmzhang2000/MMMC) |
| [Seg-Zero: Reasoning-Chain Guided Segmentation via Cognitive Reinforcement](https://arxiv.org/abs/2503.06520) | arXiv ⚠️ | Agentic / RL reasoning | [code](https://github.com/JIA-Lab-research/Seg-Zero) |
| [SegLLM: Multi-round Reasoning Segmentation with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8e125fb53198f2143716d969584d0a28-Abstract-Conference.html) | ICLR 2025 | MLLM · mask token | [code](https://berkeley-hipie.github.io/segllm.github.io/ (project page)) |
| [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/04d8c25cbf0d5e1b70d64e672ac92637-Abstract-Conference.html) | ICLR 2025 | MLLM · coords as text | [code](https://github.com/mc-lan/Text4Seg) |
| [Visual-RFT: Visual Reinforcement Fine-Tuning](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Visual-RFT_Visual_Reinforcement_Fine-Tuning_ICCV_2025_paper.html) | ICCV 2025 | Agentic / RL reasoning | [code](https://github.com/Liuziyu77/Visual-RFT) |
| [VLM-R1: A Stable and Generalizable R1-style Large Vision-Language Model](https://arxiv.org/abs/2504.07615) | arXiv ⚠️ | Agentic / RL reasoning | [code](https://github.com/om-ai-lab/VLM-R1) |
| [Why Is Spatial Reasoning Hard for VLMs? An Attention Mechanism Perspective on Focus Areas](https://proceedings.mlr.press/v267/chen25cr.html) | ICML 2025 | Training-free | [code](https://github.com/shiqichen17/AdaptVis) |
| [Your Large Vision-Language Model Only Needs A Few Attention Heads For Visual Grounding](https://doi.org/10.1109/CVPR52734.2025.00872) | CVPR 2025 | Training-free | [code](https://github.com/seilk/LocalizationHeads) |
| [Zero-Shot Referring Expression Comprehension via Vison-Language True/False Verification](https://arxiv.org/abs/2509.09958) | arXiv ⚠️ | Training-free | — |
| [Adversarial Robustness for Visual Grounding of Multimodal Large Language Models](https://arxiv.org/abs/2405.09981) | ICLR 2024 Workshop on Reliable and Responsible Foundation Models (W) | MLLM · coords as text | — |
| [CLIP-VG: Self-paced Curriculum Adapting of CLIP for Visual Grounding](https://doi.org/10.1109/TMM.2023.3321501) | IEEE TMM 2024 | Dense fusion | [code](https://github.com/linhuixiao/CLIP-VG) |
| [CogVLM: Visual Expert for Pretrained Language Models](https://doi.org/10.52202/079017-3860) | NeurIPS 2024 | MLLM · coords as text | [code](https://github.com/THUDM/CogVLM) |
| [Curriculum Point Prompting for Weakly-Supervised Referring Image Segmentation](https://doi.org/10.1109/CVPR52733.2024.01301) | CVPR 2024 | Promptable seg. + adapter | — |
| [Emergent Visual Grounding in Large Multimodal Models Without Grounding Supervision](https://arxiv.org/abs/2410.08209) | arXiv ⚠️ | Training-free | — |
| [Ferret-v2: An Improved Baseline for Referring and Grounding with Large Language Models](https://openreview.net/forum?id=EEPBOB2Xww) | COLM 2024 | MLLM · coords as text | — |
| [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | ICLR 2024 | MLLM · coords as text | [code](https://github.com/apple/ml-ferret) |
| [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](https://doi.org/10.1109/CVPR52733.2024.00461) | CVPR 2024 | MLLM · coords as text | — |
| [Generating Enhanced Negatives for Training Language-Based Object Detectors](https://doi.org/10.1109/CVPR52733.2024.01290) | CVPR 2024 | Open-set pre-training | [code](https://github.com/xiaofeng94/Gen-Enhanced-Negs) |
| [GLaMM: Pixel Grounding Large Multimodal Model](https://doi.org/10.1109/CVPR52733.2024.01236) | CVPR 2024 | MLLM · mask token | [code](https://github.com/mbzuai-oryx/groundingLMM) |
| [Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](https://doi.org/10.1007/978-3-031-72658-3_24) | ECCV 2024 | Proposal & rank | [code](https://groma-mllm.github.io/ (project page)) |
| [GROUNDHOG: Grounding Large Language Models to Holistic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_GROUNDHOG_Grounding_Large_Language_Models_to_Holistic_Segmentation_CVPR_2024_paper.html) | CVPR 2024 | MLLM · mask token | [code](https://groundhog-mllm.github.io/ (project page)) |
| [Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection](https://doi.org/10.1007/978-3-031-72970-6_3) | ECCV 2024 | Open-set pre-training | [code](https://github.com/IDEA-Research/GroundingDINO) |
| [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e112a4671e8779aa9f640a0e3f81bd26-Abstract-Conference.html) | ICLR 2024 | MLLM · coords as text | [code](https://aka.ms/kosmos-2) |
| [GSVA: Generalized Segmentation via Multimodal Large Language Models](https://doi.org/10.1109/CVPR52733.2024.00370) | CVPR 2024 | MLLM · mask token | [code](https://github.com/LeapLabTHU/GSVA) |
| [LISA: Reasoning Segmentation via Large Language Model](https://doi.org/10.1109/CVPR52733.2024.00915) | CVPR 2024 | MLLM · mask token | [code](https://github.com/dvlab-research/LISA) |
| [Mask Grounding for Referring Image Segmentation](https://doi.org/10.1109/CVPR52733.2024.02509) | CVPR 2024 | Dense fusion | — |
| [Mono3DVG: 3D Visual Grounding in Monocular Images](https://doi.org/10.1609/aaai.v38i7.28525) | AAAI 2024 | Query-based (DETR) | [code](https://github.com/ZhanYang-nwpu/Mono3DVG) |
| [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://doi.org/10.52202/079017-2291) | NeurIPS 2024 | MLLM · mask token | [code](https://lxtgh.github.io/project/omg_llava/ (project page)) |
| [OneRef: Unified One-tower Expression Grounding and Segmentation with Mask Referring Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/hash/fcd812a51b8f8d05cfea22e3c9c4b369-Abstract-Conference.html) | NeurIPS 2024 | Dense fusion | [code](https://github.com/linhuixiao/OneRef) |
| [PixelLM: Pixel Reasoning with Large Multimodal Model](https://doi.org/10.1109/CVPR52733.2024.02491) | CVPR 2024 | MLLM · mask token | [code](https://pixellm.github.io/ (project page)) |
| [PSALM: Pixelwise SegmentAtion with Large Multi-modal Model](https://doi.org/10.1007/978-3-031-72754-2_5) | ECCV 2024 | Query-based (DETR) | — |
| [SAM4MLLM: Enhance Multi-Modal Large Language Model for Referring Expression Segmentation](https://doi.org/10.1007/978-3-031-73004-7_19) | ECCV 2024 | Promptable seg. + adapter | [code](https://github.com/AI-Application-and-Integration-Lab/SAM4MLLM) |
| [See Say and Segment: Teaching LMMs to Overcome False Premises](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_See_Say_and_Segment_Teaching_LMMs_to_Overcome_False_Premises_CVPR_2024_paper.html) | CVPR 2024 | MLLM · mask token | [code](https://github.com/see-say-segment/sesame) |
| [SimVG: A Simple Framework for Visual Grounding with Decoupled Multi-modal Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dc6319dde4fb182b22fb902da9418566-Abstract-Conference.html) | NeurIPS 2024 | Dense fusion | [code](https://github.com/Dmmm1997/SimVG) |
| [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://doi.org/10.1109/CVPR52733.2024.01370) | CVPR 2024 | MLLM · coords as text | — |
| [T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy](https://doi.org/10.1007/978-3-031-73414-4_3) | ECCV 2024 | Open-set pre-training | [code](https://github.com/IDEA-Research/T-Rex) |
| [Talk2BEV: Language-enhanced Bird’s-eye View Maps for Autonomous Driving](https://doi.org/10.1109/icra57147.2024.10611485) | ICRA 2024 | Training-free | — |
| [Unveiling Parts Beyond Objects: Towards Finer-Granularity Referring Expression Segmentation](https://doi.org/10.1109/CVPR52733.2024.01235) | CVPR 2024 | Query-based (DETR) | [code](https://github.com/Rubics-Xuan/MRES) |
| [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_V_Guided_Visual_Search_as_a_Core_Mechanism_in_Multimodal_CVPR_2024_paper.html) | CVPR 2024 | Agentic / RL reasoning | [code](https://github.com/penghao-wu/vstar) |
| [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://doi.org/10.52202/079017-2235) | NeurIPS 2024 | MLLM · mask token | — |
| [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0ff38d72a2e0aa6dbe42de83a17b2223-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | MLLM · coords as text | [code](https://github.com/deepcs233/Visual-CoT) |
| [Beyond One-to-One: Rethinking the Referring Image Segmentation](https://doi.org/10.1109/ICCV51070.2023.00376) | ICCV 2023 | Dense fusion | [code](https://github.com/toggle1995/RIS-DMMI) |
| [Contrastive Grouping with Transformer for Referring Image Segmentation](https://doi.org/10.1109/CVPR52729.2023.02257) | CVPR 2023 | Query-based (DETR) | [code](https://github.com/Toneyaya/CGFormer) |
| [Generalized Decoding for Pixel, Image, and Language](https://doi.org/10.1109/CVPR52729.2023.01451) | CVPR 2023 | Query-based (DETR) | — |
| [GRES: Generalized Referring Expression Segmentation](https://doi.org/10.1109/CVPR52729.2023.02259) | CVPR 2023 | Query-based (DETR) | [code](https://henghuiding.github.io/GRES) |
| [Language Adaptive Weight Generation for Multi-task Visual Grounding](https://doi.org/10.1109/CVPR52729.2023.01045) | CVPR 2023 | Dense fusion | — |
| [LISA++: An Improved Baseline for Reasoning Segmentation with Large Language Model](https://arxiv.org/abs/2312.17240) | arXiv ⚠️ | MLLM · mask token | — |
| [MiniGPT-v2: large language model as a unified interface for vision-language multi-task learning](https://arxiv.org/abs/2310.09478) | arXiv ⚠️ | MLLM · coords as text | [code](https://minigpt-v2.github.io (project page)) |
| [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966) | arXiv ⚠️ | MLLM · coords as text | [code](https://github.com/QwenLM/Qwen-VL) |
| [Referring Image Segmentation Using Text Supervision](https://doi.org/10.1109/ICCV51070.2023.02022) | ICCV 2023 | Dense fusion | [code](https://github.com/fawnliu/TRIS) |
| [Segment Anything](https://doi.org/10.1109/ICCV51070.2023.00371) | ICCV 2023 | Promptable seg. + adapter | [code](https://segment-anything.com (project page)) |
| [Segment Everything Everywhere All at Once](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html) | NeurIPS 2023 | Promptable seg. + adapter | — |
| [Shikra: Unleashing Multimodal LLM's Referential Dialogue Magic](https://arxiv.org/abs/2306.15195) | arXiv ⚠️ | MLLM · coords as text | [code](https://github.com/shikras/shikra) |
| [TransVG++: End-to-End Visual Grounding With Language Conditioned Vision Transformer](https://doi.org/10.1109/TPAMI.2023.3296823) | IEEE TPAMI 2023 | Dense fusion | [code](https://github.com/djiajunustc/TransVG) |
| [Zero-shot Referring Image Segmentation with Global-Local Context Features](https://doi.org/10.1109/CVPR52729.2023.01864) | CVPR 2023 | Training-free | [code](https://github.com/Seonghoon-Yu/Zero-shot-RIS) |
| [CRIS: CLIP-Driven Referring Image Segmentation](https://doi.org/10.1109/CVPR52688.2022.01139) | CVPR 2022 | Dense fusion | — |
| [Grounded Language-Image Pre-training](https://doi.org/10.1109/CVPR52688.2022.01069) | CVPR 2022 | Open-set pre-training | [code](https://github.com/microsoft/GLIP) |
| [LAVT: Language-Aware Vision Transformer for Referring Image Segmentation](https://doi.org/10.1109/CVPR52688.2022.01762) | CVPR 2022 | Dense fusion | [code](https://github.com/yz93/LAVT-RIS) |
| [OFA: Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework](https://proceedings.mlr.press/v162/wang22al.html) | ICML 2022 | MLLM · coords as text | [code](https://github.com/OFA-Sys/OFA) |
| [Pseudo-Q: Generating Pseudo Language Queries for Visual Grounding](https://doi.org/10.1109/CVPR52688.2022.01507) | CVPR 2022 | Dense fusion | [code](https://github.com/LeapLabTHU/Pseudo-Q) |
| [ReCLIP: A Strong Zero-Shot Baseline for Referring Expression Comprehension](https://doi.org/10.18653/v1/2022.acl-long.357) | ACL 2022 | Training-free | [code](https://www.github.com/allenai/reclip) |
| [ReSTR: Convolution-free Referring Image Segmentation Using Transformers](https://doi.org/10.1109/CVPR52688.2022.01761) | CVPR 2022 | Dense fusion | — |
| [SeqTR: A Simple yet Universal Network for Visual Grounding](https://doi.org/10.1007/978-3-031-19833-5_35) | ECCV 2022 | Dense fusion | [code](https://github.com/sean-zhuh/SeqTR) |
| [Giving Commands to a Self-Driving Car: How to Deal with Uncertain Situations?](https://doi.org/10.1016/j.engappai.2021.104257) | Engineering Applications of Artificial Intelligence 2021 | Proposal & rank | — |
| [Locate then Segment: A Strong Pipeline for Referring Image Segmentation](https://doi.org/10.1109/CVPR46437.2021.00973) | CVPR 2021 | Dense fusion | — |
| [MDETR - Modulated Detection for End-to-End Multi-Modal Understanding](https://doi.org/10.1109/ICCV48922.2021.00180) | ICCV 2021 | Open-set pre-training | [code](https://github.com/ashkamath/mdetr) |
| [Referring Transformer: A One-step Approach to Multi-task Visual Grounding](https://proceedings.neurips.cc/paper_files/paper/2021/hash/a376802c0811f1b9088828288eb0d3f0-Abstract.html) | NeurIPS 2021 | Query-based (DETR) | — |
| [TransVG: End-to-End Visual Grounding with Transformers](https://doi.org/10.1109/ICCV48922.2021.00179) | ICCV 2021 | Dense fusion | [code](https://github.com/djiajunustc/TransVG) |
| [Vision-Language Transformer and Query Generation for Referring Segmentation](https://doi.org/10.1109/ICCV48922.2021.01601) | ICCV 2021 | Query-based (DETR) | [code](https://github.com/henghuiding/Vision-Language-Transformer) |
| [Graph-Structured Referring Expression Reasoning in the Wild](https://doi.org/10.1109/CVPR42600.2020.00997) | CVPR 2020 | Proposal & rank | [code](https://github.com/sibeiyang/sgmn) |
| [Multi-task Collaborative Network for Joint Referring Expression Comprehension and Segmentation](https://doi.org/10.1109/CVPR42600.2020.01005) | CVPR 2020 | Dense fusion | [code](https://github.com/luogen1996/MCN) |
| [Zero-Shot Grounding of Objects from Natural Language Queries](https://doi.org/10.1109/ICCV.2019.00479) | ICCV 2019 | Dense fusion | [code](https://github.com/TheShadow29/zsgnet-pytorch) |
| [MAttNet: Modular Attention Network for Referring Expression Comprehension](https://doi.org/10.1109/CVPR.2018.00142) | CVPR 2018 | Proposal & rank | [code](https://github.com/lichengunc/MAttNet) |
| [Generation and Comprehension of Unambiguous Object Descriptions](https://doi.org/10.1109/CVPR.2016.9) | CVPR 2016 | Proposal & rank | [code](https://github.com/mjhucla/Google_Refexp_toolbox) |
| [Modeling Context in Referring Expressions](https://doi.org/10.1007/978-3-319-46475-6_5) | ECCV 2016 | Proposal & rank | [code](https://github.com/lichengunc/refer) |
| [Segmentation from Natural Language Expressions](https://doi.org/10.1007/978-3-319-46448-0_7) | ECCV 2016 | Dense fusion | — |

</details>

<details>
<summary><b>Analyses & audits</b> (31)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](https://arxiv.org/abs/2607.10993) | arXiv ⚠️ | — |
| [From Drop-off to Recovery: A Mechanistic Analysis of Segmentation in MLLMs](https://arxiv.org/abs/2603.17228) | arXiv ⚠️ | — |
| [Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning?](https://arxiv.org/abs/2608.23074) | arXiv ⚠️ | — |
| [Mechanisms of Object Localization in Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Schaumloffel_Mechanisms_of_Object_Localization_in_Vision-Language_Models_CVPR_2026_paper.html) | CVPR 2026 | — |
| [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html) | ICML 2026 | — |
| [Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information](https://arxiv.org/abs/2608.27417) | arXiv ⚠️ | — |
| [Cross-modal Information Flow in Multimodal Large Language Models](https://doi.org/10.1109/CVPR52734.2025.01842) | CVPR 2025 | [code](https://github.com/FightingFighting/cross-modal-information-flow-in-MLLM) |
| [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9f14fb9acd243c13c95d4a490d1684ce-Abstract-Conference.html) | ICLR 2025 | [code](https://github.com/nickjiang2378/vlm-hallucinations) |
| [Same Task, Different Circuits: Disentangling Modality-Specific Mechanisms in VLMs](https://doi.org/10.52202/085713-2228) | NeurIPS 2025 | — |
| [Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models](https://doi.org/10.52202/085713-3202) | NeurIPS 2025 | [code](https://github.com/ExplainableML/sae-for-vlm) |
| [Towards Interpreting Visual Information Processing in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/900fb3439e4968df79a6f2bfedec49cd-Abstract-Conference.html) | ICLR 2025 | [code](https://github.com/clemneo/llava-interp) |
| [What Do VLMs NOTICE? A Mechanistic Interpretability Pipeline for Gaussian-Noise-free Text-Image Corruption and Evaluation](https://doi.org/10.18653/v1/2025.naacl-long.571) | NAACL 2025 | — |
| [What's in the Image? A Deep-Dive into the Vision of Vision Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Kaduri_Whats_in_the_Image_A_Deep-Dive_into_the_Vision_of_CVPR_2025_paper.html) | CVPR 2025 | — |
| [Words or Vision: Do Vision-Language Models Have Blind Faith in Text?](https://doi.org/10.1109/CVPR52734.2025.00366) | CVPR 2025 | — |
| [Interpreting CLIP's Image Representation via Text-Based Decomposition](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5085a2b8c298edeadc46b9ffe6df5f64-Abstract-Conference.html) | ICLR 2024 | [code](https://github.com/yossigandelsman/clip_text_span) |
| [Understanding Information Storage and Transfer in Multi-Modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0dfe31d6e703e138d46a7d2fced38b7c-Abstract-Conference.html) | NeurIPS 2024 | — |
| [MM-SHAP: A Performance-agnostic Metric for Measuring Multimodal Contributions in Vision and Language Models & Tasks](https://doi.org/10.18653/v1/2023.acl-long.223) | ACL 2023 | [code](https://github.com/Heidelberg-NLP/MM-SHAP) |
| [Multimodal Prompting with Missing Modalities for Visual Recognition](https://doi.org/10.1109/CVPR52729.2023.01435) | CVPR 2023 | [code](https://github.com/YiLunLee/missing_aware_prompts) |
| [Towards Vision-Language Mechanistic Interpretability: A Causal Tracing Tool for BLIP](https://openaccess.thecvf.com/content/ICCV2023W/CLVL/html/Palit_Towards_Vision-Language_Mechanistic_Interpretability_A_Causal_Tracing_Tool_for_BLIP_ICCVW_2023_paper.html) | ICCV 2023 Workshops (W) | [code](https://github.com/vedantpalit/Towards-Vision-Language-Mechanistic-Interpretability) |
| [Are Multimodal Transformers Robust to Missing Modality?](https://doi.org/10.1109/CVPR52688.2022.01764) | CVPR 2022 | — |
| [Reliable Visual Question Answering: Abstain Rather Than Answer Incorrectly](https://doi.org/10.1007/978-3-031-20059-5_9) | ECCV 2022 | [code](https://github.com/facebookresearch/reliable_vqa) |
| [Generic Attention-model Explainability for Interpreting Bi-Modal and Encoder-Decoder Transformers](https://doi.org/10.1109/ICCV48922.2021.00045) | ICCV 2021 | [code](https://github.com/hila-chefer/Transformer-MM-Explainability) |
| [SMIL: Multimodal Learning with Severely Missing Modality](https://doi.org/10.1609/aaai.v35i3.16330) | AAAI 2021 | — |
| [Vision-and-Language or Vision-for-Language? On Cross-Modal Influence in Multimodal Transformers](https://doi.org/10.18653/v1/2021.emnlp-main.775) | EMNLP 2021 | — |
| [Quantifying Attention Flow in Transformers](https://doi.org/10.18653/v1/2020.acl-main.385) | ACL 2020 | — |
| [Words Aren't Enough, Their Order Matters: On the Robustness of Grounding Visual Referring Expressions](https://doi.org/10.18653/v1/2020.acl-main.586) | ACL 2020 | [code](https://github.com/aws/aws-refcocog-adv) |
| [Attention is not Explanation](https://doi.org/10.18653/v1/N19-1357) | NAACL-HLT 2019 | — |
| [Fooling Vision and Language Models Despite Localization and Attention Mechanism](https://doi.org/10.1109/CVPR.2018.00520) | CVPR 2018 | — |
| [Object Hallucination in Image Captioning](https://doi.org/10.18653/v1/D18-1437) | EMNLP 2018 | — |
| [Visual Referring Expression Recognition: What Do Systems Actually Learn?](https://doi.org/10.18653/v1/N18-2123) | NAACL-HLT 2018 | — |
| [Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization](https://doi.org/10.1109/ICCV.2017.74) | ICCV 2017 | [code](https://github.com/ramprs/grad-cam) |

</details>

<a id="video"></a>

## 🎬 Video

**88 papers** · Query-based (DETR) 23 · Dense fusion 14 · Dataset / benchmark 11 · MLLM · mask token 7 · Agentic / RL reasoning 6

<details open>
<summary><b>Datasets & benchmarks</b> (11)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) | Multimedia Systems 2026 | — |
| [V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning](https://openaccess.thecvf.com/content/CVPR2026F/html/Cheng_V-STaR_Benchmarking_Video-LLMs_on_Video_Spatio-Temporal_Reasoning_CVPRF_2026_paper.html) | CVPR 2026 Findings | — |
| [VideoZeroBench: Probing the Limits of Video MLLMs with Spatio-Temporal Evidence Verification](https://arxiv.org/abs/2604.01569) | arXiv ⚠️ | — |
| [CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/70fa5df8e3300dc30bf19bee44a56155-Abstract-Conference.html) | ICLR 2025 | — |
| [Can I Trust Your Answer? Visually Grounded Video Question Answering](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Can_I_Trust_Your_Answer_Visually_Grounded_Video_Question_Answering_CVPR_2024_paper.html) | CVPR 2024 | — |
| [Described Spatial-Temporal Video Detection](https://arxiv.org/abs/2407.05610) | arXiv ⚠️ | — |
| [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://doi.org/10.52202/079017-0900) | NeurIPS 2024 | [code](https://github.com/ReXTime/ReXTime) |
| [A Closer Look at Debiased Temporal Sentence Grounding in Videos: Dataset, Metric, and Approach](https://doi.org/10.1145/3565573) | ACM TOMM 2023 | [code](https://github.com/yytzsy/grounding_changing_distribution) |
| [RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D](https://doi.org/10.1109/iccv51070.2023.01396) | ICCV 2023 | [code](https://github.com/shuheikurita/RefEgo) |
| [Robustness Analysis of Video-Language Models Against Visual and Language Perturbations](https://doi.org/10.52202/068431-2493) | NeurIPS 2022 Datasets and Benchmarks | — |
| [YouRefIt: Embodied Reference Understanding With Language and Gesture](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_YouRefIt_Embodied_Reference_Understanding_With_Language_and_Gesture_ICCV_2021_paper.html) | ICCV 2021 | — |

</details>

<details>
<summary><b>Methods</b> (72)</summary>

| Paper | Venue | Type | Code |
|---|---|---|---|
| [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414) | AAAI 2026 | Dense fusion | [code](https://github.com/KaijingOfficial/DEMR) |
| [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434) | arXiv ⚠️ | Training-free | — |
| [GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation](https://doi.org/10.1007/s11263-026-02729-y) | IJCV 2026 | Query-based (DETR) | [code](https://henghuiding.github.io/GREx) |
| [HERO: Hierarchical Embedding-Refinement for Open-Vocabulary Temporal Sentence Grounding in Videos](https://arxiv.org/abs/2603.06732) | arXiv ⚠️ | Dense fusion | [code](https://github.com/TTingHan-HDU/HERO) |
| [Knowledge-Preserved Model Tuning in Null-Space for Robust Spatio-Temporal Video Grounding](https://arxiv.org/abs/2606.03539) | arXiv ⚠️ | Query-based (DETR) | — |
| [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Learning_to_Refuse_Refusal-Aware_Reinforcement_Fine-Tuning_for_Hard-Irrelevant_Queries_in_CVPR_2026_paper.html) | CVPR 2026 | Agentic / RL reasoning | — |
| [LLM-Powered Query Expansion for Enhancing Boundary Prediction in Language-Driven Action Localization](https://doi.org/10.1007/s11263-026-03083-9) | IJCV 2026 | Dense fusion | — |
| [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458) | arXiv ⚠️ | Agentic / RL reasoning | — |
| [Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence](https://proceedings.mlr.press/v306/meng26e.html) | ICML 2026 | Agentic / RL reasoning | — |
| [Sa2VA: Marrying SAM2 with MLLM for Dense Grounded Understanding of Images and Videos](https://doi.org/10.1109/TPAMI.2026.3720379) | IEEE TPAMI 2026 | MLLM · mask token | [code](https://github.com/Bytedance/Sa2VA) |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 | Promptable seg. + adapter | [code](https://github.com/facebookresearch/sam3) |
| [SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding](https://arxiv.org/abs/2608.30451) | arXiv ⚠️ | Dense fusion | — |
| [Towards Unified Vision-Language Models with Incomplete Multi-Modal Inputs](https://doi.org/10.1609/aaai.v40i5.37387) | AAAI 2026 | Proposal & rank | — |
| [What You Ask is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA](https://arxiv.org/abs/2608.15708) | arXiv ⚠️ | Dense fusion | — |
| [Knowing Your Target: Target-Aware Transformer Makes Better Spatio-Temporal Video Grounding](https://openreview.net/forum?id=WOzffPgVjF) | ICLR 2025 | Query-based (DETR) | [code](https://github.com/HengLan/TA-STVG) |
| [Language Prompt for Autonomous Driving](https://doi.org/10.1609/aaai.v39i8.32902) | AAAI 2025 | Query-based (DETR) | [code](https://github.com/wudongming97/Prompt4Driving) |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://doi.org/10.1109/tpami.2025.3600507) | IEEE TPAMI 2025 | MLLM · mask token | [code](https://henghuiding.com/MeViS/) |
| [Moment of Untruth: Dealing with Negative Queries in Video Moment Retrieval](https://doi.org/10.1109/wacv61041.2025.00521) | WACV 2025 | Query-based (DETR) | [code](https://github.com/keflanagan/MomentofUntruth) |
| [MPG-SAM 2: Adapting SAM 2 with Mask Priors and Global Context for Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Rong_MPG-SAM_2_Adapting_SAM_2_with_Mask_Priors_and_Global_ICCV_2025_paper.html) | ICCV 2025 | Promptable seg. + adapter | [code](https://github.com/rongfu-dsb/MPG-SAM2) |
| [Number it: Temporal Grounding Videos like Flipping Manga](https://doi.org/10.1109/cvpr52734.2025.01284) | CVPR 2025 | Training-free | [code](https://github.com/yongliang-wu/NumPro) |
| [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) | arXiv ⚠️ | MLLM · coords as text | [code](https://github.com/QwenLM/Qwen2.5-VL) |
| [SAM 2: Segment Anything in Images and Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | ICLR 2025 | Promptable seg. + adapter | [code](https://ai.meta.com/sam2 (project site)) |
| [SAMWISE: Infusing Wisdom in SAM2 for Text-Driven Video Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Cuttano_SAMWISE_Infusing_Wisdom_in_SAM2_for_Text-Driven_Video_Segmentation_CVPR_2025_paper.html) | CVPR 2025 | Promptable seg. + adapter | [code](https://github.com/ClaudiaCuttano/SAMWISE) |
| [The Devil is in the Spurious Correlations: Boosting Moment Retrieval with Dynamic Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_The_Devil_is_in_the_Spurious_Correlations_Boosting_Moment_Retrieval_ICCV_2025_paper.html) | ICCV 2025 | Query-based (DETR) | — |
| [Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://doi.org/10.52202/085713-2793) | NeurIPS 2025 | Agentic / RL reasoning | — |
| [TRACE: Temporal Grounding Video LLM via Causal Event Modeling](https://openreview.net/forum?id=14fFV0chUS) | ICLR 2025 | MLLM · coords as text | [code](https://github.com/gyxxyg/TRACE) |
| [UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning](https://arxiv.org/abs/2505.14231) | arXiv ⚠️ | Agentic / RL reasoning | [code](https://amap-ml.github.io/UniVG-R1-page/ (project page)) |
| [VideoGLaMM: A Large Multimodal Model for Pixel-Level Visual Grounding in Videos](https://doi.org/10.1109/cvpr52734.2025.01773) | CVPR 2025 | MLLM · mask token | — |
| [ViLLa: Video Reasoning Segmentation with Large Language Model](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_ViLLa_Video_Reasoning_Segmentation_with_Large_Language_Model_ICCV_2025_paper.html) | ICCV 2025 | MLLM · mask token | — |
| [When Thinking Drifts: Evidential Grounding for Robust Video Reasoning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/788f0d336eeddf698c8d527b1794fca4-Abstract-Conference.html) | NeurIPS 2025 | Agentic / RL reasoning | — |
| [Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding](https://arxiv.org/abs/2408.16272) | arXiv ⚠️ | Dense fusion | [code](https://kaijing.space/SRAM/) |
| [Context-Guided Spatio-Temporal Video Grounding](https://openaccess.thecvf.com/content/CVPR2024/html/Gu_Context-Guided_Spatio-Temporal_Video_Grounding_CVPR_2024_paper.html) | CVPR 2024 | Query-based (DETR) | [code](https://github.com/HengLan/CGSTVG) |
| [Decoupling Static and Hierarchical Motion Perception for Referring Video Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/He_Decoupling_Static_and_Hierarchical_Motion_Perception_for_Referring_Video_Segmentation_CVPR_2024_paper.html) | CVPR 2024 | Query-based (DETR) | [code](https://github.com/heshuting555/DsHmp) |
| [iKUN: Speak to Trackers without Retraining](https://openaccess.thecvf.com/content/CVPR2024/html/Du_iKUN_Speak_to_Trackers_without_Retraining_CVPR_2024_paper.html) | CVPR 2024 | Open-set pre-training | [code](https://github.com/dyhBUPT/iKUN) |
| [Matcher: Segment Anything with One Shot Using All-Purpose Feature Matching](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4df9a5e6bad9e64ebcea453e031142bb-Abstract-Conference.html) | ICLR 2024 | Training-free | [code](https://github.com/aim-uofa/Matcher) |
| [Momentor: Advancing Video Large Language Model with Fine-Grained Temporal Reasoning](https://proceedings.mlr.press/v235/qian24a.html) | ICML 2024 | MLLM · coords as text | [code](https://github.com/DCDmllm/Momentor) |
| [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0cf3e7eefb9d643e93e16ff1d94090a7-Abstract-Conference.html) | NeurIPS 2024 | MLLM · mask token | [code](https://github.com/showlab/VideoLISA) |
| [Personalize Segment Anything Model with One Shot](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4f44e5c82dc7b0ba4472083e5dedb08e-Abstract-Conference.html) | ICLR 2024 | Training-free | [code](https://github.com/ZrrSkywalker/Personalize-SAM) |
| [SnAG: Scalable and Accurate Video Grounding](https://openaccess.thecvf.com/content/CVPR2024/html/Mu_SnAG_Scalable_and_Accurate_Video_Grounding_CVPR_2024_paper.html) | CVPR 2024 | Dense fusion | [code](https://github.com/fmu2/snag_release) |
| [TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding](https://doi.org/10.1109/cvpr52733.2024.01357) | CVPR 2024 | MLLM · coords as text | [code](https://github.com/RenShuhuai-Andy/TimeChat) |
| [VISA: Reasoning Video Object Segmentation via Large Language Models](https://doi.org/10.1007/978-3-031-72633-0_6) | ECCV 2024 | MLLM · mask token | [code](https://github.com/cilinyan/VISA) |
| [Visual In-Context Prompting](https://doi.org/10.1109/CVPR52733.2024.01222) | CVPR 2024 | Query-based (DETR) | [code](https://github.com/UX-Decoder/DINOv) |
| [VTimeLLM: Empower LLM to Grasp Video Moments](https://doi.org/10.1109/cvpr52733.2024.01353) | CVPR 2024 | MLLM · coords as text | [code](https://github.com/huangb23/VTimeLLM) |
| [Correlation-Guided Query-Dependency Calibration for Video Temporal Grounding](https://arxiv.org/abs/2311.08835) | arXiv ⚠️ | Query-based (DETR) | [code](https://github.com/wjun0830/CGDETR) |
| [Knowing Where to Focus: Event-aware Transformer for Video Grounding](https://openaccess.thecvf.com/content/ICCV2023/html/Jang_Knowing_Where_to_Focus_Event-aware_Transformer_for_Video_Grounding_ICCV_2023_paper.html) | ICCV 2023 | Query-based (DETR) | [code](https://github.com/jinhyunj/EaTR) |
| [MeViS: A Large-scale Benchmark for Video Segmentation with Motion Expressions](https://doi.org/10.1109/iccv51070.2023.00254) | ICCV 2023 | Query-based (DETR) | [code](https://henghuiding.github.io/MeViS/) |
| [MomentDiff: Generative Video Moment Retrieval from Random to Real](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d01bda31bbcd780774ff15b534e03c40-Abstract-Conference.html) | NeurIPS 2023 | Query-based (DETR) | [code](https://github.com/IMCCretrieval/MomentDiff) |
| [OnlineRefer: A Simple Online Baseline for Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_OnlineRefer_A_Simple_Online_Baseline_for_Referring_Video_Object_Segmentation_ICCV_2023_paper.html) | ICCV 2023 | Query-based (DETR) | [code](https://github.com/wudongming97/OnlineRefer) |
| [PolyFormer: Referring Image Segmentation as Sequential Polygon Generation](https://doi.org/10.1109/CVPR52729.2023.01789) | CVPR 2023 | Dense fusion | [code](https://polyformer.github.io/) |
| [Referring Multi-Object Tracking](https://doi.org/10.1109/cvpr52729.2023.01406) | CVPR 2023 | Query-based (DETR) | [code](https://github.com/wudongming97/RMOT) |
| [Robust Referring Video Object Segmentation with Cyclic Structural Consensus](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Robust_Referring_Video_Object_Segmentation_with_Cyclic_Structural_Consensus_ICCV_2023_paper.html) | ICCV 2023 | Query-based (DETR) | — |
| [SegGPT: Towards Segmenting Everything In Context](https://doi.org/10.1109/ICCV51070.2023.00110) | ICCV 2023 | Dense fusion | [code](https://github.com/baaivision/Painter) |
| [Spectrum-guided Multi-granularity Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Miao_Spectrum-guided_Multi-granularity_Referring_Video_Object_Segmentation_ICCV_2023_paper.html) | ICCV 2023 | Query-based (DETR) | [code](https://github.com/bo-miao/SgMg) |
| [u-LLaVA: Unifying Multi-Modal Tasks via Large Language Model](https://arxiv.org/abs/2311.05348) | arXiv ⚠️ | MLLM · mask token | [code](https://github.com/OPPOMKLab/u-LLaVA) |
| [Universal Instance Perception as Object Discovery and Retrieval](https://doi.org/10.1109/CVPR52729.2023.01471) | CVPR 2023 | Query-based (DETR) | [code](https://github.com/MasterBin-IIAU/UNINEXT) |
| [UniVTG: Towards Unified Video-Language Temporal Grounding](https://doi.org/10.1109/iccv51070.2023.00262) | ICCV 2023 | Open-set pre-training | [code](https://github.com/showlab/UniVTG) |
| [Embracing Consistency: A One-Stage Approach for Spatio-Temporal Video Grounding](https://papers.nips.cc/paper_files/paper/2022/hash/bc18c538d983cea434f9281148d43e1e-Abstract-Conference.html) | NeurIPS 2022 | Query-based (DETR) | [code](https://github.com/jy0205/STCAT) |
| [End-to-End Referring Video Object Segmentation with Multimodal Transformers](https://openaccess.thecvf.com/content/CVPR2022/html/Botach_End-to-End_Referring_Video_Object_Segmentation_With_Multimodal_Transformers_CVPR_2022_paper.html) | CVPR 2022 | Query-based (DETR) | [code](https://github.com/mttr2021/MTTR) |
| [Human-Centric Spatio-Temporal Video Grounding With Visual Transformers](https://doi.org/10.1109/tcsvt.2021.3085907) | IEEE TCSVT 2022 | Proposal & rank | — |
| [Language as Queries for Referring Video Object Segmentation](https://doi.org/10.1109/cvpr52688.2022.00492) | CVPR 2022 | Query-based (DETR) | [code](https://github.com/wjn922/ReferFormer) |
| [Negative Sample Matters: A Renaissance of Metric Learning for Temporal Grounding](https://doi.org/10.1609/aaai.v36i3.20163) | AAAI 2022 | Open-set pre-training | [code](https://github.com/MCG-NJU/MMN) |
| [Thinking Inside Uncertainty: Interest Moment Perception for Diverse Temporal Grounding](https://doi.org/10.1109/tcsvt.2022.3179314) | IEEE TCSVT 2022 | Dense fusion | — |
| [TubeDETR: Spatio-Temporal Video Grounding with Transformers](https://doi.org/10.1109/cvpr52688.2022.01595) | CVPR 2022 | Query-based (DETR) | — |
| [Video Activity Localisation with Uncertainties in Temporal Boundary](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2818_ECCV_2022_paper.php) | ECCV 2022 | Dense fusion | — |
| [Detecting Moments and Highlights in Videos via Natural Language Queries](https://proceedings.neurips.cc/paper_files/paper/2021/hash/62e0973455fd26eb03e91d5741a4a3bb-Abstract.html) | NeurIPS 2021 | Query-based (DETR) | [code](https://github.com/jayleicn/moment_detr) |
| [Learning 2D Temporal Adjacent Networks for Moment Localization with Natural Language](https://doi.org/10.1609/aaai.v34i07.6984) | AAAI 2020 | Proposal & rank | [code](https://github.com/microsoft/2D-TAN) |
| [Span-based Localizing Network for Natural Language Video Localization](https://doi.org/10.18653/v1/2020.acl-main.585) | ACL 2020 | Dense fusion | [code](https://github.com/IsaacChanghau/VSLNet) |
| [URVOS: Unified Referring Video Object Segmentation Network with a Large-Scale Benchmark](https://doi.org/10.1007/978-3-030-58555-6_13) | ECCV 2020 | Dense fusion | — |
| [Where Does It Exist: Spatio-Temporal Video Grounding for Multi-Form Sentences](https://doi.org/10.1109/cvpr42600.2020.01068) | CVPR 2020 | Proposal & rank | — |
| [Actor and Action Video Segmentation from a Sentence](https://doi.org/10.1109/cvpr.2018.00624) | CVPR 2018 | Dense fusion | — |
| [Localizing Moments in Video with Natural Language](https://doi.org/10.1109/iccv.2017.618) | ICCV 2017 | Proposal & rank | — |
| [TALL: Temporal Activity Localization via Language Query](https://doi.org/10.1109/iccv.2017.563) | ICCV 2017 | Proposal & rank | — |

</details>

<details>
<summary><b>Analyses & audits</b> (5)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding](https://doi.org/10.18653/2026.findings-emnlp.2423) | Findings of EMNLP 2026 | — |
| [On the Consistency of Video Large Language Models in Temporal Comprehension](https://openaccess.thecvf.com/content/CVPR2025/html/Jung_On_the_Consistency_of_Video_Large_Language_Models_in_Temporal_CVPR_2025_paper.html) | CVPR 2025 | [code](https://github.com/minjoong507/Consistency-of-Video-LLM) |
| [A Closer Look at Temporal Sentence Grounding in Videos: Dataset and Metric](https://doi.org/10.1145/3475723.3484247) | ACM MM 2021 Workshop (W) | — |
| [SNEAK: Synonymous Sentences-Aware Adversarial Attack on Natural Language Video Localization](https://arxiv.org/abs/2112.04154) | arXiv ⚠️ | — |
| [Uncovering Hidden Challenges in Query-Based Video Moment Retrieval](https://doi.org/10.5244/c.34.84) | BMVC 2020 | [code](https://mayu-ot.github.io/hidden-challenges-MR) |

</details>

<a id="audio-and-audio-visual"></a>

## 🔊 Audio and audio-visual

**71 papers** · Open-set pre-training 18 · Dense fusion 13 · Query-based (DETR) 12 · Dataset / benchmark 10 · Analysis / audit 5

<details open>
<summary><b>Datasets & benchmarks</b> (10)</summary>

| Paper | Venue | Code |
|---|---|---|
| [ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark](https://arxiv.org/abs/2610.22964) | arXiv ⚠️ | — |
| [AVID: A Benchmark for Omni-Modal Audio-Visual Inconsistency Understanding via Agent-Driven Construction](https://arxiv.org/abs/2604.13593) | arXiv ⚠️ | [code](https://github.com/czx1220/AVID-bench) |
| [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/abs/2609.19991) | arXiv ⚠️ | — |
| [EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning](https://arxiv.org/abs/2610.28444) | arXiv ⚠️ | — |
| [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](https://arxiv.org/abs/2609.17248) | arXiv ⚠️ | — |
| [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3cc685788a311fa35d8d41df93e288ca-Abstract-Conference.html) | ICLR 2025 | [code](https://github.com/kaist-ami/AVHBench) |
| [AVTrustBench: Assessing and Enhancing Reliability and Robustness in Audio-Visual LLMs](https://doi.org/10.1109/ICCV51701.2025.00156) | ICCV 2025 | — |
| [What's Making That Sound Right Now? Video-centric Audio-Visual Localization](https://openaccess.thecvf.com/content/ICCV2025/html/Choi_Whats_Making_That_Sound_Right_Now_Video-centric_Audio-Visual_Localization_ICCV_2025_paper.html) | ICCV 2025 | — |
| [R2-Bench: Benchmarking the Robustness of Referring Perception Models Under Perturbations](https://doi.org/10.1007/978-3-031-72673-6_12) | ECCV 2024 | — |
| [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://doi.org/10.1109/cvpr52688.2022.01842) | CVPR 2022 | [code](https://ego4d-data.org/) |

</details>

<details>
<summary><b>Methods</b> (56)</summary>

| Paper | Venue | Type | Code |
|---|---|---|---|
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 | Dense fusion | — |
| [Hearing and Seeing Through CLIP: A Framework for Self-Supervised Sound Source Localization](https://doi.org/10.1007/s11263-025-02687-x) | IJCV 2026 | Open-set pre-training | — |
| [R-AVST: Empowering Video-LLMs with Fine-Grained Spatio-Temporal Reasoning in Complex Audio-Visual Scenarios](https://doi.org/10.1609/aaai.v40i9.37704) | AAAI 2026 | Agentic / RL reasoning | [code](https://github.com/zhlllau/R-AVST) |
| [Audio Does Matter: Importance-Aware Multi-Granularity Fusion for Video Moment Retrieval](https://doi.org/10.1145/3746027.3754982) | ACM MM 2025 | Dense fusion | [code](https://github.com/HuiGuanLab/IMG) |
| [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265) | CVPR 2025 | Query-based (DETR) | — |
| [Audio-Visual Segmentation with Semantics](https://doi.org/10.1007/s11263-024-02261-x) | IJCV 2025 | Dense fusion | [code](https://github.com/OpenNLPLab/AVSBench) |
| [Crab: A Unified Audio-Visual Scene Understanding Model with Explicit Cooperation](https://doi.org/10.1109/cvpr52734.2025.01752) | CVPR 2025 | MLLM · mask token | [code](https://github.com/GeWu-Lab/Crab) |
| [Detect Any Sound: Open-Vocabulary Sound Event Detection with Multi-Modal Queries](https://doi.org/10.1145/3746027.3755574) | ACM MM 2025 | Query-based (DETR) | — |
| [Empowering LLMs with Pseudo-Untrimmed Videos for Audio-Visual Temporal Understanding](https://doi.org/10.1609/aaai.v39i7.32784) | AAAI 2025 | MLLM · coords as text | — |
| [Language-based Audio Moment Retrieval](https://doi.org/10.1109/icassp49660.2025.10890873) | ICASSP 2025 | Query-based (DETR) | — |
| [Learning from Silence and Noise for Visual Sound Source Localization](https://bmvc2025.bmva.org/proceedings/364/) | BMVC 2025 | Open-set pre-training | — |
| [LongVALE: Vision-Audio-Language-Event Benchmark Towards Time-Aware Omni-Modal Perception of Long Videos](https://doi.org/10.1109/cvpr52734.2025.01766) | CVPR 2025 | MLLM · coords as text | — |
| [MissRAG: Addressing the Missing Modality Challenge in Multimodal Large Language Models](https://doi.org/10.1109/ICCV51701.2025.00308) | ICCV 2025 | Training-free | [code](https://github.com/aimagelab/MissRAG) |
| [Robust Audio-Visual Segmentation via Audio-Guided Visual Convergent Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Robust_Audio-Visual_Segmentation_via_Audio-Guided_Visual_Convergent_Alignment_CVPR_2025_paper.html) | CVPR 2025 | Dense fusion | — |
| [SAM2-LOVE: Segment Anything Model 2 in Language-aided Audio-Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.02694) | CVPR 2025 | Promptable seg. + adapter | — |
| [Seeing Speech and Sound: Distinguishing and Locating Audio Sources in Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.01264) | CVPR 2025 | Open-set pre-training | — |
| [Towards Omnimodal Expressions and Reasoning in Referring Audio-Visual Segmentation](https://doi.org/10.1109/iccv51701.2025.02096) | ICCV 2025 | MLLM · mask token | — |
| [Towards Open-Vocabulary Audio-Visual Event Localization](https://doi.org/10.1109/cvpr52734.2025.00783) | CVPR 2025 | Open-set pre-training | [code](https://github.com/jasongief/OV-AVEL) |
| [TSAM: Temporal SAM Augmented with Multimodal Prompts for Referring Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52734.2025.02230) | CVPR 2025 | Promptable seg. + adapter | — |
| [Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM](https://doi.org/10.52202/085713-4307) | NeurIPS 2025 | MLLM · coords as text | — |
| [AVSegFormer: Audio-Visual Segmentation with Transformer](https://doi.org/10.1609/aaai.v38i11.29104) | AAAI 2024 | Query-based (DETR) | — |
| [BAVS: Bootstrapping Audio-Visual Segmentation by Integrating Foundation Knowledge](https://doi.org/10.1109/tmm.2024.3405622) | IEEE TMM 2024 | Proposal & rank | — |
| [Can CLIP Help Sound Source Localization?](https://doi.org/10.1109/wacv57701.2024.00561) | WACV 2024 | Open-set pre-training | — |
| [Cooperation Does Matter: Exploring Multi-Order Bilateral Relations for Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52733.2024.02562) | CVPR 2024 | Query-based (DETR) | — |
| [CPM: Class-Conditional Prompting Machine for Audio-Visual Segmentation](https://doi.org/10.1007/978-3-031-72684-2_25) | ECCV 2024 | Query-based (DETR) | — |
| [GroundingGPT: Language Enhanced Multi-modal Grounding Model](https://doi.org/10.18653/v1/2024.acl-long.360) | ACL 2024 | MLLM · coords as text | — |
| [MEERKAT: Audio-Visual Large Language Model for Grounding in Space and Time](https://doi.org/10.1007/978-3-031-73039-9_4) | ECCV 2024 | MLLM · coords as text | [code](https://github.com/schowdhury671/meerkat) |
| [Prompting Segmentation with Sound Is Generalizable Audio-Visual Source Localizer](https://doi.org/10.1609/aaai.v38i6.28378) | AAAI 2024 | Promptable seg. + adapter | — |
| [Ref-AVS: Refer and Segment Objects in Audio-Visual Scenes](https://doi.org/10.1007/978-3-031-72904-1_12) | ECCV 2024 | Query-based (DETR) | [code](https://github.com/GeWu-Lab/Ref-AVS) |
| [Stepping Stones: A Progressive Training Strategy for Audio-Visual Semantic Segmentation](https://doi.org/10.1007/978-3-031-73464-9_19) | ECCV 2024 | Query-based (DETR) | — |
| [Towards Weakly Supervised Text-to-Audio Grounding](https://doi.org/10.1109/tmm.2024.3443614) | IEEE TMM 2024 | Open-set pre-training | — |
| [TR-DETR: Task-Reciprocal Transformer for Joint Moment Retrieval and Highlight Detection](https://doi.org/10.1609/aaai.v38i5.28304) | AAAI 2024 | Query-based (DETR) | [code](https://github.com/mingyao1120/TR-DETR) |
| [Unraveling Instance Associations: A Closer Look for Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52733.2024.02502) | CVPR 2024 | Dense fusion | [code](https://github.com/cyh-0/CAVP) |
| [Unveiling and Mitigating Bias in Audio Visual Segmentation](https://doi.org/10.1145/3664647.3680802) | ACM MM 2024 | Query-based (DETR) | — |
| [CATR: Combinatorial-Dependence Audio-Queried Transformer for Audio-Visual Video Segmentation](https://doi.org/10.1145/3581783.3611724) | ACM MM 2023 | Query-based (DETR) | — |
| [Dense-Localizing Audio-Visual Events in Untrimmed Videos: A Large-Scale Benchmark and Baseline](https://doi.org/10.1109/cvpr52729.2023.02197) | CVPR 2023 | Dense fusion | — |
| [Investigating Pooling Strategies and Loss Functions for Weakly-Supervised Text-to-Audio Grounding via Contrastive Learning](https://doi.org/10.1109/icasspw59220.2023.10192960) | ICASSP 2023 Workshops (W) | Open-set pre-training | — |
| [Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning](https://doi.org/10.1109/cvpr52729.2023.00621) | CVPR 2023 | Open-set pre-training | — |
| [Multimodal Variational Auto-encoder based Audio-Visual Segmentation](https://doi.org/10.1109/iccv51070.2023.00094) | ICCV 2023 | Dense fusion | [code](https://github.com/OpenNLPLab/MMVAE-AVS) |
| [Query-Dependent Video Representation for Moment Retrieval and Highlight Detection](https://openaccess.thecvf.com/content/CVPR2023/html/Moon_Query-Dependent_Video_Representation_for_Moment_Retrieval_and_Highlight_Detection_CVPR_2023_paper.html) | CVPR 2023 | Query-based (DETR) | [code](https://github.com/wjun0830/QD-DETR) |
| [Sound Source Localization is All about Cross-Modal Alignment](https://doi.org/10.1109/iccv51070.2023.00715) | ICCV 2023 | Open-set pre-training | — |
| [A Closer Look at Weakly-Supervised Audio-Visual Source Localization](https://doi.org/10.52202/068431-2720) | NeurIPS 2022 | Open-set pre-training | [code](https://github.com/stoneMo/SLAVC) |
| [Audio–Visual Segmentation](https://doi.org/10.1007/978-3-031-19836-6_22) | ECCV 2022 | Dense fusion | [code](https://github.com/OpenNLPLab/AVSBench) |
| [Exploiting Transformation Invariance and Equivariance for Self-supervised Sound Localisation](https://doi.org/10.1145/3503161.3548317) | ACM MM 2022 | Open-set pre-training | — |
| [Learning Sound Localization Better from Semantically Similar Samples](https://doi.org/10.1109/icassp43922.2022.9747867) | ICASSP 2022 | Open-set pre-training | — |
| [Localizing Visual Sounds the Easy Way](https://doi.org/10.1007/978-3-031-19836-6_13) | ECCV 2022 | Open-set pre-training | [code](https://github.com/stoneMo/EZ-VSL) |
| [Mix and Localize: Localizing Sound Sources in Mixtures](https://doi.org/10.1109/cvpr52688.2022.01023) | CVPR 2022 | Open-set pre-training | — |
| [Localizing Visual Sounds the Hard Way](https://doi.org/10.1109/cvpr46437.2021.01659) | CVPR 2021 | Open-set pre-training | — |
| [Positive Sample Propagation along the Audio-Visual Event Line](https://doi.org/10.1109/cvpr46437.2021.00833) | CVPR 2021 | Dense fusion | [code](https://github.com/jasongief/PSP_CVPR_2021) |
| [Text-to-Audio Grounding: Building Correspondence Between Captions and Sound Events](https://doi.org/10.1109/icassp39728.2021.9414834) | ICASSP 2021 | Open-set pre-training | [code](https://github.com/wsntxxn/TextToAudioGrounding) |
| [Unified Multisensory Perception: Weakly-Supervised Audio-Visual Video Parsing](https://doi.org/10.1007/978-3-030-58580-8_26) | ECCV 2020 | Dense fusion | — |
| [Audio-Visual Event Localization in Unconstrained Videos](https://doi.org/10.1007/978-3-030-01216-8_16) | ECCV 2018 | Dense fusion | — |
| [Audio-Visual Scene Analysis with Self-Supervised Multisensory Features](https://doi.org/10.1007/978-3-030-01231-1_39) | ECCV 2018 | Dense fusion | [code](http://andrewowens.com/multisensory) |
| [Learning to Localize Sound Source in Visual Scenes](https://doi.org/10.1109/cvpr.2018.00458) | CVPR 2018 | Open-set pre-training | — |
| [Objects that Sound](https://doi.org/10.1007/978-3-030-01246-5_27) | ECCV 2018 | Open-set pre-training | — |
| [The Sound of Pixels](https://doi.org/10.1007/978-3-030-01246-5_35) | ECCV 2018 | Dense fusion | — |

</details>

<details>
<summary><b>Analyses & audits</b> (5)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Both-or-Neither: Counterfactual Joint-Evidence Auditing for Reliable Audio-Visual Event Localization](https://doi.org/10.1145/3840475.3841438) | Proceedings of the 1st International Workshop on Joint Audio-Video Comprehension and Generation (W) | — |
| [A Critical Assessment of Visual Sound Source Localization Models Including Negative Audio](https://doi.org/10.1109/ICASSP49660.2025.10890384) | ICASSP 2025 | — |
| [Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI models in Sound Localization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) | NeurIPS 2025 | [code](https://github.com/CuriseJia/SSHS) |
| [Unveiling Visual Biases in Audio-Visual Localization Benchmarks](https://doi.org/10.1007/978-3-031-93806-1_17) | ECCV 2024 Workshops (W) | — |
| [Can Audio-Visual Integration Strengthen Robustness Under Multimodal Attacks?](https://openaccess.thecvf.com/content/CVPR2021/html/Tian_Can_Audio-Visual_Integration_Strengthen_Robustness_Under_Multimodal_Attacks_CVPR_2021_paper.html) | CVPR 2021 | — |

</details>

<a id="3d-and-spatial"></a>

## 🧊 3D and spatial

**50 papers** · Proposal & rank 16 · Dense fusion 7 · Dataset / benchmark 6 · Analysis / audit 4 · Query-based (DETR) 4

<details open>
<summary><b>Datasets & benchmarks</b> (6)</summary>

| Paper | Venue | Code |
|---|---|---|
| [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://doi.org/10.1109/CVPR52734.2025.02747) | CVPR 2025 | [code](https://github.com/3d-grand/3d-pope) |
| [Unveiling the Mist over 3D Vision-Language Understanding: Object-centric Evaluation with Chain-of-Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Unveiling_the_Mist_over_3D_Vision-Language_Understanding_Object-centric_Evaluation_with_CVPR_2025_paper.html) | CVPR 2025 | — |
| [ViGiL3D: A Linguistically Diverse Dataset for 3D Visual Grounding](https://doi.org/10.18653/v1/2025.acl-long.1470) | ACL 2025 | — |
| [CityRefer: Geography-aware 3D Visual Grounding Dataset on City-scale Point Cloud Data](https://doi.org/10.52202/075280-3397) | NeurIPS 2023 | [code](https://github.com/ATR-DBI/CityRefer) |
| [Toward Explainable 3D Grounded Visual Question Answering: A New Benchmark and Strong Baseline](https://doi.org/10.1109/TCSVT.2022.3229081) | IEEE TCSVT 2023 | — |
| [SUN-Spot: An RGB-D Dataset With Spatial Referring Expressions](https://doi.org/10.1109/iccvw.2019.00236) | ICCV Workshops 2019 (W) | [code](https://github.com/crmauceri/ReferringExpressions) |

</details>

<details>
<summary><b>Methods</b> (40)</summary>

| Paper | Venue | Type | Code |
|---|---|---|---|
| [Affostruction: 3D Affordance Grounding with Generative Reconstruction](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Affostruction_3D_Affordance_Grounding_with_Generative_Reconstruction_CVPR_2026_paper.html) | CVPR 2026 | Dense fusion | — |
| [HAMMER: Harnessing MLLMs via Cross-Modal Integration for Intention-Driven 3D Affordance Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_HAMMER_Harnessing_MLLMs_via_Cross-Modal_Integration_for_Intention-Driven_3D_Affordance_CVPR_2026_paper.html) | CVPR 2026 | MLLM · mask token | — |
| [LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html) | CVPR 2026 | Open-set pre-training | [code](https://github.com/Tap12345/LangGS) |
| [SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes](https://proceedings.iclr.cc/paper_files/paper/2026/hash/05a3d6c357b596f8ea463e1ccfd441d6-Abstract-Conference.html) | ICLR 2026 | Agentic / RL reasoning | — |
| [GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_GEAL_Generalizable_3D_Affordance_Learning_with_Cross-Modal_Consistency_CVPR_2025_paper.html) | CVPR 2025 | Dense fusion | — |
| [I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs](https://arxiv.org/abs/2506.14495) | arXiv ⚠️ | Proposal & rank | — |
| [ReferSplat: Referring Segmentation in 3D Gaussian Splatting](https://proceedings.mlr.press/v267/he25h.html) | ICML 2025 | Dense fusion | [code](https://github.com/heshuting555/ReferSplat) |
| [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](https://doi.org/10.1109/CVPR52734.2025.00351) | CVPR 2025 | Training-free | [code](https://github.com/iris0329/SeeGround) |
| [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://doi.org/10.1109/CVPR52734.2025.00841) | CVPR 2025 | MLLM · mask token | [code](https://github.com/LaVi-Lab/Video-3D-LLM) |
| [3D-GRES: Generalized 3D Referring Expression Segmentation](https://doi.org/10.1145/3664647.3680841) | ACM MM 2024 | Query-based (DETR) | [code](https://github.com/sosppxo/MDIN) |
| [3D-STMN: Dependency-Driven Superpoint-Text Matching Network for End-to-End 3D Referring Expression Segmentation](https://doi.org/10.1609/aaai.v38i6.28408) | AAAI 2024 | Dense fusion | [code](https://github.com/sosppxo/3D-STMN) |
| [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://doi.org/10.52202/079017-3620) | NeurIPS 2024 | MLLM · coords as text | — |
| [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI](https://doi.org/10.1109/CVPR52733.2024.01868) | CVPR 2024 | Query-based (DETR) | [code](https://github.com/OpenRobotLab/EmbodiedScan) |
| [Four Ways to Improve Verbo-visual Fusion for Dense 3D Visual Grounding](https://doi.org/10.1007/978-3-031-73116-7_12) | ECCV 2024 | Dense fusion | [code](https://github.com/ouenal/concretenet) |
| [LangSplat: 3D Language Gaussian Splatting](https://doi.org/10.1109/CVPR52733.2024.01895) | CVPR 2024 | Training-free | [code](https://github.com/minghanqin/LangSplat) |
| [LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://doi.org/10.1109/ICRA57147.2024.10610443) | ICRA 2024 | Agentic / RL reasoning | — |
| [ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities](https://doi.org/10.1007/978-3-031-73242-3_9) | ECCV 2024 | MLLM · mask token | [code](https://github.com/ZCMax/ScanReason) |
| [SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](https://doi.org/10.1007/978-3-031-72673-6_16) | ECCV 2024 | Proposal & rank | [code](https://github.com/scene-verse/sceneverse) |
| [SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f38cb4cf9a5eaa92b3cfa481832719c6-Abstract-Conference.html) | NeurIPS 2024 | MLLM · coords as text | [code](https://github.com/AnjieCheng/SpatialRGPT) |
| [VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding](https://proceedings.mlr.press/v270/xu25c.html) | CoRL 2024 | Agentic / RL reasoning | [code](https://github.com/OpenRobotLab/VLM-Grounder) |
| [3D-LLM: Injecting the 3D World into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/413885e70482b95dcbeeddc1daf39177-Abstract-Conference.html) | NeurIPS 2023 | MLLM · coords as text | — |
| [3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment](https://doi.org/10.1109/ICCV51070.2023.00272) | ICCV 2023 | Proposal & rank | [code](https://github.com/3d-vista/3D-VisTA) |
| [EDA: Explicit Text-Decoupling and Dense Alignment for 3D Visual Grounding](https://doi.org/10.1109/CVPR52729.2023.01843) | CVPR 2023 | Query-based (DETR) | [code](https://github.com/yanmin-wu/EDA) |
| [LERF: Language Embedded Radiance Fields](https://doi.org/10.1109/ICCV51070.2023.01807) | ICCV 2023 | Training-free | [code](https://github.com/kerrj/lerf) |
| [Multi3DRefer: Grounding Text Description to Multiple 3D Objects](https://doi.org/10.1109/ICCV51070.2023.01397) | ICCV 2023 | Proposal & rank | [code](https://github.com/3dlg-hcvc/M3DRef-CLIP) |
| [ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding](https://doi.org/10.1109/ICCV51070.2023.01410) | ICCV 2023 | Proposal & rank | [code](https://github.com/Ivan-Tang-3D/ViewRefer3D) |
| [3D-SPS: Single-Stage 3D Visual Grounding via Referred Point Progressive Selection](https://doi.org/10.1109/CVPR52688.2022.01596) | CVPR 2022 | Dense fusion | [code](https://github.com/fjhzhixi/3D-SPS) |
| [3DJCG: A Unified Framework for Joint Dense Captioning and Visual Grounding on 3D Point Clouds](https://doi.org/10.1109/CVPR52688.2022.01597) | CVPR 2022 | Proposal & rank | — |
| [Bottom Up Top Down Detection Transformers for Language Grounding in Images and Point Clouds](https://doi.org/10.1007/978-3-031-20059-5_24) | ECCV 2022 | Query-based (DETR) | [code](https://github.com/nickgkan/butd_detr) |
| [D3Net: A Unified Speaker-Listener Architecture for 3D Dense Captioning and Visual Grounding](https://doi.org/10.1007/978-3-031-19824-3_29) | ECCV 2022 | Proposal & rank | [code](https://github.com/daveredrum/D3Net) |
| [Language Conditioned Spatial Relation Reasoning for 3D Object Grounding](https://doi.org/10.52202/068431-1492) | NeurIPS 2022 | Proposal & rank | [code](https://github.com/cshizhe/vil3dref) |
| [LanguageRefer: Spatial-Language Model for 3D Visual Grounding](https://proceedings.mlr.press/v164/roh22a.html) | CoRL 2021 | Proposal & rank | — |
| [Multi-View Transformer for 3D Visual Grounding](https://doi.org/10.1109/CVPR52688.2022.01508) | CVPR 2022 | Proposal & rank | [code](https://github.com/sega-hsj/MVT-3DVG) |
| [ScanQA: 3D Question Answering for Spatial Scene Understanding](https://openaccess.thecvf.com/content/CVPR2022/html/Azuma_ScanQA_3D_Question_Answering_for_Spatial_Scene_Understanding_CVPR_2022_paper.html) | CVPR 2022 | Proposal & rank | [code](https://github.com/ATR-DBI/ScanQA) |
| [3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds](https://doi.org/10.1109/ICCV48922.2021.00292) | ICCV 2021 | Proposal & rank | — |
| [InstanceRefer: Cooperative Holistic Understanding for Visual Grounding on Point Clouds through Instance Multi-level Contextual Referring](https://doi.org/10.1109/ICCV48922.2021.00181) | ICCV 2021 | Proposal & rank | [code](https://github.com/CurryYuan/InstanceRefer) |
| [Refer-it-in-RGBD: A Bottom-up Approach for 3D Visual Grounding in RGBD Images](https://doi.org/10.1109/CVPR46437.2021.00597) | CVPR 2021 | Dense fusion | — |
| [SAT: 2D Semantics Assisted Training for 3D Visual Grounding](https://doi.org/10.1109/ICCV48922.2021.00187) | ICCV 2021 | Proposal & rank | [code](https://github.com/zyang-ur/SAT) |
| [ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes](https://doi.org/10.1007/978-3-030-58452-8_25) | ECCV 2020 | Proposal & rank | [code](https://referit3d.github.io) |
| [ScanRefer: 3D Object Localization in RGB-D Scans Using Natural Language](https://doi.org/10.1007/978-3-030-58565-5_13) | ECCV 2020 | Proposal & rank | [code](https://github.com/daveredrum/ScanRefer) |

</details>

<details>
<summary><b>Analyses & audits</b> (4)</summary>

| Paper | Venue | Code |
|---|---|---|
| [Agreement versus Softmax under Spatial Disambiguation](https://arxiv.org/abs/2610.14210) | arXiv ⚠️ | — |
| [P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](https://neurips.cc/virtual/2026/poster/151816) | NeurIPS 2026 | — |
| [Manipulating the Bounding Box: Multimodal Controlled Backdoor Attacks on 3D Visual Grounding Models](https://doi.org/10.1109/IJCNN64981.2025.11229253) | IJCNN 2025 | — |
| [Seeing is Not Believing: Adversarial Natural Object Optimization for Hard-Label 3D Scene Attacks](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Seeing_is_Not_Believing_Adversarial_Natural_Object_Optimization_for_Hard-Label_CVPR_2025_paper.html) | CVPR 2025 | — |

</details>

<a id="other-sensors-and-domains"></a>

## 🛰️ Other sensors and domains

**18 papers** · Dense fusion 8 · Query-based (DETR) 3 · MLLM · coords as text 3 · Dataset / benchmark 1 · Training-free 1

<details open>
<summary><b>Datasets & benchmarks</b> (1)</summary>

| Paper | Venue | Code |
|---|---|---|
| [RGBT-GroundBench: Visual Grounding Beyond RGB in Complex Real-World Scenarios](https://doi.org/10.1007/978-3-032-37422-6_24) | ECCV 2026 | [code](https://github.com/crazyxiaoxi/RGBT-GroundBench) |

</details>

<details>
<summary><b>Methods</b> (17)</summary>

| Paper | Venue | Type | Code |
|---|---|---|---|
| [CroBIM-U: Uncertainty-Driven Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2601.03490) | arXiv ⚠️ | Dense fusion | — |
| [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) | IEEE TMI 2026 | Query-based (DETR) | [code](https://github.com/aehrc/MedGrounder) |
| [Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching](https://arxiv.org/abs/2608.04568) | arXiv ⚠️ | Query-based (DETR) | — |
| [Calibrating Uncertainty Quantification of Multi-Modal LLMs using Grounding](https://arxiv.org/abs/2505.03788) | arXiv ⚠️ | Training-free | — |
| [Talk2Radar: Bridging Natural Language with 4D mmWave Radar for 3D Referring Expression Comprehension](https://doi.org/10.1109/icra55743.2025.11128399) | ICRA 2025 | Dense fusion | [code](https://github.com/GuanRunwei/Talk2Radar) |
| [Uncertainty-Aware Medical Diagnostic Phrase Identification and Grounding](https://doi.org/10.1109/tpami.2025.3596878) | IEEE TPAMI 2025 | MLLM · mask token | — |
| [GeoChat: Grounded Large Vision-Language Model for Remote Sensing](https://doi.org/10.1109/cvpr52733.2024.02629) | CVPR 2024 | MLLM · coords as text | [code](https://github.com/mbzuai-oryx/geochat) |
| [GeoGround: A Unified Large Vision-Language Model for Remote Sensing Visual Grounding](https://arxiv.org/abs/2411.11904) | arXiv ⚠️ | MLLM · coords as text | [code](https://github.com/zytx121/GeoGround) |
| [Language-Guided Progressive Attention for Visual Grounding in Remote Sensing Images](https://doi.org/10.1109/TGRS.2024.3423663) | IEEE TGRS 2024 | Dense fusion | [code](https://github.com/like413/OPT-RSVG) |
| [MAIRA-2: Grounded Radiology Report Generation](https://arxiv.org/abs/2406.04449) | arXiv ⚠️ | MLLM · coords as text | [code](https://github.com/microsoft/RadFact) |
| [Rotated Multi-Scale Interaction Network for Referring Remote Sensing Image Segmentation](https://doi.org/10.1109/cvpr52733.2024.02517) | CVPR 2024 | Dense fusion | [code](https://github.com/Lsan2401/RMSIN) |
| [RRSIS: Referring Remote Sensing Image Segmentation](https://doi.org/10.1109/tgrs.2024.3369720) | IEEE TGRS 2024 | Dense fusion | [code](https://gitlab.lrz.de/ai4eo/reasoning/rrsis) |
| [WildRefer: 3D Object Localization in Large-Scale Dynamic Scenes with Multi-modal Visual Data and Natural Language](https://doi.org/10.1007/978-3-031-72952-2_26) | ECCV 2024 | Query-based (DETR) | [code](https://github.com/4DVLab/WildRefer) |
| [Medical Phrase Grounding with Region-Phrase Context Contrastive Alignment](https://doi.org/10.1007/978-3-031-43990-2_35) | MICCAI 2023 | Dense fusion | — |
| [RSVG: Exploring Data and Models for Visual Grounding on Remote Sensing Data](https://doi.org/10.1109/tgrs.2023.3250471) | IEEE TGRS 2023 | Dense fusion | [code](https://github.com/ZhanYang-nwpu/RSVG-pytorch) |
| [Making the Most of Text Semantics to Improve Biomedical Vision–Language Processing](https://doi.org/10.1007/978-3-031-20059-5_1) | ECCV 2022 | Open-set pre-training | [code](https://aka.ms/biovil-code) |
| [Visual Grounding in Remote Sensing Images](https://doi.org/10.1145/3503161.3548316) | ACM MM 2022 | Dense fusion | — |

</details>

<a id="reliability-conditions"></a>

## ⚖️ Reliability conditions

How many works evaluate or address each condition (one paper can appear under several). Expand a row's list below the table.

| Condition | Works | Recent examples |
|---|:---:|---|
| Absent target / false premise | 67 | [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z); [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) |
| Ambiguity & distractors | 81 | [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414); [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) |
| Multiple targets | 78 | [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542); [GREx](https://doi.org/10.1007/s11263-026-02729-y) |
| Novel categories | 49 | [HAMMER](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_HAMMER_Harnessing_MLLMs_via_Cross-Modal_Integration_for_Intention-Driven_3D_Affordance_CVPR_2026_paper.html); [LangRef3DGS](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html) |
| Domain / sensor shift | 35 | [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414); [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) |
| Missing modality | 28 | [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542); [Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding](https://doi.org/10.18653/2026.findings-emnlp.2423) |
| Degraded / noisy input | 20 | [Affostruction](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Affostruction_3D_Affordance_Grounding_with_Generative_Reconstruction_CVPR_2026_paper.html); [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) |
| Conflicting modalities | 16 | [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html); [AVHBench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3cc685788a311fa35d8d41df93e288ca-Abstract-Conference.html) |
| Long-horizon drift | 12 | [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265); [LongVALE](https://doi.org/10.1109/cvpr52734.2025.01766) |
| Adversarial / backdoor | 11 | [IAG](https://openaccess.thecvf.com/content/CVPR2026/html/Li_IAG_Input-aware_Backdoor_Attack_on_VLM-based_Visual_Grounding_CVPR_2026_paper.html); [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html) |

<details><summary>Absent target / false premise (67)</summary>

| Paper | Venue |
|---|---|
| [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) | Multimedia Systems 2026 |
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 |
| [Exposing and Evaluating Hallucinations for GUI Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html) | CVPR 2026 |
| [GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation](https://doi.org/10.1007/s11263-026-02729-y) | IJCV 2026 |
| [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) | IEEE TMI 2026 |
| [Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding](https://doi.org/10.18653/2026.findings-emnlp.2423) | Findings of EMNLP 2026 |
| [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Learning_to_Refuse_Refusal-Aware_Reinforcement_Fine-Tuning_for_Hard-Irrelevant_Queries_in_CVPR_2026_paper.html) | CVPR 2026 |
| [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458) | arXiv ⚠️ |
| [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440) | arXiv ⚠️ |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 |
| [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](https://arxiv.org/abs/2608.04698) | arXiv ⚠️ |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://doi.org/10.1109/CVPR52734.2025.02747) | CVPR 2025 |
| [A Critical Assessment of Visual Sound Source Localization Models Including Negative Audio](https://doi.org/10.1109/ICASSP49660.2025.10890384) | ICASSP 2025 |
| [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3cc685788a311fa35d8d41df93e288ca-Abstract-Conference.html) | ICLR 2025 |
| [Advancing Visual Large Language Model for Multi-granular Versatile Perception](https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Advancing_Visual_Large_Language_Model_for_Multi-granular_Versatile_Perception_ICCV_2025_paper.html) | ICCV 2025 |
| [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265) | CVPR 2025 |
| [Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination](https://arxiv.org/abs/2506.21546) | arXiv ⚠️ |
| [Crab: A Unified Audio-Visual Scene Understanding Model with Explicit Cooperation](https://doi.org/10.1109/cvpr52734.2025.01752) | CVPR 2025 |
| [DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy](https://doi.org/10.1109/ICCV51701.2025.01854) | ICCV 2025 |
| [Detect Anything via Next Point Prediction](https://arxiv.org/abs/2510.12798) | arXiv ⚠️ |
| [Hierarchical Alignment-enhanced Adaptive Grounding Network for Generalized Referring Expression Comprehension](https://doi.org/10.1609/aaai.v39i8.32867) | AAAI 2025 |
| [Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9f14fb9acd243c13c95d4a490d1684ce-Abstract-Conference.html) | ICLR 2025 |
| [Learning from Silence and Noise for Visual Sound Source Localization](https://bmvc2025.bmva.org/proceedings/364/) | BMVC 2025 |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://doi.org/10.1109/tpami.2025.3600507) | IEEE TPAMI 2025 |
| [Moment of Untruth: Dealing with Negative Queries in Video Moment Retrieval](https://doi.org/10.1109/wacv61041.2025.00521) | WACV 2025 |
| [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) | arXiv ⚠️ |
| [Reasoning to Attend: Try to Understand How <SEG> Token Works](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_Reasoning_to_Attend_Try_to_Understand_How_SEG_Token_Works_CVPR_2025_paper.html) | CVPR 2025 |
| [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b4008025c2182bfe16fcc8566ee14d64-Abstract-Conference.html) | ICLR 2025 |
| [SAM 2: Segment Anything in Images and Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | ICLR 2025 |
| [SAM2-LOVE: Segment Anything Model 2 in Language-aided Audio-Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.02694) | CVPR 2025 |
| [Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI models in Sound Localization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) | NeurIPS 2025 |
| [TSAM: Temporal SAM Augmented with Multimodal Prompts for Referring Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52734.2025.02230) | CVPR 2025 |
| [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/04d8c25cbf0d5e1b70d64e672ac92637-Abstract-Conference.html) | ICLR 2025 |
| [Towards Omnimodal Expressions and Reasoning in Referring Audio-Visual Segmentation](https://doi.org/10.1109/iccv51701.2025.02096) | ICCV 2025 |
| [Towards Open-Vocabulary Audio-Visual Event Localization](https://doi.org/10.1109/cvpr52734.2025.00783) | CVPR 2025 |
| [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://doi.org/10.1109/CVPR52734.2025.00841) | CVPR 2025 |
| [What's Making That Sound Right Now? Video-centric Audio-Visual Localization](https://openaccess.thecvf.com/content/ICCV2025/html/Choi_Whats_Making_That_Sound_Right_Now_Video-centric_Audio-Visual_Localization_ICCV_2025_paper.html) | ICCV 2025 |
| [3D-GRES: Generalized 3D Referring Expression Segmentation](https://doi.org/10.1145/3664647.3680841) | ACM MM 2024 |
| [Can CLIP Help Sound Source Localization?](https://doi.org/10.1109/wacv57701.2024.00561) | WACV 2024 |
| [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://doi.org/10.52202/079017-3620) | NeurIPS 2024 |
| [Described Spatial-Temporal Video Detection](https://arxiv.org/abs/2407.05610) | arXiv ⚠️ |
| [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | ICLR 2024 |
| [GROUNDHOG: Grounding Large Language Models to Holistic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_GROUNDHOG_Grounding_Large_Language_Models_to_Holistic_Segmentation_CVPR_2024_paper.html) | CVPR 2024 |
| [GSVA: Generalized Segmentation via Multimodal Large Language Models](https://doi.org/10.1109/CVPR52733.2024.00370) | CVPR 2024 |
| [Generating Enhanced Negatives for Training Language-Based Object Detectors](https://doi.org/10.1109/CVPR52733.2024.01290) | CVPR 2024 |
| [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.01363) | CVPR 2024 |
| [PSALM: Pixelwise SegmentAtion with Large Multi-modal Model](https://doi.org/10.1007/978-3-031-72754-2_5) | ECCV 2024 |
| [Ref-AVS: Refer and Segment Objects in Audio-Visual Scenes](https://doi.org/10.1007/978-3-031-72904-1_12) | ECCV 2024 |
| [SAM4MLLM: Enhance Multi-Modal Large Language Model for Referring Expression Segmentation](https://doi.org/10.1007/978-3-031-73004-7_19) | ECCV 2024 |
| [See Say and Segment: Teaching LMMs to Overcome False Premises](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_See_Say_and_Segment_Teaching_LMMs_to_Overcome_False_Premises_CVPR_2024_paper.html) | CVPR 2024 |
| [SimVG: A Simple Framework for Visual Grounding with Decoupled Multi-modal Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dc6319dde4fb182b22fb902da9418566-Abstract-Conference.html) | NeurIPS 2024 |
| [VISA: Reasoning Video Object Segmentation via Large Language Models](https://doi.org/10.1007/978-3-031-72633-0_6) | ECCV 2024 |
| [Beyond One-to-One: Rethinking the Referring Image Segmentation](https://doi.org/10.1109/ICCV51070.2023.00376) | ICCV 2023 |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 |
| [Evaluating Object Hallucination in Large Vision-Language Models](https://doi.org/10.18653/v1/2023.emnlp-main.20) | EMNLP 2023 |
| [GREC: Generalized Referring Expression Comprehension](https://arxiv.org/abs/2308.16182) | arXiv ⚠️ |
| [GRES: Generalized Referring Expression Segmentation](https://doi.org/10.1109/CVPR52729.2023.02259) | CVPR 2023 |
| [LERF: Language Embedded Radiance Fields](https://doi.org/10.1109/ICCV51070.2023.01807) | ICCV 2023 |
| [Multi3DRefer: Grounding Text Description to Multiple 3D Objects](https://doi.org/10.1109/ICCV51070.2023.01397) | ICCV 2023 |
| [RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D](https://doi.org/10.1109/iccv51070.2023.01396) | ICCV 2023 |
| [Robust Referring Video Object Segmentation with Cyclic Structural Consensus](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Robust_Referring_Video_Object_Segmentation_with_Cyclic_Structural_Consensus_ICCV_2023_paper.html) | ICCV 2023 |
| [Sound Source Localization is All about Cross-Modal Alignment](https://doi.org/10.1109/iccv51070.2023.00715) | ICCV 2023 |
| [A Closer Look at Weakly-Supervised Audio-Visual Source Localization](https://doi.org/10.52202/068431-2720) | NeurIPS 2022 |
| [Audio-Visual Scene Analysis with Self-Supervised Multisensory Features](https://doi.org/10.1007/978-3-030-01231-1_39) | ECCV 2018 |
| [Object Hallucination in Image Captioning](https://doi.org/10.18653/v1/D18-1437) | EMNLP 2018 |

</details>

<details><summary>Ambiguity & distractors (81)</summary>

| Paper | Venue |
|---|---|
| [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414) | AAAI 2026 |
| [Agreement versus Softmax under Spatial Disambiguation](https://arxiv.org/abs/2610.14210) | arXiv ⚠️ |
| [CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion](https://arxiv.org/abs/2602.08999) | arXiv ⚠️ |
| [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434) | arXiv ⚠️ |
| [CroBIM-U: Uncertainty-Driven Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2601.03490) | arXiv ⚠️ |
| [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) | Multimedia Systems 2026 |
| [Exposing and Evaluating Hallucinations for GUI Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html) | CVPR 2026 |
| [LLM-Powered Query Expansion for Enhancing Boundary Prediction in Language-Driven Action Localization](https://doi.org/10.1007/s11263-026-03083-9) | IJCV 2026 |
| [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Learning_to_Refuse_Refusal-Aware_Reinforcement_Fine-Tuning_for_Hard-Irrelevant_Queries_in_CVPR_2026_paper.html) | CVPR 2026 |
| [P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](https://neurips.cc/virtual/2026/poster/151816) | NeurIPS 2026 |
| [SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding](https://arxiv.org/abs/2608.30451) | arXiv ⚠️ |
| [Surrogate Uncertainty for Black-box Visual Grounding](https://arxiv.org/abs/2610.39798) | arXiv ⚠️ |
| [Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Method](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f09ab24aa37ae2664b3d923cdb0319b5-Abstract-Conference.html) | ICLR 2026 |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [What You Ask is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA](https://arxiv.org/abs/2608.15708) | arXiv ⚠️ |
| [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978) | arXiv ⚠️ |
| [Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination](https://arxiv.org/abs/2506.21546) | arXiv ⚠️ |
| [I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs](https://arxiv.org/abs/2506.14495) | arXiv ⚠️ |
| [Knowing Your Target: Target-Aware Transformer Makes Better Spatio-Temporal Video Grounding](https://openreview.net/forum?id=WOzffPgVjF) | ICLR 2025 |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://doi.org/10.1109/tpami.2025.3600507) | IEEE TPAMI 2025 |
| [ReferSplat: Referring Segmentation in 3D Gaussian Splatting](https://proceedings.mlr.press/v267/he25h.html) | ICML 2025 |
| [Revisiting Referring Expression Comprehension Evaluation in the Era of Large Multimodal Models](https://doi.org/10.1109/CVPRW67362.2025.00056) | CVPR 2025 Workshops (W) |
| [Robust Audio-Visual Segmentation via Audio-Guided Visual Convergent Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Robust_Audio-Visual_Segmentation_via_Audio-Guided_Visual_Convergent_Alignment_CVPR_2025_paper.html) | CVPR 2025 |
| [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](https://doi.org/10.1109/CVPR52734.2025.00351) | CVPR 2025 |
| [The Devil is in the Spurious Correlations: Boosting Moment Retrieval with Dynamic Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_The_Devil_is_in_the_Spurious_Correlations_Boosting_Moment_Retrieval_ICCV_2025_paper.html) | ICCV 2025 |
| [Unveiling Visual Biases in Audio-Visual Localization Benchmarks](https://doi.org/10.1007/978-3-031-93806-1_17) | ECCV 2024 Workshops (W) |
| [Unveiling the Mist over 3D Vision-Language Understanding: Object-centric Evaluation with Chain-of-Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Unveiling_the_Mist_over_3D_Vision-Language_Understanding_Object-centric_Evaluation_with_CVPR_2025_paper.html) | CVPR 2025 |
| [ViGiL3D: A Linguistically Diverse Dataset for 3D Visual Grounding](https://doi.org/10.18653/v1/2025.acl-long.1470) | ACL 2025 |
| [What's Making That Sound Right Now? Video-centric Audio-Visual Localization](https://openaccess.thecvf.com/content/ICCV2025/html/Choi_Whats_Making_That_Sound_Right_Now_Video-centric_Audio-Visual_Localization_ICCV_2025_paper.html) | ICCV 2025 |
| [3D-GRES: Generalized 3D Referring Expression Segmentation](https://doi.org/10.1145/3664647.3680841) | ACM MM 2024 |
| [3D-STMN: Dependency-Driven Superpoint-Text Matching Network for End-to-End 3D Referring Expression Segmentation](https://doi.org/10.1609/aaai.v38i6.28408) | AAAI 2024 |
| [CPM: Class-Conditional Prompting Machine for Audio-Visual Segmentation](https://doi.org/10.1007/978-3-031-72684-2_25) | ECCV 2024 |
| [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://doi.org/10.52202/079017-3620) | NeurIPS 2024 |
| [Context-Guided Spatio-Temporal Video Grounding](https://openaccess.thecvf.com/content/CVPR2024/html/Gu_Context-Guided_Spatio-Temporal_Video_Grounding_CVPR_2024_paper.html) | CVPR 2024 |
| [Decoupling Static and Hierarchical Motion Perception for Referring Video Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/He_Decoupling_Static_and_Hierarchical_Motion_Perception_for_Referring_Video_Segmentation_CVPR_2024_paper.html) | CVPR 2024 |
| [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI](https://doi.org/10.1109/CVPR52733.2024.01868) | CVPR 2024 |
| [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | ICLR 2024 |
| [Four Ways to Improve Verbo-visual Fusion for Dense 3D Visual Grounding](https://doi.org/10.1007/978-3-031-73116-7_12) | ECCV 2024 |
| [LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://doi.org/10.1109/ICRA57147.2024.10610443) | ICRA 2024 |
| [Mono3DVG: 3D Visual Grounding in Monocular Images](https://doi.org/10.1609/aaai.v38i7.28525) | AAAI 2024 |
| [Personalize Segment Anything Model with One Shot](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4f44e5c82dc7b0ba4472083e5dedb08e-Abstract-Conference.html) | ICLR 2024 |
| [SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](https://doi.org/10.1007/978-3-031-72673-6_16) | ECCV 2024 |
| [Unraveling Instance Associations: A Closer Look for Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52733.2024.02502) | CVPR 2024 |
| [Unveiling and Mitigating Bias in Audio Visual Segmentation](https://doi.org/10.1145/3664647.3680802) | ACM MM 2024 |
| [VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding](https://proceedings.mlr.press/v270/xu25c.html) | CoRL 2024 |
| [3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment](https://doi.org/10.1109/ICCV51070.2023.00272) | ICCV 2023 |
| [A Closer Look at Debiased Temporal Sentence Grounding in Videos: Dataset, Metric, and Approach](https://doi.org/10.1145/3565573) | ACM TOMM 2023 |
| [EDA: Explicit Text-Decoupling and Dense Alignment for 3D Visual Grounding](https://doi.org/10.1109/CVPR52729.2023.01843) | CVPR 2023 |
| [MeViS: A Large-scale Benchmark for Video Segmentation with Motion Expressions](https://doi.org/10.1109/iccv51070.2023.00254) | ICCV 2023 |
| [Multi3DRefer: Grounding Text Description to Multiple 3D Objects](https://doi.org/10.1109/ICCV51070.2023.01397) | ICCV 2023 |
| [RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D](https://doi.org/10.1109/iccv51070.2023.01396) | ICCV 2023 |
| [Segment Anything](https://doi.org/10.1109/ICCV51070.2023.00371) | ICCV 2023 |
| [ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding](https://doi.org/10.1109/ICCV51070.2023.01410) | ICCV 2023 |
| [3D-SPS: Single-Stage 3D Visual Grounding via Referred Point Progressive Selection](https://doi.org/10.1109/CVPR52688.2022.01596) | CVPR 2022 |
| [3DJCG: A Unified Framework for Joint Dense Captioning and Visual Grounding on 3D Point Clouds](https://doi.org/10.1109/CVPR52688.2022.01597) | CVPR 2022 |
| [Bottom Up Top Down Detection Transformers for Language Grounding in Images and Point Clouds](https://doi.org/10.1007/978-3-031-20059-5_24) | ECCV 2022 |
| [D3Net: A Unified Speaker-Listener Architecture for 3D Dense Captioning and Visual Grounding](https://doi.org/10.1007/978-3-031-19824-3_29) | ECCV 2022 |
| [Human-Centric Spatio-Temporal Video Grounding With Visual Transformers](https://doi.org/10.1109/tcsvt.2021.3085907) | IEEE TCSVT 2022 |
| [Language Conditioned Spatial Relation Reasoning for 3D Object Grounding](https://doi.org/10.52202/068431-1492) | NeurIPS 2022 |
| [LanguageRefer: Spatial-Language Model for 3D Visual Grounding](https://proceedings.mlr.press/v164/roh22a.html) | CoRL 2021 |
| [Multi-View Transformer for 3D Visual Grounding](https://doi.org/10.1109/CVPR52688.2022.01508) | CVPR 2022 |
| [Thinking Inside Uncertainty: Interest Moment Perception for Diverse Temporal Grounding](https://doi.org/10.1109/tcsvt.2022.3179314) | IEEE TCSVT 2022 |
| [Video Activity Localisation with Uncertainties in Temporal Boundary](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2818_ECCV_2022_paper.php) | ECCV 2022 |
| [3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds](https://doi.org/10.1109/ICCV48922.2021.00292) | ICCV 2021 |
| [Giving Commands to a Self-Driving Car: How to Deal with Uncertain Situations?](https://doi.org/10.1016/j.engappai.2021.104257) | Engineering Applications of Artificial Intelligence 2021 |
| [InstanceRefer: Cooperative Holistic Understanding for Visual Grounding on Point Clouds through Instance Multi-level Contextual Referring](https://doi.org/10.1109/ICCV48922.2021.00181) | ICCV 2021 |
| [Positive Sample Propagation along the Audio-Visual Event Line](https://doi.org/10.1109/cvpr46437.2021.00833) | CVPR 2021 |
| [SAT: 2D Semantics Assisted Training for 3D Visual Grounding](https://doi.org/10.1109/ICCV48922.2021.00187) | ICCV 2021 |
| [YouRefIt: Embodied Reference Understanding With Language and Gesture](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_YouRefIt_Embodied_Reference_Understanding_With_Language_and_Gesture_ICCV_2021_paper.html) | ICCV 2021 |
| [Cops-Ref: A New Dataset and Task on Compositional Referring Expression Comprehension](https://doi.org/10.1109/CVPR42600.2020.01010) | CVPR 2020 |
| [ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes](https://doi.org/10.1007/978-3-030-58452-8_25) | ECCV 2020 |
| [ScanRefer: 3D Object Localization in RGB-D Scans Using Natural Language](https://doi.org/10.1007/978-3-030-58565-5_13) | ECCV 2020 |
| [Uncovering Hidden Challenges in Query-Based Video Moment Retrieval](https://doi.org/10.5244/c.34.84) | BMVC 2020 |
| [Where Does It Exist: Spatio-Temporal Video Grounding for Multi-Form Sentences](https://doi.org/10.1109/cvpr42600.2020.01068) | CVPR 2020 |
| [Words Aren't Enough, Their Order Matters: On the Robustness of Grounding Visual Referring Expressions](https://doi.org/10.18653/v1/2020.acl-main.586) | ACL 2020 |
| [CLEVR-Ref+: Diagnosing Visual Reasoning With Referring Expressions](https://doi.org/10.1109/CVPR.2019.00431) | CVPR 2019 |
| [SUN-Spot: An RGB-D Dataset With Spatial Referring Expressions](https://doi.org/10.1109/iccvw.2019.00236) | ICCV Workshops 2019 (W) |
| [Talk2Car: Taking Control of Your Self-Driving Car](https://doi.org/10.18653/v1/d19-1215) | EMNLP-IJCNLP 2019 |
| [Generation and Comprehension of Unambiguous Object Descriptions](https://doi.org/10.1109/CVPR.2016.9) | CVPR 2016 |
| [Modeling Context in Referring Expressions](https://doi.org/10.1007/978-3-319-46475-6_5) | ECCV 2016 |
| [ReferItGame: Referring to Objects in Photographs of Natural Scenes](https://doi.org/10.3115/v1/D14-1086) | EMNLP 2014 |

</details>

<details><summary>Multiple targets (78)</summary>

| Paper | Venue |
|---|---|
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 |
| [GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation](https://doi.org/10.1007/s11263-026-02729-y) | IJCV 2026 |
| [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) | IEEE TMI 2026 |
| [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458) | arXiv ⚠️ |
| [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440) | arXiv ⚠️ |
| [R-AVST: Empowering Video-LLMs with Fine-Grained Spatio-Temporal Reasoning in Complex Audio-Visual Scenarios](https://doi.org/10.1609/aaai.v40i9.37704) | AAAI 2026 |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 |
| [Sa2VA: Marrying SAM2 with MLLM for Dense Grounded Understanding of Images and Videos](https://doi.org/10.1109/TPAMI.2026.3720379) | IEEE TPAMI 2026 |
| [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_SegCompass_Exploring_Interpretable_Alignment_with_Sparse_Autoencoders_for_Enhanced_Reasoning_CVPR_2026_paper.html) | CVPR 2026 |
| [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](https://arxiv.org/abs/2608.04698) | arXiv ⚠️ |
| [Advancing Visual Large Language Model for Multi-granular Versatile Perception](https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Advancing_Visual_Large_Language_Model_for_Multi-granular_Versatile_Perception_ICCV_2025_paper.html) | ICCV 2025 |
| [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265) | CVPR 2025 |
| [Audio-Visual Segmentation with Semantics](https://doi.org/10.1007/s11263-024-02261-x) | IJCV 2025 |
| [Crab: A Unified Audio-Visual Scene Understanding Model with Explicit Cooperation](https://doi.org/10.1109/cvpr52734.2025.01752) | CVPR 2025 |
| [DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy](https://doi.org/10.1109/ICCV51701.2025.01854) | ICCV 2025 |
| [Detect Anything via Next Point Prediction](https://arxiv.org/abs/2510.12798) | arXiv ⚠️ |
| [Hierarchical Alignment-enhanced Adaptive Grounding Network for Generalized Referring Expression Comprehension](https://doi.org/10.1609/aaai.v39i8.32867) | AAAI 2025 |
| [Language Prompt for Autonomous Driving](https://doi.org/10.1609/aaai.v39i8.32902) | AAAI 2025 |
| [MPG-SAM 2: Adapting SAM 2 with Mask Priors and Global Context for Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Rong_MPG-SAM_2_Adapting_SAM_2_with_Mask_Priors_and_Global_ICCV_2025_paper.html) | ICCV 2025 |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://doi.org/10.1109/tpami.2025.3600507) | IEEE TPAMI 2025 |
| [POPEN: Preference-Based Optimization and Ensemble for LVLM-Based Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_POPEN_Preference-Based_Optimization_and_Ensemble_for_LVLM-Based_Reasoning_Segmentation_CVPR_2025_paper.html) | CVPR 2025 |
| [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) | arXiv ⚠️ |
| [SAMWISE: Infusing Wisdom in SAM2 for Text-Driven Video Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Cuttano_SAMWISE_Infusing_Wisdom_in_SAM2_for_Text-Driven_Video_Segmentation_CVPR_2025_paper.html) | CVPR 2025 |
| [Seeing Speech and Sound: Distinguishing and Locating Audio Sources in Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.01264) | CVPR 2025 |
| [Talk2Radar: Bridging Natural Language with 4D mmWave Radar for 3D Referring Expression Comprehension](https://doi.org/10.1109/icra55743.2025.11128399) | ICRA 2025 |
| [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/04d8c25cbf0d5e1b70d64e672ac92637-Abstract-Conference.html) | ICLR 2025 |
| [Towards Omnimodal Expressions and Reasoning in Referring Audio-Visual Segmentation](https://doi.org/10.1109/iccv51701.2025.02096) | ICCV 2025 |
| [ViLLa: Video Reasoning Segmentation with Large Language Model](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_ViLLa_Video_Reasoning_Segmentation_with_Large_Language_Model_ICCV_2025_paper.html) | ICCV 2025 |
| [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://doi.org/10.1109/CVPR52734.2025.00841) | CVPR 2025 |
| [VideoGLaMM: A Large Multimodal Model for Pixel-Level Visual Grounding in Videos](https://doi.org/10.1109/cvpr52734.2025.01773) | CVPR 2025 |
| [What's Making That Sound Right Now? Video-centric Audio-Visual Localization](https://openaccess.thecvf.com/content/ICCV2025/html/Choi_Whats_Making_That_Sound_Right_Now_Video-centric_Audio-Visual_Localization_ICCV_2025_paper.html) | ICCV 2025 |
| [3D-GRES: Generalized 3D Referring Expression Segmentation](https://doi.org/10.1145/3664647.3680841) | ACM MM 2024 |
| [AVSegFormer: Audio-Visual Segmentation with Transformer](https://doi.org/10.1609/aaai.v38i11.29104) | AAAI 2024 |
| [BAVS: Bootstrapping Audio-Visual Segmentation by Integrating Foundation Knowledge](https://doi.org/10.1109/tmm.2024.3405622) | IEEE TMM 2024 |
| [CPM: Class-Conditional Prompting Machine for Audio-Visual Segmentation](https://doi.org/10.1007/978-3-031-72684-2_25) | ECCV 2024 |
| [Can CLIP Help Sound Source Localization?](https://doi.org/10.1109/wacv57701.2024.00561) | WACV 2024 |
| [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://doi.org/10.52202/079017-3620) | NeurIPS 2024 |
| [Cooperation Does Matter: Exploring Multi-Order Bilateral Relations for Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52733.2024.02562) | CVPR 2024 |
| [Decoupling Static and Hierarchical Motion Perception for Referring Video Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/He_Decoupling_Static_and_Hierarchical_Motion_Perception_for_Referring_Video_Segmentation_CVPR_2024_paper.html) | CVPR 2024 |
| [Described Spatial-Temporal Video Detection](https://arxiv.org/abs/2407.05610) | arXiv ⚠️ |
| [GLaMM: Pixel Grounding Large Multimodal Model](https://doi.org/10.1109/CVPR52733.2024.01236) | CVPR 2024 |
| [GROUNDHOG: Grounding Large Language Models to Holistic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_GROUNDHOG_Grounding_Large_Language_Models_to_Holistic_Segmentation_CVPR_2024_paper.html) | CVPR 2024 |
| [GSVA: Generalized Segmentation via Multimodal Large Language Models](https://doi.org/10.1109/CVPR52733.2024.00370) | CVPR 2024 |
| [Generating Enhanced Negatives for Training Language-Based Object Detectors](https://doi.org/10.1109/CVPR52733.2024.01290) | CVPR 2024 |
| [GeoChat: Grounded Large Vision-Language Model for Remote Sensing](https://doi.org/10.1109/cvpr52733.2024.02629) | CVPR 2024 |
| [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0cf3e7eefb9d643e93e16ff1d94090a7-Abstract-Conference.html) | NeurIPS 2024 |
| [PSALM: Pixelwise SegmentAtion with Large Multi-modal Model](https://doi.org/10.1007/978-3-031-72754-2_5) | ECCV 2024 |
| [PixelLM: Pixel Reasoning with Large Multimodal Model](https://doi.org/10.1109/CVPR52733.2024.02491) | CVPR 2024 |
| [Ref-AVS: Refer and Segment Objects in Audio-Visual Scenes](https://doi.org/10.1007/978-3-031-72904-1_12) | ECCV 2024 |
| [SAM4MLLM: Enhance Multi-Modal Large Language Model for Referring Expression Segmentation](https://doi.org/10.1007/978-3-031-73004-7_19) | ECCV 2024 |
| [SimVG: A Simple Framework for Visual Grounding with Decoupled Multi-modal Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dc6319dde4fb182b22fb902da9418566-Abstract-Conference.html) | NeurIPS 2024 |
| [Stepping Stones: A Progressive Training Strategy for Audio-Visual Semantic Segmentation](https://doi.org/10.1007/978-3-031-73464-9_19) | ECCV 2024 |
| [T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy](https://doi.org/10.1007/978-3-031-73414-4_3) | ECCV 2024 |
| [Unraveling Instance Associations: A Closer Look for Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52733.2024.02502) | CVPR 2024 |
| [Unveiling and Mitigating Bias in Audio Visual Segmentation](https://doi.org/10.1145/3664647.3680802) | ACM MM 2024 |
| [VISA: Reasoning Video Object Segmentation via Large Language Models](https://doi.org/10.1007/978-3-031-72633-0_6) | ECCV 2024 |
| [iKUN: Speak to Trackers without Retraining](https://openaccess.thecvf.com/content/CVPR2024/html/Du_iKUN_Speak_to_Trackers_without_Retraining_CVPR_2024_paper.html) | CVPR 2024 |
| [Beyond One-to-One: Rethinking the Referring Image Segmentation](https://doi.org/10.1109/ICCV51070.2023.00376) | ICCV 2023 |
| [CATR: Combinatorial-Dependence Audio-Queried Transformer for Audio-Visual Video Segmentation](https://doi.org/10.1145/3581783.3611724) | ACM MM 2023 |
| [Dense-Localizing Audio-Visual Events in Untrimmed Videos: A Large-Scale Benchmark and Baseline](https://doi.org/10.1109/cvpr52729.2023.02197) | CVPR 2023 |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 |
| [GREC: Generalized Referring Expression Comprehension](https://arxiv.org/abs/2308.16182) | arXiv ⚠️ |
| [GRES: Generalized Referring Expression Segmentation](https://doi.org/10.1109/CVPR52729.2023.02259) | CVPR 2023 |
| [LISA++: An Improved Baseline for Reasoning Segmentation with Large Language Model](https://arxiv.org/abs/2312.17240) | arXiv ⚠️ |
| [Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning](https://doi.org/10.1109/cvpr52729.2023.00621) | CVPR 2023 |
| [MeViS: A Large-scale Benchmark for Video Segmentation with Motion Expressions](https://doi.org/10.1109/iccv51070.2023.00254) | ICCV 2023 |
| [Multi3DRefer: Grounding Text Description to Multiple 3D Objects](https://doi.org/10.1109/ICCV51070.2023.01397) | ICCV 2023 |
| [Multimodal Variational Auto-encoder based Audio-Visual Segmentation](https://doi.org/10.1109/iccv51070.2023.00094) | ICCV 2023 |
| [Referring Multi-Object Tracking](https://doi.org/10.1109/cvpr52729.2023.01406) | CVPR 2023 |
| [Audio–Visual Segmentation](https://doi.org/10.1007/978-3-031-19836-6_22) | ECCV 2022 |
| [Mix and Localize: Localizing Sound Sources in Mixtures](https://doi.org/10.1109/cvpr52688.2022.01023) | CVPR 2022 |
| [Thinking Inside Uncertainty: Interest Moment Perception for Diverse Temporal Grounding](https://doi.org/10.1109/tcsvt.2022.3179314) | IEEE TCSVT 2022 |
| [Detecting Moments and Highlights in Videos via Natural Language Queries](https://proceedings.neurips.cc/paper_files/paper/2021/hash/62e0973455fd26eb03e91d5741a4a3bb-Abstract.html) | NeurIPS 2021 |
| [MDETR - Modulated Detection for End-to-End Multi-Modal Understanding](https://doi.org/10.1109/ICCV48922.2021.00180) | ICCV 2021 |
| [Unified Multisensory Perception: Weakly-Supervised Audio-Visual Video Parsing](https://doi.org/10.1007/978-3-030-58580-8_26) | ECCV 2020 |
| [The Sound of Pixels](https://doi.org/10.1007/978-3-030-01246-5_35) | ECCV 2018 |
| [Flickr30k Entities: Collecting Region-to-Phrase Correspondences for Richer Image-to-Sentence Models](https://doi.org/10.1007/s11263-016-0965-7) | IJCV 2017 |

</details>

<details><summary>Novel categories (49)</summary>

| Paper | Venue |
|---|---|
| [HAMMER: Harnessing MLLMs via Cross-Modal Integration for Intention-Driven 3D Affordance Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_HAMMER_Harnessing_MLLMs_via_Cross-Modal_Integration_for_Intention-Driven_3D_Affordance_CVPR_2026_paper.html) | CVPR 2026 |
| [HERO: Hierarchical Embedding-Refinement for Open-Vocabulary Temporal Sentence Grounding in Videos](https://arxiv.org/abs/2603.06732) | arXiv ⚠️ |
| [LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html) | CVPR 2026 |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 |
| [Advancing Visual Large Language Model for Multi-granular Versatile Perception](https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Advancing_Visual_Large_Language_Model_for_Multi-granular_Versatile_Perception_ICCV_2025_paper.html) | ICCV 2025 |
| [Crab: A Unified Audio-Visual Scene Understanding Model with Explicit Cooperation](https://doi.org/10.1109/cvpr52734.2025.01752) | CVPR 2025 |
| [Detect Any Sound: Open-Vocabulary Sound Event Detection with Multi-Modal Queries](https://doi.org/10.1145/3746027.3755574) | ACM MM 2025 |
| [GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_GEAL_Generalizable_3D_Affordance_Learning_with_Cross-Modal_Consistency_CVPR_2025_paper.html) | CVPR 2025 |
| [Revisiting Referring Expression Comprehension Evaluation in the Era of Large Multimodal Models](https://doi.org/10.1109/CVPRW67362.2025.00056) | CVPR 2025 Workshops (W) |
| [SAM2-LOVE: Segment Anything Model 2 in Language-aided Audio-Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.02694) | CVPR 2025 |
| [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](https://doi.org/10.1109/CVPR52734.2025.00351) | CVPR 2025 |
| [TSAM: Temporal SAM Augmented with Multimodal Prompts for Referring Audio-Visual Segmentation](https://doi.org/10.1109/cvpr52734.2025.02230) | CVPR 2025 |
| [Towards Omnimodal Expressions and Reasoning in Referring Audio-Visual Segmentation](https://doi.org/10.1109/iccv51701.2025.02096) | ICCV 2025 |
| [Towards Open-Vocabulary Audio-Visual Event Localization](https://doi.org/10.1109/cvpr52734.2025.00783) | CVPR 2025 |
| [ViGiL3D: A Linguistically Diverse Dataset for 3D Visual Grounding](https://doi.org/10.18653/v1/2025.acl-long.1470) | ACL 2025 |
| [Visual-RFT: Visual Reinforcement Fine-Tuning](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Visual-RFT_Visual_Reinforcement_Fine-Tuning_ICCV_2025_paper.html) | ICCV 2025 |
| [Can CLIP Help Sound Source Localization?](https://doi.org/10.1109/wacv57701.2024.00561) | WACV 2024 |
| [Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection](https://doi.org/10.1007/978-3-031-72970-6_3) | ECCV 2024 |
| [LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://doi.org/10.1109/ICRA57147.2024.10610443) | ICRA 2024 |
| [LangSplat: 3D Language Gaussian Splatting](https://doi.org/10.1109/CVPR52733.2024.01895) | CVPR 2024 |
| [Matcher: Segment Anything with One Shot Using All-Purpose Feature Matching](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4df9a5e6bad9e64ebcea453e031142bb-Abstract-Conference.html) | ICLR 2024 |
| [PSALM: Pixelwise SegmentAtion with Large Multi-modal Model](https://doi.org/10.1007/978-3-031-72754-2_5) | ECCV 2024 |
| [Personalize Segment Anything Model with One Shot](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4f44e5c82dc7b0ba4472083e5dedb08e-Abstract-Conference.html) | ICLR 2024 |
| [Prompting Segmentation with Sound Is Generalizable Audio-Visual Source Localizer](https://doi.org/10.1609/aaai.v38i6.28378) | AAAI 2024 |
| [Ref-AVS: Refer and Segment Objects in Audio-Visual Scenes](https://doi.org/10.1007/978-3-031-72904-1_12) | ECCV 2024 |
| [T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy](https://doi.org/10.1007/978-3-031-73414-4_3) | ECCV 2024 |
| [Visual In-Context Prompting](https://doi.org/10.1109/CVPR52733.2024.01222) | CVPR 2024 |
| [Contrastive Grouping with Transformer for Referring Image Segmentation](https://doi.org/10.1109/CVPR52729.2023.02257) | CVPR 2023 |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 |
| [Generalized Decoding for Pixel, Image, and Language](https://doi.org/10.1109/CVPR52729.2023.01451) | CVPR 2023 |
| [LERF: Language Embedded Radiance Fields](https://doi.org/10.1109/ICCV51070.2023.01807) | ICCV 2023 |
| [Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning](https://doi.org/10.1109/cvpr52729.2023.00621) | CVPR 2023 |
| [Segment Everything Everywhere All at Once](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html) | NeurIPS 2023 |
| [Sound Source Localization is All about Cross-Modal Alignment](https://doi.org/10.1109/iccv51070.2023.00715) | ICCV 2023 |
| [Zero-shot Referring Image Segmentation with Global-Local Context Features](https://doi.org/10.1109/CVPR52729.2023.01864) | CVPR 2023 |
| [A Closer Look at Weakly-Supervised Audio-Visual Source Localization](https://doi.org/10.52202/068431-2720) | NeurIPS 2022 |
| [Exploiting Transformation Invariance and Equivariance for Self-supervised Sound Localisation](https://doi.org/10.1145/3503161.3548317) | ACM MM 2022 |
| [GRIT: General Robust Image Task Benchmark](https://arxiv.org/abs/2204.13653) | arXiv ⚠️ |
| [Grounded Language-Image Pre-training](https://doi.org/10.1109/CVPR52688.2022.01069) | CVPR 2022 |
| [Localizing Visual Sounds the Easy Way](https://doi.org/10.1007/978-3-031-19836-6_13) | ECCV 2022 |
| [Localizing Visual Sounds the Hard Way](https://doi.org/10.1109/cvpr46437.2021.01659) | CVPR 2021 |
| [MDETR - Modulated Detection for End-to-End Multi-Modal Understanding](https://doi.org/10.1109/ICCV48922.2021.00180) | ICCV 2021 |
| [Cops-Ref: A New Dataset and Task on Compositional Referring Expression Comprehension](https://doi.org/10.1109/CVPR42600.2020.01010) | CVPR 2020 |
| [Graph-Structured Referring Expression Reasoning in the Wild](https://doi.org/10.1109/CVPR42600.2020.00997) | CVPR 2020 |
| [CLEVR-Ref+: Diagnosing Visual Reasoning With Referring Expressions](https://doi.org/10.1109/CVPR.2019.00431) | CVPR 2019 |
| [Zero-Shot Grounding of Objects from Natural Language Queries](https://doi.org/10.1109/ICCV.2019.00479) | ICCV 2019 |
| [Object Hallucination in Image Captioning](https://doi.org/10.18653/v1/D18-1437) | EMNLP 2018 |
| [TALL: Temporal Activity Localization via Language Query](https://doi.org/10.1109/iccv.2017.563) | ICCV 2017 |

</details>

<details><summary>Domain / sensor shift (35)</summary>

| Paper | Venue |
|---|---|
| [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414) | AAAI 2026 |
| [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) | IEEE TMI 2026 |
| [HERO: Hierarchical Embedding-Refinement for Open-Vocabulary Temporal Sentence Grounding in Videos](https://arxiv.org/abs/2603.06732) | arXiv ⚠️ |
| [Sa2VA: Marrying SAM2 with MLLM for Dense Grounded Understanding of Images and Videos](https://doi.org/10.1109/TPAMI.2026.3720379) | IEEE TPAMI 2026 |
| [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_SegCompass_Exploring_Interpretable_Alignment_with_Sparse_Autoencoders_for_Enhanced_Reasoning_CVPR_2026_paper.html) | CVPR 2026 |
| [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://doi.org/10.1109/CVPR52734.2025.02747) | CVPR 2025 |
| [Detect Any Sound: Open-Vocabulary Sound Event Detection with Multi-Modal Queries](https://doi.org/10.1145/3746027.3755574) | ACM MM 2025 |
| [Language-based Audio Moment Retrieval](https://doi.org/10.1109/icassp49660.2025.10890873) | ICASSP 2025 |
| [Moment of Untruth: Dealing with Negative Queries in Video Moment Retrieval](https://doi.org/10.1109/wacv61041.2025.00521) | WACV 2025 |
| [Seg-Zero: Reasoning-Chain Guided Segmentation via Cognitive Reinforcement](https://arxiv.org/abs/2503.06520) | arXiv ⚠️ |
| [SegLLM: Multi-round Reasoning Segmentation with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8e125fb53198f2143716d969584d0a28-Abstract-Conference.html) | ICLR 2025 |
| [The Devil is in the Spurious Correlations: Boosting Moment Retrieval with Dynamic Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_The_Devil_is_in_the_Spurious_Correlations_Boosting_Moment_Retrieval_ICCV_2025_paper.html) | ICCV 2025 |
| [Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://doi.org/10.52202/085713-2793) | NeurIPS 2025 |
| [VLM-R1: A Stable and Generalizable R1-style Large Vision-Language Model](https://arxiv.org/abs/2504.07615) | arXiv ⚠️ |
| [Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding](https://arxiv.org/abs/2408.16272) | arXiv ⚠️ |
| [One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0cf3e7eefb9d643e93e16ff1d94090a7-Abstract-Conference.html) | NeurIPS 2024 |
| [Prompting Segmentation with Sound Is Generalizable Audio-Visual Source Localizer](https://doi.org/10.1609/aaai.v38i6.28378) | AAAI 2024 |
| [R2-Bench: Benchmarking the Robustness of Referring Perception Models Under Perturbations](https://doi.org/10.1007/978-3-031-72673-6_12) | ECCV 2024 |
| [SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](https://doi.org/10.1007/978-3-031-72673-6_16) | ECCV 2024 |
| [Unveiling Parts Beyond Objects: Towards Finer-Granularity Referring Expression Segmentation](https://doi.org/10.1109/CVPR52733.2024.01235) | CVPR 2024 |
| [A Closer Look at Debiased Temporal Sentence Grounding in Videos: Dataset, Metric, and Approach](https://doi.org/10.1145/3565573) | ACM TOMM 2023 |
| [Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning](https://doi.org/10.1109/cvpr52729.2023.00621) | CVPR 2023 |
| [MomentDiff: Generative Video Moment Retrieval from Random to Real](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d01bda31bbcd780774ff15b534e03c40-Abstract-Conference.html) | NeurIPS 2023 |
| [PolyFormer: Referring Image Segmentation as Sequential Polygon Generation](https://doi.org/10.1109/CVPR52729.2023.01789) | CVPR 2023 |
| [SegGPT: Towards Segmenting Everything In Context](https://doi.org/10.1109/ICCV51070.2023.00110) | ICCV 2023 |
| [Segment Anything](https://doi.org/10.1109/ICCV51070.2023.00371) | ICCV 2023 |
| [UniVTG: Towards Unified Video-Language Temporal Grounding](https://doi.org/10.1109/iccv51070.2023.00262) | ICCV 2023 |
| [GRIT: General Robust Image Task Benchmark](https://arxiv.org/abs/2204.13653) | arXiv ⚠️ |
| [Grounded Language-Image Pre-training](https://doi.org/10.1109/CVPR52688.2022.01069) | CVPR 2022 |
| [Localizing Visual Sounds the Easy Way](https://doi.org/10.1007/978-3-031-19836-6_13) | ECCV 2022 |
| [ReCLIP: A Strong Zero-Shot Baseline for Referring Expression Comprehension](https://doi.org/10.18653/v1/2022.acl-long.357) | ACL 2022 |
| [A Closer Look at Temporal Sentence Grounding in Videos: Dataset and Metric](https://doi.org/10.1145/3475723.3484247) | ACM MM 2021 Workshop (W) |
| [URVOS: Unified Referring Video Object Segmentation Network with a Large-Scale Benchmark](https://doi.org/10.1007/978-3-030-58555-6_13) | ECCV 2020 |
| [Uncovering Hidden Challenges in Query-Based Video Moment Retrieval](https://doi.org/10.5244/c.34.84) | BMVC 2020 |
| [SUN-Spot: An RGB-D Dataset With Spatial Referring Expressions](https://doi.org/10.1109/iccvw.2019.00236) | ICCV Workshops 2019 (W) |

</details>

<details><summary>Missing modality (28)</summary>

| Paper | Venue |
|---|---|
| [ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark](https://arxiv.org/abs/2610.22964) | arXiv ⚠️ |
| [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/abs/2609.19991) | arXiv ⚠️ |
| [Both-or-Neither: Counterfactual Joint-Evidence Auditing for Reliable Audio-Visual Event Localization](https://doi.org/10.1145/3840475.3841438) | Proceedings of the 1st International Workshop on Joint Audio-Video Comprehension and Generation (W) |
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 |
| [Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding](https://doi.org/10.18653/2026.findings-emnlp.2423) | Findings of EMNLP 2026 |
| [MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_MVGGT_Multimodal_Visual_Geometry_Grounded_Transformer_for_Multiview_3D_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [RGBT-GroundBench: Visual Grounding Beyond RGB in Complex Real-World Scenarios](https://doi.org/10.1007/978-3-032-37422-6_24) | ECCV 2026 |
| [Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching](https://arxiv.org/abs/2608.04568) | arXiv ⚠️ |
| [Towards Unified Vision-Language Models with Incomplete Multi-Modal Inputs](https://doi.org/10.1609/aaai.v40i5.37387) | AAAI 2026 |
| [A Critical Assessment of Visual Sound Source Localization Models Including Negative Audio](https://doi.org/10.1109/ICASSP49660.2025.10890384) | ICASSP 2025 |
| [AVTrustBench: Assessing and Enhancing Reliability and Robustness in Audio-Visual LLMs](https://doi.org/10.1109/ICCV51701.2025.00156) | ICCV 2025 |
| [Audio Does Matter: Importance-Aware Multi-Granularity Fusion for Video Moment Retrieval](https://doi.org/10.1145/3746027.3754982) | ACM MM 2025 |
| [LongVALE: Vision-Audio-Language-Event Benchmark Towards Time-Aware Omni-Modal Perception of Long Videos](https://doi.org/10.1109/cvpr52734.2025.01766) | CVPR 2025 |
| [MissRAG: Addressing the Missing Modality Challenge in Multimodal Large Language Models](https://doi.org/10.1109/ICCV51701.2025.00308) | ICCV 2025 |
| [Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI models in Sound Localization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) | NeurIPS 2025 |
| [Unveiling Visual Biases in Audio-Visual Localization Benchmarks](https://doi.org/10.1007/978-3-031-93806-1_17) | ECCV 2024 Workshops (W) |
| [Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM](https://doi.org/10.52202/085713-4307) | NeurIPS 2025 |
| [CATR: Combinatorial-Dependence Audio-Queried Transformer for Audio-Visual Video Segmentation](https://doi.org/10.1145/3581783.3611724) | ACM MM 2023 |
| [Dense-Localizing Audio-Visual Events in Untrimmed Videos: A Large-Scale Benchmark and Baseline](https://doi.org/10.1109/cvpr52729.2023.02197) | CVPR 2023 |
| [MM-SHAP: A Performance-agnostic Metric for Measuring Multimodal Contributions in Vision and Language Models & Tasks](https://doi.org/10.18653/v1/2023.acl-long.223) | ACL 2023 |
| [Multimodal Prompting with Missing Modalities for Visual Recognition](https://doi.org/10.1109/CVPR52729.2023.01435) | CVPR 2023 |
| [A Closer Look at Weakly-Supervised Audio-Visual Source Localization](https://doi.org/10.52202/068431-2720) | NeurIPS 2022 |
| [Are Multimodal Transformers Robust to Missing Modality?](https://doi.org/10.1109/CVPR52688.2022.01764) | CVPR 2022 |
| [SMIL: Multimodal Learning with Severely Missing Modality](https://doi.org/10.1609/aaai.v35i3.16330) | AAAI 2021 |
| [Vision-and-Language or Vision-for-Language? On Cross-Modal Influence in Multimodal Transformers](https://doi.org/10.18653/v1/2021.emnlp-main.775) | EMNLP 2021 |
| [YouRefIt: Embodied Reference Understanding With Language and Gesture](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_YouRefIt_Embodied_Reference_Understanding_With_Language_and_Gesture_ICCV_2021_paper.html) | ICCV 2021 |
| [Audio-Visual Event Localization in Unconstrained Videos](https://doi.org/10.1007/978-3-030-01216-8_16) | ECCV 2018 |
| [Visual Referring Expression Recognition: What Do Systems Actually Learn?](https://doi.org/10.18653/v1/N18-2123) | NAACL-HLT 2018 |

</details>

<details><summary>Degraded / noisy input (20)</summary>

| Paper | Venue |
|---|---|
| [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/abs/2609.19991) | arXiv ⚠️ |
| [Affostruction: 3D Affordance Grounding with Generative Reconstruction](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Affostruction_3D_Affordance_Grounding_with_Generative_Reconstruction_CVPR_2026_paper.html) | CVPR 2026 |
| [Distinguishing semantically similar queries in temporal video grounding via LLM-generated query](https://doi.org/10.1007/s00530-025-02147-z) | Multimedia Systems 2026 |
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 |
| [HAMMER: Harnessing MLLMs via Cross-Modal Integration for Intention-Driven 3D Affordance Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_HAMMER_Harnessing_MLLMs_via_Cross-Modal_Integration_for_Intention-Driven_3D_Affordance_CVPR_2026_paper.html) | CVPR 2026 |
| [Knowledge-Preserved Model Tuning in Null-Space for Robust Spatio-Temporal Video Grounding](https://arxiv.org/abs/2606.03539) | arXiv ⚠️ |
| [LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html) | CVPR 2026 |
| [MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_MVGGT_Multimodal_Visual_Geometry_Grounded_Transformer_for_Multiview_3D_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [RGBT-GroundBench: Visual Grounding Beyond RGB in Complex Real-World Scenarios](https://doi.org/10.1007/978-3-032-37422-6_24) | ECCV 2026 |
| [Audio Does Matter: Importance-Aware Multi-Granularity Fusion for Video Moment Retrieval](https://doi.org/10.1145/3746027.3754982) | ACM MM 2025 |
| [GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_GEAL_Generalizable_3D_Affordance_Learning_with_Cross-Modal_Consistency_CVPR_2025_paper.html) | CVPR 2025 |
| [I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs](https://arxiv.org/abs/2506.14495) | arXiv ⚠️ |
| [On the Consistency of Video Large Language Models in Temporal Comprehension](https://openaccess.thecvf.com/content/CVPR2025/html/Jung_On_the_Consistency_of_Video_Large_Language_Models_in_Temporal_CVPR_2025_paper.html) | CVPR 2025 |
| [BAVS: Bootstrapping Audio-Visual Segmentation by Integrating Foundation Knowledge](https://doi.org/10.1109/tmm.2024.3405622) | IEEE TMM 2024 |
| [Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding](https://arxiv.org/abs/2408.16272) | arXiv ⚠️ |
| [R2-Bench: Benchmarking the Robustness of Referring Perception Models Under Perturbations](https://doi.org/10.1007/978-3-031-72673-6_12) | ECCV 2024 |
| [GRIT: General Robust Image Task Benchmark](https://arxiv.org/abs/2204.13653) | arXiv ⚠️ |
| [Robustness Analysis of Video-Language Models Against Visual and Language Perturbations](https://doi.org/10.52202/068431-2493) | NeurIPS 2022 Datasets and Benchmarks |
| [Refer-it-in-RGBD: A Bottom-up Approach for 3D Visual Grounding in RGBD Images](https://doi.org/10.1109/CVPR46437.2021.00597) | CVPR 2021 |
| [Visual Referring Expression Recognition: What Do Systems Actually Learn?](https://doi.org/10.18653/v1/N18-2123) | NAACL-HLT 2018 |

</details>

<details><summary>Conflicting modalities (16)</summary>

| Paper | Venue |
|---|---|
| [AVID: A Benchmark for Omni-Modal Audio-Visual Inconsistency Understanding via Agent-Driven Construction](https://arxiv.org/abs/2604.13593) | arXiv ⚠️ |
| [Both-or-Neither: Counterfactual Joint-Evidence Auditing for Reliable Audio-Visual Event Localization](https://doi.org/10.1145/3840475.3841438) | Proceedings of the 1st International Workshop on Joint Audio-Video Comprehension and Generation (W) |
| [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html) | ICML 2026 |
| [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3cc685788a311fa35d8d41df93e288ca-Abstract-Conference.html) | ICLR 2025 |
| [AVTrustBench: Assessing and Enhancing Reliability and Robustness in Audio-Visual LLMs](https://doi.org/10.1109/ICCV51701.2025.00156) | ICCV 2025 |
| [Robust Multimodal Large Language Models Against Modality Conflict](https://proceedings.mlr.press/v267/zhang25dq.html) | ICML 2025 |
| [Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI models in Sound Localization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) | NeurIPS 2025 |
| [Seeing Speech and Sound: Distinguishing and Locating Audio Sources in Visual Scenes](https://doi.org/10.1109/cvpr52734.2025.01264) | CVPR 2025 |
| [Words or Vision: Do Vision-Language Models Have Blind Faith in Text?](https://doi.org/10.1109/CVPR52734.2025.00366) | CVPR 2025 |
| [BAVS: Bootstrapping Audio-Visual Segmentation by Integrating Foundation Knowledge](https://doi.org/10.1109/tmm.2024.3405622) | IEEE TMM 2024 |
| [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.01363) | CVPR 2024 |
| [MEERKAT: Audio-Visual Large Language Model for Grounding in Space and Time](https://doi.org/10.1007/978-3-031-73039-9_4) | ECCV 2024 |
| [Unveiling Typographic Deceptions: Insights of the Typographic Vulnerability in Large Vision-Language Models](https://doi.org/10.1007/978-3-031-73202-7_11) | ECCV 2024 |
| [Unveiling and Mitigating Bias in Audio Visual Segmentation](https://doi.org/10.1145/3664647.3680802) | ACM MM 2024 |
| [Unified Multisensory Perception: Weakly-Supervised Audio-Visual Video Parsing](https://doi.org/10.1007/978-3-030-58580-8_26) | ECCV 2020 |
| [Objects that Sound](https://doi.org/10.1007/978-3-030-01246-5_27) | ECCV 2018 |

</details>

<details><summary>Long-horizon drift (12)</summary>

| Paper | Venue |
|---|---|
| [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265) | CVPR 2025 |
| [LongVALE: Vision-Audio-Language-Event Benchmark Towards Time-Aware Omni-Modal Perception of Long Videos](https://doi.org/10.1109/cvpr52734.2025.01766) | CVPR 2025 |
| [SAM 2: Segment Anything in Images and Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | ICLR 2025 |
| [SAMWISE: Infusing Wisdom in SAM2 for Text-Driven Video Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Cuttano_SAMWISE_Infusing_Wisdom_in_SAM2_for_Text-Driven_Video_Segmentation_CVPR_2025_paper.html) | CVPR 2025 |
| [SegLLM: Multi-round Reasoning Segmentation with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8e125fb53198f2143716d969584d0a28-Abstract-Conference.html) | ICLR 2025 |
| [ViLLa: Video Reasoning Segmentation with Large Language Model](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_ViLLa_Video_Reasoning_Segmentation_with_Large_Language_Model_ICCV_2025_paper.html) | ICCV 2025 |
| [When Thinking Drifts: Evidential Grounding for Robust Video Reasoning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/788f0d336eeddf698c8d527b1794fca4-Abstract-Conference.html) | NeurIPS 2025 |
| [SnAG: Scalable and Accurate Video Grounding](https://openaccess.thecvf.com/content/CVPR2024/html/Mu_SnAG_Scalable_and_Accurate_Video_Grounding_CVPR_2024_paper.html) | CVPR 2024 |
| [TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding](https://doi.org/10.1109/cvpr52733.2024.01357) | CVPR 2024 |
| [OnlineRefer: A Simple Online Baseline for Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_OnlineRefer_A_Simple_Online_Baseline_for_Referring_Video_Object_Segmentation_ICCV_2023_paper.html) | ICCV 2023 |
| [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://doi.org/10.1109/cvpr52688.2022.01842) | CVPR 2022 |
| [URVOS: Unified Referring Video Object Segmentation Network with a Large-Scale Benchmark](https://doi.org/10.1007/978-3-030-58555-6_13) | ECCV 2020 |

</details>

<details><summary>Adversarial / backdoor (11)</summary>

| Paper | Venue |
|---|---|
| [IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Li_IAG_Input-aware_Backdoor_Attack_on_VLM-based_Visual_Grounding_CVPR_2026_paper.html) | CVPR 2026 |
| [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html) | ICML 2026 |
| [AVTrustBench: Assessing and Enhancing Reliability and Robustness in Audio-Visual LLMs](https://doi.org/10.1109/ICCV51701.2025.00156) | ICCV 2025 |
| [Manipulating the Bounding Box: Multimodal Controlled Backdoor Attacks on 3D Visual Grounding Models](https://doi.org/10.1109/IJCNN64981.2025.11229253) | IJCNN 2025 |
| [Seeing is Not Believing: Adversarial Natural Object Optimization for Hard-Label 3D Scene Attacks](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Seeing_is_Not_Believing_Adversarial_Natural_Object_Optimization_for_Hard-Label_CVPR_2025_paper.html) | CVPR 2025 |
| [Adversarial Robustness for Visual Grounding of Multimodal Large Language Models](https://arxiv.org/abs/2405.09981) | ICLR 2024 Workshop on Reliable and Responsible Foundation Models (W) |
| [Unveiling Typographic Deceptions: Insights of the Typographic Vulnerability in Large Vision-Language Models](https://doi.org/10.1007/978-3-031-73202-7_11) | ECCV 2024 |
| [Can Audio-Visual Integration Strengthen Robustness Under Multimodal Attacks?](https://openaccess.thecvf.com/content/CVPR2021/html/Tian_Can_Audio-Visual_Integration_Strengthen_Robustness_Under_Multimodal_Attacks_CVPR_2021_paper.html) | CVPR 2021 |
| [SNEAK: Synonymous Sentences-Aware Adversarial Attack on Natural Language Video Localization](https://arxiv.org/abs/2112.04154) | arXiv ⚠️ |
| [Words Aren't Enough, Their Order Matters: On the Robustness of Grounding Visual Referring Expressions](https://doi.org/10.18653/v1/2020.acl-main.586) | ACL 2020 |
| [Fooling Vision and Language Models Despite Localization and Attention Mechanism](https://doi.org/10.1109/CVPR.2018.00520) | CVPR 2018 |

</details>

<a id="verification-mechanisms"></a>

## ✔️ Verification mechanisms

Mechanisms coded in facet H: output checks (existence or abstention heads, self-verification, external verifiers, consistency checks), uncertainty estimates, traceable evidence and interactive clarification. **213 of 284 method papers have no coded facet-H mechanism.** This is not a count of papers without output verification: facet H also covers evidence exposure and uncertainty estimation, and a non-empty code does not by itself establish that an output is checked (16 of the remaining 71 have only the traceable-evidence label). Codes are AI-assisted; see the survey for the coding audit.

| Mechanism | Works |
|---|:---:|
| Existence / abstention head | 30 |
| Traceable evidence | 30 |
| Confidence / uncertainty estimate | 21 |
| Self-verification / re-grounding | 10 |
| Temporal / cross-view consistency | 6 |
| Cycle / REG consistency | 8 |
| Interactive clarification | 7 |
| External verifier | 5 |

<details><summary>Existence / abstention head (30)</summary>

| Paper | Venue |
|---|---|
| [Do Audio-Visual Segmentation Models Truly Segment Sounding Objects?](https://doi.org/10.1609/aaai.v40i8.37542) | AAAI 2026 |
| [GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation](https://doi.org/10.1007/s11263-026-02729-y) | IJCV 2026 |
| [Generalized Medical Phrase Grounding](https://doi.org/10.1109/tmi.2026.3707568) | IEEE TMI 2026 |
| [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Learning_to_Refuse_Refusal-Aware_Reinforcement_Fine-Tuning_for_Hard-Irrelevant_Queries_in_CVPR_2026_paper.html) | CVPR 2026 |
| [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440) | arXiv ⚠️ |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 |
| [SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419) | ICLR 2026 Workshop (W) |
| [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](https://arxiv.org/abs/2608.04698) | arXiv ⚠️ |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination](https://arxiv.org/abs/2506.21546) | arXiv ⚠️ |
| [DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy](https://doi.org/10.1109/ICCV51701.2025.01854) | ICCV 2025 |
| [Hierarchical Alignment-enhanced Adaptive Grounding Network for Generalized Referring Expression Comprehension](https://doi.org/10.1609/aaai.v39i8.32867) | AAAI 2025 |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://doi.org/10.1109/tpami.2025.3600507) | IEEE TPAMI 2025 |
| [Moment of Untruth: Dealing with Negative Queries in Video Moment Retrieval](https://doi.org/10.1109/wacv61041.2025.00521) | WACV 2025 |
| [SAM 2: Segment Anything in Images and Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | ICLR 2025 |
| [Zero-Shot Referring Expression Comprehension via Vison-Language True/False Verification](https://arxiv.org/abs/2509.09958) | arXiv ⚠️ |
| [3D-GRES: Generalized 3D Referring Expression Segmentation](https://doi.org/10.1145/3664647.3680841) | ACM MM 2024 |
| [Described Spatial-Temporal Video Detection](https://arxiv.org/abs/2407.05610) | arXiv ⚠️ |
| [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | ICLR 2024 |
| [GSVA: Generalized Segmentation via Multimodal Large Language Models](https://doi.org/10.1109/CVPR52733.2024.00370) | CVPR 2024 |
| [See Say and Segment: Teaching LMMs to Overcome False Premises](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_See_Say_and_Segment_Teaching_LMMs_to_Overcome_False_Premises_CVPR_2024_paper.html) | CVPR 2024 |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 |
| [GRES: Generalized Referring Expression Segmentation](https://doi.org/10.1109/CVPR52729.2023.02259) | CVPR 2023 |
| [Multi3DRefer: Grounding Text Description to Multiple 3D Objects](https://doi.org/10.1109/ICCV51070.2023.01397) | ICCV 2023 |
| [RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D](https://doi.org/10.1109/iccv51070.2023.01396) | ICCV 2023 |
| [Robust Referring Video Object Segmentation with Cyclic Structural Consensus](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Robust_Referring_Video_Object_Segmentation_with_Cyclic_Structural_Consensus_ICCV_2023_paper.html) | ICCV 2023 |
| [A Closer Look at Weakly-Supervised Audio-Visual Source Localization](https://doi.org/10.52202/068431-2720) | NeurIPS 2022 |
| [Reliable Visual Question Answering: Abstain Rather Than Answer Incorrectly](https://doi.org/10.1007/978-3-031-20059-5_9) | ECCV 2022 |
| [Objects that Sound](https://doi.org/10.1007/978-3-030-01246-5_27) | ECCV 2018 |

</details>

<details><summary>Traceable evidence (30)</summary>

| Paper | Venue |
|---|---|
| [ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark](https://arxiv.org/abs/2610.22964) | arXiv ⚠️ |
| [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cdb347d7516d52a9280ea9d6708911f6-Abstract-Conference.html) | ICLR 2026 |
| [EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning](https://arxiv.org/abs/2610.28444) | arXiv ⚠️ |
| [Grounded Chain-of-Thought for Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Grounded_Chain-of-Thought_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html) | CVPR 2026 |
| [Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence](https://proceedings.mlr.press/v306/meng26e.html) | ICML 2026 |
| [Rex-Thinker: Grounded Object Referring via Chain-of-Thought Reasoning](https://iclr.cc/virtual/2026/poster/10008562) | ICLR 2026 |
| [SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes](https://proceedings.iclr.cc/paper_files/paper/2026/hash/05a3d6c357b596f8ea463e1ccfd441d6-Abstract-Conference.html) | ICLR 2026 |
| [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_SegCompass_Exploring_Interpretable_Alignment_with_Sparse_Autoencoders_for_Enhanced_Reasoning_CVPR_2026_paper.html) | CVPR 2026 |
| [Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Method](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f09ab24aa37ae2664b3d923cdb0319b5-Abstract-Conference.html) | ICLR 2026 |
| [V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning](https://openaccess.thecvf.com/content/CVPR2026F/html/Cheng_V-STaR_Benchmarking_Video-LLMs_on_Video_Spatio-Temporal_Reasoning_CVPRF_2026_paper.html) | CVPR 2026 Findings |
| [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](https://arxiv.org/abs/2609.17248) | arXiv ⚠️ |
| [VideoZeroBench: Probing the Limits of Video MLLMs with Spatio-Temporal Evidence Verification](https://arxiv.org/abs/2604.01569) | arXiv ⚠️ |
| [What You Ask is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA](https://arxiv.org/abs/2608.15708) | arXiv ⚠️ |
| [CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/70fa5df8e3300dc30bf19bee44a56155-Abstract-Conference.html) | ICLR 2025 |
| [Crab: A Unified Audio-Visual Scene Understanding Model with Explicit Cooperation](https://doi.org/10.1109/cvpr52734.2025.01752) | CVPR 2025 |
| [Reasoning to Attend: Try to Understand How <SEG> Token Works](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_Reasoning_to_Attend_Try_to_Understand_How_SEG_Token_Works_CVPR_2025_paper.html) | CVPR 2025 |
| [Towards Omnimodal Expressions and Reasoning in Referring Audio-Visual Segmentation](https://doi.org/10.1109/iccv51701.2025.02096) | ICCV 2025 |
| [When Thinking Drifts: Evidential Grounding for Robust Video Reasoning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/788f0d336eeddf698c8d527b1794fca4-Abstract-Conference.html) | NeurIPS 2025 |
| [Can I Trust Your Answer? Visually Grounded Video Question Answering](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Can_I_Trust_Your_Answer_Visually_Grounded_Video_Question_Answering_CVPR_2024_paper.html) | CVPR 2024 |
| [GROUNDHOG: Grounding Large Language Models to Holistic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_GROUNDHOG_Grounding_Large_Language_Models_to_Holistic_Segmentation_CVPR_2024_paper.html) | CVPR 2024 |
| [Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](https://doi.org/10.1007/978-3-031-72658-3_24) | ECCV 2024 |
| [LLM-Grounder: Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://doi.org/10.1109/ICRA57147.2024.10610443) | ICRA 2024 |
| [MAIRA-2: Grounded Radiology Report Generation](https://arxiv.org/abs/2406.04449) | arXiv ⚠️ |
| [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://doi.org/10.52202/079017-0900) | NeurIPS 2024 |
| [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_V_Guided_Visual_Search_as_a_Core_Mechanism_in_Multimodal_CVPR_2024_paper.html) | CVPR 2024 |
| [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0ff38d72a2e0aa6dbe42de83a17b2223-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks |
| [Toward Explainable 3D Grounded Visual Question Answering: A New Benchmark and Strong Baseline](https://doi.org/10.1109/TCSVT.2022.3229081) | IEEE TCSVT 2023 |
| [ScanQA: 3D Question Answering for Spatial Scene Understanding](https://openaccess.thecvf.com/content/CVPR2022/html/Azuma_ScanQA_3D_Question_Answering_for_Spatial_Scene_Understanding_CVPR_2022_paper.html) | CVPR 2022 |
| [Graph-Structured Referring Expression Reasoning in the Wild](https://doi.org/10.1109/CVPR42600.2020.00997) | CVPR 2020 |
| [CLEVR-Ref+: Diagnosing Visual Reasoning With Referring Expressions](https://doi.org/10.1109/CVPR.2019.00431) | CVPR 2019 |

</details>

<details><summary>Confidence / uncertainty estimate (21)</summary>

| Paper | Venue |
|---|---|
| [Adaptive Evidential Learning for Temporal-Semantic Robustness in Moment Retrieval](https://doi.org/10.1609/aaai.v40i7.37414) | AAAI 2026 |
| [Agreement versus Softmax under Spatial Disambiguation](https://arxiv.org/abs/2610.14210) | arXiv ⚠️ |
| [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](https://arxiv.org/abs/2607.10993) | arXiv ⚠️ |
| [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434) | arXiv ⚠️ |
| [Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence](https://proceedings.mlr.press/v306/meng26e.html) | ICML 2026 |
| [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440) | arXiv ⚠️ |
| [SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419) | ICLR 2026 Workshop (W) |
| [Surrogate Uncertainty for Black-box Visual Grounding](https://arxiv.org/abs/2610.39798) | arXiv ⚠️ |
| [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978) | arXiv ⚠️ |
| [Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines](https://arxiv.org/abs/2604.15376) | arXiv ⚠️ |
| [AVTrustBench: Assessing and Enhancing Reliability and Robustness in Audio-Visual LLMs](https://doi.org/10.1109/ICCV51701.2025.00156) | ICCV 2025 |
| [Calibrating Uncertainty Quantification of Multi-Modal LLMs using Grounding](https://arxiv.org/abs/2505.03788) | arXiv ⚠️ |
| [Enhancing Trustworthy GUI Grounding via Self-Critiqued Reinforcement Learning](https://arxiv.org/abs/2510.27266) | arXiv ⚠️ |
| [Uncertainty-Aware Medical Diagnostic Phrase Identification and Grounding](https://doi.org/10.1109/tpami.2025.3596878) | IEEE TPAMI 2025 |
| [Beyond Uncertainty: Evidential Deep Learning for Robust Video Temporal Grounding](https://arxiv.org/abs/2408.16272) | arXiv ⚠️ |
| [iKUN: Speak to Trackers without Retraining](https://openaccess.thecvf.com/content/CVPR2024/html/Du_iKUN_Speak_to_Trackers_without_Retraining_CVPR_2024_paper.html) | CVPR 2024 |
| [Described Object Detection: Liberating Object Detection with Flexible Expressions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | NeurIPS 2023 |
| [Segment Anything](https://doi.org/10.1109/ICCV51070.2023.00371) | ICCV 2023 |
| [GRIT: General Robust Image Task Benchmark](https://arxiv.org/abs/2204.13653) | arXiv ⚠️ |
| [Reliable Visual Question Answering: Abstain Rather Than Answer Incorrectly](https://doi.org/10.1007/978-3-031-20059-5_9) | ECCV 2022 |
| [Giving Commands to a Self-Driving Car: How to Deal with Uncertain Situations?](https://doi.org/10.1016/j.engappai.2021.104257) | Engineering Applications of Artificial Intelligence 2021 |

</details>

<details><summary>Self-verification / re-grounding (10)</summary>

| Paper | Venue |
|---|---|
| [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cdb347d7516d52a9280ea9d6708911f6-Abstract-Conference.html) | ICLR 2026 |
| [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458) | arXiv ⚠️ |
| [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://proceedings.mlr.press/v306/zhao26am.html) | ICML 2026 |
| [SAM 3: Segment Anything with Concepts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | ICLR 2026 |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [On the Consistency of Video Large Language Models in Temporal Comprehension](https://openaccess.thecvf.com/content/CVPR2025/html/Jung_On_the_Consistency_of_Video_Large_Language_Models_in_Temporal_CVPR_2025_paper.html) | CVPR 2025 |
| [POPEN: Preference-Based Optimization and Ensemble for LVLM-Based Reasoning Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_POPEN_Preference-Based_Optimization_and_Ensemble_for_LVLM-Based_Reasoning_Segmentation_CVPR_2025_paper.html) | CVPR 2025 |
| [SAM4MLLM: Enhance Multi-Modal Large Language Model for Referring Expression Segmentation](https://doi.org/10.1007/978-3-031-73004-7_19) | ECCV 2024 |
| [ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities](https://doi.org/10.1007/978-3-031-73242-3_9) | ECCV 2024 |
| [VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding](https://proceedings.mlr.press/v270/xu25c.html) | CoRL 2024 |

</details>

<details><summary>Temporal / cross-view consistency (6)</summary>

| Paper | Venue |
|---|---|
| [Audio-Visual Instance Segmentation](https://doi.org/10.1109/cvpr52734.2025.01265) | CVPR 2025 |
| [On the Consistency of Video Large Language Models in Temporal Comprehension](https://openaccess.thecvf.com/content/CVPR2025/html/Jung_On_the_Consistency_of_Video_Large_Language_Models_in_Temporal_CVPR_2025_paper.html) | CVPR 2025 |
| [SAMWISE: Infusing Wisdom in SAM2 for Text-Driven Video Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Cuttano_SAMWISE_Infusing_Wisdom_in_SAM2_for_Text-Driven_Video_Segmentation_CVPR_2025_paper.html) | CVPR 2025 |
| [Four Ways to Improve Verbo-visual Fusion for Dense 3D Visual Grounding](https://doi.org/10.1007/978-3-031-73116-7_12) | ECCV 2024 |
| [VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding](https://proceedings.mlr.press/v270/xu25c.html) | CoRL 2024 |
| [OnlineRefer: A Simple Online Baseline for Referring Video Object Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_OnlineRefer_A_Simple_Online_Baseline_for_Referring_Video_Object_Segmentation_ICCV_2023_paper.html) | ICCV 2023 |

</details>

<details><summary>Cycle / REG consistency (8)</summary>

| Paper | Venue |
|---|---|
| [Grounded Chain-of-Thought for Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Grounded_Chain-of-Thought_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html) | CVPR 2026 |
| [Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines](https://arxiv.org/abs/2604.15376) | arXiv ⚠️ |
| [Matcher: Segment Anything with One Shot Using All-Purpose Feature Matching](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4df9a5e6bad9e64ebcea453e031142bb-Abstract-Conference.html) | ICLR 2024 |
| [Beyond One-to-One: Rethinking the Referring Image Segmentation](https://doi.org/10.1109/ICCV51070.2023.00376) | ICCV 2023 |
| [Robust Referring Video Object Segmentation with Cyclic Structural Consensus](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Robust_Referring_Video_Object_Segmentation_with_Cyclic_Structural_Consensus_ICCV_2023_paper.html) | ICCV 2023 |
| [D3Net: A Unified Speaker-Listener Architecture for 3D Dense Captioning and Visual Grounding](https://doi.org/10.1007/978-3-031-19824-3_29) | ECCV 2022 |
| [Exploiting Transformation Invariance and Equivariance for Self-supervised Sound Localisation](https://doi.org/10.1145/3503161.3548317) | ACM MM 2022 |
| [Generation and Comprehension of Unambiguous Object Descriptions](https://doi.org/10.1109/CVPR.2016.9) | CVPR 2016 |

</details>

<details><summary>Interactive clarification (7)</summary>

| Paper | Venue |
|---|---|
| [CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion](https://arxiv.org/abs/2602.08999) | arXiv ⚠️ |
| [Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Learning_to_Refuse_Refusal-Aware_Reinforcement_Fine-Tuning_for_Hard-Irrelevant_Queries_in_CVPR_2026_paper.html) | CVPR 2026 |
| [Surrogate Uncertainty for Black-box Visual Grounding](https://arxiv.org/abs/2610.39798) | arXiv ⚠️ |
| [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978) | arXiv ⚠️ |
| [See Say and Segment: Teaching LMMs to Overcome False Premises](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_See_Say_and_Segment_Teaching_LMMs_to_Overcome_False_Premises_CVPR_2024_paper.html) | CVPR 2024 |
| [Segment Everything Everywhere All at Once](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html) | NeurIPS 2023 |
| [Giving Commands to a Self-Driving Car: How to Deal with Uncertain Situations?](https://doi.org/10.1016/j.engappai.2021.104257) | Engineering Applications of Artificial Intelligence 2021 |

</details>

<details><summary>External verifier (5)</summary>

| Paper | Venue |
|---|---|
| [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458) | arXiv ⚠️ |
| [VIRO: Robust and Efficient Neuro-Symbolic Reasoning with Verification for Referring Expression Comprehension](https://openaccess.thecvf.com/content/CVPR2026/html/Park_VIRO_Robust_and_Efficient_Neuro-Symbolic_Reasoning_with_Verification_for_Referring_CVPR_2026_paper.html) | CVPR 2026 |
| [Calibrating Uncertainty Quantification of Multi-Modal LLMs using Grounding](https://arxiv.org/abs/2505.03788) | arXiv ⚠️ |
| [Zero-Shot Referring Expression Comprehension via Vison-Language True/False Verification](https://arxiv.org/abs/2509.09958) | arXiv ⚠️ |
| [BAVS: Bootstrapping Audio-Visual Segmentation by Integrating Foundation Knowledge](https://doi.org/10.1109/tmm.2024.3405622) | IEEE TMM 2024 |

</details>

<a id="benchmarks"></a>

## 🧪 Benchmarks

Evaluation benchmarks with a localisation output and the reliability conditions they build in.

| Benchmark | Family | Output | Conditions tested |
|---|---|---|---|
| [ReferItGame](https://doi.org/10.3115/v1/D14-1086) | Image | box, mask | Ambiguity & distractors |
| [RefCOCO, RefCOCO+](https://doi.org/10.1007/978-3-319-46475-6_5) | Image | box | Ambiguity & distractors |
| [Flickr30k Entities](https://doi.org/10.1007/s11263-016-0965-7) | Image | box | Multiple targets |
| [CLEVR-Ref+](https://doi.org/10.1109/CVPR.2019.00431) | Image | box, mask | Ambiguity & distractors, Novel categories |
| [Cops-Ref](https://doi.org/10.1109/CVPR42600.2020.01010) | Image | box | Ambiguity & distractors, Novel categories |
| [YouRefIt](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_YouRefIt_Embodied_Reference_Understanding_With_Language_and_Gesture_ICCV_2021_paper.html) | Image | box | Ambiguity & distractors, Missing modality |
| [GRIT](https://arxiv.org/abs/2204.13653) ⚠️ | Image | box, mask | Novel categories, Domain / sensor shift, Degraded / noisy input |
| [gRefCOCO](https://doi.org/10.1109/CVPR52729.2023.02259) | Image | mask | Absent target / false premise, Multiple targets |
| [Ref-ZOM](https://doi.org/10.1109/ICCV51070.2023.00376) | Image | mask | Absent target / false premise, Multiple targets |
| [D³](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) | Image | box | Absent target / false premise, Multiple targets, Novel categories |
| [ReasonSeg](https://doi.org/10.1109/CVPR52733.2024.00915) | Image | mask | — |
| [PerSeg](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4f44e5c82dc7b0ba4472083e5dedb08e-Abstract-Conference.html) | Image | mask | Ambiguity & distractors, Novel categories |
| [R²-Bench](https://doi.org/10.1007/978-3-031-72673-6_12) | Image | mask | Domain / sensor shift, Degraded / noisy input |
| [Ref-L4](https://doi.org/10.1109/CVPRW67362.2025.00056) | Image | box | Ambiguity & distractors, Novel categories |
| [HalluSegBench](https://arxiv.org/abs/2506.21546) ⚠️ | Image | mask | Absent target / false premise, Ambiguity & distractors |
| [GUI-HalluBench](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html) | Image | box, map | Absent target / false premise, Ambiguity & distractors |
| [MM-GCoT](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Grounded_Chain-of-Thought_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html) | Image | box | — |
| [Charades-STA](https://doi.org/10.1109/iccv.2017.563) | Video | interval | Novel categories |
| [DiDeMo](https://doi.org/10.1109/iccv.2017.618) | Video | interval | — |
| [QVHighlights](https://proceedings.neurips.cc/paper_files/paper/2021/hash/62e0973455fd26eb03e91d5741a4a3bb-Abstract.html) | Video | interval | Multiple targets |
| [Ego4D NLQ](https://doi.org/10.1109/cvpr52688.2022.01842) | Video | interval | Long-horizon drift |
| [Charades-CD](https://doi.org/10.1145/3565573) | Video | interval | Ambiguity & distractors, Domain / sensor shift |
| [Charades-STA negatives](https://doi.org/10.1109/wacv61041.2025.00521) | Video | interval | Absent target / false premise, Domain / sensor shift |
| [NExT-GQA](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Can_I_Trust_Your_Answer_Visually_Grounded_Video_Question_Answering_CVPR_2024_paper.html) | Video | interval | — |
| [ReXTime](https://doi.org/10.52202/079017-0900) | Video | interval | — |
| [CG-Bench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/70fa5df8e3300dc30bf19bee44a56155-Abstract-Conference.html) | Video | interval | — |
| [V-STaR](https://openaccess.thecvf.com/content/CVPR2026F/html/Cheng_V-STaR_Benchmarking_Video-LLMs_on_Video_Spatio-Temporal_Reasoning_CVPRF_2026_paper.html) | Video | box, interval | — |
| [VideoZeroBench](https://arxiv.org/abs/2604.01569) ⚠️ | Video | box, interval | — |
| [Dang et al. (2026)](https://doi.org/10.1007/s00530-025-02147-z) | Video | interval | Absent target / false premise, Ambiguity & distractors, Degraded / noisy input |
| [VidSTG](https://doi.org/10.1109/cvpr42600.2020.01068) | Video | tube/track | Ambiguity & distractors |
| [HC-STVG](https://doi.org/10.1109/tcsvt.2021.3085907) | Video | tube/track | Ambiguity & distractors |
| [A2D Sentences](https://doi.org/10.1109/cvpr.2018.00624) | Video | mask | — |
| [Refer-YouTube-VOS](https://doi.org/10.1007/978-3-030-58555-6_13) | Video | mask | Domain / sensor shift, Long-horizon drift |
| [MeViS](https://doi.org/10.1109/iccv51070.2023.00254) | Video | mask | Ambiguity & distractors, Multiple targets |
| [MeViSv2](https://doi.org/10.1109/tpami.2025.3600507) | Video | mask, tube/track | Absent target / false premise, Ambiguity & distractors, Multiple targets |
| [ReVOS](https://doi.org/10.1007/978-3-031-72633-0_6) | Video | mask | Absent target / false premise, Multiple targets |
| [R²-VOS negatives](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Robust_Referring_Video_Object_Segmentation_with_Cyclic_Structural_Consensus_ICCV_2023_paper.html) | Video | mask | Absent target / false premise |
| [RefEgo](https://doi.org/10.1109/iccv51070.2023.01396) | Video | box, tube/track | Absent target / false premise, Ambiguity & distractors |
| [Refer-KITTI](https://doi.org/10.1109/cvpr52729.2023.01406) | Video | box, tube/track | Multiple targets |
| [DVD-ST](https://arxiv.org/abs/2407.05610) ⚠️ | Video | box, tube/track | Absent target / false premise, Multiple targets |
| [VGG-SS](https://doi.org/10.1109/cvpr46437.2021.01659) | Audio and audio-visual | map | Novel categories |
| [Ext. Flickr/VGG-SS](https://doi.org/10.52202/068431-2720) | Audio and audio-visual | map | Absent target / false premise, Novel categories, Missing modality |
| [AVSBench-object](https://doi.org/10.1007/978-3-031-19836-6_22) | Audio and audio-visual | mask | Multiple targets |
| [AVSBench-semantic](https://doi.org/10.1007/s11263-024-02261-x) | Audio and audio-visual | mask | Multiple targets |
| [AVSBench-Robust](https://doi.org/10.1609/aaai.v40i8.37542) | Audio and audio-visual | mask | Absent target / false premise, Multiple targets, Missing modality, Degraded / noisy input |
| [Ref-AVS](https://doi.org/10.1007/978-3-031-72904-1_12) | Audio and audio-visual | mask | Absent target / false premise, Multiple targets, Novel categories |
| [OmniAVS](https://doi.org/10.1109/iccv51701.2025.02096) | Audio and audio-visual | mask | Absent target / false premise, Multiple targets, Novel categories |
| [AVE](https://doi.org/10.1007/978-3-030-01216-8_16) | Audio and audio-visual | interval | Missing modality |
| [UnAV-100](https://doi.org/10.1109/cvpr52729.2023.02197) | Audio and audio-visual | interval | Multiple targets, Missing modality |
| [LongVALE](https://doi.org/10.1109/cvpr52734.2025.01766) | Audio and audio-visual | interval | Missing modality, Long-horizon drift |
| [AVATAR](https://openaccess.thecvf.com/content/ICCV2025/html/Choi_Whats_Making_That_Sound_Right_Now_Video-centric_Audio-Visual_Localization_ICCV_2025_paper.html) | Audio and audio-visual | map | Absent target / false premise, Ambiguity & distractors, Multiple targets |
| [EvaOmni](https://arxiv.org/abs/2610.28444) ⚠️ | Audio and audio-visual | interval | — |
| [Video-HolmesV2](https://arxiv.org/abs/2609.17248) ⚠️ | Audio and audio-visual | box, interval | — |
| [ANCHOR](https://arxiv.org/abs/2610.22964) ⚠️ | Audio and audio-visual | box, interval | Missing modality |
| [AVTrace](https://arxiv.org/abs/2609.19991) ⚠️ | Audio and audio-visual | interval | Missing modality, Degraded / noisy input |
| [AVID](https://arxiv.org/abs/2604.13593) ⚠️ | Audio and audio-visual | interval | Conflicting modalities |
| [AudioGrounding](https://doi.org/10.1109/icassp39728.2021.9414834) | Audio and audio-visual | interval | — |
| [Clotho-Moment](https://doi.org/10.1109/icassp49660.2025.10890873) | Audio and audio-visual | interval | Domain / sensor shift |
| [ScanRefer](https://doi.org/10.1007/978-3-030-58565-5_13) | 3D, other sensors and domains | 3D box | Ambiguity & distractors |
| [Nr3D, Sr3D](https://doi.org/10.1007/978-3-030-58452-8_25) | 3D, other sensors and domains | 3D mask | Ambiguity & distractors |
| [SUNRefer](https://doi.org/10.1109/CVPR46437.2021.00597) | 3D, other sensors and domains | 3D box, map | Degraded / noisy input |
| [SUN-Spot](https://doi.org/10.1109/iccvw.2019.00236) | 3D, other sensors and domains | box | Ambiguity & distractors, Domain / sensor shift |
| [Multi3DRefer](https://doi.org/10.1109/ICCV51070.2023.01397) | 3D, other sensors and domains | 3D box | Absent target / false premise, Ambiguity & distractors, Multiple targets |
| [Multi3DRes](https://doi.org/10.1145/3664647.3680841) | 3D, other sensors and domains | 3D mask | Absent target / false premise, Ambiguity & distractors, Multiple targets |
| [EmbodiedScan](https://doi.org/10.1109/CVPR52733.2024.01868) | 3D, other sensors and domains | 3D box | Ambiguity & distractors |
| [ScanReason](https://doi.org/10.1007/978-3-031-73242-3_9) | 3D, other sensors and domains | 3D box | — |
| [Beacon3D](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Unveiling_the_Mist_over_3D_Vision-Language_Understanding_Object-centric_Evaluation_with_CVPR_2025_paper.html) | 3D, other sensors and domains | 3D box | Ambiguity & distractors |
| [ViGiL3D](https://doi.org/10.18653/v1/2025.acl-long.1470) | 3D, other sensors and domains | 3D box | Ambiguity & distractors, Novel categories |
| [FE-3DGQA](https://doi.org/10.1109/TCSVT.2022.3229081) | 3D, other sensors and domains | 3D box | — |
| [3D-GRAND](https://doi.org/10.1109/CVPR52734.2025.02747) | 3D, other sensors and domains | 3D box | Absent target / false premise, Domain / sensor shift |
| [Ref-LERF](https://proceedings.mlr.press/v267/he25h.html) | 3D, other sensors and domains | 3D mask, mask | Ambiguity & distractors |
| [CityRefer](https://doi.org/10.52202/075280-3397) | 3D, other sensors and domains | 3D mask | — |
| [Mono3DRefer](https://doi.org/10.1609/aaai.v38i7.28525) | 3D, other sensors and domains | 3D box | Ambiguity & distractors |
| [Talk2Car](https://doi.org/10.18653/v1/d19-1215) | 3D, other sensors and domains | box | Ambiguity & distractors |
| [NuPrompt](https://doi.org/10.1609/aaai.v39i8.32902) | 3D, other sensors and domains | 3D box, tube/track | Multiple targets |
| [Talk2BEV-Bench](https://doi.org/10.1109/icra57147.2024.10611485) | 3D, other sensors and domains | — | — |
| [STRefer](https://doi.org/10.1007/978-3-031-72952-2_26) | 3D, other sensors and domains | 3D box | — |
| [Talk2Radar](https://doi.org/10.1109/icra55743.2025.11128399) | 3D, other sensors and domains | 3D box | Multiple targets |
| [RGBT-GroundBench](https://doi.org/10.1007/978-3-032-37422-6_24) | 3D, other sensors and domains | box | Missing modality, Degraded / noisy input |
| [RSVG](https://doi.org/10.1145/3503161.3548316) | 3D, other sensors and domains | box | — |
| [DIOR-RSVG](https://doi.org/10.1109/tgrs.2023.3250471) | 3D, other sensors and domains | box | — |
| [RefSegRS](https://doi.org/10.1109/tgrs.2024.3369720) | 3D, other sensors and domains | mask | — |
| [RRSIS-D](https://doi.org/10.1109/cvpr52733.2024.02517) | 3D, other sensors and domains | mask | — |
| [MS-CXR](https://doi.org/10.1007/978-3-031-20059-5_1) | 3D, other sensors and domains | map | — |
| [GMPG-ImaGenome](https://doi.org/10.1109/tmi.2026.3707568) | 3D, other sensors and domains | box | Absent target / false premise, Multiple targets, Domain / sensor shift |

<a id="surveys"></a>

## 📖 Surveys

| Survey | Venue | Year |
|---|---|:---:|
| [Multimodal Referring Segmentation: A Survey](https://doi.org/10.1007/s11263-026-02943-8) | International Journal of Computer Vision | 2026 |
| [Toward Visual Grounding: A Survey](https://doi.org/10.1109/tpami.2025.3630635) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2026 |
| [Reasoning Segmentation for Images and Videos: A Survey](https://doi.org/10.1007/s11263-026-02903-2) | International Journal of Computer Vision | 2026 |
| [From Words to Pixels: A Comprehensive Survey on Large Language Models in Visual Segmentation](https://doi.org/10.18653/v1/2026.acl-long.2155) | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) | 2026 |
| [Visual Grounding in 2D and 3D: A unified perspective and survey](https://doi.org/10.1016/j.inffus.2025.103625) | Information Fusion | 2026 |
| [A Survey on Video Temporal Grounding With Multimodal Large Language Model](https://doi.org/10.1109/tpami.2025.3615586) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2026 |
| [Audio-Visual Intelligence in Large Foundation Models](https://arxiv.org/abs/2605.04045) | arXiv | 2026 |
| [Omni Survey for Multimodality Analysis in Visual Object Tracking](https://arxiv.org/abs/2508.13000) | arXiv | 2026 |
| [Multimodal Alignment and Fusion: A Survey](https://doi.org/10.1007/s11263-025-02667-1) | International Journal of Computer Vision | 2026 |
| [Multimodal fusion on low-quality data: A comprehensive survey](https://doi.org/10.1016/j.inffus.2026.104437) | Information Fusion | 2026 |
| [Deep Multimodal Learning with Missing Modality: A Survey](https://openreview.net/forum?id=tc7RFcx4hT) | Transactions on Machine Learning Research | 2026 |
| [Uncertainty-Aware Decision Making in Multimodal Large Language Models](https://arxiv.org/abs/2608.17084) | arXiv | 2026 |
| [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://doi.org/10.18653/v1/2026.findings-acl.1325) | Findings of the Association for Computational Linguistics: ACL 2026 | 2026 |
| [Revealing the Seen, Imagining the Beyond: A Survey of Image-Grounded Chain-of-Thought Reasoning in Multimodal LLMs](https://doi.org/10.18653/v1/2026.acl-long.2087) | Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) | 2026 |
| [Towards Understanding Visual Grounding in Visual Language Models](https://arxiv.org/abs/2509.10345) | arXiv | 2025 |
| [A Survey on Text-Guided 3-D Visual Grounding: Elements, Recent Advances, and Future Directions](https://doi.org/10.1109/tnnls.2025.3584895) | IEEE Transactions on Neural Networks and Learning Systems | 2025 |
| [When LLMs step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via Multi-modal Large Language Models](https://arxiv.org/abs/2405.10255) | arXiv | 2025 |
| [From Waveforms to Pixels: A Survey on Audio-Visual Segmentation](https://arxiv.org/abs/2508.03724) | arXiv | 2025 |
| [A Review of Visual Grounding on Remote Sensing Images](https://doi.org/10.3390/electronics14142815) | Electronics | 2025 |
| [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930) | arXiv | 2025 |
| [A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models](https://arxiv.org/abs/2502.17516) | arXiv | 2025 |
| [Reliable and Responsible Foundation Models](https://openreview.net/forum?id=nLJZh4M6S5) | Transactions on Machine Learning Research | 2025 |
| [Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey](https://arxiv.org/abs/2503.12605) | arXiv | 2025 |
| [Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers](https://arxiv.org/abs/2506.23918) | arXiv | 2025 |
| [A survey of methods for addressing the challenges of referring image segmentation](https://doi.org/10.1016/j.neucom.2024.127599) | Neurocomputing | 2024 |
| [Foundations \& Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions](https://doi.org/10.1145/3656580) | ACM Computing Surveys | 2024 |
| [A survey on multimodal large language models](https://doi.org/10.1093/nsr/nwae403) | National Science Review | 2024 |
| [Multimodal Foundation Models: From Specialists to General-Purpose Assistants](https://doi.org/10.1561/0600000110) | Foundations and Trends® in Computer Graphics and Vision | 2024 |
| [Vision-Language Models for Vision Tasks: A Survey](https://doi.org/10.1109/tpami.2024.3369699) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2024 |
| [Towards Open Vocabulary Learning: A Survey](https://doi.org/10.1109/tpami.2024.3361862) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2024 |
| [A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future](https://doi.org/10.1109/tpami.2024.3413013) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2024 |
| [Adventures of Trustworthy Vision-Language Models: A Survey](https://doi.org/10.1609/aaai.v38i20.30275) | Proceedings of the AAAI Conference on Artificial Intelligence | 2024 |
| [A Survey on Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2402.00253) | arXiv | 2024 |
| [Explainable and Interpretable Multimodal Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2412.02104) | arXiv | 2024 |
| [Temporal Sentence Grounding in Videos: A Survey and Future Directions](https://doi.org/10.1109/tpami.2023.3258628) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2023 |
| [A Survey on Temporal Sentence Grounding in Videos](https://doi.org/10.1145/3532626) | ACM Transactions on Multimedia Computing, Communications, and Applications | 2023 |
| [A Survey on Video Moment Localization](https://doi.org/10.1145/3556537) | ACM Computing Surveys | 2023 |
| [Learning in Audio-visual Context: A Review, Analysis, and New Perspective](https://arxiv.org/abs/2208.09579) | arXiv | 2022 |
| [Referring Expression Comprehension: A Survey of Methods and Datasets](https://doi.org/10.1109/tmm.2020.3042066) | IEEE Transactions on Multimedia | 2021 |
| [Deep Audio-visual Learning: A Survey](https://doi.org/10.1007/s11633-021-1293-0) | International Journal of Automation and Computing | 2021 |
| [Multimodal Machine Learning: A Survey and Taxonomy](https://doi.org/10.1109/tpami.2018.2798607) | IEEE Transactions on Pattern Analysis and Machine Intelligence | 2019 |

<a id="data-and-scripts"></a>

## 📦 Data & scripts

| File | What it contains |
|---|---|
| [`data/literature_db.csv`](data/literature_db.csv) · [`.jsonl`](data/literature_db.jsonl) | One row per paper: facets A–H, architecture, foundation models, datasets, metrics, robustness tests, limitations, code links |
| [`data/benchmark_values.csv`](data/benchmark_values.csv) | 1,109 results, each with benchmark, split, metric, setting, and the paper version + table it was copied from |
| [`data/codebook.md`](data/codebook.md) | Definitions and decision rules for every facet value |
| [`data/references.bib`](data/references.bib) | Registry-sourced BibTeX for all papers |
| [`data/gap_search/`](data/gap_search) | Logged searches behind the survey's gap map (queries, hits, near-misses, verdicts) |
| [`data/icr/`](data/icr) · [`data/corrections/`](data/corrections) | Inter-coder reliability study and every post-review correction |
| [`data/bibliometrics/`](data/bibliometrics) · [`data/timeline.csv`](data/timeline.csv) | Publication-trend counts and verified milestones |
| [`scripts/`](scripts) | Scripts that build the tables and figures |

> ⚠️ Benchmark values are comparable **only within the same protocol** (split, metric, supervision setting). Several published comparison tables misquote baselines; every value here comes from the original paper.

## 🤝 Contributing

Missing a paper? Open an issue or a pull request with the title, venue and a link to the official version.

<a id="citation"></a>

## 📝 Citation

```bibtex
@misc{orvatinia2026reliable,
  title  = {Reliable Multimodal Grounding: A Survey},
  author = {Orvati Nia, Fahimeh},
  year   = {2026},
  note   = {In preparation},
  url    = {https://github.com/fahimehorvatinia/awesome-reliable-grounding}
}
```

## 📄 License

List and data: [CC BY 4.0](LICENSE) · Scripts: [MIT](scripts/LICENSE)
