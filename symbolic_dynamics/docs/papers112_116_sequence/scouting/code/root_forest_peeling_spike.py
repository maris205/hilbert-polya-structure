#!/usr/bin/env python3
"""Exact spike for parallel leaf peeling on labelled rooted forests.

The ambient label set is [n].  A state is a rooted forest on any subset of
[n], represented by a parent function whose only directed cycles are loops.
Every non-root leaf is deleted simultaneously; roots are immortal.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def is_rooted_forest(parent):
    n = len(parent)
    present = {v for v in range(n) if parent[v] >= 0}
    for v in present:
        if parent[v] not in present:
            return False
        seen = set()
        current = v
        while parent[current] != current:
            if current in seen:
                return False
            seen.add(current)
            current = parent[current]
        if current not in present:
            return False
    return True


def all_states(n):
    vertices = range(n)
    yield (-1,) * n
    for size in range(1, n + 1):
        for subset in combinations(vertices, size):
            for values in product(subset, repeat=size):
                parent = [-1] * n
                for vertex, image in zip(subset, values):
                    parent[vertex] = image
                parent = tuple(parent)
                if is_rooted_forest(parent):
                    yield parent


def roots(parent):
    return frozenset(v for v, image in enumerate(parent) if image == v)


def present(parent):
    return frozenset(v for v, image in enumerate(parent) if image >= 0)


def nonroot_leaves(parent):
    vertices = present(parent)
    root_set = roots(parent)
    child_count = Counter()
    for vertex in vertices:
        if vertex not in root_set:
            child_count[parent[vertex]] += 1
    return frozenset(
        vertex
        for vertex in vertices - root_set
        if child_count[vertex] == 0
    )


def update(parent):
    leaves = nonroot_leaves(parent)
    out = list(parent)
    for vertex in leaves:
        out[vertex] = -1
    result = tuple(out)
    AUDIT.check(is_rooted_forest(result))
    return result


def orbit_data(parent):
    time = 0
    current = parent
    while update(current) != current:
        current = update(current)
        time += 1
        AUDIT.check(time < len(parent) + 1)
    return time, current


def cayley_fixed_roots(total_vertices, root_count):
    if total_vertices == 0 and root_count == 0:
        return 1
    if root_count <= 0 or root_count > total_vertices:
        return 0
    if root_count == total_vertices:
        return 1
    return root_count * total_vertices ** (total_vertices - root_count - 1)


def phase_formula(n):
    total = 1
    for size in range(1, n + 1):
        total += comb(n, size) * (size + 1) ** (size - 1)
    return total


def basin_formula(n, root_count):
    if root_count == 0:
        return 1
    return sum(
        comb(n - root_count, nonroots)
        * cayley_fixed_roots(root_count + nonroots, root_count)
        for nonroots in range(n - root_count + 1)
    )


def immediate_fibre_formula(n, target):
    vertex_count = len(present(target))
    required = len(nonroot_leaves(target))
    missing = n - vertex_count
    return sum(
        (-1) ** j
        * comb(required, j)
        * (vertex_count - j + 1) ** missing
        for j in range(required + 1)
    )


def convolve(left, right, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def exp_series(series, degree):
    AUDIT.check(series[0] == 0)
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = Fraction(1)
    for n in range(1, degree + 1):
        out[n] = sum(
            k * series[k] * out[n - k] for k in range(1, n + 1)
        ) / n
    return out


def power_series(series, exponent, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = Fraction(1)
    for _ in range(exponent):
        out = convolve(out, series, degree)
    return out


def rooted_tree_egfs(max_height, degree):
    # A_h counts one tree with a distinguished, unlabelled root and labelled
    # non-root vertices, with height at most h.
    layers = [[Fraction(0) for _ in range(degree + 1)]]
    layers[0][0] = Fraction(1)
    for _ in range(max_height):
        shifted = [Fraction(0)] + layers[-1][:-1]
        layers.append(exp_series(shifted, degree))
    return layers


def bounded_basin_formula(n, root_count, height, layers):
    if root_count == 0:
        return 1
    available = n - root_count
    forest_series = power_series(layers[height], root_count, available)
    total = 0
    for nonroots in range(available + 1):
        fixed_label_count = forest_series[nonroots] * factorial(nonroots)
        AUDIT.check(fixed_label_count.denominator == 1)
        total += comb(available, nonroots) * fixed_label_count.numerator
    return total


def run_lane(n):
    states = list(all_states(n))
    AUDIT.check(len(states) == len(set(states)))
    AUDIT.check(len(states) == phase_formula(n))
    state_set = set(states)
    endpoint_basin = Counter()
    endpoint_depth = defaultdict(Counter)
    predecessors = Counter(update(state) for state in states)
    depth_histogram = Counter()

    for state in states:
        depth, endpoint = orbit_data(state)
        AUDIT.check(endpoint in state_set)
        AUDIT.check(present(endpoint) == roots(state))
        AUDIT.check(roots(endpoint) == roots(state))
        endpoint_basin[endpoint] += 1
        endpoint_depth[endpoint][depth] += 1
        depth_histogram[depth] += 1

    fixed = [state for state in states if update(state) == state]
    AUDIT.check(len(fixed) == 2**n)
    layers = rooted_tree_egfs(n, n)
    for endpoint in fixed:
        root_count = len(roots(endpoint))
        AUDIT.check(endpoint_basin[endpoint] == basin_formula(n, root_count))
        AUDIT.check(predecessors[endpoint] == immediate_fibre_formula(n, endpoint))
        for height in range(n):
            literal = sum(
                count
                for depth, count in endpoint_depth[endpoint].items()
                if depth <= height
            )
            formula = bounded_basin_formula(n, root_count, height, layers)
            AUDIT.check(
                literal == formula,
                f"height CDF mismatch n={n}, roots={root_count}, h={height}",
            )

    for target in states:
        AUDIT.check(predecessors[target] == immediate_fibre_formula(n, target))

    if n >= 1:
        AUDIT.check(max(depth_histogram) == n - 1)
    if n >= 2:
        AUDIT.check(depth_histogram[n - 1] == factorial(n))
    AUDIT.check(
        sum(comb(n, r) * basin_formula(n, r) for r in range(n + 1))
        == len(states)
    )
    print(
        f"n={n}: phase={len(states)}, fixed={len(fixed)}, "
        f"depths={dict(sorted(depth_histogram.items()))}, "
        f"deepest={depth_histogram[max(depth_histogram)]}"
    )


def main():
    for n in range(0, 7):
        run_lane(n)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
