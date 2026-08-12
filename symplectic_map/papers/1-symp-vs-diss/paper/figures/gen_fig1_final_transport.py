#!/usr/bin/env python3
"""Final split-consistency and neighbor-control transport figure."""

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
    return json.loads((RESULT_DIR / f"{stem}.json").read_text(encoding="utf-8"))


def arrays(payload: dict) -> tuple[np.ndarray, ...]:
    rows = payload["results"]
    keys = ("rho", "parity_polarity", "parity_polarity_ci_low",
            "parity_polarity_ci_high", "exposure_fraction")
    return tuple(np.array([row[key] for row in rows], dtype=float) for key in keys)


def main() -> None:
    development = load("transport_dev_frozen_v2")
    validation = load("transport_validation_frozen_v2")
    test = load("transport_test_frozen_v2")
    neighbors = [
        ("transport_test_neighbor_a150_v2", r"$a=1.50$", COLORS["orange"]),
        ("transport_test_neighbor_a152_v2", r"$a=1.52$", COLORS["green"]),
        ("transport_test_neighbor_a156_v2", r"$a=1.56$", COLORS["purple"]),
        ("transport_test_neighbor_a158_v2", r"$a=1.58$", COLORS["yellow"]),
    ]
    fig, (ax_p, ax_e) = plt.subplots(1, 2, figsize=(7.05, 2.72), sharex=True)

    for payload, label, marker, gray in [
        (development, "development", "s", "#999999"),
        (validation, "validation", "^", "#555555"),
    ]:
        rho, p, _, _, exposure = arrays(payload)
        ax_p.plot(rho, p, marker=marker, ms=3, linestyle=":", color=gray,
                  linewidth=0.9, label=label)
        ax_e.plot(rho, exposure, marker=marker, ms=3, linestyle=":", color=gray,
                  linewidth=0.9, label=label)

    rho, p, low, high, exposure = arrays(test)
    ax_p.fill_between(rho, low, high, color=COLORS["blue"], alpha=0.18,
                      linewidth=0)
    ax_p.plot(rho, p, marker="o", ms=3.8, color=COLORS["blue"],
              label=r"test, frozen $u_c$")
    ax_e.plot(rho, exposure, marker="o", ms=3.8, color=COLORS["blue"],
              label=r"test, frozen $u_c$")

    for stem, label, color in neighbors:
        rho_n, p_n, _, _, exposure_n = arrays(load(stem))
        ax_p.plot(rho_n, p_n, linestyle="--", linewidth=0.9, color=color,
                  alpha=0.78, label=label)
        ax_e.plot(rho_n, exposure_n, linestyle="--", linewidth=0.9, color=color,
                  alpha=0.78, label=label)

    ax_p.axhline(0.98, color=COLORS["black"], linewidth=0.7,
                 linestyle=(0, (3, 2)))
    ax_e.axhline(0.8, color=COLORS["black"], linewidth=0.7,
                 linestyle=(0, (3, 2)), label="availability gate")
    ax_p.set_ylabel(r"return-parity polarity $P$")
    ax_e.set_ylabel("finite exposure fraction")
    ax_p.set_ylim(-1.04, 1.05)
    ax_e.set_ylim(-0.03, 1.04)
    for label, ax in zip(("a", "b"), (ax_p, ax_e)):
        ax.set_xlim(-0.015, 1.015)
        ax.set_xticks([0, 0.2, 0.5, 1.0])
        ax.set_xlabel(r"conformal factor $\rho$")
        ax.text(0.02, 0.04, label, transform=ax.transAxes, fontweight="bold")
        ax.tick_params(direction="out", length=3, width=0.7)
    handles, labels = ax_e.get_legend_handles_labels()
    ax_e.legend(handles, labels, frameon=False, ncol=2, loc="lower left",
                bbox_to_anchor=(-0.02, -0.02), columnspacing=0.65,
                handlelength=1.6)
    fig.subplots_adjust(wspace=0.30)
    save_figure(fig, "fig1_final_shadow_transport")


if __name__ == "__main__":
    main()

