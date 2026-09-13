#!/usr/bin/env python3
"""Generate Figure 3: the complete transparent Step-9 certificate pipeline."""

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
    PALE_PURPLE,
    PALE_RED,
    PURPLE,
    VERMILLION,
    arrow,
    clean_axis,
    panel_marker,
    rounded_box,
    save_figure,
)


def stage(ax, x, y, width, height, number, text, face, edge, **kwargs):
    rounded_box(
        ax,
        x,
        y,
        width,
        height,
        f"{number}\n{text}",
        facecolor=face,
        edgecolor=edge,
        **kwargs,
    )


def build(output_dir: Path) -> None:
    contract = figure_contract(3)
    fig, ax = plt.subplots(figsize=(7.2, 5.55))
    fig.subplots_adjust(left=0.014, right=0.986, bottom=0.022, top=0.978)
    clean_axis(ax)

    panel_marker(ax, 0.008, 0.988, "A")
    stage(
        ax,
        0.04,
        0.80,
        0.205,
        0.135,
        "1",
        "recurrence (R); state (9.1)\n"
        "bases (9.2); four branches\n"
        "(9.3): strict degree decrease",
        PALE_BLUE,
        BLUE,
        fontsize=6.4,
    )
    stage(
        ax,
        0.285,
        0.80,
        0.205,
        0.135,
        "2",
        "Laurent form (9.4)\n"
        "reciprocal expansion (9.5)\n"
        "unique NF; no double counting",
        PALE_BLUE,
        BLUE,
        fontsize=6.8,
    )
    stage(
        ax,
        0.53,
        0.80,
        0.205,
        0.135,
        "3",
        "assembly (9.6)--(9.9)\n"
        "admissible tuples (9.10)--(9.13)\n"
        "signs + multiplicities retained",
        PALE_PURPLE,
        PURPLE,
        fontsize=6.7,
    )
    stage(
        ax,
        0.775,
        0.765,
        0.19,
        0.205,
        "4",
        "local identity (9.14)\n"
        r"$\sum_{\ell+A+2B=\alpha}$" "\n"
        r"$(-1)^{\ell+B}2^A\binom{N}{\ell}$" "\n"
        r"$\frac{(n+A+B)!}{n!A!B!}$" "\n"
        r"$=(-1)^\alpha\binom{N-2n-2}{\alpha}$" "\n"
        "coefficient extraction proof",
        PALE_ORANGE,
        ORANGE,
        fontsize=6.7,
        linewidth=1.05,
    )
    for start, end, color in (
        ((0.247, 0.868), (0.282, 0.868), BLUE),
        ((0.492, 0.868), (0.527, 0.868), PURPLE),
        ((0.737, 0.868), (0.772, 0.868), ORANGE),
    ):
        arrow(ax, start, end, color=color)

    panel_marker(ax, 0.008, 0.70, "B")
    stage(
        ax,
        0.045,
        0.515,
        0.40,
        0.145,
        "5",
        "integrality (9.17); sum rule (9.18)\n"
        "unique distinguished coordinate (9.19)\n"
        "incoming-transfer bijection (9.20)\n"
        "guarded factors + sign (9.21)--(9.22)",
        PALE_GREEN,
        GREEN,
        fontsize=6.6,
    )
    arrow(
        ax,
        (0.87, 0.763),
        (0.44, 0.59),
        color=GREEN,
        connectionstyle="arc3,rad=-0.20",
        linewidth=1.1,
    )

    stage(
        ax,
        0.51,
        0.535,
        0.205,
        0.125,
        "6a",
        r"$j\geq1$ flows" "\n"
        "unique coordinate\n"
        "(9.23)--(9.24)",
        PALE_GREEN,
        GREEN,
        fontsize=6.9,
    )
    stage(
        ax,
        0.76,
        0.515,
        0.205,
        0.165,
        "6b",
        r"separate $j=0$" "\n"
        "two flow types (9.25)\n"
        "exception vanishes (9.26)",
        PALE_ORANGE,
        ORANGE,
        hatch="///",
        fontsize=6.9,
        linewidth=1.05,
    )
    arrow(ax, (0.442, 0.59), (0.505, 0.59), color=GREEN)
    arrow(ax, (0.442, 0.56), (0.755, 0.56), color=ORANGE, connectionstyle="arc3,rad=-0.14")

    panel_marker(ax, 0.008, 0.455, "C")
    stage(
        ax,
        0.12,
        0.235,
        0.58,
        0.17,
        "7",
        r"$H(r,k)=\sum_{u+v=k}\binom{k}{u}\binom{r}{2u}\binom{r}{2v}$" "\n"
        r"$A_{m,r}=\sum_k(-1)^{r+k}\binom{m-1}{2(m-k)-1}H(r,k)$" "\n"
        r"$D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}\binom{m+1}{j}"
        r"(2m)^{3m+3-2j}A_{m,m-j}$",
        PALE_PURPLE,
        PURPLE,
        fontsize=7.2,
        linewidth=1.1,
    )
    arrow(ax, (0.61, 0.532), (0.52, 0.41), color=PURPLE, connectionstyle="arc3,rad=0.12")
    arrow(ax, (0.86, 0.512), (0.66, 0.405), color=PURPLE, connectionstyle="arc3,rad=-0.13")

    rounded_box(
        ax,
        0.75,
        0.235,
        0.20,
        0.17,
        "OPEN\n"
        r"universal $D_m\neq0$" "\n"
        "no finite diagnostic\n"
        "is proof evidence",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        linestyle="--",
        hatch="xx",
        fontsize=7.5,
    )
    arrow(ax, (0.702, 0.32), (0.745, 0.32), color=VERMILLION, linestyle="--")

    rounded_box(
        ax,
        0.12,
        0.065,
        0.83,
        0.095,
        "Proof certificate only: recurrence  →  Laurent/admissible tuples  →  local identity  "
        "→  transfer flows  →  finite $D_m$ formula",
        facecolor="white",
        edgecolor=MID_GRAY,
        fontsize=7.7,
    )

    save_figure(
        fig,
        output_dir,
        contract["stem"],
        "Transparent recurrence-to-Laurent-to-binomial-to-transfer-flow certificate for the all-degree slope formula.",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()
