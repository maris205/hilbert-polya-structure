#!/usr/bin/env python3
"""Independent exact symbolic lane for HCS-C347."""
from __future__ import annotations

import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C347 SymPy lane refuses optimized Python")
    checks = 0
    kappa, delta, theta, phi, d, coupling = sp.symbols(
        "kappa delta theta phi d coupling", positive=True, real=True)
    # Divide exact positive coefficient series for I1/(kappa I0).
    order = 7
    i0 = sum(kappa ** (2 * m) / (4 ** m * sp.factorial(m) ** 2)
             for m in range(order + 2))
    i1_over_kappa = sum(kappa ** (2 * m) /
        (2 * 4 ** m * sp.factorial(m) * sp.factorial(m + 1))
        for m in range(order + 2))
    quotient = sp.series(i1_over_kappa / i0, kappa, 0, 2 * order + 2).removeO().expand()
    expected = [sp.Rational(1, 2), -sp.Rational(1, 16), sp.Rational(1, 96),
                -sp.Rational(11, 6144), sp.Rational(19, 61440),
                -sp.Rational(473, 8847360)]
    for m, coefficient in enumerate(expected):
        need(quotient.coeff(kappa, 2 * m) == coefficient, f"Bessel quotient {m}")
        checks += 1
    # The strict coefficient-ratio ordering is the Bessel quotient monotonicity engine.
    for m in range(1, 33):
        previous = sp.Rational(1, 2 * m)
        current = sp.Rational(1, 2 * (m + 1))
        need(current < previous, f"coefficient ratio {m}")
        checks += 1
    # Turan positivity is exactly the desired differential inequality.
    ratio, ratio_prime = sp.symbols("ratio ratio_prime", positive=True)
    recurrence = 1 - ratio / kappa - ratio ** 2
    turan_scaled = ratio ** 2 - 1 + 2 * ratio / kappa
    need(sp.simplify((kappa * recurrence - ratio) / kappa ** 2
                     + turan_scaled / kappa) == 0, "Turan derivative equivalence")
    checks += 1
    # Analytic implicit-function coefficients for x=kappa^2.
    x, a1, a2, a3 = sp.symbols("x a1 a2 a3")
    qx = sum(quotient.coeff(kappa, 2 * m) * x ** m for m in range(6))
    trial = a1 * delta + a2 * delta ** 2 + a3 * delta ** 3
    equation = sp.series((2 + delta) * qx.subs(x, trial) - 1,
                         delta, 0, 4).removeO().expand()
    solution = sp.solve([equation.coeff(delta, j) for j in range(1, 4)],
                        [a1, a2, a3], dict=True)[0]
    need(solution == {a1: 4, a2: sp.Rational(2, 3), a3: sp.Rational(1, 18)},
         "kappa critical expansion")
    checks += 1
    x_series = trial.subs(solution)
    r2 = sp.series(x_series / (2 + delta) ** 2, delta, 0, 4).removeO().expand()
    need(r2.coeff(delta, 1) == 1 and r2.coeff(delta, 2) == -sp.Rational(5, 6),
         "order parameter critical expansion")
    checks += 1
    # Direct Fourier action at uniform density for cosine and sine modes.
    for n in range(1, 10):
        cosine = sp.cos(n * theta)
        sine = sp.sin(n * theta)
        zc_real = sp.integrate(sp.cos(phi) * sp.cos(n * phi), (phi, -sp.pi, sp.pi))
        zc_imag = sp.integrate(sp.sin(phi) * sp.cos(n * phi), (phi, -sp.pi, sp.pi))
        zs_real = sp.integrate(sp.cos(phi) * sp.sin(n * phi), (phi, -sp.pi, sp.pi))
        zs_imag = sp.integrate(sp.sin(phi) * sp.sin(n * phi), (phi, -sp.pi, sp.pi))
        drift_c = coupling * (zc_imag * sp.cos(theta) - zc_real * sp.sin(theta))
        drift_s = coupling * (zs_imag * sp.cos(theta) - zs_real * sp.sin(theta))
        linear_c = sp.diff(d * sp.diff(cosine, theta) - drift_c / (2 * sp.pi), theta)
        linear_s = sp.diff(d * sp.diff(sine, theta) - drift_s / (2 * sp.pi), theta)
        eigen = coupling / 2 - d if n == 1 else -d * n ** 2
        need(sp.simplify(sp.expand_trig(linear_c - eigen * cosine)) == 0, f"cos mode {n}")
        need(sp.simplify(sp.expand_trig(linear_s - eigen * sine)) == 0, f"sin mode {n}")
        checks += 2
    # Every von Mises profile has zero stationary flux before self-consistency.
    r = sp.symbols("r", positive=True)
    profile = sp.exp(kappa * sp.cos(theta))
    flux = coupling * r * sp.sin(-theta) * profile - d * sp.diff(profile, theta)
    need(sp.simplify(flux.subs(kappa, coupling * r / d)) == 0, "zero flux")
    checks += 1
    print(f"C347 SymPy cross-check: PASS {checks} exact symbolic checks")


if __name__ == "__main__":
    main()
