#!/usr/bin/env python3
"""SymPy-rational reconstruction of the C188 cycle, power, CSR, and orbit ledger."""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Optional

import sympy as sp


Entry = Optional[sp.Rational]
Matrix = tuple[tuple[Entry, ...], ...]
Vector = tuple[Entry, ...]
NEG: Entry = None
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c188_max_plus_evidence.json"
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def dec(text: str) -> Entry:
    return NEG if text == "-inf" else sp.Rational(text)


def matrix(raw: list[list[str]]) -> Matrix:
    return tuple(tuple(dec(x) for x in row) for row in raw)


def vector(raw: list[str]) -> Vector:
    return tuple(dec(x) for x in raw)


def eye(n: int) -> Matrix:
    return tuple(tuple(sp.Integer(0) if i == j else NEG for j in range(n)) for i in range(n))


def mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            vals = [a[i][k] + b[k][j] for k in range(n) if a[i][k] is not NEG and b[k][j] is not NEG]
            row.append(max(vals) if vals else NEG)
        rows.append(tuple(row))
    return tuple(rows)


def power(a: Matrix, exponent: int) -> Matrix:
    result = eye(len(a))
    for _ in range(exponent):
        result = mul(result, a)
    return result


def apply(a: Matrix, x: Vector) -> Vector:
    result = []
    for row in a:
        vals = [aij + xj for aij, xj in zip(row, x) if aij is not NEG and xj is not NEG]
        result.append(max(vals) if vals else NEG)
    return tuple(result)


def projective(x: Vector) -> Vector:
    finite = [v for v in x if v is not NEG]
    m = max(finite)
    return tuple(NEG if v is NEG else sp.simplify(v - m) for v in x)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    finite = data["finite_regression"]
    matrix_by_id = {}
    for row in finite["matrix_rows"]:
        matrix_id = row["matrix_id"]
        a = matrix(row["A"])
        b = matrix(row["B"])
        n = len(a)
        lam = sp.Rational(row["lambda"])
        matrix_by_id[matrix_id] = (b, row)
        cycle_means = []
        for cycle in row["simple_cycles"]:
            nodes = cycle["nodes"]
            weight = sum((a[nodes[i]][nodes[(i + 1) % len(nodes)]] for i in range(len(nodes))), sp.Integer(0))
            mean = sp.cancel(weight / len(nodes))
            check(weight == sp.Rational(cycle["weight"]), f"cycle weight {matrix_id}")
            check(mean == sp.Rational(cycle["mean"]), f"cycle mean {matrix_id}")
            check(cycle["critical"] is (mean == lam), f"critical flag {matrix_id}")
            cycle_means.append(mean)
        check(max(cycle_means) == lam, f"lambda {matrix_id}")
        for i in range(n):
            for j in range(n):
                expected = NEG if a[i][j] is NEG else sp.cancel(a[i][j] - lam)
                check(b[i][j] == expected, f"normalized cell {matrix_id}:{i},{j}")
        gamma = row["gamma"]
        transient = row["minimal_transient"]
        p_t = power(b, transient)
        p_tg = power(b, transient + gamma)
        for i in range(n):
            for j in range(n):
                check(p_t[i][j] == p_tg[i][j], f"period cell {matrix_id}:{i},{j}")
        if transient:
            check(power(b, transient - 1) != power(b, transient - 1 + gamma), f"minimal transient {matrix_id}")
        for p in range(1, gamma):
            check(power(b, transient + p) != p_t, f"minimal period {matrix_id}:{p}")
        c, s, r = matrix(row["C"]), matrix(row["S"]), matrix(row["R"])
        csr_t = row["csr_transient"]
        for t in range(csr_t, csr_t + gamma + 1):
            lhs = mul(mul(c, power(s, t)), r)
            rhs = power(b, t)
            for i in range(n):
                for j in range(n):
                    check(lhs[i][j] == rhs[i][j], f"CSR cell {matrix_id}:{t}:{i},{j}")

    for vrow in finite["vector_rows"]:
        b, mrow = matrix_by_id[vrow["matrix_id"]]
        x = vector(vrow["x"])
        gamma = mrow["gamma"]
        transient = mrow["minimal_transient"]
        states = [apply(power(b, t), x) for t in range(transient + gamma + 1)]
        projected = [projective(y) for y in states]
        raw_period = next(p for p in divisors(gamma) if states[transient + p] == states[transient])
        proj_period = next(p for p in divisors(gamma) if projected[transient + p] == projected[transient])
        check(vrow["eventual_period"] == raw_period, f"vector period {vrow['matrix_id']}:{vrow['vector_id']}")
        check(vrow["projective_period"] == proj_period, f"projective period {vrow['matrix_id']}:{vrow['vector_id']}")
        check(gamma % raw_period == 0 and gamma % proj_period == 0, f"period divisibility {vrow['matrix_id']}")
        raw_t = next(t for t in range(transient + 1) if states[t + raw_period] == states[t])
        proj_t = next(t for t in range(transient + 1) if projected[t + proj_period] == projected[t])
        check(vrow["eventual_transient"] == raw_t, f"vector transient {vrow['matrix_id']}")
        check(vrow["projective_transient"] == proj_t, f"projective transient {vrow['matrix_id']}")

    m_symbol, t_symbol = sp.symbols("m t", integer=True, positive=True)
    formula = sp.Max(-t_symbol, -m_symbol)
    check(formula.subs({t_symbol: m_symbol - 1}) == 1 - m_symbol, "symbolic pretransient branch")
    check(formula.subs({t_symbol: m_symbol}) == -m_symbol, "symbolic threshold branch")
    check(formula.subs({t_symbol: m_symbol + 1}) == -m_symbol, "symbolic posttransient branch")
    for item in finite["unbounded_transient_family"]:
        m = item["m"]
        b = ((sp.Integer(0), -sp.Integer(m)), (sp.Integer(0), -sp.Integer(1)))
        for t in range(1, m + 2):
            check(power(b, t)[1][1] == max(-sp.Integer(t), -sp.Integer(m)), f"family formula {m}:{t}")
        check(power(b, m) == power(b, m + 1), f"family stop {m}")
        if m:
            check(power(b, m - 1) != power(b, m), f"family sharp {m}")

    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B false")
    print(json.dumps({"status": "C188_SYMPY_PASS", "checks": CHECKS, "matrices": len(matrix_by_id), "vectors": len(finite["vector_rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
