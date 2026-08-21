#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C91 receipt."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c91_first_passage_race_atlas_evidence.json"
CHECKER = PROJECT / "code/c91_first_passage_race_atlas_checker.py"


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
    spec = importlib.util.spec_from_file_location("c91_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    first = original["race_atlas"]["pair_rows"][0]
    tied_index = next(
        index
        for index, row in enumerate(original["race_atlas"]["pair_rows"])
        if row["tie_nonzero"]
    )
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c88_hash": mutate(original, ["authority", "c88"], "0" * 64),
        "pair_count": mutate(original, ["source_model", "incomparable_pair_count"], 107),
        "pair_index": mutate(original, ["race_atlas", "pair_rows", 0, "right_target_index"], first["left_target_index"]),
        "incomparable": mutate(original, ["race_atlas", "pair_rows", 0, "incomparable"], False),
        "left_count": mutate(original, ["race_atlas", "pair_rows", 0, "outcome_permutation_count", "left_first"], 0),
        "tie_count": mutate(original, ["race_atlas", "pair_rows", 0, "outcome_permutation_count", "tie"], 1),
        "right_probability": mutate(original, ["race_atlas", "pair_rows", 0, "outcome_probability", "right_first", "numerator"], 0),
        "time_cell": mutate(original, ["race_atlas", "pair_rows", 0, "outcome_permutation_count_by_first_passage_time", "2", "tie"], 1),
        "edge_cell": mutate(original, ["race_atlas", "pair_rows", 0, "boundary_edge_count_by_first_passage_time", "2", "left_first"], 0),
        "identity": mutate(original, ["race_atlas", "pair_rows", 0, "winner_count_identity", "total_permutations"], 1),
        "tie_flag": mutate(original, ["race_atlas", "pair_rows", tied_index, "tie_nonzero"], False),
        "aggregate": mutate(original, ["race_atlas", "aggregate_outcome_permutation_count", "tie"], 0),
        "claim": mutate(original, ["claims", "full_table_of_marks_claimed"], True),
    }
    checker = load_checker()
    expected, _ = checker.build_expected()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c91-mutations-") as directory:
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
    print(json.dumps({"status": "C91_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
