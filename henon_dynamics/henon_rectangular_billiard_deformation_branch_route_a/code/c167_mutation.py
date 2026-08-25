#!/usr/bin/env python3
"""Hostile repaired-hash semantic mutations for HCS-C167."""
from __future__ import annotations

import argparse
import copy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def canonical_hash(payload: dict) -> str:
    clean = dict(payload)
    clean.pop("payload_sha256", None)
    return sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def changed(base: dict, path: tuple, value) -> dict:
    result = copy.deepcopy(base)
    cursor = result
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    result["payload_sha256"] = canonical_hash(result)
    return result


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path,
                        default=root / "results/c167_rectangle_evidence.json")
    args = parser.parse_args()
    base = json.loads(args.evidence.read_text())
    cases = [
        ("schema", changed(base, ("schema",), "hcs-c167-mutated")),
        ("candidate", changed(base, ("candidate_id",), "HCS-C166")),
        ("date", changed(base, ("evaluation_date",), "2026-08-24")),
        ("scope", changed(base, ("scope_literal",), "BROKEN_SCOPE")),
        ("commit", changed(base, ("source_commit",), "0" * 40)),
        ("c157_lock", changed(base, ("source_lock", "upstream_c157_evidence_sha256"), "0" * 64)),
        ("c162_lock", changed(base, ("source_lock", "upstream_c162_evidence_sha256"), "0" * 64)),
        ("trace", changed(base, ("source_lock", "trace"), "wrong trace")),
        ("all_shell", changed(base, ("source_lock", "cutoff", "all_alpha_all_shell_theorem"), False)),
        ("hard_gate", changed(base, ("hard_gate", "status"), "FAIL")),
        ("advance", changed(base, ("hard_gate", "advance_over_c162"), "finite table only")),
        ("poisson", changed(base, ("poisson_identity", "formula"), "wrong coefficient")),
        ("branch_choice", changed(base, ("poisson_identity", "principal_branch"), False)),
        ("area", changed(base, ("poisson_identity", "area_factor"), "1/alpha")),
        ("reciprocal", changed(base, ("poisson_identity", "reciprocal_aspect"), "wrong scaling")),
        ("positive_limit", changed(base, ("branch_theorem", "positive_time"), "wrong phase")),
        ("tail", changed(base, ("branch_theorem", "uniform_tail"), "finite cutoff proof")),
        ("boundary_order", changed(base, ("branch_theorem", "double_boundary_control"), "second-order pole")),
        ("collision", changed(base, ("collision_theorem", "classification"), "all beta collide")),
        ("irrational_collision", changed(base, ("collision_theorem", "irrational_branch"), "uniform gap")),
        ("divisor_overclaim", changed(base, ("collision_theorem", "general_divisor_formula_claimed"), True)),
        ("gap_overclaim", changed(base, ("collision_theorem", "irrational_uniform_gap_claimed"), True)),
        ("target_operator", changed(base, ("quantization", "target_operator_claimed"), True)),
        ("first_beta2", changed(base, ("finite_sentinels", "rational_fibres", 1,
                                         "first_positive_primitive_collision", "N"), 32)),
        ("square_65", changed(base, ("finite_sentinels", "square_swap_quotient",
                                      "first_square_symmetry_inequivalent_positive_primitive_collision_N"), 64)),
        ("irrational_false_collision", changed(base, ("finite_sentinels",
                                                        "irrational_quadratic_field",
                                                        "non_sign_collisions"), 1)),
        ("branch_multiplicity", changed(base, ("finite_sentinels", "branch_convergence", 2,
                                                "full_signed_shell_multiplicity"), 8)),
        ("route_tuple", changed(base, ("route_a", "tuple", 3), "A4_ROUTE_B_READY")),
        ("route_b", changed(base, ("route_a", "route_b_invocation_allowed"), True)),
        ("euler", changed(base, ("claim_boundary", "euler_factors"), True)),
    ]
    repaired_rejected = 0
    checker = root / "code/c167_rectangle_checker.py"
    with tempfile.TemporaryDirectory(prefix="c167-mutation-") as temp:
        temp_root = Path(temp)
        for index, (name, case) in enumerate(cases):
            path = temp_root / f"{index:02d}-{name}.json"
            path.write_text(json.dumps(case, sort_keys=True, indent=2) + "\n")
            result = subprocess.run(
                [sys.executable, str(checker), "--evidence", str(path)],
                capture_output=True, text=True,
            )
            assert result.returncode != 0, f"mutation accepted: {name}"
            repaired_rejected += 1

        stale = copy.deepcopy(base)
        stale["route_a"]["route_b_invocation_allowed"] = True
        stale_path = temp_root / "stale-hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        stale_result = subprocess.run(
            [sys.executable, str(checker), "--evidence", str(stale_path)],
            capture_output=True, text=True,
        )
        assert stale_result.returncode != 0

    print(json.dumps({
        "status": "C167_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejected,
        "stale_hash_rejections": 1,
        "total_rejections": repaired_rejected + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
