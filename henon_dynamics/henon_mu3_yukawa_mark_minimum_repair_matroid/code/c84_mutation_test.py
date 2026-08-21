#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C84 receipt."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT / "code/c84_minimum_repair_matroid_checker.py"
EVIDENCE = PROJECT / "results/c84_minimum_repair_matroid_evidence.json"


def mutate(value: object, path: list[object], replacement: object) -> object:
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_bytes())
    first_basis_mask = str(original["all_deleted_case"]["basis_masks"][0])
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad-schema"),
        "status": mutate(original, ["status"], "PASS"),
        "scope": mutate(original, ["scope_literal"], "BAD_SCOPE"),
        "c79_hash": mutate(original, ["authority", "c79"], "0" * 64),
        "ambient_order": mutate(original, ["source_model", "c75_ambient_lifted_group_order"], 1920),
        "effective_order": mutate(original, ["source_model", "c76_effective_label_group_order"], 11520),
        "direction_rank": mutate(original, ["matroid_theorem", "direction_rank"], "r(D)=t(D)"),
        "basis_identity": mutate(original, ["matroid_theorem", "basis_identification"], "all subsets"),
        "mask_count": mutate(original, ["maskwise_verification", "deletion_set_count"], 65535),
        "obligation_count": mutate(original, ["maskwise_verification", "base_exchange_ordered_obligation_count"], 0),
        "template_count": mutate(original, ["rho_witness_template_atlas", "template_count"], 9),
        "template_support": mutate(original, ["rho_witness_template_atlas", "rows", 2, "support_count"], 1983),
        "graph_type_count": mutate(original, ["unlabeled_exchange_graph_atlas", "graph_type_count"], 4),
        "line_diameter": mutate(original, ["unlabeled_exchange_graph_atlas", "rows", 4, "diameter"], 3),
        "all_deleted_basis": mutate(original, ["all_deleted_case", "basis_masks", 0], 0),
        "c76_equality": mutate(original, ["all_deleted_case", "equals_c76_full_core_minimal_triples"], False),
        "degree_by_basis": mutate(original, ["all_deleted_case", "exchange_graph", "degree_by_basis_mask", first_basis_mask], 0),
        "claim": mutate(original, ["claims", "minimum_witness_families_are_matroid_bases"], False),
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
    print(f"C84_MUTATION_TEST_PASS ({rejected}/{len(mutations)} rejected)")


if __name__ == "__main__":
    main()
