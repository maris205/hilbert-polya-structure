#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C79 receipt."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT / "code/c79_repair_witness_multiplicity_checker.py"
EVIDENCE = PROJECT / "results/c79_repair_witness_multiplicity_evidence.json"


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
        "schema": mutate(original, ["schema_id"], "bad-schema"),
        "status": mutate(original, ["status"], "PASS"),
        "scope": mutate(original, ["scope_literal"], "BAD_SCOPE"),
        "c78_hash": mutate(original, ["authority", "c78"], "0" * 64),
        "c78_manifest": mutate(original, ["authority", "c78_manifest"], "0" * 64),
        "definition_rho": mutate(original, ["definition", "rho_formula"], "rho=0"),
        "definition_witness": mutate(original, ["definition", "witness_formula"], "W=1"),
        "distance_bound": mutate(original, ["definition", "maximum_repair_distance"], 4),
        "witness_values": mutate(original, ["definition", "witness_values", 0], 2),
        "global_count": mutate(original, ["witness_multiplicity_atlas", "global_rho_witness_counts", "3,25"], 63),
        "max_witness": mutate(original, ["witness_multiplicity_atlas", "max_witness_multiplicity"], 24),
        "max_masks": mutate(original, ["witness_multiplicity_atlas", "max_witness_masks", 0], 0),
        "row_count": mutate(original, ["witness_multiplicity_atlas", "by_deleted_cardinality", 4, "rho_witness_counts", "1,4"], 2),
        "coefficient": mutate(original, ["trivariate_generating_function", "coefficient_table", "4,1,4"], 2),
        "x_convention": mutate(original, ["trivariate_generating_function", "x_convention"], "x marks retained labels"),
        "u_convention": mutate(original, ["trivariate_generating_function", "u_convention"], "u marks deleted labels"),
        "v_convention": mutate(original, ["trivariate_generating_function", "v_convention"], "v marks rho"),
        "marginal_u": mutate(original, ["trivariate_generating_function", "P_1_at_u_v1", "3"], 65),
        "marginal_w": mutate(original, ["witness_multiplicity_atlas", "witness_value_counts", "25"], 127),
        "claim": mutate(original, ["claims", "exact_minimum_restoration_witness_count"], False),
        "claim_formula": mutate(original, ["claims", "structural_witness_formula_verified"], False),
        "claim_witness": mutate(original, ["claims", "witness_values_exact"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory() as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
            result = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                rejected += 1
            else:
                print(f"MUTATION_ACCEPTED: {name}", file=sys.stderr)
    assert rejected == len(mutations), (rejected, len(mutations))
    print(f"C79_MUTATION_TEST_PASS ({rejected}/{len(mutations)} rejected)")


if __name__ == "__main__":
    main()
