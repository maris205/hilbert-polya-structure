#!/usr/bin/env python3
"""Independent toy and schema checks for the R055 true-image predicate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def square_range(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    if upper < lower:
        raise ValueError("reversed interval")
    values = [lower * lower, upper * upper]
    if lower <= 0 <= upper:
        values.append(Fraction(0))
    return min(values), max(values)


def overlap_class(
    parameter: tuple[Fraction, Fraction],
    target_parameter: tuple[Fraction, Fraction],
    lower: Fraction,
    upper: Fraction,
) -> bool | None:
    left = max(parameter[0], target_parameter[0])
    right = min(parameter[1], target_parameter[1])
    if right < left:
        return None
    sq_left, sq_right = square_range(left, right)
    q_left, q_right = 6 * sq_left, 6 * sq_right
    lo, hi = max(q_left, lower), min(q_right, upper)
    if hi < lo:
        return None
    return right > left and hi > lo


def forward_class(source, target):
    (xl, xu), (yl, yu) = source
    (XL, XU), (YL, YU) = target
    return overlap_class(
        (xl, xu),
        (YL, YU),
        1 - XU - yu,
        1 - XL - yl,
    )


def inverse_class(source, target):
    (xl, xu), (yl, yu) = source
    (XL, XU), (YL, YU) = target
    return overlap_class(
        (yl, yu),
        (XL, XU),
        1 - YU - xu,
        1 - YL - xl,
    )


def run_toy_checks() -> None:
    F = Fraction
    # Empty projected interval J.
    assert forward_class(((F(0), F(1)), (F(0), F(1))), ((F(0), F(1)), (F(2), F(3)))) is None
    # A single-point J and a single-point q contact: nonempty, touch-only.
    point_source = ((F(0), F(1)), (F(0), F(0)))
    point_target = ((F(-5), F(-5)), (F(1), F(1)))
    assert forward_class(point_source, point_target) is False
    # Strict overlap gives positive area.
    positive_target = ((F(-11, 2), F(-9, 2)), (F(0), F(1)))
    assert forward_class(((F(0), F(1)), (F(0), F(1))), positive_target) is True
    # Crossing zero must use min x^2 = 0, not an endpoint-only minimum.
    cross_source = ((F(-1), F(1)), (F(0), F(1)))
    cross_target = ((F(-5), F(-4)), (F(-1), F(1)))
    assert forward_class(cross_source, cross_target) is True
    # Exact reversibility: forward(C,D) equals inverse(D,C), including class.
    source = ((F(-1, 2), F(1, 2)), (F(-1, 3), F(2, 3)))
    target = ((F(-3), F(-2)), (F(-1, 2), F(1, 2)))
    assert forward_class(source, target) == inverse_class(target, source)


def run_schema_checks(input_path: Path) -> None:
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    assert payload["run_id"] == "R055_TRUE_IMAGE_GRAPH"
    assert len(payload["records"]) == 4
    for record in payload["records"]:
        assert record["outer_reconstruction_pass"]
        assert record["true_edge_subset_outer_pass"]
        assert record["true_positive_subset_outer_positive_pass"]
        assert record["true_forward_inverse_transpose_pass"]
        assert record["true_equals_outer_mutual_pass"]
        assert record["true_positive_equals_outer_positive_pass"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "true_image_graph_r055.json",
    )
    args = parser.parse_args()
    run_toy_checks()
    run_schema_checks(args.input)
    print("R055 independent toy/schema checks: PASS")


if __name__ == "__main__":
    main()
