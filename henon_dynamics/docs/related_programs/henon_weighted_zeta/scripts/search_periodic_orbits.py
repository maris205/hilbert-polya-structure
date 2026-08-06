#!/usr/bin/env python3
"""Run the real multistart periodic-orbit smoke search."""

from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.controls import (
    analytic_period2,
    analytic_period3,
    analytic_period3_traces,
)
from henon_zeta.orbits import OrbitRecord, cyclic_distance, search_periods


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, default=[1.0056, 1.02])
    parser.add_argument("--max-period", type=int, default=4)
    parser.add_argument("--random-starts", type=int, default=256)
    parser.add_argument("--seed", type=int, default=20260731)
    parser.add_argument("--root-tolerance", type=float, default=1.0e-12)
    parser.add_argument("--acceptance-tolerance", type=float, default=1.0e-11)
    parser.add_argument("--cluster-tolerance", type=float, default=1.0e-8)
    parser.add_argument("--output-stem", type=str, default="periodic_orbits_smoke")
    parser.add_argument("--allow-analytic-gate-failure", action="store_true")
    return parser.parse_args()


def analytic_gate(a: float, max_period: int, records: list[OrbitRecord], tolerance: float) -> dict[str, object]:
    failures: list[str] = []
    parameter_records = [record for record in records if abs(record.a - a) <= 1.0e-14]
    if max_period >= 2:
        period2 = [record for record in parameter_records if record.period == 2]
        expected_period2 = analytic_period2(a)
        if len(period2) != len(expected_period2):
            failures.append(f"period2_count expected {len(expected_period2)} got {len(period2)}")
    if max_period >= 3:
        period3 = [record for record in parameter_records if record.period == 3]
        expected_period3 = analytic_period3(a)
        if len(period3) != len(expected_period3):
            failures.append(f"period3_count expected {len(expected_period3)} got {len(period3)}")
        for expected in expected_period3:
            if not any(cyclic_distance(expected, record.sequence) <= 10.0 * tolerance for record in period3):
                failures.append(f"period3_closed_form_missing {expected}")
        if expected_period3 and len(period3) == len(expected_period3):
            def classify_trace(trace: float) -> str:
                if abs(trace) < 2.0 - 1.0e-10:
                    return "elliptic"
                if abs(trace) > 2.0 + 1.0e-10:
                    return "hyperbolic"
                return "parabolic"

            expected_stability = Counter(
                classify_trace(trace) for trace in analytic_period3_traces(a)
            )
            observed_stability = Counter(record.stability for record in period3)
            if observed_stability != expected_stability:
                failures.append(
                    "period3_stability expected "
                    f"{dict(expected_stability)} got {dict(observed_stability)}"
                )
    return {"a": a, "passed": not failures, "failures": failures}


def csv_row(record: OrbitRecord) -> dict[str, object]:
    return {
        "orbit_id": record.orbit_id,
        "a": record.a,
        "period": record.period,
        "sequence": ";".join(f"{value:.17g}" for value in record.sequence),
        "scaled_residual_inf": record.scaled_residual_inf,
        "residual_inf": record.residual_inf,
        "root_diagnostic_passed": record.root_diagnostic.passed,
        "root_diagnostic_alpha": record.root_diagnostic.alpha,
        "root_diagnostic_radius": record.root_diagnostic.radius,
        "trace": record.trace,
        "determinant": record.determinant,
        "determinant_error": record.determinant_error,
        "greene_residue": record.greene_residue,
        "stability": record.stability,
        "multiplier_large_real": record.multiplier_large.real,
        "multiplier_large_imag": record.multiplier_large.imag,
        "multiplier_small_real": record.multiplier_small.real,
        "multiplier_small_imag": record.multiplier_small.imag,
        "multiplier_product_error": record.multiplier_product_error,
        "phase_trace_spread": record.phase_trace_spread,
        "action": record.action,
        "reversor_partner_id": record.reversor_partner_id or "",
        "reversor_partner_found": record.reversor_partner_found,
        "self_reversing": record.self_reversing,
    }


def main() -> None:
    args = parse_args()
    all_records: list[OrbitRecord] = []
    stats_payload: list[dict[str, object]] = []
    for index, a_value in enumerate(args.a):
        records, stats = search_periods(
            a=a_value,
            max_period=args.max_period,
            random_starts=args.random_starts,
            seed=args.seed + 100_003 * index,
            root_tolerance=args.root_tolerance,
            acceptance_tolerance=args.acceptance_tolerance,
            cluster_tolerance=args.cluster_tolerance,
        )
        all_records.extend(records)
        stats_payload.extend(asdict(item) for item in stats)

    gates = [analytic_gate(a_value, args.max_period, all_records, args.cluster_tolerance) for a_value in args.a]
    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    output_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": "R010_orbit_smoke",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "method": "real multistart Newton smoke search; not a completeness proof",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "parameters": vars(args) | {"output_stem": args.output_stem},
        "analytic_gates": gates,
        "search_stats": stats_payload,
        "orbits": [record.to_dict() for record in all_records],
    }
    payload["parameters"].pop("allow_analytic_gate_failure", None)
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")

    rows = [csv_row(record) for record in all_records]
    if rows:
        with output_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    else:
        output_csv.write_text("orbit_id,a,period\n", encoding="utf-8")

    summary = {
        "json": str(output_json),
        "csv": str(output_csv),
        "orbit_count": len(all_records),
        "analytic_gates_passed": all(gate["passed"] for gate in gates),
    }
    print(json.dumps(summary, indent=2))
    if not summary["analytic_gates_passed"] and not args.allow_analytic_gate_failure:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
