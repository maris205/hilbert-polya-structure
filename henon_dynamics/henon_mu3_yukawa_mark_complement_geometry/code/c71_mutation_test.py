#!/usr/bin/env python3
"""Hostile semantic mutations for the C71 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c71_complement_geometry_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c71_complement_geometry_checker.py"


def mutate(source: dict, path: list[object], value: object) -> dict:
    result = deepcopy(source)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c71-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "authority": mutate(original, ["authority", "c69_manifest"], "0" * 64),
        "type_order": mutate(original, ["type_order", 0], "S16"),
        "D_type": mutate(original, ["fixed_decomposition", "D_2_type", 0], 2),
        "K_type": mutate(original, ["fixed_decomposition", "K_2_type", 0], 3),
        "hom_invariant": mutate(original, ["fixed_decomposition", "Hom_K_D_invariants", 0], 4),
        "hom_order": mutate(original, ["fixed_decomposition", "Hom_K_D_order"], 2 ** 40),
        "graph_intersection": mutate(original, ["graph_model", "pairwise_intersection"], "Gamma_f intersect Gamma_g = 0"),
        "index_definition": mutate(original, ["graph_model", "intersection_index_definition"], "[C : Gamma_f intersect Gamma_g]"),
        "translation": mutate(original, ["graph_model", "translation_invariant_spectrum"], False),
        "poset_size": mutate(original, ["target_subgroup_poset", "subgroup_count"], 37),
        "order_count": mutate(original, ["target_subgroup_poset", "subgroup_counts_by_order", "8"], 10),
        "type_count": mutate(original, ["target_subgroup_poset", "subgroup_counts_by_type", 1, "count"], 6),
        "image_type": mutate(original, ["intersection_quotient_distribution", 2, "image_type"], "Z/8"),
        "target_count": mutate(original, ["intersection_quotient_distribution", 2, "target_subgroup_count"], 3),
        "hom_into": mutate(original, ["intersection_quotient_distribution", 2, "homomorphisms_into_one_subgroup"], 32768),
        "surjections": mutate(original, ["intersection_quotient_distribution", 2, "surjections_onto_one_subgroup"], 65535),
        "parameter": mutate(original, ["intersection_quotient_distribution", 2, "parameter_count"], 262143),
        "ordered_pairs": mutate(original, ["intersection_quotient_distribution", 2, "ordered_pair_count"], 1),
        "unordered_pairs": mutate(original, ["intersection_quotient_distribution", 2, "unordered_distinct_pair_count"], 1),
        "spectrum": mutate(original, ["intersection_index_spectrum", 3, "count_from_each_fixed_complement"], 1),
        "spectrum_pairs": mutate(original, ["intersection_index_spectrum", 3, "ordered_pair_count"], 1),
        "total": mutate(original, ["spectrum_total"], 2 ** 40),
        "core_equals": mutate(original, ["universal_core", "equals_8C"], False),
        "core_primary": mutate(original, ["universal_core", "primary_invariants", "2", 0], 4),
        "core_invariants": mutate(original, ["universal_core", "invariant_factors", 1], 9),
        "core_order": mutate(original, ["universal_core", "order"], 27),
        "core_index": mutate(original, ["universal_core", "index_in_C"], 2 ** 21),
        "span": mutate(original, ["complement_span", "generated_subgroup"], "K"),
        "surjective_count": mutate(original, ["complement_span", "surjective_difference_count"], 1),
        "coordinate_order": mutate(original, ["named_core_geometry", "coordinate_orders_in_C", 0], 18),
        "eight_order": mutate(original, ["named_core_geometry", "eight_coordinate_orders", 8], 1),
        "residue_hash": mutate(original, ["named_core_geometry", "eight_coordinate_residue_sha256"], "1" * 64),
        "minimum": mutate(original, ["named_core_geometry", "minimum_named_generator_count"], 2),
        "pair_generation": mutate(original, ["named_core_geometry", "generating_subset_counts_by_size", "2"], 1),
        "triple_count": mutate(original, ["named_core_geometry", "generating_triple_count"], 24),
        "triple": mutate(original, ["named_core_geometry", "generating_triples", 0, 2], "S10"),
        "triple_pivot": mutate(original, ["named_core_geometry", "every_generating_triple_contains"], "S10"),
        "kernel_claim": mutate(original, ["claims", "full_kernel_isomorphism_types_classified"], True),
        "canonical_claim": mutate(original, ["claims", "canonical_complement_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c71-mutations-") as temporary:
        for name, document in mutations.items():
            path = Path(temporary) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({
        "status": "PASS",
        "mutations_rejected": len(rejected),
        "names": sorted(rejected),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
