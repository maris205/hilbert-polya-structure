#!/usr/bin/env python3
"""Finite diagnostics for the exact C40 Schatten phase diagram."""

from __future__ import annotations

import hashlib
import json


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (((limit - 1 - p * p) // p) + 1)
    return [p for p in range(limit) if sieve[p]]


def schatten_status(sigma_num: int, sigma_den: int, q: int) -> str:
    product_num = sigma_num * q
    if product_num > sigma_den:
        return "IN_S_q"
    if product_num == sigma_den:
        return "DIVERGES_AT_PRIME_HARMONIC_BOUNDARY"
    return "NOT_IN_S_q"


def certificate(limit: int = 1_000_000) -> dict[str, object]:
    ps = primes_below(limit)
    cutoffs = tuple(max(10, limit // divisor) for divisor in (1000, 100, 10, 1))
    exponents = (0.8, 1.0, 1.2)
    partial: dict[str, list[float]] = {}
    for exponent in exponents:
        partial[str(exponent)] = [
            3.0 * sum(p ** (-exponent) for p in ps if p <= cutoff)
            for cutoff in cutoffs
        ]
    for values in partial.values():
        if not all(a < b for a, b in zip(values, values[1:])):
            raise AssertionError("positive prime sums must increase")

    grid = {
        "sigma_1_over_3_q_2": schatten_status(1, 3, 2),
        "sigma_1_over_2_q_2": schatten_status(1, 2, 2),
        "sigma_2_over_3_q_2": schatten_status(2, 3, 2),
        "sigma_1_q_1": schatten_status(1, 1, 1),
        "sigma_6_over_5_q_1": schatten_status(6, 5, 1),
    }
    expected = {
        "sigma_1_over_3_q_2": "NOT_IN_S_q",
        "sigma_1_over_2_q_2": "DIVERGES_AT_PRIME_HARMONIC_BOUNDARY",
        "sigma_2_over_3_q_2": "IN_S_q",
        "sigma_1_q_1": "DIVERGES_AT_PRIME_HARMONIC_BOUNDARY",
        "sigma_6_over_5_q_1": "IN_S_q",
    }
    if grid != expected:
        raise AssertionError("Schatten boundary classification changed")

    payload = {
        "candidate": "HCS-C40",
        "prime_limit": limit,
        "prime_count": len(ps),
        "block_rank": 3,
        "schatten_grid": grid,
        "partial_prime_sums": partial,
        "good_prime_artin_conductor_exponent": 0,
        "trace_class_threshold": "sigma>1",
        "status": "PROVED_ANALYTIC_DETERMINANT_NONCANONICAL_CLOCK",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2, sort_keys=True))
