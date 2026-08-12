from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pytest


CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.analysis import (  # noqa: E402
    ClusterBlock,
    fixed_grid_transition,
    holm_adjust,
    odd_risk,
    paired_cluster_bootstrap,
    polarity,
)


def _block(even, odd, exposure=None, survived=None) -> ClusterBlock:
    even = np.asarray(even, dtype=np.int64)
    odd = np.asarray(odd, dtype=np.int64)
    n = len(even)
    if exposure is None:
        exposure = np.full(n, 10, dtype=np.int64)
    if survived is None:
        survived = np.ones(n, dtype=bool)
    return ClusterBlock(
        trajectory_id=np.arange(n),
        exposure_steps=np.asarray(exposure, dtype=np.int64),
        survived=np.asarray(survived, dtype=bool),
        even_gaps=even,
        odd_gaps=odd,
    )


def test_polarity_and_odd_risk_are_consistent() -> None:
    assert polarity(75, 25) == pytest.approx(0.5)
    assert odd_risk(75, 25) == pytest.approx(0.25)
    assert np.isnan(polarity(0, 0))
    values = polarity(np.array([3, 1]), np.array([1, 3]))
    np.testing.assert_allclose(values, [0.5, -0.5])


def test_paired_cluster_bootstrap_is_deterministic_and_preserves_pairing() -> None:
    primary = _block([10, 8, 12, 9], [0, 1, 0, 1])
    control = _block([6, 5, 7, 4], [4, 3, 5, 4])
    first = paired_cluster_bootstrap(
        primary,
        control,
        horizon=10,
        n_replicates=250,
        seed=19,
    )
    second = paired_cluster_bootstrap(
        primary,
        control,
        horizon=10,
        n_replicates=250,
        seed=19,
    )
    assert first == second
    assert first["paired_trajectories"] == 4
    assert first["polarity_difference"] > 0
    assert first["odd_risk_difference"] < 0
    assert first["log_odd_gap_odds_ratio"] < 0
    assert first["polarity_difference_ci_low"] > 0
    assert first["polarity_one_sided_bootstrap_p"] < 0.05


def test_directional_bootstrap_tail_rejects_wrong_direction() -> None:
    primary = _block([4, 5, 4, 6], [6, 5, 7, 4])
    control = _block([10, 9, 12, 11], [0, 1, 0, 0])
    result = paired_cluster_bootstrap(
        primary,
        control,
        horizon=10,
        n_replicates=250,
        seed=23,
    )
    assert result["polarity_difference"] < 0
    assert result["polarity_one_sided_bootstrap_p"] > 0.95


def test_holm_adjustment_is_monotone_in_sorted_order() -> None:
    raw = {"a": 0.01, "b": 0.04, "c": 0.03, "d": 0.20}
    adjusted = holm_adjust(raw)
    assert adjusted == pytest.approx(
        {"a": 0.04, "b": 0.09, "c": 0.09, "d": 0.20}
    )


def test_fixed_grid_transition_uses_only_adjacent_frozen_points() -> None:
    rows = [
        {"rho": 0.0, "parity_polarity": 1.0, "exposure_fraction": 1.0},
        {"rho": 0.2, "parity_polarity": 0.99, "exposure_fraction": 1.0},
        {"rho": 0.5, "parity_polarity": -0.8, "exposure_fraction": 0.7},
        {"rho": 1.0, "parity_polarity": -0.7, "exposure_fraction": 0.01},
    ]
    result = fixed_grid_transition(rows, exposure_gate=0.8)
    assert result["largest_polarity_change_interval"] == [0.2, 0.5]
    assert result["largest_exposure_change_interval"] == [0.5, 1.0]
    assert result["exposure_gate_crossing_intervals"] == [
        {"rho_left": 0.2, "rho_right": 0.5}
    ]
