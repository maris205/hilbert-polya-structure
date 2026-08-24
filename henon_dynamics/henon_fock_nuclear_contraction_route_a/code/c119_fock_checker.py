#!/usr/bin/env python3
"""Independent checker for C119; deliberately imports no producer code."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c119_fock_evidence.json"


def q(text: str) -> Fraction:
    return Fraction(text)


def validate(data: dict) -> None:
    assert data["schema"] == "hcs-c119-fock-nuclear-contraction-v1"
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    frozen = data["frozen_map"]
    assert frozen["formula"] == "Phi(x,y)=((3/4)x-(1/4)y,(1/2)x)"
    assert frozen["matrix"] == [["3/4", "-1/4"], ["1/2", "0"]]
    A = sp.Matrix([[sp.Rational(q(v).numerator, q(v).denominator) for v in row] for row in frozen["matrix"]])
    lam, u = sp.symbols("lam u")
    assert sp.expand(A.charpoly(lam).as_expr() - (lam - sp.Rational(1, 2)) * (lam - sp.Rational(1, 4))) == 0
    assert frozen["characteristic_polynomial"] == "(lam - 1/2)*(lam - 1/4)"
    assert frozen["eigenvalues"] == ["1/2", "1/4"]
    assert q(frozen["determinant"]) == Fraction(1, 8) and A.det() == sp.Rational(1, 8)
    assert frozen["fixed_points"] == [["0", "0"]]
    assert frozen["periodic_point_statement"] == "the origin is the only finite-period point over C"
    for n in range(1, 17):
        assert (A**n - sp.eye(2)).det() != 0

    contraction = data["euclidean_contraction"]
    gram = A.T * A
    assert contraction["A_transpose_A"] == [["13/16", "-3/16"], ["-3/16", "1/16"]]
    assert gram == sp.Matrix([[sp.Rational(13, 16), sp.Rational(-3, 16)], [sp.Rational(-3, 16), sp.Rational(1, 16)]])
    roots = [(sp.Integer(7) + 3 * sp.sqrt(5)) / 16, (sp.Integer(7) - 3 * sp.sqrt(5)) / 16]
    assert contraction["singular_value_squares_descending"] == ["(7+3*sqrt(5))/16", "(7-3*sqrt(5))/16"]
    assert sorted(gram.eigenvals(), key=lambda x: float(x), reverse=True) == roots
    assert contraction["strict_contraction"] is True
    assert len(contraction["exact_inequality_certificate"]) == 2
    assert all(0 < float(root) < 1 for root in roots)

    owner = data["fock_owner"]
    assert owner == {
        "space": "F_s(C^2)=direct_sum_{m>=0} Sym^m(C^2)",
        "operator": "Gamma(A)=direct_sum_{m>=0} Sym^m(A)",
        "degree_m_eigenvalues": "(1/2)^i*(1/4)^j for i+j=m",
        "all_eigenvalues_with_algebraic_multiplicity": "2^(-i)*4^(-j) for i,j>=0",
        "singular_values": "s_1^i*s_2^j for i,j>=0",
        "trace_class": True,
        "trace_norm_formula": "1/((1-s_1)*(1-s_2))",
        "trace_class_reason": "s_1,s_2<1 and the double geometric sum of singular values converges",
    }

    reported = data["trace_and_fredholm_data"]
    traces: dict[int, Fraction] = {}
    for n in range(1, 9):
        traces[n] = Fraction(1, 1) / ((1 - Fraction(1, 2**n)) * (1 - Fraction(1, 4**n)))
        assert q(reported["trace_powers_n1_to_8"][str(n)]) == traces[n]
        assert sp.simplify(1 / ((1 - sp.Rational(1, 2) ** n) * (1 - sp.Rational(1, 4) ** n)) - sp.Rational(traces[n].numerator, traces[n].denominator)) == 0
    coefficients = [Fraction(1)]
    for n in range(1, 9):
        coefficients.append(-sum(traces[k] * coefficients[n-k] for k in range(1, n+1)) / n)
    assert [q(value) for value in reported["taylor_coefficients_ascending_z0_to_z8"]] == coefficients
    assert reported["fredholm_product"] == "product_{i,j>=0}(1-z*2^(-i)*4^(-j))"
    assert reported["entire_genus_zero"] is True

    divisor = data["zero_divisor"]
    assert divisor["complete_description"] == "zeros are z=2^k for k>=0 with multiplicity floor(k/2)+1"
    assert len(divisor["prefix_k0_to_8"]) == 9
    for k, row in enumerate(divisor["prefix_k0_to_8"]):
        solutions = [[k - 2*j, j] for j in range(k // 2 + 1)]
        assert row == {"exponent_k": k, "zero": str(2**k), "multiplicity": k // 2 + 1, "index_solutions": solutions}

    assert data["verdict"] == {
        "A1": "A1_FAIL",
        "A1_qualification": "CONTRACTION_HAS_ONLY_THE_ORIGIN_AS_A_PERIODIC_POINT",
        "A2": "A2_FAIL",
        "A2_qualification": "FOCK_DETERMINANT_IS_NOT_PRIMITIVE_ORBIT_OWNED_AND_HAS_NO_TARGET_DIVISOR_MATCH",
        "A3": "A3_FAIL",
        "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_COUNTING_OR_CONTINUATION_CHECKS",
        "A4": "A4_FAIL",
        "overall": "ROUTE_A_EXPLORATORY",
    }
    nonclaims = data["nonclaims"]
    assert len(nonclaims) == 5
    joined = " ".join(nonclaims)
    for phrase in ["target divisor", "Euler factors", "root numbers", "Hilbert--Polya", "Route-B"]:
        assert phrase in joined


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    raw = path.read_bytes()
    data = json.loads(raw)
    validate(data)
    print("C119_CHECK_PASS", sha256(raw).hexdigest(), 8, 9)


if __name__ == "__main__":
    main()
