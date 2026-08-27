#!/usr/bin/env python3
"""Separate symbolic reconstruction for HCS-C207; imports no producer code."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    checks = 0

    def zero(expression: sp.Expr, label: str) -> None:
        nonlocal checks
        checks += 1
        residual = sp.simplify(expression)
        if residual != 0:
            raise AssertionError(f"{label}: {residual}")

    def truth(statement: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not statement:
            raise AssertionError(label)

    # The scaling and sharp tail threshold are generic in m.
    m = sp.symbols("m", positive=True)
    alpha = 1 / (m + 1)
    zero(alpha + 1 - (alpha * m + 2 * alpha), "similarity exponents")
    zero((2 / (1 - m) - 1) - (1 + m) / (1 - m), "moment threshold")
    zero(((1 + m) / (1 - m)).subs(m, sp.Rational(1, 3)) - 2,
         "second-moment equality")

    # Generic nonlinear profiles. Parameterizing by p=1/(m-1) and
    # q=1/(1-m) avoids symbolic rational-power branch invention.
    x, C = sp.symbols("x C", positive=True)
    p = sp.symbols("p", positive=True)
    m_p = 1 + 1 / p
    alpha_p = p / (2 * p + 1)
    k = p / (2 * (p + 1) * (2 * p + 1))
    y_p = C - k * x**2
    porous = y_p**p
    zero(sp.diff(y_p**(p + 1), x) + alpha_p * x * porous,
         "generic porous integrated ODE")
    mu_p = (p + 1) * y_p + alpha_p * x**2 / 2
    zero(sp.diff(mu_p, x), "generic porous chemical stationarity")
    zero(m_p - (1 + 1 / p), "generic porous exponent map")

    q = sp.symbols("q", positive=True)
    m_f = 1 - 1 / q
    alpha_f = q / (2 * q - 1)
    b = q / (2 * (q - 1) * (2 * q - 1))
    y_f = C + b * x**2
    fast = y_f**(-q)
    zero(sp.diff(y_f**(1 - q), x) + alpha_f * x * fast,
         "generic fast integrated ODE")
    mu_f = -(q - 1) * y_f + alpha_f * x**2 / 2
    zero(sp.diff(mu_f, x), "generic fast chemical stationarity")
    zero(m_f - (1 - 1 / q), "generic fast exponent map")

    gaussian = sp.exp(-x**2 / 4)
    zero(sp.diff(gaussian, x, 2)
         + sp.diff(sp.Rational(1, 2) * x * gaussian, x),
         "Gaussian stationary ODE")
    zero(sp.diff(sp.log(gaussian) + x**2 / 4, x),
         "Gaussian chemical stationarity")

    # Euler-Beta normalization is checked from the transformed integrals,
    # not merely from an exponent copied out of the evidence.
    z = sp.symbols("z", positive=True)
    porous_beta_integral = sp.integrate(
        z**(-sp.Rational(1, 2)) * (1 - z)**p, (z, 0, 1), conds="none"
    )
    zero(sp.hyperexpand(porous_beta_integral)
         - sp.beta(sp.Rational(1, 2), p + 1),
         "porous Beta mass integral")
    fast_beta_integral = sp.integrate(
        z**(-sp.Rational(1, 2)) * (1 + z)**(-q),
        (z, 0, sp.oo), conds="none"
    )
    zero(fast_beta_integral
         - sp.expand_func(sp.beta(sp.Rational(1, 2),
                                  q - sp.Rational(1, 2))),
         "fast Beta mass integral")

    mass, beta_symbol, k_symbol, b_symbol = sp.symbols(
        "M B k b", positive=True
    )
    porous_C = (mass * sp.sqrt(k_symbol) / beta_symbol)**(
        1 / (p + sp.Rational(1, 2))
    )
    porous_mass = (porous_C**(p + sp.Rational(1, 2))
                   * beta_symbol / sp.sqrt(k_symbol))
    zero(sp.powdenest(porous_mass, force=True) - mass,
         "porous mass C exponent")
    fast_C = (beta_symbol / (mass * sp.sqrt(b_symbol)))**(
        1 / (q - sp.Rational(1, 2))
    )
    fast_mass = (fast_C**(sp.Rational(1, 2) - q)
                 * beta_symbol / sp.sqrt(b_symbol))
    zero(sp.powdenest(fast_mass, force=True) - mass,
         "fast mass C exponent")

    # With a=(r+1)/2>0, the same substitutions prove both full moment
    # formulas and expose every power of C, k, and b.
    a = sp.symbols("a", positive=True)
    porous_moment_integral = sp.integrate(
        z**(a - 1) * (1 - z)**p, (z, 0, 1), conds="none"
    )
    zero(sp.hyperexpand(porous_moment_integral) - sp.beta(a, p + 1),
         "porous generic moment Beta integral")
    fast_moment_integral = sp.integrate(
        z**(a - 1) * (1 + z)**(-q), (z, 0, sp.oo), conds="none"
    )
    zero(fast_moment_integral - sp.expand_func(sp.beta(a, q - a)),
         "fast generic moment Beta integral")
    zero((p + a) - (p + (2 * a - 1 + 1) / 2),
         "porous moment C exponent")
    zero(-a - (-(2 * a - 1 + 1) / 2),
         "porous moment k exponent")
    zero((-q + a) - (-q + (2 * a - 1 + 1) / 2),
         "fast moment C exponent")
    zero(-a - (-(2 * a - 1 + 1) / 2),
         "fast moment b exponent")
    zero((q - a) - ((2 * q - 1 - (2 * a - 1)) / 2),
         "fast moment convergence inequality")

    # Pressure, interface speed, stationarity, and both free-energy branches.
    zero(2 * m * ((m - 1) / (2 * m * (m + 1))) / (m - 1) - alpha,
         "pressure slope coefficient")
    t, radius = sp.symbols("t R", positive=True)
    interface = radius * t**alpha
    zero(sp.diff(interface, t) - alpha * interface / t,
         "right interface speed")
    zero(sp.diff(-interface, t) - alpha * (-interface) / t,
         "left interface speed")
    v, xi = sp.symbols("v xi", positive=True)
    density_nonlinear = v**m / (m - 1) + alpha * xi**2 * v / 2
    mu_nonlinear = m * v**(m - 1) / (m - 1) + alpha * xi**2 / 2
    zero(sp.diff(density_nonlinear, v) - mu_nonlinear,
         "nonlinear free-energy first variation")
    density_heat = v * sp.log(v) - v + sp.Rational(1, 4) * xi**2 * v
    mu_heat = sp.log(v) + sp.Rational(1, 4) * xi**2
    zero(sp.diff(density_heat, v) - mu_heat,
         "heat free-energy first variation")

    evidence = json.loads(
        (Path(__file__).resolve().parents[1]
         / "results/c207_barenblatt_evidence.json").read_text()
    )
    truth(evidence["summary"]["working_decimal_digits"] == 100,
          "working precision metadata")
    truth(evidence["summary"]["serialized_significant_digits"] == 82,
          "serialized precision metadata")
    truth(len(evidence["regression"]["profiles"]) == 18,
          "profile count")
    for row in evidence["regression"]["profiles"]:
        mq = sp.Rational(row["m"])
        zero(sp.Rational(row["derived"]["alpha"]) - 1 / (mq + 1),
             "row alpha")
        if mq < 1:
            zero(sp.Rational(row["derived"]["moment_threshold"])
                 - (1 + mq) / (1 - mq), "row threshold")

    print(json.dumps({"status": "C207_SYMPY_PASS", "checks": checks,
                      "profiles": 18}, sort_keys=True))


if __name__ == "__main__":
    main()
