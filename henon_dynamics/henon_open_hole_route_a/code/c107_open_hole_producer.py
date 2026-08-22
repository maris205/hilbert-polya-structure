#!/usr/bin/env python3
"""Exact open-survivor pilot for a geometrically frozen H6 hole (C107)."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c107_open_hole_evidence.json"
GRAPH = sp.Matrix([[1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]])
HOLE = 3
NMAX = 12


def primitive_counts(traces: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for n in range(1, NMAX + 1):
        left = traces[n]
        for d, p in result.items():
            if n % d == 0:
                left -= d * p
        if left % n:
            raise AssertionError((n, left))
        result[n] = left // n
    return result


def main() -> None:
    keep = [i for i in range(4) if i != HOLE]
    B = GRAPH.extract(keep, keep)
    z = sp.Symbol("z")
    determinant = sp.factor((sp.eye(3) - z * B).det())
    traces = {n: int((B**n).trace()) for n in range(1, NMAX + 1)}
    prim = primitive_counts(traces)
    controls = {}
    for h in range(4):
        kk = [i for i in range(4) if i != h]
        controls[str(h)] = str(sp.factor((sp.eye(3) - z * GRAPH.extract(kk, kk)).det()))
    payload = {
        "schema": "hcs-c107-open-hole-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source": {
            "base": "certified H6 four-state local survivor interface",
        "adjacency_source_rows_target_columns": [[int(v) for v in row] for row in GRAPH.tolist()],
            "hole_state": HOLE,
            "hole_policy": "delete the frozen geometric rectangle/state 3 before every iterate",
        },
        "survivor_states": keep,
        "open_matrix": [[int(v) for v in row] for row in B.tolist()],
        "escape_determinant": str(determinant),
        "trace_counts": traces,
        "primitive_necklace_counts": prim,
        "alternative_hole_determinants": controls,
        "spectral_polynomial": str(sp.factor(B.charpoly().as_expr())),
        "verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "qualification": "symbolic open transfer only; analytic open Hénon operator remains open",
        },
        "nonclaims": ["full H6 repeller", "analytic open Fredholm determinant", "prime correspondence", "Riemann zeros", "Route B"],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    OUT.write_text(raw)
    print(json.dumps({"evidence_sha256": sha256(raw.encode()).hexdigest(), "determinant": str(determinant), "traces": traces, "primitive": prim}, sort_keys=True))


if __name__ == "__main__":
    main()
