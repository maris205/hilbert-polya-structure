#!/usr/bin/env python3
"""Exact audit for the quadratic-state shear replacement candidate.

Only the Python standard library is used.  The two canonical nonsingular
quadratic forms on F_2^(2m) are exhausted through m=5.  The assertions check
the literal map, the eight-state quotient, every orbit, every one-step fibre,
the image tower, the depth layers, and the complete cycle census.
"""

from __future__ import annotations

from collections import Counter


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def quadratic(v: int, m: int, eps: int) -> int:
    """Q_+ or Q_- on F_2^(2m), represented by an integer bit vector."""
    value = 0
    first_hyperbolic_pair = 0
    if eps == -1:
        x0 = v & 1
        x1 = (v >> 1) & 1
        value = x0 ^ x1 ^ (x0 & x1)
        first_hyperbolic_pair = 1
    for i in range(first_hyperbolic_pair, m):
        value ^= ((v >> (2 * i)) & 1) & ((v >> (2 * i + 1)) & 1)
    return value


def polar(x: int, y: int, m: int) -> int:
    value = 0
    for i in range(m):
        value ^= (((x >> (2 * i)) & 1) & ((y >> (2 * i + 1)) & 1))
        value ^= (((x >> (2 * i + 1)) & 1) & ((y >> (2 * i)) & 1))
    return value


def update(x: int, y: int, m: int, eps: int) -> tuple[int, int]:
    return y, x ^ (y if quadratic(x, m, eps) else 0)


def orbit_data(x: int, y: int, m: int, eps: int) -> tuple[int, int]:
    seen: dict[tuple[int, int], int] = {}
    state = (x, y)
    while state not in seen:
        seen[state] = len(seen)
        state = update(*state, m, eps)
        if len(seen) > 8:
            raise AssertionError("period/depth ceiling failed before quotient check")
    return seen[state], len(seen) - seen[state]


def expected_orbit(
    x: int, y: int, a: int, b: int, c: int
) -> tuple[int, int]:
    if c == 0:
        if (a, b) == (0, 0):
            return 0, 1 if x == y else 2
        if (a, b) == (0, 1):
            return 0, 2 if x == 0 else 4
        if (a, b) == (1, 0):
            return 0, 2 if y == 0 else 4
        return 1, 2 if x == y else 4
    if (a, b) == (0, 0):
        return 0, 2
    if (a, b) == (0, 1):
        return 2, 2
    if (a, b) == (1, 0):
        return 1, 2
    return 0, 3


def pair_type_formula(N: int, S: int, a: int, b: int, c: int) -> int:
    numerator = (
        N * N
        + ((-1) ** a) * S * N
        + ((-1) ** b) * N * S
        + ((-1) ** (a + b)) * S * S
        + ((-1) ** c)
        * (
            N
            + ((-1) ** a) * N
            + ((-1) ** b) * N
            + ((-1) ** (a + b)) * N * S
        )
    )
    if numerator % 8:
        raise AssertionError("nonintegral character-sum formula")
    return numerator // 8


def expected_component_counts(N: int, S: int) -> tuple[int, int, int, int, int, int]:
    n0 = (N + S) // 2
    n1 = (N - S) // 2
    c000 = pair_type_formula(N, S, 0, 0, 0)
    c010 = pair_type_formula(N, S, 0, 1, 0)
    c001 = pair_type_formula(N, S, 0, 0, 1)
    c111 = pair_type_formula(N, S, 1, 1, 1)
    return (
        n0,                    # bare fixed points
        (c000 - n0) // 2,     # bare 2-cycles
        n1,                    # 2-cycle with one leaf
        c001 // 2,             # 2-cycle with two length-2 tails
        c111 // 3,             # bare 3-cycles
        (c010 - n1) // 2,     # 4-cycle with two leaves
    )


