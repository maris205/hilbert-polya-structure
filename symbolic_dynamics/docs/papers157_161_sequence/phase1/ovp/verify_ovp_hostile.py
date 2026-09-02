#!/usr/bin/env python3
"""Independent hostile falsifier for parallel odd-vertex pruning.

This review-side program deliberately does not import or copy the bit-mask
implementation in ``verify_ovp_focused.py``.  States are immutable labelled
vertex/edge tuples, the update is reconstructed from degree sets, and the
formula lane is assembled from a separately oriented rank-transfer matrix.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations
from math import comb


ASSERTIONS = 0


def require(condition: bool, witness: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(witness)


VertexSet = tuple[int, ...]
Edge = tuple[int, int]
State = tuple[VertexSet, tuple[Edge, ...]]


@cache
def carrier(ambient_order: int) -> tuple[State, ...]:
    answer: list[State] = []
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
                answer.append((vertices, edges))
    return tuple(answer)


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
    require(odd <= set(vertices), ("edge endpoint outside carrier", state))
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
        edge for edge in edges if edge[0] in survivor_set and edge[1] in survivor_set
    )
    return survivors, induced_edges


def even_graph_count(size: int) -> int:
    if size <= 1:
        return 1
    return 1 << comb(size - 1, 2)


def strict_entry(ambient_order: int, target_rank: int, source_rank: int) -> int:
    deleted = source_rank - target_rank
    if deleted <= 0 or deleted % 2:
        return 0
    exponent = target_rank * (deleted - 1) + comb(deleted - 1, 2)
    return comb(ambient_order - target_rank, deleted) * (1 << exponent)


def transfer(ambient_order: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(strict_entry(ambient_order, target, source)
              for source in range(ambient_order + 1))
        for target in range(ambient_order + 1)
    )


def identity(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(row == column) for column in range(width))
        for row in range(width)
    )


def matrix_sum(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Entrywise sum, kept separate from composition orientation."""

    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left)))
        for row in range(len(left))
    )


