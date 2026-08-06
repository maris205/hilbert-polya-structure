#!/usr/bin/env python3
"""Unify level/gap/ratio convergence on the exact spacing-statistics window."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hp_candidate_search.quantum_fd import (
    PRODUCTION_DISCARD_HIGH,
    PRODUCTION_DISCARD_LOW,
    spectral_window,
)


def ratios(values: np.ndarray) -> np.ndarray:
    gaps = np.diff(spectral_window(values))
    return np.minimum(gaps[:-1], gaps[1:]) / np.maximum(gaps[:-1], gaps[1:])


def ratio_cdf(beta: int) -> tuple[np.ndarray, np.ndarray]:
    grid = np.linspace(0.0, 1.0, 200001)
    density = 2.0 * (grid + grid * grid) ** beta / (
        1.0 + grid + grid * grid
    ) ** (1.0 + 1.5 * beta)
    cdf = np.concatenate(([0.0], cumulative_trapezoid(density, grid)))
    cdf /= cdf[-1]
    return grid, cdf


def ks_distance(sample: np.ndarray, beta: int) -> float:
    grid, cdf = ratio_cdf(beta)
    ordered = np.sort(sample)
    model = np.interp(ordered, grid, cdf)
    n = len(ordered)
    upper = np.arange(1, n + 1) / n
    lower = np.arange(0, n) / n
    return float(max(np.max(np.abs(upper - model)), np.max(np.abs(lower - model))))


def comparison(left: np.ndarray, right: np.ndarray) -> dict[str, float]:
    left_window = spectral_window(left)
    right_window = spectral_window(right)
    relative = np.abs(left_window - right_window) / right_window
    left_gaps = np.diff(left_window)
    right_gaps = np.diff(right_window)
    left_ratios = ratios(left)
    right_ratios = ratios(right)
    return {
        "levels_compared": len(left_window),
        "median_relative_level_change": float(np.median(relative)),
        "p90_relative_level_change": float(np.quantile(relative, 0.9)),
        "median_gap_change_over_mean_fine_gap": float(
            np.median(np.abs(left_gaps - right_gaps)) / np.mean(right_gaps)
        ),
        "ratio_array_correlation": float(np.corrcoef(left_ratios, right_ratios)[0, 1]),
        "mean_ratio_left": float(np.mean(left_ratios)),
        "mean_ratio_right": float(np.mean(right_ratios)),
        "mean_ratio_absolute_difference": float(
            abs(np.mean(left_ratios) - np.mean(right_ratios))
        ),
    }


def main() -> int:
    r100 = Path("results/r100_quantum_spectrum")
    r101 = Path("results/r101_quantum_refinement")
    r102 = Path("results/r102_core_fourth_grid")
    r103 = Path("results/r103_magnetic_crossover")
    r104 = Path("results/r104_crossover_grid_check")

    r100_summary = json.loads((r100 / "summary.json").read_text(encoding="utf-8"))
    r100_by_key = {
        (record["spec"]["a"], record["spec"]["magnetic_field"], record["spec"]["nominal_spacing"]): record
        for record in r100_summary["records"]
    }
    r101_summary = json.loads((r101 / "summary.json").read_text(encoding="utf-8"))
    r101_by_key = {
        (record["spec"]["a"], record["spec"]["magnetic_field"]): record
        for record in r101_summary["records"]
    }
    r102_summary = json.loads((r102 / "summary.json").read_text(encoding="utf-8"))

    output: dict[str, object] = {
        "audit_version": 2,
        "window": (
            f"discard_low={PRODUCTION_DISCARD_LOW}, "
            f"discard_high={PRODUCTION_DISCARD_HIGH}"
        ),
        "correction_note": (
            "All level-change aggregates below are recomputed from the "
            "archived NPZ spectra. Historical summary.json aggregation "
            "fields are retained as provenance but are not authoritative "
            "for the unified 140-level window."
        ),
        "r100": {},
        "r101": {},
        "r102": {},
        "r104": {},
    }
    physics_keys = sorted(
        {
            (record["spec"]["a"], record["spec"]["magnetic_field"])
            for record in r100_summary["records"]
        }
    )
    for key in physics_keys:
        coarse_record = r100_by_key[(key[0], key[1], 0.04)]
        fine_record = r100_by_key[(key[0], key[1], 0.03)]
        coarse = np.load(r100 / coarse_record["spectrum_file"])["eigenvalues"]
        fine = np.load(r100 / fine_record["spectrum_file"])["eigenvalues"]
        output["r100"][f"a={key[0]}:B={key[1]}"] = {
            "coarse_to_fine": comparison(coarse, fine)
        }
    for key, fine_record in r101_by_key.items():
        coarse_record = r100_by_key[(key[0], key[1], 0.03)]
        coarse = np.load(r100 / coarse_record["spectrum_file"])["eigenvalues"]
        spectra = np.load(r101 / fine_record["spectrum_file"])
        fine = spectra["eigenvalues"]
        extrapolated = spectra["extrapolated_eigenvalues"]
        output["r101"][f"a={key[0]}:B={key[1]}"] = {
            "coarse_to_fine": comparison(coarse, fine),
            "fine_to_extrapolated": comparison(fine, extrapolated),
        }

    for record in r102_summary["records"]:
        field = record["spec"]["magnetic_field"]
        source_record = r101_by_key[(1.02, field)]
        source = np.load(r101 / source_record["spectrum_file"])["eigenvalues"]
        spectra = np.load(r102 / record["spectrum_file"])
        fine = spectra["eigenvalues"]
        extrapolated = spectra["extrapolated_eigenvalues"]
        fine_ratios = ratios(fine)
        extrapolated_ratios = ratios(extrapolated)
        output["r102"][f"B={field}"] = {
            "source_to_fine": comparison(source, fine),
            "fine_to_extrapolated": comparison(fine, extrapolated),
            "fine_KS_to_GOE": ks_distance(fine_ratios, 1),
            "fine_KS_to_GUE": ks_distance(fine_ratios, 2),
            "extrapolated_KS_to_GOE": ks_distance(extrapolated_ratios, 1),
            "extrapolated_KS_to_GUE": ks_distance(extrapolated_ratios, 2),
        }

    r103_summary = json.loads((r103 / "summary.json").read_text(encoding="utf-8"))
    r103_by_field = {
        float(record["field"]): record for record in r103_summary["records"]
    }
    r104_summary = json.loads((r104 / "summary.json").read_text(encoding="utf-8"))
    for record in r104_summary["records"]:
        field = float(record["field"])
        coarse_name = f"B{field:g}_h0p03".replace(".", "p") + ".npz"
        coarse = np.load(r104 / coarse_name)["eigenvalues"]
        fine_record = r103_by_field[field]
        fine = np.load(r103 / fine_record["spectrum_file"])["eigenvalues"]
        output["r104"][f"B={record['field']}"] = {
            "coarse_to_fine": comparison(coarse, fine),
            "stored_summary_median_for_provenance": record[
                "median_relative_level_change"
            ],
        }

    (Path("results") / "QUANTUM_WINDOW_AUDIT.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
