"""Exact algebra checks used by the R300-P1 proof package.

These tests verify identities and constants, not the analytic domination
arguments in the Brownian-bridge proof.
"""

import sympy as sp


def test_henon_displacement_identity() -> None:
    a, r, u, v, xi, eta = sp.symbols("a r u v xi eta")
    x = v + xi
    y = -2 * a * r * v - a * v**2 - u + eta
    transformed = sp.Matrix((-2 * a * r * x - a * x**2 - y, x))
    expected = sp.Matrix(
        (
            u - 2 * a * (r + v) * xi - a * xi**2 - eta,
            v + xi,
        )
    )
    assert sp.simplify(transformed - expected) == sp.zeros(2, 1)


def test_log_potential_derivatives_stop_at_order_four() -> None:
    a, r, x, y = sp.symbols("a r x y")
    phi = sp.pi * (x**2 + (2 * a * r * x + a * x**2 + y) ** 2)

    assert sp.diff(phi, x, 4) == 24 * sp.pi * a**2
    assert sp.diff(phi, x, 2, y) == 4 * sp.pi * a
    assert sp.diff(phi, x, 5) == 0
    assert sp.diff(phi, x, 4, y) == 0
    assert sp.diff(phi, y, 3) == 0


def test_brownian_bridge_second_moments() -> None:
    s, r = sp.symbols("s r", nonnegative=True)
    covariance_left = r * (1 - s)  # min(s,r)-sr on 0 <= r <= s <= 1
    integrated_mean = 2 * sp.integrate(
        sp.integrate(covariance_left, (r, 0, s)),
        (s, 0, 1),
    )
    integrated_diagonal = sp.integrate(s * (1 - s), (s, 0, 1))

    assert integrated_mean == sp.Rational(1, 12)
    assert integrated_diagonal == sp.Rational(1, 6)


def test_integrated_second_order_coefficient() -> None:
    t, pi_symbol = sp.symbols("t pi_symbol", positive=True)
    gradient_coefficient = t**2 / (48 * pi_symbol)
    laplacian_coefficient_after_parts = -t**2 / (24 * pi_symbol)
    assert sp.simplify(
        gradient_coefficient + laplacian_coefficient_after_parts
    ) == -t**2 / (48 * pi_symbol)

