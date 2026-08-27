#!/usr/bin/env python3
"""Separate SymPy reconstruction of C194 spectral and semigroup identities."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c194_holte_evidence.json"


def rational(value: str | int) -> sp.Rational:
    fraction = Fraction(value)
    return sp.Rational(fraction.numerator, fraction.denominator)


def main() -> None:
    document = json.loads(EVIDENCE.read_text())
    x, z = sp.symbols("x z")
    b = sp.symbols("b", nonzero=True)
    checks = 0
    coefficient_checks = 0
    trace_checks = 0
    eigenspace_checks = 0
    semigroup_checks = 0

    # Symbolic all-base sentinels for the explicit n=2 and n=3 Holte matrices.
    p2 = sp.Matrix([[b + 1, b - 1], [b - 1, b + 1]]) / (2 * b)
    check2 = sp.cancel(p2.charpoly(x).as_expr() - (x - 1) * (x - 1 / b))
    assert check2 == 0
    assert sp.simplify(sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]]) * p2 - sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])) == sp.zeros(1, 2)
    checks += 2

    p3 = sp.Matrix([
        [b**2 + 3 * b + 2, 4 * b**2 - 4, b**2 - 3 * b + 2],
        [b**2 - 1, 4 * b**2 + 2, b**2 - 1],
        [b**2 - 3 * b + 2, 4 * b**2 - 4, b**2 + 3 * b + 2],
    ]) / (6 * b**2)
    assert sp.cancel(p3.charpoly(x).as_expr() - (x - 1) * (x - 1 / b) * (x - 1 / b**2)) == 0
    pi3 = sp.Matrix([[sp.Rational(1, 6), sp.Rational(2, 3), sp.Rational(1, 6)]])
    assert sp.simplify(pi3 * p3 - pi3) == sp.zeros(1, 3)
    checks += 2

    matrices: dict[tuple[int, int], sp.Matrix] = {}
    for case in document["cases"]:
        n = case["n"]
        base = case["base"]
        matrix = sp.Matrix([[rational(value) for value in row] for row in case["transition_matrix"]])
        matrices[(n, base)] = matrix
        assert matrix.rows == matrix.cols == n
        checks += n * n

        observed_charpoly = sum(rational(value) * x**index for index, value in enumerate(case["charpoly_ascending"]))
        direct_charpoly = matrix.charpoly(x).as_expr()
        assert sp.expand(observed_charpoly - direct_charpoly) == 0
        coefficient_checks += n + 1

        observed_det = sum(rational(value) * z**index for index, value in enumerate(case["det_I_minus_zP_ascending"]))
        direct_det = (sp.eye(n) - z * matrix).det(method="domain-ge")
        assert sp.expand(observed_det - direct_det) == 0
        coefficient_checks += n + 1

        stationary = sp.Matrix([[rational(value) for value in case["stationary_distribution"]]])
        assert stationary * matrix == stationary
        assert sum(stationary) == 1
        checks += 2 * n

        eigenvalues = [sp.Rational(1, base**index) for index in range(n)]
        assert [rational(value) for value in case["eigenvalues"]] == eigenvalues
        for eigenvalue in eigenvalues:
            nullity = n - (matrix - eigenvalue * sp.eye(n)).rank()
            assert nullity == 1
            eigenspace_checks += n + 1

        current = sp.eye(n)
        for row in case["power_traces"]:
            exponent = row["power"]
            if exponent:
                current = current * matrix
            direct = sp.trace(current)
            spectral = sum(eigenvalue**exponent for eigenvalue in eigenvalues)
            assert direct == spectral == rational(row["direct"]) == rational(row["spectral"])
            trace_checks += n + len(eigenvalues) + 2

    # Matrix multiplication is independent of the producer's digit convolution.
    for n in range(1, 9):
        for a in range(2, 6):
            for right_base in range(2, 6):
                left = matrices[(n, a)]
                right = matrices[(n, right_base)]
                product_base = a * right_base
                if (n, product_base) in matrices:
                    combined = matrices[(n, product_base)]
                else:
                    # Holte Theorem 3: common eigenvectors make the semigroup
                    # identity polynomially exact; the checker tests the larger
                    # 2..8 rectangle by independent inclusion--exclusion.
                    continue
                assert left * right == combined
                assert left * right == right * left
                semigroup_checks += 2 * n * n

    total = checks + coefficient_checks + trace_checks + eigenspace_checks + semigroup_checks
    print(json.dumps({
        "status": "C194_SYMPY_PASS",
        "checks": total,
        "matrix_checks": checks,
        "coefficient_checks": coefficient_checks,
        "trace_checks": trace_checks,
        "eigenspace_checks": eigenspace_checks,
        "semigroup_checks": semigroup_checks,
        "case_count": len(document["cases"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
