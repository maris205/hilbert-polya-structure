#!/usr/bin/env python3
"""Hostile semantic mutations for the C80 receipt."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c80_threshold_repair_atlas_evidence.json"
CHECKER = PROJECT / "code/c80_threshold_repair_atlas_checker.py"


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
        "c75_hash": mutate(original, ["authority", "c75"], "0" * 64),
        "c76_manifest": mutate(original, ["authority", "c76_manifest"], "1" * 64),
        "target_count": mutate(original, ["definition", "target_count"], 19),
        "target_order": mutate(original, ["definition", "target_index_order", 0], 1),
        "profile_threshold": mutate(original, ["target_atlas", "profile_rows", 123, "thresholds", 4], 9),
        "profile_mask": mutate(original, ["target_atlas", "profile_rows", 321, "deletion_mask"], 0),
        "distribution": mutate(original, ["target_atlas", "threshold_distributions", 19, "3"], 65),
        "table": mutate(original, ["target_atlas", "deleted_cardinality_tables", 19, "16,3"], 2),
        "q_check": mutate(original, ["checks", "tau_Q_equals_c78_rho"], False),
        "claim": mutate(original, ["claims", "full_table_of_marks_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c80-mutations-") as directory:
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
    print(json.dumps({"status": "C80_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
