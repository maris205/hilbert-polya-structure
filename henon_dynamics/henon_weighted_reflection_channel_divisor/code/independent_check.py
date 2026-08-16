#!/usr/bin/env python3
"""Independent weighted-channel reconstruction for HCS-P75."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results/c75_independent_check.json"


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


def coefficient_raw(m: int) -> Fraction:
    return sum(Fraction(d * squarefree_sign(d), m) for d in factors(m) if d & 1)


def coefficient_factored(m: int) -> Fraction:
    value = m
    while value % 2 == 0:
        value //= 2
    numerator = 1
    p = 3
    while p * p <= value:
        if value % p == 0:
            numerator *= 1 - p
            while value % p == 0:
                value //= p
        p += 2
    if value > 1:
        numerator *= 1 - value
    return Fraction(numerator, m)


def polynomial_add(a: dict[int, Fraction], b: dict[int, Fraction], scale: Fraction) -> dict[int, Fraction]:
    out = dict(a)
    for exponent, value in b.items():
        out[exponent] = out.get(exponent, Fraction(0)) + scale * value
        if out[exponent] == 0:
            del out[exponent]
    return out


def all_words(n: int) -> dict[int, Fraction]:
    half = (n - 1) // 2
    return {1 + 2 * k: Fraction(2 * math.comb(half, k)) for k in range(half + 1)}


def dilate(poly: dict[int, Fraction], k: int) -> dict[int, Fraction]:
    return {k * exponent: value for exponent, value in poly.items()}


def primitive(n: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for k in factors(n):
        out = polynomial_add(out, dilate(all_words(n // k), k), Fraction(squarefree_sign(k)))
    return out


def direct_coefficient(degree: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for n in factors(degree):
        if n & 1:
            repetition = degree // n
            out = polynomial_add(out, dilate(primitive(n), repetition), Fraction(1, repetition))
    return out


def channel_coefficient(degree: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for m in factors(degree):
        quotient = degree // m
        if not quotient & 1:
            continue
        j = (quotient - 1) // 2
        term = {m + 2 * m * h: Fraction(2 * math.comb(j, h)) for h in range(j + 1)}
        out = polynomial_add(out, term, coefficient_factored(m))
    return out


rows = []
for m in range(1, 65):
    raw = coefficient_raw(m)
    factored = coefficient_factored(m)
    if raw != factored or factored == 0 or abs(factored) > 1:
        raise SystemExit(f"channel mismatch at {m}")
    rows.append({"m": m, "c_m": str(factored)})

coefficient_rows = []
for degree in range(1, 65):
    direct = direct_coefficient(degree)
    regrouped = channel_coefficient(degree)
    if direct != regrouped:
        raise SystemExit(f"weighted coefficient mismatch at {degree}")
    coefficient_rows.append({
        "degree": degree,
        "nonzero_q_terms": len(direct),
    })

geometry = []
for q in (0.5, 1.0, 2.0):
    radii = []
    max_residual = 0.0
    for m in range(1, 25):
        radius = (1 + q ** (2 * m)) ** (-1 / (2 * m))
        radii.append(radius)
        for ell in range(2 * m):
            angle = math.pi * ell / m
            root = radius * complex(math.cos(angle), math.sin(angle))
            max_residual = max(max_residual, abs(root ** (2 * m) + (q * root) ** (2 * m) - 1))
    if not all(a < b for a, b in zip(radii, radii[1:])):
        raise SystemExit(f"radius separation failed at q={q}")
    geometry.append({
        "q": q,
        "rows": len(radii),
        "strict_radius_separation": True,
        "max_hypersurface_residual": format(max_residual, ".6e"),
    })

out = {
    "candidate_id": "HCS-P75",
    "method": "independent dictionary-polynomial reconstruction and complex-root geometry",
    "channel_rows": rows,
    "coefficient_rows": coefficient_rows,
    "geometry": geometry,
    "all_channels_nonzero": True,
    "weighted_coefficients_match": True,
    "natural_boundary_tested": False,
    "operator_claimed": False,
    "check": True,
}
OUTPUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "candidate_id": "HCS-P75",
    "channels": len(rows),
    "weighted_coefficients": len(coefficient_rows),
    "geometry_blocks": len(geometry),
    "check": True,
}, sort_keys=True))
