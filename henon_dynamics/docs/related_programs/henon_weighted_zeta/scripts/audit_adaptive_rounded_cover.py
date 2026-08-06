#!/usr/bin/env python3
"""Audit adaptive, outward-rounded quadratic-strip enclosures."""

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

from scripts.audit_interval_cover import (  # noqa: E402
    A_VALUE,
    BOXES,
    abs_extrema,
    cell_index_range,
    edge_vector,
)

ETA = 0.25
MAX_SUBDIVISIONS = 64
RADIUS = BOXES["main"]
CONFIGURATIONS = (
    (64, 0.0),
    (96, 0.0),
    (128, 0.0),
    (160, 0.0),
    (128, -0.25),
    (128, 0.25),
    (160, -0.25),
    (160, 0.25),
)
SAMPLE_SEED = 20260801
SAMPLED_CELLS = 64
POINTS_PER_CELL = 32


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="adaptive_rounded_cover_r052")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    return parser.parse_args()


def outward_bounds(lower: float, upper: float) -> tuple[float, float]:
    return np.nextafter(lower, -math.inf), np.nextafter(upper, math.inf)


def adaptive_subdivisions(
    lower: float, upper: float, target_min_width: float
) -> int:
    width = upper - lower
    _, maximum_abs = abs_extrema(lower, upper)
    numerator = 2.0 * A_VALUE * maximum_abs * width
    if numerator <= 0.0:
        return 1
    raw = math.ceil(numerator / (ETA * target_min_width))
    return min(MAX_SUBDIVISIONS, max(1, raw))


def slab_bounds(
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    index: int,
    subdivisions: int,
    inverse: bool,
    rounded: bool,
) -> tuple[float, float, float, float]:
    x_lower, x_upper = source_x
    y_lower, y_upper = source_y
    if inverse:
        split = np.linspace(y_lower, y_upper, subdivisions + 1)
        sub_lower, sub_upper = float(split[index]), float(split[index + 1])
        y_abs_min, y_abs_max = abs_extrema(sub_lower, sub_upper)
        image_x_lower, image_x_upper = sub_lower, sub_upper
        image_y_lower = 1.0 - A_VALUE * y_abs_max**2 - x_upper
        image_y_upper = 1.0 - A_VALUE * y_abs_min**2 - x_lower
    else:
        split = np.linspace(x_lower, x_upper, subdivisions + 1)
        sub_lower, sub_upper = float(split[index]), float(split[index + 1])
        x_abs_min, x_abs_max = abs_extrema(sub_lower, sub_upper)
        image_x_lower = 1.0 - A_VALUE * x_abs_max**2 - y_upper
        image_x_upper = 1.0 - A_VALUE * x_abs_min**2 - y_lower
        image_y_lower, image_y_upper = sub_lower, sub_upper
    if rounded:
        image_x_lower, image_x_upper = outward_bounds(image_x_lower, image_x_upper)
        image_y_lower, image_y_upper = outward_bounds(image_y_lower, image_y_upper)
    return image_x_lower, image_x_upper, image_y_lower, image_y_upper


