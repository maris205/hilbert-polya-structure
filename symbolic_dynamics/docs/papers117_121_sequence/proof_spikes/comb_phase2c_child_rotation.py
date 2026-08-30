#!/usr/bin/env python3
"""Exact pilot for simultaneous child-list rotation on labelled plane trees.

A state is a plane rooted tree on labels {0,...,n-1}, rooted at 0.  At every
nonleaf vertex, simultaneously move the first child to the end of that
vertex's child list.  The script checks the local-LCM period theorem by
literal iteration and the fixed-point EGF recurrence by an independent
coefficient computation.
"""

from functools import lru_cache
from itertools import permutations
from math import factorial, gcd


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def forests(order):
    """All ordered forests with a total of ``order`` unlabelled vertices."""
    if order == 0:
        return ((),)
    answer = []
    for first_order in range(1, order + 1):
        for first in shapes(first_order):
            for rest in forests(order - first_order):
                answer.append((first,) + rest)
    return tuple(answer)


@lru_cache(maxsize=None)
def shapes(order):
    """Plane rooted tree shapes, represented by their child tuples."""
    if order < 1:
        return ()
    return forests(order - 1)


def label_shape(shape, labels):
    """Label nonroot vertices in preorder; the root always receives label 0."""
    iterator = iter(labels)

    def visit(node_shape, is_root=False):
        label = 0 if is_root else next(iterator)
        return (label, tuple(visit(child) for child in node_shape))

    tree = visit(shape, True)
    try:
        next(iterator)
    except StopIteration:
        return tree
    raise AssertionError("unused label")


def rotate(tree):
    """One simultaneous update."""
    label, children = tree
    changed = tuple(rotate(child) for child in children)
    if changed:
        changed = changed[1:] + changed[:1]
    return (label, changed)


def iterate(tree, steps):
    for _ in range(steps):
        tree = rotate(tree)
    return tree


def lcm(a, b):
    return a // gcd(a, b) * b


def local_period(tree):
    answer = 1
    stack = [tree]
    while stack:
        _, children = stack.pop()
        if children:
            answer = lcm(answer, len(children))
            stack.extend(children)
    return answer


def edge_set(tree):
    edges = set()
    stack = [tree]
    while stack:
        parent, children = stack.pop()
        for child in children:
            edges.add((parent, child[0]))
            stack.append(child)
    return frozenset(edges)


def convolution(left, right, cutoff):
    answer = [0] * (cutoff + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: cutoff + 1 - i]):
            if b:
                answer[i + j] += a * b
    return answer


def restricted_shape_counts(cutoff, time):
    """Coefficients of T=x*sum_{d=0 or d|time} T^d."""
    allowed = [0] + [d for d in range(1, cutoff) if time % d == 0]
    coefficients = [0] * (cutoff + 1)
    coefficients[1] = 1
    for order in range(2, cutoff + 1):
        total = 0
        base = coefficients[:]
        for degree in allowed:
            if degree == 0:
                continue
            power = [0] * (cutoff + 1)
            power[0] = 1
            for _ in range(degree):
                power = convolution(power, base, cutoff)
            total += power[order - 1]
        coefficients[order] = total
    return coefficients


def integer_partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def landau(total):
    best = 1
    for partition in integer_partitions(total):
        value = 1
        for part in partition:
            value = lcm(value, part)
        best = max(best, value)
    return best


def main():
    max_order = 7
    literal_fixed = {
        time: [0] * (max_order + 1) for time in range(1, 13)
    }
    totals = [0] * (max_order + 1)
    maxima = [0] * (max_order + 1)

    for order in range(1, max_order + 1):
        for shape in shapes(order):
            for labels in permutations(range(1, order)):
                tree = label_shape(shape, labels)
                totals[order] += 1
                image = rotate(tree)
                check(edge_set(image) == edge_set(tree), "parent relation changed")
                period = local_period(tree)
                maxima[order] = max(maxima[order], period)
                check(iterate(tree, period) == tree, "LCM is not a return time")
                for time in range(1, period):
                    check(iterate(tree, time) != tree, "LCM is not minimal")
                for time in range(1, 13):
                    is_fixed = iterate(tree, time) == tree
                    check(is_fixed == (time % period == 0))
                    literal_fixed[time][order] += int(is_fixed)

        catalan = len(shapes(order))
        check(totals[order] == catalan * factorial(order - 1))
        check(maxima[order] == landau(order - 1))

    for time in range(1, 13):
        recurrence = restricted_shape_counts(max_order, time)
        for order in range(1, max_order + 1):
            expected = recurrence[order] * factorial(order - 1)
            check(literal_fixed[time][order] == expected)

    # First superlinear period: degrees 4 and 3 use seven edges on eight nodes.
    witness = (
        0,
        (
            (1, ((5, ()), (6, ()), (7, ()))),
            (2, ()),
            (3, ()),
            (4, ()),
        ),
    )
    check(local_period(witness) == 12)
    check(iterate(witness, 12) == witness)
    check(all(iterate(witness, time) != witness for time in range(1, 12)))
    check(12 > 8)  # falsifies the tempting period <= number-of-vertices guess

    print("comb_phase2c_child_rotation: PASS")
    print(f"assertions={ASSERTIONS}")
    print("exact_orders=1..7")
    print("state_counts=" + ",".join(map(str, totals[1:])))
    print("max_periods=" + ",".join(map(str, maxima[1:])))
    print("first_superlinear_witness=n8_period12_degrees4,3")
    print("theorem=pointwise_period_lcm_outdegrees;global_max=Landau(n-1)")
    print("fixed_egf=T_t(x)=x*(1+sum_{d|t}T_t(x)^d)")


if __name__ == "__main__":
    main()
