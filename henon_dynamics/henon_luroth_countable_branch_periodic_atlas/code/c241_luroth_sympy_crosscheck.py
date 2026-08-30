#!/usr/bin/env python3
"""Independent SymPy checks for Lüroth branch and weighted-word identities."""
from __future__ import annotations

from fractions import Fraction
import itertools
import math
import sympy as sp


def slope(m: int) -> int:
    return m * (m - 1)


def affine(word: tuple[int, ...]) -> tuple[sp.Rational, sp.Rational]:
    u, v = sp.Rational(1), sp.Rational(0)
    for m in reversed(word):
        u, v = u / slope(m), (v + m - 1) / slope(m)
    return u, v


def primitive_period(word: tuple[int, ...]) -> int:
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and word == word[:d] * (len(word) // d):
            return d
    raise AssertionError


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[j:] + word[:j] for j in range(len(word)))


def main() -> None:
    x, y = sp.symbols("x y")
    checks = 0
    # Branch map and inverse are exact affine inverses.
    for m in range(2, 13):
        T = slope(m) * x - (m - 1)
        phi = (y + m - 1) / slope(m)
        assert sp.simplify(T.subs(x, phi.subs(y, y)) - y) == 0
        assert sp.simplify(phi.subs(y, T) - x) == 0
        checks += 2
    # Composition, fixed point and multiplier for every word in the receipt
    # alphabet through length four.
    for r in range(1, 5):
        for word in itertools.product(range(2, 7), repeat=r):
            u, v = affine(word)
            fixed = sp.simplify(v / (1 - u))
            assert sp.simplify((u * fixed + v) - fixed) == 0
            assert sp.simplify(1 / u - math.prod(slope(m) for m in word)) == 0
            checks += 2
    # Telescoping boundary A(1)=1 at s=1.
    m = sp.symbols("m", integer=True, positive=True)
    assert sp.summation(1 / (m * (m - 1)), (m, 2, sp.oo)) == 1
    checks += 1
    # Finite primitive factor products agree with 1/(1-z*S) as formal series.
    for M in (3, 4):
        alphabet = list(range(2, M + 1))
        R = 4
        reps: dict[int, set[tuple[int, ...]]] = {r: set() for r in range(1, R + 1)}
        for r in range(1, R + 1):
            for word in itertools.product(alphabet, repeat=r):
                if primitive_period(word) == r:
                    reps[r].add(canonical(word))
        # Keep the formal-series check exact but avoid asking SymPy to expand a
        # large rational product.  A coefficient-array convolution is the
        # same algebra in Q[z]/(z^{R+1}) and is deterministic/fast.
        coeff = [sp.Rational(1)] + [sp.Rational(0)] * R
        for r, words in reps.items():
            for word in words:
                w = sp.Rational(1, math.prod(slope(a) for a in word))
                factor = [sp.Rational(0)] * (R + 1)
                for q in range(R // r + 1):
                    factor[q * r] = w ** q
                nxt = [sp.Rational(0)] * (R + 1)
                for a, va in enumerate(coeff):
                    for b, vb in enumerate(factor[: R - a + 1]):
                        nxt[a + b] += va * vb
                coeff = nxt
        S = sum(sp.Rational(1, slope(a)) for a in alphabet)
        rhs = [S ** j for j in range(R + 1)]
        assert coeff == rhs
        checks += 1
    print(f"C241 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
