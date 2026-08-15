#!/usr/bin/env python3
"""Independent finite-cycle check for HCS-P67."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def anomaly(weights: tuple[Fraction, ...], values: tuple[Fraction, ...]) -> Fraction:
    n = len(weights)
    return sum(
        weights[j] * (values[j] - values[(j + 1) % n])
        for j in range(n)
    )


rows = []
for n in range(2, 18):
    uniform = tuple(Fraction(1, n) for _ in range(n))
    basis_checks = [
        anomaly(uniform, tuple(Fraction(int(j == k)) for j in range(n)))
        for k in range(n)
    ]
    if any(basis_checks):
        raise ArithmeticError("uniform anomaly")

    nonuniform = tuple(Fraction(j + 1, n * (n + 1) // 2) for j in range(n))
    witness_values = []
    for k in range(n):
        vector = tuple(Fraction(int(j == k)) for j in range(n))
        witness_values.append(anomaly(nonuniform, vector))
    if not any(witness_values):
        raise ArithmeticError("nonuniform escaped")
    rows.append({
        "cycle_length": n,
        "uniform_basis_anomalies": [str(value) for value in basis_checks],
        "nonuniform_max_anomaly": str(max(abs(value) for value in witness_values)),
    })

result = {"check": True, "rows": rows, "method": "basis test of the cyclic coboundary annihilator"}
(PROJECT / "results" / "c67_independent_check.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({"check": True, "rows": len(rows)}, sort_keys=True))
