#!/usr/bin/env python3
"""Create deterministic comparison tables from the raw locked-protocol output."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def optional_float(value: str) -> float | None:
    return None if value == "" else float(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True, type=Path)
    args = parser.parse_args()
    results_dir = args.results_dir
    raw = read_csv(results_dir / "raw_observables.csv")

    cutoffs = sorted({int(row["cutoff_k"]) for row in raw})
    grid_order: list[str] = []
    for row in raw:
        if row["grid_id"] not in grid_order:
            grid_order.append(row["grid_id"])

    matrix_rows: list[dict[str, Any]] = []
    for observable in ("unsigned", "liouville"):
        for grid_id in grid_order:
            subset = [
                row
                for row in raw
                if row["observable"] == observable
                and row["seed"] == "none"
                and row["grid_id"] == grid_id
            ]
            by_k = {int(row["cutoff_k"]): row for row in subset}
            first = by_k[cutoffs[0]]
            item: dict[str, Any] = {
                "observable": observable,
                "grid_id": grid_id,
                "sigma": first["sigma"],
                "tau": first["tau"],
                "target_status": first["target_status"],
            }
            for k in cutoffs:
                item[f"error_k{k}"] = optional_float(by_k[k]["target_abs_error"])
                item[f"value_abs_k{k}"] = float(by_k[k]["abs_value"])
                item[f"drift_to_k{k}"] = optional_float(by_k[k]["successive_k_drift"])
            matrix_rows.append(item)
    matrix_fields = list(matrix_rows[0].keys())
    write_csv(results_dir / "analytic_error_drift_matrix.csv", matrix_rows, matrix_fields)

    final_k = cutoffs[-1]
    final_controls = [
        row
        for row in raw
        if int(row["cutoff_k"]) == final_k
        and row["observable"] in ("mobius", "symbolic_parity", "random_state_sign")
    ]
    control_groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in final_controls:
        control_groups[(row["observable"], row["grid_id"])].append(row)

    control_rows: list[dict[str, Any]] = []
    for (observable, grid_id), group in sorted(control_groups.items()):
        magnitudes = np.array([float(row["abs_value"]) for row in group])
        drifts = np.array([float(row["successive_k_drift"]) for row in group])
        control_rows.append(
            {
                "cutoff_k": final_k,
                "observable": observable,
                "grid_id": grid_id,
                "sigma": group[0]["sigma"],
                "tau": group[0]["tau"],
                "seed_count": len(group),
                "seeds": ";".join(row["seed"] for row in group),
                "abs_value_mean": float(np.mean(magnitudes)),
                "abs_value_std_population": float(np.std(magnitudes)),
                "successive_drift_mean": float(np.mean(drifts)),
                "successive_drift_std_population": float(np.std(drifts)),
                "successive_drift_min": float(np.min(drifts)),
                "successive_drift_max": float(np.max(drifts)),
            }
        )
    control_fields = list(control_rows[0].keys())
    write_csv(results_dir / "control_final_summary.csv", control_rows, control_fields)

    precision = read_csv(results_dir / "precision_audit.csv")
    precision_summary: dict[str, dict[str, float | int]] = {}
    for method in sorted({row["method"] for row in precision}):
        differences = np.array(
            [
                float(row["abs_diff_vs_mpmath_100"])
                for row in precision
                if row["method"] == method
            ]
        )
        precision_summary[method] = {
            "row_count": int(differences.size),
            "max_abs_diff_vs_mpmath_100": float(np.max(differences)),
            "median_abs_diff_vs_mpmath_100": float(np.median(differences)),
        }
    (results_dir / "analysis_summary.json").write_text(
        json.dumps(
            {
                "cutoffs_k": cutoffs,
                "grid_point_count": len(grid_order),
                "analytic_error_drift_rows": len(matrix_rows),
                "control_summary_rows": len(control_rows),
                "precision": precision_summary,
                "data_completeness": {
                    "raw_expected_rows": len(cutoffs) * len(grid_order) * 7,
                    "raw_actual_rows": len(raw),
                    "random_expected_rows": len(cutoffs) * len(grid_order) * 3,
                    "random_actual_rows": sum(
                        row["observable"] == "random_state_sign" for row in raw
                    ),
                },
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
