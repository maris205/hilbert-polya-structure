#!/usr/bin/env python3
"""Exact falsification controls for odd-subtree contraction on plane trees.

A plane rooted tree is represented recursively by the tuple of its ordered
children.  The literal update deletes every nonroot vertex whose *current*
rooted-subtree order is odd, simultaneously, and promotes its surviving
descendants to the nearest retained ancestor in plane order.  The root is
always retained.

The finite checks below are counterexample pressure.  They do not establish
ownership, novelty, or the quantified proofs recorded in the scout dossier.
"""

from collections import Counter
from functools import lru_cache
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def compositions(total, parts):
    if parts == 0:
        return ((),) if total == 0 else ()
    answer = []
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            answer.append((first,) + rest)
    return tuple(answer)


@lru_cache(maxsize=None)
def trees(order):
    """All plane rooted trees of an exact positive order."""
    if order == 1:
        return ((),)
    answer = []
    for degree in range(1, order):
        for child_orders in compositions(order - 1, degree):
            child_lists = tuple(trees(size) for size in child_orders)

            def extend(index, prefix):
                if index == degree:
                    answer.append(prefix)
                    return
                for child in child_lists[index]:
                    extend(index + 1, prefix + (child,))

            extend(0, ())
    return tuple(answer)


@lru_cache(maxsize=None)
def order(tree):
    return 1 + sum(order(child) for child in tree)


@lru_cache(maxsize=None)
def odd_contract(tree):
    """Apply the simultaneous literal update, retaining the outer root."""

    def retained_forest(node, force_root=False):
        children = []
        for child in node:
            children.extend(retained_forest(child, False))
        if force_root or order(node) % 2 == 0:
            return (tuple(children),)
        return tuple(children)

    result = retained_forest(tree, True)
    check(len(result) == 1, ("root lost", tree, result))
    return result[0]


def iterate(tree, time):
    for _ in range(time):
        tree = odd_contract(tree)
    return tree


@lru_cache(maxsize=None)
def depth(tree):
    nxt = odd_contract(tree)
    if nxt == tree:
        return 0
    return 1 + depth(nxt)


def path(order_value):
    tree = ()
    for _ in range(order_value - 1):
        tree = (tree,)
    return tree


def ceil_log2(n):
    if n <= 1:
        return 0
    return (n - 1).bit_length()


def c_constant(time):
    value = 1
    for level in range(1, time + 1):
        value *= (2**level - 1) ** (2 ** (time - level))
    return value


@lru_cache(maxsize=None)
def local_recurrence(time, degree):
    if time == 0:
        return 1
    return sum(
        (degree - k + 1)
        * local_recurrence(time - 1, degree - k + 1)
        * local_recurrence(time - 1, k)
        for k in range(degree + 1)
    )


def local_closed(time, degree):
    boundary = 2 ** (time + 1) - 2
    return c_constant(time) * comb(degree + boundary, boundary)


def extremal_fibre(time, target):
    value = c_constant(time) ** (order(target) - 1)

    def visit(node, is_root=False):
        nonlocal value
        if not is_root:
            value *= comb(
                len(node) + 2 ** (time + 1) - 2,
                2 ** (time + 1) - 2,
            )
        for child in node:
            visit(child, False)

    visit(target, True)
    return value


def aggregate_extremal(time, target_order):
    if target_order == 1:
        return 1
    return (
        c_constant(time) ** (target_order - 1)
        * comb(2 ** (time + 1) * (target_order - 1), target_order - 2)
        // (target_order - 1)
    )


