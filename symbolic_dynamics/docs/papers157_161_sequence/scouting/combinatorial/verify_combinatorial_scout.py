#!/usr/bin/env python3
"""Deterministic breadth controls for the P157--P161 combinatorial scout.

The program intentionally mixes strong candidates with negative controls.
Its finite enumerations are counterexample pressure only: they do not prove
an all-parameter theorem, establish novelty, or authorize external release.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, permutations, product
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()


def standardize(values) -> tuple[int, ...]:
    values = tuple(values)
    ranks = {value: i + 1 for i, value in enumerate(sorted(values))}
    return tuple(ranks[value] for value in values)


def positive_compositions(n: int):
    if n == 0:
        yield ()
        return
    for mask in range(1 << (n - 1)):
        answer = []
        last = 0
        for i in range(n - 1):
            if mask & (1 << i):
                answer.append(i + 1 - last)
                last = i + 1
        answer.append(n - last)
        yield tuple(answer)


# ---------------------------------------------------------------------------
# LCP: delete the leftmost child subtree at every plane-tree vertex.


@cache
def plane_trees(n: int) -> tuple[tuple, ...]:
    if n == 1:
        return ((),)
    answer: list[tuple] = []
    for sizes in positive_compositions(n - 1):
        pools = [plane_trees(size) for size in sizes]

        def visit(i: int, prefix: list[tuple]) -> None:
            if i == len(pools):
                answer.append(tuple(prefix))
                return
            for tree in pools[i]:
                prefix.append(tree)
                visit(i + 1, prefix)
                prefix.pop()

        visit(0, [])
    return tuple(answer)


def tree_size(tree: tuple) -> int:
    return 1 + sum(tree_size(child) for child in tree)


def lcp(tree: tuple) -> tuple:
    if not tree:
        return ()
    return tuple(lcp(child) for child in tree[1:])


def lcp_iterate_formula(tree: tuple, time: int) -> tuple:
    return tuple(lcp_iterate_formula(child, time) for child in tree[time:])


@cache
def lcp_tail(tree: tuple) -> int:
    image = lcp(tree)
    return 0 if image == tree else 1 + lcp_tail(image)


def sibling_bottleneck(tree: tuple) -> int:
    answer = 0

    def visit(node: tuple, bottleneck: int) -> None:
        nonlocal answer
        for index, child in enumerate(node, 1):
            child_bottleneck = min(bottleneck, index)
            answer = max(answer, child_bottleneck)
            visit(child, child_bottleneck)

    visit(tree, 10**9)
    return answer


def poly_add(left: list[int], right: list[int]) -> list[int]:
    n = max(len(left), len(right))
    return [(left[i] if i < len(left) else 0) +
            (right[i] if i < len(right) else 0) for i in range(n)]


def poly_mul(left: list[int], right: list[int], cutoff: int) -> list[int]:
    answer = [0] * (cutoff + 1)
    for i, x in enumerate(left[:cutoff + 1]):
        if not x:
            continue
        for j, y in enumerate(right[:cutoff + 1 - i]):
            answer[i + j] += x * y
    return answer


def poly_shift(poly: list[int], amount: int, cutoff: int) -> list[int]:
    return [0] * amount + poly[:max(0, cutoff + 1 - amount)]


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


@cache
def lcp_preimage_poly(tree: tuple, time: int, cutoff: int) -> tuple[int, ...]:
    tree_series = [0] + [catalan(n - 1) for n in range(1, cutoff + 1)]
    powers = [[1] + [0] * cutoff]
    for _ in range(time):
        powers.append(poly_mul(powers[-1], tree_series, cutoff))
    if not tree:
        total = [0] * (cutoff + 1)
        for power in powers:
            total = poly_add(total, power)[:cutoff + 1]
        return tuple(poly_shift(total, 1, cutoff))
    answer = powers[time]
    for child in tree:
        answer = poly_mul(answer, list(lcp_preimage_poly(child, time, cutoff)), cutoff)
    return tuple(poly_shift(answer, 1, cutoff))


def audit_lcp() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts: list[int] = []
    image_counts: list[int] = []
    maxima: list[int] = []
    all_trees: list[tuple] = []
    for n in range(1, 11):
        trees = plane_trees(n)
        state_counts.append(len(trees))
        images = set()
        tails = []
        for tree in trees:
            all_trees.append(tree)
            image = lcp(tree)
            images.add(image)
            A.check(tree_size(image) <= n)
            A.check(lcp_tail(tree) == sibling_bottleneck(tree), tree)
            for time in range(5):
                iterate = tree
                for _ in range(time):
                    iterate = lcp(iterate)
                A.check(iterate == lcp_iterate_formula(tree, time), (tree, time))
            tails.append(lcp_tail(tree))
        image_counts.append(len(images))
        maxima.append(max(tails))
        A.check(maxima[-1] == n - 1)
    cutoff = 9
    brute: dict[tuple[int, tuple], Counter[int]] = {}
    sources = [tree for n in range(1, cutoff + 1) for tree in plane_trees(n)]
    targets = [tree for n in range(1, 5) for tree in plane_trees(n)]
    for time in range(1, 4):
        for target in targets:
            counts: Counter[int] = Counter()
            for source in sources:
                if lcp_iterate_formula(source, time) == target:
                    counts[tree_size(source)] += 1
            brute[(time, target)] = counts
            formula = lcp_preimage_poly(target, time, cutoff)
            for n in range(1, cutoff + 1):
                A.check(formula[n] == counts[n], (time, target, n, formula[n], counts[n]))
    return state_counts, image_counts, maxima


# ---------------------------------------------------------------------------
# PAE: retain entries whose position and value have the same parity.


def pae(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return standardize(value for position, value in enumerate(permutation, 1)
                       if (position - value) % 2 == 0)


@cache
def pae_tail(permutation: tuple[int, ...]) -> int:
    image = pae(permutation)
    return 0 if image == permutation else 1 + pae_tail(image)


def binary_embed_length(colors: tuple[int, ...]) -> int:
    if not colors:
        return 0
    answer = 1 if colors[0] == 1 else 2
    for left, right in zip(colors, colors[1:]):
        answer += 1 if left != right else 2
    return answer


@cache
def pae_minimum_rank(target: tuple[int, ...]) -> int:
    m = len(target)
    if m == 0:
        return 0
    inverse = [0] * m
    for position, value in enumerate(target):
        inverse[value - 1] = position
    best = 10**9
    for odd_positions in combinations(range(m), (m + 1) // 2):
        colors = [0] * m
        for position in odd_positions:
            colors[position] = 1
        colors_t = tuple(colors)
        value_colors = tuple(colors[inverse[value]] for value in range(m))
        excess = max(binary_embed_length(colors_t),
                     binary_embed_length(value_colors)) - m
        even_excess = 2 * ((excess + 1) // 2)
        best = min(best, m + even_excess)
    return best


def pae_fibre_formula(n: int, target: tuple[int, ...]) -> int:
    m = len(target)
    if n < m or (n - m) % 2:
        return 0
    answer = 0
    for positions in combinations(range(1, n + 1), m):
        for values in combinations(range(1, n + 1), m):
            if not all((positions[i] - values[target[i] - 1]) % 2 == 0
                       for i in range(m)):
                continue
            position_set = set(positions)
            value_set = set(values)
            missing_odd_positions = sum(i not in position_set and i % 2
                                        for i in range(1, n + 1))
            missing_even_positions = n - m - missing_odd_positions
            missing_odd_values = sum(i not in value_set and i % 2
                                     for i in range(1, n + 1))
            missing_even_values = n - m - missing_odd_values
            if (missing_odd_positions == missing_even_values and
                    missing_even_positions == missing_odd_values):
                answer += (factorial(missing_odd_positions) *
                           factorial(missing_even_positions))
    return answer


@cache
def pae_sharp_witness(level: int) -> tuple[int, ...]:
    """An explicit rank-2*level tower with one PAE step per level."""
    if level == 0:
        return ()
    if level == 1:
        return (2, 1)
    previous = pae_sharp_witness(level - 1)
    n = 2 * level
    answer: list[int | None] = [None] * n
    if level % 2 == 0:
        retained_values = [value for value in range(1, n + 1)
                           if value not in (n - 3, n)]
        for position, rank in enumerate(previous, 1):
            answer[position - 1] = retained_values[rank - 1]
        answer[n - 2] = n
        answer[n - 1] = n - 3
    else:
        retained_positions = list(range(1, n - 3)) + [n - 2, n - 1]
        retained_values = list(range(1, n - 1))
        for position, rank in zip(retained_positions, previous, strict=True):
            answer[position - 1] = retained_values[rank - 1]
        answer[n - 4] = n
        answer[n - 1] = n - 1
    return tuple(value for value in answer if value is not None)


def audit_pae() -> tuple[list[int], list[int], list[dict[int, int]], list[dict[int, int]]]:
    A.box()
    maxima: list[int] = []
    fixed_counts: list[int] = []
    image_profiles: list[dict[int, int]] = []
    mu_profiles: list[dict[int, int]] = []
    literal: dict[int, Counter[tuple[int, ...]]] = {}
    for n in range(0, 9):
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
                A.check(all((i - value) % 2 == 0 for i, value in enumerate(source, 1)))
            else:
                A.check(len(image) <= n - 2)
        literal[n] = fibres
        maxima.append(max(tails, default=0))
        fixed_counts.append(fixed)
        image_profiles.append(dict(sorted(Counter(map(len, fibres)).items())))
        A.check(maxima[-1] == n // 2)
        A.check(fixed == factorial((n + 1) // 2) * factorial(n // 2))
    for m in range(0, 9):
        profile: Counter[int] = Counter()
        for target in permutations(range(1, m + 1)):
            mu = pae_minimum_rank(target)
            profile[mu - m] += 1
            A.check(mu >= m and (mu - m) % 2 == 0)
            for n in range(m, 9, 2):
                observed = literal[n].get(target, 0)
                formula = pae_fibre_formula(n, target)
                A.check(observed == formula, (n, target, observed, formula))
                A.check((observed > 0) == (n >= mu), (n, target, mu))
        mu_profiles.append(dict(sorted(profile.items())))
    previous: tuple[int, ...] = ()
    for level in range(1, 31):
        even_witness = pae_sharp_witness(level)
        A.check(sorted(even_witness) == list(range(1, 2 * level + 1)))
        A.check(pae(even_witness) == previous, (level, even_witness, previous))
        A.check(pae_tail(even_witness) == level)
        odd_witness = (1,) + tuple(value + 1 for value in even_witness)
        expected_odd_image = (1,) + tuple(value + 1 for value in previous)
        A.check(pae(odd_witness) == expected_odd_image)
        A.check(pae_tail(odd_witness) == level)
        previous = even_witness
    return maxima, fixed_counts, image_profiles, mu_profiles


# ---------------------------------------------------------------------------
# CCQ: crossing-graph component quotient of a set partition.


def restricted_growth_words(n: int):
    if n == 0:
        yield ()
        return

    def visit(prefix: list[int], maximum: int):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from visit(prefix, max(maximum, value))
            prefix.pop()

    yield from visit([0], 0)


def rgs_blocks(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if not word:
        return ()
    answer: list[list[int]] = [[] for _ in range(max(word) + 1)]
    for position, block in enumerate(word, 1):
        answer[block].append(position)
    return tuple(tuple(block) for block in answer)


def blocks_cross(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    for ai, a in enumerate(left):
        for b in left[ai + 1:]:
            for ci, c in enumerate(right):
                for d in right[ci + 1:]:
                    if a < c < b < d or c < a < d < b:
                        return True
    return False


def crossing_component_quotient(word: tuple[int, ...]) -> tuple[int, ...]:
    blocks = rgs_blocks(word)
    m = len(blocks)
    parent = list(range(m))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    for i in range(m):
        for j in range(i):
            if blocks_cross(blocks[i], blocks[j]):
                x, y = find(i), find(j)
                if x != y:
                    parent[y] = x
    labels: dict[int, int] = {}
    answer = []
    for i in range(m):
        root = find(i)
        labels.setdefault(root, len(labels))
        answer.append(labels[root])
    return tuple(answer)


def is_noncrossing(word: tuple[int, ...]) -> bool:
    blocks = rgs_blocks(word)
    return all(not blocks_cross(blocks[i], blocks[j])
               for i in range(len(blocks)) for j in range(i))


def discrete_partition(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def audit_ccq() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts: list[int] = []
    image_counts: list[int] = []
    maxima: list[int] = []
    minimum_source: dict[tuple[int, ...], int] = {}
    for n in range(0, 11):
        images = set()
        tails = []
        states = 0
        for source in restricted_growth_words(n):
            states += 1
            image = crossing_component_quotient(source)
            images.add(image)
            minimum_source.setdefault(image, n)
            A.check(is_noncrossing(image), (source, image))
            second = crossing_component_quotient(image)
            A.check(second == discrete_partition(len(rgs_blocks(image))))
            expected_tail = (0 if source == discrete_partition(n) else
                             1 if is_noncrossing(source) else 2)
            actual_tail = 0
            iterate = source
            while True:
                next_iterate = crossing_component_quotient(iterate)
                if next_iterate == iterate:
                    break
                actual_tail += 1
                iterate = next_iterate
            A.check(actual_tail == expected_tail)
            tails.append(actual_tail)
        state_counts.append(states)
        image_counts.append(len(images))
        maxima.append(max(tails, default=0))
    for m in range(0, 6):
        for target in restricted_growth_words(m):
            if is_noncrossing(target):
                singleton_blocks = sum(len(block) == 1 for block in rgs_blocks(target))
                predicted = 2 * m - singleton_blocks
                A.check(minimum_source[target] == predicted,
                        (target, minimum_source[target], predicted))
            else:
                A.check(target not in minimum_source)
    return state_counts, image_counts, maxima


# ---------------------------------------------------------------------------
# ILP: parallel degree-at-most-one peeling in permutation inversion graphs.


def inversion_leaf_peel(permutation: tuple[int, ...]) -> tuple[int, ...]:
    n = len(permutation)
    degrees = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                degrees[i] += 1
                degrees[j] += 1
    return standardize(permutation[i] for i in range(n) if degrees[i] >= 2)


@cache
def ilp_tail(permutation: tuple[int, ...]) -> int:
    image = inversion_leaf_peel(permutation)
    return 0 if image == permutation else 1 + ilp_tail(image)


def audit_ilp() -> tuple[list[int], list[int], list[int]]:
    A.box()
    maxima, fixed_counts, image_counts = [], [], []
    for n in range(0, 9):
        tails, images, fixed = [], set(), 0
        for source in permutations(range(1, n + 1)):
            image = inversion_leaf_peel(source)
            images.add(image)
            tails.append(ilp_tail(source))
            if image == source:
                fixed += 1
            else:
                A.check(len(image) < n)
            A.check(inversion_leaf_peel(image) == image or len(inversion_leaf_peel(image)) < len(image))
        maxima.append(max(tails, default=0))
        fixed_counts.append(fixed)
        image_counts.append(len(images))
    return maxima, fixed_counts, image_counts


# ---------------------------------------------------------------------------
# DFC: delete all indegree-zero vertices of an endofunction.


def endofunction_core_step(function: tuple[int, ...]) -> tuple[int, ...]:
    n = len(function)
    indegree = [0] * n
    for image in function:
        indegree[image] += 1
    kept = [i for i in range(n) if indegree[i] > 0]
    labels = {old: new for new, old in enumerate(kept)}
    A.check(all(function[i] in labels for i in kept))
    return tuple(labels[function[i]] for i in kept)


@cache
def dfc_tail(function: tuple[int, ...]) -> int:
    image = endofunction_core_step(function)
    return 0 if image == function else 1 + dfc_tail(image)


def audit_dfc() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts, fixed_counts, maxima = [], [], []
    for n in range(0, 7):
        states = list(product(range(n), repeat=n)) if n else [()]
        state_counts.append(len(states))
        fixed = 0
        tails = []
        for source in states:
            image = endofunction_core_step(source)
            tails.append(dfc_tail(source))
            if image == source:
                fixed += 1
                A.check(sorted(source) == list(range(n)))
            else:
                A.check(len(image) < n)
        fixed_counts.append(fixed)
        maxima.append(max(tails, default=0))
        A.check(fixed == factorial(n))
    return state_counts, fixed_counts, maxima


# ---------------------------------------------------------------------------
# BGS: Bulgarian solitaire on integer partitions.


def integer_partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(maximum, n)
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def bulgarian(partition: tuple[int, ...]) -> tuple[int, ...]:
    if not partition:
        return ()
    return tuple(sorted(([part - 1 for part in partition if part > 1] +
                         [len(partition)]), reverse=True))


def orbit_tail_period(state, update) -> tuple[int, int]:
    seen = {}
    path = []
    while state not in seen:
        seen[state] = len(path)
        path.append(state)
        state = update(state)
    return seen[state], len(path) - seen[state]


def audit_bgs() -> tuple[list[int], list[int], list[list[int]]]:
    A.box()
    counts, maxima, periods = [], [], []
    for n in range(1, 21):
        states = list(integer_partitions(n))
        counts.append(len(states))
        info = [orbit_tail_period(state, bulgarian) for state in states]
        maxima.append(max(tail for tail, _ in info))
        periods.append(sorted(set(period for _, period in info)))
        A.check(all(sum(bulgarian(state)) == n for state in states))
    return counts, maxima, periods


# ---------------------------------------------------------------------------
# PPS: reverse every maximal descending run (pop-stack sorting).


def pop_stack(permutation: tuple[int, ...]) -> tuple[int, ...]:
    answer = []
    start = 0
    for i in range(1, len(permutation) + 1):
        if i == len(permutation) or permutation[i - 1] < permutation[i]:
            answer.extend(reversed(permutation[start:i]))
            start = i
    return tuple(answer)


@cache
def pps_tail(permutation: tuple[int, ...]) -> int:
    image = pop_stack(permutation)
    return 0 if image == permutation else 1 + pps_tail(image)


def audit_pps() -> tuple[list[int], list[int]]:
    A.box()
    maxima, image_counts = [], []
    for n in range(1, 9):
        tails, images = [], set()
        for source in permutations(range(1, n + 1)):
            image = pop_stack(source)
            tails.append(pps_tail(source))
            images.add(image)
            A.check(sorted(image) == list(range(1, n + 1)))
        maxima.append(max(tails))
        image_counts.append(len(images))
    return maxima, image_counts


# ---------------------------------------------------------------------------
# TSW: Conway's TopSwops prefix-reversal map.


def topswops(permutation: tuple[int, ...]) -> tuple[int, ...]:
    if not permutation or permutation[0] == 1:
        return permutation
    length = permutation[0]
    return tuple(reversed(permutation[:length])) + permutation[length:]


def topswops_tail(permutation: tuple[int, ...]) -> int:
    seen = set()
    steps = 0
    while permutation and permutation[0] != 1:
        A.check(permutation not in seen, ("TopSwops cycle", permutation))
        seen.add(permutation)
        permutation = topswops(permutation)
        steps += 1
    return steps


def audit_tsw() -> tuple[list[int], list[int]]:
    A.box()
    maxima, terminal_counts = [], []
    for n in range(1, 10):
        tails = []
        terminals = Counter()
        for source in permutations(range(1, n + 1)):
            tails.append(topswops_tail(source))
            target = source
            while target[0] != 1:
                target = topswops(target)
            terminals[target] += 1
        maxima.append(max(tails))
        terminal_counts.append(len(terminals))
        A.check(len(terminals) == factorial(n - 1))
    return maxima, terminal_counts


# ---------------------------------------------------------------------------
# CBB: cyclic nearest-empty box--ball matching on labeled binary cycles.


def cyclic_box_ball(word: tuple[int, ...]) -> tuple[int, ...]:
    remaining = list(range(len(word)))
    pairs: list[tuple[int, int]] = []
    while any(word[i] == 1 for i in remaining):
        adjacent = []
        for index, left in enumerate(remaining):
            right = remaining[(index + 1) % len(remaining)]
            if word[left] == 1 and word[right] == 0:
                adjacent.append((left, right))
        A.check(adjacent, ("unmatched cyclic balls", word, remaining))
        used = {value for pair in adjacent for value in pair}
        pairs.extend(adjacent)
        remaining = [value for value in remaining if value not in used]
    answer = [0] * len(word)
    for _, empty in pairs:
        answer[empty] = 1
    return tuple(answer)


def cycle_period(state, update) -> int:
    start = state
    period = 0
    while True:
        state = update(state)
        period += 1
        if state == start:
            return period
        A.check(period < 10000)


def audit_cbb() -> tuple[list[int], list[int]]:
    A.box()
    max_periods, carrier_counts = [], []
    for n in range(1, 13):
        states = [word for word in product((0, 1), repeat=n)
                  if sum(word) <= n // 2]
        carrier_counts.append(len(states))
        images = [cyclic_box_ball(word) for word in states]
        A.check(len(set(images)) == len(states))
        A.check(all(sum(source) == sum(image) for source, image in zip(states, images)))
        max_periods.append(max(cycle_period(word, cyclic_box_ball) for word in states))
    return carrier_counts, max_periods


# ---------------------------------------------------------------------------
# CSR: subtract the minimum part from a composition and delete zeros.


def composition_subtract_minimum(composition: tuple[int, ...]) -> tuple[int, ...]:
    if not composition:
        return ()
    minimum = min(composition)
    return tuple(part - minimum for part in composition if part > minimum)


@cache
def csr_tail(composition: tuple[int, ...]) -> int:
    if not composition:
        return 0
    return 1 + csr_tail(composition_subtract_minimum(composition))


def audit_csr() -> tuple[list[int], list[int]]:
    A.box()
    counts, maxima = [], []
    for n in range(1, 15):
        states = list(positive_compositions(n))
        counts.append(len(states))
        maxima.append(max(csr_tail(state) for state in states))
        A.check(all(sum(composition_subtract_minimum(state)) < n for state in states))
    return counts, maxima


# ---------------------------------------------------------------------------
# SSE: erase singleton blocks of a set partition.


def singleton_erase(word: tuple[int, ...]) -> tuple[int, ...]:
    counts = Counter(word)
    labels = {}
    answer = []
    for block in word:
        if counts[block] > 1:
            labels.setdefault(block, len(labels))
            answer.append(labels[block])
    return tuple(answer)


def audit_sse() -> tuple[list[int], list[int]]:
    A.box()
    fixed_counts, image_counts = [], []
    for n in range(0, 10):
        fixed, images = 0, set()
        for source in restricted_growth_words(n):
            image = singleton_erase(source)
            images.add(image)
            A.check(singleton_erase(image) == image)
            fixed += image == source
        fixed_counts.append(fixed)
        image_counts.append(len(images))
    return fixed_counts, image_counts


# ---------------------------------------------------------------------------
# CPE: retain all odd cycles of a permutation.


def odd_cycle_extract(permutation: tuple[int, ...]) -> tuple[int, ...]:
    n = len(permutation)
    seen = set()
    kept = set()
    for start in range(1, n + 1):
        if start in seen:
            continue
        cycle = []
        value = start
        while value not in seen:
            seen.add(value)
            cycle.append(value)
            value = permutation[value - 1]
        if len(cycle) % 2:
            kept.update(cycle)
    ordered = sorted(kept)
    labels = {old: new + 1 for new, old in enumerate(ordered)}
    return tuple(labels[permutation[old - 1]] for old in ordered)


def audit_cpe() -> tuple[list[int], list[int]]:
    A.box()
    fixed_counts, image_counts = [], []
    for n in range(0, 9):
        fixed, images = 0, set()
        for source in permutations(range(1, n + 1)):
            image = odd_cycle_extract(source)
            images.add(image)
            A.check(odd_cycle_extract(image) == image)
            fixed += image == source
        fixed_counts.append(fixed)
        image_counts.append(len(images))
    return fixed_counts, image_counts


# ---------------------------------------------------------------------------
# TUS: suppress every nonroot unary vertex of a plane tree.


def unary_suppress(tree: tuple) -> tuple:
    answer = []
    for child in tree:
        reduced = unary_suppress(child)
        while len(reduced) == 1:
            reduced = reduced[0]
        answer.append(reduced)
    return tuple(answer)


def audit_tus() -> tuple[list[int], list[int]]:
    A.box()
    fixed_counts, image_counts = [], []
    for n in range(1, 11):
        fixed, images = 0, set()
        for source in plane_trees(n):
            image = unary_suppress(source)
            images.add(image)
            A.check(unary_suppress(image) == image)
            fixed += image == source
        fixed_counts.append(fixed)
        image_counts.append(len(images))
    return fixed_counts, image_counts


# ---------------------------------------------------------------------------
# ASD: delete the second copy of the shortest, then leftmost, adjacent square.


def adjacent_square_delete(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    for half in range(1, n // 2 + 1):
        for start in range(0, n - 2 * half + 1):
            if word[start:start + half] == word[start + half:start + 2 * half]:
                return word[:start + half] + word[start + 2 * half:]
    return word


@cache
def asd_tail(word: tuple[int, ...]) -> int:
    image = adjacent_square_delete(word)
    return 0 if image == word else 1 + asd_tail(image)


def audit_asd() -> tuple[list[int], list[int]]:
    A.box()
    maxima, fixed_counts = [], []
    for n in range(0, 13):
        tails, fixed = [], 0
        for source in product((0, 1), repeat=n):
            image = adjacent_square_delete(source)
            tails.append(asd_tail(source))
            fixed += image == source
            if image != source:
                A.check(len(image) < n)
        maxima.append(max(tails, default=0))
        fixed_counts.append(fixed)
    return maxima, fixed_counts


# ---------------------------------------------------------------------------
# GQT: quotient a simple graph by equality of open neighborhoods.


def graph_pairs(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def graph_neighbors(n: int, code: int) -> list[int]:
    answer = [0] * n
    for bit, (i, j) in enumerate(graph_pairs(n)):
        if code & (1 << bit):
            answer[i] |= 1 << j
            answer[j] |= 1 << i
    return answer


def graph_twin_quotient(state: tuple[int, int]) -> tuple[int, int]:
    n, code = state
    neighbors = graph_neighbors(n, code)
    groups: dict[int, list[int]] = {}
    for vertex, row in enumerate(neighbors):
        groups.setdefault(row, []).append(vertex)
    classes = sorted(groups.values(), key=min)
    target_code = 0
    target_pairs = graph_pairs(len(classes))
    for bit, (i, j) in enumerate(target_pairs):
        if neighbors[classes[i][0]] & (1 << classes[j][0]):
            target_code |= 1 << bit
    return len(classes), target_code


def audit_gqt() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts, fixed_counts, image_counts = [], [], []
    for n in range(0, 7):
        states = [(n, code) for code in range(1 << comb(n, 2))]
        state_counts.append(len(states))
        fixed, images = 0, set()
        for state in states:
            image = graph_twin_quotient(state)
            images.add(image)
            A.check(graph_twin_quotient(image) == image)
            fixed += image == state
        fixed_counts.append(fixed)
        image_counts.append(len(images))
    return state_counts, fixed_counts, image_counts


# ---------------------------------------------------------------------------
# TSK: repeatedly strip the unique sink of a tournament.


def tournament_outdegrees(n: int, code: int) -> list[int]:
    answer = [0] * n
    for bit, (i, j) in enumerate(graph_pairs(n)):
        if code & (1 << bit):
            answer[i] += 1
        else:
            answer[j] += 1
    return answer


def induced_tournament(n: int, code: int, kept: list[int]) -> tuple[int, int]:
    edge = {}
    for bit, pair in enumerate(graph_pairs(n)):
        edge[pair] = bool(code & (1 << bit))
    answer = 0
    for bit, (i, j) in enumerate(graph_pairs(len(kept))):
        old_i, old_j = kept[i], kept[j]
        if edge[(old_i, old_j)]:
            answer |= 1 << bit
    return len(kept), answer


def tournament_sink_strip(state: tuple[int, int]) -> tuple[int, int]:
    n, code = state
    if n <= 1:
        return state
    sinks = [i for i, degree in enumerate(tournament_outdegrees(n, code)) if degree == 0]
    A.check(len(sinks) <= 1)
    if not sinks:
        return state
    return induced_tournament(n, code, [i for i in range(n) if i != sinks[0]])


@cache
def tsk_tail(state: tuple[int, int]) -> int:
    image = tournament_sink_strip(state)
    return 0 if image == state else 1 + tsk_tail(image)


def audit_tsk() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts, fixed_counts, maxima = [], [], []
    for n in range(0, 7):
        states = [(n, code) for code in range(1 << comb(n, 2))]
        state_counts.append(len(states))
        fixed, tails = 0, []
        for state in states:
            image = tournament_sink_strip(state)
            fixed += image == state
            tails.append(tsk_tail(state))
        fixed_counts.append(fixed)
        maxima.append(max(tails, default=0))
    return state_counts, fixed_counts, maxima


# ---------------------------------------------------------------------------
# PFD: delete the first preference 1 of a parking function, then decrement.


def is_parking_function(word: tuple[int, ...]) -> bool:
    return all(value <= index for index, value in enumerate(sorted(word), 1))


def parking_functions(n: int):
    if n == 0:
        yield ()
        return
    for word in product(range(1, n + 1), repeat=n):
        if is_parking_function(word):
            yield word


def parking_first_one_delete(word: tuple[int, ...]) -> tuple[int, ...]:
    if not word:
        return ()
    index = word.index(1)
    return tuple(max(1, value - 1) for i, value in enumerate(word) if i != index)


def audit_pfd() -> tuple[list[int], list[int], list[int]]:
    A.box()
    state_counts, image_counts, maxima = [], [], []
    for n in range(0, 7):
        states = list(parking_functions(n))
        state_counts.append(len(states))
        images = set()
        tails = []
        for source in states:
            image = parking_first_one_delete(source)
            images.add(image)
            A.check(is_parking_function(image))
            iterate = source
            steps = 0
            while iterate:
                iterate = parking_first_one_delete(iterate)
                steps += 1
            A.check(steps == n)
            tails.append(steps)
        image_counts.append(len(images))
        maxima.append(max(tails, default=0))
        expected = 1 if n == 0 else (n + 1) ** (n - 1)
        A.check(len(states) == expected)
    return state_counts, image_counts, maxima


# ---------------------------------------------------------------------------
# WBS: one leftmost 10 -> 01 bubble move on binary words.


def word_bubble(word: tuple[int, ...]) -> tuple[int, ...]:
    answer = list(word)
    for i in range(len(word) - 1):
        if word[i:i + 2] == (1, 0):
            answer[i], answer[i + 1] = 0, 1
            return tuple(answer)
    return word


def word_inversions(word: tuple[int, ...]) -> int:
    return sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))


@cache
def wbs_tail(word: tuple[int, ...]) -> int:
    image = word_bubble(word)
    return 0 if image == word else 1 + wbs_tail(image)


def audit_wbs() -> tuple[list[int], list[int]]:
    A.box()
    maxima, fixed_counts = [], []
    for n in range(0, 15):
        tails, fixed = [], 0
        for source in product((0, 1), repeat=n):
            tail = wbs_tail(source)
            A.check(tail == word_inversions(source))
            tails.append(tail)
            fixed += word_bubble(source) == source
        maxima.append(max(tails, default=0))
        fixed_counts.append(fixed)
        A.check(fixed == n + 1)
        A.check(maxima[-1] == (n // 2) * ((n + 1) // 2))
    return maxima, fixed_counts


def main() -> None:
    lcp_states, lcp_images, lcp_max = audit_lcp()
    pae_max, pae_fixed, pae_images, pae_mu = audit_pae()
    ccq_states, ccq_images, ccq_max = audit_ccq()
    ilp_max, ilp_fixed, ilp_images = audit_ilp()
    dfc_states, dfc_fixed, dfc_max = audit_dfc()
    bgs_counts, bgs_max, bgs_periods = audit_bgs()
    pps_max, pps_images = audit_pps()
    tsw_max, tsw_terminals = audit_tsw()
    cbb_counts, cbb_periods = audit_cbb()
    csr_counts, csr_max = audit_csr()
    sse_fixed, sse_images = audit_sse()
    cpe_fixed, cpe_images = audit_cpe()
    tus_fixed, tus_images = audit_tus()
    asd_max, asd_fixed = audit_asd()
    gqt_states, gqt_fixed, gqt_images = audit_gqt()
    tsk_states, tsk_fixed, tsk_max = audit_tsk()
    pfd_states, pfd_images, pfd_max = audit_pfd()
    wbs_max, wbs_fixed = audit_wbs()

    print("P157_P161_COMBINATORIAL_BREADTH_EXACT_CONTROL")
    print("external_status=HOLD_EXTERNAL")
    print("systems=18")
    print(f"LCP_states_n1_10={lcp_states}")
    print(f"LCP_image_counts_n1_10={lcp_images}")
    print(f"LCP_max_tail_n1_10={lcp_max}")
    print(f"PAE_max_tail_n0_8={pae_max}")
    print("PAE_constructive_tower_even_rank2_60=PASS")
    print(f"PAE_fixed_counts_n0_8={pae_fixed}")
    print(f"PAE_image_rank_profiles_n0_8={pae_images}")
    print(f"PAE_mu_excess_profiles_m0_8={pae_mu}")
    print(f"CCQ_states_n0_10={ccq_states}")
    print(f"CCQ_image_counts_n0_10={ccq_images}")
    print(f"CCQ_max_tail_n0_10={ccq_max}")
    print(f"ILP_max_tail_n0_8={ilp_max}")
    print(f"ILP_fixed_counts_n0_8={ilp_fixed}")
    print(f"ILP_image_counts_n0_8={ilp_images}")
    print(f"DFC_states_n0_6={dfc_states}")
    print(f"DFC_fixed_counts_n0_6={dfc_fixed}")
    print(f"DFC_max_tail_n0_6={dfc_max}")
    print(f"BGS_partition_counts_n1_20={bgs_counts}")
    print(f"BGS_max_tail_n1_20={bgs_max}")
    print(f"BGS_cycle_period_sets_n1_20={bgs_periods}")
    print(f"PPS_max_passes_n1_8={pps_max}")
    print(f"PPS_image_counts_n1_8={pps_images}")
    print(f"TSW_max_steps_n1_9={tsw_max}")
    print(f"TSW_terminal_counts_n1_9={tsw_terminals}")
    print(f"CBB_carrier_counts_n1_12={cbb_counts}")
    print(f"CBB_max_period_n1_12={cbb_periods}")
    print(f"CSR_state_counts_n1_14={csr_counts}")
    print(f"CSR_max_tail_n1_14={csr_max}")
    print(f"SSE_fixed_counts_n0_9={sse_fixed}")
    print(f"SSE_image_counts_n0_9={sse_images}")
    print(f"CPE_fixed_counts_n0_8={cpe_fixed}")
    print(f"CPE_image_counts_n0_8={cpe_images}")
    print(f"TUS_fixed_counts_n1_10={tus_fixed}")
    print(f"TUS_image_counts_n1_10={tus_images}")
    print(f"ASD_max_tail_n0_12={asd_max}")
    print(f"ASD_fixed_counts_n0_12={asd_fixed}")
    print(f"GQT_states_n0_6={gqt_states}")
    print(f"GQT_fixed_counts_n0_6={gqt_fixed}")
    print(f"GQT_image_counts_n0_6={gqt_images}")
    print(f"TSK_states_n0_6={tsk_states}")
    print(f"TSK_fixed_counts_n0_6={tsk_fixed}")
    print(f"TSK_max_tail_n0_6={tsk_max}")
    print(f"PFD_states_n0_6={pfd_states}")
    print(f"PFD_image_counts_n0_6={pfd_images}")
    print(f"PFD_max_tail_n0_6={pfd_max}")
    print(f"WBS_max_tail_n0_14={wbs_max}")
    print(f"WBS_fixed_counts_n0_14={wbs_fixed}")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY")
    print("owner_nonhit_role=NOT_NOVELTY_EVIDENCE")
    print("status=PASS")


if __name__ == "__main__":
    main()
