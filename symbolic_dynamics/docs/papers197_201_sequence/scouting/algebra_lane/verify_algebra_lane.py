#!/usr/bin/env python3
"""Dependency-free exact verifier for the P197--P201 algebra lane.

The program imports only the Python standard library and does not import any
paper or scouting code.  It verifies the frozen SDD contract, the Zadeh
reserve theorem, and representative exact boxes for every killed control.
On success it rewrites CANONICAL.txt next to this file.
"""

from array import array
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path


ASSERTIONS = 0
FAILURES = []


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        FAILURES.append(label)


def check_eq(actual, expected, label):
    check(actual == expected, f"{label}: actual={actual!r}, expected={expected!r}")


def fmt_hist(hist):
    return ",".join(f"{k}:{hist[k]}" for k in sorted(hist))


def summarize(states, step):
    states = list(states)
    index = {x: i for i, x in enumerate(states)}
    check_eq(len(index), len(states), "carrier has unique encodings")
    nxt = []
    for x in states:
        y = step(x)
        check(y in index, f"self-map closure at {x!r}")
        nxt.append(index[y])

    n = len(states)
    depth = [-1] * n
    period = [-1] * n
    for source in range(n):
        if depth[source] >= 0:
            continue
        path = []
        local = {}
        u = source
        while depth[u] < 0 and u not in local:
            local[u] = len(path)
            path.append(u)
            u = nxt[u]
        if depth[u] >= 0:
            d = depth[u]
            per = period[u]
            for v in reversed(path):
                d += 1
                depth[v] = d
                period[v] = per
        else:
            first = local[u]
            per = len(path) - first
            for v in path[first:]:
                depth[v] = 0
                period[v] = per
            d = 0
            for v in reversed(path[:first]):
                d += 1
                depth[v] = d
                period[v] = per

    indegree = Counter(nxt)
    recurrent_period_states = Counter(
        period[i] for i in range(n) if depth[i] == 0
    )
    cycles = {
        per: count // per for per, count in sorted(recurrent_period_states.items())
    }
    max_fibre = max(indegree.values()) if indegree else 0
    return {
        "states": n,
        "image": len(indegree),
        "fixed": sum(i == nxt[i] for i in range(n)),
        "recurrent": sum(d == 0 for d in depth),
        "max_tail": max(depth),
        "depth": dict(sorted(Counter(depth).items())),
        "period_states": dict(sorted(Counter(period).items())),
        "cycles": cycles,
        "max_fibre": max_fibre,
        "max_fibre_targets": sum(v == max_fibre for v in indegree.values()),
        "fibre": dict(sorted(Counter(indegree.get(i, 0) for i in range(n)).items())),
    }


# ---------------------------------------------------------------------------
# Self-displacement difference and its affine/fixed-point contract


def sdd_step(f, p):
    return tuple((f[(x + f[x]) % p] - f[x]) % p for x in range(p))


def affine_function(a, b, p):
    return tuple((a * x + b) % p for x in range(p))


def affine_step(z, p):
    a, b = z
    return a * a % p, a * b % p


def affine_iterate_formula(z, t, p):
    a, b = z
    if t == 0:
        return z
    exponent = 1 << t
    return pow(a, exponent, p), b * pow(a, exponent - 1, p) % p


def multiplicative_order(a, p):
    check(a % p != 0, "multiplicative order called on a unit")
    value = 1
    for order in range(1, p):
        value = value * a % p
        if value == 1:
            return order
    raise AssertionError("unit order not found")


def order_of_two_mod_odd(r):
    check(r % 2 == 1, "odd part is odd")
    if r == 1:
        return 1
    value = 1
    for order in range(1, r + 1):
        value = 2 * value % r
        if value == 1:
            return order
    raise AssertionError("order of two not found")


def nu2(n):
    value = 0
    while n % 2 == 0:
        value += 1
        n //= 2
    return value


def affine_orbit_data(z, p):
    local = {}
    x = z
    path = []
    while x not in local:
        local[x] = len(path)
        path.append(x)
        x = affine_step(x, p)
    return local[x], len(path) - local[x]


def affine_fibre_formula(A, B, t, p):
    check(t >= 1, "positive time in affine fibre formula")
    if A == 0:
        return p if B == 0 else 0
    exponent = 1 << t
    return sum(pow(a, exponent, p) == A for a in range(1, p))


