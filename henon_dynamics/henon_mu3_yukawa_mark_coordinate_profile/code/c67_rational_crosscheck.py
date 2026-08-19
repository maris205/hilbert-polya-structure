#!/usr/bin/env python3
"""Independent SymPy rational-inverse cross-check for C67."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
EVIDENCE = PROJECT / "results/c67_coordinate_profile_evidence.json"


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def order(values: list[sp.Rational]) -> int:
    result = 1
    for value in values:
        result = lcm(result, int(value.q))
    return result


def main() -> None:
    c64 = json.loads(C64.read_text())
    evidence = json.loads(EVIDENCE.read_text())
    matrix = sp.Matrix(c64["mark_matrix"])
    inverse = matrix.inv()
    assert matrix * inverse == sp.eye(16)
    assert inverse * matrix == sp.eye(16)
    columns = [order([inverse[i, j] for i in range(16)]) for j in range(16)]
    rows = [order([inverse[i, j] for j in range(16)]) for i in range(16)]
    denominator = 1
    for value in inverse:
        denominator = lcm(denominator, int(value.q))
    assert columns == evidence["coordinate_orders"]
    assert rows == evidence["dual_coordinate_orders"]
    assert denominator == 144
    assert sum(value != 0 for value in inverse) == evidence["inverse_nonzero_count"] == 43
    print(json.dumps({
        "status": "RATIONAL_CROSSCHECK_PASS",
        "coordinate_orders": columns,
        "dual_coordinate_orders": rows,
        "global_denominator": denominator,
        "inverse_nonzero_count": 43,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
