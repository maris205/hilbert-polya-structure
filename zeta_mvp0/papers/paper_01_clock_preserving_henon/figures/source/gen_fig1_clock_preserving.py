#!/usr/bin/env python3
"""Generate the analytic hero schematic."""

from __future__ import annotations

from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from paper_plot_style import COLORS, save_figure


def box(ax, x, y, width, height, edge, heading, formula, note):
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.015,rounding_size=0.02",
        facecolor="white",
        edgecolor=edge,
        linewidth=1.8,
    )
    ax.add_patch(patch)
    ax.text(x + width / 2, y + 0.74 * height, heading, ha="center", va="center", fontweight="bold")
    ax.text(x + width / 2, y + 0.47 * height, formula, ha="center", va="center", fontsize=10.5)
    ax.text(x + width / 2, y + 0.19 * height, note, ha="center", va="center", fontsize=8.2, color=COLORS["grey"])


def main() -> None:
    fig, ax = plt.subplots(figsize=(10.2, 3.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    width, height, y = 0.255, 0.52, 0.35
    xs = (0.035, 0.3725, 0.71)
    box(
        ax,
        xs[0],
        y,
        width,
        height,
        COLORS["blue"],
        "Radial exponential clock",
        r"$V_0(u)=2\pi e^{\pi|u|^2}$",
        r"$|\{\pi|u|^2<t\}|=t$",
    )
    box(
        ax,
        xs[1],
        y,
        width,
        height,
        COLORS["orange"],
        "Hénon configuration warp",
        r"$V_{a,n}(q)=V_0(\widetilde H_a^n(q))$",
        r"$\det D\widetilde H_a^n=1$ preserves sublevel area",
    )
    box(
        ax,
        xs[2],
        y,
        width,
        height,
        COLORS["green"],
        "Magnetic symmetry control",
        r"$\frac{1}{2}|-i\nabla-A_B|^2+V_{a,n}$",
        r"$p\mapsto p-A_B(q)$ preserves fiber area",
    )

    for left, right, color, label in (
        (xs[0] + width, xs[1], COLORS["orange"], "active geometry"),
        (xs[1] + width, xs[2], COLORS["green"], "TR breaking"),
    ):
        arrow = FancyArrowPatch(
            (left + 0.008, y + height / 2),
            (right - 0.008, y + height / 2),
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=1.4,
            color=color,
        )
        ax.add_patch(arrow)
        ax.text(
            (left + right) / 2,
            y + height + 0.035,
            label,
            ha="center",
            va="bottom",
            color=color,
            fontsize=8.2,
        )

    ax.text(
        0.5,
        0.205,
        r"Invariant mean clock: $\mathcal{N}_{\mathrm{cl}}(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}-\frac{E}{2\pi}+1$",
        ha="center",
        fontsize=11.2,
        fontweight="bold",
    )

    badges = (
        ("Q", "proved", COLORS["blue"]),
        ("W", "proved", COLORS["blue"]),
        (r"$S_{\mathrm{op}}$", "proved", COLORS["blue"]),
        (r"$S_{\mathrm{dyn}}$", "sampled", COLORS["orange"]),
        ("R", "finite window", COLORS["green"]),
        ("C", "admissible", COLORS["purple"]),
        ("P", "open", COLORS["vermillion"]),
        ("Z", "not tested", COLORS["grey"]),
    )
    start, gap = 0.065, 0.124
    for index, (gate, status, color) in enumerate(badges):
        x = start + index * gap
        ax.text(
            x,
            0.075,
            gate,
            ha="center",
            va="center",
            color="white",
            fontweight="bold",
            fontsize=9.0,
            bbox={"boxstyle": "round,pad=0.28", "facecolor": color, "edgecolor": color},
        )
        ax.text(x, 0.018, status, ha="center", va="center", fontsize=7.2, color=COLORS["grey"])

    save_figure(fig, "fig1_clock_preserving")


if __name__ == "__main__":
    main()
