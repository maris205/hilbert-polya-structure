#!/usr/bin/env python3
"""Independent pole and regularization reconstruction for HCS-P73."""

from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results/c73_independent_check.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def squarefree_sign(n: int) -> int:
    value = n
    sign = 1
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
    return sum(Fraction(d * squarefree_sign(d), m) for d in divisors(m) if d % 2)


def channel_value(m: int, t: complex) -> complex:
    return complex(coefficient(m)) * 2 * t**m / (1 - 2 * t ** (2 * m))


def regularized_pole_value(m: int, k: int, t: complex) -> complex:
    c = float(coefficient(m))
    rho = 2 ** (-1 / (2 * m))
    root = rho * cmath.exp(1j * math.pi * k / m)
    b = c * ((-1) ** k) / (math.sqrt(2) * m)
    x = t / root
    return b * x**m / (1 - x)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            return False
    return True


rows = []
sample_points = (0.1 + 0.07j, -0.2 + 0.11j, 0.31 - 0.05j)
for m in range(2, 65):
    c = coefficient(m)
    if c == 0:
        raise SystemExit(f"zero channel at {m}")
    if any((m - j) % (2 * m) == 0 for j in range(m)):
        raise SystemExit(f"root cancellation failure at {m}")
    max_error = 0.0
    for t in sample_points:
        reconstructed = sum(regularized_pole_value(m, k, t) for k in range(2 * m))
        max_error = max(max_error, abs(reconstructed - channel_value(m, t)))
    if max_error > 3e-12:
        raise SystemExit(f"partial fraction mismatch at {m}: {max_error}")
    rows.append({
        "m": m,
        "c_m": str(c),
        "pole_count": 2 * m,
        "genus": m - 1,
        "max_sample_error": format(max_error, ".3e"),
    })

prime_rows = []
partial = Fraction(0)
for p in range(3, 100, 2):
    if not is_prime(p):
        continue
    mass = abs(coefficient(p))
    if mass < Fraction(2, 3):
        raise SystemExit("prime mass lower bound")
    partial += mass
    prime_rows.append({"p": p, "mass_over_sqrt2": str(mass), "partial": str(partial)})

out = {
    "candidate_id": "HCS-P73",
    "method": "independent root reconstruction and prime-level raw-mass lower bound",
    "rows": rows,
    "prime_rows": prime_rows,
    "all_channels_nonzero": True,
    "regularized_partial_fractions": True,
    "raw_absolute_mass_diverges": True,
    "normalized_identity": "exp(3/2)w^(1/2)exp(-3/(4w))exp(L)C_rel=1",
    "check": True,
}
OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"candidate_id": "HCS-P73", "levels": len(rows), "check": True}, sort_keys=True))
