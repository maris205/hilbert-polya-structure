#!/usr/bin/env python3
"""Repaired-hash semantic plus stale-hash mutation suite for C137."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("c137_checker", ROOT/"code/c137_uniform_mobius_checker.py")
checker = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(checker)
base = json.loads((ROOT/"results/c137_uniform_mobius_evidence.json").read_text())


def trial(path, value, repair=True):
    data = copy.deepcopy(base)
    node = data
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        data.pop("payload_sha256", None)
        data["payload_sha256"] = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return data


mutations = [
    (["unexpected_top_level"], True, True), (["schema"], "bad", True),
    (["candidate_id"], "HCS-X", True), (["scope"], "open", True),
    (["family","branches"], "affine", True), (["family","parameter_rectangle","a",1], "4/1", True),
    (["family","operator"], "weighted", True), (["uniform_geometry","minimum_gap"], "0/1", True),
    (["uniform_geometry","minimum_corner",0], "3/1", True), (["uniform_geometry","strong_separation_uniform"], False, True),
    (["uniform_geometry","negative_rectangle","minimum_gap"], "1/45", True), (["uniform_geometry","negative_rectangle","positive_closed_gap"], True, True),
    (["uniform_operator_bounds","trace_class"], False, True), (["uniform_operator_bounds","trace_norm_upper_bound"], "1/1", True),
    (["uniform_operator_bounds","a_lipschitz_constant"], "5/1", True), (["uniform_operator_bounds","b_lipschitz_constant"], "1/1", True),
    (["all_word_theorem","fixed_point"], "linear", True), (["all_word_theorem","composition_trace"], "wrong", True),
    (["all_word_theorem","raw_absolute_convergence"], "all z", True), (["all_word_theorem","determinant_global_domain"], "raw product entire", True),
    (["grid_receipts",0,"a"], "4/1", True), (["grid_receipts",0,"closed_image_gap"], "0/1", True),
    (["grid_receipts",0,"period_receipts_through_10",0,"rooted_words"], 3, True),
    (["grid_receipts",1,"period_receipts_through_10",4,"primitive_cycles"], 99, True),
    (["grid_receipts",2,"period_receipts_through_10",7,"trace_case_sha256"], "0"*64, True),
    (["grid_receipts",8,"trace_gap"], "0/1", True), (["receipt_summary","rooted_word_receipts_through_10"], 18413, True),
    (["receipt_summary","primitive_parameter_receipts_through_10"], 2033, True),
    (["order_sensitive_uniform_control","not_cyclic_rotations"], False, True),
    (["order_sensitive_uniform_control","trace_gap_identity"], "0", True),
    (["order_sensitive_uniform_control","uniform_trace_gap_lower_bound"], "0/1", True),
    (["order_sensitive_uniform_control","composition_trace_gap_positive"], False, True),
    (["progress","uniform_order_sensitivity"], "FAIL", True),
    (["route_a","tuple"], ["A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"], True),
    (["route_a","route_b_invocation_allowed"], True, True),
    (["scope_flags","claims_target_divisor"], True, True), (["scope_flags","claims_euler_factors"], True, True),
    (["scope_flags","claims_hilbert_polya"], True, True), (["scope_flags","renamed_false_flag"], False, True),
    (["nonclaims",0], "target match", True), (["payload_sha256"], "0"*64, False),
]
caught = 0
for path, value, repair in mutations:
    try:
        checker.validate(trial(path, value, repair))
    except (AssertionError, KeyError, ValueError, TypeError):
        caught += 1
assert caught == len(mutations)
print(f"C137 mutation suite: PASS ({caught}/{len(mutations)} rejected; {len(mutations)-1} repaired-hash + 1 stale-hash)")
