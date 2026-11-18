"""Appendix B tables B4-B6: video, audio-visual and 3D grounding results under matched protocols.

Usage: python3 -I build_more_tables.py <protocols.csv> <out.tex>

Every cell is looked up in protocols.csv (values copied from each paper's own table; the paper version
and table are in the `source` column). Rows are pinned to one configuration per paper with a setting
filter; a cell is filled only when exactly one protocol row matches benchmark, split, metric and filter.
Splits that the source table does not state exactly are not used. Values reported as fractions (sound-
source localisation cIoU/AUC below 1) are shown as percentages.
"""
import csv
import re
import sys

SYN = {"R@1 IoU=0.5": "R1@0.5", "R@1 IoU=0.7": "R1@0.7", "mIoU": "J", "M_J": "J", "mIoU (J)": "J",
       "s (lower better)": "S (lower better)", "S (lower better; x100 scale in this table)": "S (lower better)"}

# ---- column definitions: (benchmark, accepted splits, metric, header) ----
VIDEO_TG = [("Charades-STA", {"test"}, "R1@0.5", "R1@0.5"), ("Charades-STA", {"test"}, "R1@0.7", "R1@0.7"),
            ("Charades-STA", {"test"}, "mIoU", "mIoU"),
            ("QVHighlights", {"test"}, "MR R1@0.5", "R1@0.5"), ("QVHighlights", {"test"}, "MR R1@0.7", "R1@0.7"),
            ("QVHighlights", {"test"}, "MR mAP (avg)", "mAP")]
VIDEO_STVG = [("VidSTG", {"test (declarative)"}, "m_vIoU", "decl."), ("VidSTG", {"test (interrogative)"}, "m_vIoU", "interr."),
              ("HC-STVG", {"v1 test"}, "m_vIoU", "v1 test")]
VIDEO_RVOS = [("Ref-YouTube-VOS", {"val", "val (server)", "val (public server)"}, "J&F", "val"),
              ("Ref-DAVIS17", {"val"}, "J&F", "val"), ("MeViS", {"valid", "v1 valid"}, "J&F", "valid")]
AV_AVS = [("AVSBench S4", {"test"}, "J", "S4"), ("AVSBench MS3", {"test"}, "J", "MS3"), ("AVSBench AVSS", {"test"}, "J", "AVSS")]
AV_REF = [("Ref-AVS", {"Seen"}, "J", "Seen $\\mathcal{J}$"), ("Ref-AVS", {"Unseen"}, "J", "Unseen $\\mathcal{J}$"),
          ("Ref-AVS", {"Null"}, "S (lower better)", "Null $\\mathcal{S}\\downarrow$")]
AV_SSL = [("VGG-SS", {"test"}, "cIoU", "cIoU"), ("VGG-SS", {"test"}, "AUC", "AUC"),
          ("Extended VGG-SS (with negatives)", {"test"}, "AP", "AP"), ("Extended VGG-SS (with negatives)", {"test"}, "max-F1", "max-F1")]
D3 = [("ScanRefer", {"val (overall)"}, "Acc@0.25", "Acc@0.25"), ("ScanRefer", {"val (overall)"}, "Acc@0.5", "Acc@0.5"),
      ("Nr3D", {"test (overall)", "overall"}, "accuracy", "Nr3D"), ("Sr3D", {"test (overall)", "overall"}, "accuracy", "Sr3D"),
      ("Multi3DRefer", {"val (all)"}, "F1@0.5", "F1@0.5")]

