#!/usr/bin/env python3
"""Finite exact controls for the accompanying all-repetition proof.

These checks reconstruct exterior coefficients and compare direct matrix
determinants; the infinite obstruction is proved in PROOF_PACKAGE.md.
"""
import itertools
import json
from collections import defaultdict

import sympy as sp


def coefficients(matrix):
    eigenvalues = []
    for value, multiplicity in matrix.eigenvals().items():
        eigenvalues.extend([value] * multiplicity)
    unstable = [v for v in eigenvalues if sp.simplify(v * sp.conjugate(v)) > 1]
    assert all(sp.simplify(v * sp.conjugate(v)) != 1 and v != 0 for v in eigenvalues)
    unstable_det = sp.simplify(sp.prod(unstable))
    orientation = int(sp.sign(unstable_det))
    grouped = defaultdict(int)
    for size in range(len(eigenvalues) + 1):
        for selected in itertools.combinations(eigenvalues, size):
            value = sp.simplify(orientation * sp.prod(selected))
            grouped[value] += (-1) ** (len(unstable) + size)
    return {v: c for v, c in grouped.items() if c}


def companion_for_prefix(values):
    n = len(values)
    elementary = [sp.Integer(1)]
    for j in range(1, n + 1):
        elementary.append(sp.simplify(sum(
            (-1) ** (r - 1) * elementary[j-r] * values[r-1]
            for r in range(1, j + 1)) / j))
    # Monic coefficient of x**(n-j) is (-1)**j * elementary[j].
    low_to_high = [(-1) ** (n-i) * elementary[n-i] for i in range(n)]
    matrix = sp.zeros(n)
    for i in range(1, n):
        matrix[i, i-1] = 1
    for i, coefficient in enumerate(low_to_high):
        matrix[i, n-1] = -coefficient
    return matrix


def main():
    half = sp.Rational(1, 2)
    cases = {
        "stable_scalar": sp.diag(half),
        "unstable_scalar": sp.diag(2),
        "negative_unstable": sp.diag(-2),
        "stable_jordan": sp.Matrix([[half, 1], [0, half]]),
        "complex_pair": sp.Matrix([[0, -2], [2, 0]]),
        "negative_symplectic_pair": sp.diag(-2, -half),
        "independent_symplectic_pairs": sp.diag(2, half, 3, sp.Rational(1, 3)),
        "resonant_symplectic_pairs": sp.diag(2, half, 4, sp.Rational(1, 4)),
    }
    count_checks = 0
    inertia_checks = 0
    records = []
    for name, matrix in cases.items():
        grouped = coefficients(matrix)
        assert sum(grouped.values()) == 0
        assert any(c < 0 for c in grouped.values())
        assert any(c > 0 for c in grouped.values())
        for repetition in range(1, 13):
            direct = abs((sp.eye(matrix.rows) - matrix**repetition).det())
            reconstructed = sp.simplify(sum(c * v**repetition for v, c in grouped.items()))
            assert direct > 0
            assert sp.simplify(direct - reconstructed) == 0
            count_checks += 1
        positive = sum(c for c in grouped.values() if c > 0)
        negative = -sum(c for c in grouped.values() if c < 0)
        assert positive == negative
        if all(v.is_real is True for v in grouped):
            x = sp.Symbol("x")
            target = next(v for v, c in grouped.items() if c < 0)
            polynomial = sp.Poly(sp.prod((x-v)/(target-v) for v in grouped if v != target), x)
            vector = sp.Matrix([polynomial.nth(i) for i in range(len(grouped))])
            for offset in (2, 4, 6):
                hankel = sp.Matrix(len(grouped), len(grouped), lambda i, j:
                    abs((sp.eye(matrix.rows) - matrix**(offset+i+j)).det()))
                characteristic = hankel.charpoly().as_poly()
                negative_count = characteristic.count_roots(-sp.oo, 0)
                positive_count = characteristic.count_roots(0, sp.oo)
                assert hankel.det() != 0
                assert negative_count == sum(c < 0 for c in grouped.values())
                assert positive_count == sum(c > 0 for c in grouped.values())
                certificate = sp.simplify((vector.T * hankel * vector)[0])
                assert certificate == grouped[target] * target**offset < 0
                inertia_checks += 1
        records.append({"case": name, "matrix_dimension": matrix.rows,
                        "distinct_products": len(grouped),
                        "graded_even": positive, "graded_odd": negative})
    assert records[-2]["graded_even"] + records[-2]["graded_odd"] == 16
    assert records[-1]["graded_even"] + records[-1]["graded_odd"] == 12

    prefix_checks = 0
    prefix_records = []
    original = sp.diag(2, half)
    weights = [abs((sp.eye(2) - original**r).det()) for r in range(1, 21)]
    assert sp.Matrix([[weights[1], weights[2]], [weights[2], weights[3]]]).det() == -sp.Rational(47, 8)
    for size in range(1, 9):
        companion = companion_for_prefix(weights[:size])
        for repetition in range(1, size + 1):
            assert sp.trace(companion**repetition) == weights[repetition-1]
            prefix_checks += 1
        first_mismatch = next(r for r in range(size+1, 21)
                              if sp.trace(companion**r) != weights[r-1])
        prefix_records.append({"dimension": size, "prefix_matched": size,
                               "first_later_mismatch": first_mismatch})

    # Actual positive controls outside the theorem's assumptions.
    for repetition in range(1, 13):
        assert abs((sp.eye(2) - sp.zeros(2)**repetition).det()) == 1
        assert sp.trace(sp.Matrix([[1]])**repetition) == 1
        assert abs((sp.eye(2) - sp.eye(2)**repetition).det()) == 0
        assert sp.trace(sp.Matrix([[0]])**repetition) == 0

    print(json.dumps({"status": "PASS", "arithmetic": "exact SymPy",
                      "sympy_version": sp.__version__, "matrix_cases": records,
                      "direct_determinant_vs_exterior_checks": count_checks,
                      "exact_hankel_inertia_and_negative_polynomial_checks": inertia_checks,
                      "finite_prefix_moment_checks": prefix_checks,
                      "finite_prefix_realizations": prefix_records,
                      "assumption_boundary_controls": ["singular_zero", "unit_eigenvalue"],
                      "scope": "finite controls, not an infinite proof or release certificate"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
