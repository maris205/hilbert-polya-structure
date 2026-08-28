#!/usr/bin/env python3
"""Exact controls for the finite-ring Rule 184 paper."""

from collections import Counter, defaultdict
from itertools import product
from math import comb, gcd


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def rule184(x):
    n = len(x)
    return tuple(
        x[i] * x[(i + 1) % n] + x[(i - 1) % n] * (1 - x[i])
        for i in range(n)
    )


def iterate(x, steps):
    for _ in range(steps):
        x = rule184(x)
    return x


def avoids(x, pair):
    n = len(x)
    return all((x[i], x[(i + 1) % n]) != pair for i in range(n))


def in_core(x):
    return avoids(x, (1, 1)) or avoids(x, (0, 0))


def particle_hole_reflection(x):
    n = len(x)
    return tuple(1 - x[(-i) % n] for i in range(n))


def lucas(n):
    if n == 0:
        return 2
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def hard_core(n, j):
    if j < 0 or 2 * j > n:
        return 0
    if j == 0:
        return 1
    return n * comb(n - j - 1, j - 1) // j


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        value = -value
    return value


def fixed_polynomial(n, k):
    d = gcd(n, k)
    r = n // d
    ans = Counter()
    for j in range(d // 2 + 1):
        h = hard_core(d, j)
        ans[r * j] += h
        ans[n - r * j] += h
    if d % 2 == 0:
        ans[n // 2] -= 2
    return +ans


def orbit_formula(n, ell):
    if n % ell:
        return 0
    primitive_points = 2 * sum(
        mobius(ell // e) * lucas(e) for e in divisors(ell)
    )
    return primitive_points // ell - int(ell == 2)


def primitive_hard_core(ell, j):
    return sum(
        mobius(e) * hard_core(ell // e, j // e)
        for e in divisors(gcd(ell, j))
    )


def particle_orbit_formula(n, ell, weight):
    if n % ell:
        return 0
    if 2 * weight == n:
        return int(ell == 2 and n % 2 == 0)
    low_weight = min(weight, n - weight)
    r = n // ell
    if low_weight % r:
        return 0
    j = low_weight // r
    if 2 * j >= ell:
        return 0
    return primitive_hard_core(ell, j) // ell


def core_cycles(n):
    unseen = {x for x in product((0, 1), repeat=n) if in_core(x)}
    cycles = []
    while unseen:
        start = next(iter(unseen))
        orbit = []
        x = start
        while x not in orbit:
            orbit.append(x)
            x = rule184(x)
        check(x == start, f"core is not permuted for n={n}")
        for y in orbit:
            unseen.remove(y)
        cycles.append(orbit)
    return cycles


def entry_depth(x):
    depth = 0
    while not in_core(x):
        x = rule184(x)
        depth += 1
        check(depth <= len(x), "entry bound unexpectedly exceeded")
    return depth


def lifted_positions(x):
    return [i for i, bit in enumerate(x) if bit]


def lift_at(pos, n, j):
    m = len(pos)
    q, r = divmod(j, m)
    return pos[r] + q * n


def min_plus_positions(pos, n, t):
    m = len(pos)
    return [
        min(lift_at(pos, n, j + r) + t - 2 * r for r in range(t + 1))
        for j in range(m)
    ]


def direct_lifted_positions(pos, n, t):
    m = len(pos)
    cur = list(pos)
    for _ in range(t):
        cur = [min(cur[j] + 1, (cur[j + 1] if j + 1 < m else cur[0] + n) - 1)
               for j in range(m)]
    return cur


def check_hard_core_counts():
    for n in range(1, 17):
        by_weight = Counter()
        for x in product((0, 1), repeat=n):
            if avoids(x, (1, 1)):
                by_weight[sum(x)] += 1
        for j in range(n + 1):
            check(by_weight[j] == hard_core(n, j), (n, j, by_weight[j]))
        check(sum(by_weight.values()) == lucas(n), (n, by_weight))


def check_fixed_polynomials():
    for n in range(1, 13):
        states = list(product((0, 1), repeat=n))
        for k in range(1, 2 * n + 1):
            actual = Counter(sum(x) for x in states if iterate(x, k) == x)
            expected = fixed_polynomial(n, k)
            check(actual == expected, (n, k, actual, expected))
            d = gcd(n, k)
            check(sum(actual.values()) == 2 * lucas(d) - 2 * int(d % 2 == 0))


def check_core_and_depth():
    global_depths = []
    for n in range(1, 15):
        maxima = defaultdict(int)
        core_count = 0
        for x in product((0, 1), repeat=n):
            y = rule184(x)
            check(sum(y) == sum(x), (n, x, y))
            theta_x = particle_hole_reflection(x)
            check(rule184(theta_x) == particle_hole_reflection(y),
                  ("particle-hole reflection", n, x))
            check(in_core(theta_x) == in_core(x),
                  ("core reflection", n, x))
            if in_core(x):
                core_count += 1
                check(in_core(y), (n, x, y))
            depth = entry_depth(x)
            maxima[sum(x)] = max(maxima[sum(x)], depth)
        check(core_count == 2 * lucas(n) - 2 * int(n % 2 == 0), n)
        for weight in range(n + 1):
            target = max(0, min(weight, n - weight) - 1)
            check(maxima[weight] == target, (n, weight, maxima[weight], target))
            witness = (1,) * weight + (0,) * (n - weight)
            check(entry_depth(witness) == target,
                  ("solid-block witness", n, weight, target))
        global_depths.append(max(maxima.values()))
    check(global_depths == [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6])


def check_min_plus_formula():
    for n in range(2, 13):
        for x in product((0, 1), repeat=n):
            m = sum(x)
            if not (1 <= m <= n // 2):
                continue
            pos = lifted_positions(x)
            for t in range(2 * n + 1):
                check(min_plus_positions(pos, n, t) == direct_lifted_positions(pos, n, t),
                      (n, x, t))
            final = min_plus_positions(pos, n, m - 1)
            gaps = [
                (final[j + 1] if j + 1 < m else final[0] + n) - final[j]
                for j in range(m)
            ]
            check(min(gaps) >= 2, (n, x, final, gaps))


def check_orbit_ledgers():
    for n in range(1, 14):
        cycles = core_cycles(n)
        actual = Counter(len(c) for c in cycles)
        actual_weighted = Counter((len(c), sum(c[0])) for c in cycles)
        for ell in range(1, n + 1):
            check(actual[ell] == orbit_formula(n, ell), (n, ell, actual[ell]))
            for weight in range(n + 1):
                check(
                    actual_weighted[(ell, weight)] == particle_orbit_formula(n, ell, weight),
                    (n, ell, weight, actual_weighted[(ell, weight)]),
                )
        for k in range(1, 2 * n + 1):
            reconstructed = sum(ell * count for ell, count in actual.items() if k % ell == 0)
            d = gcd(n, k)
            check(reconstructed == 2 * lucas(d) - 2 * int(d % 2 == 0))


def main():
    check_hard_core_counts()
    check_fixed_polynomials()
    check_core_and_depth()
    check_min_plus_formula()
    check_orbit_ledgers()
    print(f"PASS: {ASSERTIONS:,} exact assertions")
    print("rings n<=14: reflection conjugacy, recurrent core, and sharp particle-layer entry depths verified")
    print("rings n<=12: min-plus formula through t=2n and all iterate-fixed weight polynomials verified")
    print("rings n<=13: temporal orbit and particle-resolved Mobius ledgers verified")


if __name__ == "__main__":
    main()
