#!/usr/bin/env python3
"""Analyze the R049 clipped-boundary shifted-origin overlap sweep."""

from __future__ import annotations

import argparse
import csv
import json
import math
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
OFFSETS = (-0.5, -0.25, 0.0, 0.25, 0.5)
GRIDS = (256, 512)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--output-stem", default="shifted_overlap_a6_analysis_r049")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records_by_box: dict[str, list[dict[str, object]]] = {}
    for box in BOXES:
        path = args.results_dir / f"shifted_overlap_a6_{box}.json"
        if not path.exists():
            raise FileNotFoundError(path)
        records_by_box[box] = list(
            json.loads(path.read_text(encoding="utf-8"))["records"]
        )
    r048 = json.loads(
        (args.results_dir / "grid_phase_audit_r048.json").read_text(
            encoding="utf-8"
        )
    )
    high_ranges = {
        summary["box"]: summary["bands"]["high"]["range"]
        for summary in r048["series_summaries"]
        if summary["method"] == "semi_analytic_overlap"
    }

    raw_rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    material_checks: dict[str, list[bool]] = {}
    centered_checks: dict[str, list[bool]] = {}
    reversibility_checks: dict[str, list[bool]] = {}
    for box, records in records_by_box.items():
        for grid in GRIDS:
            selected = sorted(
                [record for record in records if int(record["grid"]) == grid],
                key=lambda record: float(record["grid_offset"]),
            )
            if [float(record["grid_offset"]) for record in selected] != list(OFFSETS):
                raise ValueError(f"offset set mismatch for {box}, N={grid}")
            values = np.asarray(
                [float(record["leading_modulus"]) for record in selected]
            )
            mean = float(np.mean(values))
            std = float(np.std(values, ddof=1))
            value_range = float(np.ptp(values))
            unshifted = float(values[2])
            material = value_range >= 0.5 * high_ranges[box]
            centered = abs(mean - REFERENCE) < abs(unshifted - REFERENCE)
            max_reversibility = max(
                float(record["weighted_reversibility_error"])
                for record in selected
            )
            reversible = max_reversibility < 1.0e-11
            material_checks.setdefault(box, []).append(material)
            centered_checks.setdefault(box, []).append(centered)
            reversibility_checks.setdefault(box, []).append(reversible)
            summaries.append(
                {
                    "box": box,
                    "radius": BOXES[box],
                    "grid": grid,
                    "offset_mean": mean,
                    "offset_std": std,
                    "offset_range": value_range,
                    "offset_range_relative_to_reference": value_range / REFERENCE,
                    "offset_mean_relative_gap": abs(mean - REFERENCE) / REFERENCE,
                    "unshifted_value": unshifted,
                    "unshifted_relative_gap": abs(unshifted - REFERENCE) / REFERENCE,
                    "r048_high_band_range": high_ranges[box],
                    "range_to_r048_high_band_range": (
                        value_range / high_ranges[box]
                    ),
                    "boundary_phase_material": material,
                    "offset_mean_centered": centered,
                    "maximum_weighted_reversibility_error": max_reversibility,
                    "weighted_reversibility_pass": reversible,
                }
            )
            for record in selected:
                raw_rows.append(
                    {
                        "box": box,
                        "radius": BOXES[box],
                        "grid": grid,
                        "grid_offset": record["grid_offset"],
                        "leading_modulus": record["leading_modulus"],
                        "relative_gap": abs(
                            float(record["leading_modulus"]) - REFERENCE
                        )
                        / REFERENCE,
                        "weighted_reversibility_error": record[
                            "weighted_reversibility_error"
                        ],
                        "minimum_cell_width": record["minimum_cell_width"],
                        "maximum_cell_width": record["maximum_cell_width"],
                    }
                )

    decisions = {
        "boundary_phase_material_all_boxes": bool(
            all(all(values) for values in material_checks.values())
        ),
        "offset_mean_centered_all_boxes": bool(
            all(all(values) for values in centered_checks.values())
        ),
        "weighted_reversibility_all_pass": bool(
            all(all(values) for values in reversibility_checks.values())
        ),
        "boundary_phase_material_by_box": material_checks,
        "offset_mean_centered_by_box": centered_checks,
        "weighted_reversibility_by_box": reversibility_checks,
    }
    payload = {
        "run_id": "R049_shifted_overlap_analysis",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "reference": REFERENCE,
        "offsets": list(OFFSETS),
        "grids": list(GRIDS),
        "summaries": summaries,
        "decisions": decisions,
        "rows": raw_rows,
        "scope": (
            "finite-resolution clipped-boundary phase diagnostic; "
            "offset means do not establish operator convergence"
        ),
    }
    output_json = args.results_dir / f"{args.output_stem}.json"
    output_csv = args.results_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(raw_rows[0]))
        writer.writeheader()
        writer.writerows(raw_rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "decisions": decisions,
                "summaries": summaries,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