# ---- rows: (group, key, label, filter) ; filter = substring of `setting` (str), dict benchmark->substring, or None ----
R_TG = [
    ("Fine-tuned specialist models", "gao2017tall", "CTRL", "CTRL"),
    ("Fine-tuned specialist models", "zhang2020learning", "2D-TAN", None),
    ("Fine-tuned specialist models", "zhang2020span", "VSLNet", "without fine-tuning"),
    ("Fine-tuned specialist models", "wang2022negative", "MMN", None),
    ("Fine-tuned specialist models", "lei2021detecting", "Moment-DETR", "from scratch"),
    ("Fine-tuned specialist models", "moon2023query", "QD-DETR", None),
    ("Fine-tuned specialist models", "sun2024trdetr", "TR-DETR", None),
    ("Fine-tuned specialist models", "moon2023correlation", "CG-DETR", None),
    ("Fine-tuned specialist models", "li2023momentdiff", "MomentDiff", "SlowFast+CLIP"),
    ("Fine-tuned specialist models", "mu2024snag", "SnAG", None),
    ("Fine-tuned specialist models", "zhou2025devil", "TD-DETR", {"Charades-STA": "fine-tuned, TD-DETR, SlowFast", "QVHighlights": "TD-DETR"}),
    ("Fine-tuned after grounding pre-training", "lei2021detecting", "Moment-DETR (ASR pre-training)", "ASR pre-training"),
    ("Fine-tuned after grounding pre-training", "lin2023univtg", "UniVTG", None),
    ("Fine-tuned MLLMs", "ren2024timechat", "TimeChat-7B", "fine-tuned 3 epochs"),
    ("Fine-tuned MLLMs", "wang2025timer1", "Time-R1-7B", "fine-tuned on Charades"),
    ("Fine-tuned MLLMs", "wu2025number", "NumPro-FT (LongVA-7B)", "NumPro-FT"),
    ("Zero-shot (no target-benchmark training)", "huang2024vtimellm", "VTimeLLM-7B", "7B"),
    ("Zero-shot (no target-benchmark training)", "qian2024momentor", "Momentor-7B", None),
    ("Zero-shot (no target-benchmark training)", "ren2024timechat", "TimeChat-7B", "zero-shot"),
    ("Zero-shot (no target-benchmark training)", "wu2025number", "NumPro (Qwen2-VL-7B)", "training-free"),
    ("Zero-shot (no target-benchmark training)", "guo2025trace", "TRACE-7B", None),
    ("Zero-shot (no target-benchmark training)", "wang2025timer1", "Time-R1-7B", "zero-shot"),
]
R_STVG = [
    ("Fine-tuned specialist models", "zhang2020vidstg", "STGRN", None),
    ("Fine-tuned specialist models", "tang2022hcstvg", "STGVT", "STGVT"),
    ("Fine-tuned specialist models", "yang2022tubedetr", "TubeDETR", None),
    ("Fine-tuned specialist models", "jin2022embracing", "STCAT", None),
    ("Fine-tuned specialist models", "gu2024context", "CG-STVG", None),
    ("Fine-tuned specialist models", "gu2025knowing", "TA-STVG", None),
]
R_RVOS = [
    ("Specialist models", "botach2022end", "MTTR (Video-Swin-T)", None),
    ("Specialist models", "wu2022referformer", "ReferFormer (Video-Swin-B)", {"Ref-YouTube-VOS": "no joint RefCOCO", "Ref-DAVIS17": "trained on Ref-YouTube-VOS"}),
    ("Specialist models", "wu2023onlinerefer", "OnlineRefer (Swin-L)", "online, Swin-L"),
    ("Specialist models", "miao2023spectrum", "SgMg (Video-Swin-B)", "Video-Swin-B"),
    ("Specialist models", "ding2023mevis", "LMPM (Swin-T)", None),
    ("Specialist models", "he2024decoupling", "DsHmp (Video-Swin-B)", "Video-Swin-B"),
    ("Specialist models", "he2024decoupling", "DsHmp (Swin-T)", {"Ref-YouTube-VOS": "Video-Swin-T", "MeViS": "Swin-T"}),
    ("Specialist models", "cuttano2025samwise", "SAMWISE (SAM 2 Hiera-B)", "RoBERTa"),
    ("Specialist models", "rong2025mpgsam2", "MPG-SAM 2", None),
    ("Specialist models", "zheng2025villa", "ViLLa", None),
    ("MLLM-based models", "yan2024visa", "VISA (13B)", None),
    ("MLLM-based models", "bai2024one", "VideoLISA (3.8B, post-opt.)", "post-optimization"),
    ("MLLM-based models", "munasinghe2025videoglamm", "VideoGLaMM", None),
    ("MLLM-based models", "ding2025mevistpami", "LMPM++", None),
]
R_AVS = [
    ("Trained on AVSBench", "zhou2025avss", "TPAVI (PVT-v2)", {"AVSBench S4": "PVT-v2 backbone", "AVSBench MS3": "from scratch", "AVSBench AVSS": "PVT-v2 backbone"}),
    ("Trained on AVSBench", "mao2023multimodal", "ECMVAE (PVT)", "PVT"),
    ("Trained on AVSBench", "li2023catr", "CATR (PVT-v2)", {"AVSBench S4": "original annotations", "AVSBench MS3": "original annotations", "AVSBench AVSS": "PVT-v2"}),
    ("Trained on AVSBench", "gao2024avsegformer", "AVSegFormer (PVT-v2)", None),
    ("Trained on AVSBench", "yang2024cooperation", "COMBO (PVT-v2)", None),
    ("Trained on AVSBench", "chen2024cpm", "CPM (ResNet-50)", "224x224"),
    ("Trained on AVSBench", "chen2024unraveling", "CAVP (D-ResNet-50)", None),
    ("Trained on AVSBench", "liu2024bavs", "BAVS (Swin)", None),
    ("Trained on AVSBench", "ma2024stepping", "AAVS (Swin-B)", None),
    ("Trained on AVSBench", "du2025crab", "Crab (MLLM, ViT-L/14)", None),
    ("Zero-shot (no AVSBench training)", "senocak2023sound", "Senocak et al. (2023)", None),
    ("Zero-shot (no AVSBench training)", "sun2023learning", "FNAC", None),
    ("Zero-shot (no AVSBench training)", "park2024clip", "ACL-SSL", None),
]
R_REF = [
    ("Ref-AVS", "wang2024refavs", "EEMC (Ref-AVS baseline)", None),
    ("Ref-AVS", "radman2025tsam", "TSAM (SAM ViT-B)", None),
    ("Ref-AVS", "wang2025sam2love", "SAM2-LOVE", None),
    ("Ref-AVS", "ying2025omniavs", "OISA-1B", None),
    ("Ref-AVS", "du2025crab", "Crab (MLLM)", None),
]
R_SSL = [
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "chen2021localizing", "LVS", "144k"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "senocak2022learning", "Senocak et al. (2022)", None),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "liu2022exploiting", "Liu et al. (2022)", "ResNet-18"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "mo2022ezvsl", "EZ-VSL", "no OGL"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "mo2022closer", "SLAVC", "SLAVC w/o OGL, VGG-Sound 144k"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "sun2023learning", "FNAC", "w/o OGL"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "senocak2023sound", "Senocak et al. (2023)", "w/o OGL"),
    ("Self-supervised, trained on VGG-Sound 144k, without OGL", "park2024clip", "ACL-SSL (CLIP)", "w/o OGL"),
]
R_3D = [
    ("Specialist models, no extra 3D-language data", "chen2020scanrefer", "ScanRefer", None),
    ("Specialist models, no extra 3D-language data", "achlioptas2020referit3d", "ReferIt3DNet", "DGCN"),
    ("Specialist models, no extra 3D-language data", "zhao2021threedvg", "3DVG-Transformer", {"ScanRefer": "2D+3D input", "Nr3D": "GT object boxes", "Sr3D": "GT object boxes"}),
    ("Specialist models, no extra 3D-language data", "yuan2021instancerefer", "InstanceRefer", None),
    ("Specialist models, no extra 3D-language data", "yang2021sat", "SAT", None),
    ("Specialist models, no extra 3D-language data", "huang2022multiview", "MVT", None),
    ("Specialist models, no extra 3D-language data", "luo2022threedsps", "3D-SPS", None),
    ("Specialist models, no extra 3D-language data", "cai2022threedjcg", "3DJCG-G (grounding only)", "3DJCG-G"),
    ("Specialist models, no extra 3D-language data", "chen2022d3net", "D3Net (listener only)", "listener only"),
    ("Specialist models, no extra 3D-language data", "jain2022butd", "BUTD-DETR", None),
    ("Specialist models, no extra 3D-language data", "chen2022language", "ViL3DRel", None),
    ("Specialist models, no extra 3D-language data", "wu2023eda", "EDA", None),
    ("Specialist models, no extra 3D-language data", "zhang2023multi3drefer", "M3DRef-CLIP", {"ScanRefer": None, "Multi3DRefer": None}),
    ("Specialist models, no extra 3D-language data", "unal2024four", "ConcreteNet", "ConcreteNet full"),
    ("With extra pre-training or LLM-generated data", "guo2023viewrefer", "ViewRefer (GPT-3-expanded text)", None),
    ("With extra pre-training or LLM-generated data", "zhu2023threedvista", "3D-VisTA (Mask3D proposals)", {"ScanRefer": "Mask3D", "Nr3D": None, "Sr3D": None}),
    ("With extra pre-training or LLM-generated data", "jia2024sceneverse", "GPS (SceneVerse)", None),
    ("3D-LLMs", "zhu2024scanreason", "ReGround3D (3B)", None),
    ("3D-LLMs", "huang2024chatscene", "Chat-Scene (7B)", None),
    ("3D-LLMs", "zheng2025video3dllm", "Video-3D LLM (7B)", None),
    ("Zero-shot (no 3D grounding training)", "li2025seeground", "SeeGround (Qwen2-VL-72B)", None),
]


