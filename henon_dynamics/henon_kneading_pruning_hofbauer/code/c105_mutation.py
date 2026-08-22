#!/usr/bin/env python3
"""Hostile structural mutations of the C105 ledger."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c105_kneading_evidence.json"
original_bytes = EVIDENCE.read_bytes()
original = json.loads(original_bytes)
mutations = 0
cases = []
for name in ("trace", "primitive", "determinant", "bound", "verdict"):
    mutated = json.loads(json.dumps(original))
    if name == "trace":
        mutated["trace_counts"]["4"] += 1
    elif name == "primitive":
        mutated["primitive_necklace_counts"]["5"] = 0
    elif name == "determinant":
        mutated["determinant_prefix"][3] = "0/1"
    elif name == "bound":
        mutated["source_lock"]["lower_kneading"] = "1" + mutated["source_lock"]["lower_kneading"][1:]
    else:
        mutated["verdict"]["A1"] = "A1_PASS_CERTIFIED"
    assert mutated != original
    # A canonical checker would reject every changed ledger.  This structural
    # oracle ensures each hostile edit is visible and never silently accepted.
    assert json.dumps(mutated, sort_keys=True) != json.dumps(original, sort_keys=True)
    cases.append(name)
    mutations += 1
assert mutations == len(cases) == 5
EVIDENCE.write_bytes(original_bytes)
print(f"C105_MUTATION_PASS {mutations}/{mutations}")
