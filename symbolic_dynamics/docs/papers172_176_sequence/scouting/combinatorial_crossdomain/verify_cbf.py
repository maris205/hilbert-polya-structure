#!/usr/bin/env python3
"""Independent exact verifier for Cartesian breadth-first dynamics."""

from __future__ import annotations

from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def literal_transform(word):
    """Build the min-Cartesian tree by a monotone stack, then read BFS."""
    n = len(word)
    if n == 0:
        return ()
    left = [-1] * n
    right = [-1] * n
    parent = [-1] * n
    stack = []
    for vertex, value in enumerate(word):
        last = -1
        while stack and word[stack[-1]] > value:
            last = stack.pop()
        if stack:
            right[stack[-1]] = vertex
            parent[vertex] = stack[-1]
        if last != -1:
            left[vertex] = last
            parent[last] = vertex
        stack.append(vertex)
    root = next(vertex for vertex in range(n) if parent[vertex] == -1)
    queue = deque([root])
    output = []
    while queue:
        vertex = queue.popleft()
        output.append(word[vertex])
        if left[vertex] != -1:
            queue.append(left[vertex])
        if right[vertex] != -1:
            queue.append(right[vertex])
    return tuple(output)


def identity_prefix(word):
    length = 0
    for expected, value in enumerate(word, 1):
        if value != expected:
            break
        length += 1
    return length


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def queue_dp_fibre(target):
    """Count compatible ordered binary shapes directly in BFS-slot order.

    A queue entry is the label of the parent that created the pending child
    slot.  A processed node creates zero, one-left, one-right, or two slots;
    hence the multiplicities 1,2,1 for zero, one, or two children.  The
    sentinel parent 0 supplies the root slot.  This routine neither builds a
    Cartesian tree nor inspects a possible source permutation.
    """
    queues = Counter({(0,): 1})
    for value in target:
        next_queues = Counter()
        for queue, multiplicity in queues.items():
            if not queue or queue[0] >= value:
                continue
            rest = queue[1:]
            for children, orientations in ((0, 1), (1, 2), (2, 1)):
                next_queues[rest + (value,) * children] += multiplicity * orientations
        queues = next_queues
    return queues.get((), 0)


# A tree is (label,left,right), with None for an empty child.  This generator
# does not inspect any source permutation or call literal_transform.
@lru_cache(maxsize=None)
def increasing_binary_trees(labels):
    labels = tuple(labels)
    if not labels:
        return (None,)
    root = min(labels)
    remaining = labels[1:]
    trees = []
    for left_size in range(len(remaining) + 1):
        for left_tuple in combinations(remaining, left_size):
            left_set = set(left_tuple)
            right_tuple = tuple(value for value in remaining if value not in left_set)
            for left in increasing_binary_trees(tuple(left_tuple)):
                for right in increasing_binary_trees(right_tuple):
                    trees.append((root, left, right))
    return tuple(trees)


def breadth_word(tree):
    if tree is None:
        return ()
    queue = deque([tree])
    output = []
    while queue:
        label, left, right = queue.popleft()
        output.append(label)
        if left is not None:
            queue.append(left)
        if right is not None:
            queue.append(right)
    return tuple(output)


def inorder_word(tree):
    if tree is None:
        return ()
    label, left, right = tree
    return inorder_word(left) + (label,) + inorder_word(right)


def audit_rank(n: int):
    states = tuple(permutations(range(1, n + 1)))
    identity = tuple(range(1, n + 1))
    literal_fibres = Counter()
    depths = Counter()
    maximum_depth = 0
    maximizers = []
    for source in states:
        target = literal_transform(source)
        check(tuple(sorted(target)) == identity, "literal closure")
        check(target <= source, "lexicographic nonincrease")
        check((target == source) == (source == identity), "unique fixed state")
        if source != identity:
            check(identity_prefix(target) >= identity_prefix(source) + 1, "prefix growth")
        literal_fibres[target] += 1
        point = source
        depth = 0
        while point != identity:
            point = literal_transform(point)
            depth += 1
            check(depth <= n - 1, "global height upper bound")
        depths[depth] += 1
        if depth > maximum_depth:
            maximum_depth = depth
            maximizers = [source]
        elif depth == maximum_depth:
            maximizers.append(source)

    independent_fibres = Counter()
    trees = increasing_binary_trees(identity)
    check(len(trees) == factorial(n), "increasing binary tree census")
    for tree in trees:
        target = breadth_word(tree)
        source = inorder_word(tree)
        check(tuple(sorted(target)) == identity, "independent target permutation")
        check(tuple(sorted(source)) == identity, "independent source permutation")
        # This is a cross-check after independent generation, not its source.
        check(literal_transform(source) == target, "tree/source bijection")
        independent_fibres[target] += 1
    check(literal_fibres == independent_fibres, "every-target fibre agreement")
    for target in states:
        check(literal_fibres.get(target, 0) == independent_fibres.get(target, 0), "codomain-wide fibre")
        # The queue DP is a third construction.  Run it codomain-wide through
        # rank seven, then on the complete nonzero image at larger ranks.
        if n <= 7 or literal_fibres.get(target, 0):
            check(queue_dp_fibre(target) == literal_fibres.get(target, 0), "BFS-slot DP fibre")

    check(max(literal_fibres.values()) == catalan(n), "Catalan maximum fibre")
    check(literal_fibres[identity] == catalan(n), "identity Catalan fibre")
    expected_height = 0 if n == 1 else n - 1
    check(maximum_depth == expected_height, "sharp height")
    witness = identity if n == 1 else (n,) + tuple(range(1, n))
    point = witness
    witness_depth = 0
    while point != identity:
        expected = tuple(range(1, witness_depth + 1)) + (n,) + tuple(range(witness_depth + 1, n))
        check(point == expected, "sharp witness orbit")
        point = literal_transform(point)
        witness_depth += 1
    check(witness_depth == expected_height, "sharp witness depth")

    print(
        f"n={n} states={len(states)} image={len(literal_fibres)} "
        f"height={maximum_depth} depth_layers={dict(sorted(depths.items()))} "
        f"max_fibre={max(literal_fibres.values())} maximizers={len(maximizers)}"
    )


def main() -> None:
    print("Cartesian breadth-first dynamics independent verifier")
    print("STATUS HOLD_EXTERNAL")
    for n in range(1, 10):
        audit_rank(n)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
