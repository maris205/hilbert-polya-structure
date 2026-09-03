#!/usr/bin/env python3
"""Second-pass exact breadth: non-extraction permutation/word/matching maps.

All maps preserve carrier size.  None deletes/prunes objects and none is a
parity-linear update.  Finite boxes are falsifiers, not proofs or novelty
evidence.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def finite_stats(states, step):
    states = tuple(states)
    state_set = set(states)
    successor = {}
    fibres = Counter()
    for state in states:
        target = step(state)
        check(target in state_set, "carrier closure")
        successor[state] = target
        fibres[target] += 1

    orbit_data = {}
    cycles = Counter()
    for start in states:
        if start in orbit_data:
            continue
        path = []
        position = {}
        point = start
        while point not in orbit_data and point not in position:
            position[point] = len(path)
            path.append(point)
            point = successor[point]
        if point in position:
            cycle_start = position[point]
            period = len(path) - cycle_start
            cycles[period] += 1
            for state in path[cycle_start:]:
                orbit_data[state] = (0, period)
            path = path[:cycle_start]
        for state in reversed(path):
            tail, period = orbit_data[successor[state]]
            orbit_data[state] = (tail + 1, period)
    check(len(orbit_data) == len(states), "functional graph coverage")
    period_states = Counter(period for _, period in orbit_data.values())
    return {
        "states": len(states),
        "image": len(fibres),
        "fixed": sum(successor[x] == x for x in states),
        "tail": max(tail for tail, _ in orbit_data.values()),
        "cycles": dict(sorted(cycles.items())),
        "period_states": dict(sorted(period_states.items())),
        "max_fibre": max(fibres.values()),
    }, successor, fibres


def emit(handle: str, box: str, stats: dict) -> None:
    print(
        f"{handle} {box} states={stats['states']} image={stats['image']} "
        f"fixed={stats['fixed']} tail={stats['tail']} cycles={stats['cycles']} "
        f"period_states={stats['period_states']} max_fibre={stats['max_fibre']}"
    )


# ---------------------------------------------------------------------------
# Permutations: all outputs are stable ranks of nonlinear, state-dependent
# scores.  Stable ties use the current position and are part of the literal map.


def stable_ranks(scores):
    order = sorted(range(len(scores)), key=lambda index: (scores[index], index))
    answer = [0] * len(scores)
    for rank, index in enumerate(order, 1):
        answer[index] = rank
    return tuple(answer)


def value_index_sum(word):
    return stable_ranks(tuple(value + index + 1 for index, value in enumerate(word)))


def neighbour_product(word):
    n = len(word)
    return stable_ranks(tuple(word[index] * word[(index + 1) % n] for index in range(n)))


def successor_position(word):
    n = len(word)
    position = {value: index + 1 for index, value in enumerate(word)}
    return stable_ranks(
        tuple(value + position[1 + value % n] for value in word)
    )


def inversion_degree(word):
    n = len(word)
    scores = []
    for index in range(n):
        degree = sum(
            (index - other) * (word[index] - word[other]) < 0
            for other in range(n)
            if other != index
        )
        scores.append(degree)
    return stable_ranks(tuple(scores))


def cyclic_triple_range(word):
    n = len(word)
    scores = []
    for index in range(n):
        window = (word[index - 1], word[index], word[(index + 1) % n])
        scores.append(max(window) - min(window))
    return stable_ranks(tuple(scores))


def successor_distance(word):
    n = len(word)
    position = {value: index for index, value in enumerate(word)}
    scores = tuple(
        abs(index - position[1 + value % n])
        for index, value in enumerate(word)
    )
    return stable_ranks(scores)


PERMUTATION_MAPS = (
    ("A01_VIS", value_index_sum),
    ("A02_NPR", neighbour_product),
    ("A03_SPR", successor_position),
    ("A04_IGR", inversion_degree),
    ("A05_CTR", cyclic_triple_range),
    ("A06_SDR", successor_distance),
)


def audit_permutations():
    for n in range(2, 9):
        states = tuple(permutations(range(1, n + 1)))
        identity = tuple(range(1, n + 1))
        for handle, step in PERMUTATION_MAPS:
            stats, successor, _ = finite_stats(states, step)
            emit(handle, f"n={n}", stats)
            for target in successor.values():
                check(tuple(sorted(target)) == identity, f"{handle} permutation output")


# ---------------------------------------------------------------------------
# Fixed-length words.  Every update only reorders or globally renames existing
# letters; no site is extracted or deleted.


def frequency_first_rename(word, alphabet_size: int):
    n = len(word)
    counts = Counter(word)
    first = {letter: (word.index(letter) if letter in counts else n) for letter in range(alphabet_size)}
    order = sorted(range(alphabet_size), key=lambda letter: (counts[letter], first[letter], letter))
    rename = {letter: rank for rank, letter in enumerate(order)}
    return tuple(rename[letter] for letter in word)


def linear_runs(word):
    if not word:
        return ()
    runs = []
    start = 0
    for index in range(1, len(word) + 1):
        if index == len(word) or word[index] != word[start]:
            runs.append((word[start], index - start))
            start = index
    return tuple(runs)


def flatten_runs(runs):
    return tuple(letter for letter, length in runs for _ in range(length))


def run_size_sort(word, alphabet_size: int):
    del alphabet_size
    runs = linear_runs(word)
    ordered = sorted(enumerate(runs), key=lambda item: (item[1][1], item[1][0], item[0]))
    return flatten_runs(tuple(run for _, run in ordered))


def longest_run_swap(word, alphabet_size: int):
    del alphabet_size
    runs = list(linear_runs(word))
    if len(runs) < 2:
        return word
    selected = min(range(len(runs)), key=lambda index: (-runs[index][1], index))
    neighbour = (selected + 1) % len(runs)
    runs[selected], runs[neighbour] = runs[neighbour], runs[selected]
    return flatten_runs(tuple(runs))


def first_frequency_rotate(word, alphabet_size: int):
    del alphabet_size
    if not word:
        return word
    shift = word.count(word[0]) % len(word)
    return word[shift:] + word[:shift]


def cyclic_bigram_sort(word, alphabet_size: int):
    del alphabet_size
    n = len(word)
    order = sorted(range(n), key=lambda index: (word[index], word[(index + 1) % n], index))
    return tuple(word[index] for index in order)


def occurrence_layer_shuffle(word, alphabet_size: int):
    del alphabet_size
    seen = Counter()
    keys = []
    for index, letter in enumerate(word):
        keys.append((seen[letter], letter, index))
        seen[letter] += 1
    order = sorted(range(len(word)), key=lambda index: keys[index])
    return tuple(word[index] for index in order)


WORD_MAPS = (
    ("B01_FFR", frequency_first_rename, False),
    ("B02_RSS", run_size_sort, True),
    ("B03_LRS", longest_run_swap, True),
    ("B04_FCR", first_frequency_rotate, True),
    ("B05_BGS", cyclic_bigram_sort, True),
    ("B06_OLS", occurrence_layer_shuffle, True),
)


def audit_words():
    for alphabet_size, maximum_length in ((2, 10), (3, 7)):
        for n in range(1, maximum_length + 1):
            states = tuple(product(range(alphabet_size), repeat=n))
            for handle, step, preserves_counts in WORD_MAPS:
                update = lambda word, q=alphabet_size, f=step: f(word, q)
                stats, successor, _ = finite_stats(states, update)
                emit(handle, f"q={alphabet_size},n={n}", stats)
                if preserves_counts:
                    for state, target in successor.items():
                        check(Counter(state) == Counter(target), f"{handle} content preservation")


# ---------------------------------------------------------------------------
# Perfect matchings on [2m], represented as lexicographically sorted edges.


@lru_cache(maxsize=None)
def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    first = vertices[0]
    answer = []
    for partner_index in range(1, len(vertices)):
        partner = vertices[partner_index]
        remaining = vertices[1:partner_index] + vertices[partner_index + 1 :]
        for rest in perfect_matchings(remaining):
            answer.append(tuple(sorted(((first, partner),) + rest)))
    return tuple(answer)


def canonical_matching(edges):
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def matching_valid(edges, order: int) -> bool:
    flat = [vertex for edge in edges for vertex in edge]
    return len(edges) * 2 == order and sorted(flat) == list(range(order)) and all(a < b for a, b in edges)


def cyclic_cross(edges, key):
    ordered = sorted(edges, key=key)
    lows = [edge[0] for edge in ordered]
    highs = [edge[1] for edge in ordered]
    return canonical_matching((lows[index], highs[(index + 1) % len(edges)]) for index in range(len(edges)))


def minimum_order_cross(edges):
    return cyclic_cross(edges, key=lambda edge: (edge[0], edge[1]))


def sum_order_cross(edges):
    return cyclic_cross(edges, key=lambda edge: (sum(edge), edge[1] - edge[0], edge))


def length_endpoint_weave(edges):
    ordered = sorted(edges, key=lambda edge: (edge[1] - edge[0], sum(edge), edge))
    sequence = [edge[0] for edge in ordered] + [edge[1] for edge in reversed(ordered)]
    return canonical_matching((sequence[index], sequence[index + 1]) for index in range(0, len(sequence), 2))


def relabel_matching(edges, vertex_key):
    order = 2 * len(edges)
    partner = [None] * order
    for left, right in edges:
        partner[left] = right
        partner[right] = left
    vertices = sorted(range(order), key=lambda vertex: (vertex_key(vertex, partner), vertex))
    rank = {vertex: new for new, vertex in enumerate(vertices)}
    return canonical_matching((rank[left], rank[right]) for left, right in edges)


def endpoint_sum_relabel(edges):
    return relabel_matching(edges, lambda vertex, partner: vertex + partner[vertex])


def endpoint_distance_relabel(edges):
    return relabel_matching(edges, lambda vertex, partner: abs(vertex - partner[vertex]))


def crossing_degree_relabel(edges):
    degree = {}
    for edge in edges:
        a, b = edge
        degree[edge] = sum(
            (a < c < b < d) or (c < a < d < b)
            for c, d in edges
            if (c, d) != edge
        )
    owner = {vertex: edge for edge in edges for vertex in edge}
    return relabel_matching(
        edges,
        lambda vertex, partner: (degree[owner[vertex]], int(vertex > partner[vertex])),
    )


MATCHING_MAPS = (
    ("C01_MOC", minimum_order_cross),
    ("C02_SOC", sum_order_cross),
    ("C03_LEW", length_endpoint_weave),
    ("C04_ESR", endpoint_sum_relabel),
    ("C05_EDR", endpoint_distance_relabel),
    ("C06_CDR", crossing_degree_relabel),
)


def audit_matchings():
    for pairs in range(1, 7):
        order = 2 * pairs
        states = perfect_matchings(tuple(range(order)))
        expected = 1
        for odd in range(1, order, 2):
            expected *= odd
        check(len(states) == expected, "perfect matching census")
        for handle, step in MATCHING_MAPS:
            stats, successor, _ = finite_stats(states, step)
            emit(handle, f"pairs={pairs}", stats)
            for target in successor.values():
                check(matching_valid(target, order), f"{handle} perfect matching output")


def distinctness_witnesses(states, named_steps, label):
    pairs = 0
    for left_index, (left_name, left_step) in enumerate(named_steps):
        for right_name, right_step in named_steps[left_index + 1 :]:
            witness = next(
                (state for state in states if left_step(state) != right_step(state)),
                None,
            )
            check(witness is not None, f"{label} literals {left_name}/{right_name} differ")
            pairs += 1
    print(f"DISTINCT {label}_pairs={pairs} PASS")


def audit_distinct_literals():
    permutation_states = tuple(permutations(range(1, 9)))
    distinctness_witnesses(permutation_states, PERMUTATION_MAPS, "permutation")

    word_states = tuple(product(range(2), repeat=10))
    word_steps = tuple(
        (handle, lambda word, fn=step: fn(word, 2))
        for handle, step, _ in WORD_MAPS
    )
    distinctness_witnesses(word_states, word_steps, "word")

    matching_states = perfect_matchings(tuple(range(12)))
    distinctness_witnesses(matching_states, MATCHING_MAPS, "matching")


def main() -> None:
    print("Focused non-extraction permutation/word/matching breadth")
    print("STATUS HOLD_EXTERNAL")
    audit_permutations()
    audit_words()
    audit_matchings()
    audit_distinct_literals()
    print("SYSTEMS 18")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
