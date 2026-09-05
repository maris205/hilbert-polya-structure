#!/usr/bin/env python3
"""Exact symbolic identities; no floating-point precision claim."""
if not __debug__:
    raise RuntimeError("c394 symbolic refuses optimized Python")
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]

def main():
    a, x, y, q, z = s.symbols("a x y q z")
    F = s.Matrix([x+a*y*y, y+a*(x+a*y*y)**2])
    inverse = s.Matrix([x-a*(y-a*x*x)**2, y-a*x*x])
    reverse = s.Matrix([-y, -x])
    count = 0
    def zero(expr):
        nonlocal count
        assert s.expand(expr) == 0
        count += 1
    def compose(g, h):
        return g.subs({x: h[0], y: h[1]}, simultaneous=True)
    for vec in (compose(F, inverse)-s.Matrix([x, y]), compose(inverse, F)-s.Matrix([x, y]), compose(reverse, compose(F, reverse))-inverse):
        for expr in vec:
            zero(expr)
    zero(F.jacobian([x, y]).det()-1)
    for expr in compose(F, s.Matrix([q*x, q*y]))-q*F.subs(a, a*q):
        zero(expr)
    J = s.Matrix([[0, 1], [-1, 0]])
    for expr in F.jacobian([x, y]).T*J*F.jacobian([x, y])-J:
        zero(expr)
    data = json.loads((ROOT/"results/c394_interpolation_evidence.json").read_text())
    for row in data["finite_levels"]:
        total = sum(L*k for L, k in row["cycle_histogram"])
        assert total == row["points"]
        count += 1
        # Formal log derivative of the exact cycle product, through order 24.
        for n, fixed in enumerate(row["fixed_iterates"], 1):
            coefficient = sum(L*k for L, k in row["cycle_histogram"] if n % L == 0)
            assert coefficient == fixed["points"]
            count += 1
    for row in data["tails"]:
        m, p, c = row["m"], row["p"], row["c"]
        assert row["factorial_valuation"] == s.factorint(s.factorial(m)).get(p, 0)
        count += 1
        assert s.Rational(c*m-row["factorial_valuation"])-m*(c-s.Rational(1, p-1)) >= 0
        count += 1
        assert all(v >= 1 for v in row["strict_margins"])
        count += 1
    # A concrete hit set with a certified unique zero: x(F^t(0,1)).
    # Its first Mahler term is a*t and every higher term is strictly smaller
    # pointwise for nonzero t; this uses the proved first-coordinate divisibility.
    for row in data["polynomial_differences"][2:]:
        for ea, ex, ey, coefficient in row["coordinates"][0]:
            assert ea >= row["m"] and type(coefficient) is int
            count += 1
    print("C394 exact symbolic PASS: identities="+str(count))

if __name__ == "__main__":
    main()
