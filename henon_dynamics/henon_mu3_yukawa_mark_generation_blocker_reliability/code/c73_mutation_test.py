#!/usr/bin/env python3
"""Hostile semantic mutations for the C73 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c73_generation_blocker_reliability_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c73_generation_blocker_reliability_checker.py"


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
        "schema": mutate(original, ["schema_id"], "hcs-c73-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "authority": mutate(original, ["authority", "c72"], "0" * 64),
        "pivot": mutate(original, ["generation_structure", "pivot"], "S1"),
        "direction": mutate(original, ["generation_structure", "projective_direction_blocks", 0, "labels", 0], "S2"),
        "dummy": mutate(original, ["generation_structure", "dummy_labels", 0], "S1"),
        "criterion": mutate(original, ["generation_structure", "criterion"], "all supports generate"),
        "graph": mutate(original, ["generation_structure", "base_graph"], "K_{1,1,1,6}"),
        "edge_count": mutate(original, ["generation_structure", "base_graph_edge_count"], 24),
        "edge": mutate(original, ["generation_structure", "minimal_generating_edges", 0, 2], "S10"),
        "blocker_count": mutate(original, ["blocker_geometry", "minimal_blocker_count"], 4),
        "blocker": mutate(original, ["blocker_geometry", "minimal_blockers", 0], ["S1"]),
        "blocker_poly": mutate(original, ["blocker_geometry", "minimal_blocker_polynomial_coefficients", "4"], 2),
        "independent_poly": mutate(original, ["blocker_geometry", "independent_set_polynomial_coefficients", "2"], 12),
        "cover_poly": mutate(original, ["blocker_geometry", "vertex_cover_polynomial_coefficients", "4"], 2),
        "transversal_formula": mutate(original, ["blocker_geometry", "destructive_transversal_formula"], "x"),
        "transversal_count": mutate(original, ["blocker_geometry", "destructive_transversal_count"], 35135),
        "spectrum_row": mutate(original, ["deletion_spectrum", "rows", 4, "destructive_count"], 455),
        "spectrum_total": mutate(original, ["deletion_spectrum", "destructive_total"], 35135),
        "survivors": mutate(original, ["deletion_spectrum", "surviving_total"], 30401),
        "reliability_factor": mutate(original, ["exact_reliability", "homogeneous_factorization"], "R(q)=1"),
        "reliability_coeff": mutate(original, ["exact_reliability", "homogeneous_expanded_coefficients", "1"], 1),
        "heterogeneous": mutate(original, ["exact_reliability", "heterogeneous_direction_failure_formula"], "R=1"),
        "dummy_cancel": mutate(original, ["exact_reliability", "dummy_probabilities_cancel"], False),
        "unprotected": mutate(original, ["robustness_parameters", "unprotected_worst_case_deletion_tolerance"], 1),
        "protected": mutate(original, ["robustness_parameters", "S9_protected_worst_case_deletion_tolerance"], 4),
        "maximum": mutate(original, ["robustness_parameters", "maximum_deletions_with_some_surviving_support"], 12),
        "banzhaf": mutate(original, ["coordinate_importance", "rows", 8, "uniform_banzhaf_influence"], "1"),
        "shapley": mutate(original, ["coordinate_importance", "rows", 0, "shapley_value"], "1"),
        "symmetry_order": mutate(original, ["hypergraph_symmetry", "abstract_hypergraph_automorphism_order"], 34560),
        "symmetry_claim": mutate(original, ["hypergraph_symmetry", "identified_with_core_group_automorphisms"], True),
        "claim_blocker": mutate(original, ["claims", "blocker_geometry_beyond_C72_coefficient_reversal"], False),
        "claim_reliability": mutate(original, ["claims", "heterogeneous_reliability_proved"], False),
        "claim_robustness": mutate(original, ["claims", "three_robustness_notions_distinguished"], False),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c73-mutations-") as temporary:
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
