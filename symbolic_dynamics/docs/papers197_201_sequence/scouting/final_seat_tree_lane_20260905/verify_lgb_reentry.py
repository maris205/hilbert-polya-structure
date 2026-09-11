#!/usr/bin/env python3
"""Bounded LGB re-entry audit; standalone, standard library, no old imports.

The forward carrier is a parent tuple, not the old Pruefer/edge-set code.
The inverse is generated from the compressed two-smallest-deep-leaf cases
without calling the forward rule as an admission test. Every source set is
then compared with the actual complete inverse. No novelty test is encoded.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial

ASSERTIONS = 0


def check(condition, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(context)


def tree_data(parent):
    n = len(parent)
    children = [[] for _ in parent]
    for v in range(1, n):
        children[parent[v]].append(v)
    depth = [0] * n
    for v in range(1, n):
        seen, u = set(), v
        while u:
            if u in seen:
                return None
            seen.add(u)
            u = parent[u]
        depth[v] = len(seen)
    leaves = [v for v in range(1, n) if not children[v]]
    deep = [v for v in leaves if depth[v] >= 2]
    return children, depth, leaves, deep


def all_trees(n):
    choices = [tuple(u for u in range(n) if u != v) for v in range(1, n)]
    for tail in product(*choices):
        parent = (0,) + tail
        if tree_data(parent) is not None:
            yield parent


def step(parent):
    deep = tree_data(parent)[3]
    if not deep:
        return parent
    v = deep[0]
    result = list(parent)
    result[v] = parent[parent[v]]
    return tuple(result)


def compressed_inverse(parent):
    children, depth, leaves, deep = tree_data(parent)
    result = set()
    pairs = []
    if not deep:
        result.add(parent)
        for v in leaves:
            pairs.extend((v, p) for p in children[0] if p != v)
    else:
        minimum = deep[0]
        for v in leaves:
            if v <= minimum:
                pairs.extend((v, p) for p in children[parent[v]] if p != v)
        if len(deep) >= 2 and parent[deep[0]] == parent[deep[1]]:
            pairs.append((deep[1], deep[0]))
    for v, p in pairs:
        source = list(parent)
        source[v] = p
        result.add(tuple(source))
    check(len(result) == len(pairs) + int(not deep), ("injective pairs", parent))
    return result


def compressed_size(parent):
    children, depth, leaves, deep = tree_data(parent)
    n = len(parent)
    if not deep:
        return 1 + (n - 1) * (n - 2)
    minimum = deep[0]
    root_leaf_count = sum(v < minimum and parent[v] == 0 for v in leaves)
    return (
        (len(children[0]) - 1) * root_leaf_count
        + len(children[parent[minimum]]) - 1
        + int(len(deep) >= 2 and parent[deep[0]] == parent[deep[1]])
    )


def image_criterion(parent):
    children, depth, leaves, deep = tree_data(parent)
    if not deep:
        return True
    minimum = deep[0]
    return len(children[parent[minimum]]) >= 2 or (
        len(children[0]) >= 2
        and any(v < minimum and parent[v] == 0 for v in leaves)
    )


def layer_polynomials(max_n):
    answer = {1: Counter({0: 1})}
    for n in range(2, max_n + 1):
        poly = Counter()
        for k in range(1, n):
            scale = comb(n - 2, k - 1) * k
            for a, x in answer[k].items():
                for b, y in answer[n - k].items():
                    poly[a + b + k - 1] += scale * x * y
        answer[n] = poly
    return answer


def rooted_shape(parent):
    children = tree_data(parent)[0]

    def shape(v):
        return "(" + "".join(sorted(shape(w) for w in children[v])) + ")"

    return shape(0)


def main():
    polynomials = layer_polynomials(7)
    total_states = 0
    first_label_example = None
    print("LGB_REENTRY_V1 / AUTHOR_SCOUT_ONLY / HOLD_EXTERNAL")
    for n in range(1, 8):
        states = tuple(all_trees(n))
        expected_states = 1 if n <= 2 else n ** (n - 2)
        check(len(states) == expected_states, ("Cayley carrier", n))
        total_states += len(states)
        transitions = {p: step(p) for p in states}
        predecessors = defaultdict(set)
        for source, target in transitions.items():
            check(target in transitions, ("closure", n, source))
            predecessors[target].add(source)
        tails, shape_examples = Counter(), {}
        maximum_fibre, maximizers = 0, []
        for parent in states:
            children, depth, leaves, deep = tree_data(parent)
            predicted = compressed_inverse(parent)
            actual = predecessors[parent]
            check(predicted == actual, ("complete inverse set", n, parent))
            check(len(actual) == compressed_size(parent), ("closed size", n, parent))
            check(bool(actual) == image_criterion(parent), ("image iff", n, parent))
            clock = sum(d - 1 for d in depth[1:])
            check((not deep) == (clock == 0), ("zero iff star", n, parent))
            if deep:
                next_depth = tree_data(transitions[parent])[1]
                check(sum(d - 1 for d in next_depth[1:]) == clock - 1,
                      ("unit descent", n, parent))
            visited, current = {}, parent
            while current not in visited:
                visited[current] = len(visited)
                current = transitions[current]
            tail, period = visited[current], len(visited) - visited[current]
            check(period == 1 and current == (0,) * n, ("recurrent star", n, parent))
            check(tail == clock, ("literal full orbit clock", n, parent))
            tails[tail] += 1
            if len(actual) > maximum_fibre:
                maximum_fibre, maximizers = len(actual), [parent]
            elif len(actual) == maximum_fibre:
                maximizers.append(parent)
            shape = rooted_shape(parent)
            if shape in shape_examples and first_label_example is None:
                old_parent, old_count = shape_examples[shape]
                if old_count != len(actual):
                    first_label_example = (n, old_parent, old_count, parent, len(actual))
            shape_examples[shape] = (parent, len(actual))
        maximum_tail = (n - 1) * (n - 2) // 2
        check(tails == polynomials[n], ("all clock layers", n))
        check(max(tails) == maximum_tail, ("sharp tail", n))
        check(tails[maximum_tail] == factorial(n - 1), ("all deepest paths", n))
        check(maximum_fibre == 1 + (n - 1) * (n - 2), ("sharp fibre", n))
        check(maximizers == [(0,) * n], ("all fibre maximizers", n))
        positive = sum(bool(predecessors[p]) for p in states)
        print(f"n={n} states={len(states)} image={positive} fixed=1 "
              f"max_tail={maximum_tail} deepest={tails[maximum_tail]} "
              f"max_fibre={maximum_fibre} maximizers=1")
        print("tail_hist=" + ",".join(f"{k}:{tails[k]}" for k in sorted(tails)))
    check(first_label_example is not None, "label-sensitive fibre witness")
    print("same_rooted_shape_different_fibres=" + repr(first_label_example))
    print(f"TOTAL_STATES={total_states}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("PASS_MATHEMATICS / RECOMMEND_KILL_VALUE_THIN / NO_PAPER_NUMBER")


if __name__ == "__main__":
    main()
