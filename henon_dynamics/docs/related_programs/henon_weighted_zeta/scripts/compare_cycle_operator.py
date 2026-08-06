#!/usr/bin/env python3
"""Compare finite cycle-polynomial resonances with independent Ulam spectra."""

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

from henon_zeta.geometry import sequence_points
from henon_zeta.operator import finite_time_survivor_mask
from henon_zeta.orbits import OrbitRecord
from henon_zeta.zeta import (
    determinant_coefficients,
    leading_resonance_from_determinant,
    perron_fredholm_coefficients,
)
from scripts.build_cycle_coefficients import load_orbits, validate_catalog


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orbits", type=Path, required=True)
    parser.add_argument("--operator", type=Path, required=True)
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--max-period", type=int, default=8)
    parser.add_argument("--output-stem", type=str, required=True)
    return parser.parse_args()


def orbit_survives_configuration(
    record: OrbitRecord,
    operator_row: dict[str, object],
    survivor_mask: np.ndarray | None = None,
) -> bool:
    if abs(record.a - float(operator_row["a"])) > 1.0e-12:
        return False
    points = sequence_points(record.sequence)
    radius = float(operator_row["radius"])
    if np.any(np.abs(points) >= radius):
        return False
    hole_radius = float(operator_row.get("hole_radius", 0.0))
    hole_center = operator_row.get("hole_center")
    if hole_radius > 0.0 and hole_center is not None:
        center = np.asarray(hole_center, dtype=float)
        if np.any(np.sum((points - center) ** 2, axis=1) < hole_radius**2):
            return False
    survivor_horizon = int(operator_row.get("survivor_horizon", 0) or 0)
    if survivor_horizon > 0:
        if survivor_mask is None:
            raise ValueError("survivor mask is required when survivor_horizon > 0")
        grid = int(operator_row["grid"])
        width = 2.0 * radius / grid
        x_index = np.floor((points[:, 0] + radius) / width).astype(int)
        y_index = np.floor((points[:, 1] + radius) / width).astype(int)
        if np.any(x_index < 0) or np.any(x_index >= grid):
            return False
        if np.any(y_index < 0) or np.any(y_index >= grid):
            return False
        cell_indices = y_index * grid + x_index
        if np.any(~survivor_mask[cell_indices]):
            return False
    return True


