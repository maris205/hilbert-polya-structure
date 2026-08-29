#!/usr/bin/env python3
"""Exact spike for I -> Ann(I)^r on ideals of Z/NZ."""

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


def valuations(d, fac):
    ans = []
    for p, a in fac:
        e = 0
        while e < a and d % p == 0:
            d //= p
            e += 1
        ans.append(e)
    return tuple(ans)


def literal_step(n, r, d):
    return gcd(n, (n // d) ** r)


def coordinate_step(a, r, e):
    return min(a, r * (a - e))


def recurrent_coordinate(a, r, e):
    return e in (0, a) or ((r + 1) * e == r * a)


def coordinate_depth(a, r, e):
    current = e
    for t in range(a + 3):
        if recurrent_coordinate(a, r, current):
            return t
        current = coordinate_step(a, r, current)
    raise AssertionError((a, r, e))


def threshold_depth(a, r, e):
    if recurrent_coordinate(a, r, e):
        return 0
    delta = (r + 1) * e - r * a
    for j in range(a + 2):
        if delta <= -a / r:
            return j + 1
        delta *= -r
    raise AssertionError((a, r, e))


def run():
    assertions = 0
    for r in range(2, 9):
        for a in range(1, 31):
            states = list(range(a + 1))
            fixed = [e for e in states if coordinate_step(a, r, e) == e]
            recurrent = [e for e in states if recurrent_coordinate(a, r, e)]
            assert len(fixed) == int(a % (r + 1) == 0)
            assert len(recurrent) == 2 + len(fixed)
            assertions += 2
            for e in states:
                assert coordinate_depth(a, r, e) == threshold_depth(a, r, e)
                assertions += 1
                x = e
                for _ in range(2 * a + 5):
                    x = coordinate_step(a, r, x)
                assert recurrent_coordinate(a, r, x)
                assertions += 1

    for r in range(2, 6):
        for n in range(2, 501):
            fac = factor(n)
            ds = divisors(n)
            fixed_odd = 1
            fixed_even = 1
            for _, a in fac:
                epsilon = int(a % (r + 1) == 0)
                fixed_odd *= epsilon
                fixed_even *= 2 + epsilon
            observed_odd = 0
            observed_even = 0
            depth_hist = {}
            for d in ds:
                t1 = literal_step(n, r, d)
                t2 = literal_step(n, r, t1)
                observed_odd += t1 == d
                observed_even += t2 == d
                dv = valuations(d, fac)
                nv = valuations(t1, fac)
                assert all(
                    coordinate_step(a, r, e) == ne
                    for e, ne, (_, a) in zip(dv, nv, fac)
                )
                assertions += 1
                tau = max(coordinate_depth(a, r, e) for e, (_, a) in zip(dv, fac))
                depth_hist[tau] = depth_hist.get(tau, 0) + 1
                x = d
                for _ in range(tau):
                    x = literal_step(n, r, x)
                xv = valuations(x, fac)
                assert all(recurrent_coordinate(a, r, e) for e, (_, a) in zip(xv, fac))
                assertions += 1
            assert observed_odd == fixed_odd
            assert observed_even == fixed_even
            assert sum(depth_hist.values()) == len(ds)
            assertions += 3
    print("root annihilator-power spike: PASS")
    print(f"exact assertions: {assertions}")
    print("checked r=2..8, a=1..30, and all N=2..500 for r=2..5")


if __name__ == "__main__":
    run()
