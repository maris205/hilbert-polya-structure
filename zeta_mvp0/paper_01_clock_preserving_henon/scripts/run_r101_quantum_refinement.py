#!/usr/bin/env python3
"""Add the third finite-difference grid required after the R100 gate failure."""

from __future__ import annotations

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
    compute_eigenvalues,
    spacing_diagnostics,
    spectral_window,
)


def main() -> int:
    r100_dir = Path("results/r100_quantum_spectrum")
    output_dir = Path("results/r101_quantum_refinement")
    output_dir.mkdir(parents=True, exist_ok=True)
    r100 = json.loads((r100_dir / "summary.json").read_text(encoding="utf-8"))
    coarse_records = {
        (
            record["spec"]["a"],
            record["spec"]["n"],
            record["spec"]["magnetic_field"],
        ): record
        for record in r100["records"]
        if record["spec"]["nominal_spacing"] == 0.03
    }
    physics = ((0.0, 0.0), (1.02, 0.0), (1.02, 1.0), (6.0, 0.0), (6.0, 1.0))
    records = []
    for index, (a, field) in enumerate(physics):
        print(f"[{index + 1}/{len(physics)}] a={a} B={field} h=0.0225", flush=True)
        spec = GridSpec(
            a=a,
            n=1,
            magnetic_field=field,
            target_energy=450.0,
            nominal_spacing=0.0225,
            eigenvalue_count=180,
            wall_factor=100.0,
        )
        fine, grid = compute_eigenvalues(spec)
        coarse_record = coarse_records[(a, 1, field)]
        coarse = np.load(r100_dir / coarse_record["spectrum_file"])["eigenvalues"]
        coarse_h = float(coarse_record["grid"]["hx"] * coarse_record["grid"]["hy"]) ** 0.5
        fine_h = float(grid["hx"] * grid["hy"]) ** 0.5
        extrapolated = (
            coarse_h**2 * fine - fine_h**2 * coarse
        ) / (coarse_h**2 - fine_h**2)
        coarse_core = spectral_window(coarse)
        fine_core = spectral_window(fine)
        extrapolated_core = spectral_window(extrapolated)
        relative = np.abs(coarse_core - fine_core) / fine_core
        estimated_remaining = (
            np.abs(extrapolated_core - fine_core) / extrapolated_core
        )
        label = f"a{a:g}_n1_B{field:g}_h0p0225".replace(".", "p").replace("-", "m")
        spectrum_file = f"{label}.npz"
        np.savez_compressed(
            output_dir / spectrum_file,
            eigenvalues=fine,
            extrapolated_eigenvalues=extrapolated,
        )
        records.append(
            {
                "label": label,
                "spec": asdict(spec),
                "grid": grid,
                "spectrum_file": spectrum_file,
                "fine_diagnostics": spacing_diagnostics(fine),
                "extrapolated_diagnostics": spacing_diagnostics(extrapolated),
                "median_relative_change_003_to_00225": float(np.median(relative)),
                "p90_relative_change_003_to_00225": float(np.quantile(relative, 0.9)),
                "max_relative_change_003_to_00225": float(np.max(relative)),
                "median_estimated_remaining_error": float(np.median(estimated_remaining)),
                "passes_median_1pct": bool(np.median(relative) < 0.01),
            }
        )
    output = {
        "records": records,
        "all_median_1pct_gates_pass": all(record["passes_median_1pct"] for record in records),
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
    return 0 if output["all_median_1pct_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