def lifted_L(z, p):
    x, a = z
    return (x + a) % p, 2 * a % p


def nonzero_lifted_orbits(p):
    unseen = {(x, a) for x in range(p) for a in range(1, p)}
    answer = []
    while unseen:
        seed = min(unseen)
        orbit = []
        z = seed
        while z not in orbit:
            orbit.append(z)
            z = lifted_L(z, p)
        check_eq(z, seed, "lifted orbit closes at its seed")
        for point in orbit:
            unseen.remove(point)
        xs = [x for x, _ in orbit]
        check_eq(len(xs), len(set(xs)), "nonzero orbit projects injectively")
        mask = sum(1 << x for x in xs)
        answer.append((tuple(orbit), mask))
    return answer


def matching_count(edge_masks):
    @lru_cache(None)
    def rec(position, used):
        if position == len(edge_masks):
            return 1
        total = rec(position + 1, used)
        edge = edge_masks[position]
        if edge & used == 0:
            total += rec(position + 1, used | edge)
        return total

    return rec(0, 0)


def encoded_sdd_summary(p):
    """Memory-bounded full functional graph, used for the p=7 audit."""
    n = p ** p
    powers = [1]
    for _ in range(p):
        powers.append(powers[-1] * p)
    nxt = array("I", [0]) * n
    indegree = array("I", [0]) * n
    values = [0] * p
    for code in range(n):
        quotient = code
        for x in range(p):
            values[x] = quotient % p
            quotient //= p
        out = 0
        for x in range(p):
            y = (x + values[x]) % p
            out += ((values[y] - values[x]) % p) * powers[x]
        nxt[code] = out
        indegree[out] += 1

    depth = array("i", [-1]) * n
    period = array("i", [-1]) * n
    seen = array("i", [0]) * n
    position = array("i", [0]) * n
    stamp = 0
    for source in range(n):
        if depth[source] >= 0:
            continue
        stamp += 1
        path = []
        u = source
        while depth[u] < 0 and seen[u] != stamp:
            seen[u] = stamp
            position[u] = len(path)
            path.append(u)
            u = nxt[u]
        if depth[u] >= 0:
            d = depth[u]
            per = period[u]
            for v in reversed(path):
                d += 1
                depth[v] = d
                period[v] = per
        else:
            first = position[u]
            per = len(path) - first
            for v in path[first:]:
                depth[v] = 0
                period[v] = per
            d = 0
            for v in reversed(path[:first]):
                d += 1
                depth[v] = d
                period[v] = per

    recurrent_period_states = Counter(
        period[i] for i in range(n) if depth[i] == 0
    )
    cycles = {
        per: count // per for per, count in sorted(recurrent_period_states.items())
    }
    max_fibre = max(indegree)
    return {
        "states": n,
        "image": sum(value > 0 for value in indegree),
        "fixed": sum(nxt[i] == i for i in range(n)),
        "recurrent": sum(value == 0 for value in depth),
        "max_tail": max(depth),
        "depth": dict(sorted(Counter(depth).items())),
        "period_states": dict(sorted(Counter(period).items())),
        "cycles": cycles,
        "max_fibre": max_fibre,
        "max_fibre_targets": sum(value == max_fibre for value in indegree),
    }


