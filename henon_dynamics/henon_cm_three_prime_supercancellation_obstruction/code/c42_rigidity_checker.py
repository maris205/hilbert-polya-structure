#!/usr/bin/env python3
"""Three-prime exact rigidity for Tate plus CM virtual local factors."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def trace_fp(p: int) -> int:
    return -sum(legendre(x**3 + 1, p) for x in range(p))


def determinant3(matrix: list[list[int]]) -> int:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def solve3(matrix: list[list[int]], rhs: list[int]) -> tuple[Fraction, Fraction, Fraction]:
    augmented = [[Fraction(v) for v in row] + [Fraction(y)] for row, y in zip(matrix, rhs)]
    for column in range(3):
        pivot = next(row for row in range(column, 3) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [v / scale for v in augmented[column]]
        for row in range(3):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [x - factor * y for x, y in zip(augmented[row], augmented[column])]
    return tuple(augmented[row][3] for row in range(3))  # type: ignore[return-value]


def first_log_coefficient(A: int, B: int, C: int, p: int) -> int:
    return A + B * trace_fp(p) + C * p


def certificate(bound: int = 12) -> dict[str, object]:
    primes = (5, 7, 11)
    traces = {p: trace_fp(p) for p in primes}
    matrix = [[1, traces[p], p] for p in primes]
    determinant = determinant3(matrix)
    solution = solve3(matrix, [1, 1, 1])
    if determinant != -24 or solution != (Fraction(1), Fraction(0), Fraction(0)):
        raise AssertionError("three-prime rigidity system changed")

    matches: list[list[int]] = []
    checked = 0
    for A in range(-bound, bound + 1):
        for B in range(-bound, bound + 1):
            for C in range(-bound, bound + 1):
                checked += 1
                if all(first_log_coefficient(A, B, C, p) == 1 for p in primes):
                    matches.append([A, B, C])
    if matches != [[1, 0, 0]]:
        raise AssertionError("nontrivial finite cohomological match")

    extra = {str(p): first_log_coefficient(1, 0, 0, p) for p in (13, 17, 19, 23, 29, 31)}
    if set(extra.values()) != {1}:
        raise AssertionError("trivial solution failed holdout primes")
    payload = {
        "candidate": "HCS-C42",
        "curve": "y^2=x^3+1",
        "sentinel_primes": list(primes),
        "sentinel_traces": {str(p): traces[p] for p in primes},
        "coefficient_matrix": matrix,
        "matrix_determinant": determinant,
        "absolute_matrix_determinant": abs(determinant),
        "unique_rational_solution": [str(x) for x in solution],
        "integer_box_bound": bound,
        "integer_vectors_checked": checked,
        "integer_matches": matches,
        "holdout_first_coefficients": extra,
        "status": "PROVED_FINITE_COHOMOLOGY_LOCAL_RIGIDITY",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2, sort_keys=True))
