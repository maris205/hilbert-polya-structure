#!/usr/bin/env python3
"""Hostile semantic mutations for the C97 pair-orbit certificate."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c97_pair_orbit_quotient_evidence.json"
CHECKER = PROJECT / "code/c97_pair_orbit_quotient_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def mutate(value: object, path: list[object], replacement: object) -> object:
    changed = copy.deepcopy(value)
    cursor = changed
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return changed


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    spec = importlib.util.spec_from_file_location("c97_checker", CHECKER)
    checker = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(checker)
    expected, _ = checker.build_expected()
    mutations = {
        "schema": mutate(original, ["schema_id"], "bad"),
        "scope": mutate(original, ["scope_literal"], "BAD"),
        "c90_authority": mutate(original, ["authority", "c90"], "0" * 64),
        "effective_order": mutate(original, ["source_model", "effective_label_group_order"], 11520),
        "ambient_order": mutate(original, ["source_model", "ambient_lifted_group_order"], 1920),
        "orbit_count": mutate(original, ["pair_orbit_atlas", "pair_orbit_count"], 271),
        "orbit_spectrum": mutate(original, ["pair_orbit_atlas", "orbit_size_spectrum", "1"], 143),
        "burnside_sum": mutate(original, ["pair_orbit_atlas", "burnside_fixed_ordered_pair_sum"], 522239),
        "representative": mutate(original, ["pair_orbit_atlas", "rows", 0, "representative_ordered_pair"], [0, 1]),
        "member": mutate(original, ["pair_orbit_atlas", "rows", 0, "ordered_target_pairs", 0], [1, 0]),
        "stabilizer": mutate(original, ["pair_orbit_atlas", "rows", 0, "stabilizer_order_in_effective_label_group"], 960),
        "transpose": mutate(original, ["pair_orbit_atlas", "rows", 0, "transpose_orbit_index"], 1),
        "joint_hash": mutate(original, ["pair_orbit_atlas", "rows", 0, "joint_law_sha256"], "f" * 64),
        "claim": mutate(original, ["claims", "full_table_of_marks_claimed"], True),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c97-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes(canonical(value))
            try:
                checker.validate_evidence_path(path, built=expected)
            except (AssertionError, KeyError, TypeError, ValueError):
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({"status": "C97_MUTATION_TEST_PASS", "rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
