#!/usr/bin/env python3
"""Run the frozen B-field crossover scan without zero fitting."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from hp_candidate_search.quantum_fd import GridSpec, compute_eigenvalues, spacing_diagnostics


def main() -> int:
    r101_dir = Path("results/r101_quantum_refinement")
    output_dir = Path("results/r103_magnetic_crossover")
    output_dir.mkdir(parents=True, exist_ok=True)
    r101 = json.loads((r101_dir / "summary.json").read_text(encoding="utf-8"))
    reusable = {
        record["spec"]["magnetic_field"]: record
        for record in r101["records"]
        if record["spec"]["a"] == 1.02
        and record["spec"]["nominal_spacing"] == 0.0225
    }
    fields = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0)
    records = []
    for index, field in enumerate(fields):
        print(f"[{index + 1}/{len(fields)}] B={field}", flush=True)
        spec = GridSpec(
            a=1.02,
            n=1,
            magnetic_field=field,
            target_energy=450.0,
            nominal_spacing=0.0225,
            eigenvalue_count=180,
            wall_factor=100.0,
        )
        if field in reusable:
            source = reusable[field]
            eigenvalues = np.load(r101_dir / source["spectrum_file"])["eigenvalues"]
            grid = source["grid"]
            reused = True
        else:
            eigenvalues, grid = compute_eigenvalues(spec)
            reused = False
        label = f"B{field:g}".replace(".", "p")
        spectrum_file = f"{label}.npz"
        np.savez_compressed(output_dir / spectrum_file, eigenvalues=eigenvalues)
        records.append(
            {
                "field": field,
                "spec": asdict(spec),
                "grid": grid,
                "diagnostics": spacing_diagnostics(eigenvalues),
                "reused_r101": reused,
                "spectrum_file": spectrum_file,
            }
        )
    baseline = records[0]["diagnostics"]["mean_spacing_ratio"]
    above = [
        record
        for record in records[1:]
        if record["diagnostics"]["mean_spacing_ratio"] > baseline
    ]
    output = {
        "records": records,
        "baseline_B0_mean_ratio": baseline,
        "nonzero_fields_above_baseline": len(above),
        "retention_gate_pass": len(above) >= 3,
        "post_selection_of_field": False,
        "zero_data_loaded": False,
        "prime_data_loaded": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["retention_gate_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
