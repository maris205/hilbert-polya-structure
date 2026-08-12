from __future__ import annotations

import math
from pathlib import Path
import sys

import numpy as np
import pytest


CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.attractors import (  # noqa: E402
    classify_periodic_tails,
    generate_diagnostic_parent_ensemble,
    positive_fixed_point,
    positive_fixed_point_flip_threshold,
    positive_fixed_point_jury_margins,
    positive_fixed_point_multipliers,
    simulate_and_classify_attractors,
)
from symplectic_henon.symbolic import FROZEN_A  # noqa: E402


def test_flip_threshold_puts_multiplier_at_minus_one() -> None:
    a = FROZEN_A
    threshold = positive_fixed_point_flip_threshold(a)
    x_plus = positive_fixed_point(a, threshold)
    assert threshold == pytest.approx(math.sqrt(4.0 * a / 3.0) - 1.0)
    assert 2.0 * a * x_plus == pytest.approx(1.0 + threshold)
    multipliers = positive_fixed_point_multipliers(a, threshold)
    assert min(abs(value + 1.0) for value in multipliers) < 1e-12
    assert min(abs(value + threshold) for value in multipliers) < 1e-12


def test_jury_stability_changes_at_flip_and_ends_at_rho_one() -> None:
    threshold = positive_fixed_point_flip_threshold(FROZEN_A)
    below = positive_fixed_point_jury_margins(FROZEN_A, threshold - 1e-5)
    above = positive_fixed_point_jury_margins(FROZEN_A, threshold + 1e-5)
    endpoint = positive_fixed_point_jury_margins(FROZEN_A, 1.0)
    assert below["one_minus_b_plus_rho"] < 0.0
    assert all(value > 0.0 for value in above.values())
    assert endpoint["one_minus_rho"] == 0.0
    endpoint_multipliers = positive_fixed_point_multipliers(FROZEN_A, 1.0)
    np.testing.assert_allclose(np.abs(endpoint_multipliers), 1.0, atol=1e-14)


def test_periodic_tail_classifier_finds_least_period() -> None:
    period_two = np.array([[1.0, -0.5], [-0.25, 0.75]])
    period_four = np.array(
        [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
    )
    tails = np.stack(
        (
            np.tile(period_two, (40, 1))[:64],
            np.tile(period_four, (20, 1))[:64],
        ),
        axis=1,
    )
    periods, residuals = classify_periodic_tails(
        tails,
        candidate_periods=range(1, 9),
        absolute_tolerance=1e-14,
        relative_tolerance=0.0,
    )
    assert periods.tolist() == [2, 4]
    np.testing.assert_array_equal(residuals, 0.0)


def test_diagnostic_ensemble_is_deterministic_and_separate() -> None:
    first = generate_diagnostic_parent_ensemble(
        a=FROZEN_A, n_trajectories=16, parent_burn_in=64
    )
    second = generate_diagnostic_parent_ensemble(
        a=FROZEN_A, n_trajectories=16, parent_burn_in=64
    )
    np.testing.assert_array_equal(first, second)
    with pytest.raises(ValueError, match="distinct"):
        generate_diagnostic_parent_ensemble(
            a=FROZEN_A,
            n_trajectories=2,
            parent_burn_in=2,
            seed=20260814,
        )


def test_dissipative_fixed_point_has_a_detectable_basin() -> None:
    a = FROZEN_A
    rho = 0.6
    center = positive_fixed_point(a, rho)
    initial = np.array(
        [
            [center + 0.02, center - 0.01],
            [center - 0.03, center + 0.01],
            [center + 0.01, center + 0.03],
        ]
    )
    run = simulate_and_classify_attractors(
        initial,
        a=a,
        rho=rho,
        burn_in=1024,
        tail_length=128,
        max_period=16,
        absolute_tolerance=1e-10,
        relative_tolerance=1e-10,
    )
    assert run.labels.tolist() == ["fixed_positive"] * 3
    assert run.periods.tolist() == [1, 1, 1]


def test_escape_is_absorbing_and_not_periodic() -> None:
    run = simulate_and_classify_attractors(
        np.array([[10.0, 0.0]]),
        a=6.0,
        rho=1.0,
        burn_in=10,
        tail_length=32,
        max_period=8,
        escape_bound=100.0,
    )
    assert run.labels.tolist() == ["escape"]
    assert run.periods.tolist() == [-1]
    assert run.escape_steps.tolist() == [1]
