#!/usr/bin/env python3
"""Hostile semantic mutation audit for C89."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c89_first_passage_moments_evidence.json"
CHECKER = PROJECT / "code/c89_first_passage_moments_checker.py"


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
    spec = importlib.util.spec_from_file_location("c89_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    paths = {
        "schema": (["schema_id"], "bad"),
        "scope": (["scope_literal"], "BAD"),
        "authority": (["authority", "c88"], "0" * 64),
        "definition": (["definition", "cumulant_recursion"], "wrong"),
        "target_count": (["source_model", "target_subgroup_count"], 19),
        "target_index": (["moment_atlas", "target_rows", 7, "target_subgroup_index"], 8),
        "raw": (["moment_atlas", "target_rows", 19, "raw_moments", "4", "numerator"], 0),
        "factorial": (["moment_atlas", "target_rows", 12, "falling_factorial_moments", "3", "denominator"], 1),
        "central": (["moment_atlas", "target_rows", 4, "central_moments", "2", "numerator"], 0),
        "cumulant": (["moment_atlas", "target_rows", 9, "cumulants", "5", "numerator"], 1),
        "survival": (["moment_atlas", "target_rows", 2, "survival_raw_moments", "3", "numerator"], 1),
        "identity": (["moment_atlas", "target_rows", 19, "identity_checks", "raw_equals_survival_raw"], False),
        "claim": (["claims", "arithmetic_local_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c89-mutations-") as directory:
        for name, (path, replacement) in paths.items():
            candidate = Path(directory) / f"{name}.json"
            candidate.write_bytes(canonical(mutate(original, path, replacement)))
            try:
                observed = json.loads(candidate.read_bytes())
                assert observed == expected
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(paths)
    print(json.dumps({"status": "C89_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
