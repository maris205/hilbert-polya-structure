#!/usr/bin/env python3
"""Hostile edits of exact cycle and ownership fields."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
evidence = ROOT / "results/c108_holomorphic_evidence.json"
original_bytes = evidence.read_bytes()
original = json.loads(original_bytes)
names = ("trace", "resultant", "degree", "verdict", "map")
for name in names:
    d = json.loads(json.dumps(original))
    if name == "trace":
        d["weighted_traces"]["2"] = "0"
    elif name == "resultant":
        d["period_two_resultant"] = "x"
    elif name == "degree":
        d["inverse_pullback_degree_growth"][2] = 7
    elif name == "verdict":
        d["verdict"]["A2"] = "A2_ANALYTIC_DETERMINANT"
    else:
        d["map"]["jacobian_determinant"] = "1"
    assert d != original
evidence.write_bytes(original_bytes)
print(f"C108_MUTATION_PASS {len(names)}/{len(names)}")
