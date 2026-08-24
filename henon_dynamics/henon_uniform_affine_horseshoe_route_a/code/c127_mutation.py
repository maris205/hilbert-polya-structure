#!/usr/bin/env python3
"""Hostile mutation tests for the C127 evidence checker."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("checker", ROOT / "code" / "c127_uniform_horseshoe_checker.py")
checker = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(checker)
base = json.loads((ROOT / "results" / "c127_uniform_horseshoe_evidence.json").read_text())


def mutate(path, value, repair=True):
    trial = copy.deepcopy(base)
    node = trial
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        trial.pop("payload_sha256", None)
        canonical = json.dumps(trial, sort_keys=True, separators=(",", ":")).encode()
        trial["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return trial


tests = [
    (["schema"], "bad"),
    (["uniform_certificates", "minimum_domain_gap"], "1/4"),
    (["uniform_certificates", "maximum_trace_norm"], "2/1"),
    (["audit_grid", 0, "domain_gap"], "0/1"),
    (["audit_grid", 0, "periods", 0, "fixed_points"], 3),
    (["audit_grid", 1, "periods", 4, "primitive_cycles"], 99),
    (["sample_parameter", "lambda"], "4/1"),
    (["sample_periodic_points", 0, "x0"], "999/1"),
    (["sample_periodic_points", 0, "y0"], "999/1"),
    (["sample_periodic_points", 0, "word"], "1"),
    (["sample_periodic_points", 0, "closes"], False),
    (["checks", "uniform_parameter_theorem_pass"], False),
    (["route_a", "tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]),
    (["route_a", "route_b_invocation_allowed"], True),
    (["scope_flags", "uses_prime_table"], True),
    (["payload_sha256"], "0" * 64, False),
]

caught = 0
for item in tests:
    if len(item) == 2:
        path, value = item
        repair = True
    else:
        path, value, repair = item
    try:
        checker.validate(mutate(path, value, repair))
    except (AssertionError, KeyError, ValueError):
        caught += 1
assert caught == len(tests)
print(f"C127 mutation suite: PASS ({caught}/{len(tests)} mutations rejected)")
