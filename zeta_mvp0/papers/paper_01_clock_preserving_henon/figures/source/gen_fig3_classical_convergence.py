#!/usr/bin/env python3
"""Plot FTLE/SALI time convergence and the independent magnetic audit."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from paper_plot_style import COLORS, panel_label, save_figure

PROJECT = Path(__file__).resolve().parents[1]


def main() -> None:
    with (PROJECT / "results/r001_time_convergence/records.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    audit = json.loads((PROJECT / "results/r106_adaptive_magnetic_dynamics/summary.json").read_text(encoding="utf-8"))

    times = np.array([20, 40, 80, 160])
    groups = (
        (0.0, 1, r"$a=0,n=1$", COLORS["grey"], "o"),
        (1.02, 1, r"$a=1.02,n=1$", COLORS["blue"], "s"),
        (1.02, 2, r"$a=1.02,n=2$", COLORS["orange"], "^"),
        (6.0, 1, r"$a=6,n=1$", COLORS["green"], "D"),
    )

    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.25), gridspec_kw={"width_ratios": [1.1, 1.1, 0.9]}, constrained_layout=True)
    for a, n, label, color, marker in groups:
        group = [row for row in rows if float(row["a"]) == a and int(row["n"]) == n]
        med_ftle = [np.median([float(row[f"ftle_natural_t{time}"]) for row in group]) for time in times]
        med_sali = [np.median([float(row[f"sali_t{time}"]) for row in group]) for time in times]
        axes[0].plot(times, med_ftle, marker=marker, color=color, label=label)
        axes[1].plot(times, med_sali, marker=marker, color=color, label=label)

    axes[0].axhline(0.05, color=COLORS["vermillion"], linestyle=":", linewidth=1.0)
    axes[0].set_xlabel("natural integration time")
    axes[0].set_ylabel("median dimensionless FTLE")
    axes[0].set_xticks(times)
    axes[0].legend(loc="best")
    panel_label(axes[0], "(a)")

    axes[1].axhline(1.0e-8, color=COLORS["vermillion"], linestyle=":", linewidth=1.0)
    axes[1].set_yscale("log")
    axes[1].set_xlabel("natural integration time")
    axes[1].set_ylabel("median SALI")
    axes[1].set_xticks(times)
    axes[1].set_ylim(1.0e-16, 3.0)
    panel_label(axes[1], "(b)")

    fields = [0.0, 1.0]
    x = np.arange(len(fields))
    width = 0.34
    radial = [audit["groups"][f"a=0.0:B={field}"]["median_ftle_natural"] for field in fields]
    nonlinear = [audit["groups"][f"a=1.02:B={field}"]["median_ftle_natural"] for field in fields]
    axes[2].bar(x - width / 2, radial, width, color=COLORS["grey"], label=r"$a=0$")
    axes[2].bar(x + width / 2, nonlinear, width, color=COLORS["blue"], label=r"$a=1.02$")
    axes[2].set_xticks(x, [r"$B=0$", r"$B=1$"])
    axes[2].set_ylabel("DOP853 median FTLE")
    axes[2].legend(loc="upper right")
    radial_flags = [
        (
            audit["groups"][f"a=0.0:B={field}"]["joint_flags"],
            audit["groups"][f"a=0.0:B={field}"]["records"],
        )
        for field in fields
    ]
    nonlinear_flags = [
        (
            audit["groups"][f"a=1.02:B={field}"]["joint_flags"],
            audit["groups"][f"a=1.02:B={field}"]["records"],
        )
        for field in fields
    ]
    flag_text = (
        "joint flags at $B=0,1$\n"
        + "radial: "
        + ", ".join(f"{flag}/{total}" for flag, total in radial_flags)
        + "\nHénon: "
        + ", ".join(f"{flag}/{total}" for flag, total in nonlinear_flags)
    )
    axes[2].text(
        0.03,
        0.94,
        flag_text,
        transform=axes[2].transAxes,
        va="top",
        fontsize=7.2,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.88, "pad": 1.5},
    )
    panel_label(axes[2], "(c)")

    save_figure(fig, "fig3_classical_convergence")


if __name__ == "__main__":
    main()