def verify_sdd(canonical):
    primes = [3, 5, 7, 11, 13, 17, 19]
    expected_matchings = {3: 4, 5: 6, 7: 22, 11: 12, 13: 14, 17: 52, 19: 20}
    for p in primes:
        affine_states = list(product(range(p), repeat=2))
        for a, b in affine_states:
            check_eq(
                sdd_step(affine_function(a, b, p), p),
                affine_function(*affine_step((a, b), p), p),
                f"SDD affine closure p={p}, a={a}, b={b}",
            )
            state = (a, b)
            for t in range(9):
                check_eq(
                    state,
                    affine_iterate_formula((a, b), t, p),
                    f"SDD affine iterate p={p}, a={a}, b={b}, t={t}",
                )
                state = affine_step(state, p)

            depth, period = affine_orbit_data((a, b), p)
            if a == 0:
                expected = (0, 1) if b == 0 else (1, 1)
            else:
                order = multiplicative_order(a, p)
                two_part = nu2(order)
                expected = (two_part, order_of_two_mod_odd(order >> two_part))
            check_eq((depth, period), expected, f"SDD affine orbit p={p}, a={a}, b={b}")

        for t in range(1, 9):
            targets = Counter(affine_iterate_formula(z, t, p) for z in affine_states)
            expected_fibres = {
                (A, B): affine_fibre_formula(A, B, t, p)
                for A, B in affine_states
            }
            expected_fibres = {z: value for z, value in expected_fibres.items() if value}
            check_eq(targets, Counter(expected_fibres), f"SDD affine fibres p={p}, t={t}")
            actual_fixed = sum(affine_iterate_formula(z, t, p) == z for z in affine_states)
            expected_fixed = 1 + p * gcd(p - 1, (1 << t) - 1)
            check_eq(actual_fixed, expected_fixed, f"SDD affine Fix(D^{t}) p={p}")

        orbits = nonzero_lifted_orbits(p)
        matchings = matching_count(tuple(mask for _, mask in orbits))
        check_eq(matchings, expected_matchings[p], f"SDD orbit-matching count p={p}")
        order_two = multiplicative_order(2, p)
        if order_two == p - 1:
            check_eq(matchings, p + 1, f"SDD primitive-root corollary p={p}")
        if p <= 7:
            fixed_functions = sum(
                sdd_step(f, p) == f for f in product(range(p), repeat=p)
            )
            check_eq(fixed_functions, matchings, f"SDD fixed graphs equal matchings p={p}")
        canonical.append(
            f"SDD_MATCH p={p} ord2={order_two} nonzero_L_orbits={len(orbits)} fixed={matchings}"
        )

    expected_small = {
        2: {"states": 4, "image": 3, "fixed": 3, "recurrent": 3,
            "max_tail": 1, "cycles": {1: 3}, "max_fibre": 2},
        3: {"states": 27, "image": 10, "fixed": 4, "recurrent": 10,
            "max_tail": 1, "cycles": {1: 4, 2: 3}, "max_fibre": 4},
        5: {"states": 3125, "image": 981, "fixed": 6, "recurrent": 126,
            "max_tail": 5, "cycles": {1: 6, 2: 30, 6: 10}, "max_fibre": 14},
    }
    for p, expected in expected_small.items():
        summary = summarize(product(range(p), repeat=p), lambda f, pp=p: sdd_step(f, pp))
        for key, value in expected.items():
            check_eq(summary[key], value, f"SDD full summary p={p} key={key}")
        canonical.append(
            f"SDD_FULL p={p} states={summary['states']} image={summary['image']} "
            f"fixed={summary['fixed']} recurrent={summary['recurrent']} "
            f"max_tail={summary['max_tail']} cycles={fmt_hist(summary['cycles'])} "
            f"max_fibre={summary['max_fibre']}"
        )

    p7 = encoded_sdd_summary(7)
    expected_p7 = {
        "states": 823543,
        "image": 186740,
        "fixed": 22,
        "recurrent": 2416,
        "max_tail": 12,
        "depth": {0: 2416, 1: 65890, 2: 175308, 3: 190785, 4: 147245,
                  5: 105903, 6: 62496, 7: 38430, 8: 18312, 9: 11382,
                  10: 4494, 11: 798, 12: 84},
        "period_states": {1: 4767, 2: 277039, 3: 38661, 4: 93744,
                          6: 409164, 12: 168},
        "cycles": {1: 22, 2: 588, 3: 126, 4: 42, 6: 98, 12: 7},
        "max_fibre": 298,
        "max_fibre_targets": 7,
    }
    for key, value in expected_p7.items():
        check_eq(p7[key], value, f"SDD encoded full summary p=7 key={key}")
    canonical.append(
        f"SDD_FULL p=7 states={p7['states']} image={p7['image']} fixed={p7['fixed']} "
        f"recurrent={p7['recurrent']} max_tail={p7['max_tail']} "
        f"cycles={fmt_hist(p7['cycles'])} max_fibre={p7['max_fibre']}"
    )


# ---------------------------------------------------------------------------
# Zadeh cyclic implication reserve


