#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for HCS-C160."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c160_rule90_sieve_evidence.json"
CHECKER = ROOT / "code/c160_sieve_checker.py"


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
        ("schema", ("schema",), "HCS-C160-v0"), ("candidate", ("candidate_id",), "HCS-C000"),
        ("commit", ("source_commit",), "0" * 40), ("scope", ("scope_literal",), "BROKEN"),
        ("object", ("source_lock", "object"), "forged"), ("family", ("source_lock", "family"), "one L"),
        ("clock", ("source_lock", "clock"), "two steps"), ("cutoff", ("source_lock", "cutoff"), "r<=10 theorem"),
        ("gate", ("hard_gate_record", "requested_advance"), "none"), ("passed", ("hard_gate_record", "passed_by"), "finite table"),
        ("pivot", ("hard_gate_record", "model_pivot_required"), True), ("infinity", ("hard_gate_record", "no_infinitude_claim"), "infinitely many"),
        ("identity", ("periodic_image_theorem", "identity"), "a^L=a"), ("restriction", ("periodic_image_theorem", "restriction"), "g^(L-1)=I"),
        ("dimension", ("periodic_image_theorem", "fixed_dimension"), "D=d"), ("fixed", ("periodic_image_theorem", "fixed_count"), "D"),
        ("prime_set", ("maximal_subgroup_sieve_theorem", "prime_set"), "target primes"),
        ("union", ("maximal_subgroup_sieve_theorem", "nonfull_union"), "empty"),
        ("intersection", ("maximal_subgroup_sieve_theorem", "intersection"), "unknown"),
        ("formula", ("maximal_subgroup_sieve_theorem", "exact_formula"), "union bound"),
        ("bonferroni", ("maximal_subgroup_sieve_theorem", "bonferroni"), "none"),
        ("factor_boundary", ("maximal_subgroup_sieve_theorem", "source_only_factorization"), "Euler product"),
        ("range", ("mersenne_prime_cycle_theorem", "range"), "infinitely many"),
        ("support", ("mersenne_prime_cycle_theorem", "period_support", 0), 0),
        ("proof", ("mersenne_prime_cycle_theorem", "fixed_one_proof"), "numerical"),
        ("counts", ("mersenne_prime_cycle_theorem", "exact_counts"), "P_L(1)=0"),
        ("cycles", ("mersenne_prime_cycle_theorem", "cycle_count"), "0"),
        ("probability", ("mersenne_prime_cycle_theorem", "short_probability"), "asymptotic"),
        ("zeta", ("mersenne_prime_cycle_theorem", "finite_zeta"), "1"),
        ("factor_row", ("finite_replay", "family_rows", 4, "distinct_source_length_prime_factors", 0), 5),
        ("dimension_row", ("finite_replay", "family_rows", 5, "periodic_image_dimension"), 0),
        ("subset_time", ("finite_replay", "family_rows", 6, "maximal_subgroup_rows", 0, "intersection_time"), 0),
        ("subset_points", ("finite_replay", "family_rows", 7, "maximal_subgroup_rows", 1, "fixed_points"), 3),
        ("signed", ("finite_replay", "family_rows", 8, "maximal_subgroup_rows", 2, "signed_term"), 0),
        ("divisor", ("finite_replay", "family_rows", 4, "divisor_rows", 1, "fixed_dimension"), 99),
        ("nonfull", ("finite_replay", "family_rows", 6, "nonfull_periodic_points"), 0),
        ("full", ("finite_replay", "family_rows", 7, "full_period_points"), 0),
        ("prime_row", ("finite_replay", "mersenne_prime_rows", 2, "exact_period_L_points"), 0),
        ("L3", ("finite_replay", "L3_exception", "fixed_points_at_one"), 1),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"), ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True), ("prime_flag", ("scope_flags", "uses_prime_table"), True),
        ("root", ("scope_flags", "claims_root_number"), True), ("nonclaim", ("nonclaims", 0), "infinitely many exist"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c160-mutations-") as temporary:
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
    print(json.dumps({"status": "C160_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
