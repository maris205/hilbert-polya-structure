#!/usr/bin/env python3
"""Exact theorem-interface falsifier for P149; standard library only.

The bounded census is independent counterexample pressure.  The manuscript's
all-rank statements are proved combinatorially rather than inferred here.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import factorial


ASSERTIONS = 0


def check(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


Permutation = tuple[int, ...]


def standardize(word: tuple[int, ...] | list[int]) -> Permutation:
    ranks = {value: rank for rank, value in enumerate(sorted(word), 1)}
    return tuple(ranks[value] for value in word)


def extract(state: Permutation) -> Permutation:
    if len(state) == 1:
        return state
    peaks = []
    for index, value in enumerate(state):
        left = state[index - 1] if index else 0
        right = state[index + 1] if index + 1 < len(state) else 0
        if left < value > right:
            peaks.append(value)
    return standardize(peaks)


def orbit_tail(state: Permutation) -> int:
    steps = 0
    while len(state) > 1:
        state = extract(state)
        steps += 1
    return steps


def one_step_section(target: Permutation, source_size: int) -> Permutation:
    m = len(target)
    check(source_size >= 2 * m - 1,
          (source_size, target, "one-step section packing"))
    high = tuple(source_size - m + value for value in target)
    answer = []
    for index, value in enumerate(high):
        answer.append(value)
        if index + 1 < m:
            answer.append(index + 1)
    answer.extend(range(source_size - m, m - 1, -1))
    return tuple(answer)


def iterated_section(
    target: Permutation, source_size: int, iterations: int
) -> Permutation:
    check(iterations >= 1, (iterations, "positive iterate rank"))
    state = target
    for _ in range(iterations - 1):
        state = one_step_section(state, 2 * len(state) - 1)
    return one_step_section(state, source_size)


@lru_cache(maxsize=None)
def deepest_witness(size: int) -> Permutation:
    if size == 1:
        return (1,)
    return one_step_section(deepest_witness((size + 1) // 2), size)


def peak_positions(comparisons: tuple[int, ...]) -> tuple[int, ...]:
    n = len(comparisons) + 1
    if n == 1:
        return (0,)
    answer = []
    if comparisons[0] == 0:  # D: first value exceeds its right neighbour.
        answer.append(0)
    for index in range(1, n - 1):
        if comparisons[index - 1] == 1 and comparisons[index] == 0:
            answer.append(index)
    if comparisons[-1] == 1:  # U: last value exceeds its left neighbour.
        answer.append(n - 1)
    return tuple(answer)


def linear_extensions(vertices: int, relations: list[tuple[int, int]]) -> int:
    predecessors = [0] * vertices
    for smaller, larger in relations:
        predecessors[larger] |= 1 << smaller

    @lru_cache(maxsize=None)
    def count(chosen: int) -> int:
        if chosen == (1 << vertices) - 1:
            return 1
        total = 0
        for vertex in range(vertices):
            if chosen >> vertex & 1:
                continue
            if predecessors[vertex] & ~chosen == 0:
                total += count(chosen | (1 << vertex))
        return total

    return count(0)


@lru_cache(maxsize=None)
def target_fibre(source_size: int, target: Permutation) -> int:
    if source_size == 1:
        return int(target == (1,))
    total = 0
    for comparisons in product((0, 1), repeat=source_size - 1):
        peaks = peak_positions(comparisons)
        if len(peaks) != len(target):
            continue
        relations = []
        for index, comparison in enumerate(comparisons):
            if comparison == 1:  # U
                relations.append((index, index + 1))
            else:  # D
                relations.append((index + 1, index))
        peak_by_rank = [0] * len(target)
        for output_position, rank in enumerate(target):
            peak_by_rank[rank - 1] = peaks[output_position]
        relations.extend(zip(peak_by_rank, peak_by_rank[1:]))
        total += linear_extensions(source_size, relations)
    return total


def symmetric_union(bound: int) -> set[Permutation]:
    answer = set()
    for rank in range(1, bound + 1):
        answer.update(permutations(range(1, rank + 1)))
    return answer


def main() -> None:
    print("P149 EXACT CONTROL")
    print("columns=n,states,image,fixed,max_tail,tail_profile")
    max_checked_iterate = 5
    for n in range(1, 10):
        one_step = Counter()
        iterated_images = [set() for _ in range(max_checked_iterate + 1)]
        tails = Counter()
        fixed = 0
        states = 0
        for state in permutations(range(1, n + 1)):
            states += 1
            image = extract(state)
            one_step[image] += 1
            check(1 <= len(image) <= (n + 1) // 2,
                  (n, state, "endpoint-peak packing"))
            if n > 1:
                check(len(image) < n, (n, state, "strict rank descent"))
            fixed += int(image == state)
            time = orbit_tail(state)
            tails[time] += 1
            check(time <= (n - 1).bit_length(), (n, state, "clock upper bound"))
            iterate = state
            for rank in range(1, max_checked_iterate + 1):
                iterate = extract(iterate)
                iterated_images[rank].add(iterate)

        check(states == factorial(n), (n, "symmetric-group census"))
        check(fixed == int(n == 1), (n, "unique recurrent state"))
        for rank in range(1, max_checked_iterate + 1):
            bound = (n + (1 << rank) - 1) // (1 << rank)
            expected = symmetric_union(bound)
            check(iterated_images[rank] == expected,
                  (n, rank, "all-rank iterate image"))
            if n <= 8:
                for target in expected:
                    section = iterated_section(target, n, rank)
                    check(tuple(sorted(section)) == tuple(range(1, n + 1)),
                          (n, rank, target, "section is a permutation"))
                    image = section
                    for _ in range(rank):
                        image = extract(image)
                    check(image == target, (n, rank, target, "right section"))

        if n <= 8:
            possible = symmetric_union((n + 1) // 2)
            check(set(one_step) == possible, (n, "one-step image support"))
            for target in possible:
                predicted = target_fibre(n, target)
                check(one_step[target] == predicted,
                      (n, target, "comparison-poset fibre"))
            check(sum(target_fibre(n, target) for target in possible) == factorial(n),
                  (n, "fibre mass partition"))

        maximum = (n - 1).bit_length()
        check(max(tails) == maximum, (n, "sharp logarithmic clock"))
        witness = deepest_witness(n)
        check(tuple(sorted(witness)) == tuple(range(1, n + 1)),
              (n, "recursive witness is a permutation"))
        check(orbit_tail(witness) == maximum, (n, "recursive witness clock"))
        length = n
        state = witness
        while length > 1:
            state = extract(state)
            length = (length + 1) // 2
            check(len(state) == length, (n, "witness saturates packing"))

        profile = ";".join(f"{time}:{count}" for time, count in sorted(tails.items()))
        print(n, states, len(one_step), fixed, max(tails), profile, sep=",")

    print(f"assertions={ASSERTIONS}")
    print("P149_THEOREM_INTERFACES_PASS")


if __name__ == "__main__":
    main()
