"""Unit checks for the frozen R053 exact-rational cover implementation.

These tests exercise exact primitives and tiny synthetic cells only.  They do
not run any of the four frozen production configurations.
"""

from __future__ import annotations

import hashlib
from fractions import Fraction

from scripts.audit_exact_closed_cover import (
    AREA_RATIO_BOUND,
    CONFIGURATIONS,
    ETA,
    MAX_SUBDIVISIONS,
    RADIUS,
    _direction_metrics,
    adaptive_subdivisions_exact,
    binary_float_endpoint_audit,
    closed_cell_index_range,
    closed_range_certificate,
    exact_abs_extrema,
    exact_area_ratio,
    exact_ceiling,
    exact_edge_vector,
    exact_slab_bounds,
    exact_statistics,
    fraction_text,
    half_open_cell_index_range,
    rectangle_target_classes,
    uncapped_adaptive_subdivisions_exact,
    update_adjacency_hash,
    validate_frozen_protocol,
)


def test_r053_protocol_matches_string_constructed_fraction_constants():
    payload = validate_frozen_protocol()
    assert Fraction(payload["radius"]) == RADIUS
    assert Fraction(payload["eta"]) == ETA
    assert int(payload["maximum_subdivisions"]) == MAX_SUBDIVISIONS
    assert [(item["grid"], Fraction(item["grid_offset"])) for item in payload["configurations"]] == [
        (grid, offset) for _, grid, offset in CONFIGURATIONS
    ]


def test_exact_edge_vector_is_strict_clipped_and_reflection_paired():
    minus = exact_edge_vector(RADIUS, 8, Fraction(-1, 4))
    plus = exact_edge_vector(RADIUS, 8, Fraction(1, 4))
    assert minus[0] == plus[0] == -RADIUS
    assert minus[-1] == plus[-1] == RADIUS
    assert all(lower < upper for lower, upper in zip(minus, minus[1:]))
    assert all(lower < upper for lower, upper in zip(plus, plus[1:]))
    assert plus == tuple(-value for value in reversed(minus))


def test_exact_ceiling_never_uses_binary_rounding():
    assert exact_ceiling(Fraction(3, 2)) == 2
    assert exact_ceiling(Fraction(4, 2)) == 2
    assert exact_ceiling(Fraction(-3, 2)) == -1
    assert exact_ceiling(Fraction(10**30 + 1, 10**30)) == 2


def test_exact_abs_extrema_handles_zero_and_one_sided_intervals():
    assert exact_abs_extrema(Fraction(-2), Fraction(3)) == (Fraction(0), Fraction(3))
    assert exact_abs_extrema(Fraction(-3), Fraction(-2)) == (Fraction(2), Fraction(3))
    assert exact_abs_extrema(Fraction(2), Fraction(5, 2)) == (
        Fraction(2),
        Fraction(5, 2),
    )


def test_exact_adaptive_ceiling_is_deterministic_and_cap_is_explicit():
    lower, upper = Fraction(1, 3), Fraction(1, 2)
    target_width = Fraction(1, 7)
    first = uncapped_adaptive_subdivisions_exact(lower, upper, target_width)
    second = uncapped_adaptive_subdivisions_exact(lower, upper, target_width)
    assert first == second == 28
    assert adaptive_subdivisions_exact(
        lower, upper, target_width, maximum_subdivisions=8
    ) == 8


def test_frozen_one_dimensional_exact_k_values_do_not_truncate():
    for _, grid, offset in CONFIGURATIONS:
        edges = exact_edge_vector(RADIUS, grid, offset)
        minimum_width = min(
            upper - lower for lower, upper in zip(edges, edges[1:])
        )
        values = [
            uncapped_adaptive_subdivisions_exact(
                edges[index], edges[index + 1], minimum_width
            )
            for index in range(grid)
        ]
        assert max(values) <= MAX_SUBDIVISIONS


