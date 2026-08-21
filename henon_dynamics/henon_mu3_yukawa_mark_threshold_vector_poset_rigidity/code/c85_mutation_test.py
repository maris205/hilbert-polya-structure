#!/usr/bin/env python3
"""Hostile semantic mutations for the C85 receipt."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c85_threshold_vector_poset_rigidity_evidence.json"
CHECKER = PROJECT / "code/c85_threshold_vector_poset_rigidity_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return result


def load_checker():
    spec = importlib.util.spec_from_file_location("c85_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c75_evidence_hash": mutate(original, ["authority", "c75"], "0" * 64),
        "c75_manifest_hash": mutate(original, ["authority", "c75_manifest"], "1" * 64),
        "c76_evidence_hash": mutate(original, ["authority", "c76"], "2" * 64),
        "c76_manifest_hash": mutate(original, ["authority", "c76_manifest"], "3" * 64),
        "c80_evidence_hash": mutate(original, ["authority", "c80"], "4" * 64),
        "c80_manifest_hash": mutate(original, ["authority", "c80_manifest"], "5" * 64),
        "ambient_order": mutate(original, ["source_model", "ambient_lifted_group_order"], 1920),
        "effective_order": mutate(original, ["source_model", "effective_label_group_order"], 11520),
        "threshold_matrix_hash": mutate(original, ["source_model", "c80_threshold_matrix_sha256"], "6" * 64),
        "distinct_count": mutate(original, ["rigidity", "distinct_vector_count"], 19),
        "support_class": mutate(original, ["rigidity", "support_class_indices", 261], 18),
        "vector_coordinate": mutate(original, ["rigidity", "vector_rows", 10, "threshold_vector", 19], 9),
        "zero_ideal": mutate(original, ["rigidity", "vector_rows", 18, "zero_coordinate_indices", 1], 1),
        "fibre_size": mutate(original, ["rigidity", "vector_rows", 19, "fibre_size"], 30399),
        "fibre_spectrum": mutate(original, ["rigidity", "fibre_spectrum", "30400"], 1),
        "inclusion_relation": mutate(original, ["poset", "inclusion_matrix", 0, 19], 0),
        "coordinate_order_relation": mutate(original, ["poset", "coordinatewise_ge_matrix", 0, 19], 0),
        "cover_relation": mutate(original, ["poset", "cover_relations", 0, 1], 19),
        "comparable_count": mutate(original, ["poset", "comparable_ordered_pair_count_including_reflexive"], 101),
        "claim_flag": mutate(original, ["claims", "full_table_of_marks_claimed"], True),
    }
    checker = load_checker()
    expected, _ = checker.build_expected()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c85-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path, expected)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({
        "status": "C85_MUTATION_TEST_PASS",
        "rejected": rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
