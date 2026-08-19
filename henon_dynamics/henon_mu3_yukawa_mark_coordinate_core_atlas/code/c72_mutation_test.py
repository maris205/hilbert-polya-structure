#!/usr/bin/env python3
"""Hostile semantic mutations for the C72 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c72_coordinate_core_atlas_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c72_coordinate_core_atlas_checker.py"


def mutate(source: dict, path: list[object], value: object) -> dict:
    result = deepcopy(source)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    rows = original["support_atlas"]["rows"]
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c72-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "authority": mutate(original, ["authority", "c71"], "0" * 64),
        "core_order": mutate(original, ["core", "order"], 27),
        "core_rank": mutate(original, ["core", "abstract_minimum_generator_count"], 3),
        "basis": mutate(original, ["coordinate_realization", "basis", 0], "8[S2]"),
        "moduli": mutate(original, ["coordinate_realization", "basis_moduli", 0], 8),
        "coordinate": mutate(original, ["coordinate_realization", "coordinates", 0, 0], 2),
        "coordinate_hash": mutate(original, ["coordinate_realization", "coordinates_sha256"], "0" * 64),
        "coordinate_order": mutate(original, ["coordinate_realization", "orders", 0], 18),
        "zero_labels": mutate(original, ["coordinate_realization", "zero_coordinate_labels", 0], "S2"),
        "subgroup_count": mutate(original, ["subgroup_lattice_atlas", "all_subgroup_count"], 19),
        "reached_count": mutate(original, ["subgroup_lattice_atlas", "reached_subgroup_count"], 19),
        "coverage": mutate(original, ["subgroup_lattice_atlas", "every_subgroup_reached_by_named_support"], False),
        "type_count": mutate(original, ["subgroup_lattice_atlas", "type_rows", 2, "subgroup_count_in_core"], 5),
        "support_total": mutate(original, ["support_atlas", "rows", 4, "total"], 1819),
        "support_entry": mutate(original, ["support_atlas", "rows", 3, "type_counts", "Z/3 + Z/18"], 24),
        "support_column": mutate(original, ["support_atlas", "type_column_order", 0], "Z/2"),
        "subset_count": mutate(original, ["support_atlas", "subset_count"], 65535),
        "generation_min": mutate(original, ["generation_complex", "named_minimum_generator_count"], 2),
        "generation_coeff": mutate(original, ["generation_complex", "generating_support_polynomial_coefficients", "3"], 24),
        "generation_count": mutate(original, ["generation_complex", "minimal_generating_support_count"], 24),
        "generation_support": mutate(original, ["generation_complex", "minimal_generating_supports", 0, 0], "S2"),
        "generation_pivot": mutate(original, ["generation_complex", "every_minimal_support_contains"], "S10"),
        "claim_lattice": mutate(original, ["claims", "entire_core_subgroup_lattice_reached"], False),
        "claim_rank": mutate(original, ["claims", "abstract_generator_rank_three_claimed"], True),
        "claim_canonical": mutate(original, ["claims", "canonical_smith_coordinates_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c72-mutations-") as temporary:
        for name, document in mutations.items():
            path = Path(temporary) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
