"""Figure 2 as one image: (a) verified milestones above (b) publication trends of all task families.

Usage: python3 -I make_evolution.py timeline.csv data/trend_counts_used.csv data/reliability_curated.csv fig_evolution.tex

Both panels are drawn in one TikZ picture and share the year axis of make_timeline.py, so a year in
panel (b) sits directly below the same year in panel (a). Panel (b) puts every task family on one
logarithmic y-axis (linear between 0 and 1, so years with no records stay visible), each family in its
own colour from the shared palette. The reliability series counts curated, verified works from the
literature database instead of keyword hits, so it is drawn dashed with square markers.
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_timeline import X_LEFT, X_RIGHT, Y0, Y1, build, xpos  # noqa: E402

SERIES = [  # (family, legend label, colour macro from figstyle.tex)
    ("image", "Image grounding", "cVis"),
    ("video", "Video \\& temporal grounding", "cText"),
    ("3d", "3D grounding", "c3D"),
    ("audiovisual", "Audio-visual grounding", "cAudio"),
    ("curated", "Reliability \\& interpretability (curated)", "cRel"),
]
H = 4.0            # plot height (cm)
LIN = 0.42         # height of the linear 0..1 segment (cm)
TOP = 1000         # top tick
DEC = (H - 0.25 - LIN) / math.log10(TOP)


def ymap(v):
    return v * LIN if v <= 1 else LIN + math.log10(v) * DEC


def main():
    rows = list(csv.DictReader(open(sys.argv[1])))
    data, prec = {}, {}
    for r in csv.DictReader(open(sys.argv[2])):
        data.setdefault(r["family"], {})[int(r["year"])] = int(r["total"])
        prec[r["family"]] = int(r["precision_sample_relevant"]) / int(r["precision_sample_n"])
    data["curated"] = {int(r["year"]): int(r["count"]) for r in csv.DictReader(open(sys.argv[3]))}

    body, ybase, ly = build(rows)
    out = [r"\documentclass[tikz,border=2pt]{standalone}", r"\input{figstyle}", r"\begin{document}",
           r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    out.append(r"\node[title, anchor=south west, inner sep=0pt] at (0,0.12) {(a) Milestones by modality family};")
    out += body

    # ---- panel (b) ----
    title_y = ly - 0.62
    out.append(f"\\node[title, anchor=south west, inner sep=0pt] at (0,{title_y:.3f}) "
               "{(b) Publication trends: all task families on one logarithmic axis};")
    y0 = title_y - 0.35 - H          # data baseline (value 0)
    xr = X_RIGHT + 0.6

    def Y(v):
        return y0 + ymap(v)

    # grid, year guides, axes
    out.append(r"\begin{scope}[on background layer]")
    for yr in range(Y0, Y1 + 1):
        out.append(f"\\draw[cMid!60, line width=0.3pt] ({xpos(yr):.3f},{y0:.3f}) -- ({xpos(yr):.3f},{y0 + H:.3f});")
    for t in (1, 10, 100, 1000):
        out.append(f"\\draw[cMid, line width=0.4pt] ({X_LEFT:.3f},{Y(t):.3f}) -- ({xr:.3f},{Y(t):.3f});")
    out.append(r"\end{scope}")
    out.append(f"\\draw[line width=0.6pt] ({X_LEFT:.3f},{y0 - 0.05:.3f}) -- ({xr:.3f},{y0 - 0.05:.3f});")
    out.append(f"\\draw[line width=0.6pt, cGrey] ({X_LEFT:.3f},{y0 - 0.05:.3f}) -- ({X_LEFT:.3f},{y0 + H:.3f});")
    for t, lab in ((0, "0"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")):
        out.append(f"\\draw[cGrey, line width=0.5pt] ({X_LEFT - 0.06:.3f},{Y(t):.3f}) -- ({X_LEFT:.3f},{Y(t):.3f});")
        out.append(f"\\node[anchor=east, inner sep=1pt, font=\\fontsize{{7}}{{8}}\\selectfont] at ({X_LEFT - 0.08:.3f},{Y(t):.3f}) {{{lab}}};")
    out.append(f"\\node[rotate=90, font=\\fontsize{{7.5}}{{8.8}}\\selectfont, align=center] at (1.25,{y0 + H / 2:.3f}) "
               "{papers per year\\\\(log scale)};")
    for yr in range(Y0, Y1 + 1):
        lab = f"{yr}" if yr < 2026 else "2026$^{\\ast}$"
        out.append(f"\\node[font=\\fontsize{{7}}{{8}}\\selectfont, anchor=north] at ({xpos(yr):.3f},{y0 - 0.08:.3f}) {{{lab}}};")

    # series
    for fam, label, col in SERIES:
        s = data[fam]
        dashed = fam == "curated"
        style = f"draw={col}, line width=1.25pt, line join=round" + (", dash pattern=on 3.2pt off 1.4pt" if dashed else "")
        full = [y for y in sorted(s) if y < 2026]
        pts = " -- ".join(f"({xpos(y):.3f},{Y(s[y]):.3f})" for y in full)
        out.append(f"\\draw[{style}] {pts};")
        out.append(f"\\draw[draw={col}, line width=1pt, dash pattern=on 1pt off 1.3pt] "
                   f"({xpos(2025):.3f},{Y(s[2025]):.3f}) -- ({xpos(2026):.3f},{Y(s[2026]):.3f});")
        shape = "rectangle, minimum size=0.13cm" if dashed else "circle, minimum size=0.14cm"
        for y in full:
            out.append(f"\\node[{shape}, fill={col}, draw=white, line width=0.35pt, inner sep=0pt] at ({xpos(y):.3f},{Y(s[y]):.3f}) {{}};")
        out.append(f"\\node[{shape}, fill=white, draw={col}, line width=0.8pt, inner sep=0pt] at ({xpos(2026):.3f},{Y(s[2026]):.3f}) {{}};")

    # legend (three rows below the year labels); 2025 = last complete year
    leg_y = y0 - 0.72
    cols_x = [2.45, 10.2]
    for i, (fam, label, col) in enumerate(SERIES):
        x = cols_x[i % 2]
        yy = leg_y - (i // 2) * 0.36
        dashed = fam == "curated"
        dash = ", dash pattern=on 3.2pt off 1.4pt" if dashed else ""
        shape = "rectangle, minimum size=0.13cm" if dashed else "circle, minimum size=0.14cm"
        note = f"2025: {data[fam][2025]}" + ("" if dashed else f"; precision {prec[fam]:.2f}")
        out.append(f"\\draw[draw={col}, line width=1.25pt{dash}] ({x:.3f},{yy:.3f}) -- ({x + 0.55:.3f},{yy:.3f});")
        out.append(f"\\node[{shape}, fill={col}, inner sep=0pt] at ({x + 0.275:.3f},{yy:.3f}) {{}};")
        out.append(f"\\node[small, anchor=west] at ({x + 0.65:.3f},{yy:.3f}) {{{label} \\textcolor{{cGrey}}{{({note})}}}};")
    out.append(f"\\node[small, anchor=west, text=cGrey] at ({cols_x[1] + 0.05:.3f},{leg_y - 0.72:.3f}) "
               "{$^{\\ast}$hollow markers: 2026 partial (to 17 Nov.)};")

    out += [r"\end{tikzpicture}", r"\end{document}"]
    open(sys.argv[4], "w").write("\n".join(out) + "\n")
    print(f"wrote {sys.argv[4]}")


if __name__ == "__main__":
    main()
