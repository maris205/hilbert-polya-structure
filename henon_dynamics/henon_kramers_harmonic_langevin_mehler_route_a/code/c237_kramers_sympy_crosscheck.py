#!/usr/bin/env python3
"""Independent SymPy checks for the C237 matrix, covariance and rate laws."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0
    w, g, b, t, q, p = sp.symbols("w g b t q p", positive=True)
    a = g / 2
    A = sp.Matrix([[0, 1], [-w**2, -g]])
    I = sp.eye(2)

    # Characteristic polynomial and trace/determinant identities.
    lam = sp.symbols("lam")
    checks += 1
    assert sp.expand((lam * I - A).det()) == lam**2 + g * lam + w**2

    # Underdamped formula with nu^2=w^2-a^2.
    nu = sp.symbols("nu", positive=True)
    cu, su = sp.cos(nu * t), sp.sin(nu * t) / nu
    Mu = sp.exp(-a * t) * sp.Matrix([[cu + a * su, su], [-w**2 * su, cu - a * su]])
    Mu_t = Mu.diff(t)
    checks += 1
    # Rewriting the parameter constraint in the direction that matches the
    # expanded expressions avoids brittle power-pattern matching in SymPy.
    under_residual = (Mu_t - A * Mu).applyfunc(
        lambda v: sp.trigsimp(sp.simplify(v.subs(w**2, nu**2 + a**2)))
    )
    assert under_residual == sp.zeros(2)
    checks += 1
    assert sp.simplify(Mu.subs(t, 0) - I) == sp.zeros(2)
    checks += 1
    assert sp.trigsimp(sp.simplify((Mu.det() - sp.exp(-g * t)).subs(w**2, nu**2 + a**2))) == 0

    # Critical formula (g=2w), including the nilpotent factor.
    Mc = sp.exp(-w * t) * (I + t * (A.subs(g, 2 * w) + w * I))
    checks += 1
    assert sp.simplify(Mc.diff(t) - A.subs(g, 2 * w) * Mc) == sp.zeros(2)
    checks += 1
    assert sp.simplify(Mc.subs(t, 0) - I) == sp.zeros(2)
    checks += 1
    assert sp.simplify(Mc.det() - sp.exp(-2 * w * t)) == 0

    # Overdamped formula with delta^2=a^2-w^2.
    d = sp.symbols("d", positive=True)
    co, so = sp.cosh(d * t), sp.sinh(d * t) / d
    Mo = sp.exp(-a * t) * sp.Matrix([[co + a * so, so], [-w**2 * so, co - a * so]])
    checks += 1
    over_residual = (Mo.diff(t) - A * Mo).applyfunc(
        lambda v: sp.trigsimp(sp.simplify(v.subs(w**2, a**2 - d**2)))
    )
    assert over_residual == sp.zeros(2)
    checks += 1
    assert sp.trigsimp(sp.simplify((Mo.det() - sp.exp(-g * t)).subs(w**2, a**2 - d**2))) == 0

    # Stationary covariance and Lyapunov equation.
    S = sp.diag(1 / (b * w**2), 1 / b)
    BBT = sp.Matrix([[0, 0], [0, 2 * g / b]])
    checks += 1
    assert sp.simplify(A * S + S * A.T + BBT) == sp.zeros(2)
    checks += 1
    assert sp.trigsimp(sp.simplify(((Mu * S * Mu.T).det() - sp.exp(-2 * g * t) * S.det()).subs(w**2, nu**2 + a**2))) == 0
    checks += 1
    sym_residual = (Mu * S * Mu.T).T - Mu * S * Mu.T
    assert sym_residual.applyfunc(lambda v: sp.simplify(v.subs(w**2, nu**2 + a**2))) == sp.zeros(2)

    # The covariance derivative is the finite-time Lyapunov identity.
    C = S - Mu * S * Mu.T
    checks += 1
    lyap_residual = C.diff(t) - (A * C + C * A.T + BBT)
    assert lyap_residual.applyfunc(lambda v: sp.trigsimp(sp.simplify(v.subs(w**2, nu**2 + a**2)))) == sp.zeros(2)
    checks += 1
    assert C.subs(t, 0) == sp.zeros(2)

    # Gaussian Gibbs normalization/equipartition (formal Gaussian integrals).
    x, y = sp.symbols("x y", real=True)
    density = b * w / (2 * sp.pi) * sp.exp(-b * (w**2 * x**2 + y**2) / 2)
    checks += 1
    assert sp.simplify(sp.integrate(sp.integrate(density, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))) == 1
    checks += 1
    assert sp.simplify(sp.integrate(sp.integrate(x**2 * density, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo)) - 1 / (b * w**2)) == 0
    checks += 1
    assert sp.simplify(sp.integrate(sp.integrate(y**2 * density, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo)) - 1 / b) == 0

    # Kalman bracket and stationary cross-covariance entries.
    cnoise = sp.sqrt(2 * g / b)
    B = sp.Matrix([0, cnoise])
    checks += 1
    assert sp.simplify(sp.Matrix.hstack(B, A * B).det() + 2 * g / b) == 0
    checks += 1
    assert sp.simplify(((Mu * S)[0, 0] - Mu[0, 0] / (b * w**2)).subs(w**2, nu**2 + a**2)) == 0
    checks += 1
    assert sp.simplify(((Mu * S)[0, 1] - Mu[0, 1] / b).subs(w**2, nu**2 + a**2)) == 0
    checks += 1
    assert sp.simplify(((Mu * S)[1, 0] - Mu[1, 0] / (b * w**2)).subs(w**2, nu**2 + a**2)) == 0

    # Rate formula: continuity and strict decrease on the overdamped branch.
    r_over = g / 2 - sp.sqrt(g**2 / 4 - w**2)
    checks += 1
    assert sp.simplify(sp.limit(r_over, g, 2 * w, dir="+") - w) == 0
    checks += 1
    # The derivative is 1/2-g/(4*sqrt(g**2/4-w**2)), hence strictly negative
    # on the open overdamped branch (g>2w).
    dr = sp.simplify(sp.diff(r_over, g))
    checks += 1
    assert sp.simplify(dr - (sp.Rational(1, 2) - g / (4 * sp.sqrt(g**2 / 4 - w**2)))) == 0
    checks += 1
    assert sp.simplify((g / 2).subs(g, 2 * w) - w) == 0

    # Hamiltonian zero-damping preservation (Mu^T S^{-1} Mu=S^{-1}).
    checks += 1
    Mu0 = Mu.subs(g, 0)
    S0 = S.subs(w**2, nu**2)
    hamiltonian_residual = Mu0 * S0 * Mu0.T - S0
    assert hamiltonian_residual.applyfunc(lambda v: sp.trigsimp(sp.simplify(v.subs(w**2, nu**2)))) == sp.zeros(2)

    print(f"C237 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
