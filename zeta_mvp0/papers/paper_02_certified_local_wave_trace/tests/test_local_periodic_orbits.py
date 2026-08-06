"""Regression tests for the R400 near-well periodic-orbit certificate."""

from __future__ import annotations

from math import pi

import numpy as np

from hp_candidate_search.local_periodic_orbits import (
    OrbitSearchSpec,
    fast_normal_form_data,
    normal_mode_data,
    shoot_brake_orbit,
)
from hp_candidate_search.trace_phase import fast_crr_phase_data
from hp_candidate_search.warped_henon import potential_derivatives


def test_normal_mode_formula_matches_equilibrium_hessian() -> None:
    mode = normal_mode_data(1.02)
    _, _, hessian = potential_derivatives(np.zeros(2), 1.02, 1)
    hessian_frequencies = np.sqrt(np.linalg.eigvalsh(hessian))
    assert np.allclose(hessian_frequencies, mode.angular_frequencies, rtol=2.0e-15)
    assert np.isclose(np.prod(mode.singular_values), 1.0, atol=2.0e-15)
    assert np.isclose(mode.periods[0], mode.singular_values[1])
    assert np.isclose(mode.periods[1], mode.singular_values[0])
    expected_determinant = 4.0 * np.sin(pi / mode.frequency_ratio) ** 2
    assert np.isclose(mode.fast_stability_determinant, expected_determinant)
    assert 0.6 < mode.periods[1] < 0.7
    assert abs(mode.periods[1] - 1.0) > 0.3
    normal_form = fast_normal_form_data(1.02)
    assert np.isclose(normal_form.period_energy_slope, -0.0274450756283701)
    assert np.isclose(
        normal_form.action_ratio_energy_slope,
        0.5 * normal_form.period_energy_slope,
    )


def test_fast_crr_phase_uses_positive_harmonic_trace_branch() -> None:
    phase = fast_crr_phase_data(1.02)
    assert 0.0 < phase.transverse_angle < 2.0 * pi
    assert np.isclose(
        phase.transverse_stability_determinant,
        4.0 * np.sin(0.5 * phase.transverse_angle) ** 2,
    )
    assert phase.crr_candidate_indices == (1, 3)
    assert phase.positive_time_index_mod_four == 1
    assert phase.negative_time_index_mod_four == 3
    assert phase.positive_time_phase == 1.0j
    assert phase.negative_time_phase == -1.0j


def test_fast_brake_orbit_closes_and_has_correct_small_energy_limit() -> None:
    summary, arrays = shoot_brake_orbit(
        OrbitSearchSpec(
            energy_excess=0.05,
            certification_steps_per_period=320,
        )
    )
    assert summary["optimizer_success"] is True
    assert summary["max_abs_shooting_residual"] < 1.0e-10
    assert summary["max_scaled_closure"] < 1.0e-9
    assert summary["max_energy_drift_over_excess"] < 1.0e-9
    assert summary["symplectic_defect_inf"] < 1.0e-9
    assert abs(summary["relative_period_shift"]) < 0.01
    assert abs(summary["relative_action_ratio"] - 1.0) < 0.01
    determinant = summary["transverse_stability_determinant"]
    assert abs(determinant["imag"]) < 1.0e-10
    assert determinant["real"] > 3.0
    assert arrays["states"].shape == (321, 4)
    assert arrays["monodromy"].shape == (4, 4)