def audit_catalan_and_literal(max_order=12):
    print("CATALAN n/states/image/fixed/max-depth/deepest")
    catalan = 1
    total_states = 0
    for n in range(1, max_order + 1):
        if n > 1:
            catalan = catalan * 2 * (2 * n - 3) // n
        layer = trees(n)
        check(len(layer) == catalan, ("Catalan", n, len(layer), catalan))
        total_states += len(layer)
        images = Counter()
        depths = Counter()
        fixed = 0
        for tree in layer:
            check(order(tree) == n, ("order", n, tree))
            nxt = odd_contract(tree)
            images[nxt] += 1
            check(order(nxt) <= (n + 1) // 2, ("halving", n, tree, nxt))
            if n > 1:
                check(order(nxt) < n, ("strict", n, tree, nxt))
            value = depth(tree)
            depths[value] += 1
            check(value <= ceil_log2(n), ("clock bound", n, tree, value))
            fixed += nxt == tree
        maximum = max(depths)
        check(maximum == ceil_log2(n), ("sharp", n, maximum))
        check(fixed == (1 if n == 1 else 0), ("fixed", n, fixed))
        check(odd_contract(path(n)) == path((n + 1) // 2), ("path", n))
        print(n, len(layer), len(images), fixed, maximum, depths[maximum])
    return total_states


def audit_time_images(max_cap=11):
    cells = 0
    print("TIME_IMAGE N/t/observed/predicted")
    for cap in range(1, max_cap + 1):
        phase = tuple(tree for n in range(1, cap + 1) for tree in trees(n))
        for time in range(0, ceil_log2(cap) + 2):
            observed = {iterate(tree, time) for tree in phase}
            bound = 1 + (cap - 1) // (2**time)
            predicted = {tree for n in range(1, bound + 1) for tree in trees(n)}
            check(observed == predicted, ("time image", cap, time))
            cells += len(predicted)
            if cap in (1, 5, 9, 11) and time <= 4:
                print(cap, time, len(observed), len(predicted))
    return cells


def audit_local_closed_forms():
    print("LOCAL time/c/denominator-exponent/f0/f1/f4")
    for time in range(0, 8):
        for degree in range(0, 15):
            check(
                local_recurrence(time, degree) == local_closed(time, degree),
                ("local closed", time, degree),
            )
        print(
            time,
            c_constant(time),
            2 ** (time + 1) - 1,
            local_closed(time, 0),
            local_closed(time, 1),
            local_closed(time, 4),
        )


def audit_literal_extremal_fibres():
    boxes = ((0, 1, 8), (1, 1, 6), (2, 1, 3), (3, 1, 2))
    target_cells = 0
    source_cells = 0
    print("EXTREMAL time/m/source-order/targets/sources/aggregate")
    for time, start, stop in boxes:
        for m in range(start, stop + 1):
            source_order = 1 + 2**time * (m - 1)
            counts = Counter()
            for source in trees(source_order):
                counts[iterate(source, time)] += 1
                source_cells += 1
            expected_targets = set(trees(m))
            # Sources on the extremal layer for an m-vertex target may also
            # collapse farther and land below rank m.  The extremal fibre
            # theorem concerns the rank-m slice of that image.
            positive_targets = {
                target
                for target, value in counts.items()
                if value and order(target) == m
            }
            check(positive_targets == expected_targets, ("extremal support", time, m))
            for target in trees(m):
                check(
                    counts[target] == extremal_fibre(time, target),
                    ("target fibre", time, m, target, counts[target]),
                )
                target_cells += 1
            total = sum(
                value for target, value in counts.items() if order(target) == m
            )
            predicted_total = aggregate_extremal(time, m)
            check(total == predicted_total, ("aggregate", time, m, total))
            print(
                time,
                m,
                source_order,
                len(expected_targets),
                len(trees(source_order)),
                predicted_total,
            )
    return target_cells, source_cells


def audit_minimal_deepest():
    print("DEEPEST height/min-order/count/formula")
    for height in range(1, 5):
        n = 1 + 2 ** (height - 1)
        observed = sum(depth(tree) == height for tree in trees(n))
        predicted = c_constant(height - 1)
        check(observed == predicted, ("minimal deepest", height, observed, predicted))
        print(height, n, observed, predicted)


def audit_boundaries():
    singleton = ()
    for time in range(0, 12):
        check(iterate(singleton, time) == singleton, ("singleton", time))
        check(extremal_fibre(time, singleton) == 1, ("singleton fibre", time))
        check(aggregate_extremal(time, 1) == 1, ("singleton aggregate", time))
    check(c_constant(0) == 1, "c0")
    check(local_closed(0, 37) == 1, "t0 local")
    check(extremal_fibre(0, path(8)) == 1, "t0 fibre")
    print("BOUNDARIES N=1/t=0/m=1/large-t PASS")


def main():
    total_states = audit_catalan_and_literal()
    image_cells = audit_time_images()
    audit_local_closed_forms()
    target_cells, source_cells = audit_literal_extremal_fibres()
    audit_minimal_deepest()
    audit_boundaries()
    print("SUMMARY")
    print(f"plane_trees_through_12={total_states}")
    print(f"time_image_target_cells={image_cells}")
    print(f"literal_extremal_target_cells={target_cells}")
    print(f"literal_extremal_source_visits={source_cells}")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("THEOREM halving/image/extremal-fibres/aggregate/deepest PASS")
    print("DECISION GREEN_PENDING_INDEPENDENT_OWNER_COLLISION_GATE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
