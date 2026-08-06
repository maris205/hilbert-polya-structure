#!/usr/bin/env python3
"""Plot mesh convergence of adjacent-gap ratios and level changes."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from paper_plot_style import COLORS, panel_label, save_figure

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from hp_candidate_search.quantum_fd import spectral_window  # noqa: E402

EXPECTED_LEVELS = 140


def mean_ratio(values: np.ndarray) -> float:
    core = spectral_window(values)
    assert len(core) == EXPECTED_LEVELS
    gaps = np.diff(core)
    ratios = np.minimum(gaps[:-1], gaps[1:]) / np.maximum(gaps[:-1], gaps[1:])
    return float(np.mean(ratios))


def load_values(path: Path, key: str = "eigenvalues") -> np.ndarray:
    with np.load(path, allow_pickle=False) as archive:
        return np.asarray(archive[key], dtype=float)


def series(prefix: str, has_fourth: bool) -> tuple[np.ndarray, np.ndarray]:
    h_values = [0.04, 0.03, 0.0225]
    files = [
        PROJECT / f"results/r100_quantum_spectrum/{prefix}_h0p04.npz",
        PROJECT / f"results/r100_quantum_spectrum/{prefix}_h0p03.npz",
        PROJECT / f"results/r101_quantum_refinement/{prefix}_h0p0225.npz",
    ]
    if has_fourth:
        h_values.append(0.0175)
        files.append(PROJECT / f"results/r102_core_fourth_grid/{prefix}_h0p0175.npz")
        extrapolated = load_values(files[-1], "extrapolated_eigenvalues")
    else:
        extrapolated = load_values(files[-1], "extrapolated_eigenvalues")
    x = [0.0] + [h * h for h in reversed(h_values)]
    y = [mean_ratio(extrapolated)] + [mean_ratio(load_values(path)) for path in reversed(files)]
    return np.asarray(x), np.asarray(y)


def main() -> None:
    r100 = json.loads((PROJECT / "results/r100_quantum_spectrum/summary.json").read_text(encoding="utf-8"))
    window_audit = json.loads(
        (PROJECT / "results/QUANTUM_WINDOW_AUDIT.json").read_text(encoding="utf-8")
    )
    references = r100["reference_mean_ratios"]

    branches = (
        ("a1p02_n1_B0", True, r"$a=1.02,B=0$", COLORS["blue"], "o"),
        ("a1p02_n1_B1", True, r"$a=1.02,B=1$", COLORS["orange"], "s"),
        ("a6_n1_B0", False, r"$a=6,B=0$", COLORS["green"], "^"),
        ("a6_n1_B1", False, r"$a=6,B=1$", COLORS["purple"], "D"),
    )
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.35), constrained_layout=True)
    for prefix, fourth, label, color, marker in branches:
        x, y = series(prefix, fourth)
        axes[0].plot(x, y, marker=marker, color=color, label=label)
    axes[0].axhline(references["GOE"], color=COLORS["grey"], linestyle="--", linewidth=1.0, label="GOE mean")
    axes[0].axhline(references["GUE"], color=COLORS["black"], linestyle=":", linewidth=1.0, label="GUE mean")
    axes[0].set_xlabel(r"$h^2$ (zero denotes extrapolation)")
    axes[0].set_ylabel(r"mean adjacent ratio $\langle\widetilde r\rangle$")
    axes[0].legend(ncol=2, loc="best")
    panel_label(axes[0], "(a)")

    labels, first, later = [], [], []
    for prefix, fourth, label, _, _ in branches:
        labels.append(label.replace("$", ""))
        physics = (1.02, 1.0 if prefix.endswith("B1") else 0.0)
        if prefix.startswith("a6"):
            physics = (6.0, physics[1])
        audit_key = f"a={physics[0]}:B={physics[1]}"
        first.append(
            window_audit["r100"][audit_key]["coarse_to_fine"][
                "median_relative_level_change"
            ]
        )
        if fourth:
            later.append(
                window_audit["r102"][f"B={physics[1]}"]["source_to_fine"][
                    "median_relative_level_change"
                ]
            )
        else:
            later.append(
                window_audit["r101"][audit_key]["coarse_to_fine"][
                    "median_relative_level_change"
                ]
            )
    x = np.arange(len(labels))
    width = 0.36
    axes[1].bar(x - width / 2, 100.0 * np.asarray(first), width, color=COLORS["grey"], label=r"$0.04\to0.03$")
    axes[1].bar(x + width / 2, 100.0 * np.asarray(later), width, color=COLORS["blue"], label="latest available")
    axes[1].axhline(1.0, color=COLORS["vermillion"], linestyle=":", linewidth=1.0, label="original 1% gate")
    axes[1].set_xticks(x, labels, rotation=20, ha="right")
    axes[1].set_ylabel("median relative level change (%)")
    axes[1].legend(loc="upper right")
    panel_label(axes[1], "(b)")

    save_figure(fig, "fig4_quantum_convergence")


if __name__ == "__main__":
    main()
