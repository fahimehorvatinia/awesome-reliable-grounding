"""Generate fig_taxonomy.tex: the eight-facet taxonomy with the number of coded works per value.

Usage: python3 -I make_taxonomy.py ../../../stage2/database/literature_db.jsonl fig_taxonomy.tex

Counts are computed from the facet coding of the literature database (multi-label facets: a work
counts once for every value it carries; facet E is single-label). Values with zero coded works are
kept and shown as 0, so the figure also shows where the corpus is empty.
"""
import json
import sys
from collections import Counter

FACETS = [  # (field, letter, title, colour, [(value as coded, display label)])
    ("A_query", "A", "Query modality", "cText", [
        ("referring expression", "referring expression"), ("implicit instruction", "implicit instruction"),
        ("phrase/class name", "phrase / class name"), ("non-speech sound", "non-speech sound"),
        ("visual prompt", "visual prompt"), ("visual exemplar", "visual exemplar"), ("speech", "speech"),
        ("composite", "composite (joint)"), ("gesture/gaze", "gesture / gaze")]),
    ("B_target", "B", "Target context", "cVis", [
        ("image", "image"), ("silent video", "silent video"), ("audio-visual video", "audio-visual video"),
        ("point cloud", "point cloud / mesh"), ("rgb-d", "RGB-D"), ("remote sensing", "remote sensing"),
        ("audio-only", "audio only"), ("medical", "medical"), ("radiance field/3dgs", "radiance field / 3DGS"),
        ("lidar/radar/thermal", "LiDAR / radar / thermal")]),
    ("C_referent", "C", "Referent type", "c3D", [
        ("object instance", "object instance"), ("event/action", "event / action"), ("set (0..k)", "set of 0..K referents"),
        ("sound source", "sound source"), ("stuff/region", "stuff / region"), ("part", "part"),
        ("relation/interaction", "relation / interaction"), ("affordance", "affordance")]),
    ("D_output", "D", "Output representation", "cInk", [
        ("mask", "mask"), ("2d box", "2D box"), ("grounded text", "grounded text"),
        ("temporal interval", "temporal interval"), ("point/heatmap", "point / heatmap"), ("3d box", "3D box"),
        ("tube/track", "tube / track"), ("3d mask", "3D mask"), ("rotated box", "rotated box")]),
    ("E_paradigm", "E", "Architecture paradigm", "cInk", [
        ("E1", "E1 proposal-and-rank"), ("E2", "E2 one-stage dense fusion"), ("E3", "E3 query-based set pred."),
        ("E4", "E4 open-set pre-training"), ("E5", "E5 promptable seg.\\ + adapter"), ("E6", "E6 MLLM coords-as-text"),
        ("E7", "E7 MLLM embedding-as-mask"), ("E8", "E8 agentic / RL reasoning"), ("E9", "E9 training-free comp.")]),
    ("F_supervision", "F", "Supervision", "cInk", [
        ("full", "full"), ("synthetic/llm-generated", "synthetic / LLM-generated"),
        ("zero-shot/training-free", "zero-shot / training-free"), ("weak", "weak"),
        ("self-supervised correspondence", "self-sup.\\ correspondence"), ("rl verifiable reward", "RL, verifiable reward"),
        ("semi-supervised", "semi-supervised")]),
    ("G_conditions", "G", "Reliability condition", "cRel", [
        ("nominal", "nominal only"), ("ambiguity/distractors", "ambiguity / distractors"),
        ("absent target/false premise", "absent target / false premise"), ("multi-target", "multi-target"),
        ("novel categories/compositions", "novel categories / comp."), ("missing modality", "missing modality"),
        ("domain/sensor shift", "domain / sensor shift"), ("degraded/noisy modality", "degraded / noisy modality"),
        ("conflicting modalities", "conflicting modalities"), ("long-horizon drift", "long-horizon drift"),
        ("adversarial", "adversarial")]),
    ("H_verification", "H", "Verification mechanism", "cRel", [
        ("none", "none"), ("existence/abstention head", "existence / abstention head"),
        ("traceable evidence", "traceable evidence"), ("calibrated confidence", "confidence / uncertainty"),
        ("self-verification/re-grounding", "self-verification, re-grounding"),
        ("temporal/cross-view consistency", "temporal / cross-view consist."), ("cycle/reg consistency", "cycle / REG consistency"),
        ("interactive clarification", "interactive clarification"), ("external verifier", "external verifier")]),
]
CW, GAP = 4.32, 0.16       # facet box width and gap (cm)
ROW = 0.268                 # row height (cm)
LABEL_W = 2.98              # label column width (cm)
BAR_MAX = 0.78              # longest bar in a facet (cm)


