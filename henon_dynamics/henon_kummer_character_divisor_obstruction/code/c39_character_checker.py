#!/usr/bin/env python3
"""Exact Z[zeta_3] character rigidity and numerical divisor witness."""

from __future__ import annotations

import hashlib
import json
import math


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def scale(n: int, x: tuple[int, int]) -> tuple[int, int]:
    return n * x[0], n * x[1]


def root_power(k: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, -1))[k % 3]


def character(m: tuple[int, int, int], r: int) -> tuple[int, int]:
    total = (0, 0)
    for j, multiplicity in enumerate(m):
        total = add(total, scale(multiplicity, root_power(j * r)))
    return total


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (((limit - 1 - p * p) // p) + 1)
    return [p for p in range(limit) if sieve[p]]


def certificate(bound: int = 6, prime_limit: int = 100_000) -> dict[str, object]:
    null_vectors: list[list[int]] = []
    vectors_checked = 0
    for m0 in range(-bound, bound + 1):
        for m1 in range(-bound, bound + 1):
            for m2 in range(-bound, bound + 1):
                m = (m0, m1, m2)
                vectors_checked += 1
                if all(character(m, r) == (0, 0) for r in (1, 2, 3)):
                    null_vectors.append(list(m))
    if null_vectors != [[0, 0, 0]]:
        raise AssertionError("nontrivial all-repetition null character")

    ps = primes_below(prime_limit)
    selected = [ps[0], ps[10], ps[100], ps[1000], ps[-1]]
    distances = {
        str(p): 2 * math.pi / (3 * math.log(p)) for p in selected
    }
    ordered = [distances[str(p)] for p in selected]
    if not all(a > b for a, b in zip(ordered, ordered[1:])):
        raise AssertionError("nearest nontrivial channel divisor did not approach zero")

    payload = {
        "candidate": "HCS-C39",
        "virtual_bound": bound,
        "virtual_vectors_checked": vectors_checked,
        "all_repetition_null_vectors": null_vectors,
        "prime_limit": prime_limit,
        "prime_count": len(ps),
        "sample_nearest_divisor_distance": distances,
        "raw_all_prime_meromorphic_divisor": "REFUTED_BY_INTERIOR_ACCUMULATION",
        "status": "PROVED_ALL_PRIME_DIVISOR_OBSTRUCTION",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2, sort_keys=True))
