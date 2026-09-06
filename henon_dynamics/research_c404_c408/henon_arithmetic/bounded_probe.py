#!/usr/bin/env python3
"""Five bounded resonant checks, not an all-period theorem or novelty claim.

The map is H(x,y)=(y,y**q+y**m-x), in characteristic p.  We count
the affine quotient for H**n=(x**(q**n),y**(q**n)) using grevlex.
The quotient is reduced: its Jacobian determinant is identically one.
No finite-field extension census, old producer import, or file write occurs.
"""

import json
import platform

import sympy as sp


def probe(p, q, m, n):
    x, y = sp.symbols("x y")
    X, Y = x, y
    for _ in range(n):
        X, Y = Y, sp.Poly(Y**q + Y**m - X, x, y, modulus=p).as_expr()
    Q = q**n
    equations = [X - x**Q, Y - y**Q]
    jacobian = sp.det(sp.Matrix(equations).jacobian([x, y]))
    assert sp.Poly(jacobian - 1, x, y, modulus=p).is_zero
    basis = sp.groebner(equations, x, y, modulus=p, order="grevlex")
    assert basis.is_zero_dimensional
    leading = [g.LM(order=basis.order).exponents for g in basis.polys]
    x_bound = min(i for i, j in leading if j == 0)
    y_bound = min(j for i, j in leading if i == 0)
    count = sum(
        not any(i >= a and j >= b for a, b in leading)
        for i in range(x_bound)
        for j in range(y_bound)
    )
    # A second combinatorial count of the same monomial staircase; this is
    # not advertised as an independent algebraic proof of the basis.
    staircase = sum(
        min(b for a, b in leading if a <= i) for i in range(x_bound)
    )
    assert count == staircase
    return {
        "p": p, "q": q, "m": m, "n": n,
        "jacobian_determinant": 1,
        "affine_length_and_geometric_count": count,
        "leading_monomials": [list(e) for e in leading],
        "grevlex_basis": [str(g.as_expr()) for g in basis.polys],
        "naive_nonresonant_max": q**(2*n),
        "untested_constant_density_ansatz": m*q**(2*n-1),
    }


def main():
    cases = [(3, 3, 2, 1), (3, 3, 2, 2), (3, 3, 2, 3),
             (2, 4, 3, 1), (2, 4, 3, 2)]
    rows = [probe(*case) for case in cases]
    assert [r["affine_length_and_geometric_count"] for r in rows] == [
        6, 54, 378, 12, 176,
    ]
    assert rows[2]["affine_length_and_geometric_count"] != rows[2][
        "untested_constant_density_ansatz"]
    assert rows[4]["affine_length_and_geometric_count"] != rows[4][
        "untested_constant_density_ansatz"]
    print(json.dumps({
        "scope": "five bounded exact affine quotient checks only",
        "python": platform.python_version(), "sympy": sp.__version__,
        "all_period_theorem": False, "retained_paper_contracts": 0,
        "result": "bounded checks completed; two constant-density counterexamples",
        "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