def lookup(rows, key, bench, splits, metric, filt):
    f = filt.get(bench, "__any__") if isinstance(filt, dict) else filt
    if isinstance(filt, dict) and bench not in filt:
        return None
    vals = {}
    for r in rows:
        if r["key"] != key or r["benchmark"] != bench:
            continue
        if SYN.get(r["metric"], r["metric"]) != SYN.get(metric, metric):
            continue
        if f not in (None, "__any__") and f not in r["setting"]:
            continue
        v = float(r["value"])
        if r["split"] in splits:
            pass
        elif r["split"] == "Seen / Unseen" and "Seen" in splits:
            pass  # combined row: the value is the Seen split
        elif r["split"] == "Seen / Unseen" and "Unseen" in splits:
            m = re.search(r"Unseen = ([0-9.]+)", r["setting"])
            if not m:
                continue
            v = float(m.group(1))
        else:
            continue
        if "x100 scale" in r["metric"]:
            v /= 100.0
        vals[v] = r
    if len(vals) > 1:
        sys.exit(f"ambiguous cell {key} {bench} {metric}: {sorted(vals)}")
    if not vals:
        return None
    v = next(iter(vals))
    if metric in ("cIoU", "AUC") and v <= 1:
        v *= 100
    return v


STATUS = {}


