# Codebook for the eight-facet taxonomy of multimodal grounding (Stage 3, v1.1)

The codebook gives the operational definition of every value of facets A–H, decision rules for borderline cases, and the precedence rules for the single-label facet E. A work is coded from what the paper **does** (task definition, method, experiments), not from its related-work discussion. Facets A–D, F, G, H are multi-label; facet E is single-label.

Notation (Sect. 2 of the survey): a scene X = {x^(m)}, a query q = (ι, Q) with referring intent ι and query signals Q, a referent set R* ⊆ Ω with |R*| = K ∈ {0, 1, …}, and a model f_θ(X, q) = (Ŷ, a, e) with predictions Ŷ, abstention flag a and evidence e.

---

## Admission test (applied before coding)

A work is a **grounding work** if its task satisfies all four criteria:
- **C1 query-conditional:** with X fixed, changing the referent in q changes the output.
- **C2 explicit localisation:** the output indexes the target signal (point, box, mask, interval, tube, 3D region).
- **C3 cross-modal or cross-instance:** the query and target differ in modality, or are different instances (exemplar → image).
- **C4 defined referent set:** the ground truth is a set R* with |R*| ∈ {0, 1, …, K}.

Three further kinds of work are admitted as `analysis` or `dataset` even though they propose no grounding model: (i) works that study the reliability, evaluation or interpretability of an admitted task; (ii) works that use a grounding output to verify or calibrate the output of another task; (iii) studies of object-existence hallucination, because existence judgements are the K = 0 case of selectivity. Works that fail admission are not coded on facets A–H.

---

## Facet A — Query modality (multi-label)
*The signal that specifies what to localise.* Code the modality of q, not of the scene.

| Value | Definition | Decision rules / examples |
|---|---|---|
| `phrase/class name` | A category name or short noun phrase whose referent is identified without disambiguating same-category instances. | Open-vocabulary detection prompts; phrase grounding of caption noun phrases (Flickr30k Entities); concept prompts ("all yellow school buses"). |
| `referring expression` | A natural-language description intended to single out specific instance(s) by attributes, relations, location or motion. | RefCOCO-style, Nr3D/ScanRefer, Charades-STA/QVHighlights sentence queries, motion expressions. Instructions that name the target ("click the search button") are referring expressions. |
| `implicit instruction` | A goal, question or instruction whose referent must be inferred and is not named. | Reasoning segmentation ("what keeps food cold?"), grounded VideoQA questions (NExT-GQA), interrogative STVG sentences (VidSTG), task-oriented robot instructions. |
| `speech` | A spoken-language query (waveform or speech features). | Audio-guided VOS with spoken expressions. ASR-transcribed text that is only ever used as text is `referring expression`. |
| `non-speech sound` | An audio signal used to pick out its source or event. | AVS, sound-source localisation: the audio track is the query even though it is also part of the scene. |
| `visual exemplar` | An image or crop of the target, a different instance from the target signal. | One-shot/personalised segmentation, exemplar prompts; a visual segment used to query another modality (visual-to-audio localisation). |
| `visual prompt` | A click, box, scribble or mask drawn on the target signal itself. | SAM-style prompts. Coded only when the prompt specifies what to localise: region-referring inputs whose only output is a caption (box in, text out) are not coded. |
| `gesture/gaze` | Pointing gestures, gaze or body cues. | Embodied reference datasets. |
| `composite` | The task requires *jointly* interpreting ≥2 query signals of different modalities. | Ref-AVS (expression + audio), omni-modal expressions. Always code the constituent modalities as well. Do **not** code `composite` for a model that merely supports several query types in separate tasks. |

## Facet B — Target context (multi-label)
*The signal in which the referent is localised.*

| Value | Definition | Decision rules |
|---|---|---|
| `image` | Single natural RGB image, including screenshots. | Not coded when a domain-specific value (remote sensing, medical) applies. Single-frame sound-source localisation (one frame plus an audio clip) is coded `image`, with the audio as the query (facet A). |
| `silent video` | Video or ordered frame sequence whose audio track is not used. | Moment retrieval, STVG, RVOS, RMOT; posed multi-view RGB sequences without depth. |
| `audio-visual video` | Video whose frames and audio track are processed over time. | AVS, Ref-AVS, audio-visual event localisation. |
| `audio-only` | Waveform or spectrogram; the output localises in time or time–frequency. | Text-to-audio grounding, sound-event detection conditioned on a query. |
| `RGB-D` | Single or multi-view RGB with depth used as input. | |
| `point cloud` | Point clouds, meshes or reconstructed scans. | ScanNet-based 3D-VG. Code `RGB-D` as well only if raw RGB-D frames are inputs. |
| `radiance field/3DGS` | NeRF or 3D Gaussian Splatting scene representations. | |
| `LiDAR/radar/thermal` | Non-RGB physical sensors. | Outdoor LiDAR grounding, radar, thermal. |
| `remote sensing` | Aerial or satellite imagery. | Replaces `image`. |
| `medical` | Medical images or volumes. | Replaces `image`. |

