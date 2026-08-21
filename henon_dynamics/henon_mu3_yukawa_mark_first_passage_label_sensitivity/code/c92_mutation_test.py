#!/usr/bin/env python3
"""Hostile semantic mutation audit for C92."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c92_first_passage_label_sensitivity_evidence.json"
CHECKER = PROJECT / "code/c92_first_passage_label_sensitivity_checker.py"


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
    spec = importlib.util.spec_from_file_location("c92_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "authority": mutate(original, ["authority", "c88"], "0" * 64),
        "label_count": mutate(original, ["source_model", "label_count"], 15),
        "target_count": mutate(original, ["source_model", "target_count"], 19),
        "target_index": mutate(original, ["target_atlas", "target_rows", 1, "target_subgroup_index"], 4),
        "label_index": mutate(original, ["target_atlas", "target_rows", 1, "pivotal_label_rows", 2, "label_index"], 3),
        "pivotal_count": mutate(original, ["target_atlas", "target_rows", 19, "pivotal_label_rows", 8, "pivotal_permutation_count"], 1),
        "rank_count": mutate(original, ["target_atlas", "target_rows", 19, "pivotal_label_rows", 8, "pivotal_permutation_count_by_rank", "3"], 0),
        "efficiency": mutate(original, ["target_atlas", "target_rows", 19, "efficiency_probability", "numerator"], 0),
        "rank_identity": mutate(original, ["target_atlas", "target_rows", 19, "rank_efficiency_identity"], False),
        "claim": mutate(original, ["claims", "arithmetic_local_claimed"], True),
    }
    checker = load_checker()
    expected = checker.expected(checker.source())
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c92-mutations-") as directory:
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
    print(json.dumps({"status": "C92_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
