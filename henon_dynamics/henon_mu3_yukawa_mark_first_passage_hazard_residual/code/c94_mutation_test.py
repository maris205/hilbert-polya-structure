#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C94 receipt."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c94_first_passage_hazard_residual_evidence.json"
CHECKER = PROJECT / "code/c94_first_passage_hazard_residual_checker.py"


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
    spec = importlib.util.spec_from_file_location("c94_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    mutations = {
        "schema": (["schema_id"], "bad"),
        "scope": (["scope_literal"], "BAD"),
        "authority": (["authority", "c88"], "0" * 64),
        "grid": (["source_model", "residual_r_grid", 3], 99),
        "target_count": (["source_model", "target_subgroup_count"], 19),
        "target_index": (["hazard_residual_atlas", "target_rows", 7, "target_subgroup_index"], 8),
        "hazard": (["hazard_residual_atlas", "target_rows", 2, "hazard_atlas", "hazard_probability", "3", "numerator"], 0),
        "risk": (["hazard_residual_atlas", "target_rows", 4, "hazard_atlas", "at_risk_permutation_count_before_step", "6"], 1),
        "survival": (["hazard_residual_atlas", "target_rows", 5, "survival_permutation_count_after_time", "4"], 0),
        "residual_pmf": (["hazard_residual_atlas", "target_rows", 9, "residual_life_atlas", 2, "conditional_residual_probability_mass_by_r", "3", "numerator"], 0),
        "residual_mean": (["hazard_residual_atlas", "target_rows", 13, "residual_life_atlas", 1, "mean_residual_life", "numerator"], 1),
        "residual_variance": (["hazard_residual_atlas", "target_rows", 19, "residual_life_atlas", 0, "variance_residual_life", "denominator"], 1),
        "claim": (["claims", "arithmetic_local_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c94-mutations-") as directory:
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
    print(json.dumps({"status": "C94_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
