#!/usr/bin/env python3
"""Plot orbit-count calibration and explicitly incomplete frozen ledgers."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper_plot_style import COLORS, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parents[1]
RESULT_DIR = PAPER_ROOT / "results"


def read_run(filename: str) -> dict:
    with (RESULT_DIR / filename).open(encoding="utf-8") as handle:
        return json.load(handle)["runs"][0]


def counts(run: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    periods = np.array([row["period"] for row in run["periods"]])
    expected = np.array([row["binary_primitive_necklaces"] for row in run["periods"]])
    found = np.array([row["orbits_found"] for row in run["periods"]])
    return periods, expected, found


def main() -> None:
    positive = read_run("ledger_positive_a6_rho1_n10.json")
    frozen = read_run("ledger_uc_rho1_n8_exploratory.json")
    n_p, expected_p, found_p = counts(positive)
    n_f, expected_f, found_f = counts(frozen)

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.55))
    ax_count, ax_cov = axes
    ax_count.plot(n_p, expected_p, color=COLORS["black"], marker="o", ms=3.5,
                  label="binary-necklace count")
    ax_count.scatter(n_p, found_p, color=COLORS["green"], marker="x", s=26,
                     linewidths=1.4, label=r"found at $a=6$")
    ax_count.set_yscale("log")
    ax_count.set_xlabel("primitive period")
    ax_count.set_ylabel("number of primitive cycles")
    ax_count.set_xticks([1, 2, 4, 6, 8, 10])
    ax_count.legend(frameon=False, loc="upper left")

    ax_cov.plot(n_p[:8], found_p[:8] / expected_p[:8], color=COLORS["green"],
                marker="o", ms=3.5, label=r"positive control $a=6$")
    ax_cov.plot(n_f, found_f / expected_f, color=COLORS["orange"], marker="s",
                ms=3.5, label=r"frozen $u_c$ (incomplete search)")
    ax_cov.axhline(1.0, color=COLORS["black"], linewidth=0.7,
                   linestyle=(0, (3, 2)))
    ax_cov.set_xlabel("primitive period")
    ax_cov.set_ylabel("found / binary-necklace count")
    ax_cov.set_ylim(-0.04, 1.08)
    ax_cov.set_xticks(range(1, 9))
    ax_cov.legend(frameon=False, loc="lower left")
    for label, ax in zip(("a", "b"), axes):
        ax.text(0.02, 0.94, label, transform=ax.transAxes, fontweight="bold",
                va="top")
        ax.tick_params(direction="out", length=3, width=0.7)
    fig.subplots_adjust(wspace=0.31)
    save_figure(fig, "fig2_orbit_ledger")


if __name__ == "__main__":
    main()

