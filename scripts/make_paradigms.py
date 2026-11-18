"""Figure: evolution of grounding architectures -- share of method papers per paradigm (E1-E9) by period.

Usage: python3 -I make_paradigms.py ../../../stage3/database/literature_db.jsonl ../fig_paradigms.pdf

Counts are method papers (E1-E9) in the coded corpus, by year of the cited version. Paradigms are
coloured by family (four hues, validated for colour-vision deficiency); members of a family are told
apart by texture (solid, hatched, dotted) and by direct labels inside large segments.
"""
import json
import sys
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

matplotlib.rcParams.update({
    "font.family": "Nimbus Sans", "font.size": 7.5, "pdf.fonttype": 42, "hatch.linewidth": 0.7,
    "axes.edgecolor": "#8C8C8C", "axes.linewidth": 0.6, "xtick.color": "#555555", "ytick.color": "#555555",
    "xtick.major.size": 2.5, "ytick.major.size": 2.5,
})
INK, GRID = "#222222", "#E3E3E3"
FAMILIES = [  # (name, what it relieved, colour, members)
    ("Specialist models", "end-to-end training", "#0072B2",
     [("E1", "proposal-and-rank"), ("E2", "dense fusion"), ("E3", "query-based")]),
    ("Pre-trained, promptable", "vocabulary, masks", "#009E73",
     [("E4", "open-set pre-training"), ("E5", "SAM + adapter")]),
    ("MLLM interfaces", "implicit referents", "#E69F00",
     [("E6", "coords as text"), ("E7", "embedding-as-mask")]),
    ("Agentic, training-free", "supervision cost", "#CC79A7",
     [("E8", "agentic / RL-trained"), ("E9", "training-free")]),
]
HATCH = ["", "////", "...."]
PERIODS = [("2014–20", lambda y: y <= 2020), ("2021", lambda y: y == 2021), ("2022", lambda y: y == 2022),
           ("2023", lambda y: y == 2023), ("2024", lambda y: y == 2024), ("2025", lambda y: y == 2025),
           ("2026*", lambda y: y == 2026)]


def main():
    recs = [json.loads(l) for l in open(sys.argv[1])]
    counts = defaultdict(Counter)
    for r in recs:
        e = r["E_paradigm"].split()[0]
        if not (e.startswith("E") and e[1:].isdigit()):
            continue
        for name, test in PERIODS:
            if test(int(r["year"])):
                counts[name][e] += 1
    fig = plt.figure(figsize=(6.3, 2.45))
    ax = fig.add_axes([0.06, 0.13, 0.465, 0.78])
    x = list(range(len(PERIODS)))
    bottoms = [0.0] * len(PERIODS)
    totals = [sum(counts[p].values()) for p, _ in PERIODS]
    for fam, why, col, members in FAMILIES:
        for k, (e, _) in enumerate(members):
            vals = [100 * counts[p][e] / totals[i] for i, (p, _) in enumerate(PERIODS)]
            ax.bar(x, vals, bottom=bottoms, width=0.72, color=col, edgecolor="white", linewidth=0.8,
                   hatch=HATCH[k], zorder=3)
            for i, v in enumerate(vals):
                if v >= 7.5:
                    ax.text(i, bottoms[i] + v / 2, e, ha="center", va="center", fontsize=6.4, color="white",
                            fontweight="bold", zorder=4,
                            bbox=dict(boxstyle="round,pad=0.12", fc=col, ec="none") if HATCH[k] else None)
            bottoms = [b + v for b, v in zip(bottoms, vals)]
    for i, n in enumerate(totals):
        ax.text(i, 101.5, f"n={n}", ha="center", va="bottom", fontsize=6.6, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels([p for p, _ in PERIODS], fontsize=7)
    ax.set_ylim(0, 108)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["0", "25", "50", "75", "100%"])
    ax.set_ylabel("share of method papers", color=INK)
    ax.grid(axis="y", color=GRID, lw=0.5, zorder=0)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    # grouped legend on the right
    for fi, (fam, why, col, members) in enumerate(FAMILIES):
        if fi in (0, 2):
            lx, ly = (0.575 if fi == 0 else 0.79), 0.95
        fig.text(lx, ly, fam, fontsize=7.2, fontweight="bold", color=INK, va="top")
        fig.text(lx, ly - 0.072, f"relieved: {why}", fontsize=6.2, color="#555555", va="top", style="italic")
        ly -= 0.15
        for k, (e, label) in enumerate(members):
            fig.patches.append(matplotlib.patches.Rectangle((lx + 0.005, ly - 0.045), 0.022, 0.05, transform=fig.transFigure,
                                                            facecolor=col, edgecolor="white", hatch=HATCH[k], lw=0.5))
            fig.text(lx + 0.035, ly - 0.02, f"{e}  {label}", fontsize=6.5, color=INK, va="center")
            ly -= 0.064
        ly -= 0.035
    fig.text(0.065, 0.015, "*2026 partial (to 17 Nov.). Counts: method papers in the coded corpus (n = %d); the corpus is curated, so shares describe it, not the whole field." % sum(totals),
             fontsize=6.0, color="#6B6B6B")
    fig.savefig(sys.argv[2])
    print("wrote", sys.argv[2], totals)


if __name__ == "__main__":
    main()
