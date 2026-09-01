#!/usr/bin/env python3
"""Repaired-hash semantic mutations and stale-hash control for HCS-C281."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/c281_ricci_evidence.json"


def ph(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]: target = target[key]
    target[path[-1]] = value


base = json.loads(SOURCE.read_text())
partial_collapse = next(i for i, row in enumerate(base["regression"]["collapse_rows"])
                        if row["partial_collapse"])
partial_asymptotic = next(i for i, row in enumerate(base["regression"]["asymptotic_rows"])
                          if row["normalized_time_tail"] != "infinity")
mutations = [
    (("source_commit",), "0"*40), (("fixed_epoch",), 1), (("scope_literal",), "BROKEN"),
    (("evaluator", "sha256"), "0"*64), (("proof_contract", "status"), "HEURISTIC"),
    (("route_a", "tuple", 1), "A1_WEAK"), (("route_a", "route_b_invocation_allowed"), True),
    (("scope_flags", "euler_factors"), True), (("regression", "counts", "flow_rows"), 67),
    (("regression", "case_rows", 0, "all_flat"), False),
    (("regression", "case_rows", 7, "collapsing_indices"), [0]),
    (("regression", "flow_rows", 0, "scalar_curvature"), "1/1"),
    (("regression", "case_rows", 1, "full_collapse"), True),
    (("regression", "normalized_rows", 0, "normalizing_scale"), "2.0"),
    (("regression", "case_rows", 8, "normalized_forward_endpoint"), "infinite_stationary_einstein"),
    (("regression", "collapse_rows", 0, "scalar_residue"), "99/1"),
    (("regression", "collapse_rows", 5, "full_collapse"), True),
    (("regression", "collapse_rows", 5, "pointed_blowup_euclidean_dimension"), 0),
    (("regression", "asymptotic_rows", 0, "scaled_scalar_residue"), "99.0"),
    (("regression", "covariance_rows", 0, "permutation_preserves_classification"), False),
    (("model_contract", "solution"), "BROKEN"),
    (("classification_contract", "partial_full_gate"), "BROKEN"),
    (("proof_contract", "scope"), "unbounded scope"),
    (("regression", "case_rows", 2, "dimensions"), [3]),
    (("regression", "case_rows", -1), copy.deepcopy(base["regression"]["case_rows"][0])),
    (("regression", "flow_rows", -1), copy.deepcopy(base["regression"]["flow_rows"][0])),
    (("regression", "normalized_rows", -1), copy.deepcopy(base["regression"]["normalized_rows"][0])),
    (("regression", "collapse_rows", -1), copy.deepcopy(base["regression"]["collapse_rows"][0])),
    (("regression", "asymptotic_rows", -1), copy.deepcopy(base["regression"]["asymptotic_rows"][0])),
    (("regression", "covariance_rows", -1), copy.deepcopy(base["regression"]["covariance_rows"][0])),
    (("regression", "boundary_rows", -1), copy.deepcopy(base["regression"]["boundary_rows"][0])),
    (("regression", "boundary_rows", 2, "status"), "BROKEN"),
    # Fail-closed schema and semantic-contract attacks added after hostile review.
    (("unexpected_top_level",), "must be rejected"),
    (("regression", "unexpected_nested_key"), "must be rejected"),
    (("regression", "boundary_rows", 0, "unexpected_row_key"), True),
    (("regression", "normalized_rows", 0, "normalized_scales"), []),
    (("regression", "normalized_rows", 0, "normalized_ode_rhs"), []),
    (("regression", "flow_rows", 0, "ode_residuals"), []),
    (("regression", "flow_rows", 0, "scales"), []),
    (("regression", "asymptotic_rows", partial_asymptotic, "normalized_scales"), []),
    (("regression", "asymptotic_rows", partial_asymptotic, "normalized_time_tail"), "999"),
    (("regression", "asymptotic_rows", partial_asymptotic, "normalized_time_tail"), "+inf"),
    (("regression", "collapse_rows", partial_collapse, "normalized_forward_endpoint"), "infinite_stationary_einstein"),
    (("collision_contract", "registry_range"), "tampered registry"),
    (("nonclaims", 0), "tampered nonclaim"),
    (("scope_flags", "unexpected_scope_flag"), False),
    (("headline",), "tampered but rehashed headline"),
]
drops = [
    ("nonclaims",),
    ("regression", "boundary_rows", 0, "status"),
    ("regression", "normalized_rows", 0, "normalized_ode_rhs"),
    ("regression", "collapse_rows", partial_collapse, "normalized_forward_endpoint"),
]
rejected = 0
with tempfile.TemporaryDirectory(prefix="c281-ricci-mutation-") as temp:
    for index, (path, value) in enumerate(mutations):
        trial = copy.deepcopy(base); set_path(trial, path, value); trial["payload_sha256"] = ph(trial)
        candidate = Path(temp) / f"m{index}.json"
        candidate.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        env = dict(os.environ); env["C281_EVIDENCE"] = str(candidate); env["PYTHONDONTWRITEBYTECODE"] = "1"
        run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c281_ricci_checker.py")], env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        rejected += run.returncode != 0
    for index, path in enumerate(drops, start=len(mutations)):
        trial = copy.deepcopy(base)
        target = trial
        for key in path[:-1]: target = target[key]
        del target[path[-1]]
        trial["payload_sha256"] = ph(trial)
        candidate = Path(temp) / f"m{index}.json"
        candidate.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        env = dict(os.environ); env["C281_EVIDENCE"] = str(candidate); env["PYTHONDONTWRITEBYTECODE"] = "1"
        run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c281_ricci_checker.py")], env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        rejected += run.returncode != 0
    stale = copy.deepcopy(base); stale["headline"] += " tampered"
    candidate = Path(temp) / "stale.json"
    candidate.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    env = dict(os.environ); env["C281_EVIDENCE"] = str(candidate); env["PYTHONDONTWRITEBYTECODE"] = "1"
    run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c281_ricci_checker.py")], env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    rejected += run.returncode != 0
total = len(mutations)+len(drops)+1
assert rejected == total
print(f"C281 hostile mutation audit: PASS {rejected}/{total} (repaired semantic mutations plus stale-hash control)")
