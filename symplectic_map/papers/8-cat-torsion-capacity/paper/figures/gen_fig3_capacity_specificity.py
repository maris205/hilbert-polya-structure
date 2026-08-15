#!/usr/bin/env python3
"""Generate Figure 3: intrinsic torsion capacity versus specificity."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from figure_data import clock_payload, load_sources
from paper_plot_style import (
    BLACK,
    BLUE,
    GREEN,
    MID_GRAY,
    ORANGE,
    PALE_BLUE,
    PALE_GREEN,
    PALE_ORANGE,
    PALE_RED,
    PURPLE,
    VERMILLION,
    WHITE,
    arrow,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig3_capacity_specificity"


def build_figure():
    raw, _manifest, _proof = load_sources()
    payload = clock_payload(raw)
    clock = payload["clock"]
    witnesses = payload["witnesses"]
    orbit = payload["orbit"]

    if not all(item["pass"] for item in clock["all_order_witnesses"]):
        raise RuntimeError("all-order witness assertion failed")
    if not all(item["pass"] for item in witnesses):
        raise RuntimeError("a discontinuity witness assertion failed")
    if not all(orbit["checks"].values()):
        raise RuntimeError("an orbit/monodromy assertion failed")

    fig = plt.figure(figsize=(7.2, 3.8), constrained_layout=False)
    grid = fig.add_gridspec(
        1,
        3,
        width_ratios=(0.88, 1.13, 1.32),
        left=0.045,
        right=0.985,
        bottom=0.16,
        top=0.91,
        wspace=0.25,
    )

    # (a) Surjective capacity, with no prime selector.
    ax = fig.add_subplot(grid[0, 0])
    clean_axis(ax)
    panel_label(ax, "a", "All additive orders")
    rounded_box(
        ax,
        0.13,
        0.74,
        0.74,
        0.15,
        r"$x_m=(1/m,0)$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=9.0,
    )
    rounded_box(
        ax,
        0.05,
        0.43,
        0.40,
        0.16,
        "prime $m$",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.7,
        hatch="///",
    )
    rounded_box(
        ax,
        0.55,
        0.43,
        0.40,
        0.16,
        "composite $m$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        fontsize=7.7,
        hatch="xx",
    )
    arrow(ax, (0.43, 0.74), (0.25, 0.59), color=GREEN)
    arrow(ax, (0.57, 0.74), (0.75, 0.59), color=ORANGE)
    rounded_box(
        ax,
        0.18,
        0.16,
        0.64,
        0.14,
        r"$\operatorname{ord}(x_m)=m$",
        facecolor=WHITE,
        edgecolor=BLACK,
        fontsize=8.2,
    )
    arrow(ax, (0.25, 0.43), (0.40, 0.30), color=GREEN)
    arrow(ax, (0.75, 0.43), (0.60, 0.30), color=ORANGE)
    ax.text(
        0.50,
        0.045,
        "surjective capacity\n" + r"$\ne$ prime specificity",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.3,
        color=VERMILLION,
        fontweight="bold",
    )

    # (b) Three exact locked illustrations of the general local argument.
    ax = fig.add_subplot(grid[0, 1])
    panel_label(ax, "b", "Local irregularity witnesses")
    denominators = [item["coprime_denominator"] for item in witnesses]
    orders = [item["exact_perturbed_order"] for item in witnesses]
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.scatter(
        denominators,
        orders,
        marker="D",
        s=40,
        facecolor=WHITE,
        edgecolor=PURPLE,
        linewidth=1.25,
        zorder=3,
    )
    for item in witnesses:
        ax.annotate(
            f"$1/{item['coprime_denominator']}\\mapsto {item['exact_perturbed_order']}$",
            (item["coprime_denominator"], item["exact_perturbed_order"]),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=6.65,
            color=PURPLE,
            fontweight="bold",
        )
    ax.axhline(witnesses[0]["base_order"], color=MID_GRAY, lw=0.8, ls="--")
    ax.text(
        0.03,
        0.085,
        "base order $18$",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=6.7,
        color=MID_GRAY,
        bbox={"facecolor": WHITE, "edgecolor": "none", "pad": 0.7},
    )
    ax.set_xticks(denominators)
    ax.set_xticklabels([str(value) for value in denominators])
    ax.set_yticks([18] + orders)
    ax.set_yticklabels(["18"] + [str(value) for value in orders])
    ax.minorticks_off()
    ax.set_xlim(15, 155)
    ax.set_ylim(12, 4200)
    ax.set_xlabel(r"coprime denominator $N$  (larger $\Rightarrow$ closer)")
    ax.set_ylabel("exact additive order")
    ax.grid(color="#E8EAED", lw=0.55, which="major", zorder=0)
    ax.text(
        0.97,
        0.085,
        r"exact law: $18N$",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=6.8,
        color=BLACK,
        bbox={"facecolor": WHITE, "edgecolor": "none", "pad": 0.7},
    )

    # (c) The orbit-readable torsion clock and native derivative clock differ.
    ax = fig.add_subplot(grid[0, 2])
    clean_axis(ax)
    panel_label(ax, "c", "Orbit label vs. monodromy")
    rounded_box(
        ax,
        0.02,
        0.76,
        0.43,
        0.14,
        "order-5 carrier\nperiod 10",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.4,
    )
    rounded_box(
        ax,
        0.02,
        0.42,
        0.43,
        0.25,
        "$L=\\log 5$\n$S_{10}L=10\\log 5$\n$S_{10r}L=10r\\log 5$",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.4,
    )
    arrow(ax, (0.235, 0.76), (0.235, 0.67), color=GREEN)

    matrix = orbit["monodromy"]
    coeffs = orbit["monodromy_characteristic_coefficients"]
    matrix_text = (
        r"$A^{10}=$"
        + "\n"
        + f"[ {matrix[0][0]}   {matrix[0][1]} ]"
        + "\n"
        + f"[  {matrix[1][0]}   {matrix[1][1]} ]"
    )
    rounded_box(
        ax,
        0.55,
        0.76,
        0.43,
        0.14,
        "native derivative\nperiod 10",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        fontsize=7.4,
    )
    rounded_box(
        ax,
        0.55,
        0.42,
        0.43,
        0.25,
        matrix_text
        + "\n"
        + rf"$\chi: [{coeffs[0]}, {coeffs[1]}, {coeffs[2]}]$",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        fontsize=6.65,
    )
    arrow(ax, (0.765, 0.76), (0.765, 0.67), color=VERMILLION)
    ax.text(
        0.235,
        0.28,
        "torsion-order dependent\nand repetition-scaled",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.2,
        color=GREEN,
        fontweight="bold",
    )
    ax.text(
        0.765,
        0.28,
        "period dependent /\ntorsion-order blind",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.2,
        color=VERMILLION,
        fontweight="bold",
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.43, 0.16),
            (0.57, 0.16),
            transform=ax.transAxes,
            arrowstyle="<->",
            mutation_scale=8,
            linewidth=1.0,
            color=BLACK,
        )
    )
    ax.text(
        0.50,
        0.08,
        "not the same clock",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.15,
        color=BLACK,
        fontweight="bold",
    )

    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    save_figure(
        build_figure(),
        args.output_dir.resolve(),
        STEM,
        metadata_title="Intrinsic torsion-order capacity versus prime specificity",
    )


if __name__ == "__main__":
    main()
