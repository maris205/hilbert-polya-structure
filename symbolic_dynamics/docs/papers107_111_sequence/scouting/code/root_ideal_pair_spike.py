#!/usr/bin/env python3
"""Exact discovery spike for (I,J) -> (I+J,IJ) in Z/NZ."""

from itertools import product
from math import gcd


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out.append((p, a))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    ans = [1]
    for p, a in factor(n):
        ans = [d * p**e for d in ans for e in range(a + 1)]
    return sorted(ans)


def ideal_step(n, state):
    d, e = state
    return gcd(d, e), gcd(n, d * e)


def valuation_vector(d, fac):
    ans = []
    for p, a in fac:
        e = 0
        while e < a and d % p == 0:
            d //= p
            e += 1
        ans.append(e)
    return tuple(ans)


def coordinate_step(a, state):
    e, f = state
    return min(e, f), min(a, e + f)


def coordinate_iterate_formula(a, e, f, t):
    if t == 0:
        return e, f
    m = min(e, f)
    return m, min(a, e + f + (t - 1) * m)


def hitting_time(step, state, cutoff=100):
    current = state
    for t in range(cutoff + 1):
        if step(current) == current:
            return t
        current = step(current)
    raise AssertionError((state, cutoff))


def coordinate_cdf(a, t):
    return sum(
        hitting_time(lambda s: coordinate_step(a, s), (e, f), a + 3) <= t
        for e in range(a + 1)
        for f in range(a + 1)
    )


def run():
    assertions = 0
    for a in range(1, 13):
        fixed = 0
        depths = []
        for e, f in product(range(a + 1), repeat=2):
            state = (e, f)
            fixed += coordinate_step(a, state) == state
            tau = hitting_time(lambda s: coordinate_step(a, s), state, a + 3)
            depths.append(tau)
            current = state
            for t in range(a + 3):
                assert current == coordinate_iterate_formula(a, e, f, t)
                assertions += 1
                current = coordinate_step(a, current)
        assert fixed == 2 * a + 1
        assert max(depths) == max(1, a - 1)
        assertions += 2
        assert coordinate_cdf(a, a + 1) == (a + 1) ** 2
        assertions += 1

    for n in range(2, 301):
        fac = factor(n)
        divs = divisors(n)
        expected_fixed = 1
        for _, a in fac:
            expected_fixed *= 2 * a + 1
        observed_fixed = 0
        depth_hist = {}
        for d, e in product(divs, repeat=2):
            state = (d, e)
            observed_fixed += ideal_step(n, state) == state
            tau = hitting_time(lambda s: ideal_step(n, s), state, max(a for _, a in fac) + 4)
            depth_hist[tau] = depth_hist.get(tau, 0) + 1
            dv = valuation_vector(d, fac)
            ev = valuation_vector(e, fac)
            coordinate_tau = max(
                hitting_time(lambda s, aa=a: coordinate_step(aa, s), (x, y), a + 3)
                for (x, y), (_, a) in zip(zip(dv, ev), fac)
            )
            assert tau == coordinate_tau
            assertions += 1
            next_d, next_e = ideal_step(n, state)
            ndv = valuation_vector(next_d, fac)
            nev = valuation_vector(next_e, fac)
            assert all(
                coordinate_step(a, (x, y)) == (nx, ny)
                for x, y, nx, ny, (_, a) in zip(dv, ev, ndv, nev, fac)
            )
            assertions += 1
        assert observed_fixed == expected_fixed
        assertions += 1
        for t in range(max(depth_hist) + 1):
            cdf = sum(v for depth, v in depth_hist.items() if depth <= t)
            expected_cdf = 1
            for _, a in fac:
                expected_cdf *= coordinate_cdf(a, t)
            assert cdf == expected_cdf
            assertions += 1
    print("root ideal-pair spike: PASS")
    print(f"exact assertions: {assertions}")
    print("checked prime exponents a=1..12 and all N=2..300")


if __name__ == "__main__":
    run()
