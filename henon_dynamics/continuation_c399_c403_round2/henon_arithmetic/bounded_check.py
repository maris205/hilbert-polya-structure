#!/usr/bin/env python3
"""Bounded exact tests of geometric Hénon/Frobenius intersections.

No finite-field orbit enumeration is used. The affine quotient dimension is
computed from a Groebner basis independently of the projective proof.
These tests are examples, not a proof of the quantified theorem.
"""

import itertools
import json
import platform
from pathlib import Path

import sympy as sp


x, y = sp.symbols("x y")


def affine_length(p, q, coefficients, a, n, r):
    """Coefficients are ascending, and belong to the prime subfield."""
    X, Y = x, y
    for _ in range(n):
        next_Y = sum(c * Y**j for j, c in enumerate(coefficients)) - a * X
        X, Y = Y, sp.Poly(next_Y, x, y, modulus=p).as_expr()
    Q = q**r
    equations = [X - x**Q, Y - y**Q]
    G = sp.groebner(equations, x, y, modulus=p)
    if list(G) == [1]:
        return 0, [[0, 0]]
    assert G.is_zero_dimensional
    leads = [g.LM(order=G.order).exponents for g in G.polys]
    # A pure power of each variable is necessary for a zero-dimensional
    # monomial ideal. Every standard monomial lies in this exact rectangle.
    x_bound = min(i for i, j in leads if j == 0)
    y_bound = min(j for i, j in leads if i == 0)
    dimension = sum(
        not any(i >= a0 and j >= b0 for a0, b0 in leads)
        for i in range(x_bound)
        for j in range(y_bound)
    )
    jac = sp.det(sp.Matrix(equations).jacobian([x, y]))
    assert sp.Poly(jac - a**n, x, y, modulus=p).is_zero
    return dimension, [list(t) for t in leads]


def main():
    cases = []
    # Complete 36-parameter quadratic coefficient/Jacobian test over F_3,
    # at n=2, Q=3, where D=4>Q and the large-Frobenius formula fails.
    for c0, c1, c2, a in itertools.product(range(3), range(3), (1, 2), (1, 2)):
        cases.append((3, 3, [c0, c1, c2], a, 2, 1))
    # Explicit small/large twist, higher iterate, leading coefficient,
    # characteristic-two nonadditive, and nonprime base-field examples.
    cases.extend([
        (3, 3, [1, 0, 1], 1, 1, 1),
        (3, 3, [1, 0, 1], 1, 3, 1),
        (3, 3, [1, 0, 1], 1, 4, 1),
        (3, 3, [1, 0, 1], 1, 3, 2),
        (3, 3, [1, 0, 1], 1, 4, 2),
        (3, 9, [1, 0, 1], 2, 2, 1),
        (5, 5, [1, 2, 3], 2, 2, 1),
        (5, 5, [1, 2, 3], 2, 3, 1),
        (2, 2, [1, 1, 0, 1], 1, 1, 1),
        (2, 2, [1, 1, 0, 1], 1, 2, 1),
        (2, 4, [1, 1, 0, 1], 1, 2, 1),
    ])
    rows = []
    for p, q, c, a, n, r in cases:
        actual, leading = affine_length(p, q, c, a, n, r)
        d, Q = len(c) - 1, q**r
        D = d**n
        assert D != Q
        expected = max(Q * Q, Q * D)
        assert actual == expected, (p, q, c, a, n, r, actual, expected)
        rows.append(dict(p=p, q=q, coefficients=c, a=a, n=n, r=r,
                         degree=D, frobenius_degree=Q, affine_length=actual,
                         predicted=expected, leading_monomials=leading))
    # Adversarial resonance: nonadditive cubic in characteristic three.
    # H(x,y)=(y,y^3+y^2-x), Q=3. Elimination gives x^6-x, so 6, not 9.
    resonant, leads = affine_length(3, 3, [0, 0, 1, 1], 1, 1, 1)
    assert resonant == 6
    result = dict(
        scope="bounded exact examples, not universal proof",
        python=platform.python_version(), sympy=sp.__version__,
        nonresonant_checks=len(rows), rows=rows,
        resonant_negative_control=dict(
            p=3, q=3, coefficients=[0, 0, 1, 1], a=1, n=1, r=1,
            affine_length=resonant, naive_max=9, leading_monomials=leads),
    )
    target = Path(__file__).with_name("bounded_results.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "nonresonant_checks": len(rows),
                      "resonance_control": "6 != 9", "output": str(target)}))


if __name__ == "__main__":
    main()