def count(recs):
    out = {}
    for field, *_ in FACETS:
        c = Counter()
        for r in recs:
            v = r.get(field)
            vals = [v] if isinstance(v, str) else (v or [])
            for x in vals:
                x = x.strip().lower()
                if field == "E_paradigm":
                    x = x.split()[0].upper() if x[:1] == "e" and x[1:2].isdigit() else x
                c[x] += 1
        out[field] = c
    return out


def main():
    recs = [json.loads(line) for line in open(sys.argv[1])]
    counts = count(recs)
    n_methods = sum(1 for r in recs if r["E_paradigm"].split()[0] not in ("dataset", "analysis"))
    out = [r"\documentclass[tikz,border=2pt]{standalone}", r"\input{figstyle}", r"\begin{document}",
           r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    heights = [max(len(FACETS[i][4]), len(FACETS[i + 4][4] if i + 4 < 8 else [])) for i in range(4)]
    row_h = [max(len(f[4]) for f in FACETS[:4]) * ROW + 0.62, max(len(f[4]) for f in FACETS[4:]) * ROW + 0.62]
    for i, (field, letter, title, col, values) in enumerate(FACETS):
        x0 = (i % 4) * (CW + GAP)
        y0 = 0 if i < 4 else -(row_h[0] + 0.22)
        h = row_h[i // 4]
        out.append(f"\\node[anchor=north west, draw={col}, line width=0.8pt, rounded corners=3pt, fill={col}!5, "
                   f"minimum width={CW}cm, minimum height={h:.3f}cm, inner sep=0pt] (f{i}) at ({x0:.3f},{y0:.3f}) {{}};")
        out.append(f"\\node[anchor=north west, fill={col}, text=white, rounded corners=2pt, "
                   f"font=\\fontsize{{8.5}}{{10}}\\selectfont\\bfseries, inner xsep=4pt, inner ysep=2pt] "
                   f"at ($(f{i}.north west)+(0.08,-0.08)$) {{{letter}}};")
        out.append(f"\\node[anchor=north west, font=\\fontsize{{8.5}}{{10}}\\selectfont\\bfseries, text={col}] "
                   f"at ($(f{i}.north west)+(0.48,-0.07)$) {{{title}}};")
        c = counts[field]
        top = max([c.get(v, 0) for v, _ in values] + [1])
        for k, (v, label) in enumerate(values):
            n = c.get(v, 0)
            yy = y0 - 0.56 - k * ROW
            out.append(f"\\node[anchor=west, inner sep=0pt, font=\\fontsize{{6.6}}{{7.6}}\\selectfont] "
                       f"at ({x0 + 0.12:.3f},{yy:.3f}) {{{label}}};")
            bx = x0 + 0.12 + LABEL_W
            w = BAR_MAX * n / top
            if n:
                out.append(f"\\fill[{col}!{70 if col != 'cInk' else 55}] ({bx:.3f},{yy - 0.075:.3f}) rectangle ({bx + w:.3f},{yy + 0.075:.3f});")
            out.append(f"\\node[anchor=west, inner sep=0pt, font=\\fontsize{{6.4}}{{7.4}}\\selectfont, text={'cInk' if n else 'cGrey'}] "
                       f"at ({bx + w + 0.06:.3f},{yy:.3f}) {{{n}}};")
        if field == "E_paradigm":
            out.append(f"\\node[anchor=south west, inner sep=0pt, align=left, text width={CW - 0.3:.2f}cm, font=\\fontsize{{6.2}}{{7.2}}\\selectfont, text=cGrey] "
                       f"at ($(f{i}.south west)+(0.12,0.08)$) {{{n_methods} method papers; the other {c['dataset']} dataset and {c['analysis']} analysis papers carry no paradigm}};")
    for i in (6, 7):
        out.append(f"\\node[chip, fill=cRel, text=white, font=\\fontsize{{6.8}}{{8}}\\selectfont\\bfseries] "
                   f"at ($(f{i}.north east)+(-0.42,0)$) {{new}};")
    out.append(f"\\node[anchor=north west, font=\\fontsize{{6.6}}{{7.6}}\\selectfont, text=cGrey] at (0,{-(row_h[0] + 0.22 + row_h[1]) - 0.08:.3f}) "
               f"{{Numbers: works among the {len(recs)} coded works that carry each value (facets A--D and F--H are multi-label, E is single-label). Bars are scaled within each facet.}};")
    out += [r"\end{tikzpicture}", r"\end{document}"]
    open(sys.argv[2], "w").write("\n".join(out) + "\n")
    print(f"wrote {sys.argv[2]} from {len(recs)} records")


if __name__ == "__main__":
    main()
