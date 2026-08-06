#!/usr/bin/env python3
"""Run the frozen fourth-grid check for the a=1.02 quantum core."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from hp_candidate_search.quantum_fd import (
    GridSpec,
    compute_eigenvalues,
    spacing_diagnostics,
    spectral_window,
)


def main() -> int:
    source_dir = Path("results/r101_quantum_refinement")
    output_dir = Path("results/r102_core_fourth_grid")
    output_dir.mkdir(parents=True, exist_ok=True)
    source_summary = json.loads((source_dir / "summary.json").read_text(encoding="utf-8"))
    source_records = {
        record["spec"]["magnetic_field"]: record
        for record in source_summary["records"]
        if record["spec"]["a"] == 1.02
    }
    records = []
    for index, field in enumerate((0.0, 1.0)):
        print(f"[{index + 1}/2] a=1.02 B={field} h=0.0175", flush=True)
        spec = GridSpec(
            a=1.02,
            n=1,
            magnetic_field=field,
            target_energy=450.0,
            nominal_spacing=0.0175,
            eigenvalue_count=180,
            wall_factor=100.0,
        )
        fine, grid = compute_eigenvalues(spec)
        source_record = source_records[field]
        source = np.load(source_dir / source_record["spectrum_file"])["eigenvalues"]
        source_h = float(source_record["grid"]["hx"] * source_record["grid"]["hy"]) ** 0.5
        fine_h = float(grid["hx"] * grid["hy"]) ** 0.5
        extrapolated = (
            source_h**2 * fine - fine_h**2 * source
        ) / (source_h**2 - fine_h**2)
        source_core = spectral_window(source)
        fine_core = spectral_window(fine)
        relative = np.abs(source_core - fine_core) / fine_core
        fine_stats = spacing_diagnostics(fine)
        extrapolated_stats = spacing_diagnostics(extrapolated)
        ratio_difference = abs(
            fine_stats["mean_spacing_ratio"]
            - extrapolated_stats["mean_spacing_ratio"]
        )
        label = f"a1p02_n1_B{field:g}_h0p0175".replace(".", "p")
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
                "fine_diagnostics": fine_stats,
                "extrapolated_diagnostics": extrapolated_stats,
                "median_relative_change_00225_to_00175": float(np.median(relative)),
                "p90_relative_change_00225_to_00175": float(np.quantile(relative, 0.9)),
                "max_relative_change_00225_to_00175": float(np.max(relative)),
                "mean_ratio_fine_extrapolated_difference": float(ratio_difference),
                "passes_level_0p5pct": bool(np.median(relative) < 0.005),
                "passes_ratio_0p015": bool(ratio_difference < 0.015),
            }
        )
    output = {
        "records": records,
        "all_gates_pass": all(
            record["passes_level_0p5pct"] and record["passes_ratio_0p015"]
            for record in records
        ),
        "zero_data_loaded": False,
        "prime_data_loaded": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
