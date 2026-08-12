#!/usr/bin/env python3
"""Run the frozen quantum residual/gauge/reproducibility audit."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from hp_candidate_search.quantum_fd import GridSpec, compute_eigenvalues


def relative_spectrum_difference(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.max(np.abs(left - right) / np.maximum(1.0, np.abs(right))))


def main() -> int:
    output_dir = Path("results/r105_quantum_numerical_audit")
    output_dir.mkdir(parents=True, exist_ok=True)
    configs = (
        ("B0_symmetric", 0.0, "symmetric"),
        ("B1_symmetric", 1.0, "symmetric"),
        ("B1_landau", 1.0, "landau"),
        ("Bm1_symmetric", -1.0, "symmetric"),
    )
    records = []
    spectra = {}
    for index, (label, field, gauge) in enumerate(configs):
        print(f"[{index + 1}/{len(configs)}] {label}", flush=True)
        spec = GridSpec(
            a=1.02,
            n=1,
            magnetic_field=field,
            target_energy=450.0,
            nominal_spacing=0.03,
            eigenvalue_count=180,
            wall_factor=100.0,
            gauge=gauge,
        )
        values, metadata = compute_eigenvalues(spec)
        spectra[label] = values
        np.savez_compressed(output_dir / f"{label}.npz", eigenvalues=values)
        records.append({"label": label, "spec": asdict(spec), "solver": metadata})

    r100_dir = Path("results/r100_quantum_spectrum")
    archived = json.loads((r100_dir / "summary.json").read_text(encoding="utf-8"))
    archive_by_field = {
        record["spec"]["magnetic_field"]: np.load(r100_dir / record["spectrum_file"])[
            "eigenvalues"
        ]
        for record in archived["records"]
        if record["spec"]["a"] == 1.02
        and record["spec"]["nominal_spacing"] == 0.03
    }
    comparisons = {
        "symmetric_vs_landau_B1": relative_spectrum_difference(
            spectra["B1_symmetric"], spectra["B1_landau"]
        ),
        "B1_vs_Bminus1": relative_spectrum_difference(
            spectra["B1_symmetric"], spectra["Bm1_symmetric"]
        ),
        "B0_vs_archived": relative_spectrum_difference(
            spectra["B0_symmetric"], archive_by_field[0.0]
        ),
        "B1_vs_archived": relative_spectrum_difference(
            spectra["B1_symmetric"], archive_by_field[1.0]
        ),
    }
    max_residual = max(record["solver"]["max_relative_eigen_residual"] for record in records)
    max_orthogonality = max(record["solver"]["max_orthogonality_defect"] for record in records)
    source_paths = (
        Path("src/hp_candidate_search/quantum_fd.py"),
        Path("scripts/run_r105_quantum_numerical_audit.py"),
    )
    hashes = {
        str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths
    }
    gates = {
        "relative_residual_below_1e-8": max_residual < 1.0e-8,
        "orthogonality_below_1e-8": max_orthogonality < 1.0e-8,
        "gauge_spectra_agree_1e-10": comparisons["symmetric_vs_landau_B1"] < 1.0e-10,
        "plus_minus_B_agree_1e-10": comparisons["B1_vs_Bminus1"] < 1.0e-10,
        "archived_rerun_agrees_1e-10": max(
            comparisons["B0_vs_archived"], comparisons["B1_vs_archived"]
        )
        < 1.0e-10,
    }
    output = {
        "records": records,
        "comparisons": comparisons,
        "max_relative_eigen_residual": max_residual,
        "max_orthogonality_defect": max_orthogonality,
        "source_sha256": hashes,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "zero_data_loaded": False,
        "prime_data_loaded": False,
    }
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
