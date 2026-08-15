#!/usr/bin/env python3
"""Generate Figure 1: definition-sensitive information-retention hierarchy."""

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
    LIGHT_GRAY,
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


STEM = "fig1_retention_hierarchy"


def build_figure():
    payload = load_frozen_payload()
    q2 = next(row for row in payload["rows"] if row["q"] == 2)
    q4 = next(row for row in payload["rows"] if row["q"] == 4)

    fig = plt.figure(figsize=(7.2, 5.25), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.98, 1.13],
        width_ratios=[1.14, 0.86],
        hspace=0.43,
        wspace=0.28,
        left=0.045,
        right=0.985,
        bottom=0.105,
        top=0.945,
    )

    # A: named constructions and their two information paths.
    ax_a = fig.add_subplot(grid[0, :])
    clean_axis(ax_a)
    panel_label(ax_a, "A", "named carriers retain different information")
    rounded_box(
        ax_a,
        0.01,
        0.36,
        0.16,
        0.27,
        "regular torsor\n" + r"$X_q\simeq G_q$" + "\n" + r"$\phi_q=L_{a_q}$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=6.6,
    )

    top_boxes = [
        (
            0.23,
            "point-order / fixed-point\nBurnside zeta (2008)\n"
            r"$\operatorname{supp}=r_q$; class $\mathbf{u}_q/r_q$",
            PALE_BLUE,
            BLUE,
            "..",
        ),
        (
            0.49,
            "point orbifold reduction (2015)\n"
            r"$(\operatorname{supp},\operatorname{exp})=(r_q,1/r_q)$",
            PALE_GREEN,
            GREEN,
            "//",
        ),
        (
            0.75,
            r"labelled $\mathbb{Z}\!\times\!G_q$ / enhanced" + "\n"
            + r"records $a_q^{-1}$ / $a_q$" + "\n(2013 / 2018)",
            PALE_PURPLE,
            PURPLE,
            "xx",
        ),
    ]
    bottom_boxes = [
        (
            0.23,
            "coarse quotient\n" + r"$X_q/G_q=\{*\}$" + "\nidentity dynamics",
            PALE_ORANGE,
            ORANGE,
            "//",
        ),
        (
            0.49,
            "orbit-order Burnside zeta (2015)\n"
            r"$\operatorname{supp}=1$; class $\mathbf{u}_q$",
            PALE_ORANGE,
            ORANGE,
            "..",
        ),
        (
            0.75,
            "quotient stack / inertia\nonly identity sector on torsor\n"
            "static period $1$",
            PALE_RED,
            VERMILLION,
            "xx",
        ),
    ]
    for x, text, face, edge, hatch in top_boxes:
        rounded_box(
            ax_a,
            x,
            0.61,
            0.23,
            0.28,
            text,
            facecolor=face,
            edgecolor=edge,
            hatch=hatch,
            fontsize=5.8,
        )
    for x, text, face, edge, hatch in bottom_boxes:
        rounded_box(
            ax_a,
            x,
            0.10,
            0.23,
            0.28,
            text,
            facecolor=face,
            edgecolor=edge,
            hatch=hatch,
            fontsize=5.8,
        )
    arrow(ax_a, (0.175, 0.55), (0.225, 0.73), color=BLUE, connectionstyle="arc3,rad=-0.10")
    arrow(ax_a, (0.175, 0.45), (0.225, 0.24), color=ORANGE, connectionstyle="arc3,rad=0.10")
    arrow(ax_a, (0.455, 0.75), (0.485, 0.75), color=GREEN)
    arrow(ax_a, (0.715, 0.75), (0.745, 0.75), color=PURPLE)
    arrow(ax_a, (0.455, 0.24), (0.485, 0.24), color=ORANGE)
    arrow(ax_a, (0.715, 0.24), (0.745, 0.24), color=VERMILLION)
    ax_a.text(
        0.20,
        0.80,
        "retain source\norder / twist",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        fontsize=5.3,
        color=BLUE,
        linespacing=1.0,
    )
    ax_a.text(
        0.20,
        0.18,
        "compress to\nstatic quotient",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        fontsize=5.3,
        color=VERMILLION,
        linespacing=1.0,
    )

    # B: information matrix. Text, not hue, carries the conclusion.
    ax_b = fig.add_subplot(grid[1, 0])
    clean_axis(ax_b)
    panel_label(ax_b, "B", "information ledger on the regular torsor")
    headers = ("carrier", "order\n$r_q$", "orbit\ntype", "labelled\ntwist", "isotropy", "native\nperiod")
    x_edges = (0.01, 0.33, 0.46, 0.59, 0.74, 0.87, 0.99)
    for left, right, header in zip(x_edges[:-1], x_edges[1:], headers):
        ax_b.add_patch(
            Rectangle(
                (left, 0.86),
                right - left,
                0.12,
                transform=ax_b.transAxes,
                facecolor=LIGHT_GRAY,
                edgecolor="white",
                linewidth=0.8,
            )
        )
        ax_b.text(
            (left + right) / 2,
            0.92,
            header,
            transform=ax_b.transAxes,
            ha="center",
            va="center",
            fontsize=5.5,
            fontweight="bold",
            linespacing=0.95,
        )
    rows = [
        ("point Burnside", "yes", "$[G/1]$", "subgroup only", "marks", "$r_q$", PALE_BLUE),
        ("point orbifold", "yes", "scalar", "no", "weight", "$r_q$", PALE_GREEN),
        ("orbit Burnside", "no", "$[G/1]$", "no", "marks", "$1$", PALE_ORANGE),
        (r"$\mathbb{Z}\!\times\!G$ perm.", "yes", "yes", r"$a_q^{-1}$", "yes", "labelled", PALE_PURPLE),
        ("enhanced carrier", "yes", "yes", "$a_q$", "character", "labelled", PALE_PURPLE),
        ("stack / inertia", "no", "$B1$", "no", "identity", "$1$", PALE_RED),
    ]
    row_height = 0.125
    for index, row in enumerate(rows):
        y = 0.85 - (index + 1) * row_height
        values, face = row[:-1], row[-1]
        for left, right, value in zip(x_edges[:-1], x_edges[1:], values):
            ax_b.add_patch(
                Rectangle(
                    (left, y),
                    right - left,
                    row_height - 0.006,
                    transform=ax_b.transAxes,
                    facecolor=face,
                    edgecolor="white",
                    linewidth=0.8,
                    hatch=".." if index in (0, 3, 4) else None,
                )
            )
            ax_b.text(
                (left + right) / 2,
                y + (row_height - 0.006) / 2,
                value,
                transform=ax_b.transAxes,
                ha="center",
                va="center",
                fontsize=5.35,
            )
    ax_b.text(
        0.5,
        0.015,
        "The rows are distinct established constructions; this is not a universal dominance order.",
        transform=ax_b.transAxes,
        ha="center",
        va="bottom",
        fontsize=5.8,
        color=MID_GRAY,
    )

    # C: the exact four scalar reductions and scope-corrected exception.
    ax_c = fig.add_subplot(grid[1, 1])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "scalar support/exponent ledger")
    ax_c.text(
        0.02,
        0.90,
        "reduction",
        transform=ax_c.transAxes,
        ha="left",
        va="center",
        fontsize=6.1,
        fontweight="bold",
    )
    ax_c.text(
        0.62,
        0.90,
        "support / exponent",
        transform=ax_c.transAxes,
        ha="center",
        va="center",
        fontsize=5.9,
        fontweight="bold",
    )
    ax_c.text(
        0.97,
        0.90,
        "scope",
        transform=ax_c.transAxes,
        ha="right",
        va="center",
        fontsize=5.9,
        fontweight="bold",
    )
    scalar_rows = [
        (
            r"$\kappa$(point)",
            "support $r_q$;\nexponent $m_q$",
            PALE_BLUE,
            BLUE,
            "unit when\n$m_q=1$",
        ),
        (r"$\Phi$(point)", r"$(r_q,1/r_q)$", PALE_GREEN, GREEN, "fractional"),
        (r"$\kappa$(orbit)", r"$(1,n_q)$", PALE_ORANGE, ORANGE, "static support"),
        (r"$\Phi$(orbit)", r"$(1,1)$", PALE_RED, VERMILLION, "static unit"),
    ]
    y_values = (0.74, 0.58, 0.42, 0.26)
    for y, (name, pair, face, edge, note) in zip(y_values, scalar_rows):
        ax_c.add_patch(
            Rectangle(
                (0.01, y - 0.065),
                0.98,
                0.13,
                transform=ax_c.transAxes,
                facecolor=face,
                edgecolor=edge,
                linewidth=0.8,
                hatch=".." if name == "$\\kappa$(point)" else None,
            )
        )
        ax_c.text(0.04, y, name, transform=ax_c.transAxes, ha="left", va="center", fontsize=5.8)
        pair_size = 5.0 if name == "$\\kappa$(point)" else 6.4
        ax_c.text(
            0.62,
            y,
            pair,
            transform=ax_c.transAxes,
            ha="center",
            va="center",
            fontsize=pair_size,
            linespacing=0.95,
        )
        ax_c.text(
            0.975,
            y,
            note,
            transform=ax_c.transAxes,
            ha="right",
            va="center",
            fontsize=4.55,
            linespacing=0.95,
        )

    q2_label = rf"$q=2:\ \kappa(\mathrm{{point}})=({q2['r']},{q2['m']})^\star$"
    rounded_box(
        ax_c,
        0.03,
        0.018,
        0.94,
        0.145,
        q2_label + "\nsole locked row/type exception.\n"
        + rf"$r_2=r_4={q4['r']}$: support $3$ does not identify $q$.",
        facecolor=PALE_RED,
        edgecolor=VERMILLION,
        hatch="xx",
        fontsize=5.15,
        linewidth=1.0,
    )

    fig.text(
        0.5,
        0.023,
        "Family-level conclusion: no one scalar-reduction type combines source support and unit exponent uniformly over all nine locked rows.",
        ha="center",
        va="bottom",
        color=BLACK,
        fontsize=6.4,
        fontweight="bold",
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
        metadata_title="Definition-sensitive information retention in equivariant cat-map quotients",
    )


if __name__ == "__main__":
    main()
