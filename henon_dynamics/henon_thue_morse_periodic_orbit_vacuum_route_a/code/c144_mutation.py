#!/usr/bin/env python3
"""Repaired-hash and stale-hash mutation audit for C144."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c144_thue_morse_evidence.json"
CHECKER = ROOT / "code/c144_thue_morse_checker.py"


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
        ("schema", ("schema",), "HCS-C144-v0"),
        ("date", ("date_utc",), "2026-08-24"),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("object", ("source_lock", "object"), "periodic full shift"),
        ("clock", ("source_lock", "clock"), "two iterates"),
        ("normalization", ("source_lock", "normalization"), "forged"),
        ("determinant", ("source_lock", "determinant_convention"), "det(I-A)"),
        ("cutoff", ("source_lock", "cutoff"), "theorem cutoff 32"),
        ("nonempty", ("structural_theorems", "nonempty"), False),
        ("minimal", ("structural_theorems", "minimal"), False),
        ("recurrence", ("structural_theorems", "fixed_point_recurrence"), "forged"),
        ("statement", ("aperiodicity_theorem", "statement"), "has periodic points"),
        ("all_periods", ("aperiodicity_theorem", "all_positive_periods"), False),
        ("certificate_period", ("aperiodicity_theorem", "period_certificates", 4, "putative_period"), 6),
        ("certificate_k", ("aperiodicity_theorem", "period_certificates", 7, "odd_exponent_k"), 4),
        ("certificate_d", ("aperiodicity_theorem", "period_certificates", 10, "multiple_d"), 1),
        ("certificate_parity", ("aperiodicity_theorem", "period_certificates", 13, "binary_digit_parity_of_d"), 0),
        ("certificate_bound", ("aperiodicity_theorem", "period_certificates", 17, "forbidden_window_length"), 2),
        ("complexity", ("language_prefix", "rows", 8, "complexity"), 1),
        ("language_hash", ("language_prefix", "rows", 5, "language_sha256"), "0" * 64),
        ("approx_period", ("periodic_approximants", "rows", 5, "least_cyclic_period"), 1),
        ("approx_balance", ("periodic_approximants", "rows", 3, "zero_count"), 1),
        ("word_hash", ("periodic_approximants", "rows", 7, "word_sha256"), "0" * 64),
        ("bad_count", ("periodic_approximants", "rows", 2, "block_defects", 4, "invalid_rooted_windows"), 99),
        ("bad_starts", ("periodic_approximants", "rows", 4, "block_defects", 2, "invalid_start_indices"), [0]),
        ("defect_cells", ("periodic_approximants", "defect_cells"), 0),
        ("fixed_count", ("periodic_orbit_vacuum", "periodic_point_counts", 8, "fixed_points"), 1),
        ("zeta", ("periodic_orbit_vacuum", "artin_mazur_zeta"), "zeta=2"),
        ("coefficient", ("periodic_orbit_vacuum", "zeta_coefficients_through_degree_32", 7), 1),
        ("A1", ("route_a", "tuple", 0), "A1_WEAK"),
        ("overall", ("route_a", "overall"), "ROUTE_A_EXPLORATORY"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime_flag", ("scope_flags", "uses_prime_table"), True),
        ("root_flag", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "approximants belong"),
        ("extra_key", ("progress_and_boundary", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c144-mutations-") as temporary:
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
    print(json.dumps({"status": "C144_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
