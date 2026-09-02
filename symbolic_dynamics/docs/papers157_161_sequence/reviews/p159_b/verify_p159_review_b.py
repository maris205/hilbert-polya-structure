#!/usr/bin/env python3
"""Fresh exact control for P159 Hostile Review B.

This reviewer-owned program imports neither the author verifier nor Review A.
It represents graphs by symmetric adjacency-row bitsets, independently
constructs the strict target-row/source-column transfer, and separately
audits the binary incidence systems using a column-basis calculation.
Finite checks are counterexample pressure, not proof or owner clearance.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations
from math import comb


CHECKS = 0


def require(condition: bool, witness: object) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(witness)


State = tuple[int, tuple[int, ...]]
Matrix = tuple[tuple[int, ...], ...]


def gf2_rank(columns: tuple[int, ...]) -> int:
    basis: dict[int, int] = {}
    for original in columns:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def incidence_lane() -> int:
    cases = 0
    for total in range(1, 15):
        for deleted in range(1, total + 1):
            target = total - deleted
            columns = tuple(
                (1 << u) | (1 << v)
                for u, v in combinations(range(total), 2)
                if u >= target or v >= target
            )
            rank = gf2_rank(columns)
            require(rank == total - 1, ("incidence rank", target, deleted))
            exponent = len(columns) - rank
            claimed = target * (deleted - 1) + comb(deleted - 1, 2)
            require(exponent == claimed, ("nullity", target, deleted))

            for parity in range(1 << target):
                if parity.bit_count() % 2:
                    continue
                rhs = parity | (((1 << deleted) - 1) << target)
                solvable = gf2_rank(columns + (rhs,)) == rank
                require(
                    solvable == (deleted % 2 == 0),
                    ("consistency", target, deleted, parity),
                )
                cases += 1
    return cases


@cache
def carrier(n: int) -> tuple[State, ...]:
    answer: list[State] = []
    ambient_edges = tuple(combinations(range(n), 2))
    for vertex_mask in range(1 << n):
        available = tuple(
            edge
            for edge in ambient_edges
            if vertex_mask & (1 << edge[0]) and vertex_mask & (1 << edge[1])
        )
        for selection in range(1 << len(available)):
            rows = [0] * n
            for index, (u, v) in enumerate(available):
                if selection & (1 << index):
                    rows[u] |= 1 << v
                    rows[v] |= 1 << u
            answer.append((vertex_mask, tuple(rows)))
    return tuple(answer)


def state_rank(state: State) -> int:
    return state[0].bit_count()


def even(state: State) -> bool:
    vertex_mask, rows = state
    return all(
        not (vertex_mask & (1 << v)) or rows[v].bit_count() % 2 == 0
        for v in range(len(rows))
    )


def step(state: State) -> State:
    vertex_mask, rows = state
    odd = 0
    for v in range(len(rows)):
        if vertex_mask & (1 << v) and rows[v].bit_count() % 2:
            odd |= 1 << v
    survivor_mask = vertex_mask & ~odd
    return survivor_mask, tuple(
        (rows[v] & survivor_mask) if survivor_mask & (1 << v) else 0
        for v in range(len(rows))
    )


def even_count(s: int) -> int:
    return 1 if s <= 1 else 1 << comb(s - 1, 2)


def phase_count(n: int) -> int:
    return sum(comb(n, s) * (1 << comb(s, 2)) for s in range(n + 1))


def strict_entry(n: int, target: int, source: int) -> int:
    d = source - target
    if d <= 0 or d % 2:
        return 0
    return comb(n - target, d) * (
        1 << (target * (d - 1) + comb(d - 1, 2))
    )


def transfer(n: int) -> Matrix:
    return tuple(
        tuple(strict_entry(n, s, m) for m in range(n + 1))
        for s in range(n + 1)
    )


def identity(width: int) -> Matrix:
    return tuple(
        tuple(int(row == column) for column in range(width))
        for row in range(width)
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(lrow, rrow))
        for lrow, rrow in zip(left, right)
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


def path_state(n: int) -> State:
    rows = [0] * n
    for v in range(n - 1):
        rows[v] |= 1 << (v + 1)
        rows[v + 1] |= 1 << v
    return (1 << n) - 1, tuple(rows)


def depth(state: State) -> int:
    elapsed = 0
    current = state
    while True:
        following = step(current)
        if following == current:
            return elapsed
        require(
            state_rank(following) <= state_rank(current) - 2,
            ("strict loss", state),
        )
        current = following
        elapsed += 1


def literal_lane(n: int) -> tuple[int, int, int]:
    states = carrier(n)
    require(len(states) == phase_count(n), ("phase", n))
    one_step = {source: step(source) for source in states}
    require(set(one_step.values()) <= set(states), ("closure", n))

    strict: Counter[tuple[State, int]] = Counter()
    full: Counter[tuple[State, int]] = Counter()
    for source, target in one_step.items():
        srank = state_rank(source)
        trank = state_rank(target)
        full[target, srank] += 1
        if srank > trank:
            strict[target, srank] += 1
            require(not even(source), ("strict source even", n, source))
        else:
            require(source == target and even(source), ("d=0", n, source))

    matrix = transfer(n)
    for target in states:
        trank = state_rank(target)
        for srank in range(n + 1):
            require(
                strict[target, srank] == matrix[trank][srank],
                ("strict fibre", n, target, srank),
            )
            diagonal = int(srank == trank and even(target))
            require(
                full[target, srank] == matrix[trank][srank] + diagonal,
                ("full fibre", n, target, srank),
            )

    if n >= 2:
        empty = (0, (0,) * n)
        require(strict[empty, 2] == comb(n, 2), ("s=0,d=2", n))
        for u, v in combinations(range(n), 2):
            rows = [0] * n
            rows[u] = 1 << v
            rows[v] = 1 << u
            require(step(((1 << u) | (1 << v), tuple(rows))) == empty, (u, v))

    depths = Counter(depth(state) for state in states)
    height = max(depths)
    require(height == n // 2, ("height", n))
    require(depth(path_state(n)) == n // 2, ("path", n))
    fixed = sum(even(state) for state in states)
    expected_fixed = sum(comb(n, s) * even_count(s) for s in range(n + 1))
    require(fixed == expected_fixed, ("fixed", n))
    if n == 0:
        require(len(states) == fixed == 1 and height == 0, "n=0")
    if n == 1:
        require(len(states) == fixed == 2 and height == 0, "n=1")

    power = identity(n + 1)
    geometric = identity(n + 1)
    images = {source: source for source in states}
    previous_cdf = 0
    for time in range(height + 3):
        refined = Counter((target, state_rank(source)) for source, target in images.items())
        actual_image = set(images.values())
        predicted_image = {
            target
            for target in states
            if time == 0 or even(target) or n - state_rank(target) >= 2 * time
        }
        require(actual_image == predicted_image, ("image iff", n, time))
        for target in states:
            formula = geometric if even(target) else power
            trank = state_rank(target)
            for srank in range(n + 1):
                require(
                    refined[target, srank] == formula[trank][srank],
                    ("temporal fibre", n, time, target, srank),
                )
        cdf = sum(
            comb(n, s) * even_count(s) * sum(geometric[s])
            for s in range(n + 1)
        )
        literal_cdf = sum(count for d, count in depths.items() if d <= time)
        require(cdf == literal_cdf, ("CDF", n, time))
        require(cdf - previous_cdf == depths.get(time, 0), ("shell", n, time))
        previous_cdf = cdf
        power = multiply(power, matrix)
        geometric = add(geometric, power)
        images = {source: step(target) for source, target in images.items()}
    return len(states), fixed, height


def orientation_lane() -> None:
    b4 = transfer(4)
    require(b4[0][2] == 6, "B4(0,2)")
    require(b4[2][0] == 0, "B4(2,0)")
    require(multiply(b4, b4)[0][4] == 24, "B4^2(0,4)")
    for n in range(25):
        matrix = transfer(n)
        power = identity(n + 1)
        for time in range(n // 2 + 1):
            for target in range(n + 1):
                positive = any(power[target])
                require(
                    positive == (time == 0 or n - target >= 2 * time),
                    ("rank image", n, time, target),
                )
            power = multiply(power, matrix)
        require(not any(value for row in power for value in row), ("nilpotent", n))


def main() -> None:
    incidence_cases = incidence_lane()
    rows = [(n, *literal_lane(n)) for n in range(6)]
    orientation_lane()
    print("P159_HOSTILE_REVIEW_B_EXACT_V1")
    print(f"INCIDENCE_CASES={incidence_cases};TOTAL_ORDER_LE_14")
    print("BOUNDARIES=d0;s0d2;n0;n1;t0")
    print("ORIENTATION=B4_0_2_6;B4_2_0_0;B4SQ_0_4_24")
    print("TEMPORAL=NON_EVEN_POWER;EVEN_GEOMETRIC")
    for n, total, fixed, height in rows:
        print(f"ATLAS n={n},states={total},fixed={fixed},height={height}")
    print("MATRIX_IMAGE_AND_NILPOTENCE_N_LE_24")
    print(f"ASSERTIONS={CHECKS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
