#!/usr/bin/env python3
"""Symbolic cross-checks for the open-TASEP theorem.

The implementation is separate from both producer and checker and uses
SymPy's exact rational-function simplifier on short words and generators.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c220_tasep_evidence.json"


def dehp(word: str, x: sp.Expr, y: sp.Expr) -> sp.Expr:
    if not word:
        return sp.Integer(1)
    if word[0] == "E":
        return x * dehp(word[1:], x, y)
    if word[-1] == "D":
        return y * dehp(word[:-1], x, y)
    p = word.find("DE")
    if p < 0:
        raise AssertionError(word)
    return dehp(word[:p] + "D" + word[p + 2:], x, y) + dehp(word[:p] + "E" + word[p + 2:], x, y)


def closed_z(L: int, x: sp.Expr, y: sp.Expr) -> sp.Expr:
    if L == 0:
        return sp.Integer(1)
    out = sp.Integer(0)
    for p in range(1, L + 1):
        c = sp.Rational(p * factorial(2 * L - 1 - p), factorial(L) * factorial(L - p))
        out += c * (p + 1) * x ** p if x == y else c * (y ** (p + 1) - x ** (p + 1)) / (y - x)
    return sp.factor(out)


def generator(L: int, alpha: sp.Expr, beta: sp.Expr) -> sp.Matrix:
    size = 1 << L
    Q = sp.zeros(size, size)

    def add(i: int, j: int, rate: sp.Expr) -> None:
        Q[i, j] += rate
        Q[i, i] -= rate

    if L == 0:
        return Q
    for mask in range(size):
        if not (mask & 1):
            add(mask, mask | 1, alpha)
        for i in range(L - 1):
            if (mask & (1 << i)) and not (mask & (1 << (i + 1))):
                add(mask, mask ^ (1 << i) ^ (1 << (i + 1)), sp.Integer(1))
        if mask & (1 << (L - 1)):
            add(mask, mask ^ (1 << (L - 1)), beta)
    return Q


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    evidence = json.loads(parser.parse_args().evidence.read_text())
    checks = 0

    def ok(value, message: str) -> None:
        nonlocal checks
        checks += 1
        if isinstance(value, sp.MatrixBase):
            good = all(sp.simplify(v) == 0 for v in value)
        else:
            good = sp.simplify(value) == 0
        if not good:
            raise AssertionError(message)

    x, y = sp.symbols("x y", positive=True)
    # Local algebra on every word through length five.
    for L in range(0, 6):
        for mask in range(1 << L):
            w = "".join("D" if (mask >> i) & 1 else "E" for i in range(L))
            for pos in range(L + 1):
                u, v = w[:pos], w[pos:]
                ok(dehp(u + "DE" + v, x, y) - dehp(u + "D" + v, x, y) - dehp(u + "E" + v, x, y), f"DE relation {w}/{pos}")

    # Z_N identity and the equal-rate divided-difference limit.
    for L in range(0, 6):
        direct = sp.expand(sum(dehp("".join("D" if (m >> i) & 1 else "E" for i in range(L)), x, y) for m in range(1 << L)))
        ok(direct - closed_z(L, x, y), f"Z closed L={L}")
    for p in range(1, 7):
        ok(sp.limit((y ** (p + 1) - x ** (p + 1)) / (y - x), y, x) - (p + 1) * x ** p, f"divided difference p={p}")

    # Exact stationary null vectors and current equality for L<=3.
    alpha, beta = 1 / x, 1 / y
    for L in range(0, 4):
        size = 1 << L
        weights = sp.Matrix([dehp("".join("D" if (m >> i) & 1 else "E" for i in range(L)), x, y) for m in range(size)])
        Z = sp.simplify(sum(weights))
        Q = generator(L, alpha, beta)
        for row in range(size):
            ok(sum(Q[row, col] for col in range(size)), f"generator row sum L={L},row={row}")
        for col in range(size):
            ok(sum(weights[row] * Q[row, col] for row in range(size)), f"stationarity L={L},col={col}")
        if L:
            currents = [sp.simplify(alpha * sum(weights[m] for m in range(size) if not (m & 1)) / Z)]
            currents.extend(sp.simplify(sum(weights[m] for m in range(size) if (m & (1 << i)) and not (m & (1 << (i + 1)))) / Z) for i in range(L - 1))
            currents.append(sp.simplify(beta * sum(weights[m] for m in range(size) if m & (1 << (L - 1))) / Z))
            for c in currents[1:]:
                ok(c - currents[0], f"current equality L={L}")
            expected = sp.Integer(1) / Z if L == 1 else closed_z(L - 1, x, y) / Z
            ok(currents[0] - expected, f"current ratio L={L}")

    rows = evidence["regression"]["interior_rows"]
    checks += len(rows)
    if not all(r["case_id"].startswith("L") and "_a" in r["case_id"] and "_b" in r["case_id"] for r in rows):
        raise AssertionError("evidence row ids")
    phase_rows = evidence["regression"]["phase_rows"]
    ok(len(phase_rows) - 7, "phase-row count")
    corner = next((r for r in phase_rows if r.get("phase_id") == "CRIT_CORNER"), None)
    if corner is None:
        raise AssertionError("missing CRIT_CORNER")
    ok(sp.Integer(0) if corner["condition"] == "alpha=beta=1/2" else sp.Integer(1), "critical corner condition")
    ok(sp.Integer(0) if corner["bulk_density"] == "1/2" and corner["current"] == "1/4" else sp.Integer(1), "critical corner values")
    coexistence = next((r for r in phase_rows if r.get("phase_id") == "COEXISTENCE"), None)
    if coexistence is None:
        raise AssertionError("missing COEXISTENCE")
    ok(sp.Integer(0) if coexistence["condition"] == "0<alpha=beta<1/2" else sp.Integer(1), "positive-rate coexistence condition")
    print(json.dumps({"status": "C220_SYMPY_PASS", "checks": checks, "word_algebra_checks": sum((1 << L) * (L + 1) for L in range(6)), "evidence_row_checks": len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
