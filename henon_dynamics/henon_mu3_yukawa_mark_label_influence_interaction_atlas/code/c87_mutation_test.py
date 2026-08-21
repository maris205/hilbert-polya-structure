#!/usr/bin/env python3
"""Hostile semantic mutation audit for the C87 evidence."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c87_label_influence_interaction_atlas_evidence.json"
CHECKER = PROJECT / "code/c87_label_influence_interaction_atlas_checker.py"


def changed(source: object, path: list[object], replacement: object) -> object:
    value = copy.deepcopy(source)
    cursor = value
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = replacement  # type: ignore[index]
    return value


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": changed(original, ["schema_id"], "bad"),
        "status": changed(original, ["status"], "RELEASED"),
        "scope": changed(original, ["scope_literal"], "BAD"),
        "c73_hash": changed(original, ["authority", "c73"], "0" * 64),
        "c76_manifest_hash": changed(original, ["authority", "c76_manifest"], "1" * 64),
        "support_count": changed(original, ["source_model", "support_count"], 65535),
        "one_count": changed(original, ["source_model", "one_count"], 30399),
        "kernel_order": changed(original, ["source_model", "ambient_label_action_kernel_order"], 1),
        "faithful_order": changed(original, ["source_model", "faithful_label_group_order"], 11520),
        "first_normalization": changed(original, ["definitions", "first_order_uniform_banzhaf"], "bad"),
        "second_normalization": changed(original, ["definitions", "second_order_uniform_banzhaf"], "bad"),
        "swing_vector": changed(original, ["first_order_atlas", "rows", 0, "coalition_size_swing_counts", 2], 7),
        "swing_count": changed(original, ["first_order_atlas", "rows", 0, "swing_count"], 2239),
        "first_banzhaf": changed(original, ["first_order_atlas", "rows", 0, "uniform_banzhaf_influence"], "0"),
        "first_shapley": changed(original, ["first_order_atlas", "rows", 8, "shapley_shubik_value"], "1"),
        "label_orbit": changed(original, ["first_order_atlas", "faithful_label_orbits", 0, "labels", 1], "S15"),
        "positive_size_cell": changed(original, ["second_order_atlas", "rows", 1, "positive_delta_by_coalition_size", 3], 999),
        "negative_count": changed(original, ["second_order_atlas", "rows", 1, "negative_delta_count"], 255),
        "pair_banzhaf": changed(original, ["second_order_atlas", "rows", 5, "uniform_banzhaf_interaction"], "0"),
        "pair_shapley": changed(original, ["second_order_atlas", "rows", 5, "shapley_pair_interaction"], "0"),
        "pair_orbit_size": changed(original, ["second_order_atlas", "faithful_pair_orbits", 4, "orbit_size"], 3),
        "pair_orbit_member": changed(original, ["second_order_atlas", "faithful_pair_orbits", 4, "member_pairs", 0, 1], "S2"),
        "numerical_class_count": changed(original, ["second_order_atlas", "numerical_classes", 0, "pair_count"], 74),
        "shapley_efficiency": changed(original, ["identities", "first_order_shapley_efficiency", "left_sum"], "0"),
        "endpoint_identity": changed(original, ["identities", "second_order_shapley_endpoint_identity", "incident_pair_sum_by_label", "S9"], "0"),
        "c82_boundary_identity": changed(original, ["identities", "c82_distance_one_boundary_identity", "c82_autocorrelation_by_distance_one"], 445695),
        "claim_flag": changed(original, ["claims", "all_120_unordered_pair_rows_retained"], False),
    }
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c87-mutations-") as directory:
        for name, value in mutations.items():
            path = Path(directory) / f"{name}.json"
            path.write_bytes((json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode())
            result = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            if result.returncode:
                rejected += 1
            else:
                raise AssertionError(f"mutation accepted: {name}")
    assert rejected == len(mutations)
    print(json.dumps({
        "status": "C87_MUTATION_TEST_PASS",
        "rejected": rejected,
        "total": len(mutations),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
