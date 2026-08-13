import numpy as np
import pytest

from symplectic_henon.model import HenonHomotopy, OMEGA


def test_step_jacobian_and_determinant() -> None:
    model = HenonHomotopy(a=1.7, rho=0.35)
    point = np.array([0.23, -0.41])
    assert np.allclose(model.step(point), [1.0 - 1.7 * 0.23**2 + 0.35 * 0.41, 0.23])

    epsilon = 1e-7
    finite_difference = np.column_stack(
        [
            (model.step(point + epsilon * np.eye(2)[axis]) - model.step(point - epsilon * np.eye(2)[axis]))
            / (2.0 * epsilon)
            for axis in range(2)
        ]
    )
    assert np.allclose(model.jacobian(point), finite_difference, atol=1e-9)
    assert np.isclose(np.linalg.det(model.jacobian(point)), model.rho)
    assert model.jacobian_determinant() == model.rho
    assert np.allclose(model.conformal_symplectic_defect(point), np.zeros((2, 2)))
    assert np.allclose(model.jacobian(point).T @ OMEGA @ model.jacobian(point), model.rho * OMEGA)


def test_monodromy_determinant() -> None:
    model = HenonHomotopy(a=1.2, rho=0.73)
    points = model.iterate([0.1, -0.2], 5)[:-1]
    monodromy = model.monodromy(points)
    assert np.isclose(np.linalg.det(monodromy), model.rho**5, rtol=1e-11, atol=1e-12)
    assert model.monodromy_determinant(5) == model.rho**5


def test_generating_function_reproduces_symplectic_map() -> None:
    model = HenonHomotopy(a=1.5436890126920763, rho=1.0)
    q, p = 0.19, -0.31
    Q, P = model.step([q, p])
    assert np.isclose(P, q)
    # Analytic derivatives of S=qQ-q+(a/3)q^3.
    minus_dS_dq = 1.0 - Q - model.a * q * q
    dS_dQ = q
    assert np.isclose(p, minus_dS_dq)
    assert np.isclose(P, dS_dQ)

    q_cycle = np.array([-0.4, 0.2, 0.7])
    expected = np.sum(q_cycle * np.roll(q_cycle, -1) - q_cycle + model.a * q_cycle**3 / 3.0)
    assert np.isclose(model.periodic_action(q_cycle), expected)


def test_generating_function_refuses_non_symplectic_member() -> None:
    with pytest.raises(ValueError):
        HenonHomotopy(a=1.0, rho=0.9).generating_function(0.1, 0.2)


def test_fixed_points_satisfy_map() -> None:
    model = HenonHomotopy(a=6.0, rho=1.0)
    fixed = model.fixed_points()
    assert fixed.shape == (2, 2)
    for point in fixed:
        assert np.allclose(model.step(point), point)
