#!/usr/bin/env python3
"""Exact spike for f -> gcd(f, f') on bounded monic polynomials.

The phase space in a lane is the set of monic polynomials of degree at most
``max_degree`` over the prime field F_p (including the monic constant 1).
Everything below is literal finite-field arithmetic using Python integers.
No factorisation routine is used: the temporal formula is checked against
direct derivative/GCD iteration.
"""

from collections import Counter, defaultdict
from itertools import product


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
    return trim(tuple((inv * c) % p for c in f))


def derivative(f, p):
    if len(f) <= 1:
        return (0,)
    return trim(tuple((i * f[i]) % p for i in range(1, len(f))))


def divmod_poly(a, b, p):
    a = list(trim(a))
    b = trim(b)
    if b == (0,):
        raise ZeroDivisionError("polynomial division by zero")
    db = degree(b)
    inv = pow(b[-1], -1, p)
    if degree(tuple(a)) < db:
        return (0,), tuple(a)
    q = [0] * (degree(tuple(a)) - db + 1)
    while not (len(a) == 1 and a[0] == 0) and len(a) - 1 >= db:
        shift = len(a) - 1 - db
        coeff = a[-1] * inv % p
        q[shift] = coeff
        for j, bj in enumerate(b):
            a[shift + j] = (a[shift + j] - coeff * bj) % p
        a = list(trim(tuple(a)))
    return trim(tuple(q)), trim(tuple(a))


def gcd_poly(a, b, p):
    a, b = trim(a), trim(b)
    while b != (0,):
        _, r = divmod_poly(a, b, p)
        a, b = b, r
    return monic(a, p)


def update(f, p):
    return gcd_poly(f, derivative(f, p), p)


def iterate(f, p, t):
    for _ in range(t):
        f = update(f, p)
    return f


def monics_exact(p, n):
    if n == 0:
        yield (1,)
        return
    for lower in product(range(p), repeat=n):
        yield tuple(lower) + (1,)


def pth_power(g, p):
    out = [0] * (p * degree(g) + 1)
    for i, c in enumerate(g):
        # In the prime field c^p=c.
        out[p * i] = c
    return trim(tuple(out))


def denominator_coefficient(p, n):
    """[u^n] 1 / ((1-pu)(1-pu^p))."""
    if n < 0:
        return 0
    return sum(p ** (n - (p - 1) * b) for b in range(n // p + 1))


def depth_cdf_exact_degree(p, n, t):
    """Coefficient of (1-p*u^(t+1))/((1-pu)(1-pu^p))."""
    return denominator_coefficient(p, n) - p * denominator_coefficient(
        p, n - t - 1
    )


def p_power_free_count(p, n):
    """Monic degree-n polynomials with every factor multiplicity < p."""
    if n < 0:
        return 0
    if n < p:
        return p**n
    return p**n - p ** (n - p + 1)


def fixed_count_bounded(p, n):
    return sum(p**m for m in range(n // p + 1))


def run_lane(p, max_degree):
    all_polys = [
        f for n in range(max_degree + 1) for f in monics_exact(p, n)
    ]
    by_degree_depth = defaultdict(Counter)
    stable_fibres = Counter()
    fixed = []

    for f in all_polys:
        orbit = [f]
        while update(orbit[-1], p) != orbit[-1]:
            orbit.append(update(orbit[-1], p))
            AUDIT.check(len(orbit) <= p, f"depth exceeds p-1 for p={p}: {f}")
        stable = orbit[-1]
        depth = len(orbit) - 1
        by_degree_depth[degree(f)][depth] += 1
        stable_fibres[stable] += 1

        AUDIT.check(derivative(stable, p) == (0,), "stable state has nonzero derivative")
        AUDIT.check(update(stable, p) == stable, "terminal state is not fixed")
        AUDIT.check(iterate(f, p, p - 1) == stable, "universal stabilization failed")
        AUDIT.check(iterate(f, p, p) == stable, "post-stabilization drift")
        if f == stable:
            fixed.append(f)

    AUDIT.check(len(fixed) == fixed_count_bounded(p, max_degree))
    for n in range(max_degree + 1):
        AUDIT.check(sum(by_degree_depth[n].values()) == p**n)
        AUDIT.check(
            max(by_degree_depth[n]) == min(n, p - 1),
            f"sharp depth mismatch at p={p}, n={n}",
        )
        for t in range(p):
            literal = sum(
                count for dep, count in by_degree_depth[n].items() if dep <= t
            )
            formula = depth_cdf_exact_degree(p, n, t)
            AUDIT.check(
                literal == formula,
                f"depth CDF mismatch at p={p}, n={n}, t={t}: {literal}!={formula}",
            )

    # Every fixed polynomial is a literal p-th power; each degree-resolved
    # stable fibre has the p-power-free count predicted by Euler products.
    fixed_roots = {}
    for m in range(max_degree // p + 1):
        for g in monics_exact(p, m):
            target = pth_power(g, p)
            fixed_roots[target] = g
            AUDIT.check(target in stable_fibres)
    AUDIT.check(set(fixed) == set(fixed_roots))

    for target, g in fixed_roots.items():
        m = degree(g)
        # Refine the fibre by the total input degree without factoring.
        degree_counts = Counter()
        for f in all_polys:
            if iterate(f, p, p - 1) == target:
                degree_counts[degree(f)] += 1
        for n in range(max_degree + 1):
            expected = p_power_free_count(p, n - p * m)
            AUDIT.check(
                degree_counts[n] == expected,
                f"stable fibre mismatch at p={p}, root={g}, n={n}",
            )

    profile = {
        n: dict(sorted(by_degree_depth[n].items()))
        for n in range(max(0, max_degree - 2), max_degree + 1)
    }
    print(
        f"p={p}, max_degree={max_degree}: phase={len(all_polys)}, "
        f"fixed={len(fixed)}, terminal depth profiles={profile}"
    )


def main():
    for lane in [(2, 8), (3, 7), (5, 6), (7, 5)]:
        run_lane(*lane)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
