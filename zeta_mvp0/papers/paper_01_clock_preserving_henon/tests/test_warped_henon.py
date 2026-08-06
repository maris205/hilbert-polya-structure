import numpy as np

from hp_candidate_search.warped_henon import (
    centered_fixed_point,
    hamiltonian_energy,
    henon_inverse_iterate,
    henon_iterate_jet,
    henon_step,
    potential_derivatives,
)


def test_centered_conjugacy_and_fixed_origin():
    for a in (0.0, 1.02, 6.0):
        r = centered_fixed_point(a)
        original_at_fixed = np.array([1.0 - a * r * r - r, r])
        np.testing.assert_allclose(original_at_fixed, [r, r], atol=2e-14)
        np.testing.assert_allclose(henon_step([0.0, 0.0], a), [0.0, 0.0])


def test_inverse_and_area_preservation():
    q = np.array([0.137, -0.281])
    for a in (0.0, 1.02, 6.0):
        for n in (1, 2, 3):
            u, jac, _ = henon_iterate_jet(q, a, n)
            recovered = henon_inverse_iterate(u, a, n)
            np.testing.assert_allclose(recovered, q, rtol=2e-11, atol=2e-11)
            np.testing.assert_allclose(np.linalg.det(jac), 1.0, rtol=2e-11, atol=2e-11)


def test_jet_and_potential_derivatives_by_finite_difference():
    q = np.array([0.19, -0.11])
    a = 1.02
    n = 2
    value, gradient, hessian = potential_derivatives(q, a, n)
    step = 2.0e-5

    numerical_gradient = np.empty(2)
    numerical_hessian = np.empty((2, 2))
    for j in range(2):
        direction = np.zeros(2)
        direction[j] = step
        value_plus, gradient_plus, _ = potential_derivatives(q + direction, a, n)
        value_minus, gradient_minus, _ = potential_derivatives(q - direction, a, n)
        numerical_gradient[j] = (value_plus - value_minus) / (2.0 * step)
        numerical_hessian[:, j] = (gradient_plus - gradient_minus) / (2.0 * step)

    assert value > 0.0
    np.testing.assert_allclose(gradient, numerical_gradient, rtol=2e-6, atol=2e-6)
    np.testing.assert_allclose(hessian, numerical_hessian, rtol=2e-6, atol=2e-6)
    np.testing.assert_allclose(hessian, hessian.T, rtol=1e-13, atol=1e-13)


def test_a_zero_is_exact_radial_control_for_every_iterate():
    q = np.array([0.31, -0.47])
    expected = 2.0 * np.pi * np.exp(np.pi * float(q @ q))
    for n in (1, 2, 3, 4):
        value, _, _ = potential_derivatives(q, 0.0, n)
        np.testing.assert_allclose(value, expected, rtol=2e-14, atol=2e-14)


def test_short_orbit_energy_is_finite():
    q = np.array([0.1, -0.2])
    p = np.array([0.3, 0.4])
    assert np.isfinite(hamiltonian_energy(q, p, 1.02, 1))
