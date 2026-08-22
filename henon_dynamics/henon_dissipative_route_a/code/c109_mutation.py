#!/usr/bin/env python3
"""Hostile mutation audit: altered evidence must be rejected by the checker."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
evidence = PROJECT / "results/c109_dissipative_evidence.json"
checker = PROJECT / "code/c109_dissipative_checker.py"
original_bytes = evidence.read_bytes()
original = json.loads(original_bytes)

mutations = []
d = copy.deepcopy(original)
d["map"]["b"] = "1/3"
mutations.append(("dissipation", d))
d = copy.deepcopy(original)
d["period_two_resultant"] = "1"
mutations.append(("resultant", d))
d = copy.deepcopy(original)
d["cycle_ledger"][2]["local_weight"] = "-2"
mutations.append(("local_weight", d))
d = copy.deepcopy(original)
d["transition"]["q_plus"] = "q_plus"
mutations.append(("transition", d))
d = copy.deepcopy(original)
d["witness_matrix"][0][0] = "1"
mutations.append(("matrix", d))
d = copy.deepcopy(original)
d["weighted_trace_sequence_n1_to_6"]["2"] = "0"
mutations.append(("trace", d))
d = copy.deepcopy(original)
d["finite_witness_determinant_coefficients"]["2"] = "1"
mutations.append(("determinant", d))
d = copy.deepcopy(original)
d["verdict"]["A2"] = "A2_ANALYTIC_FREDHOLM"
mutations.append(("verdict", d))

rejected = 0
try:
    for name, mutated in mutations:
        evidence.write_text(json.dumps(mutated, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        proc = subprocess.run([sys.executable, str(checker)], capture_output=True, text=True)
        assert proc.returncode != 0, name
        rejected += 1
finally:
    evidence.write_bytes(original_bytes)

assert evidence.read_bytes() == original_bytes
print(f"C109_MUTATION_PASS {rejected}/{len(mutations)}")
