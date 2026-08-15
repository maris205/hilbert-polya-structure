#!/usr/bin/env python3
"""Independent arithmetic reconstruction for HCS-P72."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results/c72_independent_check.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def squarefree_sign(n: int) -> int:
    sign = 1
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            sign = -sign
            if value % p == 0:
                return 0
        p += 1
    return -sign if value > 1 else sign


def c_raw(m: int) -> Fraction:
    return sum(Fraction(d * squarefree_sign(d), m) for d in divisors(m) if d & 1)


def c_factor(m: int) -> Fraction:
    value = m
    while value % 2 == 0:
        value //= 2
    p = 3
    numerator = 1
    while p * p <= value:
        if value % p == 0:
            numerator *= 1 - p
            while value % p == 0:
                value //= p
        p += 2
    if value > 1 and value & 1:
        numerator *= 1 - value
    return Fraction(numerator, m)


rows = []
for m in range(1, 65):
    a = c_raw(m)
    b = c_factor(m)
    if a != b or b == 0:
        raise SystemExit(f"coefficient mismatch at {m}")
    rho = 2 ** (-1 / (2 * m))
    principal = -b / m
    rows.append({
        "m": m,
        "c_m": str(b),
        "relative_principal_multiplier_of_1_over_sqrt2": str(principal),
        "rho_m": format(rho, ".17g"),
    })

if not all(float(rows[i]["rho_m"]) < float(rows[i + 1]["rho_m"])
           for i in range(len(rows) - 1)):
    raise SystemExit("rho ladder is not increasing")
if not math.isclose(float(rows[-1]["rho_m"]), 2 ** (-1 / 128), rel_tol=0, abs_tol=1e-16):
    raise SystemExit("rho endpoint")

out = {
    "candidate_id": "HCS-P72",
    "method": "independent divisor sum versus odd-radical Euler product",
    "rows": rows,
    "all_nonzero": True,
    "strictly_increasing": True,
    "limit": "1",
    "check": True,
}
OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"candidate_id": "HCS-P72", "rows": len(rows), "check": True}, sort_keys=True))
