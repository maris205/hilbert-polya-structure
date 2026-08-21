#!/usr/bin/env python3
"""Hostile semantic mutations for the C98 conditional-kernel receipt."""
from __future__ import annotations

import copy
import importlib.util
import json
from math import factorial
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c98_conditional_kernel_evidence.json"
CHECKER = PROJECT / "code/c98_conditional_kernel_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    changed = copy.deepcopy(value)
    cursor = changed
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return changed


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c98_checker", CHECKER)
    checker = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(checker)
    expected, _ = checker.build_expected()
    row0 = ["conditional_kernel_atlas", "pair_rows", 0]
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c90_authority": mutate(original, ["authority", "c90"], "0" * 64),
        "pair_count": mutate(original, ["conditional_kernel_atlas", "ordered_pair_count"], 399),
        "attainable_count": mutate(original, ["conditional_kernel_atlas", "attainable_conditioning_row_count"], 4979),
        "empty_count": mutate(original, ["conditional_kernel_atlas", "empty_conditioning_row_count"], 1821),
        "relation": mutate(original, row0 + ["relation_type"], "incomparable"),
        "joint_cell": mutate(original, row0 + ["joint_first_passage_permutation_counts", "0", "0"], TOTAL_MINUS_ONE),
        "probability": mutate(original, row0 + ["conditional_rows", 0, "conditional_probability_by_response_time", "0", "numerator"], 0),
        "empty_row": mutate(original, row0 + ["conditional_rows", 1, "conditional_probability_by_response_time"], {}),
        "mean": mutate(original, row0 + ["conditional_rows", 0, "conditional_mean_response_time", "numerator"], 1),
        "tower": mutate(original, row0 + ["tower_identities", "total_expectation_verified"], False),
        "variance": mutate(original, row0 + ["tower_identities", "c88_response_variance", "numerator"], 1),
        "bayes": mutate(original, row0 + ["bayes_reverse_identity", "joint_transpose_verified"], False),
        "diagonal": mutate(original, row0 + ["diagonal_kernel_is_identity"], False),
        "claim": mutate(original, ["claims", "hilbert_polya_operator_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c98-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path, built=expected)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C98_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


TOTAL_MINUS_ONE = factorial(16) - 1


if __name__ == "__main__":
    main()
