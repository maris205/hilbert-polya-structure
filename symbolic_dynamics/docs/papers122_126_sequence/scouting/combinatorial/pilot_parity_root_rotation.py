#!/usr/bin/env python3
"""Exact scout for parity-guided root rotations of plane full binary trees."""

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


LEAF = None


@lru_cache(None)
def trees(n):
    if n == 0:
        return (LEAF,)
    answer = []
    for left_size in range(n):
        right_size = n - 1 - left_size
        for left in trees(left_size):
            for right in trees(right_size):
                answer.append((left, right))
    return tuple(answer)


@lru_cache(None)
def size(tree):
    if tree is LEAF:
        return 0
    return 1 + size(tree[0]) + size(tree[1])


def phi(tree):
    if tree is LEAF:
        return tree
    left, right = tree
    if size(left) % 2 == 0:
        if right is LEAF:
            return tree
        middle, outer = right
        return ((left, middle), outer)
    if left is LEAF:
        return tree
    outer, middle = left
    return (outer, (middle, right))


def fixed_criterion(tree):
    if tree is LEAF:
        return True
    left, right = tree
    return size(left) % 2 == 0 and right is LEAF


def recurrent_criterion(tree):
    if fixed_criterion(tree):
        return True
    left, right = tree
    if size(left) % 2 == 0:
        return right is not LEAF and size(right[0]) % 2 == 0
    return left is not LEAF and size(left[0]) % 2 == 0


def orbit_data(tree):
    seen = {}
    state = tree
    while state not in seen:
        seen[state] = len(seen)
        state = phi(state)
    return seen[state], len(seen) - seen[state]


def catalan(n):
    values = [1]
    for m in range(1, n + 1):
        values.append(sum(values[i] * values[m - 1 - i] for i in range(m)))
    return values


def convolution(a, b, degree):
    answer = [0] * (degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= degree:
                answer[i + j] += ai * bj
    return answer


EXPECTED_RECURRENT = [1, 1, 2, 4, 12, 32, 108, 320, 1144, 3584, 13260, 43008, 162792]


def main():
    maximum_n = 12
    catalans = catalan(maximum_n)
    even_catalans = [catalans[n] if n % 2 == 0 else 0 for n in range(maximum_n + 1)]
    ee = convolution(even_catalans, even_catalans, maximum_n)
    eec = convolution(ee, catalans, maximum_n)
    predicted_recurrent = [0] * (maximum_n + 1)
    predicted_recurrent[0] = 1
    for n in range(1, maximum_n + 1):
        predicted_recurrent[n] = even_catalans[n - 1]
        if n >= 2:
            predicted_recurrent[n] += 2 * eec[n - 2]
    check(predicted_recurrent == EXPECTED_RECURRENT, "recurrent OGF coefficients")

    rows = []
    for n in range(maximum_n + 1):
        universe = trees(n)
        universe_set = set(universe)
        fixed = 0
        recurrent = 0
        depths = Counter()
        periods = Counter()
        indegrees = Counter()
        for tree in universe:
            image = phi(tree)
            indegrees[image] += 1
            check(size(image) == n, (n, "size"))
            check(image in universe_set, (n, "closure"))
            depth, period = orbit_data(tree)
            check(period <= 2, (n, tree, "period", period))
            check(depth <= max(0, (n - 1) // 2), (n, tree, "depth", depth))
            is_fixed = image == tree
            is_recurrent = phi(image) == tree
            check(is_fixed == fixed_criterion(tree), (n, tree, "fixed criterion"))
            check(is_recurrent == recurrent_criterion(tree), (n, tree, "recurrent criterion"))
            fixed += is_fixed
            recurrent += is_recurrent
            depths[depth] += 1
            periods[period] += 1
        expected_fixed = 1 if n == 0 else (catalans[n - 1] if n % 2 else 0)
        check(fixed == expected_fixed, (n, "fixed count", fixed))
        check(recurrent == predicted_recurrent[n], (n, "recurrent count", recurrent))
        check(max(indegrees.values()) <= 2, (n, "indegree", max(indegrees.values())))
        expected_depth = 0 if n == 0 else (n - 1) // 2
        check(max(depths) == expected_depth, (n, "sharp depth", max(depths)))
        check((recurrent - fixed) % 2 == 0, (n, "two-cycle points"))
        rows.append(
            (
                n,
                len(universe),
                fixed,
                recurrent,
                dict(sorted(depths.items())),
                dict(sorted(periods.items())),
                max(indegrees.values()),
            )
        )

    print("parity-guided root rotation: exhaustive full-binary-tree census")
    print("n states fixed recurrent depth_hist period_hist max_indegree")
    for row in rows:
        print(*row)
    print("recurrent_OGF_coefficients", predicted_recurrent)
    print("ASSERTIONS", ASSERTIONS)


if __name__ == "__main__":
    main()
