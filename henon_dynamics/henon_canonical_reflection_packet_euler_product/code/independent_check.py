#!/usr/bin/env python3
"""Independent recurrence check for HCS-P68."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c68_certificate.json"
OUTPUT = PROJECT / "results" / "c68_independent_check.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def fixed(n: int) -> int:
    return 2 ** ((n + 1) // 2) if n % 2 else 0


def primitive_by_subtraction(n: int, known: dict[int, int]) -> int:
    return fixed(n) - sum(known[d] for d in divisors(n) if d < n)


def main() -> None:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    primitive: dict[int, int] = {}
    for n in range(1, 42, 2):
        primitive[n] = primitive_by_subtraction(n, primitive)
    expected = [row["D_n"] for row in cert["generating_rows"]]
    if list(primitive.values()) != expected:
        raise RuntimeError("independent primitive recurrence")

    product = cert["product_coefficients_through_41"]
    recovered = [0] * len(product)
    for degree in range(1, len(product)):
        recovered[degree] = degree * product[degree]
        for j in range(1, degree):
            recovered[degree] -= recovered[j] * product[degree - j]
    if recovered != cert["log_derivative_coefficients_through_41"]:
        raise RuntimeError("independent logarithmic derivative")
    if cert["claim_status"]["arithmetic_advance"] != "NO":
        raise RuntimeError("claim promotion")

    payload = {
        "candidate_id": "HCS-P68",
        "primitive_recurrence": "PASS",
        "log_derivative_recovery": "PASS",
        "arithmetic_firewall": "PASS",
        "certificate_sha256": hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
        "check": True,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
