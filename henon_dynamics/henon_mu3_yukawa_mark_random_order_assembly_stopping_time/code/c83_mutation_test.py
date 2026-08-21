#!/usr/bin/env python3
"""Hostile semantic mutation audit for C83."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c83_random_order_stopping_time_evidence.json"
CHECKER = PROJECT / "code/c83_random_order_stopping_time_checker.py"


def mutate(value, path, replacement):
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return result


def main():
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c76_hash": mutate(original, ["authority", "c76"], "0" * 64),
        "c78_manifest": mutate(original, ["authority", "c78_manifest"], "1" * 64),
        "time_range": mutate(original, ["definition", "time_range", 0], 2),
        "formula": mutate(original, ["definition", "pivotal_formula"], "N=0"),
        "full_support": mutate(original, ["assembly_atlas", "full_support_count_by_cardinality", "3"], 24),
        "pivotal": mutate(original, ["assembly_atlas", "pivotal_support_count_by_cardinality", "3"], 24),
        "pattern": mutate(original, ["assembly_atlas", "pivotal_pattern_counts", "3,3"], 24),
        "stopping": mutate(original, ["assembly_atlas", "permutation_count_by_stopping_time", "3"], 0),
        "probability": mutate(original, ["assembly_atlas", "probability_by_stopping_time", "3", "numerator"], 1),
        "survival": mutate(original, ["assembly_atlas", "survival_permutation_counts", "3"], 0),
        "expectation": mutate(original, ["assembly_atlas", "expected_stopping_time", "numerator"], 1),
        "claim": mutate(original, ["claims", "exact_uniform_permutation_distribution"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c83-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes((json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            if run.returncode != 0:
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C83_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
