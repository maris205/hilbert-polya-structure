#!/usr/bin/env python3
"""Hostile semantic mutations for the C74 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c74_named_core_affine_rigidity_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c74_named_core_affine_rigidity_checker.py"


def mutate(source: dict, path: list[object], value: object) -> dict:
    result = deepcopy(source)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c74-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "authority": mutate(original, ["authority", "c72"], "0" * 64),
        "core_order": mutate(original, ["core_model", "core_order"], 108),
        "point_count": mutate(original, ["core_model", "distinct_named_point_count"], 9),
        "multiplicity": mutate(original, ["core_model", "multiplicity_profile", 0], 4),
        "endomorphism": mutate(original, ["automorphism_model", "full_core_endomorphism_count"], 485),
        "aut_count": mutate(original, ["automorphism_model", "automorphism_count"], 144),
        "affine_count": mutate(original, ["automorphism_model", "affine_count"], 7776),
        "matrix_condition": mutate(original, ["automorphism_model", "automorphism_condition"], "det != 0"),
        "multiset_stabilizer": mutate(original, ["stabilizers", "affine_multiset_stabilizer_count"], 2),
        "set_stabilizer": mutate(original, ["stabilizers", "affine_set_stabilizer_count"], 2),
        "overlap_histogram": mutate(original, ["overlap_distributions", "multiset_overlap", "14"], 3),
        "set_histogram": mutate(original, ["overlap_distributions", "underlying_set_overlap", "8"], 3),
        "max_overlap": mutate(original, ["rigidity_margin", "maximum_nonidentity_multiset_overlap"], 15),
        "near_count": mutate(original, ["rigidity_margin", "number_at_maximum"], 1),
        "near_matrix": mutate(original, ["rigidity_margin", "witnesses", 0, "matrix", 0], 6),
        "orbit_size": mutate(original, ["rigidity_margin", "named_multiset_orbit_size"], 108),
        "linear_orbit_size": mutate(original, ["rigidity_margin", "linear_set_orbit_size"], 5832),
        "hypergraph_order": mutate(original, ["symmetry_boundary", "c73_hypergraph_automorphism_order"], 34560),
        "core_aut_order": mutate(original, ["symmetry_boundary", "core_automorphism_order"], 144),
        "affine_group_order": mutate(original, ["symmetry_boundary", "affine_group_order"], 7776),
        "same_group": mutate(original, ["symmetry_boundary", "identified_as_same_group"], True),
        "fiber_order": mutate(original, ["symmetry_boundary", "label_fiber_permutation_order"], 4800),
        "claim_multiset": mutate(original, ["claims", "named_multiset_rigidity_proved"], False),
        "claim_set": mutate(original, ["claims", "underlying_set_rigidity_proved"], False),
        "claim_boundary": mutate(original, ["claims", "hypergraph_automorphisms_are_affine_core_automorphisms_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c74-mutations-") as temporary:
        for name, document in mutations.items():
            path = Path(temporary) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
