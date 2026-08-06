#!/usr/bin/env python3
"""Analyze the pre-frozen R049-HO shifted-origin hold-out audit."""

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

REFERENCE = 0.5261711898
BOXES = {
    "minus": 0.6176252185107651,
    "main": 0.6380064794363034,
    "plus": 0.6683877403618416,
}
DEV_GRIDS = (300, 380, 460)
HOLDOUT_GRIDS = (340, 420)
DEV_OFFSETS = (-0.375, -0.125, 0.125, 0.375)
HOLDOUT_OFFSETS = (-0.3125, 0.1875, 0.4375)
CENTER_OFFSET = 0.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument(
        "--output-stem", default="shifted_holdout_analysis_r049ho"
    )
    return parser.parse_args()


def load_records(results_dir: Path, phase: str, box: str) -> list[dict[str, object]]:
    path = results_dir / f"shifted_holdout_{phase}_a6_{box}.json"
    if not path.exists():
        raise FileNotFoundError(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("run_id") != "R049H_shifted_holdout":
        raise ValueError(f"unexpected run_id in {path}: {payload.get('run_id')}")
    return list(payload["records"])


def analyze_phase(
    records: list[dict[str, object]],
    grids: tuple[int, ...],
    nonzero_offsets: tuple[float, ...],
    box: str,
    phase: str,
    r048_high_range: float,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    summaries: list[dict[str, object]] = []
    raw_rows: list[dict[str, object]] = []
    for grid in grids:
        selected = sorted(
            [r for r in records if int(r["grid"]) == grid],
            key=lambda r: float(r["grid_offset"]),
        )
        observed = {float(r["grid_offset"]) for r in selected}
        expected = set(nonzero_offsets) | {CENTER_OFFSET}
        if observed != expected:
            raise ValueError(
                f"offset mismatch for {phase}/{box}/N={grid}: "
                f"observed={sorted(observed)}, expected={sorted(expected)}"
            )
        by_offset = {float(r["grid_offset"]): r for r in selected}
        values = np.asarray(
            [float(by_offset[offset]["leading_modulus"]) for offset in nonzero_offsets]
        )
        centered = float(by_offset[CENTER_OFFSET]["leading_modulus"])
        offset_mean = float(np.mean(values))
        offset_std = float(np.std(values, ddof=1))
        offset_range = float(np.ptp(values))
        max_reversibility = max(
            float(r["weighted_reversibility_error"]) for r in selected
        )
        all_checks = all(
            bool(r["linear_solver_passed"])
            and bool(r["nontrivial_operator_pass"])
            and float(r["weighted_reversibility_error"]) < 1.0e-11
            for r in selected
        )
        summaries.append(
            {
                "phase": phase,
                "box": box,
                "radius": BOXES[box],
                "grid": grid,
                "nonzero_offsets": list(nonzero_offsets),
                "offset_mean": offset_mean,
                "offset_std_sample": offset_std,
                "offset_range": offset_range,
                "offset_mean_relative_gap": abs(offset_mean - REFERENCE) / REFERENCE,
                "centered_value": centered,
                "centered_relative_gap": abs(centered - REFERENCE) / REFERENCE,
                "offset_mean_centered": abs(offset_mean - REFERENCE)
                < abs(centered - REFERENCE),
                "r048_high_band_range": r048_high_range,
                "range_to_r048_high_band_range": offset_range / r048_high_range,
                "boundary_phase_material": offset_range >= 0.5 * r048_high_range,
                "maximum_weighted_reversibility_error": max_reversibility,
                "finite_checks_pass": all_checks,
            }
        )
        for record in selected:
            raw_rows.append(
                {
                    "phase": phase,
                    "box": box,
                    "radius": BOXES[box],
                    "grid": grid,
                    "grid_offset": record["grid_offset"],
                    "leading_modulus": record["leading_modulus"],
                    "relative_gap": abs(float(record["leading_modulus"]) - REFERENCE)
                    / REFERENCE,
                    "weighted_reversibility_error": record[
                        "weighted_reversibility_error"
                    ],
                    "linear_solver_passed": record["linear_solver_passed"],
                }
            )
    return summaries, raw_rows


def main() -> None:
    args = parse_args()
    r048 = json.loads(
        (args.results_dir / "grid_phase_audit_r048.json").read_text(encoding="utf-8")
    )
    high_ranges = {
        summary["box"]: summary["bands"]["high"]["range"]
        for summary in r048["series_summaries"]
        if summary["method"] == "semi_analytic_overlap"
    }
    summaries: list[dict[str, object]] = []
    rows: list[dict[str, object]] = []
    for box in BOXES:
        dev_records = load_records(args.results_dir, "dev", box)
        hold_records = load_records(args.results_dir, "test", box)
        phase_summaries, phase_rows = analyze_phase(
            dev_records,
            DEV_GRIDS,
            DEV_OFFSETS,
            box,
            "dev",
            high_ranges[box],
        )
        summaries.extend(phase_summaries)
        rows.extend(phase_rows)
        phase_summaries, phase_rows = analyze_phase(
            hold_records,
            HOLDOUT_GRIDS,
            HOLDOUT_OFFSETS,
            box,
            "holdout",
            high_ranges[box],
        )
        summaries.extend(phase_summaries)
        rows.extend(phase_rows)

    holdout = [s for s in summaries if s["phase"] == "holdout"]
    dev = [s for s in summaries if s["phase"] == "dev"]
    h1 = bool(all(bool(s["offset_mean_centered"]) for s in holdout))
    h2_by_grid: dict[int, bool] = {}
    for grid in HOLDOUT_GRIDS:
        group = [s for s in holdout if int(s["grid"]) == grid]
        h2_by_grid[grid] = bool(
            np.mean([s["offset_mean_relative_gap"] for s in group])
            < np.mean([s["centered_relative_gap"] for s in group])
        )
    h2 = bool(all(h2_by_grid.values()))
    h3 = bool(all(bool(s["boundary_phase_material"]) for s in holdout))
    decisions = {
        "H1_holdout_mean_centered_all_six": h1,
        "H2_holdout_aggregate_centered_both_grids": h2,
        "H2_by_grid": {str(k): v for k, v in h2_by_grid.items()},
        "H3_holdout_boundary_phase_material_all_six": h3,
        "finite_checks_all": bool(all(bool(s["finite_checks_pass"]) for s in summaries)),
        "development_mean_centered_all": bool(
            all(bool(s["offset_mean_centered"]) for s in dev)
        ),
    }
    payload = {
        "run_id": "R049H_shifted_holdout_analysis",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "reference": REFERENCE,
        "development_grids": list(DEV_GRIDS),
        "holdout_grids": list(HOLDOUT_GRIDS),
        "development_offsets": list(DEV_OFFSETS),
        "holdout_offsets": list(HOLDOUT_OFFSETS),
        "summaries": summaries,
        "decisions": decisions,
        "rows": rows,
        "scope": (
            "pre-frozen hold-out replication of finite-resolution boundary-phase "
            "sensitivity; no continuous-operator convergence claim"
        ),
    }
    output_json = args.results_dir / f"{args.output_stem}.json"
    output_csv = args.results_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "decisions": decisions}, indent=2))


if __name__ == "__main__":
    main()