def fmt(v, metric):
    if v is None:
        return "--"
    if metric.startswith("S ("):
        return f"{v:.3f}"
    return f"{v:.1f}" if abs(v - round(v, 1)) < 1e-9 else f"{v:.2f}"


def block(rows, cols, spec, groups_hdr, title):
    out = [f"\\multicolumn{{{2 + len(cols)}}}{{@{{}}l}}{{\\textbf{{{title}}}}}\\\\"]
    out.append(groups_hdr)
    out.append("\\midrule")
    last = None
    used = 0
    for grp, key, label, filt in spec:
        vals = [lookup(rows, key, b, s, m, filt) for b, s, m, _ in cols]
        if all(v is None for v in vals):
            continue
        if grp != last:
            out.append(f"\\multicolumn{{{2 + len(cols)}}}{{@{{}}l}}{{\\emph{{{grp}}}}}\\\\")
            last = grp
        dag = "$^{\\dagger}$" if STATUS.get(key, "peer-reviewed") != "peer-reviewed" else ""
        out.append(f"{label}{dag} & \\citep{{{key}}} & " + " & ".join(fmt(v, m) for v, (_, _, m, _) in zip(vals, cols)) + "\\\\")
        used += 1
    return out, used


def header(cols, groups):
    """groups: list of (span, name)."""
    top = " & & " + " & ".join(f"\\multicolumn{{{n}}}{{c}}{{{name}}}" for n, name in groups) + "\\\\"
    rules, c = [], 3
    for n, _ in groups:
        rules.append(f"\\cmidrule(lr){{{c}-{c + n - 1}}}")
        c += n
    sub = "Method & Ref. & " + " & ".join(h for _, _, _, h in cols) + "\\\\"
    return top + "\n" + "".join(rules) + "\n" + sub


def table(rows, label, caption, blocks, split_after=None, cont_caption=None):
    out = ["\\begin{table*}[p]", f"\\caption{{{caption}}}", f"\\label{{{label}}}", "\\centering\\scriptsize",
           "\\setlength{\\tabcolsep}{3pt}\\renewcommand{\\arraystretch}{0.84}"]
    total = 0
    for i, (cols, spec, groups, title) in enumerate(blocks):
        if split_after is not None and i == split_after:
            out += ["\\end{table*}", "", "\\begin{table*}[p]", f"\\caption{{{cont_caption}}}", f"\\label{{{label}-cont1}}",
                    "\\centering\\scriptsize", "\\setlength{\\tabcolsep}{3pt}\\renewcommand{\\arraystretch}{0.84}"]
        elif i:
            out.append("\\par\\smallskip")
        out.append("\\begin{tabular}{@{}l l " + "r" * len(cols) + "@{}}")
        out.append("\\toprule")
        b, used = block(rows, cols, spec, header(cols, groups), title)
        out += b
        out += ["\\bottomrule", "\\end{tabular}"]
        total += used
    out.append("\\end{table*}")
    return out, total


