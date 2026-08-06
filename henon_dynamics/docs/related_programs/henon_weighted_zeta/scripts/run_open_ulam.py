#!/usr/bin/env python3
"""Assemble and audit standard absorbing two-dimensional Ulam operators."""

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

from henon_zeta.operator import (
    assemble_absorbing_ulam,
    assemble_overlap_ulam,
    assemble_sobol_ulam,
    dominant_spectrum,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, required=True)
    parser.add_argument("--radius", nargs="+", type=float, required=True)
    parser.add_argument("--grid", nargs="+", type=int, default=[64, 96, 128])
    parser.add_argument(
        "--method",
        choices=["gauss-legendre", "sobol", "overlap"],
        default="gauss-legendre",
    )
    parser.add_argument("--quadrature-order", type=int, default=4)
    parser.add_argument("--samples-per-cell", type=int, default=64)
    parser.add_argument("--seed", nargs="+", type=int, default=[20260801])
    parser.add_argument("--hole-radius", nargs="+", type=float, default=[0.0])
    parser.add_argument("--survivor-horizon", type=int, default=0)
    parser.add_argument("--eigenvalue-count", type=int, default=8)
    parser.add_argument("--output-stem", type=str, default="open_ulam")
    parser.add_argument("--run-id", type=str, default="R040_open_ulam")
    parser.add_argument("--save-matrices", action="store_true")
    args = parser.parse_args()
    if args.method == "overlap" and any(
        hole_radius != 0.0 for hole_radius in args.hole_radius
    ):
        parser.error("--method overlap currently requires --hole-radius 0")
    return args


