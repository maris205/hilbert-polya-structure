#!/usr/bin/env python3
"""Plot the exact-clock unfolding without zeta-zero comparisons."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from hp_candidate_search.quantum_fd import (  # noqa: E402
    classical_smooth_count,
    spectral_window,
)
from paper_plot_style import COLORS, panel_label, save_figure  # noqa: E402


def load(path: Path) -> np.ndarray:
    with np.load(path, allow_pickle=False) as archive:
        values = spectral_window(archive["extrapolated_eigenvalues"])
    assert len(values) == 140
    return values


def main() -> None:
    spectra = (
        (r"$B=0$", COLORS["blue"], load(PROJECT / "results/r102_core_fourth_grid/a1p02_n1_B0_h0p0175.npz")),
        (r"$B=1$", COLORS["orange"], load(PROJECT / "results/r102_core_fourth_grid/a1p02_n1_B1_h0p0175.npz")),
    )
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.35), constrained_layout=True)
    lengths = {len(values) for _, _, values in spectra}
    if len(lengths) != 1:
        raise ValueError("frozen spectral windows have different lengths")
    level_offset = np.arange(lengths.pop())
    for label, color, values in spectra:
        unfolded = classical_smooth_count(values)
        relative = unfolded - unfolded[0]
        axes[0].plot(level_offset, relative, color=color, label=label)
        residual = relative - level_offset
        axes[1].plot(level_offset, residual, color=color, label=label)
    axes[0].plot(level_offset, level_offset, color=COLORS["black"], linestyle="--", linewidth=1.0, label="unit mean spacing")
    axes[0].set_xlabel("level offset in the frozen window")
    axes[0].set_ylabel(r"$\mathcal{N}_{\mathrm{cl}}(E_k)-\mathcal{N}_{\mathrm{cl}}(E_{25})$")
    axes[0].legend(loc="upper left")
    panel_label(axes[0], "(a)")
    axes[1].axhline(0.0, color=COLORS["black"], linestyle="--", linewidth=1.0)
    axes[1].set_xlabel("level offset in the frozen window")
    axes[1].set_ylabel("cumulative unfolded residual")
    axes[1].legend(loc="best")
    panel_label(axes[1], "(b)")
    save_figure(fig, "fig7_smooth_clock")


if __name__ == "__main__":
    main()
