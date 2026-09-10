#!/usr/bin/env python3
"""Hostile semantic mutation audit for C103."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c103_minmax_aggregation_evidence.json"
CHECKER = PROJECT / "code/c103_minmax_aggregation_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    result = copy.deepcopy(value)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c103_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    row = original["aggregation_atlas"]["pair_rows"][17]
    min_time = next(t for t in range(17) if row["minimum_permutation_count_by_time"][str(t)] > 0)
    max_time = next(t for t in range(17) if row["maximum_permutation_count_by_time"][str(t)] > 0)
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "authority": mutate(original, ["authority", "c90"], "0" * 64),
        "count": mutate(original, ["aggregation_atlas", "pair_rows", 399, "left_target_index"], 99),
        "min_cell": mutate(original, ["aggregation_atlas", "pair_rows", 17, "minimum_permutation_count_by_time", str(min_time)], row["minimum_permutation_count_by_time"][str(min_time)] + 1),
        "max_cell": mutate(original, ["aggregation_atlas", "pair_rows", 17, "maximum_permutation_count_by_time", str(max_time)], row["maximum_permutation_count_by_time"][str(max_time)] + 1),
        "tail": mutate(original, ["aggregation_atlas", "pair_rows", 17, "tail_identities", "minimum_tail_identity_verified"], False),
        "cdf": mutate(original, ["aggregation_atlas", "pair_rows", 17, "tail_identities", "maximum_cdf_identity_verified"], False),
        "sum": mutate(original, ["aggregation_atlas", "pair_rows", 17, "expected_sum_identity", "verified"], False),
        "claim": mutate(original, ["claims", "euler_factors_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c103-mutations-") as directory:
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
    print(json.dumps({"status": "C103_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
