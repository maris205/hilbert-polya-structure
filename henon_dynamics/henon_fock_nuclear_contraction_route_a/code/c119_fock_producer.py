#!/usr/bin/env python3
"""Produce the exact C119 bosonic-Fock contraction certificate.

The operator in this package is the source-defined second quantization of one
frozen two-dimensional contraction.  It is not asserted to match any external
divisor or arithmetic object.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c119_fock_evidence.json"


def frac(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def determinant_coefficients(traces: dict[int, Fraction], degree: int) -> list[Fraction]:
    """Newton recurrence for det(I-zT) from Tr(T^n)."""
    coefficients = [Fraction(1)]
    for n in range(1, degree + 1):
        coefficients.append(-sum(traces[k] * coefficients[n - k] for k in range(1, n + 1)) / n)
    return coefficients


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    A = sp.Matrix([[sp.Rational(3, 4), sp.Rational(-1, 4)], [sp.Rational(1, 2), 0]])
    lam, u = sp.symbols("lam u")
    char = sp.factor(A.charpoly(lam).as_expr())
    assert sp.expand(char - (lam - sp.Rational(1, 2)) * (lam - sp.Rational(1, 4))) == 0
    gram = A.T * A
    gram_char = sp.factor(gram.charpoly(u).as_expr())
    assert sp.expand(gram_char - (u**2 - sp.Rational(7, 8) * u + sp.Rational(1, 64))) == 0
    singular_squares = [(sp.Integer(7) + sign * 3 * sp.sqrt(5)) / 16 for sign in (1, -1)]
    assert all(sp.simplify(gram_char.subs(u, value)) == 0 for value in singular_squares)
    # 7-3 sqrt(5)>0 follows from 49>45; 7+3 sqrt(5)<16 follows from sqrt(5)<3.
    assert all(0 < float(value) < 1 for value in singular_squares)

    traces: dict[int, Fraction] = {}
    for n in range(1, 9):
        value = Fraction(1, 1) / ((1 - Fraction(1, 2**n)) * (1 - Fraction(1, 4**n)))
        traces[n] = value
    coefficients = determinant_coefficients(traces, 8)
    zero_prefix = [
        {
            "exponent_k": k,
            "zero": str(2**k),
            "multiplicity": k // 2 + 1,
            "index_solutions": [[k - 2 * j, j] for j in range(k // 2 + 1)],
        }
        for k in range(9)
    ]

    payload = {
        "schema": "hcs-c119-fock-nuclear-contraction-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "frozen_map": {
            "formula": "Phi(x,y)=((3/4)x-(1/4)y,(1/2)x)",
            "matrix": [["3/4", "-1/4"], ["1/2", "0"]],
            "characteristic_polynomial": "(lam - 1/2)*(lam - 1/4)",
            "eigenvalues": ["1/2", "1/4"],
            "determinant": "1/8",
            "fixed_points": [["0", "0"]],
            "periodic_point_statement": "the origin is the only finite-period point over C",
            "periodic_point_reason": "Phi^n-I is invertible because neither (1/2)^n nor (1/4)^n equals 1",
        },
        "euclidean_contraction": {
            "A_transpose_A": [["13/16", "-3/16"], ["-3/16", "1/16"]],
            "singular_value_squares_descending": ["(7+3*sqrt(5))/16", "(7-3*sqrt(5))/16"],
            "strict_contraction": True,
            "exact_inequality_certificate": [
                "49>45 implies 7-3*sqrt(5)>0",
                "5<9 implies 7+3*sqrt(5)<16",
            ],
        },
        "fock_owner": {
            "space": "F_s(C^2)=direct_sum_{m>=0} Sym^m(C^2)",
            "operator": "Gamma(A)=direct_sum_{m>=0} Sym^m(A)",
            "degree_m_eigenvalues": "(1/2)^i*(1/4)^j for i+j=m",
            "all_eigenvalues_with_algebraic_multiplicity": "2^(-i)*4^(-j) for i,j>=0",
            "singular_values": "s_1^i*s_2^j for i,j>=0",
            "trace_class": True,
            "trace_norm_formula": "1/((1-s_1)*(1-s_2))",
            "trace_class_reason": "s_1,s_2<1 and the double geometric sum of singular values converges",
        },
        "trace_and_fredholm_data": {
            "trace_formula": "Tr(Gamma(A)^n)=1/((1-2^(-n))*(1-4^(-n)))",
            "trace_powers_n1_to_8": {str(n): frac(traces[n]) for n in range(1, 9)},
            "fredholm_determinant_definition": "D(z)=det(I-z*Gamma(A))",
            "fredholm_product": "product_{i,j>=0}(1-z*2^(-i)*4^(-j))",
            "entire_genus_zero": True,
            "taylor_coefficients_ascending_z0_to_z8": [frac(value) for value in coefficients],
            "coefficient_recurrence": "n*d_n=-sum_{k=1}^n Tr(Gamma(A)^k)*d_(n-k)",
        },
        "zero_divisor": {
            "complete_description": "zeros are z=2^k for k>=0 with multiplicity floor(k/2)+1",
            "derivation": "i+2*j=k has floor(k/2)+1 nonnegative integer solutions",
            "prefix_k0_to_8": zero_prefix,
        },
        "verdict": {
            "A1": "A1_FAIL",
            "A1_qualification": "CONTRACTION_HAS_ONLY_THE_ORIGIN_AS_A_PERIODIC_POINT",
            "A2": "A2_FAIL",
            "A2_qualification": "FOCK_DETERMINANT_IS_NOT_PRIMITIVE_ORBIT_OWNED_AND_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_COUNTING_OR_CONTINUATION_CHECKS",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "a nontrivial primitive-orbit atlas or orbit-derived determinant",
            "matching of the source-defined Fock zero divisor to any target divisor",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator or Riemann-zero correspondence",
            "Route-B authorization or resolution of the larger program",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(raw)
    print(json.dumps({
        "status": "C119_PREFREEZE_G3_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "trace_count": len(traces),
        "determinant_coefficient_count": len(coefficients),
        "zero_prefix_count": len(zero_prefix),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
