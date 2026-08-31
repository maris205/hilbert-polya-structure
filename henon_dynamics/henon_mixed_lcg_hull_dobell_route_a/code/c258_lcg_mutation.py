#!/usr/bin/env python3
"""Semantic hostile mutations for the HCS-C258 certificate."""
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c258_lcg_evidence.json"
CHECKER = ROOT / "code/c258_lcg_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def mutate(path, value):
    data = copy.deepcopy(BASE)
    node = data
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    data["payload_sha256"] = payload_hash(data)
    return data


BASE = json.loads(EVIDENCE.read_text())
MUTATIONS = [
    (["schema"], "bad-schema"),
    (["candidate_id"], "HCS-C257"),
    (["evaluation_date"], "2026-08-30"),
    (["source_commit"], "0" * 40),
    (["fixed_epoch"], 0),
    (["scope_literal"], "BAD_SCOPE"),
    (["evaluator", "path"], "wrong.md"),
    (["evaluator", "version"], "0.1.0"),
    (["evaluator", "sha256"], "0" * 64),
    (["headline"], "affine map"),
    (["frozen_object", "map"], "F(x)=a*x-c mod m"),
    (["frozen_object", "clock"], "two updates"),
    (["frozen_object", "normalization"], "floating residues"),
    (["frozen_object", "determinant_convention"], "target determinant"),
    (["frozen_object", "arithmetic_origin"], "fitted primes"),
    (["frozen_object", "forbidden_data"], "none"),
    (["theorem", "criterion"], "gcd(a,m)=1"),
    (["theorem", "iterate"], "wrong iterate"),
    (["theorem", "local_return"], "wrong valuation"),
    (["theorem", "crt"], "sum of periods"),
    (["theorem", "primitive"], "many primitive orbits"),
    (["theorem", "fixed_counts"], "always m"),
    (["theorem", "zeta"], "1/(1-2*t)"),
    (["theorem", "koopman"], "spectral only"),
    (["theorem", "boundaries"], "no boundary"),
    (["theorem", "route_boundary"], "target match"),
    (["regression", "max_modulus"], 95),
    (["regression", "criterion_mismatch_count"], 1),
    (["regression", "modulus_rows", 0, "m"], 3),
    (["regression", "modulus_rows", 1, "predicted_full_parameter_pairs"], 999),
    (["regression", "cycle_cases", 0, "fixed_counts_n1_to_2m"], [8]),
    (["route_a", "tuple"], ["A0_FAIL"]),
    (["route_a", "overall"], "ROUTE_A_STRONG_CANDIDATE"),
    (["route_a", "route_b_invocation_allowed"], True),
    (["scope_flags", "claims_euler_factors"], True),
    (["citations", 0, "doi"], "10.0000/fake"),
    (["nonclaims"], []),
]

passed = 0
env = dict(os.environ)
env["PYTHONDONTWRITEBYTECODE"] = "1"
with tempfile.TemporaryDirectory(prefix="c258-mutation-") as tmp:
    for index, (path, value) in enumerate(MUTATIONS):
        target = Path(tmp) / f"mutation-{index}.json"
        target.write_text(json.dumps(mutate(path, value), sort_keys=True, indent=2) + "\n")
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--quick", "--evidence", str(target)],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode == 0:
            raise AssertionError(f"mutation survived: {path}")
        passed += 1

print(f"C258 hostile mutation: PASS {passed}/{len(MUTATIONS)}")
