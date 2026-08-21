#!/usr/bin/env python3
"""Hostile semantic mutation audit for C86."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c86_effective_orbit_flip_chain_evidence.json"
CHECKER = PROJECT / "code/c86_effective_orbit_flip_chain_checker.py"


def mutate(value, path, replacement):
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c75_hash": mutate(original, ["authority", "c75"], "0" * 64),
        "c81_manifest": mutate(original, ["authority", "c81_manifest"], "1" * 64),
        "ambient_order": mutate(original, ["definition", "ambient_lift_order"], 1920),
        "effective_order": mutate(original, ["definition", "effective_label_group_order"], 11520),
        "orbit_count": mutate(original, ["quotient_chain", "orbit_count"], 3023),
        "directed_arcs": mutate(original, ["quotient_chain", "directed_nonzero_arc_count"], 30239),
        "row_sum": mutate(original, ["quotient_chain", "row_sum"], 15),
        "neighbor_spectrum": mutate(original, ["quotient_chain", "neighbor_orbit_count_spectrum", "10"], 799),
        "entry_spectrum": mutate(original, ["quotient_chain", "positive_entry_multiplicity_spectrum", "5"], 1007),
        "balance": mutate(original, ["quotient_chain", "weighted_detailed_balance_verified"], False),
        "row_representative": mutate(original, ["quotient_chain", "rows", 0, "representative_mask"], 1),
        "row_transition": mutate(original, ["quotient_chain", "rows", 0, "transitions", 0, "multiplicity"], 15),
        "repair_flow": mutate(original, ["repair_flow", "actual_directed_edge_count", "0,0"], 445695),
        "c82_identity": mutate(original, ["repair_flow", "c82_distance_one_recovered"], False),
        "spectrum": mutate(original, ["invariant_walsh_spectrum", "rows", 8, "multiplicity"], 449),
        "moment": mutate(original, ["invariant_walsh_spectrum", "second_moment"], 77759),
        "claim": mutate(original, ["claims", "effective_1920_action_used"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c86-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes((json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            if run.returncode:
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C86_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
