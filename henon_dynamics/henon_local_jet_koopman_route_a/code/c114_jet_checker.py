#!/usr/bin/env python3
"""Independent checker for the C114 local Koopman-jet evidence.

This file deliberately does not import the producer.  Its polynomial engine,
basis construction, and matrix reconstruction are repeated independently.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c114_jet_evidence.json"


def f(text: str) -> Fraction:
    return Fraction(text)


def multiply(left: dict[tuple[int, int], Fraction], right: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for (a, b), coefficient in left.items():
        for (c, d), other in right.items():
            if a + b + c + d <= 4:
                exponent = (a + c, b + d)
                result[exponent] = result.get(exponent, Fraction(0)) + coefficient * other
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def exponentiate(poly: dict[tuple[int, int], Fraction], n: int) -> dict[tuple[int, int], Fraction]:
    result = {(0, 0): Fraction(1)}
    for _ in range(n):
        result = multiply(result, poly)
    return result


def validate(data: dict[str, object]) -> None:
    assert data["schema"] == "hcs-c114-local-jet-koopman-v1"
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    germ = data["frozen_germ"]
    assert germ["formula"] == "F(u,v)=(u^2+(3/2)u-(1/2)v,u)"
    assert germ["fixed_point"] == ["0", "0"]
    assert germ["linearization_matrix"] == [["3/2", "-1/2"], ["1", "0"]]
    assert germ["linearization_eigenvalues"] == ["1", "1/2"]
    assert germ["linearization_determinant"] == "1/2"

    basis = [(0, 0)]
    for degree in range(1, 5):
        basis.extend((degree - j, j) for j in range(degree + 1))
    labels = ["1", "u", "v", "u^2", "u*v", "v^2", "u^3", "u^2*v", "u*v^2", "v^3", "u^4", "u^3*v", "u^2*v^2", "u*v^3", "v^4"]
    algebra = data["local_algebra"]
    assert algebra["definition"] == "A4=Q[u,v]/(u,v)^5"
    assert algebra["maximum_total_degree"] == 4 and algebra["dimension"] == 15
    assert algebra["basis_order"] == labels
    assert algebra["basis_exponents"] == [list(pair) for pair in basis]

    place = {monomial: index for index, monomial in enumerate(basis)}
    first = {(2, 0): Fraction(1), (1, 0): Fraction(3, 2), (0, 1): Fraction(-1, 2)}
    first_linear = {(1, 0): Fraction(3, 2), (0, 1): Fraction(-1, 2)}
    second = {(1, 0): Fraction(1)}

    def build(first_coordinate: dict[tuple[int, int], Fraction]) -> list[list[Fraction]]:
        matrix = [[Fraction(0) for _ in range(15)] for _ in range(15)]
        for column, (i, j) in enumerate(basis):
            image = multiply(exponentiate(first_coordinate, i), exponentiate(second, j))
            for monomial, coefficient in image.items():
                matrix[place[monomial]][column] = coefficient
        return matrix

    expected = build(first)
    linear = build(first_linear)
    operator = data["operator"]
    actual = [[f(value) for value in row] for row in operator["matrix"]]
    actual_linear = [[f(value) for value in row] for row in data["nonlinear_vs_linearized_control"]["linearized_matrix"]]
    assert actual == expected and actual_linear == linear
    canonical_matrix = (json.dumps(operator["matrix"], separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    assert operator["matrix_sha256"] == sha256(canonical_matrix).hexdigest()

    sym = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in actual])
    sym_linear = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in actual_linear])
    lam, z = sp.symbols("lam z")
    char = sp.Poly(sym.charpoly(lam).as_expr(), lam)
    detz = sp.Poly((sp.eye(15) - z * sym).det(), z)
    assert f(operator["trace"]) == Fraction(129, 16)
    assert f(operator["determinant"]) == Fraction(1, 2**20)
    assert operator["characteristic_polynomial_variable"] == "lam"
    assert [sp.sympify(value) for value in operator["characteristic_polynomial_coefficients_descending"]] == char.all_coeffs()
    assert sp.simplify(sp.sympify(operator["characteristic_polynomial_factorization"], locals={"lam": lam}) - char.as_expr()) == 0
    assert [sp.Rational(f(value).numerator, f(value).denominator) for value in operator["det_I_minus_zK_coefficients_ascending"]] == [detz.nth(k) for k in range(16)]
    assert sp.simplify(sp.sympify(operator["det_I_minus_zK_factorization"]) - detz.as_expr()) == 0
    assert operator["eigenvalue_multiplicities"] == {"1": 5, "1/2": 4, "1/4": 3, "1/8": 2, "1/16": 1}
    for n in range(1, 9):
        expected_trace = sum(Fraction(5 - k, 2 ** (k * n)) for k in range(5))
        assert f(operator["trace_powers_n1_to_8"][str(n)]) == expected_trace
        assert sp.trace(sym**n) == sp.Rational(expected_trace.numerator, expected_trace.denominator)

    for degree in range(5):
        positions = [i for i, pair in enumerate(basis) if sum(pair) == degree]
        block = [[actual[i][j] for j in positions] for i in positions]
        reported = data["graded_blocks"][str(degree)]
        assert [[f(value) for value in row] for row in reported["matrix"]] == block
        block_sym = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in block])
        assert f(reported["trace"]) == Fraction(2 ** (degree + 1) - 1, 2**degree)
        assert f(reported["determinant"]) == Fraction(1, 2 ** (degree * (degree + 1) // 2))
        assert [f(value) for value in reported["eigenvalues_with_multiplicity"]] == [Fraction(1, 2**k) for k in range(degree + 1)]
        assert sp.trace(block_sym) == sp.Rational(f(reported["trace"]).numerator, f(reported["trace"]).denominator)

    control = data["nonlinear_vs_linearized_control"]
    difference = sym - sym_linear
    nonzero = [(i, j) for i in range(15) for j in range(15) if difference[i, j] != 0]
    assert control["matrices_are_distinct"] is True and sym != sym_linear
    assert control["strictly_degree_raising_correction"] is True
    assert control["correction_nonzero_entry_count"] == len(nonzero)
    assert all(sum(basis[i]) > sum(basis[j]) for i, j in nonzero)
    nilpotence_index = next(n for n in range(1, 6) if difference**n == sp.zeros(15))
    assert control["correction_nilpotence_index"] == nilpotence_index
    assert control["characteristic_polynomials_match"] is True
    assert char == sp.Poly(sym_linear.charpoly(lam).as_expr(), lam)

    verdict = data["verdict"]
    assert verdict == {
        "A1": "A1_PARTIAL_CERTIFIED",
        "A1_qualification": "LOCAL_FIXED_POINT_AND_ORDER_FOUR_JET_ONLY",
        "A2": "A2_CERTIFIED_PREFIX",
        "A2_qualification": "FIFTEEN_DIMENSIONAL_FINITE_LOCAL_QUOTIENT_ONLY",
        "A3": "A3_NOT_ADDRESSED",
        "A4": "A4_FAIL",
        "overall": "ROUTE_A_EXPLORATORY",
    }
    nonclaims = data["nonclaims"]
    assert len(nonclaims) == 5
    joined = " ".join(nonclaims)
    for phrase in ["global Koopman spectrum", "Fredholm determinant", "Euler factors", "root numbers", "Hilbert--Polya", "Route-B"]:
        assert phrase in joined


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    validate(data)
    print("C114_CHECK_PASS", data["local_algebra"]["dimension"], data["operator"]["matrix_sha256"])


if __name__ == "__main__":
    main()
