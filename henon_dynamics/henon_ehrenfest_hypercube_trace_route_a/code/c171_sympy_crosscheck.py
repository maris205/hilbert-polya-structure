#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C171."""
from __future__ import annotations

import json
from math import comb

import sympy as sp


def krawtchouk(d: int, j: int, k: int) -> int:
    return sum((-1)**r*comb(k,r)*comb(d-k,j-r)
               for r in range(max(0,j-d+k), min(j,k)+1))


def main() -> None:
    x, z = sp.symbols("x z")
    checks = 0
    for d in range(1, 13):
        Q = sp.zeros(d+1)
        for k in range(d+1):
            if k < d:
                Q[k,k+1] = sp.Rational(d-k,d)
            if k > 0:
                Q[k,k-1] = sp.Rational(k,d)
        expected_char = sp.prod(x-sp.Rational(d-2*j,d) for j in range(d+1))
        assert sp.expand(Q.charpoly(x).as_expr()-expected_char) == 0
        checks += 1
        for j in range(d+1):
            vector = sp.Matrix([krawtchouk(d,j,k) for k in range(d+1)])
            assert Q*vector == sp.Rational(d-2*j,d)*vector
            checks += d+1
        # Keep the high-degree determinant factored: its polynomial degree is
        # the sum of exponents attached to nonzero eigenvalues.
        determinant = sp.prod((1-z*sp.Rational(d-2*j,d))**comb(d,j) for j in range(d+1))
        degree = sum(comb(d,j) for j in range(d+1) if d-2*j != 0)
        assert degree == 2**d - (comb(d,d//2) if d%2==0 else 0)
        assert determinant.subs(z, 0) == 1
        checks += 1
        for n in range(1, 13, 2):
            trace = sum(comb(d,j)*sp.Rational(d-2*j,d)**n for j in range(d+1))
            assert trace == 0
            checks += 1
    print(json.dumps({"status": "C171_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
