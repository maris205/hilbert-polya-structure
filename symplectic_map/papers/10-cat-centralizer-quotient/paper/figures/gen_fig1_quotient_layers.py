#!/usr/bin/env python3
"""Generate Figure 1: quotient layers and information loss."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

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
    PALE_RED,
    PURPLE,
    VERMILLION,
    arrow,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig1_quotient_layers"


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    p5 = next(row for row in rows if row["q"] == 5)
    p11 = next(row for row in rows if row["q"] == 11)

    fig = plt.figure(figsize=(7.2, 4.8), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.98, 1.16],
        width_ratios=[0.96, 1.04],
        hspace=0.46,
        wspace=0.30,
        left=0.055,
        right=0.98,
        bottom=0.12,
        top=0.94,
    )

    # A: shell versus cyclic locus.
    ax_a = fig.add_subplot(grid[0, :])
    clean_axis(ax_a)
    panel_label(ax_a, "A", "shell, cyclic locus, and the exact torsor")
    rounded_box(
        ax_a,
        0.01,
        0.22,
        0.24,
        0.58,
        "$E_q$\nexact additive-order shell\n$|E_q|=J_2(q)$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.7,
    )
    rounded_box(
        ax_a,
        0.34,
        0.22,
        0.28,
        0.58,
        "$\\mathrm{CV}_q\\subseteq E_q$\n$\\Delta_q(v)\\in R_q^\\times$\n"
        "$U\\mapsto Ue_1$ is bijective",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        hatch="..",
        fontsize=7.7,
    )
    rounded_box(
        ax_a,
        0.72,
        0.22,
        0.27,
        0.58,
        "$C_q=R_q[A]^\\times$\nfull local centralizer\n"
        "$|C_q|=|\\mathrm{CV}_q|$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=7.7,
    )
    arrow(ax_a, (0.255, 0.51), (0.335, 0.51), color=MID_GRAY)
    arrow(ax_a, (0.625, 0.51), (0.715, 0.51), color=MID_GRAY)
    ax_a.text(
        0.295,
        0.84,
        "retain cyclic\nvectors",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        color=VERMILLION,
        fontsize=5.4,
        linespacing=1.0,
    )
    ax_a.text(
        0.295,
        0.17,
        f"discard controls\nq=5: {p5['discard']}; q=11: {p11['discard']}",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        color=VERMILLION,
        fontsize=5.4,
        linespacing=1.0,
    )
    ax_a.text(
        0.67,
        0.08,
        "all-$q$ theorem: torsor equality; displayed discard counts are fixed prime controls",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        color=MID_GRAY,
        fontsize=6.4,
    )

    # B: quotient pipeline.
    ax_b = fig.add_subplot(grid[1, 0])
    clean_axis(ax_b)
    panel_label(ax_b, "B", "three quotient layers")
    rounded_box(
        ax_b,
        0.02,
        0.69,
        0.30,
        0.20,
        "$\\mathrm{CV}_q\\simeq C_q$\ncyclic vectors",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        fontsize=7.4,
    )
    rounded_box(
        ax_b,
        0.37,
        0.69,
        0.32,
        0.20,
        "$C_q/\\langle A\\rangle$\ncyclic $A$-orbits",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.4,
    )
    arrow(ax_b, (0.325, 0.79), (0.365, 0.79), color=MID_GRAY)
    rounded_box(
        ax_b,
        0.03,
        0.25,
        0.39,
        0.25,
        "quotient by full $C_q$\nONE CLASS\n$A_{\\rm quot}=\\mathrm{id}$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=7.3,
    )
    rounded_box(
        ax_b,
        0.54,
        0.25,
        0.43,
        0.25,
        "quotient by $C_q^1$\n$|\\operatorname{im}N_q|$ CLASSES\n"
        "$A_{\\rm quot}=\\mathrm{id}$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        hatch="..",
        fontsize=7.3,
    )
    arrow(ax_b, (0.52, 0.68), (0.25, 0.51), color=ORANGE, connectionstyle="arc3,rad=0.12")
    arrow(ax_b, (0.59, 0.68), (0.75, 0.51), color=BLUE, connectionstyle="arc3,rad=-0.10")
    ax_b.text(
        0.5,
        0.06,
        "Both coarse quotient clocks are erased because $A\\in C_q^1\\subset C_q$.",
        transform=ax_b.transAxes,
        ha="center",
        va="center",
        color=VERMILLION,
        fontsize=7.0,
        fontweight="bold",
    )

    # C: information-retention ledger.
    ax_c = fig.add_subplot(grid[1, 1])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "what each layer retains")
    headers = ("layer", "cyclic\nclasses", "$\\Delta$/norm\nlabel", "noncyclic\nstrata")
    x = (0.03, 0.52, 0.74, 0.92)
    for xpos, label in zip(x, headers):
        ax_c.text(
            xpos,
            0.88,
            label,
            transform=ax_c.transAxes,
            ha="left" if xpos == x[0] else "center",
            va="center",
            fontsize=6.2,
            fontweight="bold",
            linespacing=1.0,
        )
    table_rows = [
        ("full $C_q$", "1", "erased", "separate\nin $E_q$", PALE_ORANGE, ORANGE, "//"),
        ("symplectic $C_q^1$", "$|\\mathrm{im}N_q|$", "retained", "separate", PALE_BLUE, BLUE, ".."),
        ("reversor extension", "pairs $d,-d$", "paired", "not mixed\nwith CV", PALE_GREEN, GREEN, "xx"),
    ]
    ys = (0.67, 0.44, 0.21)
    for y, (layer, classes, norm, strata, face, edge, hatch) in zip(ys, table_rows):
        ax_c.add_patch(
            Rectangle(
                (0.01, y - 0.085),
                0.98,
                0.17,
                transform=ax_c.transAxes,
                facecolor=face,
                edgecolor=edge,
                linewidth=0.7,
                hatch=hatch,
            )
        )
        ax_c.text(x[0], y, layer, transform=ax_c.transAxes, ha="left", va="center", fontsize=5.7)
        ax_c.text(x[1], y, classes, transform=ax_c.transAxes, ha="center", va="center", fontsize=6.2)
        ax_c.text(x[2], y, norm, transform=ax_c.transAxes, ha="center", va="center", fontsize=6.1)
        ax_c.text(x[3], y, strata, transform=ax_c.transAxes, ha="center", va="center", fontsize=5.8)
    ax_c.text(
        0.5,
        0.015,
        "Burnside / orbifold / stacky refinements:\noutside scope, not rejected",
        transform=ax_c.transAxes,
        ha="center",
        va="bottom",
        color=PURPLE,
        fontsize=5.9,
        linespacing=1.05,
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
        metadata_title="Cat-map centralizer quotient layers and information loss",
    )


if __name__ == "__main__":
    main()
