#!/usr/bin/env python3
"""Audit subdivided quadratic-strip enclosures for the reversible Hénon map."""

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

from scripts.audit_interval_cover import (
    A_VALUE,
    BOXES,
    SHIFTED_MAIN,
    UNIFORM_GRIDS,
    abs_extrema,
    cell_index_range,
    edge_vector,
)

SUBDIVISIONS = (1, 2, 4, 8, 16)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="subdivided_cover_r051")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def rectangle_metrics(
    edges: np.ndarray,
    radius: float,
    grid: int,
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    subdivisions: int,
    inverse: bool,
) -> tuple[float, bool, int, float]:
    """Return area ratio, in-box flag, target-cell count, outward excursion."""

    x_lower, x_upper = source_x
    y_lower, y_upper = source_y
    source_area = (x_upper - x_lower) * (y_upper - y_lower)
    cover_area = 0.0
    all_inside = True
    max_outward = 0.0
    targets: set[int] = set()

    if inverse:
        split_lower, split_upper = y_lower, y_upper
    else:
        split_lower, split_upper = x_lower, x_upper
    split_edges = np.linspace(split_lower, split_upper, subdivisions + 1)

    for index in range(subdivisions):
        sub_lower = float(split_edges[index])
        sub_upper = float(split_edges[index + 1])
        if inverse:
            # H^{-1}(X,Y) = (Y, 1-aY^2-X).
            y_abs_min, y_abs_max = abs_extrema(sub_lower, sub_upper)
            image_x_lower, image_x_upper = sub_lower, sub_upper
            image_y_lower = 1.0 - A_VALUE * y_abs_max**2 - x_upper
            image_y_upper = 1.0 - A_VALUE * y_abs_min**2 - x_lower
        else:
            # H(x,y) = (1-aX^2-Y, X).
            x_abs_min, x_abs_max = abs_extrema(sub_lower, sub_upper)
            image_x_lower = 1.0 - A_VALUE * x_abs_max**2 - y_upper
            image_x_upper = 1.0 - A_VALUE * x_abs_min**2 - y_lower
            image_y_lower, image_y_upper = sub_lower, sub_upper

        rectangle_area = max(0.0, image_x_upper - image_x_lower) * max(
            0.0, image_y_upper - image_y_lower
        )
        cover_area += rectangle_area
        inside = (
            image_x_lower >= -radius
            and image_x_upper <= radius
            and image_y_lower >= -radius
            and image_y_upper <= radius
        )
        all_inside = all_inside and inside
        max_outward = max(
            max_outward,
            max(
                0.0,
                -radius - image_x_lower,
                image_x_upper - radius,
                -radius - image_y_lower,
                image_y_upper - radius,
            ),
        )

        first_x, last_x, nonempty_x = cell_index_range(
            edges, image_x_lower, image_x_upper
        )
        first_y, last_y, nonempty_y = cell_index_range(
            edges, image_y_lower, image_y_upper
        )
        if nonempty_x and nonempty_y:
            for target_y in range(first_y, last_y + 1):
                for target_x in range(first_x, last_x + 1):
                    targets.add(target_y * grid + target_x)

    return cover_area / source_area, all_inside, len(targets), max_outward


def summarize_configuration(
    box: str, radius: float, grid: int, offset: float, subdivisions: int
) -> dict[str, object]:
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
    total = grid * grid

    for source_y_index in range(grid):
        y_lower = float(edges[source_y_index])
        y_upper = float(edges[source_y_index + 1])
        for source_x_index in range(grid):
            x_lower = float(edges[source_x_index])
            x_upper = float(edges[source_x_index + 1])
            f_ratio, f_inside, f_targets, f_outward = rectangle_metrics(
                edges,
                radius,
                grid,
                (x_lower, x_upper),
                (y_lower, y_upper),
                subdivisions,
                inverse=False,
            )
            b_ratio, b_inside, b_targets, b_outward = rectangle_metrics(
                edges,
                radius,
                grid,
                (x_lower, x_upper),
                (y_lower, y_upper),
                subdivisions,
                inverse=True,
            )
            forward_ratios.append(f_ratio)
            backward_ratios.append(b_ratio)
            forward_targets.append(f_targets)
            backward_targets.append(b_targets)
            forward_inside += int(f_inside)
            backward_inside += int(b_inside)
            two_sided_inside += int(f_inside and b_inside)
            max_outward = max(max_outward, f_outward, b_outward)

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
        "subdivisions": subdivisions,
        "state_count": total,
        "minimum_cell_width": float(np.min(widths)),
        "maximum_cell_width": float(np.max(widths)),
        "forward_in_box_fraction": forward_inside / total,
        "backward_in_box_fraction": backward_inside / total,
        "two_sided_in_box_fraction": two_sided_inside / total,
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
            for subdivisions in SUBDIVISIONS:
                records.append(
                    summarize_configuration(box, radius, grid, 0.0, subdivisions)
                )
    for grid, offset in SHIFTED_MAIN:
        for subdivisions in SUBDIVISIONS:
            records.append(
                summarize_configuration("main", BOXES["main"], grid, offset, subdivisions)
            )
    payload = {
        "run_id": "R051_STRIP_COVER",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "a": A_VALUE,
        "subdivisions": list(SUBDIVISIONS),
        "records": records,
        "scope": (
            "float64 subdivided quadratic-strip enclosure diagnostic; no outward "
            "rounding and no invariant-set or convergence certificate"
        ),
    }
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "configurations": len(records),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
