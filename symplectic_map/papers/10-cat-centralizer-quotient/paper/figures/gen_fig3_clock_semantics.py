#!/usr/bin/env python3
"""Generate Figure 3: source clock, coarse identity, and external label."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

from figure_data import load_frozen_payload
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
    PALE_RED,
    PURPLE,
    VERMILLION,
    arrow,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig3_clock_semantics"


def _count_sequence(rows, key: str) -> str:
    return ", ".join(str(row[key]) for row in rows)


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    primes = payload["prime_rows"]
    composites = payload["composite_rows"]
    labels = [str(row["q"]) for row in rows]
    xpos = np.arange(len(rows))

    fig = plt.figure(figsize=(7.2, 4.9), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.95, 1.12],
        width_ratios=[1.10, 0.90],
        hspace=0.50,
        wspace=0.30,
        left=0.07,
        right=0.98,
        bottom=0.13,
        top=0.94,
    )

    # A: exact source periods versus quotient primitive period one.
    ax_a = fig.add_subplot(grid[0, :])
    panel_label(ax_a, "A", "source clock versus the two coarse quotient clocks")
    source_period = np.array([row["A_order"] for row in rows])
    bars = ax_a.bar(
        xpos,
        source_period,
        width=0.58,
        color=BLUE,
        edgecolor=BLACK,
        linewidth=0.55,
        label="source $\\operatorname{ord}_q(A)$",
    )
    for bar, value in zip(bars, source_period):
        ax_a.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.65,
            str(value),
            ha="center",
            va="bottom",
            fontsize=6.8,
        )
    ax_a.plot(
        xpos,
        np.ones(len(rows)),
        color=VERMILLION,
        linewidth=1.25,
        marker="D",
        markersize=4.2,
        markerfacecolor=PALE_RED,
        markeredgecolor=VERMILLION,
        label="native period on $\\mathrm{CV}/C$ and $\\mathrm{CV}/C^1$: $1$",
    )
    ax_a.axvspan(4.5, 8.5, color=PALE_ORANGE, alpha=0.55, zorder=-5)
    ax_a.axvline(4.5, color=MID_GRAY, linestyle="--", linewidth=0.8)
    ax_a.set_xticks(xpos, labels)
    ax_a.set_xlabel("modulus $q$  (primes | composites)")
    ax_a.set_ylabel("least positive period")
    ax_a.set_ylim(0, max(source_period) * 1.18)
    ax_a.grid(axis="y", color=LIGHT_GRAY, linewidth=0.5)
    ax_a.set_axisbelow(True)
    ax_a.legend(frameon=False, loc="upper left", fontsize=6.7, handlelength=1.5)

    # B: semantic pipeline, with the external specialization visually dashed.
    ax_b = fig.add_subplot(grid[1, 0])
    clean_axis(ax_b)
    panel_label(ax_b, "B", "factor semantics")
    rounded_box(
        ax_b,
        0.01,
        0.65,
        0.29,
        0.23,
        "source $A$ dynamics\nperiod $\\operatorname{ord}_q(A)$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.1,
    )
    rounded_box(
        ax_b,
        0.35,
        0.65,
        0.27,
        0.23,
        "coarse quotient\n$A_{\\rm quot}=\\mathrm{id}$; period $1$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.0,
    )
    rounded_box(
        ax_b,
        0.68,
        0.65,
        0.31,
        0.23,
        "intrinsic factor $(1-z)^{-k}$\n"
        "$k=1$ or $|\\mathrm{im}N_q|$",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        hatch="..",
        fontsize=5.9,
    )
    arrow(ax_b, (0.305, 0.765), (0.345, 0.765), color=MID_GRAY)
    arrow(ax_b, (0.625, 0.765), (0.675, 0.765), color=MID_GRAY)
    rounded_box(
        ax_b,
        0.31,
        0.20,
        0.46,
        0.23,
        "EXTERNAL label\n$z\\mapsto q^{-s}$ or length $\\log q$",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=6.2,
        linewidth=1.0,
    )
    arrow(
        ax_b,
        (0.84, 0.64),
        (0.70, 0.44),
        color=VERMILLION,
        linewidth=1.0,
        connectionstyle="arc3,rad=-0.15",
    )
    ax_b.text(
        0.55,
        0.06,
        "The modulus label is not a return-time law of the coarse quotient.",
        transform=ax_b.transAxes,
        ha="center",
        va="center",
        color=VERMILLION,
        fontsize=6.2,
        fontweight="bold",
    )

    # C: prime-specificity and outside-scope boundary.
    ax_c = fig.add_subplot(grid[1, 1])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "prime non-specificity / live boundary")
    rounded_box(
        ax_c,
        0.02,
        0.62,
        0.46,
        0.27,
        "prime controls\n$q=" + ",".join(str(row["q"]) for row in primes) + "$\n"
        "$|\\mathrm{CV}/C|=" + _count_sequence(primes, "CV_over_C") + "$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.7,
    )
    rounded_box(
        ax_c,
        0.52,
        0.62,
        0.46,
        0.27,
        "composite controls\n$q=" + ",".join(str(row["q"]) for row in composites) + "$\n"
        "$|\\mathrm{CV}/C|=" + _count_sequence(composites, "CV_over_C") + "$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=6.7,
    )
    rounded_box(
        ax_c,
        0.03,
        0.27,
        0.94,
        0.20,
        "same one-class full quotient + identity transition\n"
        "$\\Rightarrow$ no intrinsic prime selector",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=6.5,
    )
    ax_c.text(
        0.5,
        0.095,
        "LIVE / UNTESTED: Burnside, equivariant, orbifold,\n"
        "stacky, groupoid, twisted-sector, and Hecke refinements",
        transform=ax_c.transAxes,
        ha="center",
        va="center",
        color=PURPLE,
        fontsize=6.2,
        fontweight="bold",
        linespacing=1.2,
    )

    fig.text(
        0.5,
        0.025,
        "All $q^{-s}$ and $\\log q$ expressions are symbolic; no numerical value of $s$ or a logarithm is evaluated.",
        ha="center",
        va="bottom",
        color=MID_GRAY,
        fontsize=7.0,
    )
    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    fig = build_figure()
    save_figure(
        fig,
        args.output_dir.resolve(),
        STEM,
        metadata_title="Source cat-map clock, coarse identity, and external modulus label",
    )


if __name__ == "__main__":
    main()
