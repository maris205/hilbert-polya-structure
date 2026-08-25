#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for C155."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c155_rule90_concentration_evidence.json"
CHECKER = ROOT / "code/c155_concentration_checker.py"


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
        ("schema", ("schema",), "HCS-C155-v0"), ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-08-24"), ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"), ("object", ("source_lock", "object"), "forged"),
        ("family", ("source_lock", "family"), "L=2^r"), ("clock", ("source_lock", "clock"), "two ticks"),
        ("normalization", ("source_lock", "normalization"), "uniform on all states"),
        ("cutoff", ("source_lock", "cutoff"), "theorem r<=8"),
        ("frobenius", ("periodic_image_theorem", "frobenius_identity"), "a^L=a"),
        ("image", ("periodic_image_theorem", "periodic_set"), "all states"),
        ("restriction", ("periodic_image_theorem", "restriction_identity"), "g=I"),
        ("support", ("periodic_image_theorem", "period_support"), "all periods"),
        ("fixed_formula", ("periodic_image_theorem", "fixed_count"), "Fix=0"),
        ("gcd_dependence", ("full_period_concentration_theorem", "gcd_dependence"), "depends on j"),
        ("bezout", ("full_period_concentration_theorem", "bezout_proof"), "numeric only"),
        ("dimension", ("full_period_concentration_theorem", "dimension_bound"), "dim<=L"),
        ("proper", ("full_period_concentration_theorem", "proper_divisor_reason"), "d<=L/2"),
        ("state_bound", ("full_period_concentration_theorem", "nonfull_state_bound"), "Pr<=1"),
        ("limit", ("full_period_concentration_theorem", "full_period_limit"), "tends to zero"),
        ("burnside", ("full_period_concentration_theorem", "burnside_formula"), "C=sum Fix"),
        ("cycle_bound", ("full_period_concentration_theorem", "cycle_count_bound"), "no bound"),
        ("mean", ("full_period_concentration_theorem", "mean_period_limit"), "tends zero"),
        ("r_min", ("finite_replay", "r_min"), 1), ("r_max", ("finite_replay", "r_max"), 7),
        ("length", ("finite_replay", "family_rows", 3, "ring_length_L"), 32),
        ("periodic", ("finite_replay", "family_rows", 2, "periodic_image_points"), 1),
        ("image_dim", ("finite_replay", "family_rows", 1, "image_dimension"), 1),
        ("period_row", ("finite_replay", "family_rows", 4, "divisor_period_rows", 0, "fixed_points"), 2),
        ("proper_gcd", ("finite_replay", "family_rows", 5, "proper_time_dimension_rows", 4, "gcd_j_L"), 2),
        ("proper_dim", ("finite_replay", "family_rows", 6, "proper_time_dimension_rows", 10, "fixed_dimension"), 99),
        ("spectrum", ("finite_replay", "family_rows", 3, "fixed_dimension_spectrum", 0, "proper_times"), 0),
        ("largest", ("finite_replay", "family_rows", 2, "largest_proper_divisor"), 8),
        ("max_dim", ("finite_replay", "family_rows", 1, "maximum_proper_fixed_dimension"), 99),
        ("full", ("finite_replay", "family_rows", 4, "full_period_points"), 0),
        ("nonfull", ("finite_replay", "family_rows", 2, "nonfull_periodic_points"), 0),
        ("probability", ("finite_replay", "family_rows", 3, "full_period_state_probability", "numerator"), 0),
        ("union", ("finite_replay", "family_rows", 6, "proper_fixed_union_bound_points"), 0),
        ("cycles", ("finite_replay", "family_rows", 5, "total_periodic_cycles"), 1),
        ("burnside_sum", ("finite_replay", "family_rows", 4, "burnside_fixed_sum"), 0),
        ("mean_ratio", ("finite_replay", "family_rows", 2, "mean_cycle_length_over_L", "numerator"), 0),
        ("divisor_cells", ("finite_replay", "divisor_period_cell_count"), 0),
        ("proper_cells", ("finite_replay", "proper_time_cell_count"), 0),
        ("control", ("power_of_two_negative_control", "statement"), "invertible"),
        ("control_fixed", ("power_of_two_negative_control", "rows", 6, "fixed_counts_period_1_through_16", 3), 2),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"), ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True), ("root", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "every divisor occurs"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c155-mutations-") as temporary:
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
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C155_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
