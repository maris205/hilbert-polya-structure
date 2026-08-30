#!/usr/bin/env python3
"""Exact pilot for product--residual dynamics on square-zero ideal lattices."""

from collections import Counter
from itertools import product
import json


class Checker:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def rref(rows, p, width):
    rows = [list(row) for row in rows if any(value % p for value in row)]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][column] % p),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % p, -1, p)
        rows[pivot_row] = [(inverse * value) % p for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i == pivot_row:
                continue
            coefficient = rows[i][column] % p
            if coefficient:
                rows[i] = [
                    (a - coefficient * b) % p
                    for a, b in zip(rows[i], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return tuple(tuple(row) for row in rows[:pivot_row])


def span(basis, p, width):
    basis = rref(basis, p, width)
    return frozenset(
        tuple(
            sum(coefficients[i] * basis[i][j] for i in range(len(basis))) % p
            for j in range(width)
        )
        for coefficients in product(range(p), repeat=len(basis))
    )


def subspaces(p, dimension):
    vectors = tuple(product(range(p), repeat=dimension))
    bases = {()}
    for vector in vectors[1:]:
        bases |= {rref(basis + (vector,), p, dimension) for basis in tuple(bases)}
    spaces = {span(basis, p, dimension) for basis in bases}
    return tuple(sorted(spaces, key=lambda space: (len(space), sorted(space))))


def gaussian_binomial(n, k, q):
    if not 0 <= k <= n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def ring_multiply(left, right, p):
    """Multiply in F_p direct-sum V with V squared equal to zero."""
    a, u = left[0], left[1:]
    b, v = right[0], right[1:]
    return (a * b % p,) + tuple((a * y + b * x) % p for x, y in zip(u, v))


def ideal_product(left, right, p, width):
    generators = [ring_multiply(x, y, p) for x in left for y in right]
    return span(generators, p, width)


def ideal_colon(left, right, ring, p):
    return frozenset(
        element
        for element in ring
        if all(ring_multiply(element, value, p) in left for value in right)
    )


def orbit_type(state, transition):
    seen = {}
    current = state
    while current not in seen:
        seen[current] = len(seen)
        current = transition[current]
    return seen[current], len(seen) - seen[current]


def basin_label(state, transition, fixed_ring, fixed_radical, two_cycle):
    current = state
    for _ in range(5):
        if current == fixed_ring:
            return "fixed_ring"
        if current == fixed_radical:
            return "fixed_radical"
        if current in two_cycle:
            return "two_cycle"
        current = transition[current]
    raise AssertionError("state did not enter the advertised recurrent core")


def verify_parameter(checker, p, dimension):
    spaces = subspaces(p, dimension)
    zero_vector = (0,) * dimension
    zero_space = frozenset({zero_vector})
    full_space = frozenset(product(range(p), repeat=dimension))
    ring = frozenset(product(range(p), repeat=dimension + 1))

    proper_ideals = [
        frozenset((0,) + vector for vector in space)
        for space in spaces
    ]
    ideals = tuple(proper_ideals + [ring])
    index = {ideal: i for i, ideal in enumerate(ideals)}
    zero_ideal = frozenset({(0,) + zero_vector})
    maximal_ideal = frozenset((0,) + vector for vector in full_space)
    ring_index = index[ring]
    zero_index = index[zero_ideal]
    maximal_index = index[maximal_ideal]

    lattice_size = sum(gaussian_binomial(dimension, k, p) for k in range(dimension + 1))
    checker.check(len(spaces) == lattice_size, "subspace count disagrees with Gaussian sum")
    checker.check(len(ideals) == lattice_size + 1, "ideal classification count failed")

    transition = {}
    for i, left in enumerate(ideals):
        for j, right in enumerate(ideals):
            product_ideal = ideal_product(left, right, p, dimension + 1)
            colon_ideal = ideal_colon(left, right, ring, p)
            checker.check(product_ideal in index, "literal product left ideal list")
            checker.check(colon_ideal in index, "literal colon left ideal list")

            if i == ring_index:
                predicted_product = right
                predicted_colon = ring
            elif j == ring_index:
                predicted_product = left
                predicted_colon = left
            elif j == zero_index:
                predicted_product = zero_ideal
                predicted_colon = ring
            else:
                predicted_product = zero_ideal
                predicted_colon = ring if right <= left else maximal_ideal

            checker.check(product_ideal == predicted_product, "product case split failed")
            checker.check(colon_ideal == predicted_colon, "colon case split failed")
            transition[(i, j)] = (index[product_ideal], index[colon_ideal])

    types = Counter()
    for state in transition:
        preperiod, period = orbit_type(state, transition)
        checker.check(preperiod <= 3, "depth exceeded three")
        checker.check(period in (1, 2), "unexpected recurrent period")
        types[(preperiod, period)] += 1

    depth_counts = Counter()
    for (depth, _period), count in types.items():
        depth_counts[depth] += count
    expected_depths = {
        0: 4,
        1: lattice_size * lattice_size - 1,
        2: lattice_size - 1,
        3: lattice_size - 1,
    }
    checker.check(dict(depth_counts) == expected_depths, "exact depth census failed")

    fixed_states = {state for state in transition if transition[state] == state}
    checker.check(
        fixed_states == {(ring_index, ring_index), (zero_index, maximal_index)},
        "fixed-point classification failed",
    )
    checker.check(
        transition[(zero_index, zero_index)] == (zero_index, ring_index)
        and transition[(zero_index, ring_index)] == (zero_index, zero_index),
        "distinguished two-cycle failed",
    )
    checker.check(sum(types.values()) == (lattice_size + 1) ** 2, "phase size failed")

    def lattice_count(rank):
        return sum(gaussian_binomial(rank, k, p) for k in range(rank + 1))

    noncontainment_count = sum(
        gaussian_binomial(dimension, rank, p)
        * (lattice_size - lattice_count(dimension - rank))
        for rank in range(1, dimension + 1)
    )
    literal_noncontainment = sum(
        1
        for left in proper_ideals
        for right in proper_ideals
        if right != zero_ideal and not right <= left
    )
    checker.check(
        noncontainment_count == literal_noncontainment,
        "Gaussian noncontainment count failed",
    )

    fixed_ring = (ring_index, ring_index)
    fixed_radical = (zero_index, maximal_index)
    two_cycle = {(zero_index, zero_index), (zero_index, ring_index)}
    basin_depths = Counter()
    for state in transition:
        depth, _period = orbit_type(state, transition)
        label = basin_label(state, transition, fixed_ring, fixed_radical, two_cycle)
        basin_depths[(label, depth)] += 1
    expected_basin_depths = {
        ("fixed_ring", 0): 1,
        ("fixed_radical", 0): 1,
        ("fixed_radical", 1): noncontainment_count - 1,
        ("two_cycle", 0): 2,
        ("two_cycle", 1): lattice_size * lattice_size - noncontainment_count,
        ("two_cycle", 2): lattice_size - 1,
        ("two_cycle", 3): lattice_size - 1,
    }
    expected_basin_depths = {
        key: value for key, value in expected_basin_depths.items() if value
    }
    checker.check(
        dict(basin_depths) == expected_basin_depths,
        "basin-by-depth split failed",
    )

    indegrees = Counter(transition.values())
    expected_indegrees = {
        fixed_radical: noncontainment_count,
        (zero_index, ring_index): lattice_size * lattice_size - noncontainment_count + 1,
        (zero_index, zero_index): 1,
        fixed_ring: 1,
    }
    for proper_index, proper_ideal in enumerate(ideals):
        if proper_ideal in (zero_ideal, ring):
            continue
        expected_indegrees[(proper_index, ring_index)] = 1
        expected_indegrees[(proper_index, proper_index)] = 1
    checker.check(
        dict(indegrees) == expected_indegrees,
        "complete indegree table failed",
    )
    checker.check(
        sum(indegrees.values()) == (lattice_size + 1) ** 2,
        "indegree mass failed",
    )

    return {
        "field": p,
        "radical_dimension": dimension,
        "subspace_ideals": lattice_size,
        "all_ideals": lattice_size + 1,
        "states": (lattice_size + 1) ** 2,
        "depth_counts": dict(sorted(depth_counts.items())),
        "noncontainment_count": noncontainment_count,
        "basin_sizes": {
            "fixed_ring": 1,
            "fixed_radical": noncontainment_count,
            "two_cycle": (lattice_size + 1) ** 2 - 1 - noncontainment_count,
        },
        "distinguished_indegrees": {
            "zero_radical": noncontainment_count,
            "zero_ring": lattice_size * lattice_size - noncontainment_count + 1,
            "zero_zero": 1,
            "ring_ring": 1,
        },
        "fixed_points": 2,
        "two_cycles": 1,
    }


def main():
    checker = Checker()
    parameters = ((2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2))
    summaries = [verify_parameter(checker, p, dimension) for p, dimension in parameters]
    print(
        json.dumps(
            {"assertions": checker.assertions, "parameters": summaries},
            sort_keys=True,
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
