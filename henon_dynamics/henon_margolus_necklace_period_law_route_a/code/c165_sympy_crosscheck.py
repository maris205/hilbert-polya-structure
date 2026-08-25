#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C165."""
from __future__ import annotations

import json
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c165_margolus_evidence.json"


def permutation_matrix(images: list[int]) -> sp.Matrix:
    size = len(images)
    return sp.Matrix(size, size, lambda row, col: 1 if row == images[col] else 0)


def move_mask(mask: int, images: list[int]) -> int:
    result = 0
    for source, target in enumerate(images):
        if mask & (1 << source):
            result |= 1 << target
    return result


def configuration_cycles(images: list[int]) -> list[int]:
    size = len(images)
    seen = set()
    lengths = []
    for state in range(1 << size):
        if state in seen:
            continue
        current = state
        length = 0
        while current not in seen:
            seen.add(current)
            current = move_mask(current, images)
            length += 1
        lengths.append(length)
    return sorted(lengths)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    y, z = sp.symbols("y z")
    checks = 0
    for row in data["finite_replay"]["family_rows"]:
        m = row["half_ring_m"]
        images = row["full_tick_site_permutation"]
        matrix = permutation_matrix(images)
        assert matrix**m == sp.eye(2 * m)
        checks += 1
        characteristic = sp.Poly(matrix.charpoly(y).as_expr(), y)
        expected_characteristic = sp.Poly((y**m - 1) ** 2, y)
        assert characteristic == expected_characteristic
        checks += 1
        reflection = permutation_matrix(row["reflection_permutation"])
        assert reflection * matrix * reflection == matrix.inv()
        assert reflection**2 == sp.eye(2 * m)
        checks += 2

        periods = {item["period_d"]: item for item in row["period_rows"]}
        for d, item in periods.items():
            reconstructed = sum(int(sp.mobius(d // e)) * 4**e for e in sp.divisors(d))
            assert reconstructed == item["exact_period_configurations"]
            assert reconstructed == d * item["primitive_cycles"]
            checks += 2
        for n in range(1, 2 * m + 1):
            trace_log_coefficient = sum(
                d * item["primitive_cycles"]
                for d, item in periods.items() if n % d == 0
            )
            assert trace_log_coefficient == 4 ** gcd(m, n)
            checks += 1
        determinant = sp.prod((1 - z**d) ** item["primitive_cycles"] for d, item in periods.items())
        logarithmic = sp.cancel(-z * sp.diff(determinant, z) / determinant)
        formal = sum(
            d * item["primitive_cycles"] * z**d / (1 - z**d)
            for d, item in periods.items()
        )
        assert sp.cancel(logarithmic - formal) == 0
        checks += 1
        short = row["short_period_configurations"]
        assert sp.Rational(short, 4**m) <= sp.Rational(m, 2**m)
        checks += 1

    for row in data["finite_replay"]["family_rows"][:3]:
        m = row["half_ring_m"]
        images = row["full_tick_site_permutation"]
        lengths = configuration_cycles(images)
        koopman_images = []
        for state in range(4**m):
            koopman_images.append(move_mask(state, images))
        koopman = permutation_matrix(koopman_images)
        characteristic = sp.Poly(koopman.charpoly(y).as_expr(), y)
        expected = sp.Poly(sp.prod((y**d - 1) ** lengths.count(d) for d in sorted(set(lengths))), y)
        assert characteristic == expected
        assert lengths.count(1) == 4
        for item in row["period_rows"]:
            assert lengths.count(item["period_d"]) == item["primitive_cycles"]
            checks += 1
        checks += 2

    assert data["finite_replay"]["boundary_m1"]["T_is_identity"] is True
    assert data["finite_replay"]["boundary_m2"]["primitive_two_cycles"] == 6
    checks += 2
    print(json.dumps({"status": "C165_SYMPY_PASS", "checks": checks, "max_m": 16, "explicit_koopman_max_m": 3}, sort_keys=True))


if __name__ == "__main__":
    main()
