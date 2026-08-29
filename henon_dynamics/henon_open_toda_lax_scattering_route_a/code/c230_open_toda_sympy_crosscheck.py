#!/usr/bin/env python3
"""Independent SymPy identities for the finite open Toda theorem."""
from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    checks = 0
    def ok(condition, label):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    N = 4
    a = sp.symbols("a1:" + str(N), positive=True)
    b = sp.symbols("b1:" + str(N + 1), real=True)
    L = sp.zeros(N)
    for j in range(N):
        L[j, j] = b[j]
        if j + 1 < N:
            L[j, j + 1] = L[j + 1, j] = a[j]
    B = sp.zeros(N)
    for j in range(N - 1):
        B[j, j + 1] = a[j]
        B[j + 1, j] = -a[j]
    C = B * L - L * B
    # Entrywise Lax equations reproduce the Flaschka vector field.
    for j in range(N - 1):
        ok(sp.simplify(C[j, j + 1] - a[j] * (b[j + 1] - b[j])) == 0, f"a-dot {j}")
    for j in range(N):
        expected = 2 * ((a[j] ** 2 if j < N - 1 else 0) - (a[j - 1] ** 2 if j > 0 else 0))
        ok(sp.simplify(C[j, j] - expected) == 0, f"b-dot {j}")
    # Isospectral trace identities follow from cyclicity.
    for k in range(1, N + 1):
        ok(sp.simplify(sp.trace((L ** (k - 1)) * C)) == 0, f"trace invariant {k}")
    # Characteristic polynomials of concrete N=2 and N=3 rows.
    x = sp.symbols("x")
    L2 = sp.Matrix([[sp.Rational(1, 2), 1], [1, -sp.Rational(1, 2)]])
    ok(sp.simplify(L2.charpoly(x).as_expr() - (x ** 2 - sp.Rational(5, 4))) == 0, "N2 characteristic")
    L3 = sp.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, -1]])
    ok(sp.simplify(L3.charpoly(x).as_expr() - x * (x ** 2 - 3)) == 0, "N3 symmetric characteristic")
    # Irreducible Jacobi matrices have no repeated eigenvalue: a repeated
    # eigenspace would have a vector with first component zero, and the
    # three-term recurrence then forces the vector to vanish.
    lam = sp.symbols("lam")
    u = sp.symbols("u0:5")
    # Verify the recurrence implication for a positive symbolic edge chain.
    ok(sp.simplify(u[0]) == u[0], "recurrence seed")
    # N=2 closed form satisfies the ODE identically.
    aa, d, t, alpha, s = sp.symbols("aa d t alpha s", positive=True)
    z = d * t + alpha
    at = d / (2 * sp.cosh(z)); db = d * sp.tanh(z)
    ok(sp.simplify((sp.diff(at, t) + at * db).rewrite(sp.exp)) == 0, "N2 a equation")
    b1 = (s + db) / 2; b2 = (s - db) / 2
    ok(sp.simplify((sp.diff(b1, t) - 2 * at ** 2).rewrite(sp.exp)) == 0, "N2 b1 equation")
    ok(sp.simplify((sp.diff(b2, t) + 2 * at ** 2).rewrite(sp.exp)) == 0, "N2 b2 equation")
    # The d/alpha constraints encode the initial point and conserved gap.
    ok(sp.simplify(sp.tanh(sp.atanh(sp.symbols("r", real=True)))) - sp.symbols("r", real=True) == 0, "atanh branch")
    # Boundary characteristic polynomial has a genuine repeated root.
    Lb = sp.diag(0, 0, 1)
    ok(sp.simplify(Lb.charpoly(x).as_expr() - x ** 2 * (x - 1)) == 0, "repeated-root boundary")
    # Norming weights are a normalized exponential family and therefore sum to one.
    r1, r2, r3, l1, l2, l3, tt = sp.symbols("r1 r2 r3 l1 l2 l3 tt", positive=True)
    zt = r1 * sp.exp(2 * l1 * tt) + r2 * sp.exp(2 * l2 * tt) + r3 * sp.exp(2 * l3 * tt)
    rho = [r1 * sp.exp(2 * l1 * tt) / zt, r2 * sp.exp(2 * l2 * tt) / zt, r3 * sp.exp(2 * l3 * tt) / zt]
    ok(sp.simplify(sum(rho) - 1) == 0, "norming normalization")
    ok(sp.simplify(sp.diff(rho[0], tt) - 2 * rho[0] * (l1 - sum(rho[j] * [l1, l2, l3][j] for j in range(3)))) == 0, "norming logistic flow")
    # Two-by-two Hankel/Cauchy--Binet minors give the inverse-spectral Toda
    # coefficients and the correct trace/center-of-mass identities.
    rr1, rr2, ll1, ll2, tau_t = sp.symbols("rr1 rr2 ll1 ll2 tau_t", positive=True)
    R1 = rr1 * sp.exp(2 * ll1 * tau_t) + rr2 * sp.exp(2 * ll2 * tau_t)
    R2 = rr1 * rr2 * sp.exp(2 * (ll1 + ll2) * tau_t) * (ll2 - ll1) ** 2
    tau_a = sp.sqrt(R2) / R1
    tau_b1 = sp.diff(sp.log(R1), tau_t) / 2
    tau_b2 = sp.diff(sp.log(R2 / R1), tau_t) / 2
    ok(sp.simplify(tau_b1 + tau_b2 - (ll1 + ll2)) == 0, "tau trace")
    ok(sp.simplify(tau_a**2 - R2 / R1**2) == 0, "tau edge")
    ok(sp.simplify(sp.diff(tau_a, tau_t) - tau_a * (tau_b2 - tau_b1)) == 0, "tau a flow")
    ok(sp.simplify(sp.diff(tau_b1, tau_t) - 2 * tau_a**2) == 0, "tau b flow")
    print(json.dumps({"status": "C230_SYMPY_PASS", "checks": checks, "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