def main() -> None:
    args = parse_args()
    _, orbit_catalog = load_orbits(args.orbits)
    validate_catalog(orbit_catalog)
    operator_payload = json.loads(args.operator.read_text(encoding="utf-8"))
    rows = []
    for operator_row in operator_payload["records"]:
        survivor_horizon = int(operator_row.get("survivor_horizon", 0) or 0)
        survivor_mask = None
        if survivor_horizon > 0:
            hole_center_raw = operator_row.get("hole_center")
            hole_center = (
                None
                if hole_center_raw is None
                else (float(hole_center_raw[0]), float(hole_center_raw[1]))
            )
            survivor_mask = finite_time_survivor_mask(
                float(operator_row["a"]),
                float(operator_row["radius"]),
                int(operator_row["grid"]),
                survivor_horizon,
                float(operator_row.get("hole_radius", 0.0)),
                hole_center,
            )
        eligible_all = [
            record
            for record in orbit_catalog
            if orbit_survives_configuration(record, operator_row, survivor_mask)
        ]
        eligible_hyperbolic = [record for record in eligible_all if record.stability == "hyperbolic"]
        operator_valid = bool(
            operator_row.get(
                "nontrivial_operator_pass",
                int(operator_row.get("active_cells", 0) or 0) > 0
                and int(operator_row.get("matrix_nnz", 0) or 0) > 0,
            )
        )
        previous_resonance: complex | None = None
        previous_fredholm: complex | None = None
        for cutoff in range(1, args.max_period + 1):
            selected = [record for record in eligible_hyperbolic if record.period <= cutoff]
            selected_all = [record for record in eligible_all if record.period <= cutoff]
            coefficients = determinant_coefficients(selected, cutoff, args.beta)
            resonance = leading_resonance_from_determinant(coefficients)
            fredholm_coefficients = perron_fredholm_coefficients(selected_all, cutoff)
            fredholm_resonance = leading_resonance_from_determinant(fredholm_coefficients)
            operator_value = complex(*operator_row["leading_eigenvalue"])
            row = {
                "config_id": operator_row["config_id"],
                "a": operator_row["a"],
                "radius": operator_row["radius"],
                "grid": operator_row["grid"],
                "grid_offset": operator_row.get("grid_offset"),
                "nominal_cell_width": operator_row.get("nominal_cell_width"),
                "method": operator_row.get("method"),
                "hole_radius": operator_row["hole_radius"],
                "survivor_horizon": operator_row.get("survivor_horizon", 0),
                "survivor_active_cells": operator_row.get("active_cells"),
                "beta": args.beta,
                "period_cutoff": cutoff,
                "eligible_orbit_count": len(selected),
                "eligible_all_stability_orbit_count": len(selected_all),
                "operator_valid": operator_valid,
                "operator_real": operator_value.real,
                "operator_imag": operator_value.imag,
                "operator_modulus": abs(operator_value),
                "cycle_real": None if resonance is None else resonance.real,
                "cycle_imag": None if resonance is None else resonance.imag,
                "cycle_modulus": None if resonance is None else abs(resonance),
                "absolute_modulus_gap": None if resonance is None or not operator_valid else abs(abs(resonance) - abs(operator_value)),
                "relative_modulus_gap": None if resonance is None or not operator_valid else abs(abs(resonance) - abs(operator_value)) / max(abs(operator_value), 1.0e-15),
                "cycle_cutoff_change": None if resonance is None or previous_resonance is None else abs(resonance - previous_resonance),
                "highest_coefficient_modulus": float(abs(coefficients[-1])),
                "fredholm_real": None if fredholm_resonance is None else fredholm_resonance.real,
                "fredholm_imag": None if fredholm_resonance is None else fredholm_resonance.imag,
                "fredholm_modulus": None if fredholm_resonance is None else abs(fredholm_resonance),
                "fredholm_absolute_modulus_gap": None if fredholm_resonance is None or not operator_valid else abs(abs(fredholm_resonance) - abs(operator_value)),
                "fredholm_relative_modulus_gap": None if fredholm_resonance is None or not operator_valid else abs(abs(fredholm_resonance) - abs(operator_value)) / max(abs(operator_value), 1.0e-15),
                "fredholm_cutoff_change": None if fredholm_resonance is None or previous_fredholm is None else abs(fredholm_resonance - previous_fredholm),
                "fredholm_highest_coefficient_modulus": float(abs(fredholm_coefficients[-1])),
            }
            rows.append(row)
            if resonance is not None:
                previous_resonance = resonance
            if fredholm_resonance is not None:
                previous_fredholm = fredholm_resonance

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": str(args.output_stem),
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "orbits": str(args.orbits),
        "operator": str(args.operator),
        "operator_run_id": operator_payload.get("run_id"),
        "beta": args.beta,
        "survivor_horizon": max(
            int(row.get("survivor_horizon", 0) or 0) for row in operator_payload["records"]
        ),
        "scope": "finite cycle-polynomial diagnostic; agreement is assessed only across cutoff and grid refinements",
        "rows": rows,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    final_rows = [row for row in rows if row["period_cutoff"] == args.max_period]
    relative_gaps = [
        row["relative_modulus_gap"]
        for row in final_rows
        if row["relative_modulus_gap"] is not None
    ]
    fredholm_relative_gaps = [
        row["fredholm_relative_modulus_gap"]
        for row in final_rows
        if row["fredholm_relative_modulus_gap"] is not None
    ]
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "configurations": len(final_rows),
                "valid_comparisons": len(relative_gaps),
                "median_final_relative_gap": (
                    None if not relative_gaps else float(np.median(relative_gaps))
                ),
                "median_final_fredholm_relative_gap": (
                    None
                    if not fredholm_relative_gaps
                    else float(np.median(fredholm_relative_gaps))
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
