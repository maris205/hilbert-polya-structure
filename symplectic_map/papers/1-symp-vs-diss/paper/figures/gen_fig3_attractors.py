#!/usr/bin/env python3
"""Plot the post-validation dissipative-attractor mechanism diagnostic."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper_plot_style import COLORS, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parents[1]
CSV_PATH = PAPER_ROOT / "results" / "attractors" / "attractor_diagnostics_v1_summary.csv"
UC = 1.5436890126920763


def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle) if abs(float(row["a"]) - UC) < 1e-12]
    rho = np.array([float(row["rho"]) for row in rows])
    n = np.array([float(row["n_trajectories"]) for row in rows])
    series = {
        "unresolved": np.array([float(row["unresolved"]) for row in rows]) / n,
        "period 8": np.array([float(row["period_8"]) for row in rows]) / n,
        "period 4": np.array([float(row["period_4"]) for row in rows]) / n,
        "period 2": np.array([float(row["period_2"]) for row in rows]) / n,
        "positive fixed point": np.array([float(row["fixed_positive"]) for row in rows]) / n,
        "escaped": np.array([float(row["escaped"]) for row in rows]) / n,
    }
    colors = ["#999999", COLORS["purple"], COLORS["sky"], COLORS["green"],
              COLORS["blue"], COLORS["orange"]]
    fig, ax = plt.subplots(figsize=(4.1, 2.65))
    ax.stackplot(rho, *series.values(), labels=series.keys(), colors=colors,
                 alpha=0.86, linewidth=0)
    threshold = float(rows[0]["rho_flip"])
    ax.axvline(threshold, color=COLORS["black"], linewidth=0.9,
               linestyle=(0, (3, 2)), label=r"analytic $\rho_{\rm PD}$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r"conformal factor $\rho$")
    ax.set_ylabel("diagnostic ensemble fraction")
    ax.legend(frameon=False, fontsize=7, ncol=2, loc="upper center",
              bbox_to_anchor=(0.52, -0.22), columnspacing=0.8,
              handlelength=1.5)
    ax.tick_params(direction="out", length=3, width=0.7)
    save_figure(fig, "fig3_dissipative_attractors")


if __name__ == "__main__":
    main()

