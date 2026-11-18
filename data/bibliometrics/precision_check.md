# Precision check of keyword-based publication counts (Semantic Scholar bulk search, retrieved 2026-11-17)

Protocol: for each task family, 20 titles were sampled uniformly at random (fixed seed) from the first 60 results
returned for publication year 2024 and judged by hand as *on-topic* (a grounding task of that family, or a
method/dataset/analysis for it) or *off-topic*. Precision = on-topic / 20. Queries are in `bibliometrics.py`.

| family | query version | on-topic / 20 | estimated precision | used for Fig. 2b? |
|---|---|---|---|---|
| image | v1 | 19 | 0.95 | yes |
| video (temporal, spatio-temporal, RVOS, RMOT) | v1 | 18 | 0.90 | yes |
| audio-visual | v1 (any "sound source localization") | ~4 | ~0.2 (acoustics papers) | no |
| audio-visual | v2 (+visual terms) | ~10 | ~0.5 | no |
| audio-visual | v3 (strict phrases) | 18 | 0.90 | yes |
| 3D | v1 | 19 | 0.95 | yes |
| MLLM grounding | v2 | 9 | 0.45 | no (general MLLM papers that list grounding as one capability) |
| reliability (keyword) | v2 | 4 | 0.20 | no — reliability counts come from the curated verified database instead |

Off-topic examples recorded during judging: video — grounded text-to-video generation, audio-visual QA;
audio-visual v3 — a general audio-video survey, binaural audio generation; 3D — semi-supervised 3D semantic
segmentation; reliability keyword — efficiency, weakly-supervised and dataset papers that mention "robustness"
or "uncertainty" generically.

Caveats: counts are of Computer-Science-tagged records whose title/abstract match the query; they include
preprints and duplicates across versions; 2026 is partial (to 17 November). Counts indicate trends, not
exact population sizes; recall of strict phrase queries is lower than that of broad ones.
