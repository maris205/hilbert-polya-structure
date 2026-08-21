#!/usr/bin/env python3
"""Hostile semantic mutation audit for C81."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c81_effective_orbit_repair_profile_evidence.json"
CHECKER = PROJECT / "code/c81_effective_orbit_repair_profile_checker.py"


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
        "c80_hash": mutate(original, ["authority", "c80"], "1" * 64),
        "ambient_order": mutate(original, ["source_model", "c75_ambient_lift_order"], 1920),
        "effective_order": mutate(original, ["source_model", "effective_label_group_order"], 11520),
        "orbit_count": mutate(original, ["orbit_quotient", "orbit_count"], 3025),
        "orbit_size": mutate(original, ["orbit_quotient", "rows", 0, "orbit_size"], 2),
        "representative": mutate(original, ["orbit_quotient", "rows", 1, "representative_mask"], 65535),
        "profile_rho": mutate(original, ["orbit_quotient", "rows", 2, "profile", "rho"], 9),
        "fixed_spectrum": mutate(original, ["orbit_quotient", "fixed_support_count_spectrum", "1"], 0),
        "marginal": mutate(original, ["repair_profile_marginals", "mask_count_by_rho_witness", "3,25"], 65),
        "claim": mutate(original, ["claims", "effective_1920_label_orbit_quotient"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c81-mutations-") as directory:
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
    print(json.dumps({"status": "C81_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
