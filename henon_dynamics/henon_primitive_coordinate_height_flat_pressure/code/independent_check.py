#!/usr/bin/env python3
"""Independent finite checks for HCS-P63."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c63_certificate.json"
OUTPUT = PROJECT / "results" / "c63_independent_check.json"
X, T = sp.symbols("X T")


def canonical_sha(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def independent_quotients(max_period: int = 9) -> dict[int, sp.Poly]:
    q0 = X
    q1 = (1 - 6 * X**2) / 2
    coordinates = [sp.expand(q0), sp.expand(q1)]
    quotients: dict[int, sp.Poly] = {}
    for n in range(1, max_period + 1, 2):
        m = (n - 1) // 2
        while len(coordinates) <= m + 1:
            coordinates.append(sp.expand(1 - 6 * coordinates[-1] ** 2 - coordinates[-2]))
        closure = sp.Poly(coordinates[m + 1] - coordinates[m], X, domain=sp.QQ).monic()
        product = sp.Poly(1, X, domain=sp.QQ)
        for d in sp.divisors(n):
            if d < n:
                product *= quotients[int(d)]
        quotient, remainder = sp.div(closure, product, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError("independent primitive division failed")
        quotients[n] = quotient.monic()
    return quotients


def scaled(poly: sp.Poly) -> sp.Poly:
    d = poly.degree()
    result = sp.Poly(sp.expand(6**d * poly.as_expr().subs(X, T / 6)), T, domain=sp.QQ)
    if any(c.q != 1 for c in result.all_coeffs()):
        raise ArithmeticError("independent integrality failure")
    return sp.Poly(result.as_expr(), T, domain=sp.ZZ)


def coeff_sha(poly: sp.Poly) -> str:
    return canonical_sha([int(c) for c in poly.all_coeffs()])


def rational_less_than_bound(value: sp.Rational) -> bool:
    absolute = abs(value)
    if absolute <= 1:
        return True
    return (absolute - 1) ** 2 < 7


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    rows = {int(row["period"]): row for row in certificate["finite_exact_and_numeric_rows"]}
    quotients = independent_quotients()
    checks = []
    for n, quotient in quotients.items():
        poly = scaled(quotient)
        intervals = sp.intervals(poly, eps=sp.Rational(1, 10**18))
        # At n=1 the negative fixed coordinate is exactly -1-sqrt(7), so a
        # rational isolator necessarily straddles the closed endpoint.  The
        # exact sentinel handles that equality; later rows lie strictly inside.
        exact_bound = (
            poly.as_expr() == T**2 + 2 * T - 6
            if n == 1
            else all(
                multiplicity == 1
                and rational_less_than_bound(sp.Rational(bounds[0]))
                and rational_less_than_bound(sp.Rational(bounds[1]))
                for bounds, multiplicity in intervals
            )
        )
        checks.append({
            "period": n,
            "degree": poly.degree(),
            "coefficient_sha_match": coeff_sha(poly) == rows[n]["scaled_polynomial_coefficients_sha256"],
            "all_roots_exactly_isolated_inside_bound": exact_bound,
        })
    if scaled(quotients[1]).as_expr() != T**2 + 2 * T - 6:
        raise ArithmeticError("n=1 sentinel mismatch")
    if scaled(quotients[3]).as_expr() != T**2 - 2 * T - 4:
        raise ArithmeticError("n=3 sentinel mismatch")
    C = math.log(1 + math.sqrt(7))
    envelope_checks = []
    for row in certificate["finite_exact_and_numeric_rows"]:
        degree = int(row["primitive_degree"])
        for pressure in row["pressure_rows"]:
            s = int(pressure["s"])
            z = float(pressure["partition_diagnostic"])
            lower = degree * math.exp(-abs(s) * C)
            upper = degree * math.exp(abs(s) * C)
            envelope_checks.append(lower <= z <= upper)
    payload = {
        "candidate_id": "HCS-P63-INDEPENDENT",
        "rows": checks,
        "exact_sentinels_match": True,
        "pressure_envelopes_match": all(envelope_checks),
        "flat_pressure_sandwich": "exp(-|s|C)D_n <= Z_n(s) <= exp(|s|C)D_n",
        "all_checks_match": all(
            row["coefficient_sha_match"] and row["all_roots_exactly_isolated_inside_bound"]
            for row in checks
        ) and all(envelope_checks),
        "check": True,
    }
    payload["payload_sha256"] = canonical_sha(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": payload["all_checks_match"], "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
