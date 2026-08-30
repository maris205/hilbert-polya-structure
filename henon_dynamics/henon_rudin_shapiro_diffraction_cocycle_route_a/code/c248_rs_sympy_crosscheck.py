#!/usr/bin/env python3
"""Independent SymPy checks for the C248 Rudin--Shapiro identities."""
from __future__ import annotations

import sympy as sp


RULES = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
CODING = {"a": 1, "b": 1, "c": -1, "d": -1}


def word(step: int) -> str:
    out = "a"
    for _ in range(step):
        out = "".join(RULES[x] for x in out)
    return out


def poly(coeff: list[int], z: sp.Symbol) -> sp.Expr:
    return sum(value * z**index for index, value in enumerate(coeff))


def corr_poly(a: list[int], b: list[int], z: sp.Symbol) -> sp.Expr:
    return sp.expand(poly(a, z) * poly(b, z**-1))


def main() -> None:
    z = sp.symbols("z", nonzero=True)
    checks = 0
    p, q = [1], [1]
    for k in range(7):
        P, Q = poly(p, z), poly(q, z)
        assert sp.expand(P * P.subs(z, z**-1) + Q * Q.subs(z, z**-1) - 2 ** (k + 1)) == 0
        checks += 1
        assert max(abs(x) for x in p) == max(abs(x) for x in q) == 1
        checks += 1
        assert p == [CODING[x] for x in word(k)]
        checks += 1
        Pn, Qn = P + z ** (1 << k) * Q, P - z ** (1 << k) * Q
        pnext, qnext = p + q, p + [-x for x in q]
        assert sp.expand(Pn - poly(pnext, z)) == 0 and sp.expand(Qn - poly(qnext, z)) == 0
        checks += 1
        R, S = corr_poly(p, p, z), corr_poly(q, q, z)
        T, U = corr_poly(p, q, z), corr_poly(q, p, z)
        N = 1 << k
        assert sp.expand(corr_poly(pnext, pnext, z) - (R + S + z**(-N) * T + z**N * U)) == 0
        assert sp.expand(corr_poly(qnext, qnext, z) - (R + S - z**(-N) * T - z**N * U)) == 0
        assert sp.expand(corr_poly(pnext, qnext, z) - (R - S - z**(-N) * T + z**N * U)) == 0
        assert sp.expand(corr_poly(qnext, pnext, z) - (R - S + z**(-N) * T - z**N * U)) == 0
        checks += 4
        p, q = pnext, qnext

    # The substitution matrix has Perron vector (1,1,1,1) and a positive cube.
    M = sp.Matrix([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]])
    assert all(v > 0 for v in (M**3))
    checks += 1
    v = sp.Matrix([1, 1, 1, 1])
    assert M * v == 2 * v
    checks += 1
    # The first aperiodicity receipts are exact word inequalities, not floats.
    w = word(9)
    for period in range(1, 33):
        assert any(w[i] != w[i + period] for i in range(len(w) - period))
        checks += 1
    print(f"C248 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
