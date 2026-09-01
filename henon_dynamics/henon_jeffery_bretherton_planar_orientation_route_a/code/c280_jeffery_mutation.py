#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile mutation audit for HCS-C280."""
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
SOURCE = ROOT / "results/c280_jeffery_evidence.json"


def ph(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]: target = target[key]
    target[path[-1]] = value


base = json.loads(SOURCE.read_text())
mutations = [
    (("source_commit",), "0"*40), (("fixed_epoch",), 1), (("scope_literal",), "BROKEN"),
    (("evaluator", "sha256"), "0"*64), (("proof_contract", "status"), "HEURISTIC"),
    (("route_a", "tuple", 1), "A1_PASS_ANALYTIC"), (("route_a", "route_b_invocation_allowed"), True),
    (("scope_flags", "euler_factors"), True), (("regression", "counts", "parameter_rows"), 624),
    (("__consistent_offgrid_parameter__",), None),
    (("regression", "parameter_rows", 1, "regime"), "BROKEN"),
    (("regression", "orbit_rows", 0, "director", 0), "9.0"),
    (("regression", "orbit_rows", 1, "semigroup_defect"), "1.0"),
    (("regression", "shear_rows", 0, "director_equator_period"), "1.0"),
    (("regression", "strobe_rows", 2, "fixed_set"), "all_RP2"),
    (("regression", "orbit_rows", 2, "regime"), "BROKEN"),
    (("regression", "strobe_rows", 1, "time"), "9.0"),
    (("regression", "boundary_rows", 1, "status"), "unmarked sphere has an intrinsic axis"),
    (("regression", "orbit_rows", -1), copy.deepcopy(base["regression"]["orbit_rows"][0])),
    (("regression", "shear_rows", -1), copy.deepcopy(base["regression"]["shear_rows"][0])),
    (("model_contract", "sphere_convention"), "an unmarked sphere has an intrinsic shape director"),
    (("classification_contract", "hyperbolic"), "separatrices are projective planes without endpoint exclusions"),
    (("simple_shear_contract", "domain"), "period formulas also hold at gamma=0"),
    (("simple_shear_contract", "oriented_period"), "the vertical oriented vector has the nonzero shear period"),
]
accepted = 0
with tempfile.TemporaryDirectory(prefix="c280-mutation-") as temp:
    for index, (path, value) in enumerate(mutations):
        trial = copy.deepcopy(base)
        if path == ("__consistent_offgrid_parameter__",):
            row = trial["regression"]["parameter_rows"][0]
            row.update({
                "a": "-5/2", "B2": ["2/1", "8/5", "8/5", "-2/1"],
                "delta": "164/25", "rank_B2": 2,
                "regime": "hyperbolic", "projective_fixed_set": "three_eigenlines",
            })
        else:
            set_path(trial, path, value)
        trial["payload_sha256"] = ph(trial)
        candidate = Path(temp) / f"m{index}.json"
        candidate.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        env = dict(os.environ); env["C280_EVIDENCE"] = str(candidate); env["PYTHONDONTWRITEBYTECODE"] = "1"
        run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c280_jeffery_checker.py")], env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        accepted += run.returncode != 0
    stale = copy.deepcopy(base)
    stale["headline"] += " tampered"
    candidate = Path(temp) / "stale.json"
    candidate.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    env = dict(os.environ); env["C280_EVIDENCE"] = str(candidate); env["PYTHONDONTWRITEBYTECODE"] = "1"
    run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c280_jeffery_checker.py")], env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    accepted += run.returncode != 0
total = len(mutations)+1
assert accepted == total
print(f"C280 hostile mutation audit: PASS {accepted}/{total} (repaired semantic mutations plus stale-hash control)")
