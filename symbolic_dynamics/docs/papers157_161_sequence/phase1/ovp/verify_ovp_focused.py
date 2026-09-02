#!/usr/bin/env python3
"""Exact controls for parallel odd-vertex pruning of labelled graphs.

The carrier contains every simple graph on every subset of [n].  One epoch
simultaneously deletes all vertices of odd current degree.  The program
constructs the literal functional graph and independently checks the strict
inverse transfer, every-time target fibres, image criterion, temporal CDF,
and sharp clock.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


State = tuple[int, int]  # vertex mask, ambient edge mask


def ambient_edges(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def states(n: int) -> tuple[State, ...]:
    edges = ambient_edges(n)
    rows: list[State] = []
    for vertices in range(1 << n):
        available = [
            index
            for index, (u, v) in enumerate(edges)
            if (vertices >> u) & 1 and (vertices >> v) & 1
        ]
        for local_mask in range(1 << len(available)):
            graph = 0
            for bit, edge_index in enumerate(available):
                if (local_mask >> bit) & 1:
                    graph |= 1 << edge_index
            rows.append((vertices, graph))
    return tuple(rows)


def degrees_mod_two(state: State, n: int) -> int:
    vertices, graph = state
    parity = 0
    for index, (u, v) in enumerate(ambient_edges(n)):
        if (graph >> index) & 1:
            parity ^= (1 << u) | (1 << v)
    check(parity & ~vertices == 0, "edge has an absent endpoint")
    return parity


def step(state: State, n: int) -> State:
    vertices, graph = state
    odd = degrees_mod_two(state, n)
    survivors = vertices & ~odd
    kept_graph = 0
    for index, (u, v) in enumerate(ambient_edges(n)):
        if (
            (graph >> index) & 1
            and (survivors >> u) & 1
            and (survivors >> v) & 1
        ):
            kept_graph |= 1 << index
    return survivors, kept_graph


def iterate(state: State, n: int, time: int) -> State:
    for _ in range(time):
        state = step(state, n)
    return state


def rank(state: State) -> int:
    return state[0].bit_count()


def is_even(state: State, n: int) -> bool:
    return degrees_mod_two(state, n) == 0


def even_graph_count(size: int) -> int:
    if size <= 1:
        return 1
    return 1 << comb(size - 1, 2)


def strict_inverse_transfer(n: int) -> list[list[int]]:
    """B[s][m] counts strict rank-m predecessors of each rank-s target."""

    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for size in range(n + 1):
        for source_size in range(size + 2, n + 1, 2):
            deleted = source_size - size
            exponent = size * (deleted - 1) + comb(deleted - 1, 2)
            matrix[size][source_size] = (
                comb(n - size, deleted) * (1 << exponent)
            )
    return matrix


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n + 1)] for i in range(n + 1)]


def add(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [left[i][j] + right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    width = len(left)
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(width))
            for j in range(width)
        ]
        for i in range(width)
    ]


def target_fibre_formula(
    state: State,
    n: int,
    time: int,
    power: list[list[int]],
    partial_sum: list[list[int]],
) -> int:
    row = partial_sum if is_even(state, n) else power
    return sum(row[rank(state)])


def image_formula(state: State, n: int, time: int) -> bool:
    if time == 0 or is_even(state, n):
        return True
    return n - rank(state) >= 2 * time


def path_state(n: int) -> State:
    vertices = (1 << n) - 1
    lookup = {edge: index for index, edge in enumerate(ambient_edges(n))}
    graph = 0
    for vertex in range(n - 1):
        graph |= 1 << lookup[(vertex, vertex + 1)]
    return vertices, graph


def verify_order(n: int) -> tuple[int, int, int, int]:
    carrier = states(n)
    carrier_set = set(carrier)
    transfer = strict_inverse_transfer(n)

    literal_next = {state: step(state, n) for state in carrier}
    check(all(target in carrier_set for target in literal_next.values()), "closure")

    for state in carrier:
        deleted = rank(state) - rank(literal_next[state])
        check(deleted % 2 == 0, "odd number of odd-degree vertices")
        check((deleted == 0) == is_even(state, n), "fixed/even mismatch")
        check((literal_next[state] == state) == is_even(state, n), "fixed locus")

    depths: Counter[int] = Counter()
    endpoints: Counter[State] = Counter()
    for state in carrier:
        current = state
        depth = 0
        while literal_next[current] != current:
            current = literal_next[current]
            depth += 1
            check(depth <= n // 2, "clock bound")
        depths[depth] += 1
        endpoints[current] += 1
    check(max(depths) == n // 2, "sharp maximum depth")
    witness = path_state(n)
    witness_depth = 0
    while literal_next[witness] != witness:
        witness = literal_next[witness]
        witness_depth += 1
    check(witness_depth == n // 2, "path sharpness witness")

    expected_fixed = sum(
        comb(n, size) * even_graph_count(size) for size in range(n + 1)
    )
    observed_fixed = sum(is_even(state, n) for state in carrier)
    check(observed_fixed == expected_fixed, "even-graph fixed count")

    power = identity(n)
    partial_sum = identity(n)
    cumulative_depth = 0
    for time in range(n // 2 + 2):
        fibres = Counter(iterate(source, n, time) for source in carrier)
        observed_image = set(fibres)
        predicted_image = {
            target for target in carrier if image_formula(target, n, time)
        }
        check(observed_image == predicted_image, "exact image criterion")
        for target in carrier:
            check(
                fibres.get(target, 0)
                == target_fibre_formula(target, n, time, power, partial_sum),
                "every-time target fibre",
            )

        cumulative_depth = sum(
            comb(n, size)
            * even_graph_count(size)
            * sum(partial_sum[size])
            for size in range(n + 1)
        )
        check(
            cumulative_depth == sum(count for depth, count in depths.items() if depth <= time),
            "temporal CDF transfer",
        )

        power = multiply(power, transfer)
        partial_sum = add(partial_sum, power)

    return len(carrier), observed_fixed, max(depths), cumulative_depth


def main() -> None:
    rows = []
    for n in range(0, 7):
        rows.append((n, *verify_order(n)))

    print("ODD_VERTEX_PRUNING_FOCUSED_V1")
    print("CARRIER labelled_simple_graphs_on_all_subsets_of_[n]")
    print("UPDATE simultaneously_delete_all_current_odd_degree_vertices")
    print("CLOCK sharp_floor(n/2)_witnessed_by_the_labelled_path")
    print("INVERSE nilpotent_strict_rank_transfer_B_and_every_time_fibres")
    print("IMAGE even_graphs_or_at_least_2t_unused_labels")
    for n, total, fixed, height, cdf in rows:
        print(
            f"ORDER n={n} states={total} fixed={fixed}"
            f" height={height} terminal_cdf={cdf}"
        )
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
