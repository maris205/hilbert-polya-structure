#!/usr/bin/env python3
"""Independent hostile verifier for P166.

This program starts from T_n(x)=x+wt(x)1 on (Z/nZ)^n.  It imports no paper,
author-verifier, Gate-A, or Review-A module.  Enumeration is falsification
pressure for the separate written derivation, not a proof of all parameters.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, isqrt


ASSERTIONS = 0


def check(condition, witness):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(witness)


def encode(x, n):
    value = 0
    for digit in x:
        value = value * n + digit
    return value


def literal_step(x, n):
    weight = sum(a != 0 for a in x)
    return tuple((a + weight) % n for a in x)


def multiplicities(x, n):
    out = [0] * n
    for a in x:
        out[a] += 1
    return tuple(out)


def phase_map(m):
    n = len(m)
    return tuple((j + m[j]) % n for j in range(n))


def analyze_map(mapping):
    size = len(mapping)
    depth = [-1] * size
    period = [0] * size
    for start in range(size):
        if depth[start] >= 0:
            continue
        path = []
        where = {}
        v = start
        while depth[v] < 0 and v not in where:
            where[v] = len(path)
            path.append(v)
            v = mapping[v]
        if depth[v] >= 0:
            next_depth = depth[v] + 1
            p = period[v]
            for u in reversed(path):
                depth[u] = next_depth
                period[u] = p
                next_depth += 1
        else:
            cut = where[v]
            cycle = path[cut:]
            p = len(cycle)
            for u in cycle:
                depth[u] = 0
                period[u] = p
            next_depth = 1
            for u in reversed(path[:cut]):
                depth[u] = next_depth
                period[u] = p
                next_depth += 1
    return depth, period


def stirling2(n):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for a in range(1, n + 1):
        for b in range(1, a + 1):
            table[a][b] = table[a - 1][b - 1] + b * table[a - 1][b]
    return table


def predicted_period_points(n, k, s2):
    if k == 1:
        return 1 + (n - 1) ** n
    if 2 <= k <= n:
        return factorial(k) * s2[n][k]
    return 0


def predicted_depth_points(n, d, s2):
    if d == 0:
        return (n - 1) ** n + sum(
            factorial(k) * s2[n][k] for k in range(1, n + 1)
        )
    if 1 <= d <= n - 2:
        return factorial(d) * sum(
            comb(n, s) * s2[s][d] * (n - d - 1) ** (n - s)
            for s in range(d, n)
        )
    return 0


def predicted_fibre(y, n):
    m = multiplicities(y, n)
    answer = int(all(a == 0 for a in y)) + int(m[0] == 0)
    answer += sum(m[k] == n - k for k in range(1, n))
    return answer


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def multinomial(m):
    answer = factorial(sum(m))
    for a in m:
        answer //= factorial(a)
    return answer


def cycles(mapping):
    depth, _ = analyze_map(mapping)
    seen = set()
    out = []
    for v in range(len(mapping)):
        if depth[v] == 0 and v not in seen:
            cyc = []
            u = v
            while u not in seen:
                seen.add(u)
                cyc.append(u)
                u = mapping[u]
            out.append(tuple(cyc))
    return out


def egf_fibre_histogram(n):
    # Coefficients in z and u.  Factor zero marks m_0=0; factor r marks m=r.
    poly = {(0, 0): Fraction(1)}
    factors = []
    zero_factor = {(j, 0): Fraction(1, factorial(j)) for j in range(1, n + 1)}
    zero_factor[(0, 1)] = Fraction(1)
    factors.append(zero_factor)
    for r in range(1, n):
        factor = {(j, 0): Fraction(1, factorial(j)) for j in range(n + 1)}
        factor[(r, 0)] = Fraction(0)
        factor[(r, 1)] = Fraction(1, factorial(r))
        factors.append(factor)
    for factor in factors:
        nxt = {}
        for (za, ua), ca in poly.items():
            for (zb, ub), cb in factor.items():
                if za + zb <= n:
                    key = (za + zb, ua + ub)
                    nxt[key] = nxt.get(key, Fraction(0)) + ca * cb
        poly = nxt
    hist = Counter()
    for (zdeg, udeg), coefficient in poly.items():
        if zdeg == n:
            value = coefficient * factorial(n)
            check(value.denominator == 1, ("EGF nonintegral", n, udeg, value))
            hist[udeg] += value.numerator
    hist[0] -= 1
    hist[1] += 1
    return +hist


def max_fibre_formula(n):
    h = (isqrt(8 * n + 1) - 1) // 2
    return 1 if n == 2 else 1 + h


def exhaustive_state_checks(n):
    states = list(product(range(n), repeat=n))
    mapping = [encode(literal_step(x, n), n) for x in states]
    depth, period = analyze_map(mapping)
    fibres = Counter(mapping)
    s2 = stirling2(n)

    check(len(states) == n**n, ("state total", n))
    check(sum(fibres.values()) == n**n, ("fibre mass", n))

    actual_period = Counter(period[i] for i in range(len(states)) if depth[i] == 0)
    actual_depth = Counter(depth)
    for k in range(1, n + 2):
        check(
            actual_period[k] == predicted_period_points(n, k, s2),
            ("period formula", n, k, actual_period[k]),
        )
    for d in range(0, n + 2):
        check(
            actual_depth[d] == predicted_depth_points(n, d, s2),
            ("depth formula", n, d, actual_depth[d]),
        )

    # Literal differences are invariant; target fibres and exact equality cases.
    target_hist = Counter()
    expected_max = max_fibre_formula(n)
    for index, y in enumerate(states):
        image = states[mapping[index]]
        for a in range(1, n):
            check(
                (image[a] - image[0]) % n == (y[a] - y[0]) % n,
                ("difference invariant", n, y, a),
            )
        expected = predicted_fibre(y, n)
        actual = fibres[index]
        check(actual == expected, ("one-step fibre", n, y, actual, expected))
        target_hist[actual] += 1
        m = multiplicities(y, n)
        h = (isqrt(8 * n + 1) - 1) // 2
        middle = sum(m[k] == n - k for k in range(1, n))
        equality = n == 2 or (m[0] == 0 and middle == h)
        check(
            (actual == expected_max) == equality,
            ("maximum equality", n, y, actual, middle, h),
        )
    check(target_hist == egf_fibre_histogram(n), ("EGF histogram", n))
    check(max(fibres.values()) == expected_max, ("max fibre", n))
    check(fibres[0] == 1, ("all-zero correction", n, fibres[0]))
    check(sum(target_hist.values()) == n**n, ("EGF target mass", n))
    check(sum(k * v for k, v in target_hist.items()) == n**n, ("EGF source mass", n))

    # Full phase conjugacy for every state and every phase.
    for y in states:
        m = multiplicities(y, n)
        g = phase_map(m)
        for j in range(n):
            xj = tuple((a - j) % n for a in y)
            rhs = tuple((a - g[j]) % n for a in y)
            check(literal_step(xj, n) == rhs, ("phase conjugacy", n, y, j))

    # Direct all-time target fibres versus the independently iterated phase map.
    if n <= 6:
        image_at_t = list(range(len(states)))
        for t in range(0, 2 * n + 3):
            counts = Counter(image_at_t)
            for index, y in enumerate(states):
                m = multiplicities(y, n)
                g = phase_map(m)
                phase = list(range(n))
                for _ in range(t):
                    phase = [g[a] for a in phase]
                oracle = sum(a == 0 for a in phase)
                check(counts[index] == oracle, ("time fibre oracle", n, t, y))
            image_at_t = [mapping[a] for a in image_at_t]

    # Fixed iterates/zeta divisor conversion checked directly.
    power = list(range(len(states)))
    for r in range(1, 2 * n + 1):
        power = [mapping[a] for a in power]
        actual_fixed = sum(i == power[i] for i in range(len(states)))
        expected_fixed = sum(
            predicted_period_points(n, k, s2)
            for k in range(1, n + 1)
            if r % k == 0
        )
        check(actual_fixed == expected_fixed, ("fixed iterate", n, r))

    return (
        n,
        n**n,
        actual_depth[0],
        actual_period[1],
        max(depth),
        actual_depth[n - 2] if n >= 3 else 0,
        max(fibres.values()),
        len(fibres),
    )


def profile_checks(n):
    s2 = stirling2(n)
    weighted_depth = Counter()
    weighted_period = Counter()
    all_anchor_depth = Counter()
    profile_count = 0
    last_profiles = 0
    last_phase_pairs = 0
    for m in weak_compositions(n, n):
        profile_count += 1
        weight = multinomial(m)
        g = phase_map(m)
        depth, period = analyze_map(g)
        weighted_depth[depth[0]] += weight
        if depth[0] == 0:
            weighted_period[period[0]] += weight
        for d in depth:
            all_anchor_depth[d] += weight

        nontrivial = [c for c in cycles(g) if len(c) > 1]
        check(len(nontrivial) <= 1, ("two nontrivial cycles", n, m, nontrivial))
        for cyc in nontrivial:
            check(sum(m[j] for j in cyc) == n, ("cycle mass", n, m, cyc))
            check(set(j for j, a in enumerate(m) if a) == set(cyc), ("cycle support", n, m, cyc))
            for j in cyc:
                check(m[j] == (g[j] - j) % n, ("clockwise gap", n, m, j))

        if n >= 3:
            zeros = [j for j, a in enumerate(m) if a == 0]
            twos = [j for j, a in enumerate(m) if a == 2]
            profile_is_last = (
                len(zeros) == 1
                and len(twos) == 1
                and all(a in (0, 1, 2) for a in m)
                and twos[0] != (zeros[0] - 1) % n
            )
            actual_last_phases = {j for j, d in enumerate(depth) if d == n - 2}
            if profile_is_last:
                z = zeros[0]
                e = twos[0]
                expected = {(z + 1) % n}
                if e == (z + 1) % n:
                    expected.add((z + 2) % n)
                check(actual_last_phases == expected, ("last phases", n, m, actual_last_phases, expected))
                last_profiles += 1
                last_phase_pairs += len(expected)
            else:
                check(not actual_last_phases, ("false last profile", n, m, actual_last_phases))

    check(sum(weighted_depth.values()) == n**n, ("profile total", n))
    for d in range(n + 2):
        check(weighted_depth[d] == predicted_depth_points(n, d, s2), ("anchored depth", n, d))
        check(all_anchor_depth[d] == n * predicted_depth_points(n, d, s2), ("anchor factor", n, d))
    for k in range(1, n + 2):
        check(weighted_period[k] == predicted_period_points(n, k, s2), ("weighted period", n, k))
    if n >= 3:
        check(last_profiles == n * (n - 2), ("last profile count", n, last_profiles))
        check(last_phase_pairs == n * (n - 1), ("last anchor pairs", n, last_phase_pairs))
        check(
            weighted_depth[n - 2] == (n - 1) * factorial(n) // 2,
            ("last shell count", n, weighted_depth[n - 2]),
        )
    return n, profile_count, max(weighted_depth), weighted_depth[n - 2] if n >= 3 else 0


def max_fibre_boundary_checks():
    triangular = []
    nontriangular = []
    for n in range(2, 151):
        h = (isqrt(8 * n + 1) - 1) // 2
        check(h * (h + 1) // 2 <= n, ("h lower", n, h))
        check((h + 1) * (h + 2) // 2 > n, ("h upper", n, h))
        if n == 2:
            check(max_fibre_formula(n) == 1, ("n2 max",))
            continue
        remainder = n - h * (h + 1) // 2
        m = [0] * n
        for r in range(1, h + 1):
            m[n - r] = r
        if remainder:
            check(n >= 4 and m[1] == 0 and remainder < n - 1, ("remainder placement", n, h, remainder))
            m[1] = remainder
        check(sum(m) == n and m[0] == 0, ("max construction mass", n, m))
        middle = sum(m[k] == n - k for k in range(1, n))
        check(1 + middle == 1 + h, ("max construction", n, h, middle))
        if remainder == 0:
            triangular.append(n)
        else:
            nontriangular.append(n)
    return len(triangular), len(nontriangular), triangular[:8]


def main():
    print("P166_HOSTILE_REVIEW_B_INDEPENDENT")
    print("state rows n,states,recurrent,fixed,max_depth,last_shell,max_fibre,image")
    for n in range(2, 8):
        print("STATE", *exhaustive_state_checks(n))
    print("profile rows n,weak_compositions,max_depth,last_shell")
    for n in range(2, 11):
        print("PROFILE", *profile_checks(n))
    tri, nontri, first = max_fibre_boundary_checks()
    print("MAX_FIBRE_BOUNDARIES", tri, nontri, tuple(first))
    print("ASSERTIONS", ASSERTIONS)
    print("STATUS PASS")
    print("DECISION ACCEPT_INTERNAL")
    print("LIFECYCLE HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
