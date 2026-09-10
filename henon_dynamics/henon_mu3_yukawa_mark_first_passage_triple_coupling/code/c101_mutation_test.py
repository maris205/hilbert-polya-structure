#!/usr/bin/env python3
"""Hostile semantic mutations for C101."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c101_triple_coupling_evidence.json"
CHECKER = PROJECT / "code/c101_triple_coupling_checker.py"


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
    spec = importlib.util.spec_from_file_location("c101_checker", CHECKER)
    checker = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    row10 = original["triple_atlas"]["rows"][10]
    nonzero_cell = next(index for index, value in enumerate(row10["joint_pmf_permutation_counts_flat"]) if value > 0)
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "authority": mutate(original, ["authority", "c90"], "0" * 64),
        "triple_count": mutate(original, ["triple_atlas", "unordered_distinct_triple_count"], 1139),
        "cell_count": mutate(original, ["triple_atlas", "pmf_cell_count"], 1),
        "target_indices": mutate(original, ["triple_atlas", "rows", 10, "target_indices"], [0, 1, 3]),
        "pmf_cell": mutate(original, ["triple_atlas", "rows", 10, "joint_pmf_permutation_counts_flat", nonzero_cell], row10["joint_pmf_permutation_counts_flat"][nonzero_cell] + 1),
        "normalization": mutate(original, ["triple_atlas", "rows", 10, "joint_pmf_permutation_counts_flat", 0], 1),
        "moment": mutate(original, ["triple_atlas", "rows", 10, "raw_mixed_moments_orders_0_to_3", "1,1,1", "numerator"], 1),
        "mean": mutate(original, ["triple_atlas", "rows", 10, "mean_vector", 0, "numerator"], 1),
        "covariance": mutate(original, ["triple_atlas", "rows", 10, "covariance_matrix", 0, 1, "numerator"], 1),
        "interaction": mutate(original, ["triple_atlas", "rows", 10, "third_interaction_cumulant", "numerator"], 1),
        "check_flag": mutate(original, ["checks", "all_covariance_matrices_exact"], False),
        "claim": mutate(original, ["claims", "euler_factors_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c101-mutations-") as directory:
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
    print(json.dumps({"status": "C101_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
