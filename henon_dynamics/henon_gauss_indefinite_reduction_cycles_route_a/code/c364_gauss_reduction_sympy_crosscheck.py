#!/usr/bin/env python3
"""Independent SymPy identity lane for HCS-C364."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c364_gauss_reduction_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C364 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text(), parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    identities = 0
    delta, p, q, a, x = sp.symbols("Delta P Q a x")
    pn = a * q - p
    qn = (delta - pn ** 2) / q
    alpha = (p + sp.sqrt(delta)) / q
    transformed = 1 / (alpha - a)
    if sp.simplify(transformed - (pn + sp.sqrt(delta)) / qn) != 0:
        raise AssertionError("symbolic Gauss pair update")
    identities += 1
    alpha_bar = (p - sp.sqrt(delta)) / q
    if sp.simplify(-1 / alpha_bar - (p + sp.sqrt(delta)) / ((delta - p ** 2) / q)) != 0:
        raise AssertionError("symbolic reversal")
    identities += 1
    form_a, form_b, form_c = q / 2, -p, (p ** 2 - delta) / (2 * q)
    if sp.expand(form_b ** 2 - 4 * form_a * form_c - delta) != 0:
        raise AssertionError("symbolic form discriminant")
    identities += 1

    for row in data["cycle_rows"]:
        matrix = sp.Matrix(row["period_matrix"])
        length = row["length"]
        if matrix.det() != (-1) ** length:
            raise AssertionError("matrix determinant")
        identities += 1
        delta_value = row["delta"]
        p_value, q_value = row["seed"]
        fixed_polynomial = sp.Poly(matrix[1, 0] * x ** 2 + (matrix[1, 1] - matrix[0, 0]) * x - matrix[0, 1], x)
        minimal_polynomial = sp.Poly((q_value // 2) * x ** 2 - p_value * x + (p_value * p_value - delta_value) // (2 * q_value), x)
        if fixed_polynomial != row["stabilizer_scale"] * minimal_polynomial:
            raise AssertionError("matrix fixed polynomial")
        identities += 1
        lam = sp.symbols("lambda", positive=True)
        inverse_derivative = matrix.det() / lam ** 2
        if sp.simplify(abs(matrix.det()) / inverse_derivative ** 2 - lam ** 4) != 0:
            raise AssertionError("derivative algebra")
        identities += 1
        scale = row["stabilizer_scale"]
        if sp.expand(matrix.trace() ** 2 - 4 * matrix.det() - scale ** 2 * delta_value) != 0:
            raise AssertionError("matrix discriminant")
        identities += 1

    z = sp.symbols("z")
    for length in range(1, 13):
        permutation = sp.zeros(length)
        for index in range(length):
            permutation[(index + 1) % length, index] = 1
        if sp.expand((sp.eye(length) - z * permutation).det() - (1 - z ** length)) != 0:
            raise AssertionError("cycle determinant")
        identities += 1
        for power in range(1, 25):
            expected = length if power % length == 0 else 0
            if sp.trace(permutation ** power) != expected:
                raise AssertionError("cycle fixed trace")
            identities += 1
    print(f"C364 SymPy cross-check: PASS ({identities} exact identities)")


if __name__ == "__main__":
    main()
