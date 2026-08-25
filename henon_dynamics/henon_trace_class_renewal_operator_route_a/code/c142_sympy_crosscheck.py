#!/usr/bin/env python3
"""Separate SymPy reconstruction of C142 finite determinants and traces."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = json.loads((ROOT / "results/c142_renewal_evidence.json").read_text())
    z = sp.symbols("z")
    checks = 0
    for size in range(1, 11):
        t = sp.zeros(size)
        for j in range(size):
            t[0, j] += sp.Rational(1, 2 ** (j + 1))
            if j + 1 < size:
                t[j + 1, j] += sp.Rational(1, 2 ** (j + 1))
        expected = 1 - sum(sp.Rational(1, 2 ** (m * (m + 1) // 2)) * z**m for m in range(1, size + 1))
        assert sp.expand((sp.eye(size) - z * t).det() - expected) == 0
        checks += 1
        for power in range(1, min(size, 6) + 1):
            row = data["trace_ledger"][power - 1]["trace_Tn"]
            assert sp.trace(t**power) == sp.Rational(row)
            checks += 1
    formal = 1 - sum(sp.Rational(1, 2 ** (2 * m - 1)) * z**m for m in range(1, 15))
    rational = (1 - sp.Rational(3, 4) * z) / (1 - sp.Rational(1, 4) * z)
    assert sp.series(formal - rational, z, 0, 15).removeO() == 0
    checks += 1
    print(json.dumps({"status": "PASS", "sympy_checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
