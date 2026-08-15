#!/usr/bin/env python3
"""Generate Figure 3: effectivity, action kernels, and static inertia."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from figure_data import load_frozen_payload
from paper_plot_style import (
    BLACK,
    BLUE,
    GREEN,
    MID_GRAY,
    ORANGE,
    PALE_BLUE,
    PALE_GREEN,
    PALE_ORANGE,
    PALE_PURPLE,
    PALE_RED,
    PURPLE,
    VERMILLION,
    arrow,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig3_effectivity_counterexamples"


def build_figure():
    payload = load_frozen_payload()
    structural = payload["structural"]
    inertia_count = structural["static_inertia_sector_count"]
    source_supports = [item["support"] for item in structural["source_factors"]]
    kernel_order = structural["action_kernel_order"]

    fig = plt.figure(figsize=(7.2, 4.85), constrained_layout=False)
    grid = GridSpec(
        2,
        3,
        figure=fig,
        height_ratios=[1.10, 0.70],
        hspace=0.48,
        wspace=0.27,
        left=0.045,
        right=0.985,
        bottom=0.12,
        top=0.94,
    )

    # A: free regular orbit.
    ax_a = fig.add_subplot(grid[0, 0])
    clean_axis(ax_a)
    panel_label(ax_a, "A", "regular orbit")
    rounded_box(
        ax_a,
        0.04,
        0.68,
        0.92,
        0.20,
        r"$X=C/1$" + "\nfree and transitive",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        hatch="..",
        fontsize=7.2,
    )
    rounded_box(
        ax_a,
        0.06,
        0.39,
        0.88,
        0.19,
        r"action kernel $N=1$" + "\n"
        + r"labelled twist $a$ recovered exactly",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.5,
    )
    rounded_box(
        ax_a,
        0.06,
        0.08,
        0.88,
        0.21,
        r"source period $\operatorname{ord}(a)$" + "\n"
        + r"$[X/C]\simeq B1$" + "\n1 static inertia sector",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.3,
    )
    arrow(ax_a, (0.50, 0.67), (0.50, 0.59), color=GREEN)
    arrow(ax_a, (0.50, 0.38), (0.50, 0.30), color=ORANGE)

    # B: trivial one-point action and BC inertia.
    ax_b = fig.add_subplot(grid[0, 1])
    clean_axis(ax_b)
    panel_label(ax_b, "B", "trivial action / $BC$")
    rounded_box(
        ax_b,
        0.04,
        0.68,
        0.92,
        0.20,
        r"$X=C/C=\{*\}$" + "\n" + r"trivial $C$-action",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=7.2,
    )
    rounded_box(
        ax_b,
        0.06,
        0.39,
        0.88,
        0.19,
        r"action kernel $N=C$" + "\n"
        + r"twist known only modulo $C$",
        facecolor=PALE_PURPLE,
        edgecolor=PURPLE,
        fontsize=6.5,
    )
    rounded_box(
        ax_b,
        0.06,
        0.08,
        0.88,
        0.21,
        r"source period $1$" + "\n" + r"$[X/C]=BC$" + "\n"
        + r"$|C|$ static inertia sectors",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.4,
    )
    arrow(ax_b, (0.50, 0.67), (0.50, 0.59), color=VERMILLION)
    arrow(ax_b, (0.50, 0.38), (0.50, 0.30), color=ORANGE)

    # C: separately typed effective C6 counterexample.
    ax_c = fig.add_subplot(grid[0, 2])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "effective $C_6$ control")
    rounded_box(
        ax_c,
        0.02,
        0.68,
        0.96,
        0.20,
        r"$X=C_6/C_2\sqcup C_6/C_3$" + "\n"
        + rf"$|N|={kernel_order}$; labelled $a$ recovered",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        hatch="..",
        fontsize=6.5,
    )
    rounded_box(
        ax_c,
        0.03,
        0.36,
        0.94,
        0.22,
        r"$\zeta_X=(1-t^3)^{-1}(1-t^2)^{-1}$" + "\n"
        + f"supports ${source_supports[1]}$ and ${source_supports[0]}$; NO period-$6$ factor",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=5.8,
    )
    rounded_box(
        ax_c,
        0.03,
        0.06,
        0.94,
        0.20,
        r"$[X/C_6]\simeq BC_2\sqcup BC_3$" + "\n"
        + f"{inertia_count} static inertia sectors",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.4,
    )
    arrow(ax_c, (0.50, 0.67), (0.50, 0.59), color=GREEN)
    arrow(ax_c, (0.50, 0.35), (0.50, 0.27), color=ORANGE)

    # D: general action-kernel and stack formulas tying the cases together.
    ax_d = fig.add_subplot(grid[1, :])
    clean_axis(ax_d)
    panel_label(ax_d, "D", "what effectivity controls---and what it does not")
    rounded_box(
        ax_d,
        0.01,
        0.43,
        0.28,
        0.34,
        r"$N=\bigcap_{n_K>0}K$" + "\n"
        + r"kernel of the $C$-action",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.7,
    )
    rounded_box(
        ax_d,
        0.36,
        0.43,
        0.28,
        0.34,
        r"$(\mathbb{Z}\!\times\!C)$ stabilizers record" + "\n"
        + r"$a^{-1}K$ for every represented $K$" + "\n"
        + r"$\Rightarrow$ recover $a$ modulo $N$",
        facecolor=PALE_PURPLE,
        edgecolor=PURPLE,
        hatch="..",
        fontsize=6.0,
    )
    rounded_box(
        ax_d,
        0.71,
        0.43,
        0.28,
        0.34,
        r"$[X/C]\simeq\coprod_K n_KBK$" + "\n"
        + r"inertia count $\sum_K n_K|K|$" + "\n"
        + "identity dynamics",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.0,
    )
    arrow(ax_d, (0.295, 0.59), (0.355, 0.59), color=PURPLE)
    arrow(ax_d, (0.645, 0.59), (0.705, 0.59), color=ORANGE)
    rounded_box(
        ax_d,
        0.18,
        0.055,
        0.64,
        0.19,
        r"Effectivity ($N=1$) controls exact label recovery." + "\n"
        + r"It does NOT force a source factor at $\operatorname{ord}(a)$: the effective $C_6$ control has no period-$6$ factor.",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=6.3,
        linewidth=1.0,
    )

    fig.text(
        0.5,
        0.025,
        "The $C_6$ object is a structural control, not an arithmetic modulus row or a candidate; all inertia dynamics shown are static.",
        ha="center",
        va="bottom",
        color=MID_GRAY,
        fontsize=6.4,
    )
    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    figure = build_figure()
    save_figure(
        figure,
        args.output_dir.resolve(),
        STEM,
        metadata_title="Effectivity, action kernels, and static inertia counterexamples",
    )


if __name__ == "__main__":
    main()