def audit_form(m: int, eps: int, audit: Audit) -> str:
    N = 1 << (2 * m)
    S = eps * (1 << m)
    states = N * N

    q_values = [quadratic(x, m, eps) for x in range(N)]
    n0 = q_values.count(0)
    n1 = q_values.count(1)
    audit.check(n0 == (N + S) // 2, f"Q=0 census m={m}, eps={eps}")
    audit.check(n1 == (N - S) // 2, f"Q=1 census m={m}, eps={eps}")
    audit.check(S * S == N, f"Gauss sign normalization m={m}, eps={eps}")

    indegrees = [0] * states
    type_counts: Counter[tuple[int, int, int]] = Counter()
    orbit_counts: Counter[tuple[int, int]] = Counter()
    image2: set[int] = set()

    for x in range(N):
        a = q_values[x]
        for y in range(N):
            b = q_values[y]
            c = polar(x, y, m)
            type_counts[a, b, c] += 1

            audit.check(
                quadratic(x ^ y, m, eps) == (a ^ b ^ c),
                f"polarization m={m}, eps={eps}, x={x}, y={y}",
            )
            u, v = update(x, y, m, eps)
            audit.check(u == y and v == (x ^ (a * y)), "literal update")
            audit.check(polar(u, v, m) == c, "polar invariant")
            next_type = (b, a & (1 ^ b ^ c), c)
            audit.check(
                (q_values[u], q_values[v], polar(u, v, m)) == next_type,
                "eight-state quotient transition",
            )

            target_index = u * N + v
            indegrees[target_index] += 1
            u2, v2 = update(u, v, m, eps)
            image2.add(u2 * N + v2)

            observed = orbit_data(x, y, m, eps)
            expected = expected_orbit(x, y, a, b, c)
            audit.check(observed == expected, "pointwise depth/period classification")
            orbit_counts[observed] += 1

    audit.check(sum(type_counts.values()) == states, "type partition")
    for c in (0, 1):
        for a in (0, 1):
            for b in (0, 1):
                expected = pair_type_formula(N, S, a, b, c)
                audit.check(
                    type_counts[a, b, c] == expected,
                    f"type census {(a, b, c)} m={m}, eps={eps}",
                )

    indegree_hist = Counter()
    for u in range(N):
        a = q_values[u]
        for v in range(N):
            b = q_values[v]
            c = polar(u, v, m)
            index = u * N + v
            fibre = int(b == 0) + int((a ^ b ^ c) == 1)
            candidates: set[tuple[int, int]] = set()
            if b == 0:
                candidates.add((v, u))
            if q_values[u ^ v] == 1:
                candidates.add((u ^ v, u))
            audit.check(len(candidates) == fibre, "inverse-candidate multiplicity")
            for source in candidates:
                audit.check(update(*source, m, eps) == (u, v), "inverse candidate")
            audit.check(indegrees[index] == fibre, "complete pointwise fibre formula")
            audit.check(fibre in (0, 1, 2), "fibre ceiling")
            indegree_hist[fibre] += 1

    missing_or_double = N * (N - 1) // 4
    audit.check(indegree_hist[0] == missing_or_double, "zero-fibre census")
    audit.check(indegree_hist[2] == missing_or_double, "double-fibre census")
    audit.check(indegree_hist[1] == N * (N + 1) // 2, "single-fibre census")
    audit.check(sum(k * v for k, v in indegree_hist.items()) == states, "edge census")

    depth1 = N * (N - 1) // 4
    depth2 = N * (N + S - 2) // 8
    recurrent = N * (5 * N - S + 4) // 8
    image1_size = sum(value > 0 for value in indegrees)
    audit.check(
        sum(value for (mu, _), value in orbit_counts.items() if mu == 1) == depth1,
        "depth-one layer",
    )
    audit.check(
        sum(value for (mu, _), value in orbit_counts.items() if mu == 2) == depth2,
        "depth-two layer",
    )
    audit.check(
        sum(value for (mu, _), value in orbit_counts.items() if mu == 0) == recurrent,
        "recurrent census",
    )
    audit.check(image1_size == N * (3 * N + 1) // 4, "first image size")
    audit.check(len(image2) == recurrent, "second image equals recurrent-size formula")
    audit.check(all(mu <= 2 for mu, _ in orbit_counts), "universal depth ceiling")
    audit.check(all(period <= 4 for _, period in orbit_counts), "universal period ceiling")

    cycles = {
        1: (N + S) // 2,
        2: (N * N + 2 * N * S + 3 * N - 6 * S) // 8,
        3: N * (N - 3 * S + 2) // 24,
        4: (N * N - N * S - 4 * N + 4 * S) // 16,
    }
    for period in (1, 2, 3, 4):
        periodic_points = orbit_counts[0, period]
        audit.check(periodic_points == period * cycles[period], "cycle census")
    audit.check(
        sum(
            value
            for (mu, period), value in orbit_counts.items()
            if mu == 0 and period not in (1, 2, 3, 4)
        )
        == 0,
        "no other periods",
    )

    component_counts = expected_component_counts(N, S)
    fixed, bare2, leaf2, tail2, bare3, leaf4 = component_counts
    audit.check(fixed == cycles[1], "fixed component count")
    audit.check(bare2 + leaf2 + tail2 == cycles[2], "three 2-cycle shapes")
    audit.check(bare3 == cycles[3], "3-cycle component count")
    audit.check(leaf4 == cycles[4], "4-cycle component count")
    audit.check(
        fixed + 2 * bare2 + 3 * leaf2 + 6 * tail2 + 3 * bare3 + 6 * leaf4
        == states,
        "complete decorated-component state census",
    )

    sign = "+" if eps == 1 else "-"
    cycle_text = "/".join(str(cycles[j]) for j in (1, 2, 3, 4))
    component_text = "/".join(str(value) for value in component_counts)
    return (
        f"m={m} sign={sign} |V|={N} Q0/Q1={n0}/{n1} "
        f"layers={recurrent}/{depth1}/{depth2} "
        f"images={states}/{image1_size}/{recurrent} "
        f"cycles1/2/3/4={cycle_text} "
        f"components={component_text} "
        f"fibres0/1/2={indegree_hist[0]}/{indegree_hist[1]}/{indegree_hist[2]}"
    )


def main() -> None:
    audit = Audit()
    lines = [audit_form(0, 1, audit)]
    for m in range(1, 6):
        for eps in (1, -1):
            lines.append(audit_form(m, eps, audit))
    print("quadratic-state shear exact audit")
    for line in lines:
        print(line)
    print(f"ASSERTIONS {audit.assertions}")
    print("PASS")


if __name__ == "__main__":
    main()
