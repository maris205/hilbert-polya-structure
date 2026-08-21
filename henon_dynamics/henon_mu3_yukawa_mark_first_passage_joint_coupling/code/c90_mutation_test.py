#!/usr/bin/env python3
"""Hostile semantic mutation audit for C90."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c90_joint_first_passage_evidence.json"
CHECKER = PROJECT / "code/c90_joint_first_passage_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c90_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.expected()
    mutations = {
        "schema": (["schema_id"], "bad"),
        "status": (["status"], "RELEASED"),
        "scope": (["scope_literal"], "BAD"),
        "authority": (["authority", "c88"], "0" * 64),
        "definition": (["definition", "joint_survival"], "wrong"),
        "pair_count": (["joint_atlas", "ordered_target_pair_count"], 399),
        "pair_index": (["joint_atlas", "pair_rows", 37, "upper_target_index"], 19),
        "cell": (["joint_atlas", "pair_rows", 42, "joint_survival_permutation_counts", "3", "5"], 0),
        "probability": (["joint_atlas", "pair_rows", 42, "joint_survival_probabilities", "3", "5", "numerator"], 1),
        "mixed": (["joint_atlas", "pair_rows", 17, "mixed_raw_moments", "4", "5", "numerator"], 1),
        "covariance": (["joint_atlas", "pair_rows", 399, "covariance", "numerator"], 0),
        "marginal": (["joint_atlas", "pair_rows", 9, "marginal_consistency", "all_orders_match"], False),
        "claim": (["claims", "arithmetic_local_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c90-mutations-") as directory:
        for name, (path, replacement) in mutations.items():
            candidate = Path(directory) / f"{name}.json"
            candidate.write_bytes(canonical(mutate(original, path, replacement)))
            try:
                assert json.loads(candidate.read_bytes()) == expected
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C90_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
