#!/usr/bin/env python3
"""Generate Figure 2: exact nine-modulus centralizer ledger."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
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
    PALE_ORANGE,
    VERMILLION,
    panel_label,
    save_figure,
)


STEM = "fig2_nine_modulus_ledger"


def _shade_composites(ax, start: float = 4.5, end: float = 8.5) -> None:
    ax.axvspan(start, end, color=PALE_ORANGE, alpha=0.55, zorder=-5)
    ax.axvline(start, color=MID_GRAY, linestyle="--", linewidth=0.8, zorder=5)


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    labels = [str(row["q"]) for row in rows]
    xpos = np.arange(len(rows))

    fig = plt.figure(figsize=(7.2, 5.1), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[0.90, 1.18],
        width_ratios=[1.0, 1.0],
        hspace=0.52,
        wspace=0.28,
        left=0.095,
        right=0.985,
        bottom=0.14,
        top=0.94,
    )

    # A: full shell versus cyclic locus, with the torsor equality marker.
    ax_a = fig.add_subplot(grid[0, 0])
    panel_label(ax_a, "A", "shell, cyclic locus, and $|C_q|$")
    exact_shell = np.array([row["exact_shell"] for row in rows])
    cyclic = np.array([row["cyclic_locus"] for row in rows])
    width = 0.36
    ax_a.bar(
        xpos - width / 2,
        exact_shell,
        width,
        label="$|E_q|$",
        color=PALE_BLUE,
        edgecolor=BLUE,
        linewidth=0.8,
        hatch="//",
    )
    ax_a.bar(
        xpos + width / 2,
        cyclic,
        width,
        label="$|\\mathrm{CV}_q|$",
        color=GREEN,
        edgecolor=BLACK,
        linewidth=0.5,
    )
    ax_a.scatter(
        xpos + width / 2,
        cyclic,
        marker="D",
        s=18,
        facecolor=ORANGE,
        edgecolor=BLACK,
        linewidth=0.45,
        zorder=5,
        label="$|C_q|=|\\mathrm{CV}_q|$",
    )
    for index, row in enumerate(rows):
        if row["discard"]:
            ax_a.text(
                index - width / 2,
                row["exact_shell"] + 3.0,
                rf"$-{row['discard']}$",
                ha="center",
                va="bottom",
                fontsize=6.2,
                color=VERMILLION,
                fontweight="bold",
            )
    _shade_composites(ax_a)
    ax_a.set_xticks(xpos, labels)
    ax_a.set_xlabel("modulus $q$  (primes | composites)")
    ax_a.set_ylabel("exact cardinality")
    ax_a.set_ylim(0, max(exact_shell) * 1.20)
    ax_a.grid(axis="y", color=LIGHT_GRAY, linewidth=0.5)
    ax_a.set_axisbelow(True)
    ax_a.legend(frameon=False, loc="upper left", ncol=1, fontsize=6.2, handlelength=1.2)

    # B: acting groups and source A-orbit multiplicity.
    ax_b = fig.add_subplot(grid[0, 1])
    panel_label(ax_b, "B", "groups and source $A$-orbits")
    full_c = np.array([row["full_centralizer"] for row in rows])
    symp_c = np.array([row["symplectic_centralizer"] for row in rows])
    a_orbits = np.array([row["cyclic_A_orbits"] for row in rows])
    width_b = 0.25
    ax_b.bar(xpos - width_b, full_c, width_b, color=ORANGE, edgecolor=BLACK,
             linewidth=0.5, label="$|C_q|$")
    ax_b.bar(xpos, symp_c, width_b, color=BLUE, edgecolor=BLACK,
             linewidth=0.5, hatch="//", label="$|C_q^1|$")
    ax_b.bar(xpos + width_b, a_orbits, width_b, color=GREEN, edgecolor=BLACK,
             linewidth=0.5, hatch="..", label="cyclic $A$-orbits")
    _shade_composites(ax_b)
    ax_b.set_xticks(xpos, labels)
    ax_b.set_xlabel("modulus $q$  (primes | composites)")
    ax_b.set_ylabel("exact count")
    ax_b.set_ylim(0, max(full_c) * 1.18)
    ax_b.grid(axis="y", color=LIGHT_GRAY, linewidth=0.5)
    ax_b.set_axisbelow(True)
    ax_b.legend(frameon=False, loc="upper left", ncol=1, fontsize=6.4, handlelength=1.2)

    # C: quotient-class ledger.
    ax_c = fig.add_subplot(grid[1, :])
    panel_label(ax_c, "C", "quotient-class counts (exact annotations)")
    row_specs = [
        ("$\\mathrm{CV}/C$", "CV_over_C"),
        ("$\\mathrm{CV}/C^1$", "CV_over_C1"),
        ("$E/C$", "E_over_C"),
        ("$E/C^1$", "E_over_C1"),
        ("reversor $E$", "reversing_E"),
    ]
    numeric = [
        [row[key] if row[key] is not None else np.nan for row in rows]
        for _, key in row_specs
    ]
    norm = Normalize(vmin=1, vmax=12)
    cmap = plt.get_cmap("Blues")
    for y, values in enumerate(numeric):
        for x, value in enumerate(values):
            missing = bool(np.isnan(value))
            face = LIGHT_GRAY if missing else cmap(norm(float(value)))
            ax_c.add_patch(
                Rectangle(
                    (x - 0.5, y - 0.5),
                    1,
                    1,
                    facecolor=face,
                    edgecolor="white",
                    linewidth=1.3,
                    hatch="xx" if missing else None,
                )
            )
            label = "n/a" if missing else str(int(value))
            color = "white" if not missing and value >= 7 else BLACK
            ax_c.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                color=color,
                fontsize=7.6,
                fontweight="bold" if (not missing and value == 1) else "normal",
            )
    ax_c.set_xlim(-0.5, len(rows) - 0.5)
    ax_c.set_ylim(len(row_specs) - 0.5, -0.5)
    ax_c.set_xticks(xpos, [rf"$q={label}$" for label in labels])
    ax_c.set_yticks(np.arange(len(row_specs)), [name for name, _ in row_specs])
    ax_c.set_xlabel("frozen modulus order; reversing groups audited only at the five prime controls")
    ax_c.axvline(4.5, color=MID_GRAY, linestyle="--", linewidth=0.9)
    for spine in ax_c.spines.values():
        spine.set_visible(True)
        spine.set_color(MID_GRAY)
        spine.set_linewidth(0.6)

    fig.text(
        0.5,
        0.025,
        "Finite rows verify the implementation and fixed controls; all-$q$ formulas remain proof-sourced.",
        ha="center",
        va="bottom",
        color=MID_GRAY,
        fontsize=7.1,
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
        metadata_title="Exact nine-modulus cat-map centralizer ledger",
    )


if __name__ == "__main__":
    main()
