#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for C149."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c149_skeleton_evidence.json"
CHECKER = ROOT / "code/c149_skeleton_checker.py"


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
        ("schema", ("schema",), "HCS-C149-v0"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-08-24"),
        ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"),
        ("object", ("source_lock", "object"), "forged union"),
        ("clock", ("source_lock", "clock"), "two ticks"),
        ("cutoff", ("source_lock", "cutoff"), "theorem cutoff 60"),
        ("substitution", ("thue_morse_component", "substitution", "0"), "00"),
        ("tm_status", ("thue_morse_component", "status"), "PERIODIC"),
        ("tm_points", ("thue_morse_component", "periodic_points"), 1),
        ("tm_all", ("thue_morse_component", "all_positive_fixed_counts_zero"), False),
        ("proof", ("thue_morse_component", "proof_certificate"), "seed mismatch only"),
        ("cert_limit", ("thue_morse_component", "period_certificate_limit"), 31),
        ("cert_k", ("thue_morse_component", "period_certificates", 4, "odd_exponent_k"), 2),
        ("cert_d", ("thue_morse_component", "period_certificates", 9, "multiple_d"), 1),
        ("cert_bit", ("thue_morse_component", "period_certificates", 14, "tm_bit_at_d"), 0),
        ("lengths", ("finite_skeleton", "cycle_lengths"), [1, 2, 3, 4]),
        ("total", ("finite_skeleton", "total_points"), 10),
        ("row", ("finite_skeleton", "cycle_rows", 2, "primitive_cycles"), 2),
        ("successor", ("finite_skeleton", "successor_table", "tag_5:0"), "tag_5:0"),
        ("topology", ("finite_skeleton", "topology"), "not disjoint"),
        ("formula", ("all_period_theorem", "fixed_count_formula"), "Fix=0"),
        ("primitive", ("all_period_theorem", "primitive_skeleton", 1, "primitive_cycles"), 2),
        ("other", ("all_period_theorem", "no_other_primitive_cycles"), False),
        ("zeta", ("all_period_theorem", "artin_mazur_zeta"), "1"),
        ("minimal", ("all_period_theorem", "minimality_obstruction"), "still minimal"),
        ("period_limit", ("finite_replay", "period_limit"), 59),
        ("fixed", ("finite_replay", "rows", 29, "fixed_points"), 0),
        ("labels", ("finite_replay", "rows", 14, "fixed_point_labels"), []),
        ("exact", ("finite_replay", "rows", 4, "exact_period_points"), 0),
        ("cycle", ("finite_replay", "rows", 2, "primitive_cycles"), 0),
        ("fixed_sum", ("finite_replay", "fixed_count_sum"), 0),
        ("zeta_coeff", ("finite_replay", "zeta_coefficients", 15), 0),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"),
        ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True),
        ("root", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 1), "almost minimal"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c149-mutations-") as temporary:
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
    print(json.dumps({"status": "C149_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
