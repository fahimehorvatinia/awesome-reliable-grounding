"""Figure 2b (single-panel version): publication trends of all task families on one chart.

Usage: python3 -I make_trends_single.py data/trend_counts.csv ../fig_trends_single.pdf data/reliability_curated.csv

Same data as make_trends.py. All series share one logarithmic y-axis (linear between 0 and 1, so
years with zero records stay visible), because the families differ by more than an order of
magnitude in volume. Each family keeps its colour from the shared palette. The reliability series
counts curated, verified works from the literature database rather than keyword hits, so it is drawn
dashed with square markers to mark the different counting method.
"""
import csv
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator

matplotlib.rcParams.update({
    "font.family": "Nimbus Sans", "font.size": 7.5, "pdf.fonttype": 42,
    "axes.edgecolor": "#8C8C8C", "axes.linewidth": 0.6, "axes.labelcolor": "#222222",
    "xtick.color": "#555555", "ytick.color": "#555555", "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "xtick.major.size": 2.5, "ytick.major.size": 2.5,
})
INK, MUTED, GRID = "#222222", "#6B6B6B", "#E3E3E3"
SERIES = [  # (family, label, colour) -- colours follow the shared figure palette (Okabe-Ito)
    ("image", "Image grounding", "#009E73"),
    ("video", "Video grounding", "#0072B2"),
    ("3d", "3D grounding", "#CC79A7"),
    ("audiovisual", "Audio-visual grounding", "#E69F00"),
    ("curated", "Reliability & interpretability (curated)", "#D55E00"),
]


def spread(ys, gap):
    """Push label positions apart (in axis units) so that neighbours are at least `gap` apart."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    pos = [ys[i] for i in order]
    for _ in range(50):
        moved = False
        for j in range(1, len(pos)):
            if pos[j] - pos[j - 1] < gap:
                mid = (pos[j] + pos[j - 1]) / 2
                pos[j - 1], pos[j] = mid - gap / 2, mid + gap / 2
                moved = True
        if not moved:
            break
    out = [0.0] * len(ys)
    for k, i in enumerate(order):
        out[i] = pos[k]
    return out


def main():
    data, prec = {}, {}
    for r in csv.DictReader(open(sys.argv[1])):
        data.setdefault(r["family"], {})[int(r["year"])] = int(r["total"])
        prec[r["family"]] = int(r["precision_sample_relevant"]) / int(r["precision_sample_n"])
    data["curated"] = {int(r["year"]): int(r["count"]) for r in csv.DictReader(open(sys.argv[3]))}

    fig, ax = plt.subplots(figsize=(7.0, 2.45))
    ax.set_yscale("symlog", linthresh=1, linscale=0.35)
    ends = []
    for fam, label, col in SERIES:
        s = data[fam]
        years = sorted(y for y in s if y < 2026)
        dashed = fam == "curated"
        ax.plot(years, [s[y] for y in years], color=col, lw=1.6, ls=(0, (4, 1.6)) if dashed else "-",
                marker="s" if dashed else "o", ms=3.0, zorder=3, label=label)
        ax.plot([2025, 2026], [s[2025], s[2026]], color=col, lw=1.2, ls=(0, (1.2, 1.2)), zorder=3)
        ax.plot([2026], [s[2026]], marker="s" if dashed else "o", ms=3.6, mfc="white", mec=col, mew=1.1, zorder=4)
        ends.append((fam, label, col, s[2025], s[2026]))

    ax.set_xlim(2013.6, 2026.4)
    ax.set_ylim(0, 2600)
    ax.set_xticks(range(2014, 2027))
    ax.tick_params(axis="x", labelsize=6.8)
    ax.yaxis.set_major_locator(FixedLocator([0, 1, 10, 100, 1000]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_yticklabels(["0", "1", "10", "100", "1000"])
    ax.set_ylabel("papers per year (log scale)", color=INK)
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)

    # Direct labels at the right end of each line, de-collided in display space.
    fig.canvas.draw()
    to_ax = ax.transAxes.inverted()
    ys = [to_ax.transform(ax.transData.transform((2026, e[4])))[1] for e in ends]
    ys = spread(ys, 0.085)
    for (fam, label, col, v25, v26), y in zip(ends, ys):
        anchor = to_ax.transform(ax.transData.transform((2026, v26)))
        short = label.replace(" (curated)", "")
        note = "" if fam == "curated" else f", precision {prec[fam]:.2f}"
        ax.annotate(f"{short}: {v25} in 2025{note}", xy=(anchor[0] + 0.012, anchor[1]), xycoords="axes fraction",
                    xytext=(anchor[0] + 0.062, y), textcoords="axes fraction", va="center", ha="left",
                    fontsize=6.8, color=INK,
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.7, shrinkA=0, shrinkB=0))
        ax.plot([anchor[0] + 0.05], [y], marker="s" if fam == "curated" else "o", ms=3.2, color=col,
                transform=ax.transAxes, clip_on=False, zorder=5)

    ax.legend(loc="upper left", ncol=3, frameon=False, fontsize=6.8, handlelength=2.4, columnspacing=1.4,
              borderaxespad=0.2)
    fig.subplots_adjust(left=0.075, right=0.68, top=0.97, bottom=0.11)
    fig.savefig(sys.argv[2])
    print("wrote", sys.argv[2])


if __name__ == "__main__":
    main()