def zadeh_step(x, M):
    return tuple(
        max(M - x[i], min(x[i], x[(i + 1) % len(x)]))
        for i in range(len(x))
    )


def zadeh_core(x, M):
    centered = [2 * value - M for value in x]
    magnitudes = {abs(value) for value in centered}
    if len(magnitudes) != 1:
        return False
    magnitude = next(iter(magnitudes))
    if magnitude == 0:
        return True
    negative = [value < 0 for value in centered]
    return not any(negative[i] and negative[(i + 1) % len(x)] for i in range(len(x)))


def lucas_independent_cycle(n):
    matrix = ((1, 1), (1, 0))

    def multiply(A, B):
        return tuple(
            tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
            for i in range(2)
        )

    power = ((1, 0), (0, 1))
    for _ in range(n):
        power = multiply(power, matrix)
    return power[0][0] + power[1][1]


def zadeh_fibre_trace(target, M):
    size = M + 1
    matrices = []
    for y in target:
        matrix = [[0] * size for _ in range(size)]
        for a, b in product(range(size), repeat=2):
            matrix[a][b] = int(max(M - a, min(a, b)) == y)
        matrices.append(matrix)

    current = [[int(i == j) for j in range(size)] for i in range(size)]
    for matrix in matrices:
        current = [
            [sum(current[i][k] * matrix[k][j] for k in range(size)) for j in range(size)]
            for i in range(size)
        ]
    return sum(current[i][i] for i in range(size))