def main():
    rows = [r for r in csv.DictReader(open(sys.argv[1]))]
    for r in rows:
        STATUS[r["key"]] = r["status"]
    t4, n4 = table(rows, "tab:temporal-results",
                   "Video grounding under matched protocols: (a) temporal grounding (Charades-STA test and QVHighlights test, moment retrieval), (b) spatio-temporal video grounding (VidSTG test; HC-STVG v1 test), (c) referring video object segmentation ($\\mathcal{J}\\&\\mathcal{F}$). Values are copied from each paper's own table (paper version and table in the released \\texttt{protocols.csv}); one configuration per row, as labelled. Rows are grouped by training setting; compare only within a group and a column. Splits that the source does not state exactly are omitted (--). $^{\\dagger}$Preprint or workshop paper.",
                   [(VIDEO_TG, R_TG, [(3, "Charades-STA"), (3, "QVHighlights")], "(a) Temporal grounding"),
                    (VIDEO_STVG, R_STVG, [(2, "VidSTG m\\_vIoU"), (1, "HC-STVG m\\_vIoU")], "(b) Spatio-temporal grounding"),
                    (VIDEO_RVOS, R_RVOS, [(1, "Ref-YouTube-VOS"), (1, "Ref-DAVIS17"), (1, "MeViS")], "(c) Referring video object segmentation")],
                   split_after=2, cont_caption="Video grounding under matched protocols (continued from Table~\\ref{tab:temporal-results}).")
    t5, n5 = table(rows, "tab:av-results",
                   "Audio-visual grounding under matched protocols: (a) audio-visual segmentation on AVSBench ($\\mathcal{J}$, i.e. mIoU, test split; single-source S4, multi-source MS3, semantic AVSS), (b) referring audio-visual segmentation on Ref-AVS ($\\mathcal{J}$ on the Seen and Unseen splits; $\\mathcal{S}$ on the Null split, lower is better), (c) visual sound-source localisation on VGG-SS (cIoU, AUC) and on VGG-SS extended with negatives (AP, max-F1). Values reported as fractions are shown as percentages, and $\\mathcal{S}$ values printed on a $\\times100$ scale (OISA) are rescaled. Same conventions as Table~\\ref{tab:temporal-results}; CPM is reported at $224\\times224$ input, as the other entries.",
                   [(AV_AVS, R_AVS, [(3, "AVSBench $\\mathcal{J}$")], "(a) Audio-visual segmentation"),
                    (AV_REF, R_REF, [(3, "Ref-AVS test")], "(b) Referring audio-visual segmentation"),
                    (AV_SSL, R_SSL, [(2, "VGG-SS"), (2, "VGG-SS + negatives")], "(c) Sound-source localisation")])
    t6, n6 = table(rows, "tab:3d-results",
                   "3D visual grounding under matched protocols: ScanRefer validation (overall Acc@0.25 and Acc@0.5, detected proposals), Nr3D and Sr3D test (overall accuracy with ground-truth object proposals, ReferIt3D protocol), and Multi3DRefer validation (F1@0.5, all descriptions including zero- and multi-target). Same conventions as Table~\\ref{tab:temporal-results}; the ScanRefer and ReferIt3D protocols differ (detected vs ground-truth proposals) and are not comparable with each other.",
                   [(D3, R_3D, [(2, "ScanRefer val"), (1, "Nr3D"), (1, "Sr3D"), (1, "Multi3DRefer")], "3D visual grounding")])
    s = ["%% BEGIN generated tables B4-B6 (stage6/scripts/build_more_tables.py)"] + t4 + [""] + t5 + [""] + t6 + ["%% END generated tables B4-B6"]
    open(sys.argv[2], "w").write("\n".join(s) + "\n")
    print(f"rows: video {n4}, AV {n5}, 3D {n6}")


if __name__ == "__main__":
    main()
