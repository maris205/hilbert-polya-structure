#!/usr/bin/env python3
"""Independent SymPy quotient-algebra and resultant cross-check for C141."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c141_quadratic_ruelle_evidence.json"


def quotient_multiplication_trace(poly: sp.Poly, modulus: sp.Poly) -> sp.Rational:
    x = modulus.gens[0]
    inverse = sp.invert(poly, modulus)
    degree = modulus.degree()
    total = sp.Rational(0)
    for j in range(degree):
        image = sp.rem(sp.Poly(inverse * x**j, x, domain=sp.QQ), modulus)
        total += image.nth(j)
    return sp.factor(total)


def q(text: str) -> sp.Rational:
    a, b = text.split("/")
    return sp.Rational(int(a), int(b))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    x, t = sp.symbols("x t")
    iterate = x
    traces = []
    checks = 0
    for n, row in enumerate(data["headline_exact_prefix"]["periods"], 1):
        iterate = sp.expand(iterate**2 - 6)
        periodic = sp.Poly(iterate - x, x, domain=sp.QQ)
        multiplier = sp.Poly(sp.diff(iterate, x), x, domain=sp.QQ)
        denominator = multiplier * (multiplier - sp.Poly(1, x, domain=sp.QQ))
        trace = quotient_multiplication_trace(denominator, periodic)
        traces.append(trace)
        assert periodic.degree() == 2**n; checks += 1
        assert periodic.all_coeffs()[::-1] == row["periodic_polynomial_coefficients_low_to_high"]; checks += 1
        assert trace == q(row["trace_L2_power"]); checks += 1
        # The same quotient algebra proves the exact m=0/1 control identities.
        m1 = quotient_multiplication_trace(multiplier - sp.Poly(1, x, domain=sp.QQ), periodic)
        m0 = periodic.degree() + m1
        assert m1 == 0; checks += 1
        assert m0 == 2**n; checks += 1
        if n <= 3:
            # A second SymPy route: resultant logarithmic derivative at t=0.
            resultant = sp.resultant(periodic.as_expr(), denominator.as_expr() - t, x)
            root_sum = -sp.diff(resultant, t).subs(t, 0) / resultant.subs(t, 0)
            assert sp.factor(root_sum) == trace; checks += 1

    coeffs = [sp.Rational(1)]
    for n in range(1, 7):
        coeffs.append(-sum(coeffs[n-j] * traces[j-1] for j in range(1, n+1)) / n)
    expected = [q(v) for v in data["headline_exact_prefix"]["fredholm_coefficients_c0_through_c6"]]
    assert coeffs == expected; checks += 1

    assert sp.simplify(2 * (sp.Rational(1, 8)) / (1 - sp.sqrt(10) / 4) - 1/(4-sp.sqrt(10))) == 0; checks += 1
    qbound = 1/(2*sp.sqrt(2))
    assert sp.simplify(2**sp.Symbol("n", integer=True, positive=True) * qbound**(2*sp.Symbol("n", integer=True, positive=True)) - sp.Rational(1,4)**sp.Symbol("n", integer=True, positive=True)) == 0; checks += 1
    assert sum(row["rooted_inverse_words"] for row in data["headline_exact_prefix"]["periods"]) == 126; checks += 1
    assert [row["primitive_orbits"] for row in data["headline_exact_prefix"]["periods"]] == [2, 1, 2, 3, 6, 9]; checks += 1
    print(f"C141 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
