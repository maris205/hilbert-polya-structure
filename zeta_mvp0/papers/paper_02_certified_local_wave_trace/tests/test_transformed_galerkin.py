"""Regression tests for the form-domain-valid R401 spectral path."""

from __future__ import annotations

from math import pi

import numpy as np
import pytest

from hp_candidate_search.local_periodic_orbits import normal_mode_data
from hp_candidate_search.radial_laguerre import (
    RadialLaguerreSpec,
    solve_radial_laguerre,
)
from hp_candidate_search.semiclassical_trace import (
    energy_cutoff,
    filtered_spectral_density,
    inverse_fourier_test_function,
    ordered_spectrum_difference,
    predicted_fast_orbit_term,
    r401_window_delta_0p01,
)
from hp_candidate_search.transformed_galerkin import (
    TransformedGalerkinSpec,
    solve_transformed_galerkin,
    transformed_metric_data,
)


def _harmonic_spectrum(
    frequencies: tuple[float, float], hbar: float, ceiling: float
) -> np.ndarray:
    values: list[float] = []
    first = 0
    while hbar * frequencies[0] * (first + 0.5) + 0.5 * hbar * frequencies[1] <= ceiling:
        second = 0
        while True:
            excess = hbar * (
                frequencies[0] * (first + 0.5)
                + frequencies[1] * (second + 0.5)
            )
            if excess > ceiling:
                break
            values.append(2.0 * pi + excess)
            second += 1
        first += 1
    return np.sort(np.asarray(values))


def test_exact_coordinate_metric_normalization() -> None:
    singular, linear_map, inverse_map, _ = transformed_metric_data(1.02)
    assert np.isclose(np.prod(singular), 1.0, atol=2.0e-15)
    assert np.isclose(np.linalg.det(linear_map), 1.0, atol=2.0e-15)
    assert np.allclose(inverse_map @ linear_map, np.eye(2), atol=2.0e-15)
    assert np.allclose(
        singular,
        normal_mode_data(1.02).singular_values,
        atol=2.0e-15,
    )


def test_radial_oracle_matches_transformed_cartesian_assembly() -> None:
    hbar = 0.002
    cartesian, cartesian_meta = solve_transformed_galerkin(
        TransformedGalerkinSpec(
            hbar=hbar,
            a=0.0,
            basis_excess_cutoff=0.14,
            eigenvalue_excess_ceiling=0.09,
            quadrature_order=72,
        )
    )
    radial, radial_meta = solve_radial_laguerre(
        RadialLaguerreSpec(
            hbar=hbar,
            basis_excess_cutoff=0.14,
            eigenvalue_excess_ceiling=0.09,
            quadrature_order=88,
        )
    )
    assert len(cartesian) == len(radial) == 28
    assert np.max(np.abs(cartesian - radial)) < 3.0e-13
    assert cartesian_meta["quadrature_orthogonality_defect"] < 1.0e-12
    assert radial_meta["maximum_quadrature_orthogonality_defect"] < 1.0e-12


def test_warped_nested_ritz_convergence_and_form_domain_guard() -> None:
    hbar = 0.0016
    inner, _ = solve_transformed_galerkin(
        TransformedGalerkinSpec(hbar, 1.02, 0.16, 0.09, 72)
    )
    outer, _ = solve_transformed_galerkin(
        TransformedGalerkinSpec(hbar, 1.02, 0.20, 0.09, 80)
    )
    comparison = ordered_spectrum_difference(
        outer, inner, upper_energy=2.0 * pi + 0.075
    )
    assert comparison["compared_eigenvalues"] == 28
    assert comparison["max_absolute_difference"] < 2.0e-8

    with pytest.raises(ValueError, match="form domain"):
        solve_transformed_galerkin(
            TransformedGalerkinSpec(1.5, 1.02, 20.0, 10.0, 32)
        )


def test_trace_window_quadrature_and_exact_harmonic_oracle() -> None:
    window = r401_window_delta_0p01(512)
    window_fine = r401_window_delta_0p01(768)
    bottom = 2.0 * pi
    cutoff = energy_cutoff(
        np.array(
            [
                bottom + 0.001,
                bottom + 0.002,
                bottom + 0.004,
                bottom + 0.010,
                bottom + 0.016,
                bottom + 0.018,
            ]
        ),
        window,
    )
    assert np.allclose(cutoff[[0, 1, 5]], 0.0)
    assert np.allclose(cutoff[2:5], 1.0)
    scaled = np.array([-200.0, -80.0, 0.0, 80.0, 200.0])
    assert np.max(
        np.abs(
            inverse_fourier_test_function(scaled, window)
            - inverse_fourier_test_function(scaled, window_fine)
        )
    ) < 2.0e-12

    mode = normal_mode_data(1.02)
    hbar = 5.0e-5
    target = bottom + 0.01
    warped = _harmonic_spectrum(mode.angular_frequencies, hbar, 0.019)
    radial = _harmonic_spectrum((2.0 * pi, 2.0 * pi), hbar, 0.019)
    relative = filtered_spectral_density(
        warped, target_energy=target, hbar=hbar, window=window_fine
    ) - filtered_spectral_density(
        radial, target_energy=target, hbar=hbar, window=window_fine
    )
    prediction = predicted_fast_orbit_term(
        hbar=hbar,
        action=mode.periods[1] * 0.01,
        period=mode.periods[1],
        stability_determinant=mode.fast_stability_determinant,
    )
    assert abs(relative / prediction - 1.0) < 0.05
