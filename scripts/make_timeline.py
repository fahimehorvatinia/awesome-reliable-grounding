"""Generate fig_timeline.tex from timeline.csv (verified first peer-reviewed years).

Usage: python3 -I make_timeline.py timeline.csv fig_timeline.tex

Labels are packed into rows per lane with a greedy interval scheduler so that no two
labels overlap; lane heights adapt to the number of rows needed.
"""
import csv
import sys

LANES = [
    ("image", "Image", "cVis"),
    ("video", "Video \\& temporal", "cText"),
    ("av", "Audio-visual", "cAudio"),
    ("3d", "3D, spatial \\& sensors", "c3D"),
    ("rel", "Reliability \\& interpretability", "cRel"),
]
Y0, Y1 = 2014, 2026
X_LEFT, X_RIGHT = 2.35, 17.2          # cm
CHAR_W = 0.112                        # cm per character at 6.6 pt (conservative)
ROW_H = 0.34
MARK = {"d": "rectangle", "m": "circle", "r": "diamond"}


def xpos(year):
    return X_LEFT + (year - Y0 + 0.5) * (X_RIGHT - X_LEFT) / (Y1 - Y0 + 1)


def build(rows):
    """Return (tikz lines, y of the year axis, y of the legend row) for the milestone panel."""
    out = []
    y = 0.0
    lane_bounds = []
    for key, name, col in LANES:
        items = sorted([r for r in rows if r["lane"] == key], key=lambda r: (int(r["year"]), r["label"]))
        row_end = []  # x where each row becomes free
        placed = []
        for it in items:
            x = xpos(int(it["year"]))
            start = x - 0.09
            end = x + 0.14 + CHAR_W * len(it["label"])
            for ri, free in enumerate(row_end):
                if start > free + 0.05:
                    row_end[ri] = end
                    break
            else:
                ri = len(row_end)
                row_end.append(end)
            placed.append((it, x, ri))
        nrows = max(1, len(row_end))
        height = nrows * ROW_H + 0.22
        top = y
        bottom = y - height
        lane_bounds.append((name, col, top, bottom))
        for it, x, ri in placed:
            yy = top - 0.24 - ri * ROW_H
            shape = MARK[it["kind"]]
            size = "minimum size=0.17cm" if shape != "diamond" else "minimum size=0.22cm"
            out.append(
                f"\\node[{shape}, draw={col}, fill={col}{'!35' if it['kind'] == 'd' else ''}, line width=0.5pt, inner sep=0pt, {size}] at ({x:.3f},{yy:.3f}) {{}};")
            label = it["label"].replace("&", "\\&")
            out.append(f"\\node[anchor=west, inner sep=0pt, font=\\fontsize{{6.6}}{{7.6}}\\selectfont] at ({x + 0.12:.3f},{yy:.3f}) {{{label}}};")
        y = bottom - 0.12
    # lane backgrounds and names (drawn on background layer)
    out.append(r"\begin{scope}[on background layer]")
    for i, (name, col, top, bottom) in enumerate(lane_bounds):
        out.append(f"\\fill[{col}!{6 if i % 2 == 0 else 10}] (0,{top:.3f}) rectangle ({X_RIGHT + 0.6:.3f},{bottom:.3f});")
        out.append(f"\\node[anchor=west, align=left, text width=2.1cm, font=\\fontsize{{7.5}}{{8.8}}\\selectfont\\bfseries, text={col}] at (0.1,{(top + bottom) / 2:.3f}) {{{name}}};")
    for yr in range(Y0, Y1 + 1):
        x = xpos(yr)
        out.append(f"\\draw[cMid, line width=0.3pt] ({x:.3f},{lane_bounds[0][2]:.3f}) -- ({x:.3f},{lane_bounds[-1][3]:.3f});")
    out.append(r"\end{scope}")
    ybase = lane_bounds[-1][3]
    out.append(f"\\draw[line width=0.6pt] ({X_LEFT:.3f},{ybase - 0.05:.3f}) -- ({X_RIGHT + 0.6:.3f},{ybase - 0.05:.3f});")
    for yr in range(Y0, Y1 + 1):
        x = xpos(yr)
        out.append(f"\\node[font=\\fontsize{{7}}{{8}}\\selectfont, anchor=north] at ({x:.3f},{ybase - 0.08:.3f}) {{{yr}}};")
    # legend
    ly = ybase - 0.62
    out.append(f"\\node[rectangle, draw=cInk, fill=cInk!35, minimum size=0.17cm, inner sep=0pt] at (2.5,{ly:.3f}) {{}}; \\node[small, anchor=west] at (2.65,{ly:.3f}) {{dataset / benchmark}};")
    out.append(f"\\node[circle, draw=cInk, fill=cInk, minimum size=0.17cm, inner sep=0pt] at (5.4,{ly:.3f}) {{}}; \\node[small, anchor=west] at (5.55,{ly:.3f}) {{method / model}};")
    out.append(f"\\node[diamond, draw=cRel, fill=cRel, minimum size=0.22cm, inner sep=0pt] at (8.0,{ly:.3f}) {{}}; \\node[small, anchor=west] at (8.15,{ly:.3f}) {{reliability or interpretability study}};")
    out.append(f"\\node[small, anchor=west, text=cGrey] at (12.2,{ly:.3f}) {{year = first peer-reviewed publication}};")
    return out, ybase, ly


def main():
    rows = list(csv.DictReader(open(sys.argv[1])))
    body, _, _ = build(rows)
    out = [r"\documentclass[tikz,border=2pt]{standalone}", r"\input{figstyle}", r"\begin{document}",
           r"\begin{tikzpicture}[x=1cm,y=1cm]"] + body
    out += [r"\end{tikzpicture}", r"\end{document}"]
    open(sys.argv[2], "w").write("\n".join(out) + "\n")
    print(f"wrote {sys.argv[2]} with {len(rows)} milestones")


if __name__ == "__main__":
    main()
