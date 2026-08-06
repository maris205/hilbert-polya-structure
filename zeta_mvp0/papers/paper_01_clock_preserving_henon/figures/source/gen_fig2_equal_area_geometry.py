#!/usr/bin/env python3
"""Plot equal-area Hénon-preimage boundaries."""

from __future__ import annotations

import sys
from math import log, pi, sqrt
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from hp_candidate_search.warped_henon import henon_inverse_iterate  # noqa: E402
from paper_plot_style import COLORS, panel_label, save_figure  # noqa: E402


def boundary(a: float, energy: float, samples: int = 4096) -> np.ndarray:
    radius = sqrt(log(energy / (2.0 * pi)) / pi)
    angles = np.linspace(0.0, 2.0 * pi, samples, endpoint=True)
    points = np.empty((samples, 2))
    for index, angle in enumerate(angles):
        u = radius * np.array([np.cos(angle), np.sin(angle)])
        points[index] = henon_inverse_iterate(u, a, 1, centered=True)
    return points


def main() -> None:
    models = ((0.0, r"$a=0$ (radial)"), (1.02, r"$a=1.02$"), (6.0, r"$a=6$"))
    energies = ((100.0, "--", COLORS["sky"]), (1000.0, "-", COLORS["blue"]))
    fig, axes = plt.subplots(1, 3, figsize=(9.5, 3.05), constrained_layout=True)
    for index, (ax, (a, label)) in enumerate(zip(axes, models)):
        for energy, linestyle, color in energies:
            points = boundary(a, energy)
            ax.plot(points[:, 0], points[:, 1], linestyle=linestyle, color=color, label=rf"$E={energy:g}$")
        ax.axhline(0.0, color="#CCCCCC", linewidth=0.6, zorder=0)
        ax.axvline(0.0, color="#CCCCCC", linewidth=0.6, zorder=0)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel(r"$q_1$")
        if index == 0:
            ax.set_ylabel(r"$q_2$")
        panel_label(ax, f"({chr(97 + index)})")
        ax.text(0.5, 0.97, label, transform=ax.transAxes, ha="center", va="top", fontsize=9.3)
        if a == 6.0:
            ax.set_xticks([-1.0, 1.0])
        if index == 0:
            ax.legend(loc="lower right")
    save_figure(fig, "fig2_equal_area_geometry")


if __name__ == "__main__":
    main()
