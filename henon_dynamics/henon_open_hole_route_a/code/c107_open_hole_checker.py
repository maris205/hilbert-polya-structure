#!/usr/bin/env python3
"""Independent checker for the C107 open survivor."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
doc = json.loads((ROOT / "results/c107_open_hole_evidence.json").read_text())
A = sp.Matrix(doc["source"]["adjacency_source_rows_target_columns"])
hole = int(doc["source"]["hole_state"])
keep = [i for i in range(4) if i != hole]
B = A.extract(keep, keep)
z = sp.Symbol("z")
assert doc["survivor_states"] == keep
assert doc["open_matrix"] == B.tolist()
assert sp.factor((sp.eye(3) - z * B).det()) == sp.sympify(doc["escape_determinant"])
traces = {str(n): int((B**n).trace()) for n in range(1, 13)}
assert traces == {str(k): v for k, v in doc["trace_counts"].items()}
prim = {}
for n in range(1, 13):
    left = int(traces[str(n)])
    for d, p in prim.items():
        if n % d == 0:
            left -= d * p
    assert left % n == 0
    prim[n] = left // n
assert {str(k): v for k, v in prim.items()} == {str(k): v for k, v in doc["primitive_necklace_counts"].items()}
assert doc["alternative_hole_determinants"] == {"0": "1", "1": "1 - z", "2": "1 - z", "3": "-z**3 - z + 1"}
assert doc["verdict"]["A1"] == "A1_PARTIAL_CERTIFIED"
assert doc["verdict"]["A2"] == "A2_CERTIFIED_PREFIX"
print("C107_CHECK_PASS")
