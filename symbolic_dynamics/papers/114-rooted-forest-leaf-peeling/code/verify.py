#!/usr/bin/env python3
"""Exact controls for P114: parallel leaf peeling on rooted forests."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


class Audit:
    def __init__(self):
        self.n = 0

    def check(self, condition, message="assertion failed"):
        self.n += 1
        if not condition:
            raise AssertionError(message)


A = Audit()


def valid(parent):
    vertices = {i for i, value in enumerate(parent) if value >= 0}
    for vertex in vertices:
        if parent[vertex] not in vertices:
            return False
        seen = set()
        current = vertex
        while parent[current] != current:
            if current in seen:
                return False
            seen.add(current)
            current = parent[current]
    return True


def states(n):
    yield (-1,) * n
    for m in range(1, n + 1):
        for subset in combinations(range(n), m):
            for values in product(subset, repeat=m):
                parent = [-1] * n
                for vertex, image in zip(subset, values):
                    parent[vertex] = image
                parent = tuple(parent)
                if valid(parent):
                    yield parent


def vertices(parent):
    return frozenset(i for i, value in enumerate(parent) if value >= 0)


def roots(parent):
    return frozenset(i for i, value in enumerate(parent) if value == i)


def leaves(parent):
    present = vertices(parent)
    root_set = roots(parent)
    has_child = set()
    for vertex in present - root_set:
        has_child.add(parent[vertex])
    return frozenset((present - root_set) - has_child)


def update(parent):
    out = list(parent)
    for vertex in leaves(parent):
        out[vertex] = -1
    out = tuple(out)
    A.check(valid(out), "update left the phase")
    return out


def orbit(parent):
    current = parent
    time = 0
    while update(current) != current:
        current = update(current)
        time += 1
        A.check(time <= len(parent), "nonterminating orbit")
    return time, current


def cayley(m, r):
    if m == r:
        return 1
    return r * m ** (m - r - 1)


def basin(n, r):
    if not r:
        return 1
    return sum(comb(n - r, k) * cayley(r + k, r) for k in range(n - r + 1))


def phase(n):
    return 1 + sum(
        comb(n, m) * (m + 1) ** (m - 1) for m in range(1, n + 1)
    )


def local_fibre(n, target):
    m = len(vertices(target))
    s = len(leaves(target))
    return sum(
        (-1) ** j * comb(s, j) * (m - j + 1) ** (n - m)
        for j in range(s + 1)
    )


def multiply(left, right, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def exp_series(series, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = Fraction(1)
    for n in range(1, degree + 1):
        out[n] = sum(
            k * series[k] * out[n - k] for k in range(1, n + 1)
        ) / n
    return out


def height_series(max_height, degree):
    layers = [[Fraction(0) for _ in range(degree + 1)]]
    layers[0][0] = Fraction(1)
    for _ in range(max_height):
        layers.append(exp_series([Fraction(0)] + layers[-1][:-1], degree))
    return layers


def bounded_basin(n, r, h, layers):
    if not r:
        return 1
    degree = n - r
    forest = [Fraction(0) for _ in range(degree + 1)]
    forest[0] = Fraction(1)
    for _ in range(r):
        forest = multiply(forest, layers[h], degree)
    total = Fraction(0)
    for k in range(degree + 1):
        total += comb(degree, k) * factorial(k) * forest[k]
    A.check(total.denominator == 1)
    return total.numerator


def run(n):
    phase_states = list(states(n))
    A.check(len(phase_states) == len(set(phase_states)))
    A.check(len(phase_states) == phase(n))
    predecessor_count = Counter(update(state) for state in phase_states)
    endpoint_basin = Counter()
    endpoint_depth = defaultdict(Counter)
    depth_histogram = Counter()

    for state in phase_states:
        depth, endpoint = orbit(state)
        A.check(vertices(endpoint) == roots(state))
        A.check(roots(endpoint) == roots(state))
        endpoint_basin[endpoint] += 1
        endpoint_depth[endpoint][depth] += 1
        depth_histogram[depth] += 1

    fixed = [state for state in phase_states if update(state) == state]
    A.check(len(fixed) == 2**n)
    layers = height_series(n, n)
    for endpoint in fixed:
        r = len(roots(endpoint))
        A.check(endpoint_basin[endpoint] == basin(n, r))
        for h in range(n):
            literal = sum(
                count
                for depth, count in endpoint_depth[endpoint].items()
                if depth <= h
            )
            A.check(literal == bounded_basin(n, r, h, layers))

    for target in phase_states:
        A.check(predecessor_count[target] == local_fibre(n, target))

    if n:
        A.check(max(depth_histogram) == n - 1)
    if n >= 2:
        A.check(depth_histogram[n - 1] == factorial(n))
    A.check(sum(comb(n, r) * basin(n, r) for r in range(n + 1)) == phase(n))
    print(
        f"n={n}: phase={len(phase_states)}, fixed={len(fixed)}, "
        f"depths={dict(sorted(depth_histogram.items()))}"
    )


def main():
    for n in range(7):
        run(n)
    print(f"PASS: {A.n:,} exact assertions")


if __name__ == "__main__":
    main()
