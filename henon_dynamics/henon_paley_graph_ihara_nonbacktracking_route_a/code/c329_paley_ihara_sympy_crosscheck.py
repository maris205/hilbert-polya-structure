#!/usr/bin/env python3
"""Independent SymPy algebra lane for HCS-C329."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c329_paley_ihara_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    u, x = sp.symbols("u x")
    checks = 0
    for row in data["field_rows"]:
        q, k = row["q"], row["degree"]
        r = (-1 + sp.sqrt(q)) / 2
        s = (-1 - sp.sqrt(q)) / 2
        assert sp.expand(r ** 2 + r - (q - 1) / 4) == 0
        assert sp.expand(s ** 2 + s - (q - 1) / 4) == 0
        excess = row["bass_factorization"]["one_minus_u_squared_exponent"]
        assert 2 * excess + 2 + 4 * k == row["directed_edge_count"]
        def power_sum(lam, n):
            if n == 1:
                return lam
            previous, current = sp.Integer(2), lam
            for _ in range(2, n + 1):
                previous, current = current, sp.expand(lam * current - (k - 1) * previous)
            return current
        for cell in row["trace_rows"]:
            n = cell["n"]
            trace = (excess * (1 + (-1) ** n) + power_sum(k, n) +
                     k * (power_sum(r, n) + power_sum(s, n)))
            assert sp.simplify(trace - cell["trace"]) == 0
            checks += 1
        if q in (5, 9):
            log_factor = (-excess * sp.log(1 - u ** 2)
                          - sp.log(1 - k * u + (k - 1) * u ** 2)
                          - k * sp.log(1 - r * u + (k - 1) * u ** 2)
                          - k * sp.log(1 - s * u + (k - 1) * u ** 2))
            series = sp.series(log_factor, u, 0, 8).removeO().expand()
            for cell in row["trace_rows"][:7]:
                assert sp.simplify(series.coeff(u, cell["n"]) * cell["n"] - cell["trace"]) == 0
                checks += 1
        checks += 3
    for p in (5, 13, 17):
        residues = {a * a % p for a in range(1, p)}
        adjacency = sp.Matrix(p, p, lambda i, j: int(i != j and (j - i) % p in residues))
        characteristic = sp.factor(adjacency.charpoly(x).as_expr(), extension=sp.sqrt(p))
        k = (p - 1) // 2
        expected = sp.expand((x - k) * (x - (-1 + sp.sqrt(p)) / 2) ** k *
                             (x - (-1 - sp.sqrt(p)) / 2) ** k)
        assert sp.expand(characteristic - expected) == 0
        checks += p * p
    print(f"C329 SymPy cross-check: PASS ({checks} symbolic/exact checks)")


if __name__ == "__main__":
    main()
