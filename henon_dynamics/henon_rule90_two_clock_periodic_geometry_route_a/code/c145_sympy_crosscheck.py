#!/usr/bin/env python3
"""SymPy polynomial-gcd cross-check for all C145 table cells."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c145_rule90_evidence.json"


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    data = json.loads(path.read_text())
    x = sp.symbols("x")
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    for row in data["two_clock_table"]["rows"]:
        length = row["spatial_length_L"]
        time = row["temporal_period_n"]
        f = sp.Poly(x ** length + 1, x, modulus=2)
        h = sp.Poly((x ** 2 + 1) ** time + x ** time, x, modulus=2)
        d = f.gcd(h).degree()
        ck(d == row["gcd_degree"], f"gcd degree L={length} n={time}")
        ck(2 ** d == row["fixed_points"], f"fixed count L={length} n={time}")
    ck(sp.Poly(x ** 6 + 1, x, modulus=2) == sp.Poly((x ** 3 + 1) ** 2, x, modulus=2), "non-squarefree factorization")
    for length in range(1, 25):
        polynomial = sp.Poly(x ** length + 1, x, modulus=2)
        derivative_gcd = polynomial.gcd(polynomial.diff()).degree()
        ck((derivative_gcd > 0) == (length % 2 == 0), f"squarefree parity L={length}")
    print(json.dumps({"status": "C145_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