## Facet C — Referent type (multi-label)

| Value | Definition | Decision rules |
|---|---|---|
| `object instance` | A countable object. | Default for REC/RES/3D-VG. |
| `part` | A part of an object. | Only if parts are explicitly evaluated. |
| `stuff/region` | Amorphous region or background class (sky, road, "the area left of…"). | |
| `set (0..K)` | The task explicitly admits zero or several referents per query. | Code when the benchmark contains no-target or multi-target queries, or the output is "all instances of a concept". Not coded for strictly single-target tasks. |
| `event/action` | A temporal segment of an activity or event. | Moment retrieval, temporal sentence grounding, audio-visual events. An object identified by its motion or action (MeViS, A2D, STVG tubes) is an `object instance`. |
| `sound source` | The object or region emitting a sound. | AVS, SSL, Ref-AVS. |
| `relation/interaction` | The referent is a relation (subject–object pair, human–object interaction). | |
| `affordance` | A functional region (where to grasp, sit, press). | |

## Facet D — Output representation (multi-label)
Code every localisation output that is produced **and evaluated**.

| Value | Definition | Decision rules |
|---|---|---|
| `point/heatmap` | A point, keypoint or dense relevance/heat map. | Sound-source localisation maps; point outputs of MLLMs. |
| `2D box` | Axis-aligned 2D box. | |
| `rotated box` | Oriented 2D box. | Remote sensing. |
| `mask` | Pixel mask, including per-frame mask sequences scored per frame (J&F). | RVOS outputs are `mask`. |
| `temporal interval` | [start, end] on a time axis. | |
| `tube/track` | A spatio-temporal sequence of boxes or masks whose evaluation requires identity association over time. | STVG tubes (vIoU), RMOT tracks (HOTA). Add to `mask` only when association is evaluated. A tube includes its temporal extent; do not add `temporal interval` for it. |
| `3D box` | 3D bounding box. | |
| `3D mask` | Point- or Gaussian-level 3D mask. | |
| `grounded text` | Text output interleaved with coordinates, region tokens or timestamps. | MLLM grounders; reasoning traces citing boxes or timestamps. Coordinates emitted as text are coded both as `grounded text` and as their geometric family (e.g. `2D box`). Plain descriptions of a given region are not grounded text. |

## Facet E — Architecture paradigm (single-label)
Apply the **first matching rule** in this order.

1. `dataset` — the main contribution is a dataset/benchmark and any model is a baseline built from prior components; if the paper also proposes and evaluates a new method as a contribution, code that method's paradigm instead. `analysis` — the main contribution is an empirical analysis, audit or attack of existing models.
2. `E9 training-free composition` — no parameters are trained for grounding; frozen pre-trained models (detectors, SAM, CLIP, MLLMs) are composed by rules, prompting or test-time optimisation, including per-scene distillation of frozen features into a 3D field.
3. `E8 agentic / tool-using / RL-trained reasoning grounder` — the grounder performs multi-step reasoning with tool calls or zooming, or is trained with reinforcement learning on grounding rewards (GRPO-style), whatever its output head. Offline preference optimisation (DPO-style) without multi-step reasoning is not E8.
4. `E7 MLLM embedding-as-mask` — an MLLM emits special tokens whose embeddings are decoded into masks/boxes by a separate decoder ([SEG]-style) or used to select mask proposals.
5. `E6 MLLM coordinates-as-text` — an MLLM emits coordinates, timestamps or region indices as text tokens.
6. `E5 promptable segmenter + adapter` — a promptable segmenter (SAM family) is driven by query-derived prompts through a light, non-LLM adapter.
7. `E4 open-set grounding pre-training / dual encoder` — the contribution is large-scale grounding pre-training for open-set transfer (GLIP, Grounding DINO, UniVTG), or dual-encoder region–query matching.
8. `E3 query-based set prediction` — DETR-style decoding of learned or query-conditioned object/time queries, usually with set-based (bipartite) matching; single-target query decoders without matching are included.
9. `E1 proposal-and-rank` — external proposals (boxes, masks, temporal or 3D proposals) are scored against the query.
10. `E2 one-stage dense fusion` — the query is fused into dense features and the output is decoded densely (anchors, heatmaps, mask decoder) without set-based queries.

## Facet F — Supervision (multi-label)

| Value | Definition |
|---|---|
| `full` | Manual query–localisation pairs of the output type. |
| `weak` | Supervision weaker than the output from manual labels: image/video-level labels, boxes for masks, points for boxes, narrations without timestamps. |
| `self-supervised correspondence` | Natural co-occurrence (audio–visual synchrony, video–subtitle alignment) with no manual labels, including contrastive multiple-instance learning on audio–visual pairs. |
| `semi-supervised` | A labelled subset plus unlabelled or pseudo-labelled data, including model-in-the-loop data engines. |
| `zero-shot/training-free` | No training on the target grounding task. |
| `synthetic/LLM-generated` | Queries, labels or scenes generated by models or templates (LLM-written expressions, rendered scenes, auto-labelled boxes or masks), whether or not they were later verified by humans. |
| `RL verifiable reward` | Reinforcement learning with rule-checkable rewards (IoU, format). When labels enter only through the reward, `full` is not coded in addition. |