def test_exact_slab_bounds_contain_exact_forward_and_inverse_images():
    source_x = (Fraction(-1, 4), Fraction(1, 3))
    source_y = (Fraction(-1, 5), Fraction(2, 7))
    points = (
        (source_x[0], source_y[0]),
        (source_x[0], source_y[1]),
        (Fraction(0), source_y[0]),
        (Fraction(0), source_y[1]),
        (source_x[1], source_y[0]),
        (source_x[1], source_y[1]),
    )
    forward = exact_slab_bounds(source_x, source_y, 0, 1, False)
    backward = exact_slab_bounds(source_x, source_y, 0, 1, True)
    for x_value, y_value in points:
        image = (1 - 6 * x_value**2 - y_value, x_value)
        inverse_image = (y_value, 1 - 6 * y_value**2 - x_value)
        assert forward[0] <= image[0] <= forward[1]
        assert forward[2] <= image[1] <= forward[3]
        assert backward[0] <= inverse_image[0] <= backward[1]
        assert backward[2] <= inverse_image[1] <= backward[3]


def test_closed_indexing_keeps_both_cells_at_a_shared_edge():
    edges = (Fraction(-1), Fraction(0), Fraction(1))
    first, last, nonempty = closed_cell_index_range(edges, Fraction(0), Fraction(0))
    assert (first, last, nonempty) == (0, 1, True)
    assert closed_range_certificate(
        edges, Fraction(0), Fraction(0), first, last, nonempty
    )
    classes = rectangle_target_classes(
        edges, (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    )
    assert set(classes) == {0, 1, 2, 3}
    assert not any(classes.values())


def test_half_open_shared_edge_chooses_right_cell_and_is_closed_subset():
    edges = (Fraction(-1), Fraction(0), Fraction(1))
    closed = closed_cell_index_range(edges, Fraction(0), Fraction(0))
    half_open = half_open_cell_index_range(edges, Fraction(0), Fraction(0))
    assert closed == (0, 1, True)
    assert half_open == (1, 1, True)
    assert half_open_cell_index_range(edges, Fraction(1), Fraction(1)) == (
        1,
        1,
        True,
    )


def test_exact_statistics_uses_average_of_middle_order_statistics():
    stats = exact_statistics(
        [Fraction(1, 3), Fraction(1), Fraction(2, 3), Fraction(4, 3)]
    )
    assert stats.mean == Fraction(5, 6)
    assert stats.median == Fraction(5, 6)
    assert stats.maximum == Fraction(4, 3)
    assert stats.p95 == Fraction(77, 60)


def test_tiny_exact_direction_satisfies_local_and_global_bounds():
    edges = exact_edge_vector(RADIUS, 8, Fraction(0))
    minimum_width = min(
        upper - lower for lower, upper in zip(edges, edges[1:])
    )
    source_x = (edges[5], edges[6])
    source_y = (edges[2], edges[3])
    subdivisions = adaptive_subdivisions_exact(
        source_x[0], source_x[1], minimum_width
    )
    metrics = _direction_metrics(
        edges, source_x, source_y, subdivisions, minimum_width, False
    )
    assert metrics["local_bound_pass"]
    assert metrics["area_ratio"] <= AREA_RATIO_BOUND
    assert metrics["closed_dominates_half_open"]
    assert metrics["closed_target_count"] == len(metrics["target_classes"])


def test_exact_area_ratio_and_binary_bridge_are_deterministic():
    source_x = (Fraction(-1, 8), Fraction(1, 8))
    source_y = (Fraction(1, 10), Fraction(1, 5))
    assert exact_area_ratio(source_x, source_y, 4, False) == exact_area_ratio(
        source_x, source_y, 4, False
    )
    first = binary_float_endpoint_audit(
        (float(source_x[0]), float(source_x[1])),
        (float(source_y[0]), float(source_y[1])),
        4,
        False,
    )
    second = binary_float_endpoint_audit(
        (float(source_x[0]), float(source_x[1])),
        (float(source_y[0]), float(source_y[1])),
        4,
        False,
    )
    assert first == second
    assert first["comparison_count"] == 16
    assert isinstance(first["minimum_margin"], Fraction)


def test_adjacency_hash_retains_direction_source_target_and_class():
    digest = hashlib.sha256()
    update_adjacency_hash(digest, "F", 7, {4: False, 2: True})
    expected = hashlib.sha256(b"F,7,2,P\nF,7,4,T\n").hexdigest()
    assert digest.hexdigest() == expected
    assert fraction_text(Fraction(6, 3)) == "2"
