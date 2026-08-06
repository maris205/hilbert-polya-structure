#!/usr/bin/env python3
"""Run the frozen independent fourth-order quantum cross-check."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from hp_candidate_search.quantum_fd import (
    GridSpec,
    spacing_diagnostics,
    spectral_window,
)
from hp_candidate_search.quantum_fd4 import compute_eigenvalues_fourth


def adjacent_ratios(values: np.ndarray) -> np.ndarray:
    core = spectral_window(values)
    spacings = np.diff(core)
    return np.minimum(spacings[:-1], spacings[1:]) / np.maximum(
        spacings[:-1], spacings[1:]
    )


def main(output_dir: Path | None = None) -> int:
    if output_dir is None:
        output_dir = Path("results/r107_fourth_order_quantum")
    output_dir.mkdir(parents=True, exist_ok=True)
    reference_dir = Path("results/r102_core_fourth_grid")
    reference_summary = json.loads(
        (reference_dir / "summary.json").read_text(encoding="utf-8")
    )
    references = {
        float(record["spec"]["magnetic_field"]): np.load(
            reference_dir / record["spectrum_file"]
        )["extrapolated_eigenvalues"]
        for record in reference_summary["records"]
    }

    records: list[dict[str, object]] = []
    for field in (0.0, 1.0):
        spectra: dict[float, np.ndarray] = {}
        grids: dict[float, dict[str, object]] = {}
        files: dict[float, str] = {}
        for spacing in (0.03, 0.0225):
            print(
                f"a=1.02 n=1 B={field:g} fourth-order h={spacing:g}",
                flush=True,
            )
            spec = GridSpec(
                a=1.02,
                n=1,
                magnetic_field=field,
                target_energy=450.0,
                nominal_spacing=spacing,
                eigenvalue_count=180,
                wall_factor=100.0,
            )
            values, grid = compute_eigenvalues_fourth(spec)
            label = (
                f"a1p02_n1_B{field:g}_fd4_h{spacing:g}"
                .replace(".", "p")
            )
            filename = f"{label}.npz"
            np.savez_compressed(output_dir / filename, eigenvalues=values)
            spectra[spacing] = values
            grids[spacing] = grid
            files[spacing] = filename

        coarse = spectra[0.03]
        fine = spectra[0.0225]
        reference = references[field]
        coarse_core = spectral_window(coarse)
        fine_core = spectral_window(fine)
        reference_core = spectral_window(reference)
        coarse_fine = np.abs(coarse_core - fine_core) / fine_core
        cross_method = np.abs(fine_core - reference_core) / reference_core
        fine_stats = spacing_diagnostics(fine)
        reference_stats = spacing_diagnostics(reference)
        fine_ratios = adjacent_ratios(fine)
        reference_ratios = adjacent_ratios(reference)
        ratio_difference = abs(
            fine_stats["mean_spacing_ratio"]
            - reference_stats["mean_spacing_ratio"]
        )
        ratio_correlation = float(np.corrcoef(fine_ratios, reference_ratios)[0, 1])

        gates = {
            "fd4_coarse_fine_median_below_0p5pct": bool(
                np.median(coarse_fine) < 0.005
            ),
            "fd4_vs_fd2_extrap_median_below_0p75pct": bool(
                np.median(cross_method) < 0.0075
            ),
            "mean_ratio_difference_below_0p02": bool(ratio_difference < 0.02),
            "ratio_array_correlation_above_0p90": bool(ratio_correlation > 0.90),
            "max_relative_residual_below_1e_8": bool(
                float(grids[0.0225]["max_relative_eigen_residual"]) < 1.0e-8
            ),
        }
        records.append(
            {
                "field": field,
                "spec": asdict(
                    GridSpec(
                        a=1.02,
                        n=1,
                        magnetic_field=field,
                        target_energy=450.0,
                        nominal_spacing=0.0225,
                        eigenvalue_count=180,
                        wall_factor=100.0,
                    )
                ),
                "spectrum_files": {
                    "h0p03": files[0.03],
                    "h0p0225": files[0.0225],
                },
                "grids": {
                    "h0p03": grids[0.03],
                    "h0p0225": grids[0.0225],
                },
                "fd4_fine_diagnostics": fine_stats,
                "fd2_extrapolated_diagnostics": reference_stats,
                "fd4_coarse_fine_median_relative_change": float(
                    np.median(coarse_fine)
                ),
                "fd4_coarse_fine_p90_relative_change": float(
                    np.quantile(coarse_fine, 0.9)
                ),
                "fd4_vs_fd2_extrap_median_relative_change": float(
                    np.median(cross_method)
                ),
                "fd4_vs_fd2_extrap_p90_relative_change": float(
                    np.quantile(cross_method, 0.9)
                ),
                "mean_ratio_difference": float(ratio_difference),
                "ratio_array_correlation": ratio_correlation,
                "gates": gates,
                "all_gates_pass": all(gates.values()),
            }
        )

    output = {
        "records": records,
        "all_gates_pass": all(record["all_gates_pass"] for record in records),
        "zero_data_loaded": False,
        "prime_data_loaded": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
