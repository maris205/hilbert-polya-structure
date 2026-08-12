#!/usr/bin/env python3
"""Generate finite-audit diagnostics from frozen CSV and JSON artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from paper_plot_style import COLORS, save_figure


PAPER_ROOT = Path(__file__).resolve().parents[1]


def read_json(relative_path: str) -> dict:
    with (PAPER_ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def gauss_panel(ax: plt.Axes) -> None:
    table = pd.read_csv(PAPER_ROOT / "farey_gauss_transfer/results/cutoff_table.csv")
    summary = read_json("farey_gauss_transfer/results/summary.json")
    max_word = table["word_max"].max()
    rows = table.loc[table["word_max"].eq(max_word)].sort_values("digit_max")
    observed_max = int(rows["primitive_necklaces"].max())
    recorded_max = int(summary["baseline_max_cutoff"]["orbit_count"])
    if observed_max != recorded_max:
        raise RuntimeError("Gauss CSV/JSON maximum-cutoff mismatch")

    x = rows["digit_max"].to_numpy()
    ax.plot(
        x,
        rows["primitive_necklaces"],
        marker="o",
        color=COLORS["blue"],
        label="primitive necklaces",
    )
    ax.plot(
        x,
        rows["nonreversal_collision_group_count"],
        marker="s",
        color=COLORS["orange"],
        label="non-reversal trace collisions",
    )
    ax.set_yscale("symlog", linthresh=1)
    ax.set_xticks(x)
    ax.set_xlabel(f"digit cutoff $D$ (word cutoff $L={max_word}$)")
    ax.set_ylabel("exact count (symlog)")
    ax.legend(frameon=False, loc="upper left")
    ax.text(-0.16, 1.03, "(a)", transform=ax.transAxes, fontweight="bold")


def wheel_panel(ax: plt.Axes) -> None:
    table = pd.read_csv(PAPER_ROOT / "wheel_sieve_level_shift/results/level_table.csv")
    certificate = read_json("wheel_sieve_level_shift/results/dag_certificate.json")
    max_level = int(table["level"].max())
    rows = table.loc[table["level"].eq(max_level)].copy()

    cycle_counts = [
        int(record["directed_cycle_count"])
        for record in certificate["certificates"].values()
    ]
    if len(cycle_counts) != len(rows) or any(cycle_counts):
        raise RuntimeError("wheel CSV/JSON control-count or acyclicity mismatch")

    display_order = ("arithmetic", "fixed_branch", "cyclic_branch", "random_branch")
    display_labels = ("arithmetic", "fixed", "cyclic", "random")
    for index, name in enumerate(display_order):
        values = rows.loc[rows["control"].eq(name), "unit_jaccard"].to_numpy(dtype=float)
        offsets = np.linspace(-0.11, 0.11, max(1, len(values)))
        color = COLORS["blue"] if name == "arithmetic" else COLORS["gray"]
        ax.scatter(
            index + offsets,
            values,
            s=34,
            color=color,
            edgecolor="white",
            linewidth=0.5,
            zorder=3,
        )
        if len(values) > 1:
            ax.hlines(values.mean(), index - 0.18, index + 0.18, color=COLORS["blue"], linewidth=1.5)

    ax.set_xticks(range(len(display_labels)), display_labels, rotation=20, ha="right")
    ax.set_ylim(-0.04, 1.08)
    ax.set_ylabel("unit-set Jaccard")
    ax.set_xlabel(f"matched controls at level {max_level}")
    ax.set_title(f"all {len(cycle_counts)} ledgers: 0 directed cycles", fontsize=9)
    ax.text(-0.16, 1.03, "(b)", transform=ax.transAxes, fontweight="bold")


def knauf_panel(ax: plt.Axes) -> None:
    table = pd.read_csv(
        PAPER_ROOT / "knauf_spin_chain_audit/results/final_grid_analytic_errors.csv"
    )
    summary = read_json("knauf_spin_chain_audit/results/summary.json")
    real_rows = table.loc[
        table["tau"].eq(0)
        & table["observable"].isin(["unsigned", "liouville"])
        & table["target_abs_error"].notna()
    ].copy()
    if int(real_rows["cutoff_k"].max()) != int(summary["final_cutoff_k"]):
        raise RuntimeError("Knauf CSV/JSON cutoff mismatch")

    styles = {
        "unsigned": (COLORS["blue"], "o"),
        "liouville": (COLORS["purple"], "s"),
    }
    for observable, rows in real_rows.groupby("observable", sort=False):
        rows = rows.sort_values("sigma")
        color, marker = styles[observable]
        ax.plot(
            rows["sigma"],
            rows["target_abs_error"],
            marker=marker,
            color=color,
            label=observable,
        )

    ax.axvspan(real_rows["sigma"].min(), 2.0, color=COLORS["light_gray"], alpha=0.45)
    ax.axvline(2.0, color="black", linewidth=0.8, linestyle=":")
    ax.set_yscale("log")
    ax.set_xlabel(r"$\mathrm{Re}(s)$ on the frozen real grid")
    ax.set_ylabel("absolute benchmark error")
    ax.legend(frameon=False, loc="upper right")
    ax.text(-0.16, 1.03, "(c)", transform=ax.transAxes, fontweight="bold")


def main() -> None:
    fig = plt.figure(figsize=(7.15, 6.4), constrained_layout=True)
    grid = fig.add_gridspec(2, 2, height_ratios=(1.0, 1.05))
    gauss_panel(fig.add_subplot(grid[0, :]))
    wheel_panel(fig.add_subplot(grid[1, 0]))
    knauf_panel(fig.add_subplot(grid[1, 1]))
    save_figure(fig, "fig2_finite_audits")


if __name__ == "__main__":
    main()
