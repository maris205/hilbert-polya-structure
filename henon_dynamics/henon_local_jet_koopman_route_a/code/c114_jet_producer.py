#!/usr/bin/env python3
"""Produce the exact C114 order-four local Koopman-jet ledger.

The calculation is intentionally local and finite.  It constructs the
pullback of the frozen polynomial germ on Q[u,v]/(u,v)^5.  Nothing in this
script promotes that quotient to a global or nuclear transfer operator.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c114_jet_evidence.json"
MAX_DEGREE = 4


def add(p: dict[tuple[int, int], Fraction], q: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out = dict(p)
    for monomial, coefficient in q.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def mul(p: dict[tuple[int, int], Fraction], q: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            if i + j + k + ell <= MAX_DEGREE:
                key = (i + k, j + ell)
                out[key] = out.get(key, Fraction(0)) + a * b
    return {key: value for key, value in out.items() if value}


def power(p: dict[tuple[int, int], Fraction], exponent: int) -> dict[tuple[int, int], Fraction]:
    out = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        out = mul(out, p)
    return out


def frac(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def label(pair: tuple[int, int]) -> str:
    i, j = pair
    if i == j == 0:
        return "1"
    pieces = []
    if i:
        pieces.append("u" if i == 1 else f"u^{i}")
    if j:
        pieces.append("v" if j == 1 else f"v^{j}")
    return "*".join(pieces)


def matrix_strings(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[frac(value) for value in row] for row in matrix]


def polynomial_product(factors: list[list[Fraction]]) -> list[Fraction]:
    out = [Fraction(1)]
    for factor in factors:
        nxt = [Fraction(0)] * (len(out) + len(factor) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(factor):
                nxt[i + j] += a * b
        out = nxt
    return out


def main() -> None:
    basis = [(i, degree - i) for degree in range(MAX_DEGREE + 1) for i in range(degree, -1, -1)]
    # The preceding comprehension deliberately gives u^degree,...,v^degree.
    # Its tuple is (u exponent, v exponent).
    assert basis == [
        (0, 0),
        (1, 0), (0, 1),
        (2, 0), (1, 1), (0, 2),
        (3, 0), (2, 1), (1, 2), (0, 3),
        (4, 0), (3, 1), (2, 2), (1, 3), (0, 4),
    ]
    index = {monomial: position for position, monomial in enumerate(basis)}

    u = {(1, 0): Fraction(1)}
    v = {(0, 1): Fraction(1)}
    U = add(add(mul(u, u), {(1, 0): Fraction(3, 2)}), {(0, 1): Fraction(-1, 2)})
    V = u
    U_linear = {(1, 0): Fraction(3, 2), (0, 1): Fraction(-1, 2)}

    def koopman_matrix(first_coordinate: dict[tuple[int, int], Fraction]) -> list[list[Fraction]]:
        matrix = [[Fraction(0) for _ in basis] for _ in basis]
        for column, (i, j) in enumerate(basis):
            image = mul(power(first_coordinate, i), power(V, j))
            for monomial, coefficient in image.items():
                matrix[index[monomial]][column] = coefficient
        return matrix

    matrix = koopman_matrix(U)
    linear_control = koopman_matrix(U_linear)
    assert any(matrix[i][j] != linear_control[i][j] for i in range(15) for j in range(15))

    graded_blocks: dict[str, object] = {}
    block_traces: list[Fraction] = []
    block_determinants: list[Fraction] = []
    for degree in range(MAX_DEGREE + 1):
        positions = [i for i, monomial in enumerate(basis) if sum(monomial) == degree]
        block = [[matrix[i][j] for j in positions] for i in positions]
        block_control = [[linear_control[i][j] for j in positions] for i in positions]
        assert block == block_control
        sym_block = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in block])
        trace = Fraction(int(sp.numer(sp.trace(sym_block))), int(sp.denom(sp.trace(sym_block))))
        determinant = sp.factor(sym_block.det())
        determinant_fraction = Fraction(int(sp.numer(determinant)), int(sp.denom(determinant)))
        expected_eigenvalues = [Fraction(1, 2**k) for k in range(degree + 1)]
        block_traces.append(trace)
        block_determinants.append(determinant_fraction)
        graded_blocks[str(degree)] = {
            "basis": [label(basis[i]) for i in positions],
            "matrix": matrix_strings(block),
            "trace": frac(trace),
            "determinant": frac(determinant_fraction),
            "eigenvalues_with_multiplicity": [frac(value) for value in expected_eigenvalues],
        }

    sym_matrix = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in matrix])
    sym_linear = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in linear_control])
    lam, z = sp.symbols("lam z")
    characteristic = sp.Poly(sym_matrix.charpoly(lam).as_expr(), lam)
    control_characteristic = sp.Poly(sym_linear.charpoly(lam).as_expr(), lam)
    assert characteristic == control_characteristic
    det_i_minus_zk = sp.Poly(sp.expand((sp.eye(15) - z * sym_matrix).det()), z)

    eigenvalue_multiplicities = {frac(Fraction(1, 2**k)): MAX_DEGREE + 1 - k for k in range(MAX_DEGREE + 1)}
    expected_det_factors: list[list[Fraction]] = []
    for k in range(MAX_DEGREE + 1):
        expected_det_factors.extend([[Fraction(1), Fraction(-1, 2**k)]] * (MAX_DEGREE + 1 - k))
    expected_det_coefficients = polynomial_product(expected_det_factors)
    actual_det_coefficients = [
        Fraction(int(sp.numer(det_i_minus_zk.nth(k))), int(sp.denom(det_i_minus_zk.nth(k))))
        for k in range(16)
    ]
    assert expected_det_coefficients == actual_det_coefficients

    trace_powers = {}
    for n in range(1, 9):
        value = sum(Fraction(MAX_DEGREE + 1 - k, 2 ** (k * n)) for k in range(MAX_DEGREE + 1))
        assert sp.trace(sym_matrix**n) == sp.Rational(value.numerator, value.denominator)
        trace_powers[str(n)] = frac(value)

    correction = [[matrix[i][j] - linear_control[i][j] for j in range(15)] for i in range(15)]
    correction_nonzero = [(i, j, correction[i][j]) for i in range(15) for j in range(15) if correction[i][j]]
    assert correction_nonzero
    assert all(sum(basis[i]) > sum(basis[j]) for i, j, _ in correction_nonzero)
    correction_sym = sym_matrix - sym_linear
    nilpotence_index = next(power_index for power_index in range(1, 6) if correction_sym**power_index == sp.zeros(15))

    matrix_payload = matrix_strings(matrix)
    matrix_bytes = (json.dumps(matrix_payload, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    payload = {
        "schema": "hcs-c114-local-jet-koopman-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "frozen_germ": {
            "formula": "F(u,v)=(u^2+(3/2)u-(1/2)v,u)",
            "fixed_point": ["0", "0"],
            "linearization_matrix": [["3/2", "-1/2"], ["1", "0"]],
            "linearization_eigenvalues": ["1", "1/2"],
            "linearization_determinant": "1/2",
        },
        "local_algebra": {
            "definition": "A4=Q[u,v]/(u,v)^5",
            "maximum_total_degree": 4,
            "dimension": 15,
            "basis_order": [label(item) for item in basis],
            "basis_exponents": [[i, j] for i, j in basis],
        },
        "operator": {
            "definition": "K[p]=[p composed with F] modulo (u,v)^5",
            "matrix_convention": "column j contains K applied to basis element j",
            "matrix": matrix_payload,
            "matrix_sha256": sha256(matrix_bytes).hexdigest(),
            "trace": frac(sum(block_traces, Fraction(0))),
            "determinant": frac(Fraction(int(sp.numer(sym_matrix.det())), int(sp.denom(sym_matrix.det())))),
            "trace_powers_n1_to_8": trace_powers,
            "characteristic_polynomial_variable": "lam",
            "characteristic_polynomial_factorization": sp.sstr(sp.factor(characteristic.as_expr())),
            "characteristic_polynomial_coefficients_descending": [sp.sstr(value) for value in characteristic.all_coeffs()],
            "det_I_minus_zK_factorization": sp.sstr(sp.factor(det_i_minus_zk.as_expr())),
            "det_I_minus_zK_coefficients_ascending": [frac(value) for value in actual_det_coefficients],
            "eigenvalue_multiplicities": eigenvalue_multiplicities,
        },
        "graded_blocks": graded_blocks,
        "nonlinear_vs_linearized_control": {
            "linearized_matrix": matrix_strings(linear_control),
            "matrices_are_distinct": True,
            "strictly_degree_raising_correction": True,
            "correction_nonzero_entry_count": len(correction_nonzero),
            "correction_nilpotence_index": nilpotence_index,
            "characteristic_polynomials_match": True,
            "reason": "the nonlinear u^2 term contributes only to strictly higher total-degree rows",
        },
        "verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A1_qualification": "LOCAL_FIXED_POINT_AND_ORDER_FOUR_JET_ONLY",
            "A2": "A2_CERTIFIED_PREFIX",
            "A2_qualification": "FIFTEEN_DIMENSIONAL_FINITE_LOCAL_QUOTIENT_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "global orbit classification, Markov partition, or complete primitive-orbit atlas",
            "global Koopman spectrum, invariant Banach space, nuclearity, or Fredholm determinant",
            "analytic continuation, zero-count theorem, or spectral correspondence",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    OUT.write_text(raw)
    print(
        json.dumps(
            {
                "status": "C114_PREFREEZE_G3_PASS",
                "dimension": 15,
                "evidence_sha256": sha256(raw.encode()).hexdigest(),
                "matrix_sha256": payload["operator"]["matrix_sha256"],
                "trace": payload["operator"]["trace"],
                "determinant": payload["operator"]["determinant"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
