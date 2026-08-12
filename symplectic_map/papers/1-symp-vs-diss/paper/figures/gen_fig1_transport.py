#!/usr/bin/env python3
"""Plot the source-locked parity statistic and exposure gate from JSON."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper_plot_style import COLORS, save_figure


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parents[1]
RESULT_DIR = PAPER_ROOT / "results" / "transport"


def load(stem: str) -> dict:
    with (RESULT_DIR / f"{stem}.json").open(encoding="utf-8") as handle:
        return json.load(handle)


def arrays(payload: dict) -> tuple[np.ndarray, ...]:
    rows = payload["results"]
    rho = np.array([row["rho"] for row in rows], dtype=float)
    polarity = np.array([row["parity_polarity"] for row in rows], dtype=float)
    low = np.array([row["parity_polarity_ci_low"] for row in rows], dtype=float)
    high = np.array([row["parity_polarity_ci_high"] for row in rows], dtype=float)
    exposure = np.array([row["exposure_fraction"] for row in rows], dtype=float)
    return rho, polarity, low, high, exposure


def main() -> None:
    validation = load("transport_validation_frozen_v2")
    development = load("transport_dev_frozen_v2")
    neighbors = [
        ("transport_validation_neighbor_a150_v2", r"$a=1.50$", COLORS["orange"]),
        ("transport_validation_neighbor_a152_v2", r"$a=1.52$", COLORS["green"]),
        ("transport_validation_neighbor_a156_v2", r"$a=1.56$", COLORS["purple"]),
        ("transport_validation_neighbor_a158_v2", r"$a=1.58$", COLORS["yellow"]),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.65), sharex=True)
    ax_p, ax_e = axes

    rho_d, p_d, _, _, e_d = arrays(development)
    ax_p.plot(rho_d, p_d, color=COLORS["gray"], marker="s", ms=3,
              linestyle=":", label="development")
    ax_e.plot(rho_d, e_d, color=COLORS["gray"], marker="s", ms=3,
              linestyle=":", label="development")

    rho, polarity, low, high, exposure = arrays(validation)
    ax_p.fill_between(rho, low, high, color=COLORS["blue"], alpha=0.18,
                      linewidth=0)
    ax_p.plot(rho, polarity, color=COLORS["blue"], marker="o", ms=3.5,
              label=r"frozen $u_c$")
    ax_e.plot(rho, exposure, color=COLORS["blue"], marker="o", ms=3.5,
              label=r"frozen $u_c$")

    for stem, label, color in neighbors:
        rho_n, p_n, _, _, e_n = arrays(load(stem))
        ax_p.plot(rho_n, p_n, color=color, alpha=0.75, linestyle="--",
                  linewidth=0.9, label=label)
        ax_e.plot(rho_n, e_n, color=color, alpha=0.75, linestyle="--",
                  linewidth=0.9, label=label)

    ax_p.axhline(0.98, color=COLORS["black"], linewidth=0.7,
                 linestyle=(0, (3, 2)))
    ax_e.axhline(0.8, color=COLORS["black"], linewidth=0.7,
                 linestyle=(0, (3, 2)), label="availability gate")
    ax_p.set_xlabel(r"conformal factor $\rho$")
    ax_e.set_xlabel(r"conformal factor $\rho$")
    ax_p.set_ylabel(r"return-parity polarity $P$")
    ax_e.set_ylabel("finite exposure fraction")
    ax_p.set_ylim(-1.04, 1.05)
    ax_e.set_ylim(-0.03, 1.04)
    for ax in axes:
        ax.set_xlim(-0.015, 1.015)
        ax.set_xticks([0, 0.2, 0.5, 1.0])
        ax.tick_params(direction="out", length=3, width=0.7)
    ax_p.text(0.02, 0.04, "a", transform=ax_p.transAxes, fontweight="bold")
    ax_e.text(0.02, 0.04, "b", transform=ax_e.transAxes, fontweight="bold")
    handles, labels = ax_e.get_legend_handles_labels()
    ax_e.legend(handles, labels, frameon=False, ncol=2, loc="lower left",
                bbox_to_anchor=(-0.02, -0.02), columnspacing=0.7,
                handlelength=1.6)
    fig.subplots_adjust(wspace=0.30)
    save_figure(fig, "fig1_shadow_transport")


if __name__ == "__main__":
    main()

