#!/usr/bin/env python3
"""Exact controls for synchronous tournament score-upset reversal.

The phase space contains every labelled tournament on ``[n]``.  For an
unordered pair, the update points the edge from the endpoint of larger
current outdegree to the endpoint of smaller current outdegree; a tied pair
keeps its old orientation.  All computations are integer and exhaustive.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


ASSERTIONS = 0
STATES_ENUMERATED = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def edge_table(n):
    return tuple(combinations(range(n), 2))


@lru_cache(None)
def edge_index(n):
    return {edge: bit for bit, edge in enumerate(edge_table(n))}


def scores(state, n):
    outdegrees = [0] * n
    for bit, (left, right) in enumerate(edge_table(n)):
        winner = left if (state >> bit) & 1 else right
        outdegrees[winner] += 1
    return tuple(outdegrees)


def energy(state, n):
    return sum(value * value for value in scores(state, n))


def update(state, n):
    old_scores = scores(state, n)
    image = 0
    for bit, (left, right) in enumerate(edge_table(n)):
        if old_scores[left] > old_scores[right]:
            orientation = 1
        elif old_scores[left] < old_scores[right]:
            orientation = 0
        else:
            orientation = (state >> bit) & 1
        image |= orientation << bit
    return image


def literal_update(state, n):
    """Set-of-arcs realization, separate from the bitwise update loop."""

    arcs = set()
    for bit, (left, right) in enumerate(edge_table(n)):
        arcs.add((left, right) if (state >> bit) & 1 else (right, left))

    old_scores = tuple(sum(left == vertex for left, _ in arcs) for vertex in range(n))
    image_arcs = set()
    for left, right in edge_table(n):
        if old_scores[left] > old_scores[right]:
            image_arcs.add((left, right))
        elif old_scores[left] < old_scores[right]:
            image_arcs.add((right, left))
        elif (left, right) in arcs:
            image_arcs.add((left, right))
        else:
            image_arcs.add((right, left))

    image = 0
    for bit, edge in enumerate(edge_table(n)):
        image |= int(edge in image_arcs) << bit
    return image


def score_classes(state, n):
    grouped = {}
    for vertex, value in enumerate(scores(state, n)):
        grouped.setdefault(value, []).append(vertex)
    return tuple(tuple(grouped[value]) for value in sorted(grouped, reverse=True))


def induced_state(state, n, vertices):
    vertices = tuple(sorted(vertices))
    local = 0
    for local_bit, (left_index, right_index) in enumerate(edge_table(len(vertices))):
        left = vertices[left_index]
        right = vertices[right_index]
        original_bit = edge_index(n)[(left, right)]
        local |= ((state >> original_bit) & 1) << local_bit
    return local


def ordinal_sum(blocks, internal_states):
    """Embed local tournaments and direct every earlier block to every later one."""

    vertices = sorted(vertex for block in blocks for vertex in block)
    n = len(vertices)
    check(vertices == list(range(n)), "ordinal-sum blocks do not partition [n]")
    block_of = {}
    local_position = {}
    for block_number, block in enumerate(blocks):
        for position, vertex in enumerate(sorted(block)):
            block_of[vertex] = block_number
            local_position[vertex] = position

    state = 0
    for bit, (left, right) in enumerate(edge_table(n)):
        left_block = block_of[left]
        right_block = block_of[right]
        if left_block != right_block:
            winner = left if left_block < right_block else right
            orientation = int(winner == left)
        else:
            local_left = local_position[left]
            local_right = local_position[right]
            local_bit = edge_index(len(blocks[left_block]))[(local_left, local_right)]
            orientation = (internal_states[left_block] >> local_bit) & 1
        state |= orientation << bit
    return state


def iterate(state, n, time):
    for _ in range(time):
        state = update(state, n)
    return state


def factorized_iterate(state, n, time):
    if time == 0:
        return state
    blocks = score_classes(state, n)
    internal = []
    for block in blocks:
        local = induced_state(state, n, block)
        internal.append(iterate(local, len(block), time - 1))
    return ordinal_sum(blocks, tuple(internal))


def fixed_regular_sum_structure(state, n):
    old_scores = scores(state, n)
    blocks = score_classes(state, n)
    for block in blocks:
        local_scores = scores(induced_state(state, n, block), len(block))
        if len(set(local_scores)) > 1:
            return False
    for bit, (left, right) in enumerate(edge_table(n)):
        if old_scores[left] == old_scores[right]:
            continue
        left_wins = bool((state >> bit) & 1)
        if left_wins != (old_scores[left] > old_scores[right]):
            return False
    return True


@lru_cache(None)
def recursive_depth(state, n):
    if update(state, n) == state:
        return 0
    blocks = score_classes(state, n)
    return 1 + max(
        recursive_depth(induced_state(state, n, block), len(block))
        for block in blocks
    )


def orbit_depth(state, n):
    seen = set()
    depth = 0
    while True:
        check(state not in seen, "a nontrivial temporal cycle was found")
        seen.add(state)
        image = update(state, n)
        if image == state:
            return depth, state
        state = image
        depth += 1


def energy_identity(state, n):
    image = update(state, n)
    old_scores = scores(state, n)
    new_scores = scores(image, n)
    corrected_gap_sum = 0
    for bit, (left, right) in enumerate(edge_table(n)):
        winner, loser = (
            (left, right) if (state >> bit) & 1 else (right, left)
        )
        if old_scores[winner] < old_scores[loser]:
            corrected_gap_sum += old_scores[loser] - old_scores[winner]
    deltas = [new - old for new, old in zip(new_scores, old_scores)]
    right_hand_side = 2 * corrected_gap_sum + sum(delta * delta for delta in deltas)
    return energy(image, n) - energy(state, n), right_hand_side


def regular_counts(limit):
    counts = [0] * (limit + 1)
    for n in range(1, limit + 1, 2):
        target = (n - 1) // 2
        counts[n] = sum(
            scores(state, n) == (target,) * n
            for state in range(1 << len(edge_table(n)))
        )
    return counts


def recurrence_fixed_counts(limit, regular):
    fixed = [0] * (limit + 1)
    fixed[0] = 1
    for n in range(1, limit + 1):
        fixed[n] = sum(
            comb(n, block_size)
            * regular[block_size]
            * fixed[n - block_size]
            for block_size in range(1, n + 1)
        )
    return fixed


def lane(n):
    global STATES_ENUMERATED
    phase_size = 1 << len(edge_table(n))
    depth_histogram = Counter()
    fixed_count = 0

    for start in range(phase_size):
        STATES_ENUMERATED += 1
        image = update(start, n)
        old_scores = scores(start, n)
        new_scores = scores(image, n)
        blocks = score_classes(start, n)

        check(image == literal_update(start, n), "bit and literal updates disagree")
        local_sources = tuple(induced_state(start, n, block) for block in blocks)
        check(image == ordinal_sum(blocks, local_sources), "score-class ordinal sum failed")

        observed_energy_gain, predicted_energy_gain = energy_identity(start, n)
        check(observed_energy_gain == predicted_energy_gain, "exact energy identity failed")
        check(
            (observed_energy_gain > 0) == (image != start),
            "energy was not strict exactly on changed states",
        )

        for block_number, block in enumerate(blocks):
            lower_vertices = sum(len(later) for later in blocks[block_number + 1 :])
            local_scores = scores(local_sources[block_number], len(block))
            for local_vertex, vertex in enumerate(block):
                check(
                    new_scores[vertex] == lower_vertices + local_scores[local_vertex],
                    "new global score did not split into lower-block and internal wins",
                )
        for left in range(n):
            for right in range(n):
                if old_scores[left] > old_scores[right]:
                    check(
                        new_scores[left] > new_scores[right],
                        "strict order between old score classes was not preserved",
                    )

        for time in range(1, n + 1):
            check(
                iterate(start, n, time) == factorized_iterate(start, n, time),
                "recursive factorization of an iterate failed",
            )

        depth, endpoint = orbit_depth(start, n)
        if n == 0:
            check(depth == 0, "the empty tournament was not fixed")
        else:
            check(depth <= n - 1, "the universal n-1 depth bound failed")
        check(depth == recursive_depth(start, n), "orbit and refinement-tree depths disagree")
        check(update(endpoint, n) == endpoint, "reported endpoint was not fixed")
        check(
            fixed_regular_sum_structure(endpoint, n),
            "endpoint was not an ordered sum of regular score blocks",
        )

        fixed = image == start
        check(
            fixed == fixed_regular_sum_structure(start, n),
            "fixed-point structure criterion failed",
        )
        for period in range(1, 9):
            check(
                (iterate(start, n, period) == start) == fixed,
                "a positive iterate had an unexpected fixed point",
            )

        fixed_count += fixed
        depth_histogram[depth] += 1

    return {
        "n": n,
        "phase": phase_size,
        "fixed": fixed_count,
        "max_depth": max(depth_histogram),
        "depths": dict(sorted(depth_histogram.items())),
    }


def least_nonidempotent_in_specified_scan(limit):
    """Scan increasing orders, then increasing numerical masks."""
    for n in range(limit + 1):
        for state in range(1 << len(edge_table(n))):
            first = update(state, n)
            second = update(first, n)
            if second != first:
                return {
                    "n": n,
                    "state": state,
                    "scores": scores(state, n),
                    "first": first,
                    "first_scores": scores(first, n),
                    "second": second,
                    "second_scores": scores(second, n),
                }
    return None


def main():
    regular = regular_counts(6)
    predicted_fixed = recurrence_fixed_counts(6, regular)
    rows = [lane(n) for n in range(7)]
    observed_fixed = [row["fixed"] for row in rows]

    check(regular == [0, 1, 0, 2, 0, 24, 0], "unexpected regular-tournament counts")
    check(
        predicted_fixed == [1, 1, 2, 8, 40, 264, 2048],
        "unexpected fixed-count recurrence values",
    )
    check(observed_fixed == predicted_fixed, "fixed census and recurrence disagree")
    check(
        [row["depths"] for row in rows]
        == [
            {0: 1},
            {0: 1},
            {0: 2},
            {0: 8},
            {0: 40, 1: 24},
            {0: 264, 1: 760},
            {0: 2048, 1: 26400, 2: 4320},
        ],
        "unexpected exact depth histograms",
    )

    witness = least_nonidempotent_in_specified_scan(6)
    check(
        witness
        == {
            "n": 6,
            "state": 148,
            "scores": (2, 2, 2, 2, 3, 4),
            "first": 4,
            "first_scores": (1, 1, 2, 2, 4, 5),
            "second": 0,
            "second_scores": (0, 1, 2, 3, 4, 5),
        },
        "the least nonidempotent state in the specified scan changed",
    )

    print("synchronous tournament score-upset reversal controls: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states_enumerated={STATES_ENUMERATED}")
    print(f"regular_counts={regular}")
    print(f"fixed_counts={predicted_fixed}")
    print(f"least_nonidempotent_in_specified_scan={witness}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} phase={row['phase']} fixed={row['fixed']}"
            f" max_depth={row['max_depth']} depths={row['depths']}"
        )


if __name__ == "__main__":
    main()
