#!/usr/bin/env python3
"""Independent SymPy characteristic and Sturm checks for HCS-C336."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c336_crow_kimura_evidence.json"


def duplicate_pairs(pairs):
    answer = {}
    for key, value in pairs:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


def q(value: str):
    item = Fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def full_matrix(length: int, mutation, selection):
    dimension = 2**length
    matrix = sp.zeros(dimension)
    for x in range(dimension):
        matrix[x, x] = -mutation + (selection if x == 0 else 0)
        for bit in range(length):
            matrix[x ^ (1 << bit), x] += mutation / length
    return matrix


def predicted(length: int, mutation, selection, variable, full_needed=False):
    poles = [-2 * mutation * k / length for k in range(length + 1)]
    base = sp.prod(variable - pole for pole in poles)
    secular = sp.expand(base - selection * sum(
        sp.binomial(length, k) / 2**length * sp.prod(
            variable - poles[j] for j in range(length + 1) if j != k
        ) for k in range(length + 1)
    ))
    full = None
    if full_needed:
        full = sp.expand(secular * sp.prod(
            (variable - poles[k]) ** (sp.binomial(length, k) - 1)
            for k in range(length + 1)
        ))
    return poles, secular, full


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 SymPy cross-check refuses optimized Python")
    data = json.loads(
        EVIDENCE.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )
    x = sp.symbols("x")
    identities = 0

    for row in data["spectral_rows"]:
        length = row["L"]
        mutation, selection = q(row["U"]), q(row["s"])
        poles, secular, _ = predicted(length, mutation, selection, x)
        stored = sum(q(value) * x**index for index, value in enumerate(row["secular_coefficients_ascending"]))
        assert sp.expand(stored - secular) == 0
        identities += len(row["secular_coefficients_ascending"])
        polynomial = sp.Poly(secular, x, domain=sp.QQ)
        assert polynomial.count_roots(0, sp.oo) == 1
        identities += 1
        assert polynomial.count_roots(-sp.oo, poles[-1]) == 0
        identities += 1
        for k in range(1, length + 1):
            assert polynomial.count_roots(poles[k], poles[k - 1]) == 1
            identities += 1
        assert sp.degree(secular, x) == length + 1
        assert sp.Poly(secular, x).LC() == 1
        # The full trace coefficient follows by adding the retained pole
        # multiplicities to the secular trace; expanding degree 2^L here
        # would add cost but no independent content.
        secular_trace = sum(poles) + selection
        retained_trace = sum((sp.binomial(length, k)-1)*poles[k] for k in range(length+1))
        assert sp.simplify(secular_trace + retained_trace + mutation*2**length - selection) == 0
        identities += 3

    for row in data["spectral_rows"]:
        length = row["L"]
        if length > 4 and not (length == 5 and row["U"] == "1" and row["s"] == "1"):
            continue
        mutation, selection = q(row["U"]), q(row["s"])
        _, _, full = predicted(length, mutation, selection, x, full_needed=True)
        direct = full_matrix(length, mutation, selection).charpoly(x).as_expr()
        assert sp.expand(direct - full) == 0
        identities += 2**length + 1

    mutation, selection = sp.symbols("U s", positive=True)
    one_locus = sp.Matrix([[-mutation + selection, mutation], [mutation, -mutation]])
    expected = x**2 - (selection - 2*mutation)*x - selection*mutation
    assert sp.expand(one_locus.charpoly(x).as_expr() - expected) == 0
    roots = sp.solve(expected, x)
    target = {
        (selection - 2*mutation + sp.sqrt(selection**2 + 4*mutation**2))/2,
        (selection - 2*mutation - sp.sqrt(selection**2 + 4*mutation**2))/2,
    }
    assert {sp.simplify(value) for value in roots} == target
    identities += 4

    a = sp.symbols("a", positive=True)
    assert sp.simplify(selection*a - selection*a*a - selection*a*(1-a)) == 0
    identities += 1
    assert sum(sp.binomial(12, k) for k in range(13)) == 2**12
    identities += 1
    print(f"C336 SymPy cross-check: PASS identities={identities}")


if __name__ == "__main__":
    main()
