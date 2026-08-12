#!/usr/bin/env python3
"""Plot the frozen magnetic-field response and its mesh check."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from paper_plot_style import COLORS, panel_label, save_figure

PROJECT = Path(__file__).resolve().parents[1]


def main() -> None:
    r100 = json.loads((PROJECT / "results/r100_quantum_spectrum/summary.json").read_text(encoding="utf-8"))
    scan = json.loads((PROJECT / "results/r103_magnetic_crossover/summary.json").read_text(encoding="utf-8"))
    check = json.loads((PROJECT / "results/r104_crossover_grid_check/summary.json").read_text(encoding="utf-8"))
    records = sorted(scan["records"], key=lambda row: float(row["field"]))
    fields = np.asarray([float(row["field"]) for row in records])
    fine = np.asarray([float(row["diagnostics"]["mean_spacing_ratio"]) for row in records])
    check_by_field = {float(row["field"]): row for row in check["records"]}
    references = r100["reference_mean_ratios"]

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.3), constrained_layout=True)
    scan_positions = np.arange(len(fields))
    axes[0].plot(scan_positions, fine, marker="o", color=COLORS["blue"])
    axes[0].axhline(references["GOE"], color=COLORS["grey"], linestyle="--", label="GOE mean")
    axes[0].axhline(references["GUE"], color=COLORS["black"], linestyle=":", label="GUE mean")
    axes[0].set_xlabel(r"frozen field value $B$ (categorical spacing)")
    axes[0].set_ylabel(r"mean adjacent ratio $\langle\widetilde r\rangle$")
    axes[0].set_xticks(scan_positions, [f"{field:g}" for field in fields])
    axes[0].legend(loc="lower right")
    panel_label(axes[0], "(a)")

    checked_fields = np.asarray(sorted(check_by_field))
    coarse = np.asarray([check_by_field[field]["coarse_diagnostics"]["mean_spacing_ratio"] for field in checked_fields])
    fine_checked = np.asarray([check_by_field[field]["fine_diagnostics"]["mean_spacing_ratio"] for field in checked_fields])
    checked_positions = np.arange(len(checked_fields))
    for position, left, right in zip(checked_positions, coarse, fine_checked):
        axes[1].plot([position, position], [left, right], color=COLORS["grey"], linewidth=1.0)
    axes[1].scatter(checked_positions, coarse, facecolors="white", edgecolors=COLORS["grey"], marker="o", label=r"$h=0.03$")
    axes[1].scatter(checked_positions, fine_checked, color=COLORS["blue"], marker="s", label=r"$h=0.0225$")
    axes[1].set_xlabel(r"frozen field value $B$ (categorical spacing)")
    axes[1].set_ylabel(r"mean adjacent ratio $\langle\widetilde r\rangle$")
    axes[1].set_xticks(checked_positions, [f"{field:g}" for field in checked_fields])
    axes[1].legend(loc="best")
    panel_label(axes[1], "(b)")

    save_figure(fig, "fig6_magnetic_crossover")


if __name__ == "__main__":
    main()
