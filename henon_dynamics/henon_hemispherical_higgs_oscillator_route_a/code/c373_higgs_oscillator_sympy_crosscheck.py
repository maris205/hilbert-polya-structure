#!/usr/bin/env python3
"""Independent exact symbolic lane for HCS-C373."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c373 SymPy lane refuses optimized Python")

import argparse
import math
from fractions import Fraction

import sympy as s


def main():
    argparse.ArgumentParser().parse_args()
    checks = 0

    radial_action, ell, oscillator_scale, radius_sq = s.symbols(
        "I ell s R2", positive=True
    )
    J = 2 * radial_action + ell + oscillator_scale
    energy = (J**2 - oscillator_scale**2) / (2 * radius_sq)
    A = J**2
    B = 2 * radius_sq * energy + ell**2
    C = ell**2
    discriminant = s.factor(B**2 - 4 * A * C)
    target_discriminant = (
        16 * radial_action * (radial_action + oscillator_scale)
        * (radial_action + ell) * (radial_action + ell + oscillator_scale)
    )
    assert s.factor(discriminant - target_discriminant) == 0
    checks += 1
    assert s.simplify(A - B + C - oscillator_scale**2) == 0
    checks += 1
    assert s.simplify(C / A - (ell / J) ** 2) == 0
    checks += 1
    assert s.simplify((A - B + C) / A - (oscillator_scale / J) ** 2) == 0
    checks += 1
    recovered = J * (1 - ell / J - oscillator_scale / J) / 2
    assert s.simplify(recovered - radial_action) == 0
    checks += 1

    H = ((2 * radial_action + ell + oscillator_scale) ** 2 - oscillator_scale**2) / (2 * radius_sq)
    assert s.simplify(s.diff(H, radial_action) - 2 * J / radius_sq) == 0
    checks += 1
    assert s.simplify(s.diff(H, ell) - J / radius_sq) == 0
    checks += 1
    threshold = oscillator_scale * ell / radius_sq + ell**2 / (2 * radius_sq)
    assert s.factor(H - threshold) == 2 * radial_action * (radial_action + ell + oscillator_scale) / radius_sq
    checks += 1

    # Circular and meridional faces of the turning polynomial.
    circular_J = ell + oscillator_scale
    circular_B = circular_J**2 - oscillator_scale**2 + ell**2
    circular_root = s.simplify(circular_B / (2 * circular_J**2))
    assert s.simplify(circular_root - ell / circular_J) == 0
    checks += 1
    meridional_upper = s.simplify((J**2 - oscillator_scale**2) / J**2)
    assert s.simplify(meridional_upper - (1 - (oscillator_scale / J) ** 2)) == 0
    checks += 1

    # Standard Jacobi ODE, with beta left as the physical symbolic nu.
    x, nu = s.symbols("x nu")
    for degree in range(9):
        for alpha in range(9):
            polynomial = s.jacobi(degree, alpha, nu, x)
            ode = (
                (1 - x**2) * s.diff(polynomial, x, 2)
                + (nu - alpha - (alpha + nu + 2) * x) * s.diff(polynomial, x)
                + degree * (degree + alpha + nu + 1) * polynomial
            )
            assert s.simplify(s.expand_func(ode)) == 0
            checks += 1

    # Direct physical radial Schroedinger checks in units hbar=R=1.
    theta = s.symbols("theta", positive=True)
    for degree in range(3):
        for alpha in range(3):
            for nu_value in (s.Rational(1, 2), s.Rational(3, 2), s.Rational(5, 2)):
                radial = (
                    s.sin(theta) ** alpha
                    * s.cos(theta) ** (nu_value + s.Rational(1, 2))
                    * s.jacobi(degree, alpha, nu_value, s.cos(2 * theta))
                )
                coupling_sq = nu_value**2 - s.Rational(1, 4)
                lhs = -s.Rational(1, 2) * (
                    s.diff(radial, theta, 2)
                    + s.cot(theta) * s.diff(radial, theta)
                    - alpha**2 * radial / s.sin(theta) ** 2
                ) + s.Rational(1, 2) * coupling_sq * s.tan(theta) ** 2 * radial
                k_value = 2 * degree + alpha + 1
                eigenvalue = s.Rational(1, 2) * k_value * (k_value + 2 * nu_value)
                residual = s.trigsimp(s.simplify(s.expand_trig(lhs - eigenvalue * radial)))
                assert residual == 0
                checks += 1

    hbar, omega = s.symbols("hbar omega", positive=True)
    k = s.symbols("k", integer=True, positive=True)
    physical_nu = s.sqrt((omega * radius_sq / hbar) ** 2 + s.Rational(1, 4))
    level_energy = hbar**2 * k * (k + 2 * physical_nu) / (2 * radius_sq)
    assert s.simplify(s.limit(level_energy, radius_sq, s.oo) - hbar * omega * k) == 0
    checks += 1
    zero_coupling = s.simplify(level_energy.subs(omega, 0))
    assert zero_coupling == hbar**2 * k * (k + 1) / (2 * radius_sq)
    checks += 1
    assert sum(level + 1 for level in range(129)) == 8385
    checks += 1

    # Consecutive phase differences and the common phase.
    two_nu = s.symbols("two_nu", real=True)
    spectral_polynomial = k**2 + two_nu * k
    first_difference = s.expand(spectral_polynomial.subs(k, k + 1) - spectral_polynomial)
    assert first_difference == 2 * k + 1 + two_nu
    checks += 1
    assert s.expand(first_difference.subs(k, k + 1) - first_difference) == 2
    checks += 1
    M = s.symbols("M", integer=True, positive=True)
    assert s.expand(M * (1 + two_nu) - (M * (3 + two_nu) - 2 * M)) == 0
    checks += 1

    rational_values = sorted(
        {Fraction(n, d) for d in range(1, 33) for n in range(d, 4 * d + 1)}
    )[:256]
    for value in rational_values:
        gap = 3 + value
        minimum = gap.denominator if gap.numerator % 2 == 0 else 2 * gap.denominator
        assert (minimum * gap).denominator == 1 and (minimum * gap).numerator % 2 == 0
        assert (minimum * (1 + value)).denominator == 1
        assert (minimum * (1 + value)).numerator % 2 == 0
        assert all(
            not ((trial * gap).denominator == 1 and (trial * gap).numerator % 2 == 0)
            for trial in range(1, minimum)
        )
        checks += 4

    nonsquare_count = 0
    candidate = 2
    while nonsquare_count < 256:
        root = math.isqrt(candidate)
        if root * root != candidate:
            assert s.sqrt(candidate).is_rational is False
            nonsquare_count += 1
            checks += 1
        candidate += 1

    print(f"C373 SymPy PASS: exact_symbolic_checks={checks} jacobi_physical_checks=27")


if __name__ == "__main__":
    main()
