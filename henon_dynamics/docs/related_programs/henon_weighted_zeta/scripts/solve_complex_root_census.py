#!/usr/bin/env python3
"""Track all total-degree paths and census complex/real periodic points."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from joblib import Parallel, delayed

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.homotopy import (
    PathResult,
    cluster_endpoints,
    real_primitive_orbits,
    refine_complex_endpoint,
    total_degree_starts,
    track_path,
)
from henon_zeta.orbits import build_orbit_record, cyclic_distance


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, default=[0.9, 1.0056, 1.02])
    parser.add_argument("--min-period", type=int, default=1)
    parser.add_argument("--max-period", type=int, default=8)
    parser.add_argument("--gamma-angle", nargs="+", type=float, default=[0.371, 1.137])
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--cluster-tolerance", type=float, default=1.0e-7)
    parser.add_argument("--output-stem", type=str, default="complex_root_census")
    return parser.parse_args()


def track_period(a: float, period: int, gamma_angle: float, workers: int) -> list[PathResult]:
    gamma = complex(np.exp(1.0j * gamma_angle))
    starts = total_degree_starts(period)
    if workers == 1:
        return [track_path(start, a, gamma, path_index=index) for index, start in enumerate(starts)]
    return Parallel(n_jobs=workers, prefer="threads")(
        delayed(track_path)(start, a, gamma, path_index=index)
        for index, start in enumerate(starts)
    )


def catalogs_match(first: list[np.ndarray], second: list[np.ndarray], tolerance: float) -> bool:
    if len(first) != len(second):
        return False
    return all(
        any(float(np.linalg.norm(root - candidate, ord=np.inf)) <= tolerance for candidate in second)
        for root in first
    )


def conjugation_closed(roots: list[np.ndarray], tolerance: float) -> bool:
    return all(
        any(float(np.linalg.norm(np.conjugate(root) - candidate, ord=np.inf)) <= tolerance for candidate in roots)
        for root in roots
    )


def minimum_separation(roots: list[np.ndarray]) -> float:
    if len(roots) < 2:
        return float("inf")
    return min(
        float(np.linalg.norm(roots[first] - roots[second], ord=np.inf))
        for first in range(len(roots))
        for second in range(first + 1, len(roots))
    )


def json_refined_root(record: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in record.items() if key != "float_sequence"}


def main() -> None:
    args = parse_args()
    if args.min_period < 1 or args.max_period < args.min_period:
        raise SystemExit("require 1 <= --min-period <= --max-period")
    census_rows: list[dict[str, object]] = []
    orbit_rows: list[dict[str, object]] = []
    detailed_roots: list[dict[str, object]] = []
    all_passed = True

    for a_value in args.a:
        for period in range(args.min_period, args.max_period + 1):
            root_catalogs: list[list[np.ndarray]] = []
            refined_primary: list[dict[str, object]] = []
            gamma_summaries = []
            for gamma_index, gamma_angle in enumerate(args.gamma_angle):
                path_results = track_period(a_value, period, gamma_angle, args.workers)
                roots = cluster_endpoints(path_results, tolerance=args.cluster_tolerance)
                strict_roots = cluster_endpoints(
                    path_results, tolerance=args.cluster_tolerance / 10.0
                )
                loose_roots = cluster_endpoints(
                    path_results, tolerance=args.cluster_tolerance * 10.0
                )
                root_catalogs.append(roots)
                gamma_summaries.append(
                    {
                        "gamma_angle": gamma_angle,
                        "paths": len(path_results),
                        "successful_paths": sum(result.success for result in path_results),
                        "distinct_roots": len(roots),
                        "strict_distinct_roots": len(strict_roots),
                        "loose_distinct_roots": len(loose_roots),
                        "minimum_root_separation": minimum_separation(roots),
                        "maximum_float_residual": max((result.residual_inf for result in path_results), default=float("inf")),
                        "rejected_steps": sum(result.rejected_steps for result in path_results),
                        "maximum_condition": max((result.maximum_condition for result in path_results), default=float("inf")),
                    }
                )
                if gamma_index == 0:
                    refined_primary = [
                        refine_complex_endpoint(root, a_value, dps=args.dps)
                        for root in roots
                    ]

            expected = 2**period
            primary_roots = root_catalogs[0]
            primitive_orbits = real_primitive_orbits(
                refined_primary,
                period,
                cluster_tolerance=args.cluster_tolerance,
            )
            strict_primitive_orbits = real_primitive_orbits(
                refined_primary,
                period,
                cluster_tolerance=args.cluster_tolerance / 10.0,
            )
            loose_primitive_orbits = real_primitive_orbits(
                refined_primary,
                period,
                cluster_tolerance=args.cluster_tolerance * 10.0,
            )
            real_root_count = sum(bool(record["is_real"]) for record in refined_primary)
            gamma_match = all(
                catalogs_match(primary_roots, catalog, args.cluster_tolerance)
                for catalog in root_catalogs[1:]
            )
            paths_complete = all(
                summary["successful_paths"] == expected
                and summary["distinct_roots"] == expected
                and summary["strict_distinct_roots"] == expected
                and summary["loose_distinct_roots"] == expected
                for summary in gamma_summaries
            )
            threshold_stability_pass = (
                len(strict_primitive_orbits)
                == len(primitive_orbits)
                == len(loose_primitive_orbits)
            )
            high_precision_pass = all(
                bool(record["converged"]) and float(record["residual_inf"]) < 10.0 ** (-(args.dps - 25))
                for record in refined_primary
            )
            conjugate_pass = conjugation_closed(primary_roots, args.cluster_tolerance)
            row_passed = bool(
                paths_complete
                and high_precision_pass
                and conjugate_pass
                and gamma_match
                and threshold_stability_pass
            )
            all_passed = all_passed and row_passed

            census_rows.append(
                {
                    "a": a_value,
                    "period": period,
                    "bezout_expected_roots": expected,
                    "primary_distinct_roots": len(primary_roots),
                    "real_fixed_points_of_Hn": real_root_count,
                    "real_primitive_orbits": len(primitive_orbits),
                    "gamma_catalogs_match": gamma_match,
                    "threshold_stability_pass": threshold_stability_pass,
                    "conjugation_closed": conjugate_pass,
                    "high_precision_pass": high_precision_pass,
                    "passed": row_passed,
                    "gamma_summaries": gamma_summaries,
                }
            )

            for root_index, record in enumerate(refined_primary):
                detailed_roots.append(
                    {
                        "a": a_value,
                        "period": period,
                        "root_index": root_index,
                        **json_refined_root(record),
                    }
                )

            for orbit_index, sequence in enumerate(primitive_orbits):
                orbit = build_orbit_record(a_value, sequence, solver_success=True)
                orbit.orbit_id = f"hom_a{a_value:.8g}_n{period:02d}_o{orbit_index:04d}"
                orbit_rows.append(orbit.to_dict())

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    orbit_csv = PROJECT_ROOT / "results" / f"{args.output_stem}_real_primitive_orbits.csv"
    payload = {
        "run_id": "R013_total_degree_homotopy",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": "total-degree complex homotopy with two gamma angles and arbitrary-precision endpoint refinement",
        "scope": "numerical all-path census for generic finite periods; not a computer-assisted proof",
        "parameters": {
            "a": args.a,
            "min_period": args.min_period,
            "max_period": args.max_period,
            "gamma_angles": args.gamma_angle,
            "workers": args.workers,
            "dps": args.dps,
            "cluster_tolerance": args.cluster_tolerance,
        },
        "passed": all_passed,
        "census": census_rows,
        "real_primitive_orbits": orbit_rows,
        "roots": detailed_roots,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    flat_census = []
    for row in census_rows:
        flat_census.append({key: value for key, value in row.items() if key != "gamma_summaries"})
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat_census[0]))
        writer.writeheader()
        writer.writerows(flat_census)

    flat_orbits = []
    for row in orbit_rows:
        flat_orbits.append(
            {
                "orbit_id": row["orbit_id"],
                "a": row["a"],
                "period": row["period"],
                "sequence": ";".join(f"{value:.17g}" for value in row["sequence"]),
                "stability": row["stability"],
                "trace": row["trace"],
                "determinant_error": row["determinant_error"],
                "action": row["action"],
            }
        )
    with orbit_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat_orbits[0]))
        writer.writeheader()
        writer.writerows(flat_orbits)

    print(
        json.dumps(
            {
                "json": str(output_json),
                "census_csv": str(output_csv),
                "orbit_csv": str(orbit_csv),
                "period_parameter_rows": len(census_rows),
                "real_primitive_orbits": len(orbit_rows),
                "passed": all_passed,
            },
            indent=2,
        )
    )
    if not all_passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
