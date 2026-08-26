#!/usr/bin/env python3
"""SymPy cross-check of the C180 identities, independent of the producer."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def mu(n: int) -> int:
    return int(sp.mobius(n))


def main() -> None:
    evidence = json.loads((ROOT / "results/c180_lattes_evidence.json").read_text())
    checks = 0
    a, h, z = sp.symbols("a h z")
    plus = ((a - 1) ** 2 - h) / 2
    minus = ((a + 1) ** 2 - h) / 2
    assert sp.simplify(plus + minus + h - (a**2 + 1)) == 0
    checks += 1
    assert sp.simplify(plus / (1 - a) + minus / (1 + a) + h / (1 - a**2) - 1) == 0
    checks += 1

    for parity_h in (1, 4):
        for av in range(2, 101):
            if (av % 2 == 0 and parity_h == 1) or (av % 2 == 1 and parity_h == 4):
                pv = sp.Integer(((av - 1) ** 2 - parity_h) // 2)
                nv = sp.Integer(((av + 1) ** 2 - parity_h) // 2)
                assert pv.is_integer and nv.is_integer and pv >= 0 and nv >= 0
                assert sp.simplify(pv / (1 - av) + nv / (1 + av) + sp.Rational(parity_h, 1 - av**2)) == 1
                checks += 2

    for m in range(2, 11):
        log_series = sum((m ** (2 * n) + 1) * z**n / sp.Integer(n) for n in range(1, 13))
        rational_log = -sp.log(1 - z) - sp.log(1 - m * m * z)
        assert sp.series(log_series - rational_log, z, 0, 13).removeO().expand() == 0
        checks += 1
        for n in range(1, 13):
            exact = sum(mu(n // d) * (m ** (2 * d) + 1) for d in sp.divisors(n))
            assert exact >= 0 and exact % n == 0
            row = next(r for r in evidence["formula_rows"] if r["m"] == m and r["n"] == n)
            assert row["exact_period_points"] == exact and row["primitive_cycles"] == exact // n
            checks += 2

    for row in evidence["wold_rows"]:
        m = row["m"]
        k = tuple(row["k"])
        root = tuple(row["root"])
        depth = row["depth"]
        assert sp.Matrix(root) * (m**depth) == sp.Matrix(k)
        assert not (root[0] % m == 0 and root[1] % m == 0)
        assert sp.Matrix(row["shifted_k"]) == m * sp.Matrix(k)
        checks += 3

    print(json.dumps({"status": "C180_SYMPY_PASS", "checks": checks, "sympy_version": sp.__version__}, sort_keys=True))


if __name__ == "__main__":
    main()
