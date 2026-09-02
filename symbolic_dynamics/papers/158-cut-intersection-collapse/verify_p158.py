#!/usr/bin/env python3
"""Exact finite falsification for P158 cut-intersection collapse.

The script enumerates every vertex-history assignment in the frozen parameter
window and, independently, every labelled simple graph.  For each history it
first performs the successive cut intersections and compares their result
with a separately coded complement-word graph.  It then checks the empty-state
count, complete image classification, and fibre formula for every target.
Enumeration is evidence against small counterexamples, not a proof premise.
"""

from __future__ import annotations

from collections import Counter, deque
from functools import cache
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def avoidance_count(pair_count: int, vertex_count: int) -> int:
    """Assignments to antipodal pairs with no pair occupied on both sides."""
    return sum(
        (-1) ** (pair_count - used)
        * comb(pair_count, used)
        * (2**used)
        * (used**vertex_count)
        for used in range(pair_count + 1)
    )


def falling(value: int, length: int) -> int:
    answer = 1
    for offset in range(length):
        answer *= value - offset
    return answer


@cache
def component_family_count(vertex_count: int, component_count: int) -> int:
    """Labelled unions of exactly r nontrivial complete bipartite components."""
    if vertex_count == 0:
        return int(component_count == 0)
    if component_count == 0:
        return 0
    total = 0
    for size in range(2, vertex_count + 1):
        bipartitions = (1 << (size - 1)) - 1
        total += (
            comb(vertex_count - 1, size - 1)
            * bipartitions
            * component_family_count(vertex_count - size, component_count - 1)
        )
    return total


def image_count_formula(vertex_count: int, pair_count: int) -> int:
    """Independent labelled-species count with isolate boundary enforced."""
    total = 0
    for isolate_count in range(vertex_count + 1):
        remaining = vertex_count - isolate_count
        component_cap = pair_count if isolate_count == 0 else pair_count - 1
        for component_count in range(max(0, component_cap) + 1):
            total += (
                comb(vertex_count, isolate_count)
                * component_family_count(remaining, component_count)
            )
    return total


def edge_table(vertex_count: int) -> list[tuple[int, int]]:
    return [
        (left, right)
        for left in range(vertex_count)
        for right in range(left + 1, vertex_count)
    ]


def graph_mask(words: tuple[int, ...], time: int) -> int:
    """Graph whose edges join complementary length-time history words."""
    complement_mask = (1 << time) - 1
    mask = 0
    for bit, (left, right) in enumerate(edge_table(len(words))):
        if words[left] ^ words[right] == complement_mask:
            mask |= 1 << bit
    return mask


def literal_intersection_mask(words: tuple[int, ...], time: int) -> int:
    """Start from K_n and intersect the literal cut masks epoch by epoch."""
    edges = edge_table(len(words))
    surviving = (1 << len(edges)) - 1
    for epoch in range(time):
        cut = 0
        for bit, (left, right) in enumerate(edges):
            left_bit = (words[left] >> epoch) & 1
            right_bit = (words[right] >> epoch) & 1
            if left_bit != right_bit:
                cut |= 1 << bit
        surviving &= cut
    return surviving


def classify_target(vertex_count: int, mask: int) -> tuple[bool, int, int]:
    """Recognize isolates plus nontrivial complete bipartite components."""
    edges = edge_table(vertex_count)
    adjacency = [set() for _ in range(vertex_count)]
    for bit, (left, right) in enumerate(edges):
        if mask & (1 << bit):
            adjacency[left].add(right)
            adjacency[right].add(left)

    isolates = sum(not neighbours for neighbours in adjacency)
    seen: set[int] = set()
    nontrivial_components = 0

    for root in range(vertex_count):
        if root in seen or not adjacency[root]:
            continue
        colour = {root: 0}
        queue = deque([root])
        seen.add(root)
        component: list[int] = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbour in adjacency[current]:
                if neighbour not in colour:
                    colour[neighbour] = 1 - colour[current]
                    seen.add(neighbour)
                    queue.append(neighbour)
                elif colour[neighbour] == colour[current]:
                    return False, 0, isolates

        left = [vertex for vertex in component if colour[vertex] == 0]
        right = [vertex for vertex in component if colour[vertex] == 1]
        if not left or not right:
            return False, 0, isolates
        for first_index, first in enumerate(component):
            for second in component[first_index + 1 :]:
                has_edge = second in adjacency[first]
                should_have_edge = colour[first] != colour[second]
                if has_edge != should_have_edge:
                    return False, 0, isolates
        nontrivial_components += 1

    return True, nontrivial_components, isolates


