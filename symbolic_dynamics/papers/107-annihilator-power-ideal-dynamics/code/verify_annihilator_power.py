#!/usr/bin/env python3
"""Exact controls for I -> Ann(I)^r on ideals of Z/NZ."""

from collections import Counter
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def ceil_div(x, y):
    return (x + y - 1) // y


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
    out = [1]
    for p, a in factor(n):
        out = [d * p**e for d in out for e in range(a + 1)]
    return sorted(out)


def valuations(d, fac):
    out = []
    for p, a in fac:
        e = 0
        while e < a and d % p == 0:
            d //= p
            e += 1
        out.append(e)
    return tuple(out)


def coordinate_step(a, r, e):
    return min(a, r * (a - e))


def literal_step(n, r, d):
    return gcd(n, (n // d) ** r)


def recurrent_coordinate(a, r, e):
    return e in (0, a) or (r + 1) * e == r * a


def literal_depth(step, state, cutoff):
    x = state
    for t in range(cutoff + 1):
        if step(step(x)) == x:
            return t
        x = step(x)
    raise AssertionError((state, cutoff))


def coordinate_depth_formula(a, r, e):
    if recurrent_coordinate(a, r, e):
        return 0
    delta = (r + 1) * e - r * a
    if delta < 0:
        k = 0
        while r ** (2 * k + 1) * (-delta) < a:
            k += 1
        return 2 * k + 1
    k = 0
    while r ** (2 * k + 2) * delta < a:
        k += 1
    return 2 * k + 2


def cdf_formula(a, r, t):
    epsilon = int(a % (r + 1) == 0)
    if t == 0:
        return 2 + epsilon
    jminus = 2 * ((t - 1) // 2)
    lminus = ceil_div(a, r ** (jminus + 1))
    mminus = max(0, min(a - 1, (r * a - lminus) // (r + 1)))
    mplus = 0
    if t >= 2:
        jplus = 2 * ((t - 2) // 2) + 1
        lplus = ceil_div(a, r ** (jplus + 1))
        low = max(1, ceil_div(r * a + lplus, r + 1))
        mplus = max(0, a - low)
    return 2 + epsilon + mminus + mplus


def coordinate_lane():
    states_checked = 0
    for r in range(2, 11):
        for a in range(1, 81):
            depths = Counter()
            recurrent = []
            for e in range(a + 1):
                states_checked += 1
                step = lambda x, aa=a, rr=r: coordinate_step(aa, rr, x)
                observed = literal_depth(step, e, 2 * a + 4)
                predicted = coordinate_depth_formula(a, r, e)
                check(observed == predicted, ("depth", a, r, e))
                depths[observed] += 1
                if observed == 0:
                    recurrent.append(e)
                x = e
                delta = (r + 1) * e - r * a
                for _ in range(observed):
                    y = step(x)
                    if y < a:
                        check((r + 1) * y - r * a == -r * ((r + 1) * x - r * a),
                              ("deviation", a, r, x))
                    x = y
            expected_rec = [0, a]
            if a % (r + 1) == 0:
                expected_rec.append(r * a // (r + 1))
            check(sorted(recurrent) == sorted(expected_rec), ("rec", a, r))
            for t in range(max(depths) + 2):
                observed = sum(v for depth, v in depths.items() if depth <= t)
                check(observed == cdf_formula(a, r, t), ("cdf", a, r, t))
            for k in range(1, 9):
                fixed = 0
                for e in range(a + 1):
                    x = e
                    for _ in range(k):
                        x = coordinate_step(a, r, x)
                    fixed += x == e
                expected = int(a % (r + 1) == 0) if k % 2 else 2 + int(a % (r + 1) == 0)
                check(fixed == expected, ("fixed", a, r, k))
    return states_checked


def divisor_lane():
    ideal_states = 0
    for n in range(2, 1001):
        fac = factor(n)
        ds = divisors(n)
        for r in range(2, 9):
            predicted_recurrent = 1
            predicted_fixed = 1
            for _, a in fac:
                epsilon = int(a % (r + 1) == 0)
                predicted_recurrent *= 2 + epsilon
                predicted_fixed *= epsilon
            observed_recurrent = 0
            depth_hist = Counter()
            for d in ds:
                ideal_states += 1
                coord = valuations(d, fac)
                literal = literal_step(n, r, d)
                predicted_coord = tuple(coordinate_step(a, r, e)
                                        for e, (_, a) in zip(coord, fac))
                check(valuations(literal, fac) == predicted_coord,
                      ("crt-step", n, r, d))
                observed_depth = literal_depth(lambda x: literal_step(n, r, x), d,
                                               2 * max(a for _, a in fac) + 6)
                predicted_depth = max(coordinate_depth_formula(a, r, e)
                                      for e, (_, a) in zip(coord, fac))
                check(observed_depth == predicted_depth, ("crt-depth", n, r, d))
                depth_hist[observed_depth] += 1
                observed_recurrent += observed_depth == 0
            check(observed_recurrent == predicted_recurrent, ("crt-rec", n, r))
            for t in range(max(depth_hist) + 1):
                observed = sum(v for depth, v in depth_hist.items() if depth <= t)
                predicted = 1
                for _, a in fac:
                    predicted *= cdf_formula(a, r, t)
                check(observed == predicted, ("crt-cdf", n, r, t))
            for k in range(1, 7):
                observed = 0
                for d in ds:
                    x = d
                    for _ in range(k):
                        x = literal_step(n, r, x)
                    observed += x == d
                expected = predicted_fixed if k % 2 else predicted_recurrent
                check(observed == expected, ("crt-fixed", n, r, k))
            # Recurrent points must partition into fixed points and 2-cycles.
            check((predicted_recurrent - predicted_fixed) % 2 == 0,
                  ("cycle-integrality", n, r))
    return ideal_states


def main():
    coordinate_states = coordinate_lane()
    ideal_states = divisor_lane()
    print("annihilator-power ideal dynamics exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"coordinate_states={coordinate_states}")
    print(f"literal_divisor_ideal_states={ideal_states}")
    print("coordinate_grid=r=2..10, a=1..80")
    print("literal_moduli=N=2..1000, r=2..8")


if __name__ == "__main__":
    main()
