#!/usr/bin/env python3
"""Separate SymPy reconstruction of C200, without producer imports."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c200_jacobi_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(expression, message):
        nonlocal checks
        checks += 1
        if sp.simplify(expression) != 0:
            raise AssertionError(message)

    x = sp.symbols("x", positive=True)
    alpha, beta = sp.symbols("alpha beta", positive=True)
    pi = x ** (alpha - 1) * (1 - x) ** (beta - 1)
    f = sp.Function("f")(x)
    generator = x * (1 - x) * sp.diff(f, x, 2) + (alpha - (alpha + beta) * x) * sp.diff(f, x)
    divergence = sp.diff(x * (1 - x) * pi * sp.diff(f, x), x) / pi
    check(generator - divergence, "divergence form")
    for k in range(1, 9):
        monomial = x ** k
        expected = k * (k + alpha - 1) * x ** (k - 1) - k * (k + alpha + beta - 1) * x ** k
        check(x * (1 - x) * sp.diff(monomial, x, 2) +
              (alpha - (alpha + beta) * x) * sp.diff(monomial, x) - expected, "moment action")
    for n in range(9):
        jacobi = sp.jacobi(n, beta - 1, alpha - 1, 2 * x - 1)
        value = x * (1 - x) * sp.diff(jacobi, x, 2) + (alpha - (alpha + beta) * x) * sp.diff(jacobi, x)
        check(value + n * (n + alpha + beta - 1) * jacobi, "Jacobi eigenfunction")

    evidence_checks = 0
    for case in data["regression"]["parameter_cases"]:
        a, b = sp.Rational(case["alpha"]), sp.Rational(case["beta"])
        moments = [sp.Rational(value) for value in case["stationary_moments_0_to_8"]]
        for k in range(1, 9):
            check(k * (k + a - 1) * moments[k - 1] - k * (k + a + b - 1) * moments[k], "evidence moment")
            evidence_checks += 1
        for row in case["polynomial_rows"]:
            coefficients = [sp.Rational(value) for value in row["coefficients_ascending"]]
            polynomial = sum(value * x ** j for j, value in enumerate(coefficients))
            n = row["degree"]
            residual = x * (1 - x) * sp.diff(polynomial, x, 2) + (a - (a + b) * x) * sp.diff(polynomial, x)
            check(residual + n * (n + a + b - 1) * polynomial, "evidence eigenpolynomial")
            evidence_checks += 1
    print(json.dumps({
        "status": "C200_SYMPY_PASS",
        "checks": checks,
        "generic_symbolic_identities": 18,
        "evidence_symbolic_identities": evidence_checks,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
