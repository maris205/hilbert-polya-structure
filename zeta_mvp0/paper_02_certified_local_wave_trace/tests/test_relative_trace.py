"""Unit tests for the bounded R200 common-grid implementation."""

from __future__ import annotations

import numpy as np
from scipy import sparse

from hp_candidate_search.relative_trace import (
    CommonGridSpec,
    build_common_grid_pair,
    common_grid_geometry,
    compressed_resolvent_differences,
    frozen_window_definitions,
    heat_trace_diagnostics,
    relative_counting_staircase,
    truncated_resolvent_trace_diagnostics,
    wave_trace_diagnostics,
)


def test_common_pair_shares_grid_kinetic_and_offdiagonal() -> None:
    spec = CommonGridSpec(
        target_energy=50.0,
        nominal_spacing=0.35,
        eigenvalue_count=6,
        wall_factor=10.0,
        boundary_padding=0.15,
        cap_multiplier=100.0,
        boundary_samples=256,
    )
    pair = build_common_grid_pair(spec)
    delta = (pair.h1 - pair.h0).tocsr()
    offdiagonal = delta - sparse.diags(delta.diagonal(), format="csr")
    assert pair.h0.shape == pair.h1.shape == pair.kinetic.shape
    assert offdiagonal.nnz == 0 or np.max(np.abs(offdiagonal.data)) < 1.0e-14
    assert np.issubdtype(pair.h0.dtype, np.floating)
    assert np.max(np.abs((pair.h0 - pair.h0.T).data), initial=0.0) < 1.0e-14
    assert pair.metadata["same_kinetic_matrix"] is True


def test_physical_rectangle_is_independent_of_spacing() -> None:
    common = dict(
        target_energy=80.0,
        eigenvalue_count=8,
        wall_factor=20.0,
        boundary_padding=0.2,
        boundary_samples=256,
    )
    _, _, _, _, coarse = common_grid_geometry(
        CommonGridSpec(nominal_spacing=0.2, **common)
    )
    _, _, _, _, fine = common_grid_geometry(
        CommonGridSpec(nominal_spacing=0.1, **common)
    )
    assert coarse["common_rectangle"] == fine["common_rectangle"]


def test_dense_resolvent_identity_direct_and_nuclear_norm() -> None:
    h0_dense = np.diag([2.0, 3.0, 5.0, 8.0])
    h1_dense = h0_dense + np.array(
        [
            [0.4, 0.1, 0.0, 0.0],
            [0.1, 0.2, 0.1, 0.0],
            [0.0, 0.1, 0.3, 0.1],
            [0.0, 0.0, 0.1, 0.2],
        ]
    )
    values0, vectors0 = np.linalg.eigh(h0_dense)
    arrays, summary = compressed_resolvent_differences(
        sparse.csr_matrix(h0_dense),
        sparse.csr_matrix(h1_dense),
        values0,
        vectors0,
        cutoffs=(2, 4),
        repeat=True,
    )
    for power in (1, 2, 3):
        direct = arrays[f"compressed_direct_difference_power{power}_M4"]
        identity = arrays[f"compressed_identity_difference_power{power}_M4"]
        assert np.linalg.norm(direct - identity) < 1.0e-13
        singular_values = np.linalg.svd(identity, compute_uv=False)
        assert np.allclose(arrays[f"singular_values_power{power}_M4"], singular_values)
        assert np.isclose(
            summary["nuclear_norms"][f"power{power}_M4"],
            np.sum(singular_values),
        )
        assert summary["repeat_relative_differences"][f"power{power}_M4"] < 1.0e-14


def test_xi_sign_heat_and_resolvent_trace_identities() -> None:
    values0 = np.array([1.0, 3.0, 6.0, 10.0])
    values1 = np.array([2.0, 4.0, 7.0, 11.0])
    events, xi = relative_counting_staircase(values0, values1)
    assert np.array_equal(events, np.arange(1.0, 12.0)) is False
    assert xi[0] == 1
    assert xi[1] == 0
    heat_arrays, heat_summary = heat_trace_diagnostics(
        values0, values1, np.array([0.05, 0.2, 1.0])
    )
    assert np.allclose(
        heat_arrays["heat_direct"],
        heat_arrays["heat_from_staircase"],
        atol=2.0e-15,
    )
    assert heat_summary["max_scaled_identity_error"] < 2.0e-15
    _, trace_summary = truncated_resolvent_trace_diagnostics(values0, values1)
    assert max(trace_summary["absolute_identity_errors"].values()) < 2.0e-15


def test_wave_staircase_conjugacy_null_and_surrogate() -> None:
    values0 = np.array([20.0, 31.0, 45.0, 60.0])
    values1 = np.array([21.0, 29.0, 47.0, 63.0])
    times = np.linspace(0.0, 0.5, 101)
    window = {
        "window_index": 0,
        "width_index": 0,
        "center": 40.0,
        "sigma": 12.0,
    }
    arrays, summary = wave_trace_diagnostics(
        values0, values1, times, window, surrogate_seed=20260806
    )
    relative = arrays["wave_relative_real"] + 1.0j * arrays["wave_relative_imag"]
    from_staircase = arrays["wave_from_staircase_real"] + 1.0j * arrays[
        "wave_from_staircase_imag"
    ]
    surrogate = arrays["wave_surrogate_real"] + 1.0j * arrays[
        "wave_surrogate_imag"
    ]
    assert np.max(np.abs(relative - from_staircase)) < 2.0e-13
    assert summary["max_h0_h0_null"] == 0.0
    assert not np.allclose(relative, surrogate)

    negative_arrays, _ = wave_trace_diagnostics(
        values0, values1, -times[::-1], window, surrogate_seed=20260806
    )
    negative = negative_arrays["wave_relative_real"] + 1.0j * negative_arrays[
        "wave_relative_imag"
    ]
    assert np.allclose(negative, np.conjugate(relative[::-1]))


def test_frozen_window_rule_is_deterministic() -> None:
    values0 = np.linspace(10.0, 210.0, 50)
    values1 = np.linspace(12.0, 212.0, 50)
    first = frozen_window_definitions(values0, values1)
    second = frozen_window_definitions(values0, values1)
    assert first == second
    assert len(first) == 9
    assert {item["window_index"] for item in first} == {0, 1, 2}
    assert {item["width_multiplier"] for item in first} == {0.8, 1.0, 1.2}

