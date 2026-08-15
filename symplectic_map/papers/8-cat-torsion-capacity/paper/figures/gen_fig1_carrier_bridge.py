#!/usr/bin/env python3
"""Generate Figure 1: the exact primitive-divisor carrier bridge."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figure_data import load_sources
from paper_plot_style import (
    BLACK,
    BLUE,
    GREEN,
    LIGHT_GRAY,
    MID_GRAY,
    ORANGE,
    PALE_BLUE,
    PALE_GREEN,
    PALE_ORANGE,
    PURPLE,
    WHITE,
    arrow,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig1_carrier_bridge"


def build_figure():
    raw, manifest, _proof = load_sources()
    contract = raw["general_theorem_contract"]
    if not all(
        section["pass"]
        for section in (
            contract["norm_determinant"],
            contract["primitive_kernel"],
            contract["negative_trace_parity"],
        )
    ):
        raise RuntimeError("theorem-contract assertion flags are not all passing")
    if contract["tail_evidence"] != "IMPORTED_THEOREM_PLUS_SEPARATE_PARITY_PROOF_ONLY":
        raise RuntimeError("unexpected theorem-tail evidence class")
    if contract["tail_periods_computed"] != []:
        raise RuntimeError("tail computation firewall violated")

    fig = plt.figure(figsize=(7.2, 3.55), constrained_layout=False)
    grid = fig.add_gridspec(
        1,
        3,
        width_ratios=(1.03, 1.35, 0.96),
        left=0.035,
        right=0.985,
        bottom=0.075,
        top=0.91,
        wspace=0.17,
    )

    # (a) Arithmetic bridge.
    ax = fig.add_subplot(grid[0, 0])
    clean_axis(ax)
    panel_label(ax, "a", "Arithmetic bridge")
    box_x, box_w, box_h = 0.06, 0.88, 0.145
    ys = (0.79, 0.57, 0.35, 0.13)
    boxes = (
        (
            r"$N(\alpha^n-1)=\det(M^n-I)$",
            PALE_BLUE,
            BLUE,
        ),
        (r"primitive rational prime $p$", PALE_GREEN, GREEN),
        (r"$0\ne v\in\ker(M^n-I)\ (\mathrm{mod}\ p)$", PALE_ORANGE, ORANGE),
        (r"order $p$  $\boldsymbol{\cdot}$  exact period $n$", PALE_GREEN, GREEN),
    )
    for y, (label, face, edge) in zip(ys, boxes):
        rounded_box(
            ax,
            box_x,
            y,
            box_w,
            box_h,
            label,
            facecolor=face,
            edgecolor=edge,
            fontsize=7.9,
        )
    for upper, lower in zip(ys[:-1], ys[1:]):
        arrow(ax, (0.5, upper - 0.01), (0.5, lower + box_h + 0.01), color=MID_GRAY)
    ax.text(
        0.5,
        0.035,
        r"if $r=\dim\ker(M^n-I)$:  $(p^r-1)/n$ cycles",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.0,
        color=BLACK,
    )

    # (b) The negative-trace argument is explicitly separate.
    ax = fig.add_subplot(grid[0, 1])
    clean_axis(ax)
    panel_label(ax, "b", "Sign and parity routing")
    rounded_box(
        ax,
        0.24,
        0.83,
        0.52,
        0.12,
        r"hyperbolic $M\in\mathrm{SL}_2(\mathbf{Z})$",
        facecolor=WHITE,
        edgecolor=BLACK,
        fontsize=6.9,
    )
    rounded_box(
        ax,
        0.02,
        0.63,
        0.38,
        0.12,
        r"$\operatorname{tr}M>2$",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.8,
    )
    rounded_box(
        ax,
        0.60,
        0.63,
        0.38,
        0.12,
        r"$\operatorname{tr}M<-2$:  $B=-M$" + "\nPaper 8 conversion",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        fontsize=6.45,
    )
    arrow(ax, (0.43, 0.83), (0.21, 0.75), color=GREEN)
    arrow(ax, (0.57, 0.83), (0.79, 0.75), color=ORANGE)
    rounded_box(
        ax,
        0.02,
        0.39,
        0.38,
        0.15,
        "Flatters\npositive norm-one unit",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.2,
    )
    arrow(ax, (0.21, 0.63), (0.21, 0.54), color=GREEN)

    branch_y = (0.47, 0.33, 0.19)
    branch_labels = (
        r"$n$ odd  $\longrightarrow$  index $2n$",
        r"$4\mid n$  $\longrightarrow$  index $n$",
        r"$n=2k$ ($k$ odd)  $\longrightarrow$  index $k$",
    )
    ax.plot([0.49, 0.49], [0.24, 0.54], transform=ax.transAxes, color=ORANGE, lw=0.9)
    arrow(ax, (0.79, 0.63), (0.49, 0.54), color=ORANGE, mutation_scale=7)
    for y, label in zip(branch_y, branch_labels):
        rounded_box(
            ax,
            0.54,
            y,
            0.44,
            0.095,
            label,
            facecolor=PALE_ORANGE,
            edgecolor=ORANGE,
            fontsize=6.15 if y != branch_y[-1] else 5.65,
        )
        arrow(ax, (0.49, y + 0.047), (0.54, y + 0.047), color=ORANGE, mutation_scale=6)
    rounded_box(
        ax,
        0.13,
        0.025,
        0.74,
        0.10,
        r"prime-order carrier of exact period $n$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.65,
    )
    arrow(ax, (0.21, 0.39), (0.31, 0.125), color=GREEN)
    arrow(ax, (0.76, 0.19), (0.69, 0.125), color=ORANGE, mutation_scale=7)
    # (c) The evidence boundary is categorical, not a computed continuation.
    ax = fig.add_subplot(grid[0, 2])
    clean_axis(ax)
    panel_label(ax, "c", "Evidence boundary")
    ax.add_patch(
        Rectangle(
            (0.04, 0.42),
            0.53,
            0.18,
            transform=ax.transAxes,
            facecolor=PALE_BLUE,
            edgecolor=BLUE,
            linewidth=0.9,
            hatch="///",
        )
    )
    ax.add_patch(
        Rectangle(
            (0.57, 0.42),
            0.38,
            0.18,
            transform=ax.transAxes,
            facecolor=PALE_GREEN,
            edgecolor=GREEN,
            linewidth=0.9,
            hatch="..",
        )
    )
    ax.plot([0.57, 0.57], [0.34, 0.69], transform=ax.transAxes, color=BLACK, lw=1.1)
    ax.text(0.57, 0.72, r"boundary $12$", transform=ax.transAxes, ha="center", fontsize=7.2)
    ax.text(
        0.27,
        0.51,
        "exact audit\n" + r"$1\leq n\leq12$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.2,
        color=BLUE,
        fontweight="bold",
    )
    ax.text(
        0.79,
        0.51,
        "theorem only\n" + r"$n>12$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.2,
        color=GREEN,
        fontweight="bold",
    )
    ax.text(
        0.50,
        0.23,
        "computed tail periods: 0\n"
        "imported primitive-divisor theorem\n"
        "+ separate parity proof",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.15,
        color=BLACK,
        linespacing=1.35,
    )
    ax.text(
        0.50,
        0.91,
        "manifest PASS",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.0,
        color=GREEN,
        fontweight="bold",
    )
    if manifest["pass"] is not True:
        raise RuntimeError("unreachable: manifest status changed during rendering")

    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    save_figure(
        build_figure(),
        args.output_dir.resolve(),
        STEM,
        metadata_title="Primitive-divisor carrier bridge and theorem boundary",
    )


if __name__ == "__main__":
    main()
