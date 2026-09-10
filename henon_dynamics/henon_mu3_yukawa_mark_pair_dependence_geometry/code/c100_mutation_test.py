#!/usr/bin/env python3
"""Hostile semantic mutation audit for C100."""
from __future__ import annotations
import copy, importlib.util, json, tempfile
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c100_pair_dependence_geometry_evidence.json"
CHECKER = PROJECT / "code/c100_pair_dependence_geometry_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    out = copy.deepcopy(value)
    cursor = out
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return out


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    row = original["dependence_atlas"]["pair_rows"][21]
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c90_hash": mutate(original, ["authority", "c90"], "0" * 64),
        "spectrum": mutate(original, ["dependence_atlas", "relation_type_spectrum", "incomparable", "count"], 215),
        "relation": mutate(original, ["dependence_atlas", "pair_rows", 1, "relation_type"], "diagonal"),
        "pmf": mutate(original, ["dependence_atlas", "pair_rows", 22, "joint_pmf_permutation_counts", "3", "4"], 0),
        "left_axis": mutate(original, ["dependence_atlas", "pair_rows", 21, "marginal_permutation_counts", "left", "2"], 0),
        "covariance": mutate(original, ["dependence_atlas", "pair_rows", 21, "covariance", "numerator"], 0),
        "rational_correlation": mutate(original, ["dependence_atlas", "pair_rows", 22, "rational_correlation", "numerator"], 0),
        "variance": mutate(original, ["dependence_atlas", "pair_rows", 21, "left_variance", "numerator"], 0),
        "corr_squared": mutate(original, ["dependence_atlas", "pair_rows", 21, "pearson_correlation_squared", "numerator"], 0),
        "tv": mutate(original, ["dependence_atlas", "pair_rows", 21, "total_variation_from_product_marginals", "numerator"], 0),
        "frechet": mutate(original, ["dependence_atlas", "pair_rows", 21, "frechet_violation_l1", "numerator"], 1),
        "diagonal_check": mutate(original, ["dependence_atlas", "pair_rows", 0, "diagonal_checks", "covariance_equals_variance"], False),
        "claim": mutate(original, ["claims", "arithmetic_local_claimed"], True),
    }
    spec = importlib.util.spec_from_file_location("c100_checker", CHECKER)
    assert spec and spec.loader
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    expected = checker.build_expected()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c100-mutations-") as directory:
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
    print(json.dumps({"status": "C100_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
