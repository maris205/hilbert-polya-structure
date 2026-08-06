#!/usr/bin/env python3
"""Plot empirical adjacent-ratio CDFs against GOE/GUE surmises."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import cumulative_trapezoid

from paper_plot_style import COLORS, save_figure

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from hp_candidate_search.quantum_fd import spectral_window  # noqa: E402

EXPECTED_LEVELS = 140
EXPECTED_RATIOS = 138


def ratios(path: Path) -> np.ndarray:
    with np.load(path, allow_pickle=False) as archive:
        values = spectral_window(archive["eigenvalues"])
    assert len(values) == EXPECTED_LEVELS
    gaps = np.diff(values)
    adjacent = np.minimum(gaps[:-1], gaps[1:]) / np.maximum(gaps[:-1], gaps[1:])
    assert len(adjacent) == EXPECTED_RATIOS
    return np.sort(adjacent)


def surmise_cdf(beta: int, grid: np.ndarray) -> np.ndarray:
    density = (grid + grid * grid) ** beta / (1.0 + grid + grid * grid) ** (1.0 + 1.5 * beta)
    cdf = cumulative_trapezoid(density, grid, initial=0.0)
    return cdf / cdf[-1]


def sup_cdf_distance(sample: np.ndarray, grid: np.ndarray, reference: np.ndarray) -> float:
    """Return the two-sided empirical-CDF sup distance at the sample jumps."""
    ref_at_sample = np.interp(sample, grid, reference)
    n = len(sample)
    right = np.arange(1, n + 1, dtype=float) / n
    left = np.arange(0, n, dtype=float) / n
    return float(max(np.max(np.abs(right - ref_at_sample)), np.max(np.abs(left - ref_at_sample))))


def main() -> None:
    b0 = ratios(PROJECT / "results/r102_core_fourth_grid/a1p02_n1_B0_h0p0175.npz")
    b1 = ratios(PROJECT / "results/r102_core_fourth_grid/a1p02_n1_B1_h0p0175.npz")
    grid = np.linspace(0.0, 1.0, 4001)
    goe = surmise_cdf(1, grid)
    gue = surmise_cdf(2, grid)
    d_b0_goe = sup_cdf_distance(b0, grid, goe)
    d_b1_gue = sup_cdf_distance(b1, grid, gue)
    fig, ax = plt.subplots(figsize=(5.1, 3.55))
    ax.step(b0, np.arange(1, len(b0) + 1) / len(b0), where="post", color=COLORS["blue"], label=rf"$B=0$ ($n={len(b0)}$)")
    ax.step(b1, np.arange(1, len(b1) + 1) / len(b1), where="post", color=COLORS["orange"], label=rf"$B=1$ ($n={len(b1)}$)")
    ax.plot(grid, goe, color=COLORS["grey"], linestyle="--", label="GOE surmise")
    ax.plot(grid, gue, color=COLORS["black"], linestyle=":", label="GUE surmise")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel(r"adjacent ratio $\widetilde r$")
    ax.set_ylabel("empirical cumulative fraction")
    ax.legend(loc="lower right")
    ax.text(
        0.03,
        0.96,
        rf"sup distances: $B=0$ to GOE {d_b0_goe:.3f}; $B=1$ to GUE {d_b1_gue:.3f}",
        transform=ax.transAxes,
        va="top",
        fontsize=8.0,
    )
    save_figure(fig, "fig5_ratio_cdfs")


if __name__ == "__main__":
    main()
