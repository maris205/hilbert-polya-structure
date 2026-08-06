#!/usr/bin/env python3
"""Run the zero-input R100 finite-difference spectrum pilot."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from hp_candidate_search.quantum_fd import (
    GridSpec,
    PRODUCTION_DISCARD_HIGH,
    PRODUCTION_DISCARD_LOW,
    compute_eigenvalues,
    spectral_window,
    spacing_diagnostics,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("smoke", "production"), default="smoke")
    args = parser.parse_args()
    output_dir = Path("results") / (
        "r100_quantum_spectrum_smoke" if args.mode == "smoke" else "r100_quantum_spectrum"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.mode == "smoke":
        configurations = [
            GridSpec(a=a, n=1, magnetic_field=field, target_energy=250.0,
                     nominal_spacing=0.06, eigenvalue_count=60, wall_factor=50.0)
            for a, field in ((0.0, 0.0), (1.02, 0.0), (1.02, 1.0))
        ]
        discard_low, discard_high = 10, 5
    else:
        configurations = [
            GridSpec(a=a, n=1, magnetic_field=field, target_energy=450.0,
                     nominal_spacing=spacing, eigenvalue_count=180, wall_factor=100.0)
            for a, field in ((0.0, 0.0), (1.02, 0.0), (1.02, 1.0), (6.0, 0.0), (6.0, 1.0))
            for spacing in (0.04, 0.03)
        ]
        discard_low, discard_high = (
            PRODUCTION_DISCARD_LOW,
            PRODUCTION_DISCARD_HIGH,
        )

    records = []
    for index, spec in enumerate(configurations):
        print(
            f"[{index + 1}/{len(configurations)}] a={spec.a} B={spec.magnetic_field} "
            f"h={spec.nominal_spacing}",
            flush=True,
        )
        eigenvalues, grid = compute_eigenvalues(spec)
        diagnostics = spacing_diagnostics(
            eigenvalues, discard_low=discard_low, discard_high=discard_high
        )
        label = (
            f"a{spec.a:g}_n{spec.n}_B{spec.magnetic_field:g}_"
            f"h{spec.nominal_spacing:g}"
        ).replace("-", "m").replace(".", "p")
        np.savez_compressed(output_dir / f"{label}.npz", eigenvalues=eigenvalues)
        records.append(
            {
                "label": label,
                "spec": asdict(spec),
                "grid": grid,
                "diagnostics": diagnostics,
                "spectrum_file": f"{label}.npz",
            }
        )

    convergence = []
    if args.mode == "production":
        by_physics = {}
        for record in records:
            spec = record["spec"]
            key = (spec["a"], spec["n"], spec["magnetic_field"])
            by_physics.setdefault(key, []).append(record)
        for key, pair in sorted(by_physics.items()):
            pair.sort(key=lambda record: record["spec"]["nominal_spacing"], reverse=True)
            coarse = np.load(output_dir / pair[0]["spectrum_file"])["eigenvalues"]
            fine = np.load(output_dir / pair[1]["spectrum_file"])["eigenvalues"]
            coarse_core = spectral_window(coarse)
            fine_core = spectral_window(fine)
            relative = np.abs(coarse_core - fine_core) / fine_core
            convergence.append(
                {
                    "a": key[0],
                    "n": key[1],
                    "magnetic_field": key[2],
                    "median_relative_level_change": float(np.median(relative)),
                    "p90_relative_level_change": float(np.quantile(relative, 0.9)),
                    "max_relative_level_change": float(np.max(relative)),
                    "passes_median_1pct": bool(np.median(relative) < 0.01),
                }
            )

    output = {
        "mode": args.mode,
        "records": records,
        "convergence": convergence,
        "reference_mean_ratios": {"Poisson": 0.386294, "GOE": 0.535898, "GUE": 0.60266},
        "zero_data_loaded": False,
        "prime_data_loaded": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
