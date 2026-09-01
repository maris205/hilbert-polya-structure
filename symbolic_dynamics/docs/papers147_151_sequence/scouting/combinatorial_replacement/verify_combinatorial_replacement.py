#!/usr/bin/env python3
"""Exact falsifier for the P147--P151 combinatorial replacement scout.

Enumeration is deliberately bounded.  The all-parameter statements in the
accompanying note have separate proofs; this program tries to break their
literal maps, clocks, images, and target-resolved inverse formulae.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


def derangement_number(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for k in range(2, n + 1):
        a, b = b, (k - 1) * (a + b)
    return b


# ---------------------------------------------------------------------------
# Plane-tree utilities.  A tree is the tuple of its ordered child trees.


Tree = tuple["Tree", ...]


@lru_cache(maxsize=None)
def positive_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    result = []
    for first in range(1, total + 1):
        for suffix in positive_compositions(total - first):
            result.append((first,) + suffix)
    return tuple(result)


@lru_cache(maxsize=None)
def plane_trees(vertices: int) -> tuple[Tree, ...]:
    check(vertices >= 1, "positive plane-tree size")
    if vertices == 1:
        return ((),)
    result = []
    for sizes in positive_compositions(vertices - 1):
        for children in product(*(plane_trees(size) for size in sizes)):
            result.append(tuple(children))
    return tuple(result)


@lru_cache(maxsize=None)
def tree_size(tree: Tree) -> int:
    return 1 + sum(tree_size(child) for child in tree)


@lru_cache(maxsize=None)
def tree_height(tree: Tree) -> int:
    return 0 if not tree else 1 + max(tree_height(child) for child in tree)


@lru_cache(maxsize=None)
def internal_vertices(tree: Tree) -> int:
    return int(bool(tree)) + sum(internal_vertices(child) for child in tree)


def path_tree(vertices: int) -> Tree:
    tree: Tree = ()
    for _ in range(vertices - 1):
        tree = (tree,)
    return tree


def vertex_addresses(tree: Tree, prefix: tuple[int, ...] = ()):
    yield prefix
    for index, child in enumerate(tree):
        yield from vertex_addresses(child, prefix + (index,))


# ---------------------------------------------------------------------------
# ELC: even-level contraction of plane trees.


@lru_cache(maxsize=None)
def even_level_contract(tree: Tree) -> Tree:
    # The grandchildren become children, in contour order.  Recursion begins
    # again at every retained even-level grandchild.
    return tuple(
        even_level_contract(grandchild)
        for child in tree
        for grandchild in child
    )


def elc_tail(tree: Tree) -> int:
    steps = 0
    while tree:
        tree = even_level_contract(tree)
        steps += 1
    return steps


def elc_fibre_count(source_size: int, target: Tree) -> int:
    target_size = tree_size(target)
    inserted_odd = source_size - target_size
    required = internal_vertices(target)
    if inserted_odd < required:
        return 0
    # [y^(source_size-target_size)]
    # y^int(target)/(1-y)^(2|target|-1).
    return comb(
        inserted_odd - required + 2 * target_size - 2,
        2 * target_size - 2,
    )


def audit_elc() -> list[str]:
    lines = []
    targets_by_bound: list[Tree] = []
    for vertices in range(1, 12):
        states = plane_trees(vertices)
        check(len(states) == catalan(vertices - 1), "ELC Catalan carrier")
        targets_by_bound.extend(states)
        observed = Counter(even_level_contract(tree) for tree in states)
        tails = Counter()
        fixed = 0
        for tree in states:
            target = even_level_contract(tree)
            check(tree_size(target) <= tree_size(tree), "ELC carrier descent")
            check(tree_height(target) == tree_height(tree) // 2,
                  "ELC height-halving identity")
            tail = elc_tail(tree)
            check(tail == tree_height(tree).bit_length(),
                  "ELC pointwise height clock")
            endpoint = tree
            for _ in range(tail):
                endpoint = even_level_contract(endpoint)
            check(endpoint == (), "ELC singleton endpoint")
            tails[tail] += 1
            fixed += int(target == tree)
        for target in targets_by_bound:
            check(
                observed.get(target, 0) == elc_fibre_count(vertices, target),
                "ELC every-target size-refined fibre",
            )
        expected_image = sum(
            tree_size(target) + internal_vertices(target) <= vertices
            for target in targets_by_bound
        )
        check(len(observed) == expected_image, "ELC minimum-cost image test")
        expected_maximum = (vertices - 1).bit_length()
        check(max(tails) == expected_maximum, "ELC sharp logarithmic clock")
        witness = path_tree(vertices)
        check(elc_tail(witness) == expected_maximum, "ELC path witness")
        check(fixed == int(vertices == 1), "ELC fixed census")
        profile = ",".join(f"{tail}:{count}" for tail, count in sorted(tails.items()))
        lines.append(
            f"ELC n={vertices} states={len(states)} image={len(observed)} "
            f"fixed={fixed} max_tail={max(tails)} tails={profile}"
        )
    return lines


# ---------------------------------------------------------------------------
# PKE: standardized endpoint-peak extraction on permutations.


Permutation = tuple[int, ...]


def standardize(word: tuple[int, ...] | list[int]) -> Permutation:
    rank = {value: index + 1 for index, value in enumerate(sorted(word))}
    return tuple(rank[value] for value in word)


def peak_extract(state: Permutation) -> Permutation:
    if len(state) <= 1:
        return state
    peaks = []
    for index, value in enumerate(state):
        left = state[index - 1] if index else 0
        right = state[index + 1] if index + 1 < len(state) else 0
        if value > left and value > right:
            peaks.append(value)
    return standardize(peaks)


def peak_tail(state: Permutation) -> int:
    steps = 0
    while len(state) > 1:
        state = peak_extract(state)
        steps += 1
    return steps


def peak_lift(target: Permutation, source_size: int) -> Permutation:
    m = len(target)
    check(source_size >= 2 * m - 1, "PKE lift packing condition")
    if source_size == 1:
        return (1,)
    high = tuple(source_size - m + value for value in target)
    result = []
    for index, value in enumerate(high):
        result.append(value)
        if index + 1 < m:
            result.append(index + 1)
    # All unused low values form a decreasing terminal slope and hence create
    # no additional endpoint or interior peak.
    result.extend(range(source_size - m, m - 1, -1))
    return tuple(result)


@lru_cache(maxsize=None)
def deepest_peak_witness(size: int) -> Permutation:
    if size == 1:
        return (1,)
    target = deepest_peak_witness((size + 1) // 2)
    return peak_lift(target, size)


def peak_positions(comparisons: tuple[int, ...]) -> tuple[int, ...]:
    n = len(comparisons) + 1
    if n == 1:
        return (0,)
    result = []
    if comparisons[0] == 0:  # first entry is greater than the second
        result.append(0)
    for index in range(1, n - 1):
        if comparisons[index - 1] == 1 and comparisons[index] == 0:
            result.append(index)
    if comparisons[-1] == 1:
        result.append(n - 1)
    return tuple(result)


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
            if chosen & (1 << vertex):
                continue
            if predecessors[vertex] & ~chosen == 0:
                total += count(chosen | (1 << vertex))
        return total

    return count(0)


@lru_cache(maxsize=None)
def peak_target_fibre(source_size: int, target: Permutation) -> int:
    if source_size == 1:
        return int(target == (1,))
    total = 0
    for comparisons in product((0, 1), repeat=source_size - 1):
        peaks = peak_positions(comparisons)
        if len(peaks) != len(target):
            continue
        relations = []
        for index, comparison in enumerate(comparisons):
            if comparison:
                relations.append((index, index + 1))
            else:
                relations.append((index + 1, index))
        position_by_rank = [0] * len(target)
        for output_position, rank in enumerate(target):
            position_by_rank[rank - 1] = peaks[output_position]
        relations.extend(zip(position_by_rank, position_by_rank[1:]))
        total += linear_extensions(source_size, relations)
    return total


def peak_iterated_lift(target: Permutation, source_size: int, iterations: int) -> Permutation:
    check(iterations >= 1, "PKE positive inverse rank")
    state = target
    for _ in range(iterations - 1):
        state = peak_lift(state, 2 * len(state) - 1)
    return peak_lift(state, source_size)


def audit_pke() -> list[str]:
    lines = []
    for n in range(1, 10):
        states = permutations(range(1, n + 1))
        observed = Counter()
        tails = Counter()
        maximum_possible = (n - 1).bit_length()
        iterated_images = [set() for _ in range(maximum_possible + 1)]
        count = 0
        fixed = 0
        for state in states:
            count += 1
            target = peak_extract(state)
            observed[target] += 1
            iterate = state
            for rank in range(1, maximum_possible + 1):
                iterate = peak_extract(iterate)
                iterated_images[rank].add(iterate)
            tail = peak_tail(state)
            tails[tail] += 1
            check(len(target) <= (n + 1) // 2, "PKE peak packing bound")
            check(tail <= (n - 1).bit_length(), "PKE logarithmic upper clock")
            fixed += int(target == state)
        check(count == factorial(n), "PKE permutation census")
        expected_image = sum(factorial(m) for m in range(1, (n + 1) // 2 + 1))
        check(len(observed) == expected_image, "PKE full image theorem")
        for rank in range(1, maximum_possible + 1):
            bound = (n + (1 << rank) - 1) // (1 << rank)
            expected_rank_image = sum(factorial(m) for m in range(1, bound + 1))
            check(len(iterated_images[rank]) == expected_rank_image,
                  "PKE every-iterate image theorem")
            if n <= 8:
                for m in range(1, bound + 1):
                    for target in permutations(range(1, m + 1)):
                        section = peak_iterated_lift(target, n, rank)
                        iterate = section
                        for _ in range(rank):
                            iterate = peak_extract(iterate)
                        check(iterate == target, "PKE every-rank target section")
        check(max(tails) == (n - 1).bit_length(), "PKE sharp clock")
        witness = deepest_peak_witness(n)
        check(tuple(sorted(witness)) == tuple(range(1, n + 1)),
              "PKE lift is a permutation")
        check(peak_tail(witness) == (n - 1).bit_length(),
              "PKE recursive deepest witness")
        if n > 1:
            check(peak_extract(witness) == deepest_peak_witness((n + 1) // 2),
                  "PKE explicit section")
        check(fixed == int(n == 1), "PKE fixed census")
        if n <= 8:
            for target, multiplicity in observed.items():
                check(
                    multiplicity == peak_target_fibre(n, target),
                    "PKE every-target zigzag-poset fibre",
                )
                section = peak_lift(target, n)
                check(tuple(sorted(section)) == tuple(range(1, n + 1)),
                      "PKE every-target section is a permutation")
                check(peak_extract(section) == target,
                      "PKE every-target explicit section")
        profile = ",".join(f"{tail}:{value}" for tail, value in sorted(tails.items()))
        lines.append(
            f"PKE n={n} states={count} image={len(observed)} fixed={fixed} "
            f"max_tail={max(tails)} tails={profile}"
        )
    return lines


# ---------------------------------------------------------------------------
# FPD: delete the least fixed point of a permutation and standardize.


def fixed_points(state: Permutation) -> tuple[int, ...]:
    return tuple(index for index, value in enumerate(state, 1) if index == value)


def erase_least_fixed_point(state: Permutation) -> Permutation:
    points = fixed_points(state)
    if not points:
        return state
    removed = points[0]
    return tuple(
        value - int(value > removed)
        for index, value in enumerate(state, 1)
        if index != removed
    )


def fixed_point_endpoint(state: Permutation) -> tuple[Permutation, int]:
    steps = 0
    while fixed_points(state):
        state = erase_least_fixed_point(state)
        steps += 1
    return state, steps


def audit_fpd() -> list[str]:
    lines = []
    for n in range(0, 10):
        observed_image = set()
        basins = Counter()
        one_step = Counter()
        fixed = 0
        maximum = 0
        count = 0
        for state in permutations(range(1, n + 1)):
            count += 1
            target = erase_least_fixed_point(state)
            observed_image.add(target)
            if target != state:
                one_step[target] += 1
            endpoint, tail = fixed_point_endpoint(state)
            points = fixed_points(state)
            check(tail == len(points), "FPD fixed-point clock")
            check(not fixed_points(endpoint), "FPD derangement endpoint")
            basins[endpoint] += 1
            fixed += int(target == state)
            maximum = max(maximum, tail)
        check(count == factorial(n), "FPD permutation census")
        check(fixed == derangement_number(n), "FPD derangement fixed census")
        expected_image = 1 if n == 0 else derangement_number(n) + factorial(n - 1)
        check(len(observed_image) == expected_image, "FPD image census")
        check(maximum == n, "FPD sharp identity clock")
        for m in range(n + 1):
            for target in permutations(range(1, m + 1)):
                if fixed_points(target):
                    continue
                check(basins.get(target, 0) == comb(n, m),
                      "FPD every-derangement target basin")
        if n >= 1:
            for target in permutations(range(1, n)):
                points = fixed_points(target)
                predicted = points[0] if points else n
                check(one_step[target] == predicted, "FPD scheduled one-step fibre")
        lines.append(
            f"FPD n={n} states={count} image={len(observed_image)} "
            f"fixed={fixed} max_tail={maximum} basins={len(basins)}"
        )
    return lines


# ---------------------------------------------------------------------------
# APL: move a marked vertex to its parent in a fixed plane tree.


def ancestor_step(address: tuple[int, ...]) -> tuple[int, ...]:
    return address[:-1] if address else address


def audit_apl() -> list[str]:
    lines = []
    for n in range(1, 12):
        state_count = 0
        image_count = 0
        fixed = 0
        maximum = 0
        for tree in plane_trees(n):
            addresses = tuple(vertex_addresses(tree))
            check(len(addresses) == n, "APL pointed carrier census")
            image = {ancestor_step(address) for address in addresses}
            predicted_image = max(1, internal_vertices(tree))
            check(len(image) == predicted_image, "APL image marks")
            level_polynomial = Counter(map(len, addresses))
            for address in addresses:
                current = address
                steps = 0
                while current:
                    current = ancestor_step(current)
                    steps += 1
                check(steps == len(address), "APL depth clock")
                check(current == (), "APL root endpoint")
                maximum = max(maximum, steps)
                fixed += int(not address)
            check(sum(level_polynomial.values()) == n, "APL target basin polynomial")
            state_count += len(addresses)
            image_count += len(image)
        check(state_count == n * catalan(n - 1), "APL pointed Catalan census")
        check(fixed == catalan(n - 1), "APL root fixed census")
        check(maximum == n - 1, "APL sharp path clock")
        lines.append(
            f"APL n={n} states={state_count} image={image_count} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# CCS: successor of a marked corner in the contour of a plane tree.


def audit_ccs() -> list[str]:
    lines = []
    for n in range(1, 12):
        corners = 1 if n == 1 else 2 * (n - 1)
        state_count = 0
        fixed = 0
        periods = Counter()
        for _tree in plane_trees(n):
            for corner in range(corners):
                successor = (corner + 1) % corners
                predecessor = (successor - 1) % corners
                check(predecessor == corner, "CCS unique target inverse")
                current = corner
                period = 0
                while True:
                    current = (current + 1) % corners
                    period += 1
                    if current == corner:
                        break
                check(period == corners, "CCS full contour period")
                fixed += int(successor == corner)
                periods[period] += 1
                state_count += 1
        expected_states = corners * catalan(n - 1)
        check(state_count == expected_states, "CCS corner-pointed census")
        check(fixed == int(n == 1), "CCS fixed census")
        profile = ",".join(f"{period}:{count}" for period, count in sorted(periods.items()))
        lines.append(
            f"CCS n={n} states={state_count} image={state_count} "
            f"fixed={fixed} periods={profile}"
        )
    return lines


def main() -> None:
    print("P147-P151 COMBINATORIAL REPLACEMENT SCOUT")
    audits = (
        ("ELC_EVEN_LEVEL_CONTRACTION", audit_elc),
        ("PKE_PEAK_EXTRACTION", audit_pke),
        ("FPD_FIXED_POINT_DELETION", audit_fpd),
        ("APL_ANCESTOR_POINT_LIFT", audit_apl),
        ("CCS_CONTOUR_CORNER_SUCCESSOR", audit_ccs),
    )
    for name, audit in audits:
        print(f"[{name}]")
        for line in audit():
            print(line)
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