def serialize_complex(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def main() -> None:
    args = parse_args()
    if args.method == "overlap" and any(a_value < 0.0 for a_value in args.a):
        raise ValueError("--method overlap requires nonnegative a")
    records = []
    all_linear_solver_passed = True
    all_nontrivial_operator_passed = True
    for a_value in args.a:
        for radius in args.radius:
            for grid in args.grid:
                seeds: list[int | None] = args.seed if args.method == "sobol" else [None]
                for hole_radius in args.hole_radius:
                    for seed in seeds:
                        start = time.perf_counter()
                        if args.method == "gauss-legendre":
                            assembly = assemble_absorbing_ulam(
                                a=a_value,
                                radius=radius,
                                cells_per_axis=grid,
                                quadrature_order=args.quadrature_order,
                                hole_radius=hole_radius,
                                survivor_horizon=args.survivor_horizon,
                            )
                        elif args.method == "overlap":
                            assembly = assemble_overlap_ulam(
                                a=a_value,
                                radius=radius,
                                cells_per_axis=grid,
                                survivor_horizon=args.survivor_horizon,
                            )
                        else:
                            assert seed is not None
                            assembly = assemble_sobol_ulam(
                                a=a_value,
                                radius=radius,
                                cells_per_axis=grid,
                                samples_per_cell=args.samples_per_cell,
                                seed=seed,
                                hole_radius=hole_radius,
                                survivor_horizon=args.survivor_horizon,
                            )
                        assembly_seconds = time.perf_counter() - start
                        start = time.perf_counter()
                        spectrum = dominant_spectrum(
                            assembly, eigenvalue_count=args.eigenvalue_count
                        )
                        spectrum_seconds = time.perf_counter() - start
                        active_sums = assembly.row_sums[assembly.active_cells]
                        if active_sums.size:
                            mean_active_row_sum: float | None = float(np.mean(active_sums))
                            minimum_active_row_sum: float | None = float(np.min(active_sums))
                            maximum_active_row_sum: float | None = float(np.max(active_sums))
                            leaky_active_row_fraction: float | None = float(
                                np.mean(active_sums < 1.0 - 1.0e-12)
                            )
                            zero_active_row_fraction: float | None = float(
                                np.mean(active_sums == 0.0)
                            )
                        else:
                            mean_active_row_sum = None
                            minimum_active_row_sum = None
                            maximum_active_row_sum = None
                            leaky_active_row_fraction = None
                            zero_active_row_fraction = None
                        leading_modulus = abs(spectrum.leading_eigenvalue)
                        active_cell_count = int(np.sum(assembly.active_cells))
                        nontrivial_operator_pass = bool(
                            active_cell_count > 0 and assembly.matrix.nnz > 0
                        )
                        residual_pass = max(
                            max(item.right_residual, item.left_residual)
                            for item in spectrum.eigenpairs
                        ) < 1.0e-7
                        contraction_pass = leading_modulus <= 1.0 + 1.0e-8
                        linear_solver_passed = bool(
                            residual_pass
                            and contraction_pass
                            and nontrivial_operator_pass
                        )
                        all_linear_solver_passed = (
                            all_linear_solver_passed and linear_solver_passed
                        )
                        all_nontrivial_operator_passed = (
                            all_nontrivial_operator_passed
                            and nontrivial_operator_pass
                        )
                        if args.method == "gauss-legendre":
                            config_id = (
                                f"a{a_value:.8g}_R{radius:.6g}_N{grid}_q{args.quadrature_order}"
                                f"_hole{hole_radius:.6g}_H{args.survivor_horizon}"
                            )
                        elif args.method == "overlap":
                            config_id = (
                                f"a{a_value:.8g}_R{radius:.6g}_N{grid}"
                                f"_overlap_H{args.survivor_horizon}"
                            )
                        else:
                            config_id = (
                                f"a{a_value:.8g}_R{radius:.6g}_N{grid}_sobol{args.samples_per_cell}"
                                f"_seed{seed}_hole{hole_radius:.6g}_H{args.survivor_horizon}"
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
                                "state_count": grid**2,
                                "method": assembly.method,
                                "quadrature_order": assembly.quadrature_order,
                                "samples_per_cell": assembly.samples_per_cell,
                                "seed": assembly.seed,
                                "survivor_horizon": assembly.survivor_horizon,
                                "survivor_rule": assembly.survivor_rule,
                                "hole_radius": hole_radius,
                                "hole_center": (
                                    list(assembly.hole_center)
                                    if assembly.hole_center
                                    else None
                                ),
                                "active_cells": active_cell_count,
                                "matrix_nnz": int(assembly.matrix.nnz),
                                "mean_active_row_sum": mean_active_row_sum,
                                "minimum_active_row_sum": minimum_active_row_sum,
                                "maximum_active_row_sum": maximum_active_row_sum,
                                "leaky_active_row_fraction": leaky_active_row_fraction,
                                "zero_active_row_fraction": zero_active_row_fraction,
                                "leading_eigenvalue": serialize_complex(
                                    spectrum.leading_eigenvalue
                                ),
                                "leading_modulus": leading_modulus,
                                "escape_rate": spectrum.escape_rate,
                                "elliptic_mass_fraction_r03": (
                                    spectrum.elliptic_mass_fraction_r03
                                ),
                                "reference_fixed_point_mass_fraction_r03": (
                                    spectrum.elliptic_mass_fraction_r03
                                ),
                                "reference_fixed_point_stability": (
                                    spectrum.reference_fixed_point_stability
                                ),
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
                                "nontrivial_operator_pass": nontrivial_operator_pass,
                                "linear_solver_passed": linear_solver_passed,
                            }
                        )

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": args.run_id,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": {
            "gauss-legendre": "tensor Gauss-Legendre finite-volume Ulam",
            "sobol": "independently randomized-shift Sobol cell-sampling Ulam",
            "overlap": "semi-analytic finite-volume cell-overlap Ulam",
        }[args.method]
        + "; substochastic rows; no escape-mass renormalization",
        "linear_solver_checks_passed": all_linear_solver_passed,
        "nontrivial_operator_checks_passed": all_nontrivial_operator_passed,
        "research_gate_passed": False,
        "research_gate_note": "operator convergence, common-domain cycle agreement, and pseudospectral checks are assessed separately",
        "records": records,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    flat_rows = []
    for record in records:
        flat_rows.append({key: value for key, value in record.items() if key not in {"eigenpairs", "hole_center"}})
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
                "linear_solver_checks_passed": all_linear_solver_passed,
                "nontrivial_operator_checks_passed": (
                    all_nontrivial_operator_passed
                ),
            },
            indent=2,
        )
    )
    if not all_linear_solver_passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
