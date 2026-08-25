#!/usr/bin/env python3
"""Repaired-hash and stale-hash mutation audit for C145."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c145_rule90_evidence.json"
CHECKER = ROOT / "code/c145_rule90_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(container, path, value) -> None:
    current = container
    for item in path[:-1]:
        current = current[item]
    current[path[-1]] = value


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C145-v0"),
        ("date", ("date_utc",), "2026-08-24"),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("object", ("source_lock", "object"), "Rule 30"),
        ("clock", ("source_lock", "clock"), "area only"),
        ("normalization", ("source_lock", "normalization"), "divide Fix by n"),
        ("determinant", ("source_lock", "determinant_convention"), "target determinant matched"),
        ("cutoff", ("source_lock", "cutoff"), "theorem through 24"),
        ("theorem", ("kernel_gcd_theorem", "statement"), "wrong gcd"),
        ("clearance", ("kernel_gcd_theorem", "laurent_clearance"), "wrong sign"),
        ("kernel_lemma", ("kernel_gcd_theorem", "kernel_lemma"), "distinct roots only"),
        ("kernel_proof", ("kernel_gcd_theorem", "kernel_proof"), "forged proof"),
        ("all_sizes", ("kernel_gcd_theorem", "all_positive_lengths_and_times"), False),
        ("row_degree", ("two_clock_table", "rows", 0, "gcd_degree"), 1),
        ("row_fixed", ("two_clock_table", "rows", 100, "fixed_points"), 3),
        ("row_exact", ("two_clock_table", "rows", 250, "exact_temporal_period_points"), 1),
        ("row_cycles", ("two_clock_table", "rows", 400, "primitive_temporal_cycles"), 99),
        ("row_area", ("two_clock_table", "rows", 575, "area_Ln"), 1),
        ("cell_count", ("two_clock_table", "cell_count"), 575),
        ("fixed_sum", ("two_clock_table", "fixed_point_sum"), 0),
        ("exact_sum", ("two_clock_table", "exact_period_point_sum"), 0),
        ("cycle_sum", ("two_clock_table", "primitive_cycle_sum"), 0),
        ("mobius", ("mobius_orbit_theorem", "exact_period_formula"), "wrong inversion"),
        ("cycle_formula", ("mobius_orbit_theorem", "cycle_formula"), "C=P"),
        ("torus_equation", ("spatiotemporal_torus", "equations"), "wrong local rule"),
        ("global_area", ("aspect_ratio_witnesses", "global_positive_domain", "minimal_same_area_with_different_fixed_counts", "area"), 6),
        ("nondegenerate_area", ("aspect_ratio_witnesses", "nondegenerate_domain", "minimal_same_area_with_different_fixed_counts", "area"), 3),
        ("nonzero_area", ("aspect_ratio_witnesses", "nonzero_exact_period_domain", "minimal_same_area_with_different_fixed_counts", "area"), 6),
        ("control_fixed", ("aspect_ratio_witnesses", "same_fixed_count_different_primitive_structure", "first_cell", "fixed_points"), 8),
        ("control_exact", ("aspect_ratio_witnesses", "same_fixed_count_different_primitive_structure", "second_cell", "exact_temporal_period_points"), 15),
        ("conclusion", ("aspect_ratio_witnesses", "conclusion"), "area sufficient"),
        ("even_cell", ("even_length_control", "cell", "gcd_degree"), 0),
        ("factorization", ("even_length_control", "factorization"), "squarefree"),
        ("progress", ("progress_and_boundary", "progress"), "forged"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS_ANALYTIC"),
        ("A2", ("route_a", "tuple", 1), "A2_ANALYTIC_DETERMINANT"),
        ("overall", ("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime_flag", ("scope_flags", "uses_prime_table"), True),
        ("automorphy_flag", ("scope_flags", "claims_automorphy"), True),
        ("nonclaim", ("nonclaims", 1), "area determines geometry"),
        ("extra_key", ("even_length_control", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c145-mutations-") as temporary:
        for name, path, value in repaired:
            candidate_data = deepcopy(source)
            set_path(candidate_data, path, value)
            candidate_data["payload_sha256"] = payload_hash(candidate_data)
            candidate = Path(temporary) / f"{name}.json"
            candidate.write_text(json.dumps(candidate_data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        candidate = Path(temporary) / "stale.json"
        candidate.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale payload hash")
    print(json.dumps({"status": "C145_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