def direction_metrics(
    edges: np.ndarray,
    grid: int,
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    target_min_width: float,
    inverse: bool,
) -> dict[str, object]:
    split_lower, split_upper = source_y if inverse else source_x
    subdivisions = adaptive_subdivisions(split_lower, split_upper, target_min_width)
    source_area = (source_x[1] - source_x[0]) * (source_y[1] - source_y[0])
    raw_area = 0.0
    rounded_area = 0.0
    raw_inside = True
    rounded_inside = True
    raw_targets: set[int] = set()
    rounded_targets: set[int] = set()
    max_outward = 0.0
    minimum_endpoint_margin = math.inf
    maximum_rounding_area_delta = 0.0
    for index in range(subdivisions):
        raw = slab_bounds(source_x, source_y, index, subdivisions, inverse, False)
        rounded = slab_bounds(source_x, source_y, index, subdivisions, inverse, True)
        raw_area += max(0.0, raw[1] - raw[0]) * max(0.0, raw[3] - raw[2])
        raw_rectangle_area = max(0.0, raw[1] - raw[0]) * max(0.0, raw[3] - raw[2])
        rounded_rectangle_area = max(0.0, rounded[1] - rounded[0]) * max(
            0.0, rounded[3] - rounded[2]
        )
        rounded_area += rounded_rectangle_area
        # Positive slack means that the final float64 endpoints were expanded
        # away from the corresponding unrounded endpoints.  This checks only
        # the final ``nextafter`` operation; it is not directed interval
        # arithmetic for the intermediate polynomial evaluation.
        minimum_endpoint_margin = min(
            minimum_endpoint_margin,
            raw[0] - rounded[0],
            rounded[1] - raw[1],
            raw[2] - rounded[2],
            rounded[3] - raw[3],
        )
        maximum_rounding_area_delta = max(
            maximum_rounding_area_delta,
            rounded_rectangle_area - raw_rectangle_area,
        )
        raw_inside = raw_inside and (
            raw[0] >= -RADIUS and raw[1] <= RADIUS and raw[2] >= -RADIUS and raw[3] <= RADIUS
        )
        rounded_inside = rounded_inside and (
            rounded[0] >= -RADIUS
            and rounded[1] <= RADIUS
            and rounded[2] >= -RADIUS
            and rounded[3] <= RADIUS
        )
        max_outward = max(
            max_outward,
            max(0.0, -RADIUS - rounded[0], rounded[1] - RADIUS, -RADIUS - rounded[2], rounded[3] - RADIUS),
        )
        for bounds, target_set in ((raw, raw_targets), (rounded, rounded_targets)):
            first_x, last_x, nonempty_x = cell_index_range(edges, bounds[0], bounds[1])
            first_y, last_y, nonempty_y = cell_index_range(edges, bounds[2], bounds[3])
            if nonempty_x and nonempty_y:
                for target_y in range(first_y, last_y + 1):
                    for target_x in range(first_x, last_x + 1):
                        target_set.add(target_y * grid + target_x)
    return {
        "subdivisions": subdivisions,
        "raw_area_ratio": raw_area / source_area,
        "rounded_area_ratio": rounded_area / source_area,
        "raw_inside": raw_inside,
        "rounded_inside": rounded_inside,
        "raw_target_count": len(raw_targets),
        "rounded_target_count": len(rounded_targets),
        "maximum_outward_excursion": max_outward,
        "minimum_endpoint_margin": float(minimum_endpoint_margin),
        "maximum_rounding_area_delta": float(maximum_rounding_area_delta),
    }


def contains_sample(
    point: tuple[float, float],
    source_x: tuple[float, float],
    source_y: tuple[float, float],
    target_min_width: float,
    inverse: bool,
) -> bool:
    split_lower, split_upper = source_y if inverse else source_x
    subdivisions = adaptive_subdivisions(split_lower, split_upper, target_min_width)
    coordinate = point[1] if inverse else point[0]
    fraction = (coordinate - split_lower) / max(split_upper - split_lower, np.finfo(float).tiny)
    index = min(subdivisions - 1, max(0, int(math.floor(fraction * subdivisions))))
    bounds = slab_bounds(source_x, source_y, index, subdivisions, inverse, True)
    if inverse:
        image_x, image_y = point[1], 1.0 - A_VALUE * point[1] ** 2 - point[0]
    else:
        image_x, image_y = 1.0 - A_VALUE * point[0] ** 2 - point[1], point[0]
    return bounds[0] <= image_x <= bounds[1] and bounds[2] <= image_y <= bounds[3]


