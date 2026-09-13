#!/usr/bin/env python3
"""Generate Figure 1: theorem architecture and proof-only evidence firewall."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt

from figure_data import figure_contract
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
    VERMILLION,
    arrow,
    clean_axis,
    panel_marker,
    rounded_box,
    save_figure,
)


def build(output_dir: Path) -> None:
    contract = figure_contract(1)
    fig, ax = plt.subplots(figsize=(7.2, 5.05))
    fig.subplots_adjust(left=0.018, right=0.982, bottom=0.025, top=0.975)
    clean_axis(ax)

    panel_marker(ax, 0.012, 0.985, "A")
    rounded_box(
        ax,
        0.055,
        0.735,
        0.245,
        0.175,
        "Formal period one\n"
        r"spectrum $0^{\times 2m}$" "\n"
        r"$q^2=0$; $q$ may be nonzero",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.8,
    )
    rounded_box(
        ax,
        0.378,
        0.735,
        0.245,
        0.175,
        "Formal exact period two\n"
        r"spectrum $2^{\times((2m)^2-2m)}$" "\n"
        r"retain $2+q(x)q(y)$, then subtract",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.4,
    )
    rounded_box(
        ax,
        0.70,
        0.735,
        0.245,
        0.175,
        "Formal period three\n"
        r"$S_m(a,1)=C_m+D_ma^{2m-1}$" "\n"
        "finite slope certificate\n"
        r"$C_m=0$ if $m$ is odd",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.1,
    )

    arrow(ax, (0.302, 0.822), (0.372, 0.822), color=BLUE)
    arrow(ax, (0.625, 0.822), (0.694, 0.822), color=GREEN)

    rounded_box(
        ax,
        0.425,
        0.465,
        0.52,
        0.19,
        "Complete normalized quartic $0^4$ fiber\n"
        r"$p=(x^2-L)^2$,  $f_L\sim f_M\Longleftrightarrow L^3=M^3$" "\n"
        r"pointwise: $-384(3375+4096L^3)$; exact length $60$" "\n"
        r"period three is the first separator on this fiber",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        linewidth=1.15,
        fontsize=7.8,
    )
    arrow(ax, (0.50, 0.73), (0.54, 0.66), color=MID_GRAY, connectionstyle="arc3,rad=0.14")
    arrow(ax, (0.82, 0.73), (0.76, 0.66), color=GREEN, linewidth=1.15)
    ax.text(
        0.355,
        0.68,
        "lower periods blind",
        transform=ax.transAxes,
        fontsize=6.8,
        color=MID_GRAY,
        ha="center",
        va="center",
    )

    panel_marker(ax, 0.012, 0.395, "B")
    ax.plot(
        [0.04, 0.96],
        [0.375, 0.375],
        transform=ax.transAxes,
        color=BLACK,
        linewidth=1.0,
        linestyle=(0, (4, 2)),
    )
    ax.text(
        0.43,
        0.386,
        "PROOF-ONLY EVIDENCE FIREWALL",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=7.1,
        fontweight="bold",
        color=BLACK,
    )

    rounded_box(
        ax,
        0.055,
        0.105,
        0.255,
        0.17,
        "Source-locked proof\n"
        "sole scientific authority\n"
        "registered evidence used: false",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.7,
    )
    rounded_box(
        ax,
        0.365,
        0.105,
        0.255,
        0.17,
        "Independent proof reviews\n"
        "SOURCE_LOCK_PASS\n"
        "PROOF_ONLY_HANDOFF_PASS",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.6,
    )
    rounded_box(
        ax,
        0.675,
        0.085,
        0.275,
        0.21,
        "Consumed registered audit\n"
        "TERMINAL FAIL / NO RERUN\n"
        "NO RAW RESULT / NO RESULT PASS\n"
        "provenance only\n"
        "finalization not authorized",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        linestyle="--",
        hatch="///",
        fontsize=6.9,
    )

    arrow(ax, (0.31, 0.19), (0.36, 0.19), color=GREEN)
    arrow(ax, (0.56, 0.28), (0.62, 0.46), color=BLUE, linewidth=1.2)
    arrow(
        ax,
        (0.80, 0.30),
        (0.80, 0.365),
        color=VERMILLION,
        linestyle="--",
        connectionstyle="arc3,rad=-0.32",
    )
    ax.text(
        0.86,
        0.338,
        "no theorem arrow",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.6,
        color=VERMILLION,
    )

    save_figure(
        fig,
        output_dir,
        contract["stem"],
        "Proof-only theorem architecture for formal periods one through three and the quartic separator.",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()
