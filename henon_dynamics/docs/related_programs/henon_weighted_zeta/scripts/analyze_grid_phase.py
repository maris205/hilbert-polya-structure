#!/usr/bin/env python3
"""Summarize the preregistered R048 grid-phase audit."""

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


FREDHOLM_REFERENCE = 0.5261711898
RADII = {
    "minus": 0.6176252185107651,
    "main": 0.6380064794363034,
    "plus": 0.6683877403618416,
}
EXPECTED_GRIDS = tuple(range(160, 513, 16))
BANDS = {
    "low": tuple(range(160, 257, 16)),
    "middle": tuple(range(272, 385, 16)),
    "high": tuple(range(400, 513, 16)),
}


def fixed_point_phase_model(
    values_by_grid: dict[int, float],
    radius: float,
) -> dict[str, float]:
    """Fit a post-hoc one-harmonic model from the two fixed-point grid phases."""

    grids = np.asarray(EXPECTED_GRIDS, dtype=float)
    values = np.asarray([values_by_grid[int(grid)] for grid in grids], dtype=float)
    negative = -(1.0 + math.sqrt(7.0)) / 6.0
    positive = (-1.0 + math.sqrt(7.0)) / 6.0
    phases = [
        grids * (negative + radius) / (2.0 * radius),
        grids * (positive + radius) / (2.0 * radius),
    ]
    design = np.column_stack(
        [np.ones(grids.size)]
        + [
            function(2.0 * np.pi * phase)
            for phase in phases
            for function in (np.cos, np.sin)
        ]
    )
    coefficients = np.linalg.lstsq(design, values, rcond=None)[0]
    fitted = design @ coefficients
    centered_sum_squares = float(np.sum((values - np.mean(values)) ** 2))
    residual_sum_squares = float(np.sum((values - fitted) ** 2))
    full_r_squared = (
        float("nan")
        if centered_sum_squares == 0.0
        else 1.0 - residual_sum_squares / centered_sum_squares
    )
    training = np.arange(15)
    high_band = np.arange(15, len(EXPECTED_GRIDS))
    training_coefficients = np.linalg.lstsq(
        design[training], values[training], rcond=None
    )[0]
    high_prediction = design[high_band] @ training_coefficients
    high_rmse = float(
        np.sqrt(np.mean((values[high_band] - high_prediction) ** 2))
    )
    baseline = float(np.mean(values[training]))
    baseline_rmse = float(
        np.sqrt(np.mean((values[high_band] - baseline) ** 2))
    )
    return {
        "scope": "post-hoc E0; not a preregistered decision criterion",
        "full_sample_r_squared": full_r_squared,
        "high_band_prediction_rmse": high_rmse,
        "high_band_training_mean_baseline_rmse": baseline_rmse,
        "prediction_to_baseline_rmse_ratio": high_rmse / baseline_rmse,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--output-stem", default="grid_phase_audit_r048")
    return parser.parse_args()


def load_payload(path: Path) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return list(payload["records"])


def select_record(
    records: list[dict[str, object]],
    radius: float,
    grid: int,
    method: str,
) -> dict[str, object] | None:
    matches = [
        record
        for record in records
        if abs(float(record["radius"]) - radius) <= 1.0e-12
        and int(record["grid"]) == grid
        and str(record["method"]) == method
    ]
    if not matches:
        return None
    if len(matches) != 1:
        raise ValueError(
            f"expected one record for radius={radius}, grid={grid}, method={method}"
        )
    return matches[0]


def band_summary(values: np.ndarray, reference: float) -> dict[str, float]:
    median = float(np.median(values))
    mad = float(np.median(np.abs(values - median)))
    value_range = float(np.max(values) - np.min(values))
    relative_gaps = np.abs(values - reference) / reference
    return {
        "median": median,
        "mad": mad,
        "minimum": float(np.min(values)),
        "maximum": float(np.max(values)),
        "range": value_range,
        "range_relative_to_reference": value_range / reference,
        "median_relative_gap": float(np.median(relative_gaps)),
        "rms_relative_gap": float(np.sqrt(np.mean(relative_gaps**2))),
    }


def collect_series(results_dir: Path) -> tuple[
    dict[tuple[str, str], dict[int, dict[str, object]]],
    list[dict[str, object]],
]:
    paths = {
        "overlap_anchor": results_dir / "open_ulam_a6_overlap_preregistered_R1.json",
        "overlap_anchor_256": (
            results_dir / "open_ulam_a6_overlap_preregistered_R1_N256.json"
        ),
        "overlap_anchor_512_main": (
            results_dir / "open_ulam_a6_overlap_mainbox_N512.json"
        ),
        "overlap_anchor_512_other": (
            results_dir / "open_ulam_a6_overlap_otherboxes_N512.json"
        ),
        "overlap_minus": results_dir / "open_ulam_a6_overlap_gridphase_minus.json",
        "overlap_main": results_dir / "open_ulam_a6_overlap_gridphase_main.json",
        "overlap_plus": results_dir / "open_ulam_a6_overlap_gridphase_plus.json",
        "gauss_anchor": results_dir / "open_ulam_a6_preregistered_boxes_q8.json",
        "gauss_anchor_256": (
            results_dir / "open_ulam_a6_gauss_q8_preregistered_N256.json"
        ),
        "gauss_anchor_512": (
            results_dir / "open_ulam_a6_gauss_q8_preregistered_N512.json"
        ),
        "gauss_main": results_dir / "open_ulam_a6_gauss_q8_gridphase_main.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R048 inputs: " + ", ".join(missing))
    payloads = {name: load_payload(path) for name, path in paths.items()}

    series: dict[tuple[str, str], dict[int, dict[str, object]]] = {}
    raw_rows: list[dict[str, object]] = []
    overlap_sources = {
        "minus": ["overlap_anchor", "overlap_anchor_256", "overlap_anchor_512_other", "overlap_minus"],
        "main": ["overlap_anchor", "overlap_anchor_256", "overlap_anchor_512_main", "overlap_main"],
        "plus": ["overlap_anchor", "overlap_anchor_256", "overlap_anchor_512_other", "overlap_plus"],
    }
    for box, source_names in overlap_sources.items():
        key = ("semi_analytic_overlap", box)
        series[key] = {}
        radius = RADII[box]
        for grid in EXPECTED_GRIDS:
            found: list[tuple[str, dict[str, object]]] = []
            for source_name in source_names:
                record = select_record(
                    payloads[source_name],
                    radius,
                    grid,
                    "semi_analytic_overlap",
                )
                if record is not None:
                    found.append((source_name, record))
            if len(found) != 1:
                raise ValueError(
                    f"expected one overlap source for box={box}, grid={grid}; "
                    f"found {[name for name, _ in found]}"
                )
            source_name, record = found[0]
            series[key][grid] = record
            leading = float(record["leading_modulus"])
            raw_rows.append(
                {
                    "method": "semi_analytic_overlap",
                    "box": box,
                    "radius": radius,
                    "grid": grid,
                    "leading_modulus": leading,
                    "relative_gap": abs(leading - FREDHOLM_REFERENCE)
                    / FREDHOLM_REFERENCE,
                    "source_file": str(paths[source_name]),
                }
            )

    gauss_sources = ["gauss_anchor", "gauss_anchor_256", "gauss_anchor_512", "gauss_main"]
    gauss_key = ("tensor_gauss_legendre", "main")
    series[gauss_key] = {}
    for grid in EXPECTED_GRIDS:
        found = []
        for source_name in gauss_sources:
            record = select_record(
                payloads[source_name],
                RADII["main"],
                grid,
                "tensor_gauss_legendre",
            )
            if record is not None:
                found.append((source_name, record))
        if len(found) != 1:
            raise ValueError(
                f"expected one Gauss source for grid={grid}; "
                f"found {[name for name, _ in found]}"
            )
        source_name, record = found[0]
        series[gauss_key][grid] = record
        leading = float(record["leading_modulus"])
        raw_rows.append(
            {
                "method": "tensor_gauss_legendre",
                "box": "main",
                "radius": RADII["main"],
                "grid": grid,
                "leading_modulus": leading,
                "relative_gap": abs(leading - FREDHOLM_REFERENCE)
                / FREDHOLM_REFERENCE,
                "source_file": str(paths[source_name]),
            }
        )
    return series, raw_rows


def summarize(
    series: dict[tuple[str, str], dict[int, dict[str, object]]]
) -> dict[str, object]:
    series_summaries: list[dict[str, object]] = []
    overlap_high_low_ratios: dict[str, float] = {}
    tight_window_checks: dict[str, bool] = {}
    for (method, box), grid_records in sorted(series.items()):
        values_by_grid = {
            grid: float(record["leading_modulus"])
            for grid, record in grid_records.items()
        }
        band_summaries: dict[str, dict[str, float]] = {}
        for band, grids in BANDS.items():
            values = np.asarray([values_by_grid[grid] for grid in grids], dtype=float)
            band_summaries[band] = band_summary(values, FREDHOLM_REFERENCE)
        high_low_ratio = (
            band_summaries["high"]["range"] / band_summaries["low"]["range"]
            if band_summaries["low"]["range"] > 0.0
            else math.inf
        )
        if method == "semi_analytic_overlap":
            overlap_high_low_ratios[box] = high_low_ratio
            high = band_summaries["high"]
            tight_window_checks[box] = (
                high["median_relative_gap"] <= 0.0025
                and high["range_relative_to_reference"] <= 0.005
            )
        series_summary: dict[str, object] = {
            "method": method,
            "box": box,
            "radius": RADII[box],
            "grid_count": len(values_by_grid),
            "bands": band_summaries,
            "high_to_low_range_ratio": high_low_ratio,
        }
        if method == "semi_analytic_overlap":
            series_summary["exploratory_fixed_point_phase_model"] = (
                fixed_point_phase_model(values_by_grid, RADII[box])
            )
        series_summaries.append(series_summary)

    overlap = np.asarray(
        [
            float(series[("semi_analytic_overlap", "main")][grid]["leading_modulus"])
            for grid in EXPECTED_GRIDS
        ]
    )
    gauss = np.asarray(
        [
            float(series[("tensor_gauss_legendre", "main")][grid]["leading_modulus"])
            for grid in EXPECTED_GRIDS
        ]
    )
    correlation = float(np.corrcoef(overlap, gauss)[0, 1])
    differences = np.abs(overlap - gauss)
    median_difference_relative = float(
        np.median(differences) / FREDHOLM_REFERENCE
    )
    cross_method = {
        "grid_count": len(EXPECTED_GRIDS),
        "pearson_correlation": correlation,
        "median_absolute_difference": float(np.median(differences)),
        "median_difference_relative_to_reference": median_difference_relative,
        "maximum_absolute_difference": float(np.max(differences)),
        "maximum_difference_relative_to_reference": float(
            np.max(differences) / FREDHOLM_REFERENCE
        ),
    }
    decisions = {
        "D1_shrinking_oscillation_band": bool(
            overlap_high_low_ratios
            and all(ratio <= 0.75 for ratio in overlap_high_low_ratios.values())
        ),
        "D1_box_high_to_low_ratios": overlap_high_low_ratios,
        "D2_tight_common_window": bool(
            tight_window_checks and all(tight_window_checks.values())
        ),
        "D2_box_checks": tight_window_checks,
        "D3_synchronized_grid_geometry": bool(
            correlation >= 0.8 and median_difference_relative <= 0.0025
        ),
    }
    return {
        "fredholm_reference": FREDHOLM_REFERENCE,
        "expected_grids": list(EXPECTED_GRIDS),
        "bands": {name: list(grids) for name, grids in BANDS.items()},
        "series_summaries": series_summaries,
        "cross_method_main_box": cross_method,
        "decisions": decisions,
    }


def main() -> None:
    args = parse_args()
    series, raw_rows = collect_series(args.results_dir)
    audit = summarize(series)
    payload = {
        "run_id": "R048_grid_phase_audit",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "preregistered intermediate-grid finite-resolution audit; "
            "anchors N=160,256,512 were known before freezing"
        ),
        **audit,
        "rows": sorted(
            raw_rows,
            key=lambda row: (str(row["method"]), str(row["box"]), int(row["grid"])),
        ),
    }
    output_json = args.results_dir / f"{args.output_stem}.json"
    output_csv = args.results_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(payload["rows"][0]))
        writer.writeheader()
        writer.writerows(payload["rows"])
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "decisions": payload["decisions"],
                "cross_method_main_box": payload["cross_method_main_box"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
