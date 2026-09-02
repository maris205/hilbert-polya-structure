#!/usr/bin/env python3
"""Independent hostile exact audit for P159.

The reviewer uses global vertex/edge bit masks, not the paper verifier's tuple
carrier.  Literal orbit dictionaries are compared with a separately built
target-row/source-column transfer.  A second, graph-free syndrome-counting DP
checks all strict parity-extension systems through total order twelve without
Gaussian elimination.  The checks are finite falsification pressure, not an
all-parameter proof or an ownership/release certificate.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations
from math import comb


CHECKS = 0


def demand(condition: bool, label: object) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


State = tuple[int, int]
Matrix = tuple[tuple[int, ...], ...]


@cache
def ambient_edges(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


@cache
def states(n: int) -> tuple[State, ...]:
    answer: list[State] = []
    all_edges = ambient_edges(n)
    for vertex_mask in range(1 << n):
        available = [
            index
            for index, (u, v) in enumerate(all_edges)
            if vertex_mask & (1 << u) and vertex_mask & (1 << v)
        ]
        for local_mask in range(1 << len(available)):
            edge_mask = 0
            for local_index, global_index in enumerate(available):
                if local_mask & (1 << local_index):
                    edge_mask |= 1 << global_index
            answer.append((vertex_mask, edge_mask))
    return tuple(answer)


def rank(state: State) -> int:
    return state[0].bit_count()


def odd_mask(state: State, n: int) -> int:
    vertex_mask, edge_mask = state
    odd = 0
    for index, (u, v) in enumerate(ambient_edges(n)):
        if edge_mask & (1 << index):
            odd ^= (1 << u) | (1 << v)
    demand(not (odd & ~vertex_mask), ("odd vertex outside state", n, state))
    return odd


def even(state: State, n: int) -> bool:
    return odd_mask(state, n) == 0


def step(state: State, n: int) -> State:
    vertex_mask, edge_mask = state
    deleted = odd_mask(state, n)
    survivor_mask = vertex_mask & ~deleted
    survivor_edges = 0
    for index, (u, v) in enumerate(ambient_edges(n)):
        if (
            edge_mask & (1 << index)
            and survivor_mask & (1 << u)
            and survivor_mask & (1 << v)
        ):
            survivor_edges |= 1 << index
    return survivor_mask, survivor_edges


def phase_formula(n: int) -> int:
    return sum(comb(n, s) * (1 << comb(s, 2)) for s in range(n + 1))


def even_count(s: int) -> int:
    return 1 if s <= 1 else 1 << comb(s - 1, 2)


def strict_formula(n: int, target: int, source: int) -> int:
    deleted = source - target
    if deleted <= 0 or deleted % 2:
        return 0
    return comb(n - target, deleted) * (
        1 << (target * (deleted - 1) + comb(deleted - 1, 2))
    )


def transfer(n: int) -> Matrix:
    return tuple(
        tuple(strict_formula(n, target, source) for source in range(n + 1))
        for target in range(n + 1)
    )


def identity(width: int) -> Matrix:
    return tuple(
        tuple(int(row == column) for column in range(width))
        for row in range(width)
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    width = len(left)
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(width))
            for column in range(width)
        )
        for row in range(width)
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def zero(matrix: Matrix) -> bool:
    return all(value == 0 for row in matrix for value in row)


def syndrome_distribution(target: int, deleted: int) -> Counter[int]:
    """Count variable-edge subsets by their full endpoint parity vector."""
    total = target + deleted
    variable_edges = [
        (u, v)
        for u, v in combinations(range(total), 2)
        if u >= target or v >= target
    ]
    counts: Counter[int] = Counter({0: 1})
    for u, v in variable_edges:
        toggle = (1 << u) | (1 << v)
        next_counts: Counter[int] = Counter()
        for syndrome, multiplicity in counts.items():
            next_counts[syndrome] += multiplicity
            next_counts[syndrome ^ toggle] += multiplicity
        counts = next_counts
    demand(sum(counts.values()) == 1 << len(variable_edges), "syndrome mass")
    return counts


def strict_system_lane() -> None:
    cases = 0
    for total in range(1, 13):
        for deleted in range(1, total + 1):
            target = total - deleted
            distribution = syndrome_distribution(target, deleted)
            expected_nonzero = 1 << (
                target * (deleted - 1) + comb(deleted - 1, 2)
            )
            for target_parity in range(1 << target):
                if target_parity.bit_count() % 2:
                    continue
                rhs = target_parity | (((1 << deleted) - 1) << target)
                observed = distribution.get(rhs, 0)
                expected = expected_nonzero if deleted % 2 == 0 else 0
                demand(
                    observed == expected,
                    ("strict syndrome", target, deleted, target_parity),
                )
                cases += 1
    demand(cases == 4095, ("syndrome case census", cases))


def path_state(n: int) -> State:
    edge_lookup = {edge: index for index, edge in enumerate(ambient_edges(n))}
    mask = 0
    for vertex in range(n - 1):
        mask |= 1 << edge_lookup[vertex, vertex + 1]
    return (1 << n) - 1, mask


def depth(state: State, n: int) -> int:
    current = state
    elapsed = 0
    while True:
        following = step(current, n)
        if following == current:
            return elapsed
        demand(rank(following) <= rank(current) - 2, ("non-strict loss", n, current))
        current = following
        elapsed += 1
        demand(elapsed <= n // 2, ("orbit guard", n, state))


def image_count_formula(n: int, time: int) -> int:
    if time == 0:
        return phase_formula(n)
    return sum(
        comb(n, s)
        * (
            even_count(s)
            + int(n - s >= 2 * time) * ((1 << comb(s, 2)) - even_count(s))
        )
        for s in range(n + 1)
    )


def literal_order_lane(n: int) -> tuple[int, int, int]:
    carrier = states(n)
    demand(len(carrier) == phase_formula(n), ("phase size", n))
    carrier_set = set(carrier)
    one_step = {source: step(source, n) for source in carrier}
    demand(set(one_step.values()) <= carrier_set, ("closure", n))

    strict: Counter[tuple[State, int]] = Counter()
    full: Counter[tuple[State, int]] = Counter()
    for source, target in one_step.items():
        source_rank = rank(source)
        target_rank = rank(target)
        full[target, source_rank] += 1
        loss = source_rank - target_rank
        demand(loss == odd_mask(source, n).bit_count(), ("loss set", n, source))
        demand(loss % 2 == 0, ("odd loss", n, source))
        if loss:
            strict[target, source_rank] += 1
            demand(not even(source, n), ("strict source even", n, source))
        else:
            demand(source == target and even(source, n), ("diagonal", n, source))

    matrix = transfer(n)
    for target in carrier:
        target_rank = rank(target)
        for source_rank in range(n + 1):
            strict_expected = matrix[target_rank][source_rank]
            demand(
                strict[target, source_rank] == strict_expected,
                ("strict fibre", n, target, source_rank),
            )
            diagonal = int(source_rank == target_rank and even(target, n))
            demand(
                full[target, source_rank] == strict_expected + diagonal,
                ("full fibre", n, target, source_rank),
            )

    empty = (0, 0)
    if n >= 2:
        demand(strict[empty, 2] == comb(n, 2), ("aggregate s0d2", n))
        lookup = {edge: index for index, edge in enumerate(ambient_edges(n))}
        for u, v in combinations(range(n), 2):
            pair = (1 << u) | (1 << v)
            k2 = pair, 1 << lookup[u, v]
            demand(step(k2, n) == empty, ("fixed-D K2", n, u, v))

    depths = Counter(depth(state, n) for state in carrier)
    maximum = max(depths)
    demand(maximum == n // 2, ("maximum depth", n))
    demand(depth(path_state(n), n) == n // 2, ("path depth", n))
    fixed = sum(even(state, n) for state in carrier)
    fixed_formula = sum(comb(n, s) * even_count(s) for s in range(n + 1))
    demand(fixed == fixed_formula, ("fixed count", n))
    if n == 0:
        demand(len(carrier) == fixed == 1 and maximum == 0, "n=0")
    if n == 1:
        demand(len(carrier) == fixed == 2 and maximum == 0, "n=1")

    power = identity(n + 1)
    geometric = identity(n + 1)
    images = {state: state for state in carrier}
    previous_cdf = 0
    for time in range(maximum + 3):
        refined = Counter((target, rank(source)) for source, target in images.items())
        observed_image = set(images.values())
        expected_image = {
            target
            for target in carrier
            if time == 0 or even(target, n) or n - rank(target) >= 2 * time
        }
        demand(observed_image == expected_image, ("image iff", n, time))
        demand(len(observed_image) == image_count_formula(n, time), ("image count", n, time))
        for target in carrier:
            target_rank = rank(target)
            formula = geometric if even(target, n) else power
            for source_rank in range(n + 1):
                demand(
                    refined[target, source_rank] == formula[target_rank][source_rank],
                    ("temporal fibre", n, time, target, source_rank),
                )

        cdf_formula = sum(
            comb(n, s) * even_count(s) * sum(geometric[s])
            for s in range(n + 1)
        )
        cdf_literal = sum(count for d, count in depths.items() if d <= time)
        demand(cdf_formula == cdf_literal, ("CDF", n, time))
        demand(cdf_formula - previous_cdf == depths.get(time, 0), ("shell", n, time))
        previous_cdf = cdf_formula

        power = multiply(power, matrix)
        geometric = add(geometric, power)
        images = {source: step(target, n) for source, target in images.items()}

    demand(previous_cdf == len(carrier), ("terminal CDF", n))
    return len(carrier), fixed, maximum


def boundary_and_orientation_lane() -> None:
    matrix = transfer(4)
    square = multiply(matrix, matrix)
    demand(matrix[0][2] == 6, "B4 target-row source-column")
    demand(matrix[2][0] == 0, "B4 transpose rejection")
    demand(square[0][4] == 24, "B4 squared direction")

    # K2 is non-even: at t=1 the strict matrix has zero diagonal, whereas an
    # incorrectly applied geometric sum would add a spurious same-rank source.
    k2: State = (0b11, 0b1)
    actual_same_rank = sum(
        1 for source in states(2) if rank(source) == 2 and step(source, 2) == k2
    )
    demand(not even(k2, 2), "K2 must be non-even")
    demand(actual_same_rank == 0, "non-even same-rank predecessor")
    demand(transfer(2)[2][2] == 0, "strict diagonal")
    demand(add(identity(3), transfer(2))[2][2] == 1, "geometric discriminator")

    for n in range(21):
        matrix = transfer(n)
        power = identity(n + 1)
        for time in range(n // 2 + 1):
            for target in range(n + 1):
                positive = any(power[target][source] for source in range(n + 1))
                expected = time == 0 or n - target >= 2 * time
                demand(positive == expected, ("strict image positivity", n, time, target))
            power = multiply(power, matrix)
        demand(zero(power), ("nilpotence", n))


def main() -> None:
    strict_system_lane()
    rows = [(n, *literal_order_lane(n)) for n in range(7)]
    boundary_and_orientation_lane()
    print("P159_HOSTILE_REVIEW_A_EXACT_V1")
    print("STRICT positive_even_d_formula_syndrome_DP_total_order<=12")
    print("BOUNDARIES d=0;s=0,d=2;n=0,1;t=0:exact")
    print("ORIENTATION target_rows_source_columns:B4_0_2=6;B4_2_0=0;B4sq_0_4=24")
    print("EVEN_SPLIT non_even=B^t;even=I+...+B^t")
    for n, total, fixed, height in rows:
        print(f"ATLAS n={n},states={total},fixed={fixed},height={height}")
    print("IMAGE_IFF_AND_CDF literal_all_states_n<=6")
    print("MATRIX_POSITIVITY_AND_NILPOTENCE n<=20")
    print(f"ASSERTIONS={CHECKS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
