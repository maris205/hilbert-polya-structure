#!/usr/bin/env python3
"""Exact theorem-interface falsifier for P148; standard library only.

Finite enumeration is counterexample pressure, not a proof of the
all-parameter statements in the manuscript.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


Tree = tuple["Tree", ...]
Address = tuple[int, ...]
LabelledTree = tuple[Address, tuple["LabelledTree", ...]]


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


@lru_cache(maxsize=None)
def positive_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    answer = []
    for first in range(1, total + 1):
        for rest in positive_compositions(total - first):
            answer.append((first,) + rest)
    return tuple(answer)


@lru_cache(maxsize=None)
def plane_trees(vertices: int) -> tuple[Tree, ...]:
    check(vertices >= 1, (vertices, "positive tree size"))
    if vertices == 1:
        return ((),)
    answer = []
    for sizes in positive_compositions(vertices - 1):
        for children in product(*(plane_trees(size) for size in sizes)):
            answer.append(tuple(children))
    return tuple(answer)


@lru_cache(maxsize=None)
def tree_size(tree: Tree) -> int:
    return 1 + sum(tree_size(child) for child in tree)


@lru_cache(maxsize=None)
def tree_height(tree: Tree) -> int:
    return 0 if not tree else 1 + max(tree_height(child) for child in tree)


@lru_cache(maxsize=None)
def internal_vertices(tree: Tree) -> int:
    return int(bool(tree)) + sum(internal_vertices(child) for child in tree)


@lru_cache(maxsize=None)
def contract(tree: Tree) -> Tree:
    return tuple(
        contract(grandchild)
        for child in tree
        for grandchild in child
    )


def tail(tree: Tree) -> int:
    steps = 0
    while tree:
        tree = contract(tree)
        steps += 1
    return steps


def path_tree(vertices: int) -> Tree:
    tree: Tree = ()
    for _ in range(vertices - 1):
        tree = (tree,)
    return tree


def label_tree(tree: Tree, address: Address = ()) -> LabelledTree:
    return (
        address,
        tuple(
            label_tree(child, address + (index,))
            for index, child in enumerate(tree)
        ),
    )


def contract_labelled(tree: LabelledTree) -> LabelledTree:
    label, children = tree
    return (
        label,
        tuple(
            contract_labelled(grandchild)
            for child in children
            for grandchild in child[1]
        ),
    )


def descendants_at_depth(
    tree: Tree, depth: int, address: Address
) -> tuple[tuple[Tree, Address], ...]:
    if depth == 0:
        return ((tree, address),)
    answer = []
    for index, child in enumerate(tree):
        answer.extend(descendants_at_depth(child, depth - 1, address + (index,)))
    return tuple(answer)


def divisibility_skeleton(
    tree: Tree, spacing: int, address: Address = ()
) -> LabelledTree:
    children = tuple(
        divisibility_skeleton(subtree, spacing, descendant_address)
        for subtree, descendant_address in descendants_at_depth(tree, spacing, address)
    )
    return address, children


def fibre_count(source_size: int, target: Tree) -> int:
    m = tree_size(target)
    inserted = source_size - m
    required = internal_vertices(target)
    if inserted < required:
        return 0
    return comb(inserted - required + 2 * m - 2, 2 * m - 2)


def verify_local_factors(max_degree: int, max_inserted: int) -> None:
    # For d>0, sum_r C(d-1,r-1)y^r/(1-y)^(r+1)
    # must equal y/(1-y)^(d+1), coefficient by coefficient.
    for degree in range(1, max_degree + 1):
        for exponent in range(max_inserted + 1):
            lhs = sum(
                comb(degree - 1, productive - 1) * comb(exponent, productive)
                for productive in range(1, degree + 1)
                if exponent >= productive
            )
            rhs = 0 if exponent == 0 else comb(exponent - 1 + degree, degree)
            check(lhs == rhs, (degree, exponent, "local block-gap factor"))


def reciprocal_one_minus(series: list[int]) -> list[int]:
    answer = [0] * len(series)
    answer[0] = 1
    for degree in range(1, len(series)):
        answer[degree] = sum(
            series[index] * answer[degree - index]
            for index in range(1, degree + 1)
        )
    return answer


def algebraic_h_coefficients(bound: int) -> list[int]:
    # Coefficientwise solution of H=z+z^2 H/(1-H), H(0)=0.
    series = [0] * (bound + 1)
    if bound >= 1:
        series[1] = 1
    for degree in range(2, bound + 1):
        inverse = reciprocal_one_minus(series)
        wanted = degree - 2
        series[degree] = sum(
            series[index] * inverse[wanted - index]
            for index in range(wanted + 1)
        )
    return series


def main() -> None:
    print("P148 EXACT CONTROL")
    print("columns=n,states,image,fixed,max_tail,tail_profile")
    targets_by_size: list[Tree] = []
    image_counts = []
    for vertices in range(1, 12):
        states = plane_trees(vertices)
        check(len(states) == catalan(vertices - 1), (vertices, "Catalan carrier"))
        targets_by_size.extend(states)
        observed = Counter(contract(tree) for tree in states)
        tails = Counter()
        fixed = 0
        for tree in states:
            image = contract(tree)
            check(tree_size(image) <= vertices, (vertices, tree, "finite carrier closure"))
            check(tree_height(image) == tree_height(tree) // 2,
                  (vertices, tree, "height halving"))
            time = tail(tree)
            check(time == tree_height(tree).bit_length(),
                  (vertices, tree, "pointwise clock"))
            tails[time] += 1
            fixed += int(image == tree)

            labelled_iterate = label_tree(tree)
            for rank in range(time + 2):
                expected = divisibility_skeleton(tree, 1 << rank)
                check(labelled_iterate == expected,
                      (vertices, tree, rank, "divisible-depth iterate"))
                labelled_iterate = contract_labelled(labelled_iterate)

        expected_targets = {
            target
            for target in targets_by_size
            if tree_size(target) + internal_vertices(target) <= vertices
        }
        check(set(observed) == expected_targets, (vertices, "exact image condition"))
        for target in targets_by_size:
            check(observed.get(target, 0) == fibre_count(vertices, target),
                  (vertices, target, "every-target fibre"))
        maximum = (vertices - 1).bit_length()
        check(max(tails) == maximum, (vertices, "sharp clock"))
        check(tail(path_tree(vertices)) == maximum, (vertices, "path witness"))
        check(fixed == int(vertices == 1), (vertices, "unique fixed point"))
        image_counts.append(len(observed))
        profile = ";".join(f"{time}:{count}" for time, count in sorted(tails.items()))
        print(vertices, len(states), len(observed), fixed, max(tails), profile, sep=",")

    verify_local_factors(max_degree=10, max_inserted=11)

    bound = 11
    enumerated_h = [0] * (bound + 1)
    for target in targets_by_size:
        weight = tree_size(target) + internal_vertices(target)
        if weight <= bound:
            enumerated_h[weight] += 1
    formal_h = algebraic_h_coefficients(bound)
    check(enumerated_h == formal_h, "algebraic image series H")
    cumulative = [sum(formal_h[: degree + 1]) for degree in range(1, bound + 1)]
    check(cumulative == image_counts, "image series H/(1-z)")
    print("H_coefficients=" + ",".join(map(str, formal_h[1:])))
    print("image_counts=" + ",".join(map(str, image_counts)))
    print(f"assertions={ASSERTIONS}")
    print("P148_THEOREM_INTERFACES_PASS")


if __name__ == "__main__":
    main()
