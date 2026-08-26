#!/usr/bin/env python3
"""Separate SymPy reconstruction for HCS-C184."""
from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c184_spectral_decimation_evidence.json"


def graph_matrix(level: int) -> sp.Matrix:
    scale = 1
    edges = {
        tuple(sorted(((0, 0), (1, 0)))),
        tuple(sorted(((0, 0), (0, 1)))),
        tuple(sorted(((1, 0), (0, 1)))),
    }
    for _ in range(level):
        edges = {
            tuple(sorted(((u[0] + dx, u[1] + dy), (v[0] + dx, v[1] + dy))))
            for dx, dy in ((0, 0), (scale, 0), (0, scale))
            for u, v in edges
        }
        scale *= 2
    vertices = {vertex for edge in edges for vertex in edge}
    interior = sorted(vertices - {(0, 0), (scale, 0), (0, scale)})
    position = {vertex: index for index, vertex in enumerate(interior)}
    degree = defaultdict(int)
    matrix = sp.zeros(len(interior))
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        if u in position and v in position:
            matrix[position[u], position[v]] = matrix[position[v], position[u]] = -1
    for vertex, index in position.items():
        matrix[index, index] = degree[vertex]
    return matrix


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    level_rows = {row["level"]: row for row in data["finite_regression"]["level_rows"]}
    checks = 0
    t, u = sp.symbols("t u")
    R = t * (5 - t)
    phi_minus = (5 - sp.sqrt(25 - 4 * u)) / 2
    phi_plus = (5 + sp.sqrt(25 - 4 * u)) / 2
    assert sp.simplify(phi_minus * (5 - phi_minus) - u) == 0
    checks += 1
    assert sp.simplify(phi_plus * (5 - phi_plus) - u) == 0
    checks += 1
    assert sp.expand((R - 6) + (t - 2) * (t - 3)) == 0
    checks += 1

    direct_polynomials = {}
    for level in range(1, 5):
        matrix = graph_matrix(level)
        dimension = (3 ** (level + 1) - 3) // 2
        assert matrix.rows == dimension
        checks += 1
        for i in range(dimension):
            assert matrix[i, i] == 4
            checks += 1
            for j in range(dimension):
                assert matrix[i, j] == matrix[j, i]
                checks += 1
                assert matrix[i, j] in {-1, 0, 4}
                checks += 1
        polynomial = sp.Poly(matrix.charpoly(t).as_expr(), t)
        direct_polynomials[level] = polynomial
        ascending = list(reversed([int(value) for value in polynomial.all_coeffs()]))
        recorded = list(map(int, level_rows[level]["characteristic_polynomial_coefficients_ascending"]))
        assert ascending == recorded
        checks += 1
        for got, expected in zip(ascending, recorded):
            assert got == expected
            checks += 1
        assert int(matrix.det()) == int(level_rows[level]["determinant"])
        checks += 1
        assert sp.trace(matrix) == 4 * dimension
        checks += 1
        if level <= 3:
            inverse = matrix.inv()
            zeta_one = sp.trace(inverse)
            zeta_two = sp.trace(inverse * inverse)
            assert zeta_one.is_Rational and zeta_one > 0
            checks += 1
            assert zeta_two.is_Rational and zeta_two > 0
            checks += 1

    previous = direct_polynomials[1]
    for level in range(2, 6):
        old_dimension = (3**level - 3) // 2
        previous_six = (3 ** (level - 1) - 3) // 2 if level >= 3 else 0
        five_birth = (3 ** (level - 1) + 3) // 2
        six_birth = (3**level - 3) // 2
        expression = sp.Poly(sp.cancel(
            (-1) ** old_dimension
            * (t - 5) ** five_birth
            * (t - 6) ** six_birth
            * previous.as_expr().subs(t, R)
            / (t - 2) ** previous_six
        ), t)
        recorded = list(map(int, level_rows[level]["characteristic_polynomial_coefficients_ascending"]))
        rebuilt = list(reversed([int(value) for value in expression.all_coeffs()]))
        assert rebuilt == recorded
        checks += 1
        for got, expected in zip(rebuilt, recorded):
            assert got == expected
            checks += 1
        if level <= 4:
            assert expression == direct_polynomials[level]
            checks += 1
        previous = expression

    previous_a = 1
    previous_b = 0
    previous_c = 2
    for level in range(1, 21):
        two_exp = (3**level - 1) // 2
        three_exp = (3 ** (level + 1) - 6 * level - 3) // 4
        five_exp = (3**level + 6 * level - 1) // 4
        assert all(value >= 0 and isinstance(value, int) for value in (two_exp, three_exp, five_exp))
        checks += 1
        if level > 1:
            b_level = (3**level - 3) // 2
            b_previous = (3 ** (level - 1) - 3) // 2
            a_level = (3 ** (level - 1) + 3) // 2
            assert two_exp == previous_a + b_level - b_previous
            checks += 1
            assert three_exp == previous_b + b_level
            checks += 1
            assert five_exp == previous_c + a_level
            checks += 1
        previous_a, previous_b, previous_c = two_exp, three_exp, five_exp

    for level in range(1, 31):
        dimension = (3 ** (level + 1) - 3) // 2
        two_population = 2 ** (level - 1)
        five_population = sum(
            2 ** (level - birth) * (3 ** (birth - 1) + 3) // 2
            for birth in range(1, level + 1)
        )
        six_population = (3**level - 3) // 2
        six_population += sum(
            2 ** (level - birth - 1) * (3**birth - 3) // 2
            for birth in range(2, level)
        )
        assert two_population + five_population + six_population == dimension
        checks += 1

    print(json.dumps({"status": "C184_SYMPY_PASS", "checks": checks, "direct_graph_charpolys": 4}, sort_keys=True))


if __name__ == "__main__":
    main()
