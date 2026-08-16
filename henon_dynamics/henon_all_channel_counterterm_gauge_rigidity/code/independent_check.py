#!/usr/bin/env python3
"""Independent arithmetic reconstruction for HCS-P74.

This checker deliberately does not import c74_gauge_rigidity.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results/c74_certificate.json"
OUTPUT = PROJECT / "results/c74_independent_check.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    value = n
    count = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            count += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        count += 1
    return -1 if count % 2 else 1


def c_value(m: int) -> Fraction:
    return Fraction(sum(d * mu(d) for d in divisors(m) if d % 2), m)


def channel(m: int, degree: int) -> Fraction:
    if degree % m:
        return Fraction(0)
    q = degree // m
    if q % 2 == 0:
        return Fraction(0)
    return c_value(m) * 2 ** ((q + 1) // 2)


def multiplier(m: int, genus: int, degree: int) -> Fraction:
    return channel(m, degree) if degree > genus else Fraction(0)


def main() -> None:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    rows = []
    for degree in range(1, 97):
        relative = -sum(
            (channel(m, degree) for m in divisors(degree) if m >= 2),
            Fraction(0),
        )
        gm1 = sum(
            (multiplier(m, m - 1, degree) for m in divisors(degree) if m >= 2),
            Fraction(0),
        )
        gm = sum(
            (multiplier(m, m, degree) for m in divisors(degree) if m >= 2),
            Fraction(0),
        )
        annihilated = relative + gm1
        residual = relative + gm
        expected = Fraction(0) if degree == 1 else -2 * c_value(degree)
        if annihilated != 0 or residual != expected:
            raise ArithmeticError(f"independent sign failure at {degree}")
        cert_row = cert["coefficient_crosscheck"][degree - 1]
        if Fraction(cert_row["source_preserving_residual_log"]) != expected:
            raise ArithmeticError("certificate disagreement")
        rows.append({
            "degree": degree,
            "annihilated": str(annihilated),
            "source_preserving_residual": str(residual),
        })

    forced = cert["source_forced_pair"]
    if forced != {"a": "3/4", "beta": "1/2"}:
        raise ArithmeticError("source pair")
    if cert["claim_status"]["absolute_canonical_gauge"] != "OPEN":
        raise ArithmeticError("canonicity firewall")
    if cert["claim_status"]["operator_ownership"] != "OPEN":
        raise ArithmeticError("operator firewall")
    if cert["claim_status"]["route_b_authorized"] is not False:
        raise ArithmeticError("route B firewall")

    out = {
        "candidate_id": "HCS-P74",
        "method": "independent divisor reconstruction; no import from producer",
        "coefficient_rows": rows,
        "source_pair": forced,
        "genus_m_minus_1": "ZERO_RESIDUAL",
        "genus_m": "NEGATIVE_TWO_C_M_RESIDUAL",
        "certificate_sha256": hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
        "check": True,
    }
    OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": "HCS-P74",
        "rows": len(rows),
        "source_pair": forced,
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
