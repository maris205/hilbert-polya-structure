#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C88 receipt."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c88_subgroup_first_passage_atlas_evidence.json"
CHECKER = PROJECT / "code/c88_subgroup_first_passage_atlas_checker.py"


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
    spec = importlib.util.spec_from_file_location("c88_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c75_hash": mutate(original, ["authority", "c75"], "0" * 64),
        "c75_manifest": mutate(original, ["authority", "c75_manifest"], "1" * 64),
        "c83_hash": mutate(original, ["authority", "c83"], "2" * 64),
        "c83_manifest": mutate(original, ["authority", "c83_manifest"], "3" * 64),
        "c85_hash": mutate(original, ["authority", "c85"], "4" * 64),
        "c85_manifest": mutate(original, ["authority", "c85_manifest"], "5" * 64),
        "definition": mutate(original, ["definition", "cdf_formula"], "P=0"),
        "label_count": mutate(original, ["source_model", "label_count"], 15),
        "support_count": mutate(original, ["source_model", "support_count"], 65535),
        "subgroup_count": mutate(original, ["source_model", "subgroup_count"], 19),
        "coordinate_hash": mutate(original, ["source_model", "coordinate_sha256"], "6" * 64),
        "target_index": mutate(original, ["first_passage_atlas", "target_rows", 10, "target_subgroup_index"], 9),
        "target_order": mutate(original, ["first_passage_atlas", "target_rows", 10, "target_subgroup_order"], 8),
        "minimum_time": mutate(original, ["first_passage_atlas", "target_rows", 19, "minimum_first_passage_time"], 2),
        "maximum_time": mutate(original, ["first_passage_atlas", "target_rows", 18, "maximum_first_passage_time"], 16),
        "minimal_mask": mutate(original, ["first_passage_atlas", "target_rows", 19, "minimal_hitting_support_masks", 0], 0),
        "minimal_count": mutate(original, ["first_passage_atlas", "target_rows", 19, "minimal_hitting_support_count_by_cardinality", "3"], 24),
        "hit_bitset": mutate(original, ["first_passage_atlas", "target_rows", 1, "subset_hit_bitset_hex"], "00" * 8192),
        "hit_bitset_hash": mutate(original, ["first_passage_atlas", "target_rows", 1, "subset_hit_bitset_sha256"], "7" * 64),
        "hit_count": mutate(original, ["first_passage_atlas", "target_rows", 10, "subset_hit_count_by_cardinality", "2"], 0),
        "nonhit_count": mutate(original, ["first_passage_atlas", "target_rows", 10, "subset_nonhit_count_by_cardinality", "2"], 120),
        "hit_probability": mutate(original, ["first_passage_atlas", "target_rows", 10, "subset_hit_probability_by_cardinality", "2", "numerator"], 0),
        "survival_probability": mutate(original, ["first_passage_atlas", "target_rows", 10, "subset_survival_probability_by_cardinality", "2", "denominator"], 1),
        "pivotal_edge": mutate(original, ["first_passage_atlas", "target_rows", 19, "pivotal_edge_count_by_cardinality", "3"], 74),
        "pivotal_pattern": mutate(original, ["first_passage_atlas", "target_rows", 19, "pivotal_pattern_counts", "3,3"], 24),
        "permutation_count": mutate(original, ["first_passage_atlas", "target_rows", 19, "permutation_count_by_first_passage_time", "3"], 0),
        "first_passage_probability": mutate(original, ["first_passage_atlas", "target_rows", 19, "probability_by_first_passage_time", "3", "numerator"], 1),
        "survival_count": mutate(original, ["first_passage_atlas", "target_rows", 19, "survival_permutation_count_after_time", "3"], 0),
        "expectation": mutate(original, ["first_passage_atlas", "target_rows", 19, "expected_first_passage_time", "numerator"], 1),
        "inclusion": mutate(original, ["target_poset", "inclusion_matrix", 0, 19], 0),
        "cover": mutate(original, ["target_poset", "cover_relations", 0, 1], 19),
        "pair_count": mutate(original, ["target_poset", "comparable_ordered_pair_count_including_reflexive"], 101),
        "monotone_pair": mutate(original, ["target_poset", "monotonicity_pairs", 0, "cdf_order_all_times"], False),
        "top_hash": mutate(original, ["c83_top_target_identity", "c83_assembly_atlas_sha256"], "8" * 64),
        "top_check": mutate(original, ["c83_top_target_identity", "field_checks", "expectation"], False),
        "enumeration_check": mutate(original, ["checks", "all_65536_supports_enumerated"], False),
        "claim_flag": mutate(original, ["claims", "full_table_of_marks_claimed"], True),
    }
    checker = load_checker()
    expected, _ = checker.build_expected()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c88-mutations-") as directory:
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
    print(json.dumps({"status": "C88_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
