#!/usr/bin/env python3
"""Hostile repaired-hash mutation rejection for HCS-C263."""
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
EVIDENCE = ROOT / "results/c263_polya_evidence.json"
CHECKER = ROOT / "code/c263_polya_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main():
    base = json.loads(EVIDENCE.read_text())
    mutations = [
        ("candidate", ["candidate_id"], "HCS-C262"),
        ("source", ["source_commit"], "0" * 40),
        ("scope", ["scope_literal"], "OPEN"),
        ("evaluator", ["evaluator", "sha256"], "0" * 64),
        ("tuple", ["route_a", "tuple", 1], "A1_WEAK"),
        ("verdict", ["route_a", "overall"], "ROUTE_A_EXPLORATORY"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope_flag", ["scope_flags", "claims_euler_factor"], True),
        ("case_c", ["regression", "cases", 1, "reinforcement"], 2),
        ("case_alpha", ["regression", "cases", 1, "normalization", 0], "2/1"),
        ("composition", ["regression", "composition_rows", 5, "closed_probability"], "2/1"),
        ("recursive", ["regression", "composition_rows", 7, "recursive_probability"], "0/1"),
        ("multiplicity", ["regression", "composition_rows", 12, "multiplicity"], 99),
        ("marginal", ["regression", "marginal_rows", 10, "closed"], "7/11"),
        ("mean", ["regression", "moment_rows", 8, "mean", 0], "99/1"),
        ("covariance", ["regression", "moment_rows", 10, "covariance", 0, 0], "7/3"),
        ("factorial", ["regression", "factorial_rows", 5, "closed"], "8/7"),
        ("martingale", ["regression", "martingale_rows", 5, "expected_next"], "8/7"),
        ("word", ["regression", "ordered_word_rows", 10, "probability"], "8/7"),
        ("word_count", ["regression", "exchangeability_rows", 3, "word_count"], 999),
        ("de_finetti", ["regression", "de_finetti_rows", 3, "dirichlet_monomial_moment"], "8/7"),
        ("row_count", ["regression", "counts", "composition_rows"], 1),
    ]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    rejected = 0
    with tempfile.TemporaryDirectory() as tmp:
        for name, path, value in mutations:
            mutant = copy.deepcopy(base)
            set_path(mutant, path, value)
            mutant["payload_sha256"] = payload_hash(mutant)
            target = Path(tmp) / f"{name}.json"
            target.write_text(json.dumps(mutant, sort_keys=True, indent=2) + "\n")
            result = subprocess.run(
                [sys.executable, "-B", str(CHECKER), str(target)],
                env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            assert result.returncode != 0, name
            rejected += 1
        stale = copy.deepcopy(base)
        stale["headline"] += " mutated"
        target = Path(tmp) / "stale_hash.json"
        target.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(target)],
            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        assert result.returncode != 0
        rejected += 1
    total = len(mutations) + 1
    print(f"C263_MUTATION_PASS {rejected}/{total} (repaired-hash semantic plus stale-hash rejection)")


if __name__ == "__main__":
    main()
