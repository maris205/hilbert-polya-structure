from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pytest


CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.symbolic import (  # noqa: E402
    FROZEN_A,
    SPLIT_SEEDS,
    cluster_bootstrap,
    evaluate_confirmatory_endpoint,
    generate_parent_ensemble,
    henon_step,
    markov_return_polarity,
    parity_polarity,
    quadratic_step,
    simulate_transport,
    split_seed,
)


def test_rho_zero_is_exact_parent_lift() -> None:
    state = generate_parent_ensemble(
        split="train", n_trajectories=32, burn_in=64
    )
    x = state[:, 0]
    y = state[:, 1]
    for _ in range(12):
        next_x, next_y = henon_step(x, y, a=FROZEN_A, rho=0.0)
        np.testing.assert_array_equal(next_x, quadratic_step(x, FROZEN_A))
        np.testing.assert_array_equal(next_y, x)
        x, y = next_x, next_y


def test_splits_are_deterministic_and_test_is_locked() -> None:
    first = generate_parent_ensemble(
        split="dev", n_trajectories=16, burn_in=32
    )
    second = generate_parent_ensemble(
        split="dev", n_trajectories=16, burn_in=32
    )
    np.testing.assert_array_equal(first, second)
    assert split_seed("validation") == SPLIT_SEEDS["validation"]
    with pytest.raises(PermissionError):
        split_seed("test")
    with pytest.raises(PermissionError):
        generate_parent_ensemble(
            split="test", n_trajectories=2, burn_in=2
        )


def test_parent_reference_has_frozen_even_gap_shadow() -> None:
    state = generate_parent_ensemble(
        split="train", n_trajectories=128, burn_in=512
    )
    result = simulate_transport(state, rho=0.0, horizon=256)
    assert result.exposure_fraction == 1.0
    assert result.survival_fraction == 1.0
    assert result.total_gaps > 1000
    assert result.odd_gaps == 0
    assert result.parity_polarity == 1.0
    assert int(result.gap_histogram.sum()) == result.total_gaps
    assert np.all(result.clusters.gap_counts <= result.clusters.left_visits)


def test_markov_null_formula_for_strict_alternation() -> None:
    transitions = np.array([[0, 100], [100, 0]], dtype=np.int64)
    assert markov_return_polarity(transitions) == pytest.approx(1.0)
    assert parity_polarity(75, 25) == pytest.approx(0.5)
    assert np.isnan(parity_polarity(0, 0))


def test_cluster_bootstrap_is_deterministic_and_clustered() -> None:
    state = generate_parent_ensemble(
        split="train", n_trajectories=64, burn_in=256
    )
    result = simulate_transport(state, rho=0.05, horizon=128)
    first = cluster_bootstrap(result, n_replicates=100, seed=37)
    second = cluster_bootstrap(result, n_replicates=100, seed=37)
    assert first == second
    parity_low, parity_high = first["parity_polarity"]
    assert -1.0 <= parity_low <= parity_high <= 1.0
    exposure_low, exposure_high = first["exposure_fraction"]
    assert 0.0 <= exposure_low <= exposure_high <= 1.0


def test_escape_exposure_is_counted_before_censoring() -> None:
    state = np.array([[10.0, 0.0]])
    result = simulate_transport(
        state,
        rho=1.0,
        a=6.0,
        horizon=5,
        escape_bound=100.0,
    )
    assert result.clusters.exposure_steps.tolist() == [1]
    assert result.exposure_fraction == pytest.approx(0.2)
    assert result.survival_fraction == 0.0
    assert result.escape_times.tolist() == [1]


def test_confirmatory_endpoint_requires_both_availability_gates() -> None:
    base_summary = {
        "parity_polarity": 0.995,
        "parity_polarity_ci_low": 0.99,
        "parity_polarity_ci_high": 0.999,
        "exposure_fraction": 0.9,
        "total_gaps": 9_999,
    }
    too_few_gaps = evaluate_confirmatory_endpoint(
        base_summary,
        split="test",
        neighbor_specificity_passed=True,
    )
    assert too_few_gaps["exposure_gate_passed"] is True
    assert too_few_gaps["gap_count_gate_passed"] is False
    assert too_few_gaps["availability_gate_passed"] is False
    assert too_few_gaps["confirmatory_passed"] is False
    assert too_few_gaps["status"] == "a0_shadow_fail_carrier_unavailable"

    passing_summary = dict(base_summary, total_gaps=10_000)
    passing = evaluate_confirmatory_endpoint(
        passing_summary,
        split="test",
        neighbor_specificity_passed=True,
    )
    assert passing["availability_gate_passed"] is True
    assert passing["polarity_ci_gate_passed"] is True
    assert passing["confirmatory_passed"] is True
    assert passing["status"] == "confirmatory_pass"

    no_exposure = evaluate_confirmatory_endpoint(
        dict(passing_summary, exposure_fraction=0.799),
        split="test",
        neighbor_specificity_passed=True,
    )
    assert no_exposure["availability_gate_passed"] is False
    assert no_exposure["confirmatory_passed"] is False
