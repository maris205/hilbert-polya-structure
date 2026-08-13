#!/usr/bin/env python3
"""Exact finite sentinels for the all-period C46 integrality theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT / "results" / "c46_certificate.json"


def cyclic_relations(symbols: tuple[sp.Symbol, ...]) -> list[sp.Expr]:
    n = len(symbols)
    if n == 1:
        return [symbols[0] ** 2 + 2 * symbols[0] - 6]
    if n == 2:
        return [symbols[0] ** 2 + 2 * symbols[1] - 6, symbols[1] ** 2 + 2 * symbols[0] - 6]
    return [symbols[i] ** 2 + symbols[(i - 1) % n] + symbols[(i + 1) % n] - 6 for i in range(n)]


def monodromy_trace(symbols: tuple[sp.Symbol, ...]) -> sp.Expr:
    matrix = sp.eye(2)
    for coordinate in symbols:
        matrix = sp.Matrix([[-2 * coordinate, -1], [1, 0]]) * matrix
    return sp.expand(matrix.trace())


def period_record(period: int) -> dict[str, object]:
    symbols = sp.symbols(f"x0:{period}")
    relations = cyclic_relations(symbols)
    basis = sp.groebner(relations, *symbols, order="grlex", domain=sp.ZZ)
    leading = [list(poly.LM(order=basis.order).exponents) for poly in basis.polys]
    expected = [[int(i == j) * 2 for i in range(period)] for j in range(period)]
    if sorted(leading) != sorted(expected):
        raise ArithmeticError(f"unexpected leading monomials at period {period}")
    trace = monodromy_trace(symbols)
    reduced = sp.expand(basis.reduce(trace)[1])
    polynomial = sp.Poly(reduced, *symbols, domain=sp.ZZ)
    squarefree_basis = all(all(exponent <= 1 for exponent in monomial) for monomial, _ in polynomial.terms())
    if not squarefree_basis:
        raise ArithmeticError("trace did not reduce to the integral square-free basis")
    return {
        "period": period,
        "fixed_algebra_rank": 2**period,
        "groebner_leading_monomials": leading,
        "trace_term_count": len(polynomial.terms()),
        "trace_total_degree": polynomial.total_degree(),
        "trace_reduced": str(reduced),
        "integer_coefficients": all(coefficient.q == 1 for _, coefficient in polynomial.terms()),
    }


def fixed_multiplier_polynomial() -> sp.Poly:
    X = sp.symbols("X")
    root7 = sp.sqrt(7)
    traces = (2 + 2 * root7, 2 - 2 * root7)
    expression = sp.expand((X**2 - traces[0] * X + 1) * (X**2 - traces[1] * X + 1))
    return sp.Poly(expression, X, domain=sp.ZZ)


def build_certificate(max_period: int = 10) -> dict[str, object]:
    if max_period < 3 or max_period > 12:
        raise ValueError("max-period must lie in [3,12]")
    rows = [period_record(period) for period in range(1, max_period + 1)]
    fixed_poly = fixed_multiplier_polynomial()
    expected = [1, -4, -22, -4, 1]
    if fixed_poly.all_coeffs() != expected:
        raise ArithmeticError("fixed multiplier polynomial mismatch")
    payload = {
        "candidate_id": "HCS-C46",
        "coordinate_scaling": "x_i=6*q_i",
        "cyclic_equation": "x_i^2+x_(i-1)+x_(i+1)-6=0",
        "monodromy_step": "[[-2*x_i,-1],[1,0]]",
        "all_period_theorem": {
            "fixed_algebra": "finite free over Z of rank 2^n",
            "trace": "algebraic integer",
            "multiplier": "algebraic unit",
            "status": "PROVED",
        },
        "finite_rows": rows,
        "fixed_multiplier_polynomial": [int(value) for value in fixed_poly.all_coeffs()],
        "status": "PROVED_ALL_PERIOD_INTEGRAL_MONODROMY_UNIT_THEOREM",
        "claim_boundary": "does not classify the pressure power |Lambda|^h_star",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=10)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_certificate(args.max_period)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "periods": args.max_period, "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
