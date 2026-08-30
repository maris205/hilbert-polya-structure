#!/usr/bin/env python3
"""Exact paper-local audit for P125 quadratic-state shear.

The two canonical nonsingular quadratic forms on F_2^(2m) are exhausted
through m=5.  In addition to pointwise orbit and fibre checks, the verifier
asserts literal set equality im(Phi^2)=Rec(Phi) and traverses every functional
component, comparing its decorated rooted-cycle shape with the six formulas.
Only the Python standard library is used.
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
    """The plus or minus nonsingular form on F_2^(2m)."""
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
        value ^= ((x >> (2 * i)) & 1) & ((y >> (2 * i + 1)) & 1)
        value ^= ((x >> (2 * i + 1)) & 1) & ((y >> (2 * i)) & 1)
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
            raise AssertionError("depth/period ceiling failed")
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
        raise AssertionError("nonintegral pair-type formula")
    return numerator // 8


def canonical_cycle(sequence: tuple[tuple, ...]) -> tuple[tuple, ...]:
    """Directed-cycle decoration modulo cyclic rotation only."""
    n = len(sequence)
    rotations = [sequence[i:] + sequence[:i] for i in range(n)]
    return min(rotations, key=repr)


def shape_key(cycle_decorations: tuple[tuple, ...]) -> tuple[int, tuple]:
    return len(cycle_decorations), canonical_cycle(cycle_decorations)


FIXED = shape_key(((),))
BARE_TWO = shape_key(((), ()))
LEAF_TWO = shape_key(((), ((),)))
TAIL_TWO = shape_key(((((),),), (((),),)))
BARE_THREE = shape_key(((), (), ()))
LEAF_FOUR = shape_key((((),), (), ((),), ()))
ALLOWED_SHAPES = {FIXED, BARE_TWO, LEAF_TWO, TAIL_TWO, BARE_THREE, LEAF_FOUR}


def expected_component_counts(N: int, S: int) -> dict[tuple[int, tuple], int]:
    n0 = (N + S) // 2
    n1 = (N - S) // 2
    H = pair_type_formula(N, S, 0, 0, 0)
    M = pair_type_formula(N, S, 0, 1, 0)
    A = pair_type_formula(N, S, 0, 0, 1)
    Z = pair_type_formula(N, S, 1, 1, 1)
    return {
        FIXED: n0,
        BARE_TWO: (H - n0) // 2,
        LEAF_TWO: n1,
        TAIL_TWO: A // 2,
        BARE_THREE: Z // 3,
        LEAF_FOUR: (M - n1) // 2,
    }


def literal_component_census(
    next_indices: list[int],
    pred0: list[int],
    pred1: list[int],
    recurrent_bits: bytearray,
    audit: Audit,
) -> Counter[tuple[int, tuple]]:
    """Traverse every cycle and its reverse trees, returning literal shapes."""
    states = len(next_indices)
    cycle_seen = bytearray(states)
    state_seen = bytearray(states)
    census: Counter[tuple[int, tuple]] = Counter()

    def predecessors(index: int):
        if pred0[index] >= 0:
            yield pred0[index]
        if pred1[index] >= 0:
            yield pred1[index]

    for start in range(states):
        if not recurrent_bits[start] or cycle_seen[start]:
            continue

        cycle = [start]
        cycle_seen[start] = 1
        current = next_indices[start]
        while current != start:
            audit.check(recurrent_bits[current] == 1, "cycle left recurrent set")
            audit.check(cycle_seen[current] == 0, "cycles intersected")
            cycle.append(current)
            cycle_seen[current] = 1
            current = next_indices[current]
        cycle_set = set(cycle)

        def reverse_tree(index: int) -> tuple[tuple, int]:
            audit.check(state_seen[index] == 0, "component trees intersected")
            state_seen[index] = 1
            children = []
            size = 1
            for predecessor in predecessors(index):
                if predecessor in cycle_set:
                    continue
                child_signature, child_size = reverse_tree(predecessor)
                children.append(child_signature)
                size += child_size
            return tuple(sorted(children, key=repr)), size

        decorations = []
        component_size = 0
        for vertex in cycle:
            signature, tree_size = reverse_tree(vertex)
            decorations.append(signature)
            component_size += tree_size
        key = shape_key(tuple(decorations))
        audit.check(key in ALLOWED_SHAPES, f"unlisted component shape {key}")
        audit.check(component_size in (1, 2, 3, 6), "unlisted component size")
        census[key] += 1

    audit.check(all(cycle_seen[i] == recurrent_bits[i] for i in range(states)),
                "not every recurrent state was traversed on a cycle")
    audit.check(all(state_seen), "not every state belongs to a traversed component")
    return census


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
    pred0 = [-1] * states
    pred1 = [-1] * states
    next_indices = [0] * states
    recurrent_bits = bytearray(states)
    type_counts: Counter[tuple[int, int, int]] = Counter()
    orbit_counts: Counter[tuple[int, int]] = Counter()
    image2: set[int] = set()

    for x in range(N):
        a = q_values[x]
        for y in range(N):
            source_index = x * N + y
            b = q_values[y]
            c = polar(x, y, m)
            type_counts[a, b, c] += 1

            audit.check(q_values[x ^ y] == (a ^ b ^ c), "polarization")
            u, v = update(x, y, m, eps)
            audit.check(u == y and v == (x ^ (a * y)), "literal update")
            audit.check(polar(u, v, m) == c, "polar invariant")
            next_type = (b, a & (1 ^ b ^ c), c)
            audit.check(
                (q_values[u], q_values[v], polar(u, v, m)) == next_type,
                "eight-state quotient transition",
            )

            target_index = u * N + v
            next_indices[source_index] = target_index
            if indegrees[target_index] == 0:
                pred0[target_index] = source_index
            elif indegrees[target_index] == 1:
                pred1[target_index] = source_index
            else:
                audit.check(False, "literal fibre exceeds two")
            indegrees[target_index] += 1
            u2, v2 = update(u, v, m, eps)
            image2.add(u2 * N + v2)

            observed = orbit_data(x, y, m, eps)
            expected = expected_orbit(x, y, a, b, c)
            audit.check(observed == expected, "pointwise depth/period classification")
            orbit_counts[observed] += 1
            if observed[0] == 0:
                recurrent_bits[source_index] = 1

    audit.check(sum(type_counts.values()) == states, "type partition")
    for c in (0, 1):
        for a in (0, 1):
            for b in (0, 1):
                audit.check(
                    type_counts[a, b, c] == pair_type_formula(N, S, a, b, c),
                    f"type census {(a, b, c)}",
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
    audit.check(sum(v for (mu, _), v in orbit_counts.items() if mu == 1) == depth1,
                "depth-one layer")
    audit.check(sum(v for (mu, _), v in orbit_counts.items() if mu == 2) == depth2,
                "depth-two layer")
    audit.check(sum(v for (mu, _), v in orbit_counts.items() if mu == 0) == recurrent,
                "recurrent census")
    audit.check(image1_size == N * (3 * N + 1) // 4, "first image size")
    audit.check(len(image2) == recurrent, "second image size")
    for index in range(states):
        audit.check((index in image2) == bool(recurrent_bits[index]),
                    "literal im(Phi^2)=recurrent set")

    cycles = {
        1: (N + S) // 2,
        2: (N * N + 2 * N * S + 3 * N - 6 * S) // 8,
        3: N * (N - 3 * S + 2) // 24,
        4: (N * N - N * S - 4 * N + 4 * S) // 16,
    }
    for period in (1, 2, 3, 4):
        audit.check(orbit_counts[0, period] == period * cycles[period],
                    "cycle census")
    audit.check(all(mu <= 2 and period <= 4 for mu, period in orbit_counts),
                "universal temporal ceiling")

    literal_components = literal_component_census(
        next_indices, pred0, pred1, recurrent_bits, audit
    )
    expected_components = expected_component_counts(N, S)
    for key in ALLOWED_SHAPES:
        audit.check(literal_components[key] == expected_components[key],
                    f"literal decorated-component census {key}")
    audit.check(set(literal_components) <= ALLOWED_SHAPES,
                "literal component shape support")

    component_values = [
        literal_components[FIXED],
        literal_components[BARE_TWO],
        literal_components[LEAF_TWO],
        literal_components[TAIL_TWO],
        literal_components[BARE_THREE],
        literal_components[LEAF_FOUR],
    ]
    sign = "+" if eps == 1 else "-"
    cycle_text = "/".join(str(cycles[j]) for j in (1, 2, 3, 4))
    component_text = "/".join(str(value) for value in component_values)
    return (
        f"m={m} sign={sign} |V|={N} Q0/Q1={n0}/{n1} "
        f"layers={recurrent}/{depth1}/{depth2} "
        f"images={states}/{image1_size}/{len(image2)} "
        f"cycles1/2/3/4={cycle_text} components={component_text} "
        f"fibres0/1/2={indegree_hist[0]}/{indegree_hist[1]}/{indegree_hist[2]}"
    )


def main() -> None:
    audit = Audit()
    asymmetric = ((), ((),), (((),),))
    audit.check(
        canonical_cycle(asymmetric) != canonical_cycle(asymmetric[::-1]),
        "directed-cycle canonicalization identified a reflection",
    )
    lines = [audit_form(0, 1, audit)]
    for m in range(1, 6):
        for eps in (1, -1):
            lines.append(audit_form(m, eps, audit))
    print("P125 quadratic-state shear exact audit")
    print("literal_im2_equals_recurrent PASS")
    print("literal_six_component_shapes PASS")
    for line in lines:
        print(line)
    print(f"ASSERTIONS {audit.assertions}")
    print("PASS")


if __name__ == "__main__":
    main()