## Facet G — Reliability condition evaluated or addressed (multi-label; `nominal` if none)
Code a condition only if the work **evaluates** it on a dedicated split, protocol or perturbation, **or** proposes a mechanism explicitly designed for it. A mention in the discussion is not enough. Standard benchmarks whose design contains the condition count when they are evaluated (gRefCOCO, MeViS and AVSBench MS3 contain multi-target queries; gRefCOCO, Multi3DRefer, Ref-AVS Null and HumanRef contain no-target queries). Each condition corresponds to a transformation of (X, q) (survey Table "conditions").

| Value | Definition | Decision rules |
|---|---|---|
| `nominal` | No condition beyond the standard i.i.d. benchmark. | |
| `missing modality` | A modality of X or q is absent at test (or training) time. | Includes muted audio, dropped depth, missing subtitles, and blind or unimodal baselines reported as tests of modality reliance. A task designed without a modality (depth-free 3D grounding) is not a missing-modality test. |
| `degraded/noisy modality` | An input modality is corrupted (noise, blur, compression, weather, sensor noise). | Annotation (label) noise is **not** this value; code label-noise audits as `analysis` with the relevant other G values. |
| `conflicting modalities` | Modalities carry incongruent evidence (mismatched audio, misleading text, swapped streams). | |
| `ambiguity/distractors` | Several plausible candidates; same-category distractors; ambiguous or underspecified queries; hard negatives. | |
| `absent target/false premise` | Queries whose referent does not exist (K = 0). | |
| `multi-target` | Queries with K > 1 referents. | |
| `domain/sensor shift` | Train/test distribution shift: cross-dataset, new domain, new sensor or viewpoint. | Includes zero-shot evaluation on a dataset not used for training and unseen query templates. |
| `novel categories/compositions` | Unseen categories, attributes or compositions at test time; open-vocabulary transfer. | |
| `adversarial` | Worst-case perturbations, adversarial queries or backdoors. | |
| `long-horizon drift` | Long videos or sequences where context is long or errors accumulate. | Includes multi-round conversational grounding evaluated per round. |

## Facet H — Verification mechanism in the method (multi-label; `none` if none)

| Value | Definition |
|---|---|
| `none` | No mechanism that checks or qualifies the output. |
| `existence/abstention head` | An explicit output for "no referent" or abstention (token, classifier, trained threshold), including a trained correspondence score used to decide whether the queried source is present. A fixed threshold applied only at evaluation is not coded. |
| `calibrated confidence` | Confidence or uncertainty estimates designed to reflect correctness (uncertainty modelling, calibration, conformal sets). A plain detection score is not enough. |
| `cycle/REG consistency` | Regenerating or re-describing the predicted region and checking it against the query (speaker–listener). |
| `temporal/cross-view consistency` | Agreement across frames or views used to check or filter outputs. Mechanisms that only enforce consistency during training or prediction (memory attention, multi-view fusion) are not verification. |
| `self-verification/re-grounding` | The model re-examines its own output (zoom-in, critique, re-ground) before answering. |
| `external verifier` | A separate model scores or validates the output. |
| `traceable evidence` | The output exposes checkable intermediate evidence (cited boxes, timestamps, reasoning steps tied to regions). |
| `interactive clarification` | The system asks the user to resolve ambiguity. |

---

## Changes from v1.0 to v1.1
v1.0 was used for the blind re-coding of the inter-coder reliability sample (40 works); agreement is reported on v1.0. The disagreements exposed the ambiguities below, which v1.1 resolves; adjudication used v1.1.
- **Admission:** works that use grounding to verify another task, and object-existence hallucination studies, are admitted as analyses; works failing admission are not coded.
- **A:** instructions that name the target are referring expressions; interrogative STVG sentences are implicit; visual prompts count only when they specify what to localise; a visual segment used as a query is a visual exemplar.
- **B:** single-frame sound-source localisation is `image`; posed RGB sequences are `silent video`; `audio-visual video` requires temporal processing of frames and audio.
- **C:** objects identified by motion or action are object instances; `event/action` is reserved for temporal-segment referents.
- **D:** tubes include their temporal extent; coordinates emitted as text are coded with their geometric family; region descriptions are not grounded text.
- **E:** dataset papers that also contribute a method are coded by the method; E3 includes single-target query decoders; E7 includes token embeddings that select proposals; DPO-style preference optimisation is not E8; per-scene distillation of frozen features is E9.
- **F:** generated labels count as synthetic even when verified by humans; contrastive MIL on audio–visual pairs is self-supervised correspondence; RL-only supervision is not also coded as full.
- **G:** evaluated standard benchmarks whose design contains a condition count; zero-shot cross-dataset evaluation and unseen query templates are domain shift; blind/unimodal reliance baselines are missing-modality tests.
- **H:** consistency enforced only during training or prediction is not verification; fixed evaluation-only thresholds are not abstention heads; trained correspondence scores that decide presence are.
