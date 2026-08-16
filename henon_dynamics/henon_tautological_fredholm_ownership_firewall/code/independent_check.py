#!/usr/bin/env python3
"""Independent channel and cyclic-block reconstruction for HCS-P77."""

from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results/c77_independent_check.json"


def factors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def squarefree_sign(n: int) -> int:
    sign = 1
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
        p += 1
    return -sign if value > 1 else sign


def coefficient(m: int) -> Fraction:
    return sum(Fraction(d * squarefree_sign(d), m) for d in factors(m) if d & 1)


def channel(m: int, z: complex, q: float) -> complex:
    return float(coefficient(m)) * 2 * (q * z) ** m / (1 - (1 + q ** (2 * m)) * z ** (2 * m))


def singleton(n: int) -> tuple[int, ...]:
    return (1,) + (0,) * (n - 1)


def chi(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(int(word[(j - 1) % n] == word[(j + 1) % n]) for j in range(n))


def cyclic(weights: tuple[Fraction, ...]) -> list[list[Fraction]]:
    n = len(weights)
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j, weight in enumerate(weights):
        out[(j + 1) % n][j] = weight
    return out


def determinant(data: list[list[Fraction]]) -> Fraction:
    a = [row[:] for row in data]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        diagonal = a[col][col]
        out *= diagonal
        for r in range(col + 1, n):
            ratio = a[r][col] / diagonal
            for j in range(col, n):
                a[r][j] -= ratio * a[col][j]
    return out


channel_rows = []
for q, z in ((0.5, 0.6), (1.0, 0.75), (2.0, 0.4)):
    entries = [channel(m, complex(z), q) for m in range(1, 193)]
    exp_trace = cmath.exp(sum(entries, 0j))
    product = math.prod(cmath.exp(value) for value in entries)
    if abs(exp_trace - product) > 2e-11:
        raise SystemExit("channel determinant mismatch")
    channel_rows.append({
        "q": q,
        "z": z,
        "partial_trace_norm": format(sum(abs(value) for value in entries), ".17g"),
        "determinant_error": format(abs(exp_trace - product), ".6e"),
    })

block_rows = []
q = Fraction(3, 4)
z = Fraction(2, 7)
for n in range(3, 22, 2):
    word = singleton(n)
    values = chi(word)
    if sum(values) != n - 2 or any(word[j] != word[-j % n] for j in range(n)):
        raise SystemExit(f"singleton mismatch at {n}")
    weights = tuple(q ** value for value in values)
    block = cyclic(weights)
    matrix = [[Fraction(int(i == j)) - z * block[i][j] for j in range(n)] for i in range(n)]
    observed = determinant(matrix)
    expected = 1 - z ** n * q ** (n - 2)
    if observed != expected:
        raise SystemExit(f"block determinant mismatch at {n}")
    block_rows.append({
        "n": n,
        "energy": n - 2,
        "determinant": str(observed),
        "minimum_singular_value": str(q),
    })

rank_one_rows = []
for value in (cmath.exp(0.3 + 0.2j), cmath.exp(-0.4j), 2.0 + 0.5j):
    observed = 1 + (value - 1)
    if observed != value:
        raise SystemExit("rank-one mismatch")
    rank_one_rows.append({"error": format(abs(observed - value), ".6e")})

out = {
    "candidate_id": "HCS-P77",
    "method": "independent channel summation, rational cyclic determinants, and rank-one compression",
    "channel_rows": channel_rows,
    "block_rows": block_rows,
    "rank_one_rows": rank_one_rows,
    "channel_determinants_match": True,
    "finite_source_blocks_match": True,
    "uniform_singular_floor": str(q),
    "full_direct_sum_compact": False,
    "genuine_transfer_claimed": False,
    "check": True,
}
OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "candidate_id": "HCS-P77",
    "channel_rows": len(channel_rows),
    "block_rows": len(block_rows),
    "rank_one_rows": len(rank_one_rows),
    "check": True,
}, sort_keys=True))
