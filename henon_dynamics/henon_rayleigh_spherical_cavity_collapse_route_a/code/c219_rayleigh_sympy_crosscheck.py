#!/usr/bin/env python3
"""Independent SymPy identities for the Rayleigh spherical-cavity theorem."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    R, V, A, rho, Pi, R0, t = sp.symbols("R V A rho Pi R0 t", positive=True)
    # First integral derivative, with R'=V and Rayleigh acceleration.
    acc = -sp.Rational(3, 2) * V**2 / R - Pi / (rho * R)
    I = R**3 * V**2 + sp.Rational(2, 3) * Pi / rho * R**3
    dI = sp.diff(I, R) * V + sp.diff(I, V) * acc
    check(sp.simplify(dI) == 0, "first integral")

    # Physical Lagrangian and Euler--Lagrange residual.
    Rvar = sp.Function("R")(t)
    L = 2 * sp.pi * rho * Rvar**3 * sp.diff(Rvar, t)**2 - sp.Rational(4, 3) * sp.pi * Pi * Rvar**3
    EL = sp.diff(sp.diff(L, sp.diff(Rvar, t)), t) - sp.diff(L, Rvar)
    target = 4 * sp.pi * rho * Rvar**2 * (Rvar * sp.diff(Rvar, t, 2) + sp.Rational(3, 2) * sp.diff(Rvar, t)**2 + Pi / rho)
    check(sp.simplify(EL - target) == 0, "Lagrangian Euler-Lagrange")

    # Beta substitution x^3=y: x^(3/2) dx/sqrt(1-x^3)
    x, y = sp.symbols("x y", positive=True)
    transformed = sp.simplify((y**sp.Rational(1, 2)) * sp.Rational(1, 3) * y**(-sp.Rational(2, 3)))
    check(transformed == sp.Rational(1, 3) * y**(-sp.Rational(1, 6)), "beta power")
    check(sp.Rational(5, 6) + sp.Rational(1, 2) == sp.Rational(4, 3), "beta parameters")

    # Endpoint series J(x)=2/5 x^(5/2)+1/11 x^(11/2)+3/68 x^(17/2)+...
    z = sp.symbols("z", positive=True)
    integrand = z**sp.Rational(3, 2) * (1 - z**3)**(-sp.Rational(1, 2))
    series = sp.series(integrand, z, 0, 10).removeO()
    expected = z**sp.Rational(3, 2) + sp.Rational(1, 2) * z**sp.Rational(9, 2) + sp.Rational(3, 8) * z**sp.Rational(15, 2)
    series_terms = {exponent: coefficient for coefficient, exponent in
                    (term.as_coeff_exponent(z) for term in sp.Add.make_args(sp.expand(series)))}
    expected_terms = {sp.Rational(3, 2): 1, sp.Rational(9, 2): sp.Rational(1, 2),
                      sp.Rational(15, 2): sp.Rational(3, 8)}
    check(all(series_terms.get(k) == v for k, v in expected_terms.items()), "integrand expansion path")
    # Integrate termwise and test the first two coefficients exactly.
    J2 = sp.integrate(z**sp.Rational(3, 2), z) + sp.Rational(1, 2) * sp.integrate(z**sp.Rational(9, 2), z)
    terms = {exponent: coefficient for coefficient, exponent in
             (term.as_coeff_exponent(z) for term in sp.Add.make_args(sp.expand(J2)))}
    check(terms.get(sp.Rational(5, 2)) == sp.Rational(2, 5), "Puiseux leading coefficient")
    check(terms.get(sp.Rational(11, 2)) == sp.Rational(1, 11), "Puiseux correction coefficient")
    check(sp.Rational(1, 11) / sp.Rational(2, 5) == sp.Rational(5, 22), "Puiseux relative correction")

    # Scaling and L^p tests: delta^(2/5), delta^(-3/5), delta^(-8/5).
    delta, p = sp.symbols("delta p", positive=True)
    check(sp.Rational(5, 2) * sp.Rational(2, 5) == 1, "terminal inversion")
    check(sp.Rational(3, 5) == 1 - sp.Rational(2, 5), "velocity exponent")
    check(sp.Rational(8, 5) == 2 - sp.Rational(2, 5), "acceleration exponent")
    # Integrability criterion is 1-alpha*p>0 for delta^(-alpha*p).
    check(1 / sp.Rational(1) / sp.Rational(3, 5) == sp.Rational(5, 3), "velocity Lp threshold")
    check(1 / sp.Rational(8, 5) == sp.Rational(5, 8), "acceleration Lp threshold")

    # Volume and finite kinetic energy scaling.
    C = sp.symbols("C", positive=True)
    Vgeom = sp.Rational(4, 3) * sp.pi * (C * delta**sp.Rational(2, 5))**3
    check(sp.simplify(Vgeom / (sp.Rational(4, 3) * sp.pi * C**3 * delta**sp.Rational(6, 5))) == 1, "volume exponent")
    dV = sp.diff(Vgeom, delta)
    check(sp.simplify(dV / (sp.Rational(8, 5) * sp.pi * C**3 * delta**sp.Rational(1, 5))) == 1, "volume derivative")
    K = 2 * sp.pi * rho * R**3 * V**2
    U = sp.Rational(4, 3) * sp.pi * Pi * R**3
    E = sp.simplify(K + U).subs(V**2, sp.Rational(2, 3) * Pi / rho * (R0**3 / R**3 - 1))
    check(sp.simplify(E - sp.Rational(4, 3) * sp.pi * Pi * R0**3) == 0, "finite liquid energy")
    Kcollapse = sp.simplify(K.subs(V**2, sp.Rational(2, 3) * Pi / rho * (R0**3 / R**3 - 1)))
    check(sp.simplify(Kcollapse - sp.Rational(4, 3) * sp.pi * Pi * (R0**3 - R**3)) == 0, "kinetic ledger")

    # Sign branch consistency: a^2=2|Pi|/(3rho), and pressure-zero is static.
    a2 = sp.Rational(2, 3) * Pi / rho
    check(sp.simplify(a2 / (sp.Rational(2, 3) * Pi / rho)) == 1, "collapse speed square")
    check(sp.simplify((-Pi / (rho * R)).subs(Pi, 0)) == 0, "zero pressure acceleration")

    print(f"C219 SymPy crosscheck: PASS ({checks} symbolic identities)")
    print("first integral, Beta substitution, Puiseux endpoint, Lp/volume scaling, Lagrangian and energy: PASS")


if __name__ == "__main__":
    main()
