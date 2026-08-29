#!/usr/bin/env python3
"""Independent symbolic checks for the Duffing atlas."""
from __future__ import annotations
import sympy as sp


def main() -> None:
    x, v, delta, beta, alpha, t, E, y = sp.symbols("x v delta beta alpha t E y", positive=True)
    checks = 0

    def ok(expr, label):
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.simplify(expr)))

    V = delta*x**2/2 + beta*x**4/4
    H = v**2/2 + V
    ok(sp.diff(H, x)*v + sp.diff(H, v)*(-delta*x-beta*x**3), "Hamiltonian conservation")
    ok(sp.expand((beta/4)*(x**2+delta/beta)**2 - (delta*x**2/2+beta*x**4/4+delta**2/(4*beta))), "double-well factor")
    ok(sp.expand(beta*y**2/4 + delta*y/2 - E - (beta*x**4/4+delta*x**2/2-E).subs(x**2,y)), "turning quadratic")

    # Exact homoclinic profile on delta=-alpha^2.
    profile = sp.sqrt(2)*alpha/sp.sqrt(beta) * sp.sech(alpha*t)
    residual = sp.diff(profile, t, 2) - alpha**2*profile + beta*profile**3
    ok(sp.trigsimp(residual), "homoclinic residual")
    ok(sp.simplify(sp.diff(profile, t).subs(t, 0)), "homoclinic central velocity")

    # Equilibrium Hessians and linear rates.
    ok(sp.diff(V, x, 2).subs(x, 0) - delta, "origin Hessian")
    well = sp.sqrt(-delta/beta)
    ok(sp.simplify(sp.diff(V, x, 2).subs(x, well) + 2*delta), "well Hessian")
    lam = sp.symbols("lam")
    lin = sp.Matrix([[0, 1], [-delta, 0]])
    ok(sp.expand(lin.charpoly(lam).as_expr() - (lam**2 + delta)), "center characteristic")

    # Reversibility and quartic scaling substitution x=E^(1/4) beta^(-1/4) u.
    u = sp.symbols("u", real=True)
    scale = E**sp.Rational(1,4) * beta**(-sp.Rational(1,4))
    quartic = (beta*(scale*u)**4/4)/E
    ok(sp.simplify(quartic-u**4/4), "quartic scale")
    # The action integrand differentiates to the period integrand away from
    # endpoints (the endpoint terms vanish by the square-root factor).
    integrand = sp.sqrt(2*(E-(delta*x**2/2+beta*x**4/4))) / sp.pi
    ok(sp.simplify(sp.diff(integrand, E) - 1/(sp.pi*sp.sqrt(2*(E-(delta*x**2/2+beta*x**4/4))))), "action derivative integrand")

    print(f"C232 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__": main()
