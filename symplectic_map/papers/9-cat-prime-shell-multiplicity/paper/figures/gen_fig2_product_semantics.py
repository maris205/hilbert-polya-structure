#!/usr/bin/env python3
"""Generate Figure 2: raw-return versus one-time orbit-label semantics."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

from figure_data import fraction_text, load_frozen_payload
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
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig2_product_semantics"


def _raw_factor_tex(row: dict) -> str:
    pieces = []
    for factor in row["raw_factors"]:
        length = int(factor["orbit_length"])
        multiplicity = int(factor["denominator_multiplicity"])
        pieces.append(rf"(1-{row['prime']}^{{-{length}s}})^{{-{multiplicity}}}")
    return "".join(pieces)


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    p5 = next(row for row in rows if row["prime"] == 5)

    fig = plt.figure(figsize=(7.2, 4.75), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.92, 1.18],
        width_ratios=[1.05, 1.15],
        hspace=0.5,
        wspace=0.34,
        left=0.06,
        right=0.98,
        bottom=0.17,
        top=0.94,
    )

    # A: semantic construction pipelines.
    ax_a = fig.add_subplot(grid[0, :])
    clean_axis(ax_a)
    panel_label(ax_a, "A", "two different constructions")
    y_raw, y_label = 0.63, 0.18
    raw_boxes = [
        (0.01, 0.22, "point potential\n$L(x)=\\log p$"),
        (0.29, 0.25, "primitive return\n$|\\gamma|\\log p$"),
        (0.60, 0.37, "$Z_{\\rm raw,p}=\\prod_\\gamma$\n$(1-p^{-s|\\gamma|})^{-1}$"),
    ]
    label_boxes = [
        (0.01, 0.22, "external one-time\nshell label $\\log p$"),
        (0.29, 0.25, "$m_p$ primitive orbits\nall receive one label"),
        (0.60, 0.37, "$Z_{\\rm lab,p}$\n$=(1-p^{-s})^{-m_p}$"),
    ]
    for x, width, text in raw_boxes:
        rounded_box(
            ax_a,
            x,
            y_raw,
            width,
            0.25,
            text,
            facecolor=PALE_BLUE,
            edgecolor=BLUE,
            fontsize=7.8,
        )
    for x, width, text in label_boxes:
        rounded_box(
            ax_a,
            x,
            y_label,
            width,
            0.25,
            text,
            facecolor=PALE_ORANGE,
            edgecolor=ORANGE,
            fontsize=7.8,
            hatch="//",
        )
    for y in (y_raw + 0.125, y_label + 0.125):
        arrow(ax_a, (0.235, y), (0.285, y), color=MID_GRAY)
        arrow(ax_a, (0.55, y), (0.595, y), color=MID_GRAY)
    ax_a.text(
        0.958,
        y_raw + 0.125,
        "retains $|\\gamma|$",
        transform=ax_a.transAxes,
        ha="right",
        va="center",
        fontsize=6.9,
        color=BLUE,
        fontweight="bold",
    )
    ax_a.text(
        0.958,
        y_label + 0.125,
        "imports $m_p$",
        transform=ax_a.transAxes,
        ha="right",
        va="center",
        fontsize=6.9,
        color=VERMILLION,
        fontweight="bold",
    )
    ax_a.text(
        0.5,
        0.01,
        "Dividing a return by its period changes the label; it does not remove any denominator factor.",
        transform=ax_a.transAxes,
        ha="center",
        va="bottom",
        fontsize=7.3,
        color=MID_GRAY,
    )

    # B: ramified stress test.
    ax_b = fig.add_subplot(grid[1, 0])
    clean_axis(ax_b)
    panel_label(ax_b, "B", "ramified stress test at $p=5$")
    rounded_box(
        ax_b,
        0.03,
        0.62,
        0.94,
        0.25,
        "$Z_{\\rm raw,5}=" + _raw_factor_tex(p5) + "$\n"
        "$2$ cycles of length $2$; $2$ cycles of length $10$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        fontsize=7.6,
    )
    rounded_box(
        ax_b,
        0.03,
        0.26,
        0.94,
        0.22,
        rf"$Z_{{\rm lab,5}}=(1-5^{{-s}})^{{-{p5['m_p']}}}$"
        + "\n"
        + rf"one label on each of $m_5={p5['m_p']}$ primitive cycles",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        hatch="//",
        fontsize=7.7,
    )
    ax_b.text(
        0.5,
        0.045,
        "Raw mixed factor $\\ne$ relabeled degree-four factor.\n"
        "The constructions answer different questions.",
        transform=ax_b.transAxes,
        ha="center",
        va="center",
        fontsize=6.8,
        color=VERMILLION,
        fontweight="bold",
        linespacing=1.15,
    )

    # C: exact repetition ledger.
    ax_c = fig.add_subplot(grid[1, 1])
    panel_label(ax_c, "C", "orbit-label coefficient $m_p/r$")
    exact = [[value for value in row["label_coefficients"]] for row in rows]
    norm = Normalize(vmin=0, vmax=24)
    cmap = plt.get_cmap("Blues")
    for y, row_values in enumerate(exact):
        for x, value in enumerate(row_values):
            ax_c.add_patch(
                Rectangle(
                    (x - 0.5, y - 0.5),
                    1,
                    1,
                    facecolor=cmap(norm(float(value))),
                    edgecolor="white",
                    linewidth=1.2,
                )
            )
            color = "white" if float(value) >= 8 else BLACK
            ax_c.text(
                x,
                y,
                fraction_text(value),
                ha="center",
                va="center",
                color=color,
                fontsize=8.1,
                fontweight="bold",
            )
    ax_c.set_xlim(-0.5, 2.5)
    ax_c.set_ylim(len(rows) - 0.5, -0.5)
    ax_c.set_aspect("auto")
    ax_c.set_xticks([0, 1, 2], [r"$r=1$", r"$r=2$", r"$r=3$"])
    ax_c.set_yticks(list(range(len(rows))), [rf"$p={row['prime']}$" for row in rows])
    ax_c.set_xlabel("formal repetition (annotations are exact)")
    for spine in ax_c.spines.values():
        spine.set_visible(True)
        spine.set_color(MID_GRAY)
        spine.set_linewidth(0.6)
    ax_c.set_xticks(np.arange(-0.5, 3, 1), minor=True)
    ax_c.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
    ax_c.grid(which="minor", color="white", linewidth=1.2)
    ax_c.tick_params(which="minor", bottom=False, left=False)
    for tick, row in zip(ax_c.get_yticklabels(), rows):
        if row["prime"] == 2:
            tick.set_color(BLUE)
            tick.set_fontweight("bold")
        elif row["prime"] == 5:
            tick.set_color(VERMILLION)
            tick.set_fontweight("bold")
    fig.text(
        0.5,
        0.025,
        "All entries are symbolic exact controls; no numerical value of $s$ or $\\log p$ is evaluated.",
        ha="center",
        va="bottom",
        fontsize=7.2,
        color=MID_GRAY,
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
        metadata_title="Raw-return versus one-time orbit-label products",
    )


if __name__ == "__main__":
    main()
