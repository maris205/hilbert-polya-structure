#!/usr/bin/env python3
"""Generate Figure 2: weighted support, eliminations, and quartic law."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt

from figure_data import figure_contract
from paper_plot_style import (
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
    cross_out,
    panel_marker,
    rounded_box,
    save_figure,
)


def build(output_dir: Path) -> None:
    contract = figure_contract(2)
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    fig.subplots_adjust(left=0.018, right=0.982, bottom=0.025, top=0.975)
    clean_axis(ax)

    panel_marker(ax, 0.012, 0.985, "A")
    rounded_box(
        ax,
        0.245,
        0.86,
        0.51,
        0.095,
        r"$mr+(2m-1)s=3m(2m-1)$"
        "\nexactly four nonnegative parameter supports",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=8.2,
    )

    x_positions = (0.045, 0.285, 0.525, 0.765)
    terms = (
        (r"$C_m\varepsilon^{3m}$" "\nSURVIVES", PALE_GREEN, GREEN, None),
        (r"$D_ma^{2m-1}\varepsilon^{2m}$" "\nSURVIVES", PALE_GREEN, GREEN, None),
        (r"$a^{2(2m-1)}\varepsilon^m$" "\nREMOVED", PALE_RED, VERMILLION, None),
        (r"$a^{3(2m-1)}$" "\nREMOVED", PALE_RED, VERMILLION, None),
    )
    for x, (text, face, edge, hatch) in zip(x_positions, terms):
        rounded_box(
            ax,
            x,
            0.665,
            0.19,
            0.115,
            text,
            facecolor=face,
            edgecolor=edge,
            hatch=hatch,
            fontsize=7.7,
        )
        arrow(ax, (0.50, 0.858), (x + 0.095, 0.785), color=MID_GRAY, connectionstyle="arc3,rad=0.10")
    cross_out(ax, 0.525, 0.665, 0.19, 0.115)
    cross_out(ax, 0.765, 0.665, 0.19, 0.115)

    rounded_box(
        ax,
        0.505,
        0.505,
        0.215,
        0.105,
        "three nonfixed root patterns\n"
        r"$v(t_\varepsilon)\geq 3/2,\ 7/4,\ 3$" "\n"
        "+ exact diagonal branch",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        fontsize=6.9,
    )
    rounded_box(
        ax,
        0.755,
        0.505,
        0.205,
        0.105,
        "separated algebra\n"
        r"$\varepsilon=0$, $q_i^2=0$" "\n"
        "constant term vanishes",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        fontsize=7.0,
    )
    arrow(ax, (0.62, 0.612), (0.62, 0.66), color=VERMILLION)
    arrow(ax, (0.86, 0.612), (0.86, 0.66), color=VERMILLION)

    panel_marker(ax, 0.012, 0.455, "B")
    rounded_box(
        ax,
        0.07,
        0.31,
        0.50,
        0.11,
        r"$S_m(a,\varepsilon)=C_m\varepsilon^{3m}"
        r"+D_ma^{2m-1}\varepsilon^{2m}$",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        linewidth=1.15,
        fontsize=9.0,
    )
    arrow(ax, (0.14, 0.66), (0.22, 0.425), color=GREEN, connectionstyle="arc3,rad=-0.12")
    arrow(ax, (0.38, 0.66), (0.42, 0.425), color=GREEN, connectionstyle="arc3,rad=0.08")
    rounded_box(
        ax,
        0.63,
        0.31,
        0.31,
        0.11,
        "cyclic reversal\n"
        r"$C_m=0$ for odd $m$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=8.2,
    )
    arrow(ax, (0.575, 0.365), (0.625, 0.365), color=BLUE)

    panel_marker(ax, 0.012, 0.255, "C")
    rounded_box(
        ax,
        0.07,
        0.075,
        0.50,
        0.13,
        "quartic specialization $m=2$\n"
        r"$S_2^{(3)}(L)=-1296000-1572864L^3$" "\n"
        r"$=-384(3375+4096L^3)$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        fontsize=8.2,
    )
    rounded_box(
        ax,
        0.63,
        0.062,
        0.31,
        0.155,
        "OPEN\n"
        r"$D_m\neq0$ for every $m\geq2$?" "\n"
        "no all-degree separator claimed",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        linestyle="--",
        hatch="///",
        fontsize=7.9,
    )
    arrow(ax, (0.32, 0.305), (0.32, 0.21), color=ORANGE)
    arrow(ax, (0.57, 0.135), (0.625, 0.135), color=VERMILLION, linestyle="--")

    save_figure(
        fig,
        output_dir,
        contract["stem"],
        "Weighted support reduction, two-term residue law, quartic specialization, and open nonvanishing boundary.",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()
