#!/usr/bin/env python3
"""Generate Figure 2: exact nine-row n/r/m ledger and period collisions."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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
    panel_label,
    save_figure,
)


STEM = "fig2_nine_row_retention"


def fraction_text(value: tuple[int, int]) -> str:
    numerator, denominator = value
    return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    labels = [str(row["q"]) for row in rows]
    xpos = np.arange(len(rows))

    fig = plt.figure(figsize=(7.2, 5.85), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.92, 1.20],
        width_ratios=[1.10, 0.90],
        hspace=0.48,
        wspace=0.30,
        left=0.075,
        right=0.985,
        bottom=0.115,
        top=0.945,
    )

    # A: exact torsor size, source order, and source-cycle multiplicity.
    ax_a = fig.add_subplot(grid[0, 0])
    panel_label(ax_a, "A", "exact regular-torsor ledger")
    width = 0.25
    n_values = np.array([row["n"] for row in rows])
    r_values = np.array([row["r"] for row in rows])
    m_values = np.array([row["m"] for row in rows])
    bars_n = ax_a.bar(
        xpos - width,
        n_values,
        width,
        color=BLUE,
        edgecolor=BLACK,
        linewidth=0.5,
        label="$n_q=|G_q|$",
    )
    bars_r = ax_a.bar(
        xpos,
        r_values,
        width,
        color=ORANGE,
        edgecolor=BLACK,
        linewidth=0.5,
        hatch="//",
        label=r"$r_q=\operatorname{ord}(a_q)$",
    )
    bars_m = ax_a.bar(
        xpos + width,
        m_values,
        width,
        color=GREEN,
        edgecolor=BLACK,
        linewidth=0.5,
        hatch="..",
        label="$m_q=n_q/r_q$",
    )
    for collection, values, y_offset in (
        (bars_n, n_values, 1.7),
        (bars_r, r_values, 1.2),
        (bars_m, m_values, 1.2),
    ):
        for bar, value in zip(collection, values):
            ax_a.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + y_offset,
                str(int(value)),
                ha="center",
                va="bottom",
                fontsize=5.2,
                color=BLACK,
            )
    ax_a.axvspan(4.5, 8.5, color=PALE_ORANGE, alpha=0.55, zorder=-5)
    ax_a.axvline(4.5, color=MID_GRAY, linestyle="--", linewidth=0.8)
    ax_a.set_xticks(xpos, labels)
    ax_a.set_xlabel("frozen modulus order  (primes | composites)")
    ax_a.set_ylabel("exact integer")
    ax_a.set_ylim(0, 118)
    ax_a.grid(axis="y", color=LIGHT_GRAY, linewidth=0.5)
    ax_a.set_axisbelow(True)
    ax_a.legend(frameon=False, loc="upper left", fontsize=5.7, handlelength=1.2)

    # B: exact order collisions, preserving the registered order.
    ax_b = fig.add_subplot(grid[0, 1])
    panel_label(ax_b, "B", "retained order does not identify $q$")
    prime_indices = [index for index, row in enumerate(rows) if row["kind"] == "prime"]
    composite_indices = [index for index, row in enumerate(rows) if row["kind"] == "composite"]
    ax_b.scatter(
        prime_indices,
        [rows[index]["r"] for index in prime_indices],
        s=44,
        marker="o",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        linewidth=1.0,
        zorder=4,
        label="prime control",
    )
    ax_b.scatter(
        composite_indices,
        [rows[index]["r"] for index in composite_indices],
        s=48,
        marker="s",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        linewidth=1.0,
        zorder=4,
        label="composite control",
    )
    for index, row in enumerate(rows):
        ax_b.text(
            index,
            row["r"] + 1.2,
            f"q={row['q']}",
            ha="center",
            va="bottom",
            fontsize=5.7,
        )
    collision_pairs = [((0, 5), 3, "$r_2=r_4=3$"), ((6, 7), 12, "$r_6=r_9=12$")]
    for (left, right), level, text in collision_pairs:
        ax_b.plot(
            [left, right],
            [level, level],
            color=VERMILLION,
            linewidth=1.4,
            linestyle="--",
            zorder=2,
        )
        ax_b.text(
            (left + right) / 2,
            level - 2.1,
            text,
            ha="center",
            va="top",
            color=VERMILLION,
            fontsize=6.2,
            fontweight="bold",
        )
    ax_b.axvspan(4.5, 8.5, color=PALE_ORANGE, alpha=0.55, zorder=-5)
    ax_b.axvline(4.5, color=MID_GRAY, linestyle="--", linewidth=0.8)
    ax_b.set_xticks(xpos, labels)
    ax_b.set_xlabel("registered row position  (primes | composites)")
    ax_b.set_ylabel("source support $r_q$")
    ax_b.set_xlim(-0.55, len(rows) - 0.45)
    ax_b.set_ylim(0, 35)
    ax_b.grid(axis="y", color=LIGHT_GRAY, linewidth=0.5)
    ax_b.set_axisbelow(True)
    ax_b.legend(frameon=False, loc="upper left", fontsize=5.7, handletextpad=0.4)

    # C: all 36 scalar reduction pairs. The q=2 exception is explicit.
    ax_c = fig.add_subplot(grid[1, :])
    panel_label(ax_c, "C", "exact scalar pairs: cell = (support, exponent)")
    row_specs = [
        (r"$\kappa$(point)", "point_cardinality", PALE_BLUE, BLUE),
        (r"$\Phi$(point)", "point_orbifold", PALE_GREEN, GREEN),
        (r"$\kappa$(orbit)", "orbit_cardinality", PALE_ORANGE, ORANGE),
        (r"$\Phi$(orbit)", "orbit_orbifold", PALE_PURPLE, PURPLE),
    ]
    for y, (row_name, key, face, edge) in enumerate(row_specs):
        for x, row in enumerate(rows):
            support, exponent = row[key]
            is_exception = row["q"] == 2 and key == "point_cardinality"
            cell_face = PALE_RED if is_exception else face
            cell_edge = VERMILLION if is_exception else "white"
            cell_width = 1.0
            ax_c.add_patch(
                Rectangle(
                    (x - 0.5, y - 0.5),
                    cell_width,
                    1.0,
                    facecolor=cell_face,
                    edgecolor=cell_edge,
                    linewidth=1.6 if is_exception else 1.0,
                    hatch="xx" if is_exception else (".." if y == 0 else None),
                )
            )
            label = f"({support},{fraction_text(exponent)})"
            if is_exception:
                label = rf"$({support},1)^\star$"
            ax_c.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                fontsize=6.15,
                color=BLACK,
                fontweight="bold" if is_exception else "normal",
            )
        ax_c.text(
            len(rows) - 0.36,
            y - 0.36,
            "source support" if y < 2 else "static support",
            ha="right",
            va="bottom",
            fontsize=4.7,
            color=edge,
        )
    ax_c.set_xlim(-0.5, len(rows) - 0.5)
    ax_c.set_ylim(len(row_specs) - 0.5, -0.5)
    ax_c.set_xticks(xpos, [rf"$q={label}$" for label in labels])
    ax_c.set_yticks(np.arange(len(row_specs)), [item[0] for item in row_specs])
    ax_c.axvline(4.5, color=MID_GRAY, linestyle="--", linewidth=0.9)
    ax_c.set_xlabel(
        r"$^\star q=2$: sole locked row/type pair with source support and unit exponent; "
        "no family-uniform starred column."
    )
    for spine in ax_c.spines.values():
        spine.set_visible(True)
        spine.set_color(MID_GRAY)
        spine.set_linewidth(0.6)

    fig.text(
        0.5,
        0.026,
        r"$q=2$ gives $(3,1)^\star$, but $r_2=r_4=3$: the sole exception is not modulus-specific.",
        ha="center",
        va="bottom",
        color=VERMILLION,
        fontsize=6.6,
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
        metadata_title="Exact nine-row cat-map equivariant retention ledger and collisions",
    )


if __name__ == "__main__":
    main()
