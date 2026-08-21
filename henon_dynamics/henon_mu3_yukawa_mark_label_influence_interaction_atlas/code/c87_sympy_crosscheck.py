#!/usr/bin/env python3
"""SymPy multilinear and finite-enumeration cross-check for C87."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import factorial
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c87_label_influence_interaction_atlas_evidence.json"
LABELS = tuple(f"S{index}" for index in range(1, 17))
BLOCKS = ((0,), (15,), (6, 14), (2, 3, 7, 10, 11))
PIVOT = 8


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def derivative(expression: sp.Expr, variables: tuple[sp.Symbol, ...], indices: tuple[int, ...]) -> sp.Expr:
    result = expression
    for index in indices:
        result = sp.expand(result.subs(variables[index], 1) - result.subs(variables[index], 0))
    return sp.expand(result)


def coalition_enumerator(
    expression: sp.Expr,
    variables: tuple[sp.Symbol, ...],
    excluded: tuple[int, ...],
    marker: sp.Symbol,
) -> sp.Poly:
    remaining = [variable for index, variable in enumerate(variables) if index not in excluded]
    polynomial = sp.Poly(expression, *remaining)
    total = sp.Integer(0)
    dimension = len(remaining)
    for powers, coefficient in polynomial.terms():
        degree = sum(powers)
        assert all(power in (0, 1) for power in powers)
        total += coefficient * marker ** degree * (1 + marker) ** (dimension - degree)
    return sp.Poly(sp.expand(total), marker)


def coefficients(polynomial: sp.Poly, maximum: int) -> list[int]:
    return [int(polynomial.nth(index)) for index in range(maximum + 1)]


def predicate(mask: int) -> int:
    return int(bool(mask & (1 << PIVOT)) and sum(any(mask & (1 << index) for index in block) for block in BLOCKS) >= 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    evidence = json.loads(args.evidence.read_text())
    first_rows = evidence["first_order_atlas"]["rows"]
    pair_rows = evidence["second_order_atlas"]["rows"]
    pair_lookup = {tuple(LABELS.index(label) for label in row["pair"]): row for row in pair_rows}

    variables = sp.symbols("x1:17")
    marker = sp.symbols("z")
    hit = [1 - sp.prod(1 - variables[index] for index in block) for block in BLOCKS]
    fewer_than_two = sp.prod(1 - value for value in hit)
    fewer_than_two += sum(
        hit[index] * sp.prod(1 - hit[other] for other in range(4) if other != index)
        for index in range(4)
    )
    boolean_polynomial = sp.Poly(sp.expand(variables[PIVOT] * (1 - fewer_than_two)), *variables)
    assert boolean_polynomial.total_degree() == 10
    assert all(all(power in (0, 1) for power in powers) for powers, _ in boolean_polynomial.terms())
    assert all(boolean_polynomial.degree(variables[index]) == 0 for index in (1, 4, 5, 9, 12, 13))

    truth = [predicate(mask) for mask in range(1 << 16)]
    polynomial_terms = [
        (tuple(index for index, power in enumerate(powers) if power), int(coefficient))
        for powers, coefficient in boolean_polynomial.terms()
    ]
    for mask in range(1 << 16):
        value = sum(
            coefficient
            for support, coefficient in polynomial_terms
            if all(mask & (1 << index) for index in support)
        )
        assert value == truth[mask]

    for index, row in enumerate(first_rows):
        symbolic = coalition_enumerator(
            derivative(boolean_polynomial.as_expr(), variables, (index,)),
            variables,
            (index,),
            marker,
        )
        vector = coefficients(symbolic, 15)
        assert vector == row["coalition_size_swing_counts"]
        assert sum(vector) == row["swing_count"]
        shapley = sum(
            Fraction(count * factorial(size) * factorial(15 - size), factorial(16))
            for size, count in enumerate(vector)
        )
        assert fraction_text(shapley) == row["shapley_shubik_value"]

    for pair in combinations(range(16), 2):
        row = pair_lookup[pair]
        symbolic = coalition_enumerator(
            derivative(boolean_polynomial.as_expr(), variables, pair),
            variables,
            pair,
            marker,
        )
        signed = coefficients(symbolic, 14)
        assert signed == row["signed_delta_by_coalition_size"]
        positive = [0] * 15
        negative = [0] * 15
        both = (1 << pair[0]) | (1 << pair[1])
        for coalition in range(1 << 16):
            if coalition & both:
                continue
            delta = truth[coalition | both] + truth[coalition]
            delta -= truth[coalition | (1 << pair[0])] + truth[coalition | (1 << pair[1])]
            if delta > 0:
                positive[coalition.bit_count()] += 1
            elif delta < 0:
                negative[coalition.bit_count()] += 1
        assert positive == row["positive_delta_by_coalition_size"]
        assert negative == row["negative_delta_by_coalition_size"]
        signed_sum = sum(signed)
        assert fraction_text(Fraction(signed_sum, 2 ** 14)) == row["uniform_banzhaf_interaction"]
        shapley = sum(
            Fraction(count * factorial(size) * factorial(14 - size), factorial(15))
            for size, count in enumerate(signed)
        )
        assert fraction_text(shapley) == row["shapley_pair_interaction"]

    print(json.dumps({
        "status": "C87_SYMPY_FINITE_CROSSCHECK_PASS",
        "multilinear_degree": boolean_polynomial.total_degree(),
        "multilinear_term_count": len(boolean_polynomial.terms()),
        "truth_table_rows": len(truth),
        "first_derivatives_checked": len(first_rows),
        "second_derivatives_checked": len(pair_rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
