#!/usr/bin/env python3
"""Exact theorem-interface replay for P146; standard library only."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


ASSERTIONS = 0


def check(value, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(message)


def catalan(index):
    return comb(2 * index, index) // (index + 1)


def endpoint(n, deletion_order):
    current = list(range(n))
    diagonals = set()
    for vertex in deletion_order:
        position = current.index(vertex)
        left = current[position - 1]
        right = current[(position + 1) % len(current)]
        diagonals.add(tuple(sorted((left, right))))
        current.pop(position)
    return tuple(sorted(diagonals)), tuple(sorted(current))


def faces(n, diagonals):
    graph_edges = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    graph_edges.update(diagonals)
    return tuple(
        triple for triple in combinations(range(n), 3)
        if all(tuple(sorted(pair)) in graph_edges for pair in combinations(triple, 2))
    )


def weak_dual(face_list):
    adjacency = [[] for _ in face_list]
    for i, j in combinations(range(len(face_list)), 2):
        if len(set(face_list[i]) & set(face_list[j])) == 2:
            adjacency[i].append(j)
            adjacency[j].append(i)
    return adjacency


def hook_count(adjacency, root):
    parent = {root: None}
    order = [root]
    for vertex in order:
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                order.append(neighbor)
    size = [1] * len(adjacency)
    for vertex in reversed(order[1:]):
        size[parent[vertex]] += size[vertex]
    denominator = 1
    for vertex in range(len(adjacency)):
        if vertex != root:
            denominator *= size[vertex]
    return factorial(len(adjacency) - 1) // denominator


def connected(adjacency):
    if not adjacency:
        return True
    seen = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return len(seen) == len(adjacency)


def leaf_order_count(adjacency):
    """Count unrooted leaf deletions until one survivor, independently."""
    masks = tuple(sum(1 << neighbor for neighbor in neighbors)
                  for neighbors in adjacency)

    @lru_cache(None)
    def count(alive):
        if alive.bit_count() == 1:
            return 1
        return sum(
            count(alive ^ (1 << vertex))
            for vertex in range(len(masks))
            if alive >> vertex & 1
            and (masks[vertex] & alive).bit_count() == 1
        )

    return count((1 << len(masks)) - 1)


def brute_root_orders(adjacency, root):
    """Enumerate child-before-parent permutations; bounded to small trees."""
    parent = {root: None}
    queue = [root]
    for vertex in queue:
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)
    nonroot = tuple(vertex for vertex in range(len(adjacency))
                    if vertex != root)
    answer = 0
    for order in permutations(nonroot):
        position = {vertex: index for index, vertex in enumerate(order)}
        if all(
            parent[vertex] == root
            or position[vertex] < position[parent[vertex]]
            for vertex in nonroot
        ):
            answer += 1
    return answer


def verify(n):
    endpoint_count = Counter()
    marked_count = Counter()
    for order in permutations(range(n), n - 3):
        triangulation, final_face = endpoint(n, order)
        endpoint_count[triangulation] += 1
        marked_count[(triangulation, final_face)] += 1

    histories = factorial(n) // 6
    check(sum(endpoint_count.values()) == histories, (n, "history mass"))
    check(len(endpoint_count) == catalan(n - 2), (n, "Catalan endpoints"))

    path_dual_count = 0
    for triangulation, observed in endpoint_count.items():
        face_list = faces(n, triangulation)
        adjacency = weak_dual(face_list)
        check(len(face_list) == n - 2, (n, triangulation, "faces"))
        check(connected(adjacency), (n, triangulation, "dual connected"))
        check(sum(map(len, adjacency)) == 2 * (len(adjacency) - 1),
              (n, triangulation, "dual tree"))
        hook_sum = 0
        for root, face in enumerate(face_list):
            predicted = hook_count(adjacency, root)
            hook_sum += predicted
            check(marked_count[(triangulation, tuple(sorted(face)))] == predicted,
                  (n, triangulation, face, "marked hook"))
            if len(adjacency) <= 6:
                check(brute_root_orders(adjacency, root) == predicted,
                      (n, triangulation, root, "root-order enumeration"))
        check(observed == hook_sum, (n, triangulation, "hook sum"))
        check(leaf_order_count(adjacency) == hook_sum,
              (n, triangulation, "leaf recurrence versus hooks"))
        check(leaf_order_count(adjacency) == observed,
              (n, triangulation, "leaf recurrence versus histories"))

        is_path = max(map(len, adjacency), default=0) <= 2
        check((observed == 2 ** (n - 3)) == is_path,
              (n, triangulation, observed, "sharp equality"))
        path_dual_count += is_path

    probability_mass = sum(Fraction(6 * count, factorial(n))
                           for count in endpoint_count.values())
    check(probability_mass == 1, (n, "probability mass"))
    check(min(endpoint_count.values()) == 2 ** (n - 3), (n, "minimum"))
    return (histories, len(endpoint_count), min(endpoint_count.values()),
            max(endpoint_count.values()), path_dual_count)


def main():
    print("P146 EXACT CONTROL")
    print("columns=n,histories,triangulations,min_H,max_H,path_dual_equalities")
    for n in range(3, 10):
        result = verify(n)
        print(n, *result, sep=",")
    print(f"assertions={ASSERTIONS}")
    print("P146_THEOREM_INTERFACES_PASS")


if __name__ == "__main__":
    main()
