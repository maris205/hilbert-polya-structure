#!/usr/bin/env python3
"""Independent SymPy checks for the C251 majority/domain-wall identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c251_majority_evidence.json"


def matpow(a: sp.Matrix, n: int) -> sp.Matrix:
    return a ** n


def run_matrix(m: int, signed: bool = False) -> sp.Matrix:
    out = sp.zeros(m + 1)
    for r in range(m + 1):
        out[r, 0] = 1
        if r < m:
            out[r, r + 1] = -1 if signed else 1
    return out


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    M = sp.Matrix(data["regression"]["fixed_debruijn_matrix"])
    checks = 0
    lam = sp.symbols("lambda")
    assert sp.factor(M.charpoly(lam).as_expr()) == (lam**2 - lam - 1) * (lam**2 - lam + 1)
    checks += 1

    rows = data["regression"]["fixed_formula_rows"]
    for row in rows:
        n = row["n"]
        assert int(sp.trace(matpow(M, n))) == row["fixed_count_trace"]
        checks += 1
        # The two quadratic factors imply Lucas plus sixth-root trace.
        L = sp.lucas(n)
        c = 2 * sp.cos(sp.pi * n / 3)
        assert int(L + c) == row["fixed_count_closed"]
        checks += 1

    # Parity-twisted run matrices independently reproduce every receipt.
    for row in data["regression"]["wall_run_rows"]:
        n, m = row["n"], row["max_run_bound"]
        plain = int(sp.trace(run_matrix(m) ** n))
        signed = int(sp.trace(run_matrix(m, True) ** n))
        assert plain == row["cyclic_wall_words_all_parities"]
        assert (plain + signed) // 2 == row["cyclic_wall_words_even_parity"]
        checks += 2

    # Verify the local wall identity as a polynomial over F_2 for all eight
    # neighborhoods; this is separate from the producer's direct iteration.
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                x = (a, b, c)
                y = tuple(int(x[(i - 1) % 3] + x[i] + x[(i + 1) % 3] >= 2) for i in range(3))
                w = tuple(x[i] ^ x[(i + 1) % 3] for i in range(3))
                wp = tuple(y[i] ^ y[(i + 1) % 3] for i in range(3))
                pred = tuple(w[i] & (1 ^ w[(i - 1) % 3] ^ w[(i + 1) % 3]) for i in range(3))
                assert wp == pred
                checks += 1

    print(f"C251 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
