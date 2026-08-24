#!/usr/bin/env python3
"""Hostile-evidence mutation suite for the independent C124 checker."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c124_hardy_evidence.json"
CHECKER = ROOT / "code/c124_hardy_checker.py"


def main() -> None:
    source = json.loads(EVIDENCE.read_text())

    def set_path(data: dict, path: tuple[object, ...], value: object) -> None:
        target: object = data
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]

    mutations = [
        ("schema", ("schema",), "hcs-c124-forged"),
        ("scope", ("scope_literal",), "ALLOW_FORBIDDEN_DATA"),
        ("A_entry", ("frozen_model", "A", 0, 0), "1/4"),
        ("translation", ("frozen_model", "translations", 0), "-3"),
        ("adjacency", ("frozen_model", "adjacency_B", 0, 2), "1"),
        ("edge_weight", ("frozen_model", "edge_weights_c", 1), "1/4"),
        ("weighted_matrix", ("frozen_model", "weighted_adjacency_W_equals_B_diag_c", 0, 1), "1/4"),
        ("separation_gap", ("strong_separation", "original_pairwise_first_coordinate_gap"), "-1"),
        ("rooted_count", ("periodic_orbits", "rooted_closed_word_counts_n1_to_8", "8"), 132),
        ("primitive_rep", ("periodic_orbits", "primitive_representatives_n1_to_8", "3", 1), "011"),
        ("cycle_point", ("periodic_orbits", "example_fixed_phase_points", 0, 0), "0"),
        ("hardy_trace", ("hardy_operator", "hardy_trace_powers_n1_to_8", "3"), "1"),
        ("fredholm_coefficient", ("fredholm_and_primitive_identity", "taylor_coefficients_ascending_z0_to_z8", 4), "0"),
        ("control_point", ("translation_blindness_control", "control_example_fixed_phase_points", 0, 0), "0"),
        ("A2_promotion", ("verdict", "A2"), "A2_ANALYTIC_DETERMINANT"),
        ("route_b", ("verdict", "route_b_invocation_allowed"), True),
        ("nonclaim", ("nonclaims", 5), "determinant sees every translation"),
    ]

    rejected = []
    with tempfile.TemporaryDirectory(prefix="c124-mutations-") as tmp:
        for name, path, value in mutations:
            data = deepcopy(source)
            set_path(data, path, value)
            candidate = Path(tmp) / f"{name}.json"
            candidate.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
            completed = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if completed.returncode == 0:
                raise AssertionError(f"checker accepted hostile mutation: {name}")
            rejected.append(name)

    print(json.dumps({"status": "C124_MUTATION_PASS", "rejected": len(rejected), "total": len(mutations), "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
