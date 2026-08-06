#!/usr/bin/env python3
"""Check the four new R103 fields on an independent grid spacing."""

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
    source_dir = Path("results/r103_magnetic_crossover")
    output_dir = Path("results/r104_crossover_grid_check")
    output_dir.mkdir(parents=True, exist_ok=True)
    source = json.loads((source_dir / "summary.json").read_text(encoding="utf-8"))
    fine_records = {record["field"]: record for record in source["records"]}
    records = []
    for index, field in enumerate((0.25, 0.5, 2.0, 4.0)):
        print(f"[{index + 1}/4] B={field} h=0.03", flush=True)
        spec = GridSpec(
            a=1.02,
            n=1,
            magnetic_field=field,
            target_energy=450.0,
            nominal_spacing=0.03,
            eigenvalue_count=180,
            wall_factor=100.0,
        )
        coarse, grid = compute_eigenvalues(spec)
        fine_record = fine_records[field]
        fine = np.load(source_dir / fine_record["spectrum_file"])["eigenvalues"]
        coarse_core = spectral_window(coarse)
        fine_core = spectral_window(fine)
        relative = np.abs(coarse_core - fine_core) / fine_core
        coarse_stats = spacing_diagnostics(coarse)
        fine_stats = spacing_diagnostics(fine)
        ratio_difference = abs(
            coarse_stats["mean_spacing_ratio"] - fine_stats["mean_spacing_ratio"]
        )
        label = f"B{field:g}_h0p03".replace(".", "p")
        np.savez_compressed(output_dir / f"{label}.npz", eigenvalues=coarse)
        records.append(
            {
                "field": field,
                "spec": asdict(spec),
                "grid": grid,
                "coarse_diagnostics": coarse_stats,
                "fine_diagnostics": fine_stats,
                "median_relative_level_change": float(np.median(relative)),
                "p90_relative_level_change": float(np.quantile(relative, 0.9)),
                "mean_ratio_coarse_fine_difference": float(ratio_difference),
                "passes_level_1pct": bool(np.median(relative) < 0.01),
                "passes_ratio_0p03": bool(ratio_difference < 0.03),
            }
        )
    output = {
        "records": records,
        "all_gates_pass": all(
            record["passes_level_1pct"] and record["passes_ratio_0p03"]
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
