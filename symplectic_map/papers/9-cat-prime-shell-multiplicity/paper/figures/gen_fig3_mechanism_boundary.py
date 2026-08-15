#!/usr/bin/env python3
"""Generate Figure 3: scalar, normalization, selector, and escape boundary."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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
    PURPLE,
    VERMILLION,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig3_mechanism_boundary"


def _fractional_summary(weights) -> str:
    counts = Counter(weights)
    parts = []
    for value in sorted(counts):
        count = counts[value]
        exact = fraction_text(value)
        parts.append(exact if count == 1 else f"{count} x {exact}")
    return "; ".join(parts)


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    symbolic = payload["symbolic_composite_control"]
    proof_only = payload["proof_only_contract"]

    if (
        symbolic.get("q_value") is not None
        or symbolic.get("q_is_symbolic") is not True
        or symbolic.get("composite_shells_enumerated") != 0
        or symbolic.get("numeric_q_inputs") != 0
    ):
        raise RuntimeError("symbolic composite boundary changed")
    if proof_only.get("centralizer_computations_run") != 0:
        raise RuntimeError("centralizer was unexpectedly computed")

    fig = plt.figure(figsize=(7.2, 5.0), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.92, 1.18],
        width_ratios=[1.0, 1.17],
        hspace=0.52,
        wspace=0.34,
        left=0.065,
        right=0.98,
        bottom=0.18,
        top=0.94,
    )

    # A: route decision cards.
    ax_a = fig.add_subplot(grid[0, :])
    clean_axis(ax_a)
    panel_label(ax_a, "A", "five mechanism statuses")
    cards = [
        (
            "fixed nonzero\nscalars",
            "FAIL (odd $p$)\ndegree $m_p>1$",
            PALE_RED,
            VERMILLION,
            "xx",
        ),
        (
            "equal scalars\n$w_\\gamma=1/m_p$",
            "$r=1$ ONLY\n$m_p^{1-r}$",
            PALE_ORANGE,
            ORANGE,
            "//",
        ),
        (
            "fractional shell\n$|\\gamma|/(p^2-1)$",
            "EXACT / GLOBAL\nnon-prime-specific",
            PALE_GREEN,
            GREEN,
            "..",
        ),
        (
            "one-orbit\nselector",
            "EXACT / DISCARD\n$m_p-1$ cycles",
            PALE_ORANGE,
            ORANGE,
            "\\\\",
        ),
        (
            "centralizer quotient",
            "UNTESTED\nfollow-up route",
            PALE_BLUE,
            BLUE,
            None,
        ),
    ]
    gap = 0.012
    width = (0.98 - 4 * gap) / 5
    for index, (heading, status, face, edge, hatch) in enumerate(cards):
        x = 0.01 + index * (width + gap)
        rounded_box(
            ax_a,
            x,
            0.34,
            width,
            0.50,
            heading + "\n\n" + status,
            facecolor=face,
            edgecolor=edge,
            hatch=hatch,
            linewidth=1.05,
            fontsize=6.05,
        )
    ax_a.text(
        0.5,
        0.08,
        "Only the pure scalar denominator family is obstructed; richer matrix/numerator/Fredholm mechanisms remain outside the theorem.",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        fontsize=7.25,
        color=MID_GRAY,
    )

    # B: equal-weight power sums.
    ax_b = fig.add_subplot(grid[1, 0])
    panel_label(ax_b, "B", "equal-weight power sums")
    exact = [row["equal_power_sums"] for row in rows]
    cmap = plt.get_cmap("YlOrBr")
    for y, values in enumerate(exact):
        for x, value in enumerate(values):
            ax_b.add_patch(
                Rectangle(
                    (x - 0.5, y - 0.5),
                    1,
                    1,
                    facecolor=cmap(float(value)),
                    edgecolor="white",
                    linewidth=1.2,
                )
            )
            ax_b.text(
                x,
                y,
                fraction_text(value),
                ha="center",
                va="center",
                fontsize=7.8,
                color="white" if float(value) >= 0.75 else BLACK,
                fontweight="bold" if value == 1 else "normal",
            )
    ax_b.set_xlim(-0.5, 2.5)
    ax_b.set_ylim(len(rows) - 0.5, -0.5)
    ax_b.set_aspect("auto")
    ax_b.set_xticks([0, 1, 2], [r"$r=1$", r"$r=2$", r"$r=3$"])
    ax_b.set_yticks(list(range(len(rows))), [rf"$p={row['prime']}$" for row in rows])
    ax_b.set_xlabel(r"$\sum_\gamma w_\gamma^r$ (target $=1$)")
    ax_b.set_xticks(np.arange(-0.5, 3, 1), minor=True)
    ax_b.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
    ax_b.grid(which="minor", color="white", linewidth=1.2)
    ax_b.tick_params(which="minor", bottom=False, left=False)
    for spine in ax_b.spines.values():
        spine.set_visible(True)
        spine.set_color(MID_GRAY)
        spine.set_linewidth(0.6)
    # C: fractional weights and selector costs.
    ax_c = fig.add_subplot(grid[1, 1])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "exact repair and construction cost")
    columns = (0.05, 0.19, 0.55, 0.88)
    ax_c.text(columns[0], 0.88, "$p$", transform=ax_c.transAxes, fontweight="bold", ha="center")
    ax_c.text(columns[1], 0.88, "$m_p$", transform=ax_c.transAxes, fontweight="bold", ha="center")
    ax_c.text(
        columns[2], 0.895, "fractional\nexponents", transform=ax_c.transAxes,
        fontweight="bold", ha="center", va="center", fontsize=6.9, linespacing=1.0,
    )
    ax_c.text(
        columns[3], 0.895, "selector\ndiscards", transform=ax_c.transAxes,
        fontweight="bold", ha="center", va="center", fontsize=6.9, linespacing=1.0,
    )
    row_y = [0.76, 0.64, 0.52, 0.40, 0.28]
    for y, row in zip(row_y, rows):
        shade = PALE_BLUE if row["prime"] == 2 else PALE_ORANGE if row["prime"] == 5 else "white"
        ax_c.add_patch(
            Rectangle(
                (0.01, y - 0.045),
                0.97,
                0.09,
                transform=ax_c.transAxes,
                facecolor=shade,
                edgecolor="none",
                zorder=0,
            )
        )
        ax_c.text(columns[0], y, str(row["prime"]), transform=ax_c.transAxes, ha="center", va="center")
        ax_c.text(columns[1], y, str(row["m_p"]), transform=ax_c.transAxes, ha="center", va="center")
        ax_c.text(
            columns[2],
            y,
            _fractional_summary(row["fractional_weights"]),
            transform=ax_c.transAxes,
            ha="center",
            va="center",
            fontsize=7.2,
        )
        ax_c.text(
            columns[3],
            y,
            str(row["selector_discards"]),
            transform=ax_c.transAxes,
            ha="center",
            va="center",
            fontsize=7.5,
        )
    ax_c.plot([0.01, 0.98], [0.83, 0.83], transform=ax_c.transAxes, color=MID_GRAY, linewidth=0.7)
    rounded_box(
        ax_c,
        0.03,
        0.015,
        0.94,
        0.15,
        "symbolic composite control: $J_2(q)$ shell, $q$ unspecified\n"
        "partition identity exact • no composite scan",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        hatch="..",
        fontsize=6.7,
    )

    fig.text(
        0.5,
        0.025,
        "Classification: A0 fails by global normalization only; the follow-up centralizer route is not opened.",
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
        metadata_title="Scalar, normalization, selector, and centralizer boundary",
    )


if __name__ == "__main__":
    main()