def verify_zadeh(canonical):
    expected = {
        2: {
            "image": [14, 34, 82, 198, 478, 1154],
            "recurrent": [5, 8, 12, 19, 30, 48],
            "max_fibre": [4, 7, 11, 18, 29, 47],
            "max_targets": [1, 1, 1, 1, 1, 1],
        },
        3: {
            "image": [26, 82, 242, 730, 2186, 6562],
            "recurrent": [8, 14, 22, 36, 58, 94],
            "max_fibre": [5, 10, 18, 31, 52, 100],
            "max_targets": [4, 4, 5, 6, 7, 4],
        },
    }
    for M in [2, 3]:
        for offset, m in enumerate(range(3, 9)):
            states = list(product(range(M + 1), repeat=m))
            summary = summarize(states, lambda x, MM=M: zadeh_step(x, MM))
            check_eq(summary["image"], expected[M]["image"][offset], f"ZCI image M={M},m={m}")
            check_eq(summary["recurrent"], expected[M]["recurrent"][offset], f"ZCI recurrent M={M},m={m}")
            check_eq(summary["fixed"], 2, f"ZCI fixed M={M},m={m}")
            check_eq(summary["max_tail"], m, f"ZCI sharp tail M={M},m={m}")
            check_eq(summary["max_fibre"], expected[M]["max_fibre"][offset], f"ZCI max fibre M={M},m={m}")
            check_eq(summary["max_fibre_targets"], expected[M]["max_targets"][offset], f"ZCI max targets M={M},m={m}")

            predicted_recurrent = ((M + 1) // 2) * lucas_independent_cycle(m) + int(M % 2 == 0)
            check_eq(summary["recurrent"], predicted_recurrent, f"ZCI recurrent formula M={M},m={m}")
            for t in range(1, m + 1):
                actual_iterate_fixed = sum(
                    length * count for length, count in summary["cycles"].items()
                    if t % length == 0
                )
                predicted = ((M + 1) // 2) * lucas_independent_cycle(gcd(m, t)) + int(M % 2 == 0)
                check_eq(actual_iterate_fixed, predicted, f"ZCI Fix(T^{t}) M={M},m={m}")

            lands_in_core = True
            fibre_direct = Counter()
            for x in states:
                y = x
                for _ in range(m):
                    y = zadeh_step(y, M)
                if not zadeh_core(y, M):
                    lands_in_core = False
                    break
                fibre_direct[zadeh_step(x, M)] += 1
            check(lands_in_core, f"ZCI T^m lands in core M={M},m={m}")
            if m <= 5:
                check(
                    all(zadeh_fibre_trace(y, M) == count for y, count in fibre_direct.items()),
                    f"ZCI local transfer trace on reached targets M={M},m={m}",
                )
                check(
                    all(zadeh_fibre_trace(y, M) == 0 for y in states if y not in fibre_direct),
                    f"ZCI local transfer trace on missing targets M={M},m={m}",
                )

            canonical.append(
                f"ZCI M={M} m={m} states={summary['states']} image={summary['image']} "
                f"fixed={summary['fixed']} recurrent={summary['recurrent']} "
                f"max_tail={summary['max_tail']} cycles={fmt_hist(summary['cycles'])} "
                f"max_fibre={summary['max_fibre']} max_targets={summary['max_fibre_targets']}"
            )

    for m in range(3, 9):
        summary = summarize(product(range(2), repeat=m), lambda x: zadeh_step(x, 1))
        check_eq(summary["max_tail"], 1, f"ZCI M=1 exceptional clock m={m}")


# ---------------------------------------------------------------------------
# Killed controls


S3 = tuple(permutations(range(3)))


def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    answer = [0] * len(p)
    for i, value in enumerate(p):
        answer[value] = i
    return tuple(answer)


def conjugation_ca_step(x):
    return tuple(
        perm_mul(perm_mul(perm_inv(x[(i + 1) % len(x)]), x[i]), x[(i + 1) % len(x)])
        for i in range(len(x))
    )


def least_nonsquare_vieta_step(z, p):
    squares = {x * x % p for x in range(1, p)}
    x, y, w = z
    for i, value in enumerate(z):
        if value != 0 and value not in squares:
            if i == 0:
                return (y * w - x) % p, y, w
            if i == 1:
                return x, (x * w - y) % p, w
            return x, y, (x * y - w) % p
    return z


def quadratic_translation_step(z, p):
    a, b = z
    return (a + 2 * b) % p, (b * b + a * b + b) % p


def star_implication(r, A, B):
    top = (1 << r) - 1
    if A == -1:
        return top
    if B == -1:
        return -1
    return ((~A) & top) | B


def star_cyclic_step(x, r):
    return tuple(star_implication(r, x[i], x[(i + 1) % len(x)]) for i in range(len(x)))


def chain_cyclic_step(x, rule):
    return tuple(rule(x[i], x[(i + 1) % len(x)]) for i in range(len(x)))


def mat_mul(A, B, p):
    return (
        (A[0] * B[0] + A[1] * B[2]) % p,
        (A[0] * B[1] + A[1] * B[3]) % p,
        (A[2] * B[0] + A[3] * B[2]) % p,
        (A[2] * B[1] + A[3] * B[3]) % p,
    )


def anticommutator_step(z, p):
    A, B = z
    AB = mat_mul(A, B, p)
    BA = mat_mul(B, A, p)
    return B, tuple((u + v) % p for u, v in zip(AB, BA))


def boolean_esymmetric_step(z, k):
    answer = []
    for size in range(1, k + 1):
        value = 0
        for indices in combinations(range(k), size):
            term = z[indices[0]]
            for i in indices[1:]:
                term &= z[i]
            value ^= term
        answer.append(value)
    return tuple(answer)


def steiner_product(x, y):
    return x if x == y else x ^ y


def steiner_cyclic_step(x):
    return tuple(steiner_product(x[i], x[(i + 1) % len(x)]) for i in range(len(x)))


def star_meet(A, B):
    if A == -1 or B == -1:
        return -1
    return A & B


def verify_control(name, states, step, expected, canonical):
    summary = summarize(states, step)
    for key, value in expected.items():
        check_eq(summary[key], value, f"{name} summary key={key}")
    canonical.append(
        f"CONTROL {name} states={summary['states']} image={summary['image']} "
        f"fixed={summary['fixed']} recurrent={summary['recurrent']} "
        f"max_tail={summary['max_tail']} cycles={fmt_hist(summary['cycles'])} "
        f"max_fibre={summary['max_fibre']}"
    )
    return summary


def verify_killed_controls(canonical):
    verify_control(
        "CRC_S3_m3", product(S3, repeat=3), conjugation_ca_step,
        {"states": 216, "image": 216, "fixed": 48, "recurrent": 216,
         "max_tail": 0, "cycles": {1: 48, 2: 18, 3: 14, 6: 15}, "max_fibre": 1},
        canonical,
    )
    verify_control(
        "CRC_S3_m4", product(S3, repeat=4), conjugation_ca_step,
        {"states": 1296, "image": 1242, "fixed": 162, "recurrent": 1242,
         "max_tail": 1, "cycles": {1: 162, 2: 168, 3: 32, 6: 104, 8: 3}, "max_fibre": 3},
        canonical,
    )

    for p, expected in [
        (11, {"states": 1331, "image": 848, "fixed": 316, "recurrent": 666,
              "max_tail": 3, "cycles": {1: 316, 2: 175}, "max_fibre": 4}),
        (13, {"states": 2197, "image": 1513, "fixed": 487, "recurrent": 1333,
              "max_tail": 3, "cycles": {1: 487, 2: 423}, "max_fibre": 4}),
    ]:
        summary = verify_control(
            f"LNV_p{p}", product(range(p), repeat=3),
            lambda z, pp=p: least_nonsquare_vieta_step(z, pp), expected, canonical,
        )
        check(
            all(
                (z[0] * z[0] + z[1] * z[1] + z[2] * z[2] - z[0] * z[1] * z[2]) % p
                ==
                (least_nonsquare_vieta_step(z, p)[0] ** 2
                 + least_nonsquare_vieta_step(z, p)[1] ** 2
                 + least_nonsquare_vieta_step(z, p)[2] ** 2
                 - least_nonsquare_vieta_step(z, p)[0]
                 * least_nonsquare_vieta_step(z, p)[1]
                 * least_nonsquare_vieta_step(z, p)[2]) % p
                for z in product(range(p), repeat=3)
            ),
            f"LNV Markoff invariant p={p}",
        )
        check(summary["fixed"] > ((p + 1) // 2) ** 3, f"LNV selected involutions add fixed points p={p}")

    verify_control(
        "QCT_p11", product(range(11), repeat=2),
        lambda z: quadratic_translation_step(z, 11),
        {"states": 121, "image": 66, "fixed": 11, "recurrent": 39,
         "max_tail": 5, "cycles": {1: 11, 2: 5, 3: 3, 4: 1, 5: 1}, "max_fibre": 2},
        canonical,
    )
    inv2 = pow(2, -1, 11)
    # Directly verify the useful coordinate reduction without a symbolic package.
    for a, b in product(range(11), repeat=2):
        s = a * inv2 % 11
        c = (b - s * s) % 11
        A, B = quadratic_translation_step((a, b), 11)
        S = A * inv2 % 11
        C = (B - S * S) % 11
        check_eq(C, c, "QCT invariant c")
        check_eq(S, (s * s + s + c) % 11, "QCT scalar quadratic reduction")

    H3 = tuple([-1] + list(range(8)))
    verify_control(
        "SHI_r3_m4", product(H3, repeat=4), lambda x: star_cyclic_step(x, 3),
        {"states": 6561, "image": 453, "fixed": 1, "recurrent": 453,
         "max_tail": 1, "cycles": {1: 1, 2: 14, 4: 106}, "max_fibre": 99},
        canonical,
    )
    check(
        all(
            star_cyclic_step(star_cyclic_step(x, 3), 3) == star_cyclic_step(x, 3)[1:] + star_cyclic_step(x, 3)[:1]
            for x in product(H3, repeat=4)
        ),
        "SHI identity T^2=rho*T",
    )

    M, m = 3, 5
    fodor = lambda a, b: M if a <= b else max(M - a, b)
    verify_control(
        "FCI_M3_m5", product(range(M + 1), repeat=m),
        lambda x: chain_cyclic_step(x, fodor),
        {"states": 1024, "image": 106, "fixed": 1, "recurrent": 81,
         "max_tail": 2, "cycles": {1: 1, 5: 16}, "max_fibre": 24},
        canonical,
    )

    M, m = 3, 4
    gr = lambda a, b: M if a <= b else 0
    verify_control(
        "GRC_M3_m4", product(range(M + 1), repeat=m),
        lambda x: chain_cyclic_step(x, gr),
        {"states": 256, "image": 15, "fixed": 1, "recurrent": 7,
         "max_tail": 2, "cycles": {1: 1, 2: 1, 4: 1}, "max_fibre": 34},
        canonical,
    )
    check(
        all(set(chain_cyclic_step(x, gr)) <= {0, M} for x in product(range(M + 1), repeat=m)),
        "GRC first image is binary",
    )

    M, m = 3, 5
    kd = lambda a, b: max(M - a, b)
    verify_control(
        "KDC_M3_m5", product(range(M + 1), repeat=m),
        lambda x: chain_cyclic_step(x, kd),
        {"states": 1024, "image": 197, "fixed": 2, "recurrent": 197,
         "max_tail": 1, "cycles": {1: 2, 5: 39}, "max_fibre": 10},
        canonical,
    )
    check(
        all(
            chain_cyclic_step(chain_cyclic_step(x, kd), kd)
            == chain_cyclic_step(x, kd)[1:] + chain_cyclic_step(x, kd)[:1]
            for x in product(range(M + 1), repeat=m)
        ),
        "KDC identity T^2=rho*T",
    )

    for p, expected in [
        (2, {"states": 256, "image": 58, "fixed": 1, "recurrent": 1,
             "max_tail": 4, "cycles": {1: 1}, "max_fibre": 16}),
        (3, {"states": 6561, "image": 3313, "fixed": 14, "recurrent": 625,
             "max_tail": 8,
             "cycles": {1: 14, 3: 101, 6: 6, 8: 4, 12: 12, 24: 4},
             "max_fibre": 81}),
    ]:
        matrices = tuple(product(range(p), repeat=4))
        verify_control(
            f"MAR_p{p}", product(matrices, repeat=2),
            lambda z, pp=p: anticommutator_step(z, pp), expected, canonical,
        )

    verify_control(
        "BES_k5_r2", product(range(4), repeat=5),
        lambda z: boolean_esymmetric_step(z, 5),
        {"states": 1024, "image": 36, "fixed": 9, "recurrent": 9,
         "max_tail": 2, "cycles": {1: 9}, "max_fibre": 100},
        canonical,
    )

    for d, m, expected in [
        (3, 4, {"states": 2401, "image": 1057, "fixed": 7, "recurrent": 175,
                "max_tail": 4, "cycles": {1: 7, 8: 21}, "max_fibre": 7}),
        (4, 4, {"states": 50625, "image": 13665, "fixed": 15, "recurrent": 855,
                "max_tail": 4, "cycles": {1: 15, 8: 105}, "max_fibre": 15}),
    ]:
        verify_control(
            f"BPS_d{d}_m{m}", product(range(1, 1 << d), repeat=m),
            steiner_cyclic_step, expected, canonical,
        )

    H4 = tuple([-1] + list(range(16)))
    verify_control(
        "HEYTING_SPLIT_r4", product(H4, repeat=2),
        lambda z: (star_meet(z[0], z[1]), star_implication(4, z[0], z[1])),
        {"states": 289, "image": 83, "fixed": 17, "recurrent": 17,
         "max_tail": 2, "cycles": {1: 17}, "max_fibre": 17},
        canonical,
    )
    top = 15
    check(
        all(
            (lambda first: (star_meet(first[0], first[1]), star_implication(4, first[0], first[1])))
            ((star_meet(A, B), star_implication(4, A, B)))
            == (star_meet(A, B), top)
            for A, B in product(H4, repeat=2)
        ),
        "Heyting split identity T^2=(meet,top)",
    )


def main():
    canonical = [
        "P197-P201 ALGEBRA LANE EXACT CANONICAL",
        "DEPENDENCIES=PYTHON_STANDARD_LIBRARY_ONLY",
        "NOVELTY_CLAIM=NO",
        "OWNER_STATUS=OWNER_AMBER/HOLD_EXTERNAL",
    ]
    verify_sdd(canonical)
    verify_zadeh(canonical)
    verify_killed_controls(canonical)

    if FAILURES:
        print(f"ASSERTIONS={ASSERTIONS}")
        print(f"FAILURES={len(FAILURES)}")
        for failure in FAILURES[:50]:
            print("FAIL", failure)
        raise SystemExit(1)

    canonical.extend([
        f"ASSERTIONS={ASSERTIONS}",
        "FAILURES=0",
        "STATUS=PASS",
    ])
    payload = "\n".join(canonical) + "\n"
    output = Path(__file__).with_name("CANONICAL.txt")
    output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
