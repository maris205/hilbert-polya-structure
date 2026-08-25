#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for HCS-C164."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c164_fredholm_owner_evidence.json"
CHECKER = ROOT / "code/c164_owner_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def set_path(container, path, value) -> None:
    current = container
    for item in path[:-1]:
        current = current[item]
    current[path[-1]] = value


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C164-v0"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-01-01"),
        ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"),
        ("object", ("source_lock", "object"), "forged"),
        ("family", ("source_lock", "family"), "scalar only"),
        ("clock", ("source_lock", "clock"), "first return is one tick"),
        ("normalization", ("source_lock", "normalization"), "det=0"),
        ("cutoff", ("source_lock", "cutoff"), "finite theorem"),
        ("precision", ("source_lock", "precision"), "floating inference"),
        ("allowed", ("source_lock", "allowed_data"), "target table"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("space", ("induced_owner_theorem", "hilbert_space"), "C"),
        ("gauge", ("induced_owner_theorem", "gauge"), "q=1"),
        ("functional", ("induced_owner_theorem", "functional"), "ell=0"),
        ("branches", ("induced_owner_theorem", "branch_resolution"), "none"),
        ("family_op", ("induced_owner_theorem", "operator_family"), "scalar"),
        ("holomorphy", ("induced_owner_theorem", "trace_norm_holomorphy"), "assumed"),
        ("trace", ("induced_owner_theorem", "rank_and_trace"), "Tr=0"),
        ("fredholm", ("induced_owner_theorem", "fredholm_identity"), "det=1"),
        ("invariance", ("induced_owner_theorem", "gauge_invariance"), "gauge dependent"),
        ("owner", ("induced_owner_theorem", "owner_status"), "time-one adjacency"),
        ("adjacency", ("uninduced_no_go_theorem", "adjacency"), "A=0"),
        ("basis", ("uninduced_no_go_theorem", "normalized_basis_law"), "forged"),
        ("weak", ("uninduced_no_go_theorem", "weak_null_test"), "none"),
        ("shift", ("uninduced_no_go_theorem", "shift_consequence"), "weights grow"),
        ("return", ("uninduced_no_go_theorem", "return_consequence"), "weights vanish"),
        ("contradiction", ("uninduced_no_go_theorem", "contradiction"), "trace class"),
        ("control", ("uninduced_no_go_theorem", "nonempty_control"), "no bounded example"),
        ("boundary_input", ("continuation_obstruction", "input"), "entire"),
        ("trace_transfer", ("continuation_obstruction", "trace_transfer"), "unsupported"),
        ("boundary", ("continuation_obstruction", "conclusion"), "extends across circle"),
        ("scalar", ("continuation_obstruction", "tautological_scalar_boundary"), "scalar suffices"),
        ("tm", ("finite_replay", "tm_prefix", 63), 1 - source["finite_replay"]["tm_prefix"][63]),
        ("S", ("finite_replay", "s_prefix", 12), 999),
        ("F", ("finite_replay", "F_coefficients", 31), 9),
        ("trace_power", ("finite_replay", "trace_power_rows", 3, "power"), 99),
        ("trace_cell", ("finite_replay", "trace_power_rows", 4, "coefficients", 40), 999),
        ("det", ("finite_replay", "determinant_coefficients", 24), 8),
        ("branch", ("finite_replay", "branch_rows", 15, "code_length"), 999),
        ("trunc", ("finite_replay", "truncation_rows", 2, "active_branches"), 0),
        ("weight", ("finite_replay", "bounded_weight_control", "weight"), "w=1"),
        ("shift_ratio", ("finite_replay", "bounded_weight_control", "shift_ratio_squared"), 1),
        ("return_norm", ("finite_replay", "bounded_weight_control", "return_row_squared_norm_partial_128", "numerator"), 1),
        ("dyadic", ("finite_replay", "dyadic_boundary_rows", 5, "root_order"), 63),
        ("progress", ("progress_and_boundary", "progress"), "no progress"),
        ("obstruction", ("progress_and_boundary", "route_a_obstruction"), "target solved"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"),
        ("A2", ("route_a", "tuple", 1), "A2_ANALYTIC_DETERMINANT"),
        ("A3", ("route_a", "tuple", 2), "A3_GLOBAL_STRUCTURE"),
        ("A4", ("route_a", "tuple", 3), "A4_NATURAL_QUANTIZATION"),
        ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True),
        ("zero", ("scope_flags", "uses_zero_table"), True),
        ("euler", ("scope_flags", "claims_arithmetic_euler_factors"), True),
        ("root", ("scope_flags", "claims_root_number"), True),
        ("automorphy", ("scope_flags", "claims_automorphy"), True),
        ("hp", ("scope_flags", "claims_hilbert_polya"), True),
        ("nonclaim", ("nonclaims", 0), "time-one owner"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c164-mutations-") as temporary:
        for name, path, value in repaired:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            target = Path(temporary) / f"{name}.json"
            target.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            run = subprocess.run([sys.executable, str(CHECKER), str(target)], capture_output=True, text=True)
            if run.returncode == 0:
                raise AssertionError(f"repaired-hash mutation survived: {name}")
            rejected.append(name)

        stale = deepcopy(source)
        stale["route_a"]["route_b_invocation_allowed"] = True
        stale_target = Path(temporary) / "stale.json"
        stale_target.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        stale_run = subprocess.run([sys.executable, str(CHECKER), str(stale_target)], capture_output=True, text=True)
        if stale_run.returncode == 0:
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C164_MUTATION_PASS", "repaired_hash_rejected": len(rejected), "stale_hash_rejected": 1, "cases": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
