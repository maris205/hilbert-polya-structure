#!/usr/bin/env python3
"""Post-freeze inventory evaluator and arbitrary-label controls for SD-C28."""

from __future__ import annotations

import hashlib
import math


def sieve(limit: int) -> list[bool]:
    flags = [True] * (limit + 1)
    if limit >= 0:
        flags[0] = False
    if limit >= 1:
        flags[1] = False
    for candidate in range(2, math.isqrt(limit) + 1):
        if flags[candidate]:
            start = candidate * candidate
            flags[start : limit + 1 : candidate] = [False] * (
                (limit - start) // candidate + 1
            )
    return flags


def fibonacci_set(limit: int) -> set[int]:
    values: set[int] = set()
    left, right = 1, 2
    while right <= limit:
        values.add(right)
        left, right = right, left + right
    return values


def hash_ranked(limit: int, count: int, salt: str) -> list[int]:
    ranked = sorted(
        range(2, limit + 1),
        key=lambda value: hashlib.sha256(f"{salt}:{value}".encode()).digest(),
    )
    return sorted(ranked[:count])


def inventories_at_cutoff(limit: int) -> dict[str, list[int]]:
    flags = sieve(limit)
    primes = [value for value in range(2, limit + 1) if flags[value]]
    fibonacci = fibonacci_set(limit)
    return {
        "prime_evaluator": primes,
        "square_control": [
            value
            for value in range(2, limit + 1)
            if math.isqrt(value) ** 2 == value
        ],
        "fibonacci_control": sorted(fibonacci),
        "all_integer_control": list(range(2, limit + 1)),
        "matched_density_seeded_random": hash_ranked(
            limit, len(primes), "SD-C28-SEEDED-RANDOM"
        ),
        "matched_density_hash": hash_ranked(limit, len(primes), "SD-C28-HASH"),
        "arbitrary_decidable_modular": [
            value for value in range(2, limit + 1) if value % 7 in {1, 2, 4}
        ],
    }


INVENTORY_NAMES = (
    "prime_evaluator",
    "square_control",
    "fibonacci_control",
    "all_integer_control",
    "matched_density_seeded_random",
    "matched_density_hash",
    "arbitrary_decidable_modular",
)
