#!/usr/bin/env python3
"""Separate SymPy cyclotomic reconstruction for HCS-C187."""
from __future__ import annotations

from functools import lru_cache
import json
from math import factorial, gcd, prod
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c187_tableau_csp_evidence.json"
q, z = sp.symbols("q z")


def divisors(n: int) -> list[int]:
    return list(sp.divisors(n))


def hooks(a: int, b: int) -> list[int]:
    return [a + b - row - column - 1 for row in range(a) for column in range(b)]


@lru_cache(maxsize=None)
def q_integer(n: int) -> sp.Poly:
    return sp.Poly(sum(q**power for power in range(n)), q, domain=sp.ZZ)


@lru_cache(maxsize=None)
def q_factorial(n: int) -> sp.Poly:
    answer = sp.Poly(1, q, domain=sp.ZZ)
    for value in range(1, n + 1):
        answer *= q_integer(value)
    return answer


def q_hook(a: int, b: int) -> sp.Poly:
    denominator = sp.Poly(1, q, domain=sp.ZZ)
    for hook in hooks(a, b):
        denominator *= q_integer(hook)
    answer, residual = sp.div(q_factorial(a * b), denominator, domain=sp.ZZ)
    assert residual.is_zero
    return answer


def ascending(poly: sp.Poly) -> list[int]:
    return [int(poly.nth(index)) for index in range(poly.degree() + 1)]


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    finite = data["finite_replay"]
    rectangles = {(row["a"], row["b"]): row for row in finite["rectangles"]}
    iterates = {(row["a"], row["b"], row["iterate"]): row for row in finite["iterate_rows"]}
    periods = {(row["a"], row["b"], row["period"]): row for row in finite["period_rows"]}
    spectra = {(row["a"], row["b"], row["root_exponent_mod_n"]): row for row in finite["spectral_rows"]}
    checks = 0

    for a in range(1, 7):
        for b in range(1, 7):
            n = a * b
            row = rectangles[(a, b)]
            polynomial = q_hook(a, b)
            coefficients = ascending(polynomial)
            assert coefficients == row["q_hook_coefficients"]
            checks += 1
            assert int(polynomial.eval(1)) == row["tableau_count"]
            checks += 1
            assert polynomial.degree() == row["q_hook_degree"]
            checks += 1
            assert row["tableau_count"] == factorial(n) // prod(hooks(a, b))
            checks += 1

            factorization = sp.factor_list(polynomial.as_expr(), q)[1]
            recovered: dict[str, int] = {}
            for factor, exponent in factorization:
                factor_poly = sp.Poly(factor, q, domain=sp.QQ).monic()
                matched = None
                for order in range(2, n + 1):
                    candidate = sp.Poly(sp.cyclotomic_poly(order, q), q, domain=sp.QQ).monic()
                    if factor_poly.all_coeffs() == candidate.all_coeffs():
                        matched = order
                        break
                assert matched is not None
                recovered[str(matched)] = int(exponent)
                checks += 1
            assert recovered == row["q_hook_cyclotomic_exponents"]
            checks += 1

            fixed = {}
            for power in range(n):
                order = n // gcd(n, power)
                if order == 1:
                    value = int(polynomial.eval(1))
                else:
                    modulus = sp.Poly(sp.cyclotomic_poly(order, q), q, domain=sp.ZZ)
                    residual = sp.rem(polynomial, modulus, domain=sp.ZZ)
                    assert residual.degree() <= 0
                    value = int(residual.nth(0))
                    checks += 1
                item = iterates[(a, b, power)]
                assert value == item["fixed_count"]
                checks += 1
                assert item["root_order"] == order
                checks += 1
                fixed[power] = value

            cycle_counts = {}
            for period in divisors(n):
                exact = sum(
                    int(sp.mobius(period // d)) * (row["tableau_count"] if d == n else fixed[d])
                    for d in divisors(period)
                )
                item = periods[(a, b, period)]
                assert item["exact_period_count"] == exact
                checks += 1
                assert exact % period == 0 and item["cycle_count"] == exact // period
                checks += 1
                cycle_counts[period] = exact // period
            assert sum(period * count for period, count in cycle_counts.items()) == row["tableau_count"]
            checks += 1

            for power in range(n):
                trace = sum(period * count for period, count in cycle_counts.items() if power % period == 0)
                assert trace == fixed[power]
                checks += 1

            spectral_total = 0
            for exponent in range(n):
                multiplicity = sum(
                    count for period, count in cycle_counts.items()
                    if exponent * period % n == 0
                )
                assert spectra[(a, b, exponent)]["multiplicity"] == multiplicity
                checks += 1
                spectral_total += multiplicity
            assert spectral_total == row["tableau_count"]
            checks += 1

            if row["tableau_count"] <= 500:
                determinant = sp.Poly(1, z, domain=sp.ZZ)
                for period, count in cycle_counts.items():
                    determinant *= sp.Poly((1 - z**period) ** count, z, domain=sp.ZZ)
                assert determinant.degree() == row["tableau_count"]
                checks += 1
                assert determinant.nth(0) == 1
                checks += 1

            if a == 1 or b == 1:
                assert polynomial == sp.Poly(1, q, domain=sp.ZZ)
                checks += 1
                assert row["actual_promotion_order"] == 1
                checks += 1

    assert rectangles[(2, 2)]["actual_promotion_order"] == 2
    checks += 1
    assert rectangles[(2, 2)]["q_hook_coefficients"] == [1, 0, 1]
    checks += 1
    print(json.dumps({"status": "C187_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
