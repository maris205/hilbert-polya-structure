#!/usr/bin/env python3
"""Hostile semantic mutations for the C78 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c78_repair_distance_geometry_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c78_repair_distance_geometry_checker.py"


def mutate(document, path, value):
    result = deepcopy(document)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main():
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c78-mutated-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "c77_authority": mutate(original, ["authority", "c77"], "0" * 64),
        "c77_manifest": mutate(original, ["authority", "c77_manifest"], "1" * 64),
        "c76_authority": mutate(original, ["authority", "c76"], "2" * 64),
        "c76_manifest": mutate(original, ["authority", "c76_manifest"], "3" * 64),
        "c73_authority": mutate(original, ["authority", "c73"], "2" * 64),
        "definition_formula": mutate(original, ["definition", "formula"], "rho=0"),
        "pivot": mutate(original, ["definition", "pivot"], "S1"),
        "block_size": mutate(original, ["definition", "direction_block_sizes", 0], 2),
        "max_distance": mutate(original, ["definition", "maximum_distance"], 2),
        "distance_distribution": mutate(original, ["repair_distance_atlas", "deletion_count_distribution", "3"], 65),
        "retained_row": mutate(original, ["repair_distance_atlas", "by_retained_cardinality", 3, "distance_counts", "0"], 26),
        "distance_mask": mutate(original, ["repair_distance_atlas", "distance_three_masks", 0], 0),
        "coefficient": mutate(original, ["bivariate_generating_function", "coefficient_table", "0,0"], 2),
        "x_marginal": mutate(original, ["bivariate_generating_function", "P_x_at_y1", "0"], 2),
        "y_marginal": mutate(original, ["bivariate_generating_function", "P_1_at_y", "3"], 65),
        "claim_distance": mutate(original, ["claims", "exact_minimum_repair_distance"], False),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c78-mutations-") as temp:
        for name, document in mutations.items():
            path = Path(temp) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "MUTATION_TEST_PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
