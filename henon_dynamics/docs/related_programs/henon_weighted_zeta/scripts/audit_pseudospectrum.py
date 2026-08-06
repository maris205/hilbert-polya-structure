#!/usr/bin/env python3
"""Estimate local resolvent growth around the leading open-map resonance.

The calculation is a finite-dimensional numerical audit, not a rigorous
pseudospectral enclosure.  It estimates ||(L-zI)^(-1)||_2 by alternating sparse
LU solves for the resolvent and its adjoint on circles around the selected
Perron eigenvalue.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.sparse import eye
from scipy.sparse.linalg import splu

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
    parser.add_argument("--a", type=float, required=True)
    parser.add_argument("--radius", type=float, required=True)
    parser.add_argument("--grid", nargs="+", type=int, default=[64, 96, 128])
    parser.add_argument(
        "--method",
        choices=["gauss-legendre", "sobol", "overlap"],
        default="gauss-legendre",
    )
    parser.add_argument("--quadrature-order", type=int, default=8)
    parser.add_argument("--samples-per-cell", type=int, default=256)
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--epsilon", nargs="+", type=float, default=[1.0e-4, 1.0e-3, 1.0e-2])
    parser.add_argument("--angles", type=int, default=8)
    parser.add_argument("--power-iterations", type=int, default=15)
    parser.add_argument("--eigenvalue-count", type=int, default=8)
    parser.add_argument("--output-stem", type=str, default="pseudospectrum_audit")
    return parser.parse_args()


def serialize_complex(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def resolvent_norm_estimate(
    operator: object,
    shift: complex,
    iterations: int,
    seed: int,
) -> float:
    size = operator.shape[0]
    shifted = operator - shift * eye(size, format="csc")
    factor = splu(shifted.tocsc())
    generator = np.random.default_rng(seed)
    vector = generator.standard_normal(size) + 1.0j * generator.standard_normal(size)
    vector /= np.linalg.norm(vector)
    estimate = 0.0
    for _ in range(iterations):
        image = factor.solve(vector)
        estimate = float(np.linalg.norm(image))
        if estimate == 0.0:
            return 0.0
        image /= estimate
        vector = factor.solve(image, trans="H")
        vector_norm = float(np.linalg.norm(vector))
        if vector_norm == 0.0:
            return estimate
        vector /= vector_norm
    return estimate


def main() -> None:
    args = parse_args()
    if args.angles < 1 or args.power_iterations < 1:
        raise SystemExit("--angles and --power-iterations must be positive")
    rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []

    for grid in args.grid:
        if args.method == "gauss-legendre":
            assembly = assemble_absorbing_ulam(
                a=args.a,
                radius=args.radius,
                cells_per_axis=grid,
                quadrature_order=args.quadrature_order,
            )
        elif args.method == "overlap":
            assembly = assemble_overlap_ulam(
                a=args.a,
                radius=args.radius,
                cells_per_axis=grid,
            )
        else:
            assembly = assemble_sobol_ulam(
                a=args.a,
                radius=args.radius,
                cells_per_axis=grid,
                samples_per_cell=args.samples_per_cell,
                seed=args.seed,
            )
        spectrum = dominant_spectrum(assembly, eigenvalue_count=args.eigenvalue_count)
        leading = complex(spectrum.leading_eigenvalue)
        leading_audit = min(
            spectrum.eigenpairs,
            key=lambda item: abs(item.eigenvalue - leading),
        )
        operator = assembly.matrix.transpose().tocsc().astype(np.complex128)

        for epsilon_index, epsilon in enumerate(args.epsilon):
            estimates: list[float] = []
            started = time.perf_counter()
            for angle_index in range(args.angles):
                angle = 2.0 * np.pi * angle_index / args.angles
                shift = leading + epsilon * np.exp(1.0j * angle)
                estimate = resolvent_norm_estimate(
                    operator,
                    shift,
                    args.power_iterations,
                    args.seed + 1009 * grid + 97 * epsilon_index + angle_index,
                )
                estimates.append(estimate)
                rows.append(
                    {
                        "a": args.a,
                        "radius": args.radius,
                        "grid": grid,
                        "method": assembly.method,
                        "samples_per_cell": assembly.samples_per_cell,
                        "seed": assembly.seed,
                        "leading_real": leading.real,
                        "leading_imag": leading.imag,
                        "leading_modulus": abs(leading),
                        "leading_condition_estimate": leading_audit.condition_estimate,
                        "epsilon": epsilon,
                        "angle": angle,
                        "shift_real": shift.real,
                        "shift_imag": shift.imag,
                        "resolvent_norm_estimate": estimate,
                        "epsilon_times_resolvent": epsilon * estimate,
                        "scaled_by_eigenvalue_condition": (
                            epsilon * estimate / leading_audit.condition_estimate
                        ),
                    }
                )
            scaled = np.asarray(estimates) * epsilon
            summaries.append(
                {
                    "a": args.a,
                    "radius": args.radius,
                    "grid": grid,
                    "method": assembly.method,
                    "leading_eigenvalue": serialize_complex(leading),
                    "leading_condition_estimate": leading_audit.condition_estimate,
                    "epsilon": epsilon,
                    "minimum_epsilon_times_resolvent": float(np.min(scaled)),
                    "median_epsilon_times_resolvent": float(np.median(scaled)),
                    "maximum_epsilon_times_resolvent": float(np.max(scaled)),
                    "maximum_to_condition_ratio": float(
                        np.max(scaled) / leading_audit.condition_estimate
                    ),
                    "seconds": time.perf_counter() - started,
                }
            )

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": "R046_local_pseudospectrum_audit",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": "local resolvent 2-norm power estimate from alternating sparse LU solves",
        "scope": "finite-dimensional numerical estimate; not a rigorous pseudospectral enclosure",
        "parameters": vars(args),
        "summaries": summaries,
        "rows": rows,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "configurations": len(summaries),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
