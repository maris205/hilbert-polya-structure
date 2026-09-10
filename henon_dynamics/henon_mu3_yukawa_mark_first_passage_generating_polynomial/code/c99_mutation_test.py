#!/usr/bin/env python3
"""Hostile semantic mutation audit for C99."""
from __future__ import annotations
import copy, importlib.util, json, tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c99_generating_polynomial_evidence.json"
CHECKER = PROJECT / "code/c99_generating_polynomial_checker.py"


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
    row = original["polynomial_atlas"]["target_rows"][5]
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c88_hash": mutate(original, ["authority", "c88"], "0" * 64),
        "c89_hash": mutate(original, ["authority", "c89"], "0" * 64),
        "row_count": mutate(original, ["polynomial_atlas", "target_rows", 19, "target_subgroup_index"], 99),
        "coefficient": mutate(original, ["polynomial_atlas", "target_rows", 5, "permutation_count_by_time", "2"], 0),
        "probability": mutate(original, ["polynomial_atlas", "target_rows", 5, "probability_coefficient_by_time", "2", "numerator"], 0),
        "support": mutate(original, ["polynomial_atlas", "target_rows", 5, "support_times", 0], 99),
        "degree": mutate(original, ["polynomial_atlas", "target_rows", 5, "degree"], 99),
        "gcd": mutate(original, ["polynomial_atlas", "target_rows", 5, "support_gcd"], 99),
        "derivative": mutate(original, ["polynomial_atlas", "target_rows", 5, "derivative_at_one_orders_0_to_6", "2", "numerator"], 999),
        "recovered_raw": mutate(original, ["polynomial_atlas", "target_rows", 5, "raw_moment_recovery_from_derivatives", "3", "numerator"], 999),
        "stirling_term": mutate(original, ["polynomial_atlas", "target_rows", 5, "stirling_recovery_terms", "3", "2", "numerator"], 999),
        "check_flag": mutate(original, ["checks", "all_c89_raw_moment_recoveries_orders_0_to_6"], False),
        "claim": mutate(original, ["claims", "euler_factors_claimed"], True),
    }
    spec = importlib.util.spec_from_file_location("c99_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c99-mutations-") as directory:
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
    print(json.dumps({"status": "C99_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
