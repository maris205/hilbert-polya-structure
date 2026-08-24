#!/usr/bin/env python3
"""Second exact-algebra cross-check for C115."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
DATA = json.loads((PROJECT / "results/c115_mcmillan_evidence.json").read_text())
x, y, z, lam = sp.symbols("x y z lam")


def same(left: object, right: object) -> bool:
    return sp.simplify(sp.sympify(left) - sp.sympify(right)) == 0


def main() -> None:
    checks = 0

    def check(condition: bool) -> None:
        nonlocal checks
        assert condition
        checks += 1

    f = -4 * x / (1 + x**2)
    X, Y = f - y, x
    I = x**2 * y**2 + x**2 + y**2 + 4 * x * y
    check(sp.cancel(I.subs({x: X, y: Y}, simultaneous=True) - I) == 0)

    # Direct Groebner elimination for the cleared F^2 equations.
    X2 = sp.cancel(-4 * X / (1 + X**2) - Y)
    Y2 = X
    n1 = sp.factor(sp.together(X2 - x).as_numer_denom()[0])
    n2 = sp.factor(sp.together(Y2 - y).as_numer_denom()[0])
    basis = sp.groebner([n1, n2], y, x, order="lex")
    check(any(same(poly.as_expr(), x**5 + 2 * x**3 - 3 * x) for poly in basis.polys))
    check(sp.factor(x**5 + 2 * x**3 - 3 * x) == x * (x - 1) * (x + 1) * (x**2 + 3))
    check(same(DATA["period_two_elimination"]["valid_factor_after_pole_exclusion"], x**5 + 2 * x**3 - 3 * x))

    # Check every valid F^2 root with its corresponding y, separately from poles.
    roots = [0, 1, -1, sp.I * sp.sqrt(3), -sp.I * sp.sqrt(3)]
    for root in roots:
        ordinate = sp.simplify(-(root**3 + root) / 2)
        check(sp.simplify(root**2 + 1) != 0)
        image1 = (sp.cancel(-4 * root / (1 + root**2) - ordinate), root)
        image2 = (sp.cancel(-4 * image1[0] / (1 + image1[0] ** 2) - image1[1]), image1[0])
        check(all(same(a, b) for a, b in zip(image2, (root, ordinate))))

    for root in (sp.I, -sp.I):
        check(sp.simplify(root**2 + 1) == 0)

    derivative = sp.diff(f, x)
    J = sp.Matrix([[derivative, -1], [1, 0]])
    P2 = sp.simplify(J.subs(x, -1) * J.subs(x, 1))
    check(P2 == -sp.eye(2))
    check(P2.eigenvals() == {-1: 2})
    check(same(DATA["period_two_monodromy"]["characteristic_polynomial"], (lam + 1) ** 2))
    check(same(DATA["period_two_monodromy"]["det_I_minus_zP2"], (z + 1) ** 2))
    J0 = J.subs(x, 0)
    check(same(DATA["fixed_origin_control"]["characteristic_polynomial"], lam**2 + 4 * lam + 1))
    check(same(DATA["fixed_origin_control"]["det_I_minus_zDM"], z**2 + 4 * z + 1))
    check(DATA["verdict"]["A2"] == "A2_FAIL")
    print(f"C115_SYMPY_PASS {checks}")


if __name__ == "__main__":
    main()
