#!/usr/bin/env python3
"""Audit float64 full-cell interval-image enclosures for the Hénon map."""

from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]

BOXES = {
    "minus": 0.6176252185107651,
    "main": 0.6380064794363034,
    "plus": 0.6683877403618416,
}
UNIFORM_GRIDS = (64, 96, 128, 160)
SHIFTED_MAIN = ((128, -0.25), (128, 0.25), (160, -0.25), (160, 0.25))
A_VALUE = 6.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="interval_cover_r050")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def edge_vector(radius: float, grid: int, offset: float) -> np.ndarray:
    if not -0.5 <= offset <= 0.5:
        raise ValueError("offset must lie in [-0.5, 0.5]")
    width = 2.0 * radius / grid
    interior = -radius + (np.arange(1, grid, dtype=float) + offset) * width
    edges = np.concatenate((np.asarray([-radius]), interior, np.asarray([radius])))
    if np.any(np.diff(edges) <= 0.0):
        raise ValueError("non-increasing cell edges")
    return edges


def abs_extrema(lower: float, upper: float) -> tuple[float, float]:
    maximum = max(abs(lower), abs(upper))
    minimum = 0.0 if lower <= 0.0 <= upper else min(abs(lower), abs(upper))
    return minimum, maximum


def cell_index_range(edges: np.ndarray, lower: float, upper: float) -> tuple[int, int, bool]:
    if upper <= lower:
        return 0, -1, False
    first = max(0, int(np.searchsorted(edges, lower, side="right") - 1))
    last = min(
        len(edges) - 2,
        int(np.searchsorted(edges, np.nextafter(upper, -math.inf), side="right") - 1),
    )
    return first, last, first <= last


def summarize_configuration(box: str, radius: float, grid: int, offset: float) -> dict[str, object]:
    edges = edge_vector(radius, grid, offset)
    widths = np.diff(edges)
    forward_ratios: list[float] = []
    backward_ratios: list[float] = []
    forward_targets: list[int] = []
    backward_targets: list[int] = []
    forward_inside = 0
    backward_inside = 0
    two_sided_inside = 0
    max_outward = 0.0
    nonempty_forward = 0
    nonempty_backward = 0
    total = grid * grid

    for iy in range(grid):
        yl = float(edges[iy])
        yu = float(edges[iy + 1])
        for ix in range(grid):
            xl = float(edges[ix])
            xu = float(edges[ix + 1])
            source_area = (xu - xl) * (yu - yl)
            xmin_abs, xmax_abs = abs_extrema(xl, xu)
            ymin_abs, ymax_abs = abs_extrema(yl, yu)

            # H(x,y) = (1-a*x^2-y, x).
            fx0 = 1.0 - A_VALUE * xmax_abs**2 - yu
            fx1 = 1.0 - A_VALUE * xmin_abs**2 - yl
            fy0, fy1 = xl, xu
            # H^{-1}(X,Y) = (Y, 1-a*Y^2-X).
            bx0, bx1 = yl, yu
            by0 = 1.0 - A_VALUE * ymax_abs**2 - xu
            by1 = 1.0 - A_VALUE * ymin_abs**2 - xl

            f_area = max(0.0, fx1 - fx0) * max(0.0, fy1 - fy0)
            b_area = max(0.0, bx1 - bx0) * max(0.0, by1 - by0)
            forward_ratios.append(f_area / source_area)
            backward_ratios.append(b_area / source_area)

            f_first_x, f_last_x, f_nonempty_x = cell_index_range(edges, fx0, fx1)
            f_first_y, f_last_y, f_nonempty_y = cell_index_range(edges, fy0, fy1)
            b_first_x, b_last_x, b_nonempty_x = cell_index_range(edges, bx0, bx1)
            b_first_y, b_last_y, b_nonempty_y = cell_index_range(edges, by0, by1)
            f_count = (
                (f_last_x - f_first_x + 1) * (f_last_y - f_first_y + 1)
                if f_nonempty_x and f_nonempty_y
                else 0
            )
            b_count = (
                (b_last_x - b_first_x + 1) * (b_last_y - b_first_y + 1)
                if b_nonempty_x and b_nonempty_y
                else 0
            )
            forward_targets.append(f_count)
            backward_targets.append(b_count)
            if f_count > 0:
                nonempty_forward += 1
            if b_count > 0:
                nonempty_backward += 1

            f_inside = fx0 >= -radius and fx1 <= radius and fy0 >= -radius and fy1 <= radius
            b_inside = bx0 >= -radius and bx1 <= radius and by0 >= -radius and by1 <= radius
            if f_inside:
                forward_inside += 1
            if b_inside:
                backward_inside += 1
            if f_inside and b_inside:
                two_sided_inside += 1
            max_outward = max(
                max_outward,
                max(0.0, -radius - fx0, fx1 - radius, -radius - fy0, fy1 - radius),
                max(0.0, -radius - bx0, bx1 - radius, -radius - by0, by1 - radius),
            )

    def quantiles(values: list[float]) -> tuple[float, float, float]:
        array = np.asarray(values, dtype=float)
        return (
            float(np.median(array)),
            float(np.quantile(array, 0.95)),
            float(np.max(array)),
        )

    f_ratio = quantiles(forward_ratios)
    b_ratio = quantiles(backward_ratios)
    f_targets = quantiles([float(x) for x in forward_targets])
    b_targets = quantiles([float(x) for x in backward_targets])
    return {
        "box": box,
        "radius": radius,
        "grid": grid,
        "grid_offset": offset,
        "state_count": total,
        "minimum_cell_width": float(np.min(widths)),
        "maximum_cell_width": float(np.max(widths)),
        "forward_in_box_fraction": forward_inside / total,
        "backward_in_box_fraction": backward_inside / total,
        "two_sided_in_box_fraction": two_sided_inside / total,
        "forward_nonempty_target_fraction": nonempty_forward / total,
        "backward_nonempty_target_fraction": nonempty_backward / total,
        "forward_enclosure_area_ratio_median": f_ratio[0],
        "forward_enclosure_area_ratio_p95": f_ratio[1],
        "forward_enclosure_area_ratio_max": f_ratio[2],
        "backward_enclosure_area_ratio_median": b_ratio[0],
        "backward_enclosure_area_ratio_p95": b_ratio[1],
        "backward_enclosure_area_ratio_max": b_ratio[2],
        "forward_target_count_median": f_targets[0],
        "forward_target_count_p95": f_targets[1],
        "forward_target_count_max": f_targets[2],
        "backward_target_count_median": b_targets[0],
        "backward_target_count_p95": b_targets[1],
        "backward_target_count_max": b_targets[2],
        "maximum_outward_excursion": max_outward,
        "float64_diagnostic_only": True,
    }


def main() -> None:
    args = parse_args()
    records: list[dict[str, object]] = []
    for box, radius in BOXES.items():
        for grid in UNIFORM_GRIDS:
            records.append(summarize_configuration(box, radius, grid, 0.0))
    for grid, offset in SHIFTED_MAIN:
        records.append(summarize_configuration("main", BOXES["main"], grid, offset))
    payload = {
        "run_id": "R050COV_interval_cover",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "a": A_VALUE,
        "records": records,
        "scope": (
            "float64 full-cell interval-image enclosure diagnostic; no outward "
            "rounding and no invariant-set or convergence certificate"
        ),
    }
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    flat = [{k: v for k, v in row.items()} for row in records]
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat[0]))
        writer.writeheader()
        writer.writerows(flat)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "configurations": len(records)}, indent=2))


if __name__ == "__main__":
    main()
