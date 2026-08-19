#!/usr/bin/env python3
"""Hostile semantic mutations for the C75 lifted-incidence checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c75_closure_incidence_lift_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c75_closure_incidence_lift_checker.py"


def mutate(document: dict, path: list[object], value: object) -> dict:
    result = deepcopy(document)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c75-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "c72_authority": mutate(original, ["authority", "c72"], "0" * 64),
        "c74_authority": mutate(original, ["authority", "c74"], "1" * 64),
        "ambient_order": mutate(original, ["ambient_model", "order"], 108),
        "aut_order": mutate(original, ["ambient_model", "automorphism_order"], 144),
        "subgroup_count": mutate(original, ["ambient_model", "all_subgroup_count"], 19),
        "coordinate": mutate(original, ["named_coordinate_source", "coordinates", 0, 0], 2),
        "coordinate_hash": mutate(original, ["named_coordinate_source", "coordinate_sha256"], "f" * 64),
        "incidence_definition": mutate(original, ["closure_incidence", "definition"], "point equality"),
        "fiber_label": mutate(original, ["closure_incidence", "selected_fibers", 0, "labels", 0], "S1"),
        "fiber_weight": mutate(original, ["closure_incidence", "selected_fibers", 0, "weight"], 4),
        "subgroup_weight": mutate(original, ["closure_incidence", "all_subgroups", 6, "closure_weight"], 1),
        "stabilizer_order": mutate(original, ["closure_incidence", "weighted_stabilizer_order"], 18),
        "stabilizer_matrix": mutate(original, ["closure_incidence", "weighted_stabilizer_matrices", 0, 0], 3),
        "stabilizer_action": mutate(original, ["closure_incidence", "weighted_stabilizer_fiber_actions", "(2, 1, 2, 1)", 2], 2),
        "stabilizer_structure": mutate(original, ["closure_incidence", "abstract_stabilizer_candidate"], "D12"),
        "pair_definition": mutate(original, ["lifted_symmetry", "definition"], "lattice action only"),
        "pair_count": mutate(original, ["lifted_symmetry", "direct_compatible_pair_count"], 11514),
        "fiber_order": mutate(original, ["lifted_symmetry", "label_fiber_order"], 480),
        "factorization": mutate(original, ["lifted_symmetry", "fiber_factorization"], "5! * 2! * 2!"),
        "kernel_order": mutate(original, ["lifted_symmetry", "projection_kernel_order"], 480),
        "lifted_order": mutate(original, ["lifted_symmetry", "lifted_group_order"], 1152),
        "order_distribution": mutate(original, ["lifted_symmetry", "order_distribution", "60"], 385),
        "center": mutate(original, ["lifted_symmetry", "center_order"], 12),
        "generator_matrix": mutate(original, ["lifted_symmetry", "generators", 5, "matrix", 0], 1),
        "generator_cycle": mutate(original, ["lifted_symmetry", "generators", 0, "label_cycles", 0, 0], "S6"),
        "generated_order": mutate(original, ["lifted_symmetry", "generated_group_order"], 5760),
        "structure": mutate(original, ["lifted_symmetry", "abstract_group_candidate"], "S5 x C2 x D12"),
        "lattice_image": mutate(original, ["nonfaithful_lattice_diagnostic", "twenty_subgroup_lattice_action_image_order"], 108),
        "lattice_warning": mutate(original, ["nonfaithful_lattice_diagnostic", "warning"], "lattice action is faithful"),
        "claim_lift": mutate(original, ["claims", "lifted_order_11520"], False),
        "claim_firewall": mutate(original, ["claims", "arithmetic_local_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c75-mutations-") as temporary:
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
