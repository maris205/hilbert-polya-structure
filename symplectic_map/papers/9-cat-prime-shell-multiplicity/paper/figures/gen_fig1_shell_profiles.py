#!/usr/bin/env python3
"""Generate Figure 1: exact fixed-shell profiles and multiplicities."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

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
    PURPLE,
    SKY,
    VERMILLION,
    WHITE,
    clean_axis,
    panel_label,
    rounded_box,
    save_figure,
)


STEM = "fig1_shell_profiles"
PERIOD_COLORS = {
    2: VERMILLION,
    3: BLUE,
    4: SKY,
    5: GREEN,
    8: PURPLE,
    10: ORANGE,
}
CASE_LABELS = {
    "binary_inert": "binary boundary",
    "inert": "inert",
    "ramified": "ramified Jordan",
    "split": "split",
}


def build_figure():
    payload = load_frozen_payload()
    rows = payload["rows"]
    primes = [row["prime"] for row in rows]

    fig = plt.figure(figsize=(7.2, 4.45), constrained_layout=False)
    grid = GridSpec(
        2,
        2,
        figure=fig,
        height_ratios=[1.15, 0.95],
        width_ratios=[1.55, 1.0],
        hspace=0.52,
        wspace=0.38,
        left=0.085,
        right=0.98,
        bottom=0.08,
        top=0.94,
    )

    # A: point-period shell profiles.
    ax_a = fig.add_subplot(grid[0, 0])
    panel_label(ax_a, "A", "nonzero points by exact period")
    y_positions = list(range(len(rows)))
    left = [0] * len(rows)
    all_periods = sorted({period for row in rows for period in row["point_profile"]})
    for period in all_periods:
        values = [row["point_profile"].get(period, 0) for row in rows]
        bars = ax_a.barh(
            y_positions,
            values,
            left=left,
            height=0.62,
            color=PERIOD_COLORS[period],
            edgecolor=BLACK,
            linewidth=0.55,
            label=rf"period ${period}$",
        )
        for index, (bar, value) in enumerate(zip(bars, values)):
            if value:
                ax_a.text(
                    left[index] + value / 2,
                    bar.get_y() + bar.get_height() / 2,
                    str(value),
                    ha="center",
                    va="center",
                    fontsize=7.2,
                    color=WHITE if period in (2, 3, 8) else BLACK,
                    fontweight="bold",
                )
        left = [old + value for old, value in zip(left, values)]
    ax_a.set_yticks(y_positions, [rf"$p={prime}$" for prime in primes])
    ax_a.invert_yaxis()
    ax_a.set_xlim(0, max(row["shell_cardinality"] for row in rows) + 8)
    ax_a.set_xlabel(r"points in $V_p=\mathbf{F}_p^2\setminus\{0\}$")
    ax_a.grid(axis="x", color=LIGHT_GRAY, linewidth=0.6, zorder=0)
    ax_a.set_axisbelow(True)
    ax_a.legend(
        ncol=2,
        loc="upper right",
        bbox_to_anchor=(0.995, 0.995),
        frameon=True,
        framealpha=0.94,
        facecolor=WHITE,
        edgecolor=LIGHT_GRAY,
        columnspacing=0.7,
        handlelength=1.2,
    )
    for tick, prime in zip(ax_a.get_yticklabels(), primes):
        if prime == 2:
            tick.set_color(BLUE)
            tick.set_fontweight("bold")
        elif prime == 5:
            tick.set_color(VERMILLION)
            tick.set_fontweight("bold")

    # B: cycle multiplicity.
    ax_b = fig.add_subplot(grid[0, 1])
    panel_label(ax_b, "B", "primitive-orbit multiplicity")
    multiplicities = [row["m_p"] for row in rows]
    colors = [BLUE if p == 2 else ORANGE if p == 5 else MID_GRAY for p in primes]
    bars = ax_b.bar(
        list(range(len(rows))),
        multiplicities,
        color=colors,
        edgecolor=BLACK,
        linewidth=0.65,
        width=0.68,
    )
    for bar, value in zip(bars, multiplicities):
        ax_b.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.55,
            rf"$m_p={value}$",
            ha="center",
            va="bottom",
            fontsize=7.3,
            fontweight="bold" if value in (1, 4) else "normal",
        )
    ax_b.axhline(1, color=BLUE, linestyle="--", linewidth=0.9)
    ax_b.text(2.90, 1.28, "single factor", ha="right", va="bottom", color=BLUE, fontsize=6.8)
    ax_b.set_xticks(list(range(len(rows))), [str(p) for p in primes])
    ax_b.set_xlabel(r"prime $p$")
    ax_b.set_ylabel(r"$m_p=|\Gamma_p|$")
    ax_b.set_ylim(0, max(multiplicities) + 4.2)
    ax_b.grid(axis="y", color=LIGHT_GRAY, linewidth=0.6)
    ax_b.set_axisbelow(True)

    # C: exact boundary cards and the split stratum control.
    ax_c = fig.add_subplot(grid[1, :])
    clean_axis(ax_c)
    panel_label(ax_c, "C", "boundary cases and split stratum")
    p2 = next(row for row in rows if row["prime"] == 2)
    p5 = next(row for row in rows if row["prime"] == 5)
    p11 = next(row for row in rows if row["prime"] == 11)
    rounded_box(
        ax_c,
        0.01,
        0.28,
        0.27,
        0.57,
        "binary boundary  $p=2$\n"
        + rf"$|V_2|={p2['shell_cardinality']}$  •  period $3$: {p2['point_profile'][3]} points"
        + "\n"
        + rf"one length-$3$ cycle  •  $m_2={p2['m_p']}$",
        facecolor=PALE_BLUE,
        edgecolor=BLUE,
        linewidth=1.1,
        hatch="//",
    )
    rounded_box(
        ax_c,
        0.365,
        0.28,
        0.29,
        0.57,
        "ramified boundary  $p=5$\n"
        + rf"period $2$: {p5['point_profile'][2]} points / {p5['cycle_profile'][2]} cycles"
        + "\n"
        + rf"period $10$: {p5['point_profile'][10]} points / {p5['cycle_profile'][10]} cycles"
        + "\n"
        + rf"mixed shell  •  $m_5={p5['m_p']}$",
        facecolor=PALE_ORANGE,
        edgecolor=ORANGE,
        linewidth=1.1,
        hatch="xx",
        fontsize=7.7,
    )
    rounded_box(
        ax_c,
        0.72,
        0.28,
        0.27,
        0.57,
        "split control  $p=11$\n"
        + rf"{p11['cycle_profile'][5]} length-$5$ cycles  •  $m_{{11}}={p11['m_p']}$"
        + "\n"
        + rf"eigenlines: ${p11['eigenline_cycles']}$ cycles"
        + "\n"
        + rf"off eigenlines: ${p11['off_eigenline_cycles']}$ cycles",
        facecolor=PALE_GREEN,
        edgecolor=GREEN,
        linewidth=1.1,
        hatch="..",
        fontsize=7.7,
    )
    ax_c.text(
        0.5,
        0.06,
        "Five fixed rows are development-seen exact controls; uniqueness of $p=2$ and the odd-prime bound are proof-sourced.",
        transform=ax_c.transAxes,
        ha="center",
        va="bottom",
        color=MID_GRAY,
        fontsize=7.4,
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
        metadata_title="Fixed prime-shell profiles and primitive-orbit multiplicity",
    )


if __name__ == "__main__":
    main()
