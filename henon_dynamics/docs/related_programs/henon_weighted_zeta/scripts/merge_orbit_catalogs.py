#!/usr/bin/env python3
"""Merge validated orbit catalogs while removing overlapping period blocks."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.controls import divisors, mobius
from henon_zeta.orbits import OrbitRecord, cyclic_distance
from scripts.build_cycle_coefficients import load_orbits, validate_catalog


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", nargs="+", type=Path, required=True)
    parser.add_argument("--cluster-tolerance", type=float, default=1.0e-8)
    parser.add_argument("--expect-binary-full-shift", action="store_true")
    parser.add_argument("--output-stem", type=str, required=True)
    return parser.parse_args()


def binary_full_shift_primitive_orbits(period: int) -> int:
    numerator = sum(
        mobius(divisor) * 2 ** (period // divisor)
        for divisor in divisors(period)
    )
    quotient, remainder = divmod(numerator, period)
    if remainder:
        raise ArithmeticError("binary full-shift count failed integrality check")
    return quotient


def merge_records(
    catalogs: list[list[OrbitRecord]], tolerance: float
) -> list[OrbitRecord]:
    merged: list[OrbitRecord] = []
    for records in catalogs:
        for record in records:
            duplicate_index = next(
                (
                    index
                    for index, candidate in enumerate(merged)
                    if candidate.a == record.a
                    and candidate.period == record.period
                    and cyclic_distance(candidate.sequence, record.sequence) <= tolerance
                ),
                None,
            )
            if duplicate_index is None:
                merged.append(record)
            elif record.scaled_residual_inf < merged[duplicate_index].scaled_residual_inf:
                merged[duplicate_index] = record
    merged.sort(key=lambda record: (record.a, record.period, record.sequence))
    return merged


def main() -> None:
    args = parse_args()
    sources: list[dict[str, object]] = []
    catalogs: list[list[OrbitRecord]] = []
    for path in args.input:
        source, records = load_orbits(path)
        validate_catalog(records, tolerance=args.cluster_tolerance)
        sources.append(
            {
                "path": str(path),
                "run_id": source.get("run_id"),
                "record_count": len(records),
            }
        )
        catalogs.append(records)

    merged = merge_records(catalogs, args.cluster_tolerance)
    validate_catalog(merged, tolerance=args.cluster_tolerance)
    parameters = sorted({record.a for record in merged})
    periods = sorted({record.period for record in merged})
    counts = Counter(record.period for record in merged)
    expected: dict[str, int] = {}
    if args.expect_binary_full_shift:
        if len(parameters) != 1:
            raise SystemExit("binary full-shift check requires exactly one map parameter")
        failures: list[str] = []
        for period in range(1, max(periods) + 1):
            expected_count = binary_full_shift_primitive_orbits(period)
            expected[str(period)] = expected_count
            if counts.get(period, 0) != expected_count:
                failures.append(
                    f"period {period}: expected {expected_count}, got {counts.get(period, 0)}"
                )
        nonhyperbolic = [record.orbit_id for record in merged if record.stability != "hyperbolic"]
        if nonhyperbolic:
            failures.append(f"nonhyperbolic records: {nonhyperbolic[:5]}")
        if failures:
            raise SystemExit("binary full-shift gate failed: " + "; ".join(failures))

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": "R043_merged_high_period_catalog",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": "merge diagnostic-passing finite-period orbit catalogs with cyclic deduplication",
        "scope": "finite-period numerical all-path evidence; not an interval-certified global proof",
        "sources": sources,
        "parameters": parameters,
        "min_period": min(periods),
        "max_period": max(periods),
        "period_counts": {str(period): counts[period] for period in periods},
        "binary_full_shift_expected_counts": expected or None,
        "binary_full_shift_gate_passed": bool(args.expect_binary_full_shift),
        "real_primitive_orbits": [record.to_dict() for record in merged],
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rows = [
        {
            "orbit_id": record.orbit_id,
            "a": record.a,
            "period": record.period,
            "sequence": ";".join(f"{value:.17g}" for value in record.sequence),
            "stability": record.stability,
            "trace": record.trace,
            "determinant_error": record.determinant_error,
            "scaled_residual_inf": record.scaled_residual_inf,
            "action": record.action,
        }
        for record in merged
    ]
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "orbit_count": len(merged),
                "period_counts": payload["period_counts"],
                "binary_full_shift_gate_passed": payload[
                    "binary_full_shift_gate_passed"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
