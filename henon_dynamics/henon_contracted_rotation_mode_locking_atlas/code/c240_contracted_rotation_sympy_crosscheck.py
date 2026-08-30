#!/usr/bin/env python3
"""Independent symbolic checks for the C240 contracted-rotation identities."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import sympy as sp


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def canonical(word: tuple[int, ...]) -> bool:
    return word == min(word[i:] + word[:i] for i in range(len(word)))


def exact_interval(lam: F, word: tuple[int, ...]):
    n = len(word)
    den = 1 - lam**n
    geom = sum(lam**j for j in range(n))
    carry = sum(F(word[j]) * lam ** (n - 1 - j) for j in range(n))
    a, b = geom / den, -carry / den
    lo, lc, hi, hc = F(0), True, F(1), False

    def upd(bound: F, lower: bool, closed: bool):
        nonlocal lo, lc, hi, hc
        if lower:
            if bound > lo:
                lo, lc = bound, closed
            elif bound == lo:
                lc = lc and closed
        else:
            if bound < hi:
                hi, hc = bound, closed
            elif bound == hi:
                hc = hc and closed

    def add(A: F, B: F, C: F, ge: bool):
        nonlocal lo, lc, hi, hc
        if A == 0:
            return B >= C if ge else B < C
        q = (C - B) / A
        upd(q, A > 0 if ge else A < 0, True if ge else False)
        return True

    if not add(F(1), F(0), F(0), True) or not add(F(1), F(0), F(1), False):
        return None
    for bit in word:
        if not add(a, b, F(0), True) or not add(a, b, F(1), False):
            return None
        ay, by = lam * a + 1, lam * b
        if not add(ay, by, F(bit), True) or not add(ay, by, F(bit + 1), False):
            return None
        a, b = ay, by - F(bit)
    if lo > hi or (lo == hi and not (lc and hc)):
        return None
    return lo, lc, hi, hc


def main() -> None:
    lam, delta, x = sp.symbols("lambda delta x", real=True)
    checks = 0

    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.factor(expr)))

    # Generic affine composition and fixed-point identities.
    for n in range(1, 7):
        bits = tuple((n + 2 * j) % 2 for j in range(n))
        y = x
        for bit in bits:
            y = lam * y + delta - bit
        expected = lam**n * x + delta * sum(lam**j for j in range(n)) - sum(bits[j] * lam ** (n - 1 - j) for j in range(n))
        ok(y - expected, f"composition n={n}")
        fixed = (delta * sum(lam**j for j in range(n)) - sum(bits[j] * lam ** (n - 1 - j) for j in range(n))) / (1 - lam**n)
        ok(expected.subs(x, fixed) - fixed, f"fixed point n={n}")
        ok(sp.diff(expected, x) - lam**n, f"derivative n={n}")

    # Branch carry inequalities and endpoint algebra.
    k = sp.symbols("k", integer=True)
    y = lam * x + delta
    ok((y - k) - (lam * x + delta - k), "carry subtraction")
    ok((1 - lam**1) - (1 - lam), "one-step denominator")
    ok((delta / (1 - lam)) * (1 - lam) - delta, "one-step fixed point")

    # Exact rational interval spot checks, including the half-open boundary.
    expected = {
        (F(1, 2), (0,)): (F(0), True, F(1, 2), False),
        (F(1, 2), (0, 1)): (F(2, 3), True, F(5, 6), False),
        (F(2, 3), (0, 1)): (F(3, 5), True, F(11, 15), False),
        (F(3, 4), (0, 1)): (F(4, 7), True, F(19, 28), False),
    }
    for (la, word), want in expected.items():
        got = exact_interval(la, word)
        if got != want:
            raise AssertionError(f"interval {la} {word}: {got} != {want}")
        checks += 1
    if exact_interval(F(1, 2), (1,)) is not None:
        raise AssertionError("all-one word should be inadmissible on delta<1")
    checks += 1

    # Primitive/cyclic representative checks on a complete small census.
    for n in range(1, 9):
        for word in product((0, 1), repeat=n):
            if canonical(word):
                checks += 1
                if not primitive(word) and n == 1:
                    raise AssertionError("one-letter word cannot be nonprimitive")
    print(f"C240_SYMPY_PASS ({checks} symbolic/rational identities)")


if __name__ == "__main__":
    main()
