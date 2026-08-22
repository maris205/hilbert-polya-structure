#!/usr/bin/env python3
"""Independent symbolic determinant and trace check."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
doc = json.loads((ROOT / "results/c107_open_hole_evidence.json").read_text())
B = sp.Matrix([[1, 0, 1], [1, 0, 0], [0, 1, 0]])
z = sp.Symbol("z")
assert sp.expand((sp.eye(3) - z * B).det()) == sp.expand(sp.sympify(doc["escape_determinant"]))
assert [int((B**n).trace()) for n in range(1, 13)] == [doc["trace_counts"][str(n)] for n in range(1, 13)]
print("C107_SYMPY_PASS")
