#!/usr/bin/env python3
"""Independent SymPy polynomial checks for HCS-C170."""
from __future__ import annotations

import json
import sympy as sp


def state_list(n: int) -> list[tuple[int, int]]:
    return [(j, sign) for j in range(n) for sign in (-1, 1)]


def matrix_for(eps: list[int]) -> sp.Matrix:
    n = len(eps)
    states = state_list(n)
    index = {state: i for i, state in enumerate(states)}
    matrix = sp.zeros(2 * n)
    for source, (j, sign) in enumerate(states):
        target = index[((j + 1) % n, eps[j] * sign)]
        matrix[target, source] = 1
    return matrix


def main() -> None:
    z = sp.symbols("z")
    checks = 0
    for n in range(1, 13):
        for eta in (1, -1):
            eps = [1] * n
            if eta == -1:
                eps[-1] = -1
            matrix = matrix_for(eps)
            length = n if eta == 1 else 2 * n
            multiplicity = 2 if eta == 1 else 1
            assert matrix ** length == sp.eye(2 * n)
            checks += 1
            if length > 1:
                assert matrix ** (length - 1) != sp.eye(2 * n)
                checks += 1
            determinant = sp.factor((sp.eye(2 * n) - z * matrix).det())
            assert sp.expand(determinant - (1 - z**length) ** multiplicity) == 0
            checks += 1
            characteristic = sp.factor(matrix.charpoly().as_expr())
            lam = matrix.charpoly().gen
            assert sp.expand(characteristic - (lam**length - 1) ** multiplicity) == 0
            checks += 1

    # Exhaustive small marker words confirm that only eta changes the polynomial.
    for n in range(1, 7):
        for mask in range(1 << n):
            eps = [1 if mask & (1 << j) else -1 for j in range(n)]
            eta = 1
            for sign in eps:
                eta *= sign
            length = n if eta == 1 else 2 * n
            multiplicity = 2 if eta == 1 else 1
            matrix = matrix_for(eps)
            determinant = sp.factor((sp.eye(2 * n) - z * matrix).det())
            assert sp.expand(determinant - (1 - z**length) ** multiplicity) == 0
            checks += 1
    print(json.dumps({"status": "C170_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
