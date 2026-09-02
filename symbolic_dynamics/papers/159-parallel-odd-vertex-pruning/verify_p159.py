#!/usr/bin/env python3
"""Exact falsifier for P159 parallel odd-vertex pruning.

The script is self-contained and uses immutable labelled vertex/edge tuples.
It does not import the phase-one scout verifiers.  Literal graph dynamics,
rank-transfer algebra, and GF(2) incidence ranks are computed in separate
lanes.  Finite enumeration is counterexample pressure, not an all-parameter
proof, ownership certificate, novelty statement, or release gate.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations
from math import comb


ASSERTIONS = 0
SECTION_ASSERTIONS: dict[str, int] = {}
CURRENT_SECTION = "setup"
DIAGNOSTICS: dict[str, int] = {}


def check(condition: bool, witness: object = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    SECTION_ASSERTIONS[CURRENT_SECTION] = (
        SECTION_ASSERTIONS.get(CURRENT_SECTION, 0) + 1
    )
    if not condition:
        raise AssertionError(witness)


VertexSet = tuple[int, ...]
Edge = tuple[int, int]
State = tuple[VertexSet, tuple[Edge, ...]]
Matrix = tuple[tuple[int, ...], ...]


@cache
def carrier(ambient_order: int) -> tuple[State, ...]:
    states: list[State] = []
    labels = tuple(range(ambient_order))
    for size in range(ambient_order + 1):
        for vertices in combinations(labels, size):
            possible_edges = tuple(combinations(vertices, 2))
            for mask in range(1 << len(possible_edges)):
                edges = tuple(
                    edge
                    for index, edge in enumerate(possible_edges)
                    if mask & (1 << index)
                )
                states.append((vertices, edges))
    return tuple(states)


def state_rank(state: State) -> int:
    return len(state[0])


def odd_vertices(state: State) -> frozenset[int]:
    vertices, edges = state
    odd: set[int] = set()
    for left, right in edges:
        for vertex in (left, right):
            if vertex in odd:
                odd.remove(vertex)
            else:
                odd.add(vertex)
    check(odd <= set(vertices), ("edge endpoint outside carrier", state))
    return frozenset(odd)


def is_even(state: State) -> bool:
    return not odd_vertices(state)


@cache
def update(state: State) -> State:
    vertices, edges = state
    deleted = odd_vertices(state)
    survivors = tuple(vertex for vertex in vertices if vertex not in deleted)
    survivor_set = set(survivors)
    induced_edges = tuple(
        edge
        for edge in edges
        if edge[0] in survivor_set and edge[1] in survivor_set
    )
    return survivors, induced_edges


def even_graph_count(size: int) -> int:
    if size <= 1:
        return 1
    return 1 << comb(size - 1, 2)


def phase_count(ambient_order: int) -> int:
    return sum(
        comb(ambient_order, size) * (1 << comb(size, 2))
        for size in range(ambient_order + 1)
    )


def strict_entry(ambient_order: int, target_rank: int, source_rank: int) -> int:
    deleted = source_rank - target_rank
    if deleted <= 0 or deleted % 2:
        return 0
    exponent = target_rank * (deleted - 1) + comb(deleted - 1, 2)
    return comb(ambient_order - target_rank, deleted) * (1 << exponent)


def transfer(ambient_order: int) -> Matrix:
    return tuple(
        tuple(
            strict_entry(ambient_order, target, source)
            for source in range(ambient_order + 1)
        )
        for target in range(ambient_order + 1)
    )


def identity(width: int) -> Matrix:
    return tuple(
        tuple(int(row == column) for column in range(width))
        for row in range(width)
    )


def matrix_sum(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] + right[row][column]
            for column in range(len(left))
        )
        for row in range(len(left))
    )


def compose(left: Matrix, right: Matrix) -> Matrix:
    """Conventional product for row=target and column=source."""

    width = len(left)
    return tuple(
        tuple(
            sum(
                left[target][middle] * right[middle][source]
                for middle in range(width)
            )
            for source in range(width)
        )
        for target in range(width)
    )


def zero_matrix(matrix: Matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def gf2_rank(rows: tuple[int, ...]) -> int:
    basis: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def audit_parity_systems() -> None:
    """Check strict inverse consistency and nullity without graph enumeration."""

    global CURRENT_SECTION
    CURRENT_SECTION = "GF2 incidence rank/nullity"
    cases = 0
    for total in range(1, 10):
        for deleted in range(1, total + 1):
            target = total - deleted
            variables = tuple(
                edge
                for edge in combinations(range(total), 2)
                if edge[0] >= target or edge[1] >= target
            )
            coefficient_rows: list[int] = []
            for vertex in range(total):
                row = 0
                for index, edge in enumerate(variables):
                    if vertex in edge:
                        row |= 1 << index
                coefficient_rows.append(row)
            coefficient_rank = gf2_rank(tuple(coefficient_rows))
            check(
                coefficient_rank == total - 1,
                ("connected incidence rank", target, deleted),
            )

            # The degree-parity vectors attained by target graphs are exactly
            # the even-weight vectors (with the s=0,1 boundaries included).
            for target_parity in range(1 << target):
                if target_parity.bit_count() % 2:
                    continue
                rhs = tuple(
                    ((target_parity >> vertex) & 1) if vertex < target else 1
                    for vertex in range(total)
                )
                augmented_rows = tuple(
                    coefficient_rows[vertex]
                    | (rhs[vertex] << len(variables))
                    for vertex in range(total)
                )
                augmented_rank = gf2_rank(augmented_rows)
                solvable = augmented_rank == coefficient_rank
                check(
                    solvable == (deleted % 2 == 0),
                    ("consistency parity", target, deleted, target_parity),
                )
                if solvable:
                    nullity = len(variables) - coefficient_rank
                    claimed = (
                        target * (deleted - 1) + comb(deleted - 1, 2)
                    )
                    check(
                        nullity == claimed,
                        ("strict inverse nullity", target, deleted, target_parity),
                    )
                cases += 1
    DIAGNOSTICS["parity_system_cases"] = cases


def orbit_depth(state: State) -> int:
    seen: set[State] = set()
    current = state
    depth = 0
    while update(current) != current:
        check(current not in seen, ("strict cycle", state))
        seen.add(current)
        current = update(current)
        depth += 1
    return depth


def path_state(order: int) -> State:
    return (
        tuple(range(order)),
        tuple((index, index + 1) for index in range(order - 1)),
    )


def predicted_image_count(ambient_order: int, time: int) -> int:
    if time == 0:
        return phase_count(ambient_order)
    answer = 0
    for size in range(ambient_order + 1):
        fixed = even_graph_count(size)
        all_graphs = 1 << comb(size, 2)
        allowed_nonfixed = all_graphs - fixed if ambient_order - size >= 2 * time else 0
        answer += comb(ambient_order, size) * (fixed + allowed_nonfixed)
    return answer


def audit_order(ambient_order: int) -> tuple[int, int, int, int]:
    global CURRENT_SECTION
    CURRENT_SECTION = "literal one-step fibres/boundaries"
    states = carrier(ambient_order)
    check(len(states) == phase_count(ambient_order), ("phase count", ambient_order))
    state_set = set(states)
    one_step = {source: update(source) for source in states}
    check(set(one_step.values()) <= state_set, ("closure", ambient_order))

    strict_fibres: Counter[tuple[State, int]] = Counter()
    full_one_step: Counter[tuple[State, int]] = Counter()
    for source, target in one_step.items():
        source_size = state_rank(source)
        target_size = state_rank(target)
        full_one_step[target, source_size] += 1
        loss = source_size - target_size
        check(loss == len(odd_vertices(source)), ("rank loss", source))
        check(loss % 2 == 0, ("strict rank-loss parity", source))
        if loss:
            strict_fibres[target, source_size] += 1
            check(not is_even(source), ("strict predecessor fixed", source))
        else:
            check(source == target and is_even(source), ("d=0 branch", source))

    matrix = transfer(ambient_order)
    for target in states:
        target_size = state_rank(target)
        for source_size in range(ambient_order + 1):
            strict_expected = matrix[target_size][source_size]
            check(
                strict_fibres[target, source_size] == strict_expected,
                ("strict fibre", ambient_order, target, source_size),
            )
            same_rank_wait = int(source_size == target_size and is_even(target))
            check(
                full_one_step[target, source_size]
                == strict_expected + same_rank_wait,
                ("full one-step fibre", ambient_order, target, source_size),
            )

    if ambient_order >= 2:
        empty: State = ((), ())
        check(
            strict_fibres[empty, 2] == comb(ambient_order, 2),
            ("s=0,d=2 aggregate", ambient_order),
        )
        for pair in combinations(range(ambient_order), 2):
            check(update((pair, (pair,))) == empty, ("fixed-D K2", pair))

    CURRENT_SECTION = "clock/fixed census"
    depths = Counter(orbit_depth(state) for state in states)
    maximum_depth = max(depths)
    check(maximum_depth == ambient_order // 2, ("sharp clock", ambient_order))
    check(
        orbit_depth(path_state(ambient_order)) == ambient_order // 2,
        ("path witness", ambient_order),
    )
    fixed = sum(is_even(state) for state in states)
    expected_fixed = sum(
        comb(ambient_order, size) * even_graph_count(size)
        for size in range(ambient_order + 1)
    )
    check(fixed == expected_fixed, ("fixed census", ambient_order))
    if ambient_order == 0:
        check(len(states) == fixed == 1 and maximum_depth == 0, "n=0")
    if ambient_order == 1:
        check(len(states) == fixed == 2 and maximum_depth == 0, "n=1")

    CURRENT_SECTION = "all-time fibres/images/CDF"
    power = identity(ambient_order + 1)
    geometric = identity(ambient_order + 1)
    current = {state: state for state in states}
    terminal_cdf = 0
    previous_cdf = 0
    for time in range(maximum_depth + 3):
        refined: Counter[tuple[State, int]] = Counter(
            (target, state_rank(source)) for source, target in current.items()
        )
        observed_image = set(current.values())
        predicted_image = {
            target
            for target in states
            if time == 0
            or is_even(target)
            or ambient_order - state_rank(target) >= 2 * time
        }
        check(observed_image == predicted_image, ("image set", ambient_order, time))
        check(
            len(observed_image) == predicted_image_count(ambient_order, time),
            ("image count", ambient_order, time),
        )

        for target in states:
            target_size = state_rank(target)
            formula = geometric if is_even(target) else power
            for source_size in range(ambient_order + 1):
                check(
                    refined[target, source_size]
                    == formula[target_size][source_size],
                    ("iterate fibre", ambient_order, time, target, source_size),
                )

        terminal_cdf = sum(
            comb(ambient_order, target_size)
            * even_graph_count(target_size)
            * sum(geometric[target_size])
            for target_size in range(ambient_order + 1)
        )
        literal_cdf = sum(
            multiplicity
            for depth, multiplicity in depths.items()
            if depth <= time
        )
        check(terminal_cdf == literal_cdf, ("temporal CDF", ambient_order, time))
        literal_shell = depths.get(time, 0)
        check(
            terminal_cdf - previous_cdf == literal_shell,
            ("exact shell", ambient_order, time),
        )
        previous_cdf = terminal_cdf

        power = compose(power, matrix)
        geometric = matrix_sum(geometric, power)
        current = {source: update(target) for source, target in current.items()}

    check(terminal_cdf == len(states), ("terminal CDF", ambient_order))
    return len(states), fixed, maximum_depth, terminal_cdf


def audit_orientation_and_nilpotence() -> None:
    global CURRENT_SECTION
    CURRENT_SECTION = "matrix orientation/nilpotence"
    matrix = transfer(4)
    square = compose(matrix, matrix)
    check(matrix[0][2] == 6, "B4[0,2]")
    check(matrix[2][0] == 0, "B4[2,0]")
    check(square[0][4] == 24, "B4^2[0,4]")

    for ambient_order in range(11):
        matrix = transfer(ambient_order)
        power = identity(ambient_order + 1)
        for _ in range(ambient_order // 2 + 1):
            power = compose(power, matrix)
        check(zero_matrix(power), ("nilpotence", ambient_order))


def main() -> None:
    audit_parity_systems()
    rows = [(order, *audit_order(order)) for order in range(7)]
    audit_orientation_and_nilpotence()

    DIAGNOSTICS["total_enumerated_states"] = sum(row[1] for row in rows)
    print("P159 parallel odd-vertex pruning exact verifier")
    for section in sorted(SECTION_ASSERTIONS):
        print(f"{section}: {SECTION_ASSERTIONS[section]}")
    for order, total, fixed, height, cdf in rows:
        print(
            f"order_n={order} states={total} fixed={fixed}"
            f" height={height} terminal_cdf={cdf}"
        )
    for diagnostic in sorted(DIAGNOSTICS):
        print(f"{diagnostic}={DIAGNOSTICS[diagnostic]}")
    print("orientation_B4_0_2=6 orientation_B4_2_0=0 square_B4_0_4=24")
    print(f"assertions={ASSERTIONS}")
    print("arithmetic=integer_and_GF2_exact")
    print("enumeration_is_not_proof=1")
    print("owner_clearance=0")
    print("external_status=HOLD_EXTERNAL")
    print("PASS")


if __name__ == "__main__":
    main()