def compose(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Conventional product: row=final target, column=initial source."""

    width = len(left)
    return tuple(
        tuple(
            sum(left[target][middle] * right[middle][source]
                for middle in range(width))
            for source in range(width)
        )
        for target in range(width)
    )


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


def parity_system_audit() -> int:
    """Audit coefficient/augmented ranks without enumerating graph states."""

    cases = 0
    for total in range(1, 10):
        for deleted in range(1, total + 1):
            target = total - deleted
            variables = tuple(
                edge
                for edge in combinations(range(total), 2)
                if edge[0] >= target or edge[1] >= target
            )
            coefficient_rows = []
            for vertex in range(total):
                row = 0
                for index, edge in enumerate(variables):
                    if vertex in edge:
                        row |= 1 << index
                coefficient_rows.append(row)
            coefficient_rank = gf2_rank(tuple(coefficient_rows))
            require(coefficient_rank == total - 1,
                    ("wrong connected-incidence rank", target, deleted))

            # Every degree-parity vector of a graph on target labelled vertices
            # has even Hamming weight, and every such vector is attainable.
            for target_parity in range(1 << target):
                if target_parity.bit_count() % 2:
                    continue
                rhs = tuple(
                    ((target_parity >> vertex) & 1) if vertex < target else 1
                    for vertex in range(total)
                )
                augmented_rows = tuple(
                    coefficient_rows[vertex] | (rhs[vertex] << len(variables))
                    for vertex in range(total)
                )
                augmented_rank = gf2_rank(augmented_rows)
                solvable = augmented_rank == coefficient_rank
                require(solvable == (deleted % 2 == 0),
                        ("wrong parity consistency", target, deleted, target_parity))
                if solvable:
                    dimension = len(variables) - coefficient_rank
                    claimed_dimension = (
                        target * (deleted - 1) + comb(deleted - 1, 2)
                    )
                    require(dimension == claimed_dimension,
                            ("wrong nullity", target, deleted, target_parity))
                cases += 1
    return cases


def orbit_depth(state: State) -> int:
    seen: set[State] = set()
    current = state
    depth = 0
    while update(current) != current:
        require(current not in seen, ("strict cycle", state))
        seen.add(current)
        current = update(current)
        depth += 1
    return depth


def path_state(order: int) -> State:
    vertices = tuple(range(order))
    edges = tuple((index, index + 1) for index in range(order - 1))
    return vertices, edges


def audit_order(ambient_order: int) -> tuple[int, int, int, int]:
    states = carrier(ambient_order)
    state_set = set(states)
    one_step = {source: update(source) for source in states}
    require(set(one_step.values()) <= state_set, ("closure", ambient_order))

    strict_fibres: Counter[tuple[State, int]] = Counter()
    full_one_step: Counter[tuple[State, int]] = Counter()
    for source, target in one_step.items():
        source_size = state_rank(source)
        full_one_step[target, source_size] += 1
        loss = source_size - state_rank(target)
        require(loss == len(odd_vertices(source)), ("loss mismatch", source))
        require(loss % 2 == 0, ("odd rank loss", source))
        if loss:
            strict_fibres[target, source_size] += 1
            require(not is_even(source), ("strict predecessor is even", source))
        else:
            require(source == target and is_even(source), ("bad d=0 branch", source))

    matrix = transfer(ambient_order)
    for target in states:
        target_size = state_rank(target)
        for source_size in range(ambient_order + 1):
            require(
                strict_fibres[target, source_size]
                == matrix[target_size][source_size],
                ("strict fibre mismatch", ambient_order, target, source_size),
            )
            same_rank_expected = int(source_size == target_size and is_even(target))
            if source_size == target_size:
                require(
                    full_one_step[target, source_size] == same_rank_expected,
                    ("d=0 boundary mismatch", ambient_order, target),
                )

    depths = Counter(orbit_depth(state) for state in states)
    maximum_depth = max(depths)
    require(maximum_depth == ambient_order // 2,
            ("maximum clock", ambient_order, maximum_depth))
    require(orbit_depth(path_state(ambient_order)) == ambient_order // 2,
            ("path witness", ambient_order))
    fixed = sum(is_even(state) for state in states)
    expected_fixed = sum(
        comb(ambient_order, size) * even_graph_count(size)
        for size in range(ambient_order + 1)
    )
    require(fixed == expected_fixed, ("fixed census", ambient_order))

    power = identity(ambient_order + 1)
    geometric = identity(ambient_order + 1)
    current = {state: state for state in states}
    terminal_cdf = 0
    for time in range(ambient_order // 2 + 3):
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
        require(observed_image == predicted_image,
                ("image mismatch", ambient_order, time))

        for target in states:
            target_size = state_rank(target)
            formula = geometric if is_even(target) else power
            for source_size in range(ambient_order + 1):
                require(
                    refined[target, source_size]
                    == formula[target_size][source_size],
                    ("iterate fibre mismatch", ambient_order, time,
                     target, source_size),
                )

        terminal_cdf = sum(
            comb(ambient_order, target_size)
            * even_graph_count(target_size)
            * sum(geometric[target_size])
            for target_size in range(ambient_order + 1)
        )
        literal_cdf = sum(
            multiplicity for depth, multiplicity in depths.items() if depth <= time
        )
        require(terminal_cdf == literal_cdf,
                ("CDF mismatch", ambient_order, time))

        power = compose(power, matrix)
        geometric = matrix_sum(geometric, power)
        current = {source: update(target) for source, target in current.items()}

    if ambient_order == 0:
        require(len(states) == fixed == 1 and maximum_depth == 0, "n=0")
    if ambient_order == 1:
        require(len(states) == fixed == 2 and maximum_depth == 0, "n=1")
    if ambient_order >= 2:
        empty: State = ((), ())
        require(strict_fibres[empty, 2] == comb(ambient_order, 2),
                ("s=0,d=2", ambient_order))

    return len(states), fixed, maximum_depth, terminal_cdf


def main() -> None:
    parity_cases = parity_system_audit()
    rows = [(order, *audit_order(order)) for order in range(7)]

    orientation = transfer(4)
    square = compose(orientation, orientation)
    require(orientation[0][2] == 6, "row target / column source sentinel")
    require(orientation[2][0] == 0, "transpose sentinel")
    require(square[0][4] == 24, "two-step orientation sentinel")

    print("OVP_HOSTILE_REVIEW_VERIFIER_V1")
    print(f"PARITY_SYSTEM_CASES={parity_cases} RANK_NULLITY=PASS")
    print("BOUNDARY d=0:self_iff_even d=2,s=0:one_per_label_pair")
    print("MATRIX row=target_rank column=source_rank")
    print("ORIENTATION B4[0,2]=6 B4[2,0]=0 B4^2[0,4]=24")
    for order, total, fixed, height, cdf in rows:
        print(
            f"ORDER n={order} states={total} fixed={fixed}"
            f" height={height} terminal_cdf={cdf}"
        )
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
