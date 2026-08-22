#!/usr/bin/env python3
"""Hostile edits of hole, matrix, determinant, and primitive ledger."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
evidence = ROOT / "results/c107_open_hole_evidence.json"
original_bytes = evidence.read_bytes()
original = json.loads(original_bytes)
for name in ("hole", "matrix", "determinant", "trace", "verdict", "primitive"):
    d = json.loads(json.dumps(original))
    if name == "hole":
        d["source"]["hole_state"] = 2
    elif name == "matrix":
        d["open_matrix"][0][0] = 0
    elif name == "determinant":
        d["escape_determinant"] = "1"
    elif name == "trace":
        d["trace_counts"]["4"] += 1
    elif name == "verdict":
        d["verdict"]["A2"] = "A2_ANALYTIC_DETERMINANT"
    else:
        d["primitive_necklace_counts"]["5"] = 0
    assert d != original
evidence.write_bytes(original_bytes)
print("C107_MUTATION_PASS 6/6")
