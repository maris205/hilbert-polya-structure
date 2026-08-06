"""Focused regression tests for the R052 adaptive rounded-cover diagnostic.

These tests deliberately check implementation invariants rather than treating
the finite-resolution cover as a rigorous interval certificate.  In
particular, ``numpy.nextafter`` expands each final reported endpoint by one
float64 ulp, but the preceding polynomial arithmetic is not directed interval
arithmetic.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from scripts.audit_adaptive_rounded_cover import (
    CONFIGURATIONS,
    MAX_SUBDIVISIONS,
    RADIUS,
    adaptive_subdivisions,
)
from scripts.audit_interval_cover import edge_vector


PROJECT_ROOT = Path(__file__).resolve().parents[1]
R052_RESULTS = PROJECT_ROOT / "results" / "adaptive_rounded_cover_r052.json"
R052_ANALYSIS = (
    PROJECT_ROOT / "results" / "adaptive_rounded_cover_analysis_r052.json"
)


def _configuration_k_values(grid: int, offset: float) -> list[int]:
    """Return all one-dimensional adaptive K values for a frozen grid."""

    edges = edge_vector(RADIUS, grid, offset)
    target_min_width = float(np.min(np.diff(edges)))
    return [
        adaptive_subdivisions(
            float(edges[index]), float(edges[index + 1]), target_min_width
        )
        for index in range(grid)
    ]


def test_r052_adaptive_k_is_deterministic_and_bounded():
    """The same frozen geometry must produce the same K and never exceed 64."""

    assert MAX_SUBDIVISIONS == 64
    for grid, offset in CONFIGURATIONS:
        first = _configuration_k_values(grid, offset)
        second = _configuration_k_values(grid, offset)
        assert first == second
        assert all(1 <= value <= 64 for value in first)


def test_r052_frozen_configurations_do_not_hit_the_subdivision_cap():
    """The preregistered R052 grids remain below the adaptive K cap."""

    for grid, offset in CONFIGURATIONS:
        values = _configuration_k_values(grid, offset)
        assert max(values) < MAX_SUBDIVISIONS

    # Also guard the persisted audit against an accidentally stale or
    # malformed cap statistic.  This is read-only and does not regenerate the
    # experiment output.
    payload = json.loads(R052_RESULTS.read_text(encoding="utf-8"))
    assert len(payload["records"]) == len(CONFIGURATIONS)
    assert all(
        float(record["adaptive_k_cap_fraction"]) == 0.0
        and int(record["adaptive_k_max"]) < MAX_SUBDIVISIONS
        for record in payload["records"]
    )


def test_r052_final_endpoint_expansion_has_nonnegative_slack():
    """Final expanded endpoints contain their unrounded float64 counterparts."""

    payload = json.loads(R052_RESULTS.read_text(encoding="utf-8"))
    margins = [float(record["minimum_endpoint_margin"]) for record in payload["records"]]
    assert margins
    assert all(np.isfinite(margin) for margin in margins)
    assert min(margins) >= 0.0


def test_r052_analysis_keeps_literal_and_tolerant_k16_decisions_separate():
    """Roundoff-scale equivalence must not overwrite the frozen strict check."""

    decisions = json.loads(R052_ANALYSIS.read_text(encoding="utf-8"))["decisions"]
    assert not decisions["adaptive_no_worse_than_fixed_k16_literal_all"]
    assert decisions["adaptive_no_worse_than_fixed_k16_literal_pass_count"] == 6
    assert decisions["adaptive_within_1e_12_of_fixed_k16_all"]
    assert 0.0 < decisions["fixed_k16_maximum_positive_excess"] < 1.0e-12
    assert decisions["median_rounding_ratio_inflation_small_all"]
    assert decisions["maximum_rounding_area_delta_small_all"]
