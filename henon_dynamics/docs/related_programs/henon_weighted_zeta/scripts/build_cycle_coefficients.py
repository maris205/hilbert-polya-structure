#!/usr/bin/env python3
"""Build finite weighted zeta and determinant coefficients from an orbit catalog."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.geometry import fixed_points, sequence_points
from henon_zeta.orbits import (
    FloatingPointKantorovichDiagnostic,
    OrbitRecord,
    cyclic_distance,
    primitive_period,
)
from henon_zeta.zeta import (
    determinant_coefficients,
    euler_log_derivative_coefficients,
    factor_poles,
    log_zeta_coefficients,
    zeta_coefficients,
)


def complex_value(value: list[float]) -> complex:
    return complex(float(value[0]), float(value[1]))


def load_orbits(path: Path) -> tuple[dict[str, object], list[OrbitRecord]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = []
    orbit_rows = payload.get("orbits", payload.get("real_primitive_orbits"))
    if orbit_rows is None:
        raise KeyError("input must contain 'orbits' or 'real_primitive_orbits'")
    for row in orbit_rows:
        diagnostic_payload = row.get("root_diagnostic", row.get("certificate"))
        if diagnostic_payload is None:
            raise KeyError(f"orbit {row.get('orbit_id')} lacks a root diagnostic")
        root_diagnostic = FloatingPointKantorovichDiagnostic(**diagnostic_payload)
        independent_payload = row.get(
            "independent_eigenvalues",
            [row["multiplier_large"], row["multiplier_small"]],
        )
        records.append(
            OrbitRecord(
                orbit_id=row["orbit_id"],
                a=float(row["a"]),
                period=int(row["period"]),
                sequence=tuple(float(value) for value in row["sequence"]),
                scaled_residual_inf=float(row["scaled_residual_inf"]),
                residual_inf=float(row["residual_inf"]),
                solver_success=bool(row["solver_success"]),
                root_diagnostic=root_diagnostic,
                trace=float(row["trace"]),
                determinant=float(row["determinant"]),
                determinant_error=float(row["determinant_error"]),
                greene_residue=float(row["greene_residue"]),
                stability=row["stability"],
                multiplier_large=complex_value(row["multiplier_large"]),
                multiplier_small=complex_value(row["multiplier_small"]),
                independent_eigenvalues=(
                    complex_value(independent_payload[0]),
                    complex_value(independent_payload[1]),
                ),
                multiplier_product_error=float(row["multiplier_product_error"]),
                phase_trace_spread=float(row["phase_trace_spread"]),
                action=float(row["action"]),
                reversor_partner_id=row.get("reversor_partner_id"),
                reversor_partner_found=bool(row.get("reversor_partner_found", False)),
                self_reversing=bool(row.get("self_reversing", False)),
            )
        )
    return payload, records


def serialize_complex(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def validate_catalog(records: list[OrbitRecord], tolerance: float = 1.0e-8) -> None:
    for record in records:
        if not record.root_diagnostic.passed:
            raise ValueError(f"orbit {record.orbit_id} failed its floating-point root diagnostic")
        if primitive_period(record.sequence, tolerance=tolerance) != record.period:
            raise ValueError(f"orbit {record.orbit_id} is not primitive at its recorded period")
    for index, record in enumerate(records):
        for candidate in records[index + 1 :]:
            if record.a != candidate.a or record.period != candidate.period:
                continue
            if cyclic_distance(record.sequence, candidate.sequence) <= tolerance:
                raise ValueError(f"duplicate orbit records: {record.orbit_id}, {candidate.orbit_id}")


def in_requested_domain(
    record: OrbitRecord,
    radius: float | None,
    hole_radius: float,
) -> bool:
    points = sequence_points(record.sequence)
    if radius is not None and np.any(np.abs(points) >= radius):
        return False
    if hole_radius > 0.0:
        elliptic = fixed_points(record.a)[0].coordinate
        center = np.array([elliptic, elliptic])
        if np.any(np.sum((points - center) ** 2, axis=1) < hole_radius**2):
            return False
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "periodic_orbits_baseline.json",
    )
    parser.add_argument("--beta", nargs="+", type=float, default=[0.0, 0.5, 1.0])
    parser.add_argument("--max-degree", type=int)
    parser.add_argument("--allow-untrusted-degree", action="store_true")
    parser.add_argument("--radius", type=float)
    parser.add_argument("--hole-radius", type=float, default=0.0)
    parser.add_argument("--output-stem", type=str, default="cycle_coefficients")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source, records = load_orbits(args.input)
    validate_catalog(records)
    catalog_max_period = max(record.period for record in records)
    max_degree = catalog_max_period if args.max_degree is None else args.max_degree
    if max_degree > catalog_max_period and not args.allow_untrusted_degree:
        raise SystemExit(
            f"requested degree {max_degree} exceeds catalog period {catalog_max_period}; "
            "pass --allow-untrusted-degree only for formal algebra diagnostics"
        )
    trusted_degree = min(max_degree, catalog_max_period)
    parameter_values = sorted({record.a for record in records})
    rows: list[dict[str, object]] = []
    blocks: list[dict[str, object]] = []
    for a_value in parameter_values:
        selected = [
            record
            for record in records
            if record.a == a_value
            and record.stability == "hyperbolic"
            and in_requested_domain(record, args.radius, args.hole_radius)
        ]
        for beta in args.beta:
            determinant = determinant_coefficients(selected, max_degree, beta)
            zeta = zeta_coefficients(selected, max_degree, beta)
            log_zeta = log_zeta_coefficients(selected, max_degree, beta)
            log_derivative = euler_log_derivative_coefficients(selected, max_degree, beta)
            for degree in range(max_degree + 1):
                rows.append(
                    {
                        "a": a_value,
                        "beta": beta,
                        "degree": degree,
                        "determinant_real": determinant[degree].real,
                        "determinant_imag": determinant[degree].imag,
                        "zeta_real": zeta[degree].real,
                        "zeta_imag": zeta[degree].imag,
                        "log_zeta_real": log_zeta[degree].real,
                        "log_zeta_imag": log_zeta[degree].imag,
                        "euler_log_derivative_real": log_derivative[degree].real,
                        "euler_log_derivative_imag": log_derivative[degree].imag,
                        "trusted_degree": degree <= trusted_degree,
                    }
                )
            poles = [
                {"orbit_id": record.orbit_id, "values": [serialize_complex(value) for value in factor_poles(record, beta)]}
                for record in selected
            ]
            blocks.append(
                {
                    "a": a_value,
                    "beta": beta,
                    "hyperbolic_orbit_count": len(selected),
                    "determinant_coefficients": [serialize_complex(value) for value in determinant],
                    "zeta_coefficients": [serialize_complex(value) for value in zeta],
                    "log_zeta_coefficients": [serialize_complex(value) for value in log_zeta],
                    "euler_log_derivative_coefficients": [
                        serialize_complex(value) for value in log_derivative
                    ],
                    "finite_factor_poles": poles,
                }
            )

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": "R030_cycle_coefficients",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source": str(args.input),
        "source_run_id": source.get("run_id"),
        "scope": "finite Euler product over numerically refined, diagnostic-passing hyperbolic real orbits; not an interval-certified complete zeta",
        "catalog_max_period": catalog_max_period,
        "series_degree": max_degree,
        "trusted_degree": trusted_degree,
        "radius": args.radius,
        "hole_radius": args.hole_radius,
        "blocks": blocks,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "blocks": len(blocks)}, indent=2))


if __name__ == "__main__":
    main()