def predicted_fibre(vertex_count: int, time: int, mask: int) -> int:
    valid, component_count, isolate_count = classify_target(vertex_count, mask)
    pair_count = 1 << (time - 1)
    if not valid or component_count > pair_count:
        return 0
    return (
        falling(pair_count, component_count)
        * (2**component_count)
        * avoidance_count(pair_count - component_count, isolate_count)
    )


def enumerate_case(vertex_count: int, time: int) -> tuple[int, int, int, int]:
    alphabet_size = 1 << time
    fibres: Counter[int] = Counter()
    for words in product(range(alphabet_size), repeat=vertex_count):
        compressed = graph_mask(words, time)
        literal = literal_intersection_mask(words, time)
        check(
            literal == compressed,
            f"literal/complement mismatch for n={vertex_count}, t={time}, words={words}",
        )
        fibres[compressed] += 1

    pair_count = 1 << (time - 1)
    edge_count = comb(vertex_count, 2)
    predicted_total = 0
    predicted_image = 0
    maximum_fibre = 0
    for mask in range(1 << edge_count):
        predicted = predicted_fibre(vertex_count, time, mask)
        observed = fibres.get(mask, 0)
        check(
            observed == predicted,
            f"target fibre mismatch for n={vertex_count}, t={time}, mask={mask}",
        )
        predicted_total += predicted
        predicted_image += predicted > 0
        maximum_fibre = max(maximum_fibre, predicted)

    history_count = alphabet_size**vertex_count
    check(predicted_total == history_count, "target fibres do not partition histories")
    check(sum(fibres.values()) == history_count, "enumeration lost histories")
    check(len(fibres) == predicted_image, "image-size classification mismatch")
    check(
        len(fibres) == image_count_formula(vertex_count, pair_count),
        "independent labelled image-count formula mismatch",
    )
    check(
        fibres[0] == avoidance_count(pair_count, vertex_count),
        "empty-state count mismatch",
    )
    total_edges = sum(
        mask.bit_count() * multiplicity for mask, multiplicity in fibres.items()
    )
    check(
        total_edges == edge_count * alphabet_size ** (vertex_count - 1),
        "first edge moment mismatch",
    )
    return history_count, len(fibres), fibres[0], maximum_fibre


def check_temporal_law() -> None:
    check(avoidance_count(0, 0) == 1, "A_0(0) boundary failed")
    for vertex_count in range(1, 10):
        check(avoidance_count(0, vertex_count) == 0, "A_0(n>0) boundary failed")
    for pair_count in range(1, 9):
        check(avoidance_count(pair_count, 0) == 1, "A_R(0) boundary failed")

    for vertex_count in range(2, 13):
        previous_numerator = 0
        previous_denominator = 1
        for time in range(1, 9):
            pair_count = 1 << (time - 1)
            denominator = (1 << time) ** vertex_count
            numerator = avoidance_count(pair_count, vertex_count)
            check(0 <= numerator <= denominator, "CDF outside [0,1]")
            check(
                numerator * previous_denominator
                >= previous_numerator * denominator,
                "absorption CDF is not monotone",
            )
            survival_numerator = denominator - numerator
            check(
                survival_numerator * (1 << time)
                <= comb(vertex_count, 2) * denominator,
                "union-bound tail failed",
            )
            previous_numerator = numerator
            previous_denominator = denominator


def main() -> None:
    check_temporal_law()
    cases = [(2, 1), (3, 1), (4, 2), (4, 3), (5, 2), (5, 3), (6, 2)]
    print("CIC_FOCUSED_EXACT_V1")
    print("BOUNDARY A_0(0)=1 A_0(n>0)=0 A_R(0)=1")
    for vertex_count, time in cases:
        histories, image_size, empty_fibre, maximum_fibre = enumerate_case(
            vertex_count, time
        )
        print(
            "CASE"
            f" n={vertex_count}"
            f" t={time}"
            f" histories={histories}"
            f" image={image_size}"
            f" empty={empty_fibre}"
            f" max_fibre={maximum_fibre}"
        )
    print("TARGET_CLASS isolates_plus_disjoint_nontrivial_complete_bipartites")
    print("FIBRE (R)_r*2^r*A_(R-r)(z)")
    print("IMAGE_EGF exp(x)*sum_(r<R)B(x)^r/r!+B(x)^R/R!")
    print("TEMPORAL P(T<=t)=A_(2^(t-1))(n)/2^(tn)")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