def summarize_configuration(grid: int, offset: float, rng: np.random.Generator) -> dict[str, object]:
    edges = edge_vector(RADIUS, grid, offset)
    widths = np.diff(edges)
    target_min_width = float(np.min(widths))
    forward_ratios: list[float] = []
    rounded_forward_ratios: list[float] = []
    backward_ratios: list[float] = []
    rounded_backward_ratios: list[float] = []
    forward_inside = backward_inside = two_sided_inside = 0
    cap_hits = 0
    k_values: list[int] = []
    outward_max = 0.0
    minimum_endpoint_margin = math.inf
    maximum_rounding_area_delta = 0.0
    for y_index in range(grid):
        source_y = (float(edges[y_index]), float(edges[y_index + 1]))
        for x_index in range(grid):
            source_x = (float(edges[x_index]), float(edges[x_index + 1]))
            forward = direction_metrics(edges, grid, source_x, source_y, target_min_width, False)
            backward = direction_metrics(edges, grid, source_x, source_y, target_min_width, True)
            forward_ratios.append(float(forward["raw_area_ratio"]))
            rounded_forward_ratios.append(float(forward["rounded_area_ratio"]))
            backward_ratios.append(float(backward["raw_area_ratio"]))
            rounded_backward_ratios.append(float(backward["rounded_area_ratio"]))
            forward_inside += int(bool(forward["rounded_inside"]))
            backward_inside += int(bool(backward["rounded_inside"]))
            two_sided_inside += int(bool(forward["rounded_inside"] and backward["rounded_inside"]))
            k_values.extend([int(forward["subdivisions"]), int(backward["subdivisions"])])
            cap_hits += int(forward["subdivisions"] == MAX_SUBDIVISIONS)
            cap_hits += int(backward["subdivisions"] == MAX_SUBDIVISIONS)
            outward_max = max(outward_max, float(forward["maximum_outward_excursion"]), float(backward["maximum_outward_excursion"]))
            minimum_endpoint_margin = min(
                minimum_endpoint_margin,
                float(forward["minimum_endpoint_margin"]),
                float(backward["minimum_endpoint_margin"]),
            )
            maximum_rounding_area_delta = max(
                maximum_rounding_area_delta,
                float(forward["maximum_rounding_area_delta"]),
                float(backward["maximum_rounding_area_delta"]),
            )

    sample_indices = rng.choice(grid * grid, size=min(SAMPLED_CELLS, grid * grid), replace=False)
    sample_forward = True
    sample_backward = True
    sample_count = 0
    for flat in sample_indices:
        y_index, x_index = divmod(int(flat), grid)
        source_x = (float(edges[x_index]), float(edges[x_index + 1]))
        source_y = (float(edges[y_index]), float(edges[y_index + 1]))
        for _ in range(POINTS_PER_CELL):
            x = float(rng.uniform(*source_x))
            y = float(rng.uniform(*source_y))
            sample_forward = sample_forward and contains_sample((x, y), source_x, source_y, target_min_width, False)
            sample_backward = sample_backward and contains_sample((x, y), source_x, source_y, target_min_width, True)
            sample_count += 1

    def stats(values: list[float]) -> tuple[float, float, float]:
        arr = np.asarray(values, dtype=float)
        return float(np.median(arr)), float(np.quantile(arr, 0.95)), float(np.max(arr))

    raw_f = stats(forward_ratios)
    rounded_f = stats(rounded_forward_ratios)
    raw_b = stats(backward_ratios)
    rounded_b = stats(rounded_backward_ratios)
    k_array = np.asarray(k_values, dtype=float)
    return {
        "box": "main",
        "radius": RADIUS,
        "grid": grid,
        "grid_offset": offset,
        "state_count": grid * grid,
        "minimum_cell_width": target_min_width,
        "adaptive_eta": ETA,
        "maximum_subdivisions": MAX_SUBDIVISIONS,
        "adaptive_k_median": float(np.median(k_array)),
        "adaptive_k_p95": float(np.quantile(k_array, 0.95)),
        "adaptive_k_max": int(np.max(k_array)),
        "adaptive_k_cap_fraction": cap_hits / len(k_values),
        "forward_raw_ratio_median": raw_f[0],
        "forward_raw_ratio_p95": raw_f[1],
        "forward_raw_ratio_max": raw_f[2],
        "forward_rounded_ratio_median": rounded_f[0],
        "forward_rounded_ratio_p95": rounded_f[1],
        "forward_rounded_ratio_max": rounded_f[2],
        "backward_raw_ratio_median": raw_b[0],
        "backward_raw_ratio_p95": raw_b[1],
        "backward_raw_ratio_max": raw_b[2],
        "backward_rounded_ratio_median": rounded_b[0],
        "backward_rounded_ratio_p95": rounded_b[1],
        "backward_rounded_ratio_max": rounded_b[2],
        "forward_rounded_in_box_fraction": forward_inside / (grid * grid),
        "backward_rounded_in_box_fraction": backward_inside / (grid * grid),
        "two_sided_rounded_in_box_fraction": two_sided_inside / (grid * grid),
        "maximum_outward_excursion": outward_max,
        "minimum_endpoint_margin": float(minimum_endpoint_margin),
        "maximum_rounding_area_delta": float(maximum_rounding_area_delta),
        "sample_count": sample_count,
        "sample_forward_containment_pass": bool(sample_forward),
        "sample_backward_containment_pass": bool(sample_backward),
        "rounded_minus_raw_forward_median": rounded_f[0] - raw_f[0],
        "rounded_minus_raw_backward_median": rounded_b[0] - raw_b[0],
    }


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(SAMPLE_SEED)
    records = [summarize_configuration(grid, offset, rng) for grid, offset in CONFIGURATIONS]
    payload = {
        "run_id": "R052_ADAPTIVE_ROUNDED",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "a": A_VALUE,
        "eta": ETA,
        "maximum_subdivisions": MAX_SUBDIVISIONS,
        "sample_seed": SAMPLE_SEED,
        "records": records,
        "scope": "float64 nextafter-outward diagnostic with deterministic sampled containment; not a proof",
    }
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "configurations": len(records)}, indent=2))


if __name__ == "__main__":
    main()
