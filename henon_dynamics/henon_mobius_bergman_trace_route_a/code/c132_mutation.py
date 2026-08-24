#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash mutation suite for C132."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("c132_checker", ROOT / "code/c132_mobius_bergman_checker.py")
checker = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(checker)
base = json.loads((ROOT / "results/c132_mobius_bergman_evidence.json").read_text())


def trial(path, value, repair=True):
    data = copy.deepcopy(base)
    node = data
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        data.pop("payload_sha256", None)
        payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


mutations = [
    (["unexpected_top_level"], True, True),
    (["schema"], "bad", True),
    (["digits", 0], 2, True),
    (["branches"], "affine", True),
    (["mobius_matrices", "3", 0, 1], 2, True),
    (["geometry", "branch_images", 0, "image_center"], "1/2", True),
    (["geometry", "closed_image_separation_gap"], "0/1", True),
    (["geometry", "strong_separation"], False, True),
    (["operator", "space"], "L2 boundary", True),
    (["operator", "trace_class"], False, True),
    (["operator", "trace_norm_upper_bound"], "1/1", True),
    (["all_word_theorem", "fixed_polynomial"], "linear", True),
    (["all_word_theorem", "multiplier"], "absolute value", True),
    (["all_word_theorem", "composition_trace"], "1/(1+lambda)", True),
    (["all_word_theorem", "all_n_trace"], "cutoff only", True),
    (["period_receipts_through_10", 0, "rooted_words"], 3, True),
    (["period_receipts_through_10", 3, "primitive_cycles"], 4, True),
    (["period_receipts_through_10", 5, "trace_case_sha256"], "0" * 64, True),
    (["period_receipts_through_10", 8, "trace_sum_decimal_30"], "0", True),
    (["total_rooted_word_receipts"], 2045, True),
    (["primitive_fredholm_product", "raw_absolute_convergence"], "all z", True),
    (["primitive_fredholm_product", "global_statement"], "raw product entire", True),
    (["order_sensitive_anagram_control", "not_cyclic_rotations"], False, True),
    (["order_sensitive_anagram_control", "first", "matrix", 0, 0], 64, True),
    (["order_sensitive_anagram_control", "first", "word"], "33636", True),
    (["order_sensitive_anagram_control", "second", "trace"], 1344, True),
    (["order_sensitive_anagram_control", "multiplier_differs"], False, True),
    (["progress", "common_linear_location_blindness_repaired"], "EXTERNAL_PHASE", True),
    (["checks", "anagram_control_pass"], False, True),
    (["checks", "unexpected_receipt"], True, True),
    (["route_a", "tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], True),
    (["route_a", "structural_gate"], "FAIL", True),
    (["route_a", "route_b_invocation_allowed"], True, True),
    (["scope_flags", "claims_euler_factors"], True, True),
    (["scope_flags", "claims_hilbert_polya"], True, True),
    (["scope_flags", "renamed_false_flag"], False, True),
    (["payload_sha256"], "0" * 64, False),
]
caught = 0
for path, value, repair in mutations:
    try:
        checker.validate(trial(path, value, repair))
    except (AssertionError, KeyError, ValueError):
        caught += 1
assert caught == len(mutations)
print(f"C132 mutation suite: PASS ({caught}/{len(mutations)} mutations rejected)")
