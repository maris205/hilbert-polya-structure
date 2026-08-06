#!/usr/bin/env python3
"""Run the clipped-boundary shifted-origin overlap audit."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.sparse import save_npz

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.operator import assemble_shifted_overlap_ulam, dominant_spectrum


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, required=True)
    parser.add_argument("--radius", nargs="+", type=float, required=True)
    parser.add_argument("--grid", nargs="+", type=int, required=True)
    parser.add_argument("--offset", nargs="+", type=float, required=True)
    parser.add_argument("--eigenvalue-count", type=int, default=8)
    parser.add_argument("--run-id", type=str, default="R049_shifted_overlap")
    parser.add_argument("--output-stem", type=str, default="shifted_overlap")
    parser.add_argument("--save-matrices", action="store_true")
    return parser.parse_args()


def serialize_complex(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def main() -> None:
    args = parse_args()
    records: list[dict[str, object]] = []
    all_passed = True
    for a_value in args.a:
        for radius in args.radius:
            for grid in args.grid:
                for offset in args.offset:
                    started = time.perf_counter()
                    assembly = assemble_shifted_overlap_ulam(
                        a=a_value,
                        radius=radius,
                        cells_per_axis=grid,
                        grid_offset=offset,
                    )
                    assembly_seconds = time.perf_counter() - started
                    started = time.perf_counter()
                    spectrum = dominant_spectrum(
                        assembly,
                        eigenvalue_count=args.eigenvalue_count,
                    )
                    spectrum_seconds = time.perf_counter() - started
                    leading_modulus = abs(spectrum.leading_eigenvalue)
                    residual_pass = max(
                        max(item.right_residual, item.left_residual)
                        for item in spectrum.eigenpairs
                    ) < 1.0e-7
                    contraction_pass = leading_modulus <= 1.0 + 1.0e-8
                    nontrivial_pass = bool(
                        np.any(assembly.active_cells) and assembly.matrix.nnz > 0
                    )
                    passed = bool(
                        residual_pass and contraction_pass and nontrivial_pass
                    )
                    all_passed = all_passed and passed
                    nominal_width = 2.0 * radius / grid
                    edges = np.concatenate(
                        (
                            np.asarray([-radius]),
                            -radius
                            + (np.arange(1, grid) + offset) * nominal_width,
                            np.asarray([radius]),
                        )
                    )
                    widths = np.diff(edges)
                    cell_areas = np.outer(widths, widths).ravel()
                    swap = np.arange(grid**2).reshape(grid, grid).T.ravel()
                    unnormalized = assembly.matrix.multiply(
                        cell_areas[:, None]
                    ).tocsr()
                    reversed_unnormalized = unnormalized[swap][:, swap].transpose()
                    reversibility_difference = (
                        unnormalized - reversed_unnormalized
                    )
                    weighted_reversibility_error = float(
                        np.max(
                            np.abs(reversibility_difference.data),
                            initial=0.0,
                        )
                    )
                    config_id = (
                        f"a{a_value:.8g}_R{radius:.8g}_N{grid}"
                        f"_shift{offset:+.6g}"
                    )
                    if args.save_matrices:
                        save_npz(
                            PROJECT_ROOT / "results" / f"ulam_{config_id}.npz",
                            assembly.matrix,
                        )
                    records.append(
                        {
                            "config_id": config_id,
                            "a": a_value,
                            "radius": radius,
                            "grid": grid,
                            "grid_offset": offset,
                            "nominal_cell_width": nominal_width,
                            "minimum_cell_width": float(np.min(widths)),
                            "maximum_cell_width": float(np.max(widths)),
                            "weighted_reversibility_error": weighted_reversibility_error,
                            "state_count": grid**2,
                            "method": assembly.method,
                            "survivor_horizon": 0,
                            "survivor_rule": "box_center_mask_horizon_0",
                            "hole_radius": 0.0,
                            "hole_center": None,
                            "active_cells": int(np.sum(assembly.active_cells)),
                            "matrix_nnz": int(assembly.matrix.nnz),
                            "minimum_row_sum": float(np.min(assembly.row_sums)),
                            "maximum_row_sum": float(np.max(assembly.row_sums)),
                            "leading_eigenvalue": serialize_complex(
                                spectrum.leading_eigenvalue
                            ),
                            "leading_modulus": leading_modulus,
                            "escape_rate": spectrum.escape_rate,
                            "eigenpairs": [
                                {
                                    "eigenvalue": serialize_complex(item.eigenvalue),
                                    "modulus": item.modulus,
                                    "right_residual": item.right_residual,
                                    "left_residual": item.left_residual,
                                    "condition_estimate": item.condition_estimate,
                                }
                                for item in spectrum.eigenpairs
                            ],
                            "assembly_seconds": assembly_seconds,
                            "spectrum_seconds": spectrum_seconds,
                            "residual_pass": residual_pass,
                            "contraction_pass": contraction_pass,
                            "nontrivial_operator_pass": nontrivial_pass,
                            "linear_solver_passed": passed,
                        }
                    )

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": args.run_id,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": (
            "semi-analytic overlap with clipped shifted boundary cells; "
            "H=0, no hole; rows are source-area normalized"
        ),
        "linear_solver_checks_passed": all_passed,
        "research_gate_passed": False,
        "research_gate_note": (
            "shifted tessellation is a finite-resolution boundary-alignment "
            "diagnostic, not a continuous operator convergence certificate"
        ),
        "records": records,
    }
    output_json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    flat_rows = [
        {key: value for key, value in record.items() if key != "eigenpairs"}
        for record in records
    ]
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat_rows[0]))
        writer.writeheader()
        writer.writerows(flat_rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "configurations": len(records),
                "linear_solver_checks_passed": all_passed,
            },
            indent=2,
        )
    )
    if not all_passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
