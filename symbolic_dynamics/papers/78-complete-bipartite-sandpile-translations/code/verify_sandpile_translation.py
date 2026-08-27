#!/usr/bin/env python3
"""Exact cokernel and literal-dynamics checks for P78."""

from itertools import product
from math import gcd, lcm

import sympy as sp


def reduced_laplacian(m, n):
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
    return lcm(*(int(sp.denom(value)) for value in matrix.inv() * vector))


def closed_order(m, n, alpha, beta):
    modulus = m * n
    numerators = [
        alpha * (m + n - 1) + beta * n,
        alpha * (n - 1) + beta * n,
        n * (alpha + 2 * beta),
    ]
    if n >= 3:
        numerators.append(n * (alpha + beta))
    divisor = modulus
    for value in numerators:
        divisor = gcd(divisor, value)
    return modulus // divisor


def closed_profile_order(m, n, alphas, betas):
    """Order predicted by the arbitrary-profile theorem."""

    assert len(alphas) == m and len(betas) == n - 1
    total_a = sum(alphas)
    total_b = sum(betas)
    denominators = [
        m * n // gcd(m * n, (n - 1) * total_a + n * total_b + m * alpha)
        for alpha in alphas
    ]
    denominators.extend(
        m // gcd(m, total_a + total_b + beta)
        for beta in betas
    )
    return lcm(*denominators)


def deterministic_profiles(m, n):
    """Signed nonlocal profiles, including sparse and dense edge cases."""

    yield (0,) * m, (0,) * (n - 1)
    yield (1,) + (0,) * (m - 1), (0,) * (n - 1)
    yield (0,) * m, (1,) + (0,) * (n - 2)
    for seed in range(9):
        alphas = tuple(((seed + 2) * (i + 1) + i * i) % 9 - 4 for i in range(m))
        betas = tuple(((seed + 3) * (j + 2) + 2 * j * j) % 11 - 5 for j in range(n - 1))
        yield alphas, betas


def check_lattice_formula():
    two_site_checks = 0
    profile_checks = 0
    for m in range(2, 9):
        for n in range(2, 9):
            matrix = reduced_laplacian(m, n)
            inverse = matrix.inv()
            assert abs(int(matrix.det())) == m ** (n - 1) * n ** (m - 1)
            for alpha in range(-4, 5):
                for beta in range(-4, 5):
                    vector = sp.zeros(m + n - 1, 1)
                    vector[0] = alpha
                    vector[m] = beta
                    solution = inverse * vector
                    actual = lcm(*(int(sp.denom(value)) for value in solution))
                    expected = closed_order(m, n, alpha, beta)
                    assert actual == expected
                    assert all(value.q == 1 for value in expected * solution)
                    two_site_checks += 2

            for alphas, betas in deterministic_profiles(m, n):
                vector = sp.Matrix((*alphas, *betas))
                solution = inverse * vector
                actual = lcm(*(int(sp.denom(value)) for value in solution))
                expected = closed_profile_order(m, n, alphas, betas)
                assert actual == expected
                assert all(value.q == 1 for value in expected * solution)
                profile_checks += 2
    return two_site_checks, profile_checks


def stabilize(configuration, m, n):
    heights = list(configuration)
    topplings = [0] * len(heights)
    while True:
        unstable = next((i for i in range(m) if heights[i] >= n), None)
        if unstable is None:
            unstable = next((m + b for b in range(n - 1) if heights[m + b] >= m), None)
        if unstable is None:
            return tuple(heights), tuple(topplings)
        topplings[unstable] += 1
        if unstable < m:
            heights[unstable] -= n
            for b in range(n - 1):
                heights[m + b] += 1
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
            burned[a] += 1
        result, topplings = stabilize(burned, m, n)
        if result == state and all(count == 1 for count in topplings):
            recurrent.append(state)
    return recurrent


def add_and_stabilize(state, m, n, alpha, beta):
    loaded = list(state)
    loaded[0] += alpha
    loaded[m] += beta
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
            size = m ** (n - 1) * n ** (m - 1)
            assert len(recurrent) == size
            recurrent_set = set(recurrent)
            for alpha, beta in ((1, 0), (0, 1), (1, 1), (2, 1)):
                images = {state: add_and_stabilize(state, m, n, alpha, beta) for state in recurrent}
                assert set(images.values()) == recurrent_set
                period = closed_order(m, n, alpha, beta)
                lengths = cycle_lengths(images)
                assert lengths and set(lengths) == {period}
                assert len(lengths) == size // period
                rows.append((m, n, alpha, beta, size, period, len(lengths)))
                checks += len(recurrent) + len(lengths) + 3
    return checks, rows


def main():
    two_site_checks, profile_checks = check_lattice_formula()
    dynamics_checks, rows = check_literal_dynamics()
    print(f"PASS two-site reduced-Laplacian checks: {two_site_checks}")
    print(f"PASS arbitrary-profile reduced-Laplacian checks: {profile_checks}")
    print(f"PASS literal recurrent-addition orbit checks: {dynamics_checks}")
    print("rows (m,n,alpha,beta,recurrent states,period,cycles):")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
