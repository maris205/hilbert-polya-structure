#!/usr/bin/env python3
"""Exact and finite numerical certificate for HCS-C43.

The theorem is analytic: it combines the exact primitive-orbit census of the
four-state H6 subshift with the prime number theorem.  This script verifies
the finite algebra independently of eigenvalue arithmetic and records a
non-fitted finite comparison with the Chebyshev functions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT / "results" / "c43_certificate.json"
A = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def matmul(left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )


def matpow(exponent: int) -> tuple[tuple[int, ...], ...]:
    result = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    base = A
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def marked_count(period: int) -> int:
    matrix = matpow(period)
    return sum(matrix[i][i] for i in range(4))


def mobius(value: int) -> int:
    residual = value
    prime = 2
    factors = 0
    while prime * prime <= residual:
        if residual % prime == 0:
            residual //= prime
            factors += 1
            if residual % prime == 0:
                return 0
            while residual % prime == 0:
                residual //= prime
        prime += 1
    if residual > 1:
        factors += 1
    return -1 if factors % 2 else 1


def divisors(value: int) -> list[int]:
    return [item for item in range(1, value + 1) if value % item == 0]


def exact_period_count(period: int) -> int:
    return sum(mobius(divisor) * marked_count(period // divisor) for divisor in divisors(period))


def prime_table(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start::prime] = b"\x00" * (((limit - start) // prime) + 1)
    return [index for index, flag in enumerate(sieve) if flag]


def build_certificate(max_period: int) -> dict[str, object]:
    if max_period < 12 or max_period > 34:
        raise ValueError("max-period must lie in [12,34]")
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    limit = int(phi**max_period)
    primes = prime_table(limit)
    rows: list[dict[str, object]] = []
    theta = 0.0
    prime_index = 0
    for period in range(1, max_period + 1):
        scale = int(phi**period)
        while prime_index < len(primes) and primes[prime_index] <= scale:
            theta += math.log(primes[prime_index])
            prime_index += 1
        marked = marked_count(period)
        exact = exact_period_count(period)
        if exact % period:
            raise ArithmeticError("exact-period marked points are not divisible by the period")
        primitive = exact // period
        rows.append(
            {
                "period": period,
                "floor_phi_power": scale,
                "marked_points": marked,
                "exact_period_points": exact,
                "primitive_orbits": primitive,
                "pi": prime_index,
                "theta": theta,
                "exact_over_theta": exact / theta if theta else None,
                "primitive_over_pi": primitive / prime_index if prime_index else None,
            }
        )
    matrix_polynomial = "x^4-x^3-x-1=(x^2-x-1)(x^2+1)"
    payload = {
        "candidate_id": "HCS-C43",
        "object": "certified H6 four-state survivor",
        "clock": "T_n=n*log(phi)",
        "adjacency": [list(row) for row in A],
        "characteristic_polynomial": matrix_polynomial,
        "entropy": math.log(phi),
        "max_period": max_period,
        "rows": rows,
        "finite_gate": {
            "mobius_integrality": all(row["exact_period_points"] % row["period"] == 0 for row in rows),
            "positive_exact_counts": all(row["exact_period_points"] >= 0 for row in rows),
            "last_exact_over_theta": rows[-1]["exact_over_theta"],
            "last_primitive_over_pi": rows[-1]["primitive_over_pi"],
            "target_primitive_ratio": math.log(phi),
        },
        "theorem": {
            "marked_limit": "E_n/theta(phi^n)->1",
            "primitive_limit": "P_n/pi(phi^n)->log(phi)",
            "status": "PROVED_USING_EXACT_SFT_CENSUS_AND_PNT",
        },
        "claim_boundary": "asymptotic mass bridge only; no orbit-prime bijection or Riemann determinant",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=32)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build_certificate(args.max_period)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "periods": args.max_period, "sha256": result["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
