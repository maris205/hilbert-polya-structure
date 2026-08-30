#!/usr/bin/env python3
"""Exact reverse-delete pilot on complete graphs.

At each state choose uniformly among edges whose deletion preserves
connectivity.  This is the embedded deletion chain of reverse-delete with a
uniform random strict edge order.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def double_factorial_odd(k):
    out = 1
    for value in range(1, k + 1, 2):
        out *= value
    return out


def model(n):
    edges = tuple(combinations(range(n), 2))
    full = (1 << len(edges)) - 1

    @lru_cache(None)
    def connected(mask):
        adjacency = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                adjacency[u].append(v)
                adjacency[v].append(u)
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == n

    @lru_cache(None)
    def deletable(mask):
        return tuple(
            i
            for i in range(len(edges))
            if mask >> i & 1 and connected(mask ^ (1 << i))
        )

    @lru_cache(None)
    def law(mask):
        active = deletable(mask)
        if not active:
            return ((mask, Fraction(1)),)
        out = defaultdict(Fraction)
        for i in active:
            for tree, probability in law(mask ^ (1 << i)):
                out[tree] += probability / len(active)
        return tuple(sorted(out.items()))

    return edges, full, connected, deletable, law


def degrees(n, edges, mask):
    result = [0] * n
    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            result[u] += 1
            result[v] += 1
    return tuple(sorted(result))


def fixed_tree_probability(n, target_edges):
    edges, full, connected, deletable, _ = model(n)
    index = {edge: i for i, edge in enumerate(edges)}
    target = sum(1 << index[tuple(sorted(edge))] for edge in target_edges)

    @lru_cache(None)
    def probability(mask):
        if mask == target:
            return Fraction(1)
        active = deletable(mask)
        if not active:
            return Fraction(0)
        total = Fraction(0)
        for i in active:
            if target >> i & 1:
                continue
            total += probability(mask ^ (1 << i))
        return total / len(active)

    return probability(full)


def permutation_law(n):
    edges, full, connected, _, _ = model(n)
    counts = Counter()
    for order in permutations(range(len(edges))):
        mask = full
        for i in order:
            if mask >> i & 1 and connected(mask ^ (1 << i)):
                mask ^= 1 << i
        counts[mask] += 1
    denominator = 1
    for i in range(2, len(edges) + 1):
        denominator *= i
    return tuple(sorted((tree, Fraction(count, denominator)) for tree, count in counts.items()))


def main():
    snapshots = {}
    for n in (3, 4, 5):
        edges, full, connected, deletable, law = model(n)
        distribution = law(full)
        check(sum(probability for _, probability in distribution) == 1)
        check(len(distribution) == n ** (n - 2))
        for tree, probability in distribution:
            check(probability > 0)
            check(connected(tree))
            check(tree.bit_count() == n - 1)
            check(not deletable(tree))
        shape = defaultdict(Fraction)
        for tree, probability in distribution:
            shape[degrees(n, edges, tree)] += probability
        snapshots[n] = dict(sorted(shape.items()))

    edges4, full4, _, _, law4 = model(4)
    check(law4(full4) == permutation_law(4))
    check(
        snapshots[4]
        == {(1, 1, 1, 3): Fraction(4, 15), (1, 1, 2, 2): Fraction(11, 15)}
    )
    check(
        snapshots[5]
        == {
            (1, 1, 1, 1, 4): Fraction(1, 21),
            (1, 1, 1, 2, 3): Fraction(127, 252),
            (1, 1, 2, 2, 2): Fraction(113, 252),
        }
    )

    star_probabilities = []
    for n in range(2, 8):
        star = tuple((0, v) for v in range(1, n))
        probability = fixed_tree_probability(n, star)
        predicted = Fraction(1, double_factorial_odd(2 * n - 3))
        check(probability == predicted)
        star_probabilities.append(probability)

    print("random reverse-delete pilot: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("complete-graph full laws: K_3, K_4, K_5")
    print("independent random-edge-order replay: K_4 (6! orders)")
    print("fixed-star formula checked: 2 <= n <= 7")
    print("P_K4(star/path): 4/15,11/15")
    print("P_K5(star/T/path): 1/21,127/252,113/252")
    print("fixed labeled star probabilities: " + ",".join(map(str, star_probabilities)))


if __name__ == "__main__":
    main()
