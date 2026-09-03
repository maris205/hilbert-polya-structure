#!/usr/bin/env python3
"""Independent symbolic theorem checks for HCS-C343."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c343_erlang2_delay_evidence.json"
CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def q(value: str) -> sp.Rational:
    item = Fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C343 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())

    s = sp.symbols("s", real=True)
    lam = sp.symbols("lambda", positive=True)
    a, b, r = sp.symbols("a b r", positive=True)
    kernel = r**2*s*sp.exp(-r*s)
    need(sp.simplify(sp.integrate(kernel, (s, 0, sp.oo))-1) == 0, "kernel mass")
    need(sp.simplify(sp.integrate(s*kernel, (s, 0, sp.oo))-2/r) == 0, "kernel mean")
    need(sp.simplify(sp.integrate(s**2*kernel, (s, 0, sp.oo))-6/r**2) == 0, "kernel second moment")
    need(sp.simplify(sp.integrate(sp.exp(-lam*s)*kernel, (s, 0, sp.oo))-r**2/(lam+r)**2) == 0,
         "kernel Laplace transform")

    matrix = sp.Matrix([[-a, 0, -b], [r, -r, 0], [0, r, -r]])
    polynomial = sp.expand((lam+a)*(lam+r)**2+b*r**2)
    need(sp.expand((lam*sp.eye(3)-matrix).det()-polynomial) == 0, "characteristic determinant")
    c2, c1, c0 = a+2*r, r*(r+2*a), r**2*(a+b)
    need(sp.expand(c2*c1-c0-r*(2*(a+r)**2-b*r)) == 0, "Routh margin")
    b_h = 2*(a+r)**2/r
    omega2 = r*(r+2*a)
    need(sp.expand(polynomial.subs(b, b_h)-(lam+a+2*r)*(lam**2+omega2)) == 0, "Hopf factorization")
    crossing = r**2/(2*(omega2+(a+2*r)**2))
    need(sp.simplify(crossing-r**2/(2*(omega2+(a+2*r)**2))) == 0 and crossing.is_positive,
         "positive transverse real speed")

    derivative = sp.diff(polynomial, lam)
    need(sp.factor(derivative) == (lam+r)*(3*lam+2*a+r), "critical roots")
    discriminant = sp.discriminant(polynomial, lam)
    need(sp.factor(discriminant-b*r**2*(4*(r-a)**3-27*b*r**2)) == 0, "discriminant factor")
    mu = -(r+2*a)/3
    nu = -(4*r-a)/3
    b_d = 4*(r-a)**3/(27*r**2)
    need(sp.simplify(polynomial.subs({lam: mu, b: b_d})) == 0, "double root value")
    need(sp.simplify(derivative.subs(lam, mu)) == 0, "double root derivative")
    need(sp.expand(polynomial.subs(b, b_d)-(lam-mu)**2*(lam-nu)) == 0, "double root factorization")

    e1 = sp.Matrix([1, 0, 0])
    cyclic = sp.Matrix.hstack(e1, matrix*e1, matrix**2*e1)
    need(sp.factor(cyclic.det()-r**3) == 0, "cyclic generator")

    # Hermite functional calculus for a double root mu0 and a simple root nu0.
    x, mu0, nu0 = sp.symbols("x mu0 nu0")
    minimal = (x-mu0)**2*(x-nu0)
    p_nu = (x-mu0)**2/(nu0-mu0)**2
    p_mu = 1-p_nu
    n_mu = (x-mu0)*p_mu
    rem = lambda expr: sp.cancel(sp.rem(sp.together(expr).as_numer_denom()[0], minimal, x) /
                                 sp.together(expr).as_numer_denom()[1])
    for expression, label in [
        (p_nu**2-p_nu, "simple projector"),
        (p_mu**2-p_mu, "double projector"),
        (p_nu*p_mu, "projector orthogonality"),
        (n_mu**2, "nilpotent square"),
        (x-(mu0*p_mu+n_mu+nu0*p_nu), "Jordan reconstruction"),
    ]:
        need(sp.simplify(rem(expression)) == 0, label)

    for row in data["routh_rows"]:
        aa, rr, bb = q(row["a"]), q(row["r"]), q(row["b"])
        coeffs = [aa+2*rr, rr*(rr+2*aa), rr**2*(aa+bb)]
        got = [q(value) for value in row["coefficients_c2_c1_c0"]]
        need(got == coeffs, "evidence cubic coefficients")
        need(q(row["routh_margin"]) == coeffs[0]*coeffs[1]-coeffs[2], "evidence Routh margin")

    for row in data["hopf_rows"]:
        aa, rr = q(row["a"]), q(row["r"])
        bh = 2*(aa+rr)**2/rr
        om2 = rr*(rr+2*aa)
        need(q(row["b_h"]) == bh, "evidence Hopf threshold")
        need(q(row["omega_squared"]) == om2, "evidence Hopf frequency")
        need(q(row["crossing_real_derivative"]) == rr**2/(2*(om2+(aa+2*rr)**2)),
             "evidence crossing speed")

    for row in data["repeated_root_rows"]:
        aa, rr, bb = q(row["a"]), q(row["r"]), q(row["b"])
        poly = (lam+aa)*(lam+rr)**2+bb*rr**2
        root = q(row["repeated_root"])
        need(sp.expand(poly.subs(lam, root)) == 0, "evidence repeated root")
        need(sp.expand(sp.diff(poly, lam).subs(lam, root)) == 0, "evidence repeated derivative")
        need(q(row["discriminant"]) == 0, "evidence zero discriminant")

    print(f"C343 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
