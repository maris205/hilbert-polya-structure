#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for C150."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c150_rule90_mersenne_evidence.json"
CHECKER = ROOT / "code/c150_mersenne_checker.py"


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
        ("schema", ("schema",), "HCS-C150-v0"), ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-08-24"), ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"), ("object", ("source_lock", "object"), "forged"),
        ("family", ("source_lock", "family"), "L=2^r"), ("clock", ("source_lock", "clock"), "two ticks"),
        ("cutoff", ("source_lock", "cutoff"), "theorem r<=8"),
        ("frobenius", ("mersenne_theorem", "frobenius_identity"), "a^L=a"),
        ("identity", ("mersenne_theorem", "equivalent_identity"), "a^L=a"),
        ("kernel", ("mersenne_theorem", "kernel_statement"), "kernel zero"),
        ("kernel_proof", ("mersenne_theorem", "kernel_proof"), "forged"),
        ("image", ("mersenne_theorem", "image_periodicity"), "not periodic"),
        ("entry", ("mersenne_theorem", "eventual_image"), "two steps"),
        ("equal", ("mersenne_theorem", "periodic_set_equals_image"), False),
        ("fraction", ("mersenne_theorem", "periodic_fraction"), "1/3"),
        ("period_support", ("mersenne_theorem", "all_cycle_periods_divide_L"), False),
        ("fixed_formula", ("fixed_and_primitive_formula", "fixed_count"), "Fix=0"),
        ("exact_formula", ("fixed_and_primitive_formula", "exact_period"), "P=Fix"),
        ("cycle_formula", ("fixed_and_primitive_formula", "primitive_cycles"), "C=P"),
        ("r_limit", ("mersenne_replay", "r_limit"), 7),
        ("length", ("mersenne_replay", "family_rows", 4, "ring_length_L"), 32),
        ("rank", ("mersenne_replay", "family_rows", 5, "image_dimension"), 1),
        ("periodic", ("mersenne_replay", "family_rows", 2, "periodic_points"), 1),
        ("transient", ("mersenne_replay", "family_rows", 3, "transient_points"), 0),
        ("entry_time", ("mersenne_replay", "family_rows", 1, "entry_time_bound"), 2),
        ("row_period", ("mersenne_replay", "family_rows", 6, "divisor_period_rows", 1, "period_n"), 2),
        ("row_fixed", ("mersenne_replay", "family_rows", 7, "divisor_period_rows", 0, "fixed_points"), 2),
        ("row_exact", ("mersenne_replay", "family_rows", 3, "divisor_period_rows", 1, "exact_period_points"), 0),
        ("cell_count", ("mersenne_replay", "divisor_period_cell_count"), 26),
        ("periodic_sum", ("mersenne_replay", "periodic_point_sum"), 0),
        ("control_statement", ("power_of_two_negative_control", "statement"), "invertible"),
        ("control_length", ("power_of_two_negative_control", "rows", 4, "ring_length_L"), 31),
        ("control_exp", ("power_of_two_negative_control", "rows", 6, "annihilating_iterate"), 1),
        ("control_state", ("power_of_two_negative_control", "rows", 1, "only_periodic_state"), "all"),
        ("control_fixed", ("power_of_two_negative_control", "rows", 7, "fixed_counts_period_1_through_16", 5), 2),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"), ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True), ("root", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "every divisor occurs"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c150-mutations-") as temporary:
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
    print(json.dumps({"status": "C150_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
