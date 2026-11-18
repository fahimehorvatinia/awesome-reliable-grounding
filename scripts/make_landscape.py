"""Figure: evaluation-benchmark landscape -- which benchmarks test which modalities, outputs and conditions.

Usage: python3 -I make_landscape.py ../../../stage3/database/literature_db.jsonl fig_landscape.tex

Rows are evaluation benchmarks introduced by works in the coded corpus (curated list below: benchmarks
with a localisation output; training-only corpora and answer-only hallucination benchmarks are left
out). Each dot is read from the facet coding of the introducing work (facets A, B, D, G), so the
conditions are those the introducing paper defines or evaluates.
"""
import json
import sys

GROUPS = [
    ("Image", [
        ("kazemzadeh2014referitgame", "ReferItGame"), ("yu2016modeling", "RefCOCO, RefCOCO+"),
        ("plummer2017flickr30k", "Flickr30k Entities"), ("liu2019clevrref", "CLEVR-Ref+"), ("chen2020copsref", "Cops-Ref"),
        ("chen2021yourefit", "YouRefIt"), ("gupta2022grit", "GRIT"), ("liu2023gres", "gRefCOCO"), ("hu2023beyond", "Ref-ZOM"),
        ("xie2023described", "D$^3$"), ("lai2024lisa", "ReasonSeg"), ("zhang2024persam", "PerSeg"), ("li2024r2bench", "R$^2$-Bench"),
        ("chen2025refl4", "Ref-L4"), ("li2025counterfactual", "HalluSegBench"), ("zhang2026exposing", "GUI-HalluBench"),
        ("wu2026gcot", "MM-GCoT")]),
    ("Video", [
        ("gao2017tall", "Charades-STA"), ("hendricks2017didemo", "DiDeMo"), ("lei2021detecting", "QVHighlights"),
        ("grauman2022ego4d", "Ego4D NLQ"), ("lan2023closer", "Charades-CD"), ("flanagan2025moment", "Charades-STA negatives"),
        ("xiao2024can", "NExT-GQA"), ("chen2024rextime", "ReXTime"), ("chen2025cgbench", "CG-Bench"), ("cheng2026vstar", "V-STaR"), ("meng2026videozerobench", "VideoZeroBench"), ("dang2026distinguishing", "Dang et al. (2026)"),
        ("zhang2020vidstg", "VidSTG"), ("tang2022hcstvg", "HC-STVG"), ("gavrilyuk2018actor", "A2D Sentences"),
        ("seo2020urvos", "Refer-YouTube-VOS"), ("ding2023mevis", "MeViS"), ("ding2025mevistpami", "MeViSv2"),
        ("yan2024visa", "ReVOS"), ("li2023robust", "R$^2$-VOS negatives"), ("kurita2023refego", "RefEgo"),
        ("wu2023rmot", "Refer-KITTI"), ("ji2024described", "DVD-ST")]),
    ("Audio and audio-visual", [
        ("chen2021localizing", "VGG-SS"), ("mo2022closer", "Ext.\\ Flickr/VGG-SS"), ("zhou2022avs", "AVSBench-object"),
        ("zhou2025avss", "AVSBench-semantic"), ("li2026avsbenchrobust", "AVSBench-Robust"), ("wang2024refavs", "Ref-AVS"),
        ("ying2025omniavs", "OmniAVS"), ("tian2018ave", "AVE"), ("geng2023dense", "UnAV-100"), ("geng2025longvale", "LongVALE"),
        ("choi2025avatar", "AVATAR"), ("hu2026evaomni", "EvaOmni"), ("wei2026videoholmesv2", "Video-HolmesV2"),
        ("julin2026anchor", "ANCHOR"), ("zhang2026avtrace", "AVTrace"), ("chen2026avid", "AVID"), ("xu2021texttoaudio", "AudioGrounding"), ("munakata2025language", "Clotho-Moment")]),
    ("3D, other sensors and domains", [
        ("chen2020scanrefer", "ScanRefer"), ("achlioptas2020referit3d", "Nr3D, Sr3D"), ("liu2021referitinrgbd", "SUNRefer"),
        ("mauceri2019sunspot", "SUN-Spot"), ("zhang2023multi3drefer", "Multi3DRefer"), ("wu2024threedgres", "Multi3DRes"),
        ("wang2024embodiedscan", "EmbodiedScan"), ("zhu2024scanreason", "ScanReason"), ("huang2025beacon3d", "Beacon3D"),
        ("wang2025vigil3d", "ViGiL3D"), ("zhao2023toward", "FE-3DGQA"), ("yang2025threedgrand", "3D-GRAND"), ("he2025refersplat", "Ref-LERF"),
        ("miyanishi2023cityrefer", "CityRefer"), ("zhan2024mono3dvg", "Mono3DRefer"), ("deruyttere2019talk2car", "Talk2Car"),
        ("wu2025language", "NuPrompt"), ("choudhary2024talk2bev", "Talk2BEV-Bench"), ("lin2024wildrefer", "STRefer"),
        ("guan2025talk2radar", "Talk2Radar"), ("zhao2026rgbtgroundbench", "RGBT-GroundBench"), ("sun2022rsvg", "RSVG"),
        ("zhan2023rsvg", "DIOR-RSVG"), ("yuan2024rrsis", "RefSegRS"), ("liu2024rotated", "RRSIS-D"),
        ("boecking2022biovil", "MS-CXR"), ("zhang2026medgrounder", "GMPG-ImaGenome")]),
]
COLS = [  # (group, colour, [(label, test)])
    ("Query", "cText", [
        ("text", lambda r: bool({"referring expression", "implicit instruction", "phrase/class name"} & r["A"])),
        ("speech", lambda r: "speech" in r["A"]),
        ("sound", lambda r: "non-speech sound" in r["A"]),
        ("visual", lambda r: bool({"visual exemplar", "visual prompt", "gesture/gaze"} & r["A"]))]),
    ("Target", "cVis", [
        ("image", lambda r: "image" in r["B"]),
        ("video", lambda r: "silent video" in r["B"]),
        ("AV video", lambda r: "audio-visual video" in r["B"]),
        ("audio", lambda r: "audio-only" in r["B"]),
        ("3D", lambda r: bool({"point cloud", "rgb-d", "radiance field/3dgs"} & r["B"])),
        ("sensor/domain", lambda r: bool({"lidar/radar/thermal", "remote sensing", "medical"} & r["B"]))]),
    ("Output", "cInk", [
        ("point/map", lambda r: "point/heatmap" in r["D"]),
        ("box", lambda r: bool({"2d box", "rotated box"} & r["D"])),
        ("mask", lambda r: "mask" in r["D"]),
        ("interval", lambda r: "temporal interval" in r["D"]),
        ("tube/track", lambda r: "tube/track" in r["D"]),
        ("3D region", lambda r: bool({"3d box", "3d mask"} & r["D"]))]),
    ("Condition tested", "cRel", [
        ("absent target", lambda r: "absent target/false premise" in r["G"]),
        ("multi-target", lambda r: "multi-target" in r["G"]),
        ("ambiguity", lambda r: "ambiguity/distractors" in r["G"]),
        ("novel", lambda r: "novel categories/compositions" in r["G"]),
        ("domain shift", lambda r: "domain/sensor shift" in r["G"]),
        ("missing mod.", lambda r: "missing modality" in r["G"]),
        ("degraded", lambda r: "degraded/noisy modality" in r["G"]),
        ("conflicting", lambda r: "conflicting modalities" in r["G"]),
        ("adversarial", lambda r: "adversarial" in r["G"]),
        ("long horizon", lambda r: "long-horizon drift" in r["G"])]),
]
DX, DY = 0.205, 0.245      # cm per column / row
LABEL_W = 2.12             # row-label width (cm)
GAPG = 0.12                # gap between column groups (cm)


