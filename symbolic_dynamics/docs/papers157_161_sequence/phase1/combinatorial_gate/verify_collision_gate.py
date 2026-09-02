#!/usr/bin/env python3
"""Independent counterexample search for the LCP/PAE focused collision gate.

The script deliberately imports no earlier scout or paper verifier.  It
reconstructs both literal maps and compares them with closed formulas.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations, permutations
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, witness: object = None) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(witness)


A = Audit()


def standardize(values) -> tuple[int, ...]:
    word = tuple(values)
    order = {value: rank + 1 for rank, value in enumerate(sorted(word))}
    return tuple(order[value] for value in word)


def positive_compositions(total: int):
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        for rest in positive_compositions(total - first):
            yield (first,) + rest


# ---------------------------------------------------------------------------
# LCP: recursively delete the whole first-child subtree.


@cache
def plane_trees(size: int) -> tuple[tuple, ...]:
    if size == 1:
        return ((),)
    answer: list[tuple] = []
    for child_sizes in positive_compositions(size - 1):
        pools = [plane_trees(part) for part in child_sizes]

        def choose(index: int, prefix: list[tuple]) -> None:
            if index == len(pools):
                answer.append(tuple(prefix))
                return
            for child in pools[index]:
                prefix.append(child)
                choose(index + 1, prefix)
                prefix.pop()

        choose(0, [])
    return tuple(answer)


@cache
def tree_size(tree: tuple) -> int:
    return 1 + sum(tree_size(child) for child in tree)


def lcp(tree: tuple) -> tuple:
    return tuple(lcp(child) for child in tree[1:])


def lcp_power_literal(tree: tuple, time: int) -> tuple:
    for _ in range(time):
        tree = lcp(tree)
    return tree


def lcp_coordinate_formula(tree: tuple, time: int) -> tuple:
    return tuple(lcp_coordinate_formula(child, time) for child in tree[time:])


def sibling_bottleneck(tree: tuple) -> int:
    answer = 0

    def visit(node: tuple, path_minimum: int) -> None:
        nonlocal answer
        for index, child in enumerate(node, 1):
            child_minimum = min(path_minimum, index)
            answer = max(answer, child_minimum)
            visit(child, child_minimum)

    visit(tree, 10**9)
    return answer


def lcp_tail(tree: tuple) -> int:
    time = 0
    while tree:
        tree = lcp(tree)
        time += 1
    return time


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


def poly_multiply(left: list[int], right: list[int], cutoff: int) -> list[int]:
    answer = [0] * (cutoff + 1)
    for i, x in enumerate(left):
        if x == 0:
            continue
        for j, y in enumerate(right[: cutoff + 1 - i]):
            answer[i + j] += x * y
    return answer


def poly_power(base: list[int], exponent: int, cutoff: int) -> list[int]:
    answer = [1] + [0] * cutoff
    for _ in range(exponent):
        answer = poly_multiply(answer, base, cutoff)
    return answer


@cache
def lcp_inverse_series(target: tuple, time: int, cutoff: int) -> tuple[int, ...]:
    tree_series = [0] + [catalan(n - 1) for n in range(1, cutoff + 1)]
    if not target:
        body = [0] * (cutoff + 1)
        power = [1] + [0] * cutoff
        for exponent in range(time + 1):
            if exponent:
                power = poly_multiply(power, tree_series, cutoff)
            body = [x + y for x, y in zip(body, power)]
    else:
        body = poly_power(tree_series, time, cutoff)
        for child in target:
            body = poly_multiply(
                body, list(lcp_inverse_series(child, time, cutoff)), cutoff
            )
    return tuple([0] + body[:cutoff])


def internal_vertices(tree: tuple) -> int:
    return bool(tree) + sum(internal_vertices(child) for child in tree)


def audit_lcp() -> tuple[list[int], list[int], list[int]]:
    states: list[int] = []
    images: list[int] = []
    maxima: list[int] = []
    all_sources: list[tuple] = []
    for n in range(1, 11):
        layer = plane_trees(n)
        all_sources.extend(layer)
        states.append(len(layer))
        image_set = set()
        layer_tails = []
        for tree in layer:
            image_set.add(lcp(tree))
            A.check(tree_size(lcp(tree)) <= n)
            A.check(lcp_tail(tree) == sibling_bottleneck(tree), tree)
            for time in range(5):
                A.check(
                    lcp_power_literal(tree, time)
                    == lcp_coordinate_formula(tree, time),
                    (tree, time),
                )
            layer_tails.append(lcp_tail(tree))
        images.append(len(image_set))
        maxima.append(max(layer_tails))
        A.check(maxima[-1] == n - 1, (n, maxima[-1]))

    cutoff = 9
    sources = [tree for n in range(1, cutoff + 1) for tree in plane_trees(n)]
    targets = [tree for n in range(1, 5) for tree in plane_trees(n)]
    for time in range(1, 4):
        for target in targets:
            observed = Counter(
                tree_size(source)
                for source in sources
                if lcp_power_literal(source, time) == target
            )
            formula = lcp_inverse_series(target, time, cutoff)
            minimum = tree_size(target) + time * internal_vertices(target)
            for n in range(1, cutoff + 1):
                A.check(observed[n] == formula[n], (time, target, n))
                A.check((formula[n] > 0) == (n >= minimum), (time, target, n))
    A.check(states == [catalan(n - 1) for n in range(1, 11)])
    return states, images, maxima


# ---------------------------------------------------------------------------
# PAE: retain position/value parity agreements and standardize.


def pae(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return standardize(
        value
        for position, value in enumerate(permutation, 1)
        if (position - value) % 2 == 0
    )


@cache
def pae_tail(permutation: tuple[int, ...]) -> int:
    image = pae(permutation)
    return 0 if image == permutation else 1 + pae_tail(image)


def embedding_length(colors: tuple[int, ...]) -> int:
    if not colors:
        return 0
    return (
        len(colors)
        + sum(left == right for left, right in zip(colors, colors[1:]))
        + (colors[0] == 0)
    )


def embedding_count(host_rank: int, colors: tuple[int, ...]) -> int:
    minimum = embedding_length(colors)
    if host_rank < minimum:
        return 0
    return comb(len(colors) + (host_rank - minimum) // 2, len(colors))


@cache
def pae_optimal_color(target: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    m = len(target)
    if m == 0:
        return 0, ()
    inverse = [0] * m
    for position, value in enumerate(target):
        inverse[value - 1] = position
    best_key = None
    best_color = None
    for odd_positions in combinations(range(m), (m + 1) // 2):
        odd_set = set(odd_positions)
        color = tuple(int(i in odd_set) for i in range(m))
        value_color = tuple(color[inverse[j]] for j in range(m))
        raw = max(embedding_length(color), embedding_length(value_color))
        rank = m + 2 * ((raw - m + 1) // 2)
        key = (rank, color)
        if best_key is None or key < best_key:
            best_key, best_color = key, color
    assert best_key is not None and best_color is not None
    return best_key[0], best_color


def pae_fibre_formula(host_rank: int, target: tuple[int, ...]) -> int:
    m = len(target)
    if host_rank < m or (host_rank - m) % 2:
        return 0
    if m == 0:
        return factorial(host_rank // 2) ** 2
    inverse = [0] * m
    for position, value in enumerate(target):
        inverse[value - 1] = position
    total = 0
    for odd_positions in combinations(range(m), (m + 1) // 2):
        odd_set = set(odd_positions)
        color = tuple(int(i in odd_set) for i in range(m))
        value_color = tuple(color[inverse[j]] for j in range(m))
        total += embedding_count(host_rank, color) * embedding_count(
            host_rank, value_color
        )
    return total * factorial((host_rank - m) // 2) ** 2


def greedy_embedding(colors: tuple[int, ...]) -> tuple[int, ...]:
    if not colors:
        return ()
    answer = [1 if colors[0] else 2]
    for left, right in zip(colors, colors[1:]):
        answer.append(answer[-1] + (1 if left != right else 2))
    return tuple(answer)


def pae_section(target: tuple[int, ...], host_rank: int) -> tuple[int, ...]:
    m = len(target)
    minimum, color = pae_optimal_color(target)
    if host_rank < minimum or (host_rank - m) % 2:
        raise ValueError("inadmissible host rank")
    if m == 0:
        return tuple(
            value
            for pair in ((2 * i, 2 * i - 1) for i in range(1, host_rank // 2 + 1))
            for value in pair
        )
    inverse = [0] * m
    for position, value in enumerate(target):
        inverse[value - 1] = position
    value_color = tuple(color[inverse[j]] for j in range(m))
    selected_positions = greedy_embedding(color)
    selected_values = greedy_embedding(value_color)
    A.check(max(selected_positions) <= host_rank)
    A.check(max(selected_values) <= host_rank)
    permutation = [0] * host_rank
    for i, position in enumerate(selected_positions):
        permutation[position - 1] = selected_values[target[i] - 1]
    remaining_positions = [i for i in range(1, host_rank + 1) if permutation[i - 1] == 0]
    selected_value_set = set(selected_values)
    remaining_values = [i for i in range(1, host_rank + 1) if i not in selected_value_set]
    odd_positions = [i for i in remaining_positions if i % 2]
    even_positions = [i for i in remaining_positions if not i % 2]
    odd_values = [i for i in remaining_values if i % 2]
    even_values = [i for i in remaining_values if not i % 2]
    A.check(len(odd_positions) == len(even_values))
    A.check(len(even_positions) == len(odd_values))
    for position, value in zip(odd_positions, even_values, strict=True):
        permutation[position - 1] = value
    for position, value in zip(even_positions, odd_values, strict=True):
        permutation[position - 1] = value
    return tuple(permutation)


@cache
def pae_witness(level: int) -> tuple[int, ...]:
    if level == 0:
        return ()
    if level == 1:
        return (2, 1)
    previous = pae_witness(level - 1)
    n = 2 * level
    answer = [0] * n
    if level % 2 == 0:
        retained_values = [v for v in range(1, n + 1) if v not in (n - 3, n)]
        for position, rank in enumerate(previous, 1):
            answer[position - 1] = retained_values[rank - 1]
        answer[n - 2], answer[n - 1] = n, n - 3
    else:
        retained_positions = list(range(1, n - 3)) + [n - 2, n - 1]
        for position, rank in zip(retained_positions, previous, strict=True):
            answer[position - 1] = rank
        answer[n - 4], answer[n - 1] = n, n - 1
    return tuple(answer)


def audit_pae() -> tuple[list[int], list[int], list[dict[int, int]]]:
    maxima: list[int] = []
    fixed_counts: list[int] = []
    literal: dict[int, Counter[tuple[int, ...]]] = {}
    for n in range(9):
        fibres: Counter[tuple[int, ...]] = Counter()
        tails = []
        fixed = 0
        for source in permutations(range(1, n + 1)):
            image = pae(source)
            fibres[image] += 1
            tails.append(pae_tail(source))
            A.check((n - len(image)) % 2 == 0)
            if image == source:
                fixed += 1
                A.check(all((i - v) % 2 == 0 for i, v in enumerate(source, 1)))
            else:
                A.check(len(image) <= n - 2)
        literal[n] = fibres
        maxima.append(max(tails, default=0))
        fixed_counts.append(fixed)
        A.check(maxima[-1] == n // 2)
        A.check(fixed == factorial((n + 1) // 2) * factorial(n // 2))

    threshold_profiles: list[dict[int, int]] = []
    for m in range(9):
        profile: Counter[int] = Counter()
        for target in permutations(range(1, m + 1)):
            minimum, _ = pae_optimal_color(target)
            profile[minimum - m] += 1
            for n in range(m, 9, 2):
                observed = literal[n][target]
                formula = pae_fibre_formula(n, target)
                A.check(observed == formula, (n, target, observed, formula))
                A.check((observed > 0) == (n >= minimum), (n, target, minimum))
            if m <= 7:
                for n in (minimum, minimum + 2):
                    section = pae_section(target, n)
                    A.check(sorted(section) == list(range(1, n + 1)))
                    A.check(pae(section) == target, (target, n, section))
        threshold_profiles.append(dict(sorted(profile.items())))

    previous = ()
    for level in range(1, 31):
        witness = pae_witness(level)
        A.check(sorted(witness) == list(range(1, 2 * level + 1)))
        A.check(pae(witness) == previous, (level, witness))
        A.check(pae_tail(witness) == level)
        odd_witness = (1,) + tuple(value + 1 for value in witness)
        expected = (1,) + tuple(value + 1 for value in previous)
        A.check(pae(odd_witness) == expected)
        A.check(pae_tail(odd_witness) == level)
        previous = witness
    return maxima, fixed_counts, threshold_profiles


def main() -> None:
    lcp_states, lcp_images, lcp_maxima = audit_lcp()
    pae_maxima, pae_fixed, pae_thresholds = audit_pae()
    print("FOCUSED_COLLISION_GATE_COUNTEREXAMPLE_VERIFIER v1")
    print(f"LCP states n=1..10: {lcp_states}")
    print(f"LCP one-step images n=1..10: {lcp_images}")
    print(f"LCP max tails n=1..10: {lcp_maxima}")
    print(f"PAE max tails n=0..8: {pae_maxima}")
    print(f"PAE fixed counts n=0..8: {pae_fixed}")
    print(f"PAE target-rank excess profiles m=0..8: {pae_thresholds}")
    print("LCP theorem contract: PASS exact-coordinate/inverse falsifier")
    print("PAE theorem contract: PASS exact-threshold/closed-fibre/tower falsifier")
    print(f"ASSERTIONS {A.assertions}")
    print("PASS")


if __name__ == "__main__":
    main()
