import numpy as np
import pytest

from henon_zeta.controls import analytic_period3, analytic_period3_traces
from henon_zeta.geometry import fixed_points
from henon_zeta.orbits import (
    canonical_rotation,
    cyclic_jacobian,
    cyclic_residual,
    floating_point_kantorovich_diagnostic,
    primitive_period,
    search_period,
)


@pytest.mark.parametrize("period", [1, 2, 3, 5])
def test_cyclic_jacobian_matches_finite_difference(period):
    a = 1.02
    sequence = np.linspace(-0.8, 0.7, period)
    analytic = cyclic_jacobian(sequence, a)
    numerical = np.empty_like(analytic)
    epsilon = 1.0e-7
    for column in range(period):
        direction = np.zeros(period)
        direction[column] = epsilon
        numerical[:, column] = (cyclic_residual(sequence + direction, a) - cyclic_residual(sequence - direction, a)) / (2.0 * epsilon)
    assert np.allclose(analytic, numerical, atol=1e-8)


def test_primitive_and_canonical_sequence_logic():
    sequence = np.array([0.1, 0.2, 0.1, 0.2])
    assert primitive_period(sequence) == 2
    assert np.allclose(canonical_rotation([0.2, 0.1, 0.2, 0.1]), sequence)


def test_floating_point_kantorovich_diagnostic_for_fixed_point():
    coordinate = fixed_points(1.02)[0].coordinate
    diagnostic = floating_point_kantorovich_diagnostic([coordinate], 1.02)
    assert diagnostic.passed
    assert diagnostic.alpha < 1e-12


def test_period3_smoke_recovers_closed_form_orbits():
    records, stats = search_period(1.02, 3, random_starts=16, seed=7)
    assert stats.orbit_count == 2
    assert stats.diagnostic_passed_orbits == 2
    assert {record.stability for record in records} == {"elliptic", "hyperbolic"}
    assert sorted(record.trace for record in records) == pytest.approx(sorted(analytic_period3_traces(1.02)), abs=1e-10)
    for expected in analytic_period3(1.02):
        assert any(np.min([np.linalg.norm(np.asarray(expected) - np.roll(record.sequence, shift), ord=np.inf) for shift in range(3)]) < 1e-9 for record in records)
