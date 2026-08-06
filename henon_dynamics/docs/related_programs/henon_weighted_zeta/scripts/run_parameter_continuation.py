#!/usr/bin/env python3
"""Run the R042 parameter continuation from the hyperbolic control to mixed phase.

This is deliberately an exploratory continuation, not a completeness or
uniform-hyperbolicity certificate.  For every sampled ``a`` it combines the
same finite real-orbit search with (i) box-filtered cycle diagnostics and (ii)
absorbing Ulam spectra on the requested boxes and grids.  The output keeps the
Euler-product diagnostic and the Perron flat-trace diagnostic separate.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
import time
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.operator import assemble_absorbing_ulam, dominant_spectrum
from henon_zeta.orbits import OrbitRecord, search_periods
from henon_zeta.geometry import fixed_points, sequence_points
from henon_zeta.zeta import (
    determinant_coefficients,
    leading_resonance_from_determinant,
    perron_fredholm_coefficients,
)


DEFAULT_A_VALUES = (
    1.0056,
    1.02,
    1.10,
    1.20,
    1.24,
    1.26,
    2.00,
    2.90,
    3.10,
    3.90,
    4.10,
    5.00,
    6.00,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, default=list(DEFAULT_A_VALUES))
    parser.add_argument("--max-period", type=int, default=8)
    parser.add_argument("--random-starts", type=int, default=256)
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--root-tolerance", type=float, default=1.0e-12)
    parser.add_argument("--acceptance-tolerance", type=float, default=1.0e-11)
    parser.add_argument("--cluster-tolerance", type=float, default=1.0e-8)
    parser.add_argument("--radius", nargs="+", type=float, default=[1.0, 2.5])
    parser.add_argument("--grid", nargs="+", type=int, default=[64, 96])
    parser.add_argument("--quadrature-order", type=int, default=4)
    parser.add_argument("--beta", nargs="+", type=float, default=[0.0, 0.5, 1.0])
    parser.add_argument("--eigenvalue-count", type=int, default=8)
    parser.add_argument("--output-stem", type=str, default="parameter_continuation_r042")
    return parser.parse_args()


def serialize_complex(value: complex | None) -> list[float] | None:
    if value is None:
        return None
    return [float(value.real), float(value.imag)]


def in_box(record: OrbitRecord, radius: float) -> bool:
    points = sequence_points(record.sequence)
    return bool(np.all(np.abs(points) < float(radius)))


def stability_counts(records: list[OrbitRecord]) -> dict[str, int]:
    counts = Counter(record.stability for record in records)
    return {
        "hyperbolic": int(counts.get("hyperbolic", 0)),
        "elliptic": int(counts.get("elliptic", 0)),
        "parabolic": int(counts.get("parabolic", 0)),
    }


def orbit_summary(a_value: float, records: list[OrbitRecord], radius: float) -> dict[str, object]:
    inside = [record for record in records if in_box(record, radius)]
    counts = stability_counts(inside)
    by_period: dict[str, dict[str, int]] = {}
    for period in range(1, max((record.period for record in records), default=0) + 1):
        period_records = [record for record in inside if record.period == period]
        by_period[str(period)] = {
            "total": len(period_records),
            **stability_counts(period_records),
        }
    total = len(inside)
    return {
        "a": float(a_value),
        "radius": float(radius),
        "catalog_orbit_count": len(records),
        "in_box_orbit_count": total,
        "hyperbolic_count": counts["hyperbolic"],
        "elliptic_count": counts["elliptic"],
        "parabolic_count": counts["parabolic"],
        "elliptic_fraction": (counts["elliptic"] / total) if total else None,
        "hyperbolic_fraction": (counts["hyperbolic"] / total) if total else None,
        "self_reversing_count": int(sum(record.self_reversing for record in inside)),
        "reversor_pair_fraction": (
            float(np.mean([record.reversor_partner_found for record in inside]))
            if inside
            else None
        ),
        "period_counts": by_period,
    }


def cycle_curve(
    records: list[OrbitRecord],
    radius: float,
    beta: float,
    max_period: int,
) -> list[dict[str, object]]:
    eligible = [record for record in records if in_box(record, radius)]
    hyperbolic = [record for record in eligible if record.stability == "hyperbolic"]
    rows: list[dict[str, object]] = []
    previous_euler: complex | None = None
    previous_fredholm: complex | None = None
    for cutoff in range(1, max_period + 1):
        determinant = determinant_coefficients(hyperbolic, cutoff, beta)
        euler_resonance = leading_resonance_from_determinant(determinant)
        fredholm_resonance: complex | None = None
        fredholm_error: str | None = None
        try:
            # Include elliptic records in this separate flat-trace diagnostic;
            # it is not silently identified with the Euler product.
            fredholm = perron_fredholm_coefficients(eligible, cutoff)
            fredholm_resonance = leading_resonance_from_determinant(fredholm)
        except (ValueError, FloatingPointError) as error:
            fredholm_error = str(error)
        rows.append(
            {
                "a": float(records[0].a) if records else None,
                "radius": float(radius),
                "beta": float(beta),
                "period_cutoff": int(cutoff),
                "in_box_orbit_count": len(eligible),
                "hyperbolic_orbit_count": len(hyperbolic),
                "euler_resonance": serialize_complex(euler_resonance),
                "euler_modulus": None if euler_resonance is None else abs(euler_resonance),
                "euler_cutoff_change": (
                    None
                    if euler_resonance is None or previous_euler is None
                    else abs(euler_resonance - previous_euler)
                ),
                "euler_highest_coefficient_modulus": float(abs(determinant[-1])),
                "fredholm_resonance": serialize_complex(fredholm_resonance),
                "fredholm_modulus": (
                    None if fredholm_resonance is None else abs(fredholm_resonance)
                ),
                "fredholm_cutoff_change": (
                    None
                    if fredholm_resonance is None or previous_fredholm is None
                    else abs(fredholm_resonance - previous_fredholm)
                ),
                "fredholm_error": fredholm_error,
            }
        )
        if euler_resonance is not None:
            previous_euler = euler_resonance
        if fredholm_resonance is not None:
            previous_fredholm = fredholm_resonance
    return rows


def leading_condition(spectrum: object) -> float | None:
    # SpectrumAudit exposes a tuple of EigenpairAudit objects.  Match by the
    # selected Perron eigenvalue rather than relying on eigensolver ordering.
    leading = complex(spectrum.leading_eigenvalue)
    candidates = list(spectrum.eigenpairs)
    if not candidates:
        return None
    item = min(candidates, key=lambda candidate: abs(candidate.eigenvalue - leading))
    return float(item.condition_estimate)


def main() -> None:
    args = parse_args()
    if args.max_period < 1:
        raise SystemExit("--max-period must be positive")
    records_by_a: dict[float, list[OrbitRecord]] = {}
    search_stats: list[dict[str, object]] = []
    started = time.perf_counter()

    for index, a_value in enumerate(args.a):
        records, stats = search_periods(
            a=float(a_value),
            max_period=args.max_period,
            random_starts=args.random_starts,
            seed=args.seed + 100_003 * index,
            root_tolerance=args.root_tolerance,
            acceptance_tolerance=args.acceptance_tolerance,
            cluster_tolerance=args.cluster_tolerance,
        )
        records_by_a[float(a_value)] = records
        search_stats.extend(asdict(item) for item in stats)
        print(
            json.dumps(
                {
                    "stage": "orbit_search",
                    "a": a_value,
                    "orbit_count": len(records),
                    "period_counts": [item.orbit_count for item in stats],
                    "stability": stability_counts(records),
                },
                sort_keys=True,
            ),
            flush=True,
        )

    summaries: list[dict[str, object]] = []
    cycle_rows: list[dict[str, object]] = []
    operator_rows: list[dict[str, object]] = []
    comparison_rows: list[dict[str, object]] = []

    for a_value in args.a:
        records = records_by_a[float(a_value)]
        for radius in args.radius:
            summaries.append(orbit_summary(float(a_value), records, float(radius)))
            for beta in args.beta:
                cycle_rows.extend(cycle_curve(records, float(radius), float(beta), args.max_period))

            for grid in args.grid:
                assembly_start = time.perf_counter()
                assembly = assemble_absorbing_ulam(
                    a=float(a_value),
                    radius=float(radius),
                    cells_per_axis=int(grid),
                    quadrature_order=args.quadrature_order,
                )
                assembly_seconds = time.perf_counter() - assembly_start
                spectrum_start = time.perf_counter()
                spectrum = dominant_spectrum(assembly, eigenvalue_count=args.eigenvalue_count)
                spectrum_seconds = time.perf_counter() - spectrum_start
                operator_row = {
                    "a": float(a_value),
                    "radius": float(radius),
                    "grid": int(grid),
                    "quadrature_order": int(args.quadrature_order),
                    "state_count": int(grid**2),
                    "active_cells": int(np.sum(assembly.active_cells)),
                    "matrix_nnz": int(assembly.matrix.nnz),
                    "leading_eigenvalue": serialize_complex(spectrum.leading_eigenvalue),
                    "leading_modulus": float(abs(spectrum.leading_eigenvalue)),
                    "escape_rate": float(spectrum.escape_rate),
                    "elliptic_mass_fraction_r03": float(spectrum.elliptic_mass_fraction_r03),
                    "reference_fixed_point_mass_fraction_r03": float(
                        spectrum.elliptic_mass_fraction_r03
                    ),
                    "reference_fixed_point_stability": fixed_points(float(a_value))[
                        0
                    ].stability,
                    "leading_condition_estimate": leading_condition(spectrum),
                    "max_eigenpair_condition_estimate": float(
                        max(item.condition_estimate for item in spectrum.eigenpairs)
                    ),
                    "max_eigenpair_right_residual": float(
                        max(item.right_residual for item in spectrum.eigenpairs)
                    ),
                    "max_eigenpair_left_residual": float(
                        max(item.left_residual for item in spectrum.eigenpairs)
                    ),
                    "mean_active_row_sum": float(
                        np.mean(assembly.row_sums[assembly.active_cells])
                    ),
                    "leaky_active_row_fraction": float(
                        np.mean(assembly.row_sums[assembly.active_cells] < 1.0 - 1.0e-12)
                    ),
                    "assembly_seconds": float(assembly_seconds),
                    "spectrum_seconds": float(spectrum_seconds),
                }
                operator_rows.append(operator_row)
                for beta in args.beta:
                    for cycle in [
                        row
                        for row in cycle_rows
                        if row["a"] == float(a_value)
                        and row["radius"] == float(radius)
                        and row["beta"] == float(beta)
                    ]:
                        operator_modulus = operator_row["leading_modulus"]
                        euler_modulus = cycle["euler_modulus"]
                        fredholm_modulus = cycle["fredholm_modulus"]
                        comparison_rows.append(
                            {
                                "a": float(a_value),
                                "radius": float(radius),
                                "grid": int(grid),
                                "beta": float(beta),
                                "period_cutoff": cycle["period_cutoff"],
                                "in_box_orbit_count": cycle["in_box_orbit_count"],
                                "hyperbolic_orbit_count": cycle["hyperbolic_orbit_count"],
                                "operator_modulus": operator_modulus,
                                "operator_escape_rate": operator_row["escape_rate"],
                                "elliptic_mass_fraction_r03": operator_row[
                                    "elliptic_mass_fraction_r03"
                                ],
                                "reference_fixed_point_mass_fraction_r03": operator_row[
                                    "reference_fixed_point_mass_fraction_r03"
                                ],
                                "reference_fixed_point_stability": operator_row[
                                    "reference_fixed_point_stability"
                                ],
                                "leading_condition_estimate": operator_row[
                                    "leading_condition_estimate"
                                ],
                                "euler_modulus": euler_modulus,
                                "fredholm_modulus": fredholm_modulus,
                                "euler_relative_gap": (
                                    None
                                    if euler_modulus is None
                                    else abs(euler_modulus - operator_modulus)
                                    / max(operator_modulus, 1.0e-15)
                                ),
                                "fredholm_relative_gap": (
                                    None
                                    if fredholm_modulus is None
                                    else abs(fredholm_modulus - operator_modulus)
                                    / max(operator_modulus, 1.0e-15)
                                ),
                                "euler_cutoff_change": cycle["euler_cutoff_change"],
                                "fredholm_cutoff_change": cycle["fredholm_cutoff_change"],
                                "fredholm_error": cycle["fredholm_error"],
                            }
                        )

    payload = {
        "run_id": "R042_parameter_continuation",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": (
            "exploratory continuation; real multistart catalog plus box-filtered "
            "Euler/Fredholm cycle diagnostics and tensor Gauss-Legendre absorbing Ulam"
        ),
        "scope_note": (
            "Finite-period catalogs are not complete proofs. The Euler product and "
            "Perron flat-trace diagnostic are reported as distinct objects; no claim "
            "of exact transfer-operator equivalence is made."
        ),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "parameters": vars(args),
        "elapsed_seconds": time.perf_counter() - started,
        "search_stats": search_stats,
        "orbit_summaries": summaries,
        "cycle_rows": cycle_rows,
        "operator_rows": operator_rows,
        "comparison_rows": comparison_rows,
        "orbits": [record.to_dict() for records in records_by_a.values() for record in records],
    }
    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if comparison_rows:
        with output_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(comparison_rows[0]))
            writer.writeheader()
            writer.writerows(comparison_rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "parameters": len(args.a),
                "boxes": len(args.radius),
                "grids": len(args.grid),
                "comparisons": len(comparison_rows),
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
