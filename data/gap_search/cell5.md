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