def main():
    db = {}
    for line in open(sys.argv[1]):
        r = json.loads(line)
        db[r["key"]] = {"A": {x.lower() for x in r["A_query"]}, "B": {x.lower() for x in r["B_target"]},
                        "D": {x.lower() for x in r["D_output"]}, "G": {x.lower() for x in r["G_conditions"]},
                        "status": r["status"]}
    missing = [k for _, rows in GROUPS for k, _ in rows if k not in db]
    assert not missing, missing
    # column x positions (relative to the start of the dot area)
    xs, x = [], 0.0
    for gi, (g, col, cols) in enumerate(COLS):
        for c in cols:
            xs.append((gi, x))
            x += DX
        x += GAPG
    dot_w = x - GAPG
    half_w = LABEL_W + dot_w
    halves = [GROUPS[:2], GROUPS[2:]]
    out = [r"\documentclass[tikz,border=2pt]{standalone}", r"\input{figstyle}", r"\begin{document}",
           r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    flat = [c for _, _, cols in COLS for c in cols]
    colours = [col for _, col, cols in COLS for _ in cols]
    n_rows = {}
    for h, groups in enumerate(halves):
        x0 = h * (half_w + 0.22)
        # header: group names and rotated column labels
        for gi, (g, col, cols) in enumerate(COLS):
            gx = [xx for (gg, xx) in xs if gg == gi]
            out.append(f"\\draw[{col}, line width=1.4pt] ({x0 + LABEL_W + gx[0] - 0.08:.3f},2.05) -- ({x0 + LABEL_W + gx[-1] + 0.08:.3f},2.05);")
            out.append(f"\\node[anchor=south, font=\\fontsize{{6.6}}{{7.6}}\\selectfont\\bfseries, text={col}] at ({x0 + LABEL_W + (gx[0] + gx[-1]) / 2:.3f},2.08) {{{g}}};")
        for (gi, xx), (lab, _), col in zip(xs, flat, colours):
            out.append(f"\\node[anchor=west, rotate=90, inner sep=0pt, font=\\fontsize{{6.1}}{{7}}\\selectfont] at ({x0 + LABEL_W + xx:.3f},0.12) {{{lab}}};")
        y = 0.0
        for gname, rows in groups:
            y -= 0.22
            out.append(f"\\node[anchor=west, font=\\fontsize{{6.8}}{{8}}\\selectfont\\bfseries] at ({x0:.3f},{y:.3f}) {{{gname}}};")
            out.append(f"\\draw[cMid, line width=0.4pt] ({x0:.3f},{y - 0.13:.3f}) -- ({x0 + half_w:.3f},{y - 0.13:.3f});")
            y -= 0.08
            for k, (key, name) in enumerate(rows):
                y -= DY
                r = db[key]
                if k % 2 == 0:
                    out.append(f"\\fill[cLight!70] ({x0:.3f},{y - DY / 2:.3f}) rectangle ({x0 + half_w:.3f},{y + DY / 2:.3f});")
                dag = "$^\\dagger$" if r["status"] != "peer-reviewed" else ""
                out.append(f"\\node[anchor=west, inner sep=0pt, font=\\fontsize{{6.2}}{{7}}\\selectfont] at ({x0 + 0.05:.3f},{y:.3f}) {{{name}{dag}}};")
                for (gi, xx), (lab, test), col in zip(xs, flat, colours):
                    if test(r):
                        out.append(f"\\fill[{col}] ({x0 + LABEL_W + xx:.3f},{y:.3f}) circle (0.072);")
                    else:
                        out.append(f"\\fill[cMid!80] ({x0 + LABEL_W + xx:.3f},{y:.3f}) circle (0.018);")
            y -= 0.06
        n_rows[h] = y
    ybot = min(n_rows.values())
    out.append(f"\\node[anchor=north west, align=left, text width=15.4cm, font=\\fontsize{{6.2}}{{7.4}}\\selectfont, text=cGrey] at (0,{ybot - 0.05:.3f}) "
               "{Each row is an evaluation benchmark introduced by a work in the coded corpus; dots are read from that work's facet coding "
               "(query A, target B, output D, condition G). $^\\dagger$Introduced in a preprint or workshop paper.};")
    out += [r"\end{tikzpicture}", r"\end{document}"]
    open(sys.argv[2], "w").write("\n".join(out) + "\n")
    n = sum(len(rows) for _, rows in GROUPS)
    print(f"wrote {sys.argv[2]}: {n} benchmarks")


if __name__ == "__main__":
    main()
