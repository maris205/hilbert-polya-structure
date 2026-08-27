#!/usr/bin/env python3
"""Exact finite shadows of the spherical orthogonality-shift contract.

The topological proof is geometric.  These controls target its fragile
algebraic inputs: all-length bridge positivity on a signed-coordinate test
set, regularity/dimension of path manifolds, and the normalized Funk
eigenvalues on spherical harmonics.
"""

import sympy as sp


def check_coordinate_bridges():
    checks = 0
    for d in range(3, 11):
        # Vertices are +/- e_i.  Orthogonality depends only on the axis.
        adjacency = sp.Matrix(
            2 * d,
            2 * d,
            lambda row, col: int(row // 2 != col // 2),
        )
        power = adjacency
        for length in range(2, 13):
            power *= adjacency
            assert all(entry > 0 for entry in power)
            checks += (2 * d) ** 2

        # One inserted coordinate vector closes every possible endpoint pair.
        for first in range(2 * d):
            for last in range(2 * d):
                spare_axes = set(range(d)) - {first // 2, last // 2}
                assert spare_axes
                inserted_axis = min(spare_axes)
                assert first // 2 != inserted_axis != last // 2
                checks += 1
    return checks


def constraint_jacobian(d, block_length):
    """Jacobian at the exact legal path e_0,e_1,e_2,... (cyclic)."""

    points = []
    for index in range(block_length):
        point = [0] * d
        point[index % d] = 1
        points.append(point)

    rows = []
    # Sphere equations ||x_i||^2=1.
    for index, point in enumerate(points):
        row = [0] * (d * block_length)
        for coordinate in range(d):
            row[d * index + coordinate] = 2 * point[coordinate]
        rows.append(row)
    # Edge equations <x_i,x_{i+1}>=0.
    for index in range(block_length - 1):
        row = [0] * (d * block_length)
        for coordinate in range(d):
            row[d * index + coordinate] = points[index + 1][coordinate]
            row[d * (index + 1) + coordinate] = points[index][coordinate]
        rows.append(row)
    return sp.Matrix(rows)


def check_path_dimensions():
    checks = 0
    rows = []
    for d in range(3, 11):
        for block_length in range(1, 13):
            jacobian = constraint_jacobian(d, block_length)
            expected_rank = 2 * block_length - 1
            expected_dimension = block_length * (d - 2) + 1
            assert jacobian.rank() == expected_rank
            assert d * block_length - jacobian.rank() == expected_dimension
            checks += 2
            rows.append((d, block_length, expected_rank, expected_dimension))
    return checks, rows


def check_funk_spectrum():
    checks = 0
    rows = []
    for d in range(3, 11):
        nu = sp.Rational(d - 2, 2)
        previous = sp.Integer(1)
        for k in range(0, 13):
            degree = 2 * k
            gegenbauer_ratio = sp.simplify(
                sp.gegenbauer(degree, nu, 0) / sp.gegenbauer(degree, nu, 1)
            )
            closed = sp.simplify(
                (-1) ** k * sp.rf(sp.Rational(1, 2), k)
                / sp.rf(sp.Rational(d - 1, 2), k)
            )
            assert sp.simplify(gegenbauer_ratio - closed) == 0
            if k >= 1:
                assert abs(closed) <= abs(previous)
            previous = closed
            checks += 1
            rows.append((d, degree, closed))

        # Odd harmonics vanish at the equator; the largest nonconstant
        # eigenvalue modulus is |lambda_2|=1/(d-1).
        for degree in range(1, 24, 2):
            assert sp.gegenbauer(degree, nu, 0) == 0
            checks += 1
        assert abs(
            sp.gegenbauer(2, nu, 0) / sp.gegenbauer(2, nu, 1)
        ) == sp.Rational(1, d - 1)
        checks += 1
    return checks, rows


def main():
    bridge_checks = check_coordinate_bridges()
    dimension_checks, dimension_rows = check_path_dimensions()
    spectrum_checks, spectrum_rows = check_funk_spectrum()
    print(f"PASS signed-coordinate bridge/closing checks: {bridge_checks}")
    print(f"PASS exact Jacobian rank/dimension checks: {dimension_checks}")
    print(f"PASS Gegenbauer/Funk spectral checks: {spectrum_checks}")
    print("sample dimensions (d,n,rank,dimension):", dimension_rows[:8])
    print("sample eigenvalues (d,degree,lambda):", spectrum_rows[:8])


if __name__ == "__main__":
    main()
