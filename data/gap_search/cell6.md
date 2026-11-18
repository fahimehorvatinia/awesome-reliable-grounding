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
