#!/usr/bin/env python3
"""Independent symbolic audit of the C209 ledger.

SymPy is used only for exact polynomial arithmetic and cyclotomic remainders;
the producer and finite partition enumerator are not imported.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb, gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c209_kreweras_evidence.json"
q = sp.Symbol("q")


def cat(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def group_order(n: int) -> int:
    return 1 if n == 1 else 2 * n


def actual_order(n: int) -> int:
    return 1 if n == 1 else 2 if n == 2 else 2 * n


def fixed(n: int, d: int) -> int:
    d %= actual_order(n)
    if n == 1:
        return 1
    if d % 2 == 0:
        half = (d // 2) % n
        return cat(n) if half == 0 else comb(2 * gcd(n, half), gcd(n, half))
    return comb(n, (n - 1) // 2) if n % 2 and d == n else 0


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value = n
    sign = 1
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        sign = -sign
    return sign


def qcat(n: int) -> sp.Poly:
    if n == 1:
        return sp.Poly(1, q, domain=sp.ZZ)
    numerator = sp.Poly(1, q, domain=sp.ZZ)
    for j in range(1, 2 * n + 1):
        numerator *= sp.Poly(sum(q**i for i in range(j)), q, domain=sp.ZZ)
    denominator = sp.Poly(1, q, domain=sp.ZZ)
    for j in range(1, n + 1):
        factor = sp.Poly(sum(q**i for i in range(j)), q, domain=sp.ZZ)
        denominator *= factor
    for j in range(1, n + 2):
        factor = sp.Poly(sum(q**i for i in range(j)), q, domain=sp.ZZ)
        denominator *= factor
    quotient, remainder = sp.div(numerator, denominator, domain=sp.ZZ)
    assert remainder.is_zero
    return quotient


def root_value(poly: sp.Poly, order: int) -> int:
    if order == 1:
        return int(poly.eval(1))
    modulus = sp.Poly(sp.cyclotomic_poly(order, q), q, domain=sp.ZZ)
    remainder = poly.rem(modulus)
    assert remainder.degree() <= 0, (order, remainder)
    return int(remainder.eval(0))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0
    by_n = {row["n"]: row for row in data["finite_replay"]["n_rows"]}
    q_rows = {row["n"]: row for row in data["finite_replay"]["q_catalan_rows"]}

    for n in range(1, 13):
        polynomial = qcat(n)
        row = q_rows[n]
        coefficients = [int(polynomial.nth(i)) for i in range(polynomial.degree() + 1)]
        assert coefficients == row["coefficients"]
        assert sum(coefficients) == cat(n)
        digest = sha256(json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest()
        assert digest == row["sha256"]
        assert polynomial.degree() == row["degree"]
        checks += 4
        for d in range(group_order(n)):
            root_order = group_order(n) // gcd(group_order(n), d)
            assert root_value(polynomial, root_order) == fixed(n, d)
            checks += 1

    # Reconstruct all period and spectral rows symbolically from the fixed row.
    for n in range(1, 25):
        L = actual_order(n)
        row = by_n[n]
        periods: dict[int, int] = {}
        for ell in divisors(L):
            value = sum(mobius(ell // d) * fixed(n, d) for d in divisors(ell))
            assert value == next(x for x in data["finite_replay"]["period_rows"] if x["n"] == n and x["period"] == ell)["exact_period_population"]
            assert value >= 0 and value % ell == 0
            periods[ell] = value
            checks += 2
        assert sum(periods.values()) == cat(n)
        for k in range(L):
            multiplicity = sum(periods[ell] // ell for ell in periods if (k * ell) % L == 0)
            stored = next(x for x in data["finite_replay"]["spectral_rows"] if x["n"] == n and x["root_exponent"] == k)
            assert stored["multiplicity"] == multiplicity
            checks += 1
        assert row["cycle_count_total"] == sum(periods[ell] // ell for ell in periods)
        checks += 2

    print(json.dumps({
        "status": "C209_SYMPY_PASS",
        "checks": checks,
        "q_polynomial_n_max": 12,
        "ledger_n_max": 24,
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
