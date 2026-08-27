#!/usr/bin/env python3
"""Hostile controls for complete-bipartite sandpile translations.

The first layer verifies the proposed period formula directly in the reduced
Laplacian cokernel.  The second enumerates literal recurrent configurations,
stabilizes physical chip additions, and checks every resulting orbit for
2 <= m,n <= 4.
"""

from itertools import product
from math import gcd, lcm

import sympy as sp


def reduced_laplacian(m, n):
    """K_{m,n}, with the final vertex in the n-part chosen as sink."""

    size = m + n - 1
    matrix = sp.zeros(size)
    for a in range(m):
        matrix[a, a] = n
        for b in range(n - 1):
            matrix[a, m + b] = -1
            matrix[m + b, a] = -1
    for b in range(n - 1):
        matrix[m + b, m + b] = m
    return matrix


def inverse_denominator_order(matrix, vector):
    solution = matrix.inv() * vector
    return lcm(*(int(sp.denom(value)) for value in solution))


def closed_order(m, n, r, s):
    """Order of r[e_a]+s[e_b] in the reduced Laplacian cokernel."""

    modulus = m * n
    numerators = [
        r * (m + n - 1) + s * n,
        r * (n - 1) + s * n,
        n * (r + 2 * s),
    ]
    # There are additional nonsink vertices in the n-part only when n >= 3.
    if n >= 3:
        numerators.append(n * (r + s))
    divisor = modulus
    for value in numerators:
        divisor = gcd(divisor, value)
    return modulus // divisor


def check_lattice_formula():
    checks = 0
    for m in range(2, 9):
        for n in range(2, 9):
            matrix = reduced_laplacian(m, n)
            assert abs(int(matrix.det())) == m ** (n - 1) * n ** (m - 1)
            for r in range(-4, 5):
                for s in range(-4, 5):
                    vector = sp.zeros(m + n - 1, 1)
                    vector[0] = r
                    vector[m] = s
                    actual = inverse_denominator_order(matrix, vector)
                    expected = closed_order(m, n, r, s)
                    assert actual == expected
                    integral_solution = expected * matrix.inv() * vector
                    assert all(value.q == 1 for value in integral_solution)
                    checks += 2
    return checks


def stabilize(configuration, m, n):
    heights = list(configuration)
    topplings = [0] * len(heights)
    while True:
        unstable = None
        for index in range(m):
            if heights[index] >= n:
                unstable = index
                break
        if unstable is None:
            for b in range(n - 1):
                index = m + b
                if heights[index] >= m:
                    unstable = index
                    break
        if unstable is None:
            return tuple(heights), tuple(topplings)

        topplings[unstable] += 1
        if unstable < m:
            heights[unstable] -= n
            for b in range(n - 1):
                heights[m + b] += 1
            # The remaining chip falls into the sink.
        else:
            heights[unstable] -= m
            for a in range(m):
                heights[a] += 1


def recurrent_states(m, n):
    recurrent = []
    ranges = [range(n)] * m + [range(m)] * (n - 1)
    for state in product(*ranges):
        burned = list(state)
        for a in range(m):
            burned[a] += 1  # one sink edge at every vertex in the m-part
        result, topplings = stabilize(burned, m, n)
        if result == state and all(count == 1 for count in topplings):
            recurrent.append(state)
    return recurrent


def add_and_stabilize(state, m, n, r, s):
    loaded = list(state)
    loaded[0] += r
    loaded[m] += s
    return stabilize(loaded, m, n)[0]


def cycle_lengths(images):
    seen = set()
    lengths = []
    for start in images:
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = images[current]
            length += 1
        assert current == start
        lengths.append(length)
    return lengths


def check_literal_dynamics():
    checks = 0
    rows = []
    for m in range(2, 5):
        for n in range(2, 5):
            recurrent = recurrent_states(m, n)
            expected_size = m ** (n - 1) * n ** (m - 1)
            assert len(recurrent) == expected_size
            recurrent_set = set(recurrent)
            for r, s in ((1, 0), (0, 1), (1, 1), (2, 1)):
                images = {
                    state: add_and_stabilize(state, m, n, r, s)
                    for state in recurrent
                }
                assert set(images.values()) == recurrent_set
                period = closed_order(m, n, r, s)
                lengths = cycle_lengths(images)
                assert lengths and set(lengths) == {period}
                assert len(lengths) == expected_size // period
                rows.append((m, n, r, s, expected_size, period, len(lengths)))
                checks += len(recurrent) + len(lengths) + 3
    return checks, rows


def main():
    lattice_checks = check_lattice_formula()
    dynamics_checks, rows = check_literal_dynamics()
    print(f"PASS reduced-Laplacian order/determinant checks: {lattice_checks}")
    print(f"PASS literal recurrent-addition orbit checks: {dynamics_checks}")
    print("rows (m,n,r,s,recurrent states,period,cycles):")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
