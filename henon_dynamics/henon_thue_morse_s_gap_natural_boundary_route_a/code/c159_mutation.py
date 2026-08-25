#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for HCS-C159."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c159_s_gap_evidence.json"
CHECKER = ROOT / "code/c159_s_gap_checker.py"


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
        ("schema", ("schema",), "HCS-C159-v0"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"),
        ("object", ("source_lock", "object"), "forged"),
        ("clock", ("source_lock", "clock"), "two shifts"),
        ("cutoff", ("source_lock", "cutoff"), "finite theorem"),
        ("pivot", ("pivot_record", "rejected_candidate"), "none"),
        ("pivot_reason", ("pivot_record", "reason"), "success"),
        ("reframe", ("pivot_record", "bug_or_failure_reframed_as_insight"), True),
        ("gap", ("renewal_dynamics_theorem", "gap_set"), "all gaps"),
        ("code", ("renewal_dynamics_theorem", "code"), "C={1}"),
        ("length", ("renewal_dynamics_theorem", "short_code_lengths", 0), 1),
        ("parse", ("renewal_dynamics_theorem", "unique_circular_parse"), "ambiguous"),
        ("mixing", ("renewal_dynamics_theorem", "mixing"), "not mixing"),
        ("dense", ("renewal_dynamics_theorem", "dense_periodic_points"), "none"),
        ("T", ("exact_zeta_theorem", "T"), "0"),
        ("P", ("exact_zeta_theorem", "P"), "1"),
        ("relation", ("exact_zeta_theorem", "relation"), "T=P"),
        ("zeta", ("exact_zeta_theorem", "zeta_product"), "1"),
        ("entropy", ("exact_zeta_theorem", "entropy"), "zero"),
        ("bracket", ("exact_zeta_theorem", "entropy_root_bracket", "lower", "numerator"), 1),
        ("radial", ("natural_boundary_theorem", "radial_zero_set"), "none"),
        ("density", ("natural_boundary_theorem", "density"), "not dense"),
        ("identity", ("natural_boundary_theorem", "identity_argument"), "unsupported"),
        ("transfer", ("natural_boundary_theorem", "transfer_to_zeta"), "unsupported"),
        ("boundary", ("natural_boundary_theorem", "conclusion"), "entire"),
        ("tm", ("finite_replay", "tm_prefix", 127), 1 - source["finite_replay"]["tm_prefix"][127]),
        ("S", ("finite_replay", "s_prefix", 10), 999),
        ("fixed", ("finite_replay", "fixed_rows", 9, "fixed_points"), 0),
        ("exact", ("finite_replay", "fixed_rows", 11, "exact_period_points"), 0),
        ("cycle", ("finite_replay", "fixed_rows", 12, "primitive_cycles"), 0),
        ("P_coeff", ("finite_replay", "P_coefficients", 32), 0),
        ("renewal_coeff", ("finite_replay", "renewal_coefficients", 24), 0),
        ("zeta_coeff", ("finite_replay", "zeta_coefficients", 18), 0),
        ("denominator", ("finite_replay", "denominator_coefficients", 17), 9),
        ("dyadic", ("finite_replay", "dyadic_boundary_rows", 5, "root_order"), 63),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"),
        ("A2", ("route_a", "tuple", 1), "A2_ANALYTIC_DETERMINANT"),
        ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True),
        ("root", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "target divisor proved"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c159-mutations-") as temporary:
        for name, path, value in repaired:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            target = Path(temporary) / f"{name}.json"
            target.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(target)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        target = Path(temporary) / "stale.json"
        target.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(target)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C159_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
