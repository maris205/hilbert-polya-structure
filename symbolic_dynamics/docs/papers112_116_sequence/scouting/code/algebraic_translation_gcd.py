#!/usr/bin/env python3
"""Exact spike for translation-GCD erosion on bounded monic polynomials.

Over F_p define T(f)(x)=gcd(f(x),f(x+1)).  Direct polynomial arithmetic is
used to verify the sliding-window identity

    T^t(f)=gcd(f(x),f(x+1),...,f(x+t))

and the resulting stabilization after at most p-1 steps.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def trim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return tuple(f)


def degree(f):
    f = trim(f)
    return -1 if f == (0,) else len(f) - 1


def monic(f, p):
    f = trim(f)
    if f == (0,):
        return f
    inv = pow(f[-1], -1, p)
    return trim(tuple(inv * c % p for c in f))


def add_poly(a, b, p):
    n = max(len(a), len(b))
    return trim(
        tuple(
            ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0))
            % p
            for i in range(n)
        )
    )


def mul_poly(a, b, p):
    if a == (0,) or b == (0,):
        return (0,)
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(tuple(out))


def divmod_poly(a, b, p):
    a = list(trim(a))
    b = trim(b)
    if b == (0,):
        raise ZeroDivisionError
    db = degree(b)
    inv = pow(b[-1], -1, p)
    if degree(tuple(a)) < db:
        return (0,), tuple(a)
    quotient = [0] * (degree(tuple(a)) - db + 1)
    while not (len(a) == 1 and a[0] == 0) and len(a) - 1 >= db:
        shift = len(a) - 1 - db
        coeff = a[-1] * inv % p
        quotient[shift] = coeff
        for j, value in enumerate(b):
            a[shift + j] = (a[shift + j] - coeff * value) % p
        a = list(trim(tuple(a)))
    return trim(tuple(quotient)), trim(tuple(a))


def gcd_poly(a, b, p):
    while trim(b) != (0,):
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    return monic(a, p)


def translate(f, amount, p):
    """Return f(x+amount)."""
    amount %= p
    out = [0] * len(f)
    for i, coeff in enumerate(f):
        for j in range(i + 1):
            out[j] = (
                out[j] + coeff * comb(i, j) * pow(amount, i - j, p)
            ) % p
    return trim(tuple(out))


def update(f, p):
    return gcd_poly(f, translate(f, 1, p), p)


def iterate(f, p, t):
    for _ in range(t):
        f = update(f, p)
    return f


def window_gcd(f, p, t):
    out = f
    for amount in range(1, t + 1):
        out = gcd_poly(out, translate(f, amount, p), p)
    return out


def monics_exact(p, n):
    if n == 0:
        yield (1,)
        return
    for lower in product(range(p), repeat=n):
        yield tuple(lower) + (1,)


def compose_with_artin_schreier(h, p):
    """Compute h(x^p-x) by Horner's rule."""
    y = [0] * (p + 1)
    y[1] = (-1) % p
    y[p] = 1
    y = tuple(y)
    out = (0,)
    for coefficient in reversed(h):
        out = add_poly(mul_poly(out, y, p), (coefficient % p,), p)
    return trim(out)


def fixed_count_bounded(p, n):
    return sum(p**m for m in range(n // p + 1))


def missing_one_linear_orbit(p):
    """Product over p-1 of the p linear factors x-a."""
    out = (1,)
    for a in range(p - 1):
        out = mul_poly(out, ((-a) % p, 1), p)
    return out


def run_lane(p, max_degree):
    polys = [f for n in range(max_degree + 1) for f in monics_exact(p, n)]
    profiles = defaultdict(Counter)
    fixed = []
    for f in polys:
        orbit = [f]
        while update(orbit[-1], p) != orbit[-1]:
            orbit.append(update(orbit[-1], p))
            AUDIT.check(len(orbit) <= p, f"translation erosion exceeded p-1: {f}")
        depth = len(orbit) - 1
        profiles[degree(f)][depth] += 1
        if depth == 0:
            fixed.append(f)
        for t in range(p):
            AUDIT.check(
                iterate(f, p, t) == window_gcd(f, p, t),
                f"sliding-window mismatch p={p}, f={f}, t={t}",
            )
        AUDIT.check(iterate(f, p, p - 1) == orbit[-1])
        AUDIT.check(translate(orbit[-1], 1, p) == orbit[-1])

    expected_fixed = set()
    for m in range(max_degree // p + 1):
        for h in monics_exact(p, m):
            expected_fixed.add(compose_with_artin_schreier(h, p))
    AUDIT.check(len(fixed) == fixed_count_bounded(p, max_degree))
    AUDIT.check(set(fixed) == expected_fixed)
    for n in range(max_degree + 1):
        AUDIT.check(sum(profiles[n].values()) == p**n)
        AUDIT.check(
            max(profiles[n]) == min(n, p - 1),
            f"sharp translation depth mismatch at p={p}, n={n}",
        )

    witness = missing_one_linear_orbit(p)
    if degree(witness) <= max_degree:
        witness_depth = next(
            depth for depth in range(p) if iterate(witness, p, depth) == iterate(witness, p, p - 1)
        )
        AUDIT.check(witness_depth == p - 1, "sharp-depth witness failed")

    terminal = {
        n: dict(sorted(profiles[n].items()))
        for n in range(max(0, max_degree - 2), max_degree + 1)
    }
    print(
        f"p={p}, max_degree={max_degree}: phase={len(polys)}, fixed={len(fixed)}, "
        f"terminal depth profiles={terminal}"
    )


def main():
    for lane in [(2, 8), (3, 7), (5, 6), (7, 5)]:
        run_lane(*lane)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
