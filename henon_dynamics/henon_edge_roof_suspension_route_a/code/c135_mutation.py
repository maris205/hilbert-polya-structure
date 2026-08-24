#!/usr/bin/env python3
"""Repaired-hash plus stale-hash mutation suite for C135."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c135_edge_roof_evidence.json"
CHECKER = ROOT / "code/c135_edge_roof_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main():
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C135-forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("scope", ("scope_literal",), "ALLOW_FORBIDDEN_DATA"),
        ("roof_entry", ("source_lock", "roof_matrix", 0, 1), "sqrt(5)"),
        ("determinant_lock", ("source_lock", "determinant_convention"), "det(I+M)"),
        ("formal_determinant", ("frozen_model", "formal_determinant"), "Delta=1-x00-x11+x01*x10"),
        ("determinant_receipt", ("frozen_model", "formal_determinant_receipt", "0,1,1,0"), 1),
        ("laplace_matrix", ("frozen_model", "laplace_matrix", 1, 0), "exp(-sqrt(5)*s)"),
        ("exponential_polynomial", ("frozen_model", "exponential_polynomial"), "FORGED_EXPONENTIAL"),
        ("basis", ("frozen_model", "basis_independence"), "dependent basis"),
        ("trace_formula", ("all_period_identity", "trace_formula"), "FORGED_TRACE"),
        ("log_determinant", ("all_period_identity", "log_determinant"), "FORGED_LOG"),
        ("primitive_product", ("all_period_identity", "primitive_product"), "FORGED_PRODUCT"),
        ("suspension_product", ("all_period_identity", "suspension_product"), "FORGED_SUSPENSION"),
        ("roof_length", ("all_period_identity", "roof_length"), "FORGED_LENGTH"),
        ("sector_injectivity", ("edge_sector_theorem", "injectivity"), "orbit injective"),
        ("flow_conservation", ("edge_sector_theorem", "flow_conservation"), "N01 need not equal N10"),
        ("observable_sum", ("edge_sector_theorem", "observable_off_diagonal_combination"), "tau01 and tau10 separately"),
        ("orientation_boundary", ("edge_sector_theorem", "orientation_blindness"), "orientation recovered"),
        ("nonlattice", ("edge_sector_theorem", "nonlattice_witness"), "all lengths rational"),
        ("trace_row", ("replay_prefix", "rows", 5, "trace_edge_count_coefficients", "2,1,1,2"), 7),
        ("primitive_rep", ("replay_prefix", "primitive_representatives", "6", 0), "000000"),
        ("rooted_total", ("replay_prefix", "rooted_closed_words_total"), 2045),
        ("word_receipt", ("controls", "word_receipts", "symbol_count_collision_C130_a", "edge_counts_N00_N01_N10_N11", 0), 1),
        ("separated_pair", ("controls", "separated_pair", 1), "001101"),
        ("separation_vector", ("controls", "separation_vector_1_sqrt2_sqrt3_sqrt6", 0), 0),
        ("separation_statement", ("controls", "separation_statement"), "the lengths agree"),
        ("multiplicity6", ("controls", "period6_trace_multiplicity_000111_sector"), 5),
        ("multiplicity12", ("controls", "period6_trace_multiplicity_001011_sector"), 11),
        ("collision_pair", ("controls", "remaining_collision_pair", 1), "000111"),
        ("collision_counts", ("controls", "remaining_collision_edge_counts", 0), 2),
        ("collision_nonrotation", ("controls", "remaining_collision_is_nonrotation"), False),
        ("first_collision", ("controls", "first_same_edge_count_primitive_collision_period"), 5),
        ("C130_control", ("controls", "C130_destination_symbol_control"), "FORGED_CONTROL"),
        ("progress", ("progress_and_boundary", "progress_over_C130"), "FORGED_PROGRESS"),
        ("boundary", ("progress_and_boundary", "remaining_internal_obstruction"), "all orbits recovered"),
        ("A4_promotion", ("route_a", "tuple", 3), "A4_ROUTE_B_READY"),
        ("A1_qualification", ("route_a", "A1_qualification"), "PRIME_MATCH"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("scope_flag", ("scope_flags", "claims_arithmetic_euler_factors"), True),
        ("nonclaim", ("nonclaims", 0), "orbit injectivity"),
        ("extra_key", ("edge_sector_theorem", "forged_headline"), "FORGED"),
    ]
    cases = [(name, path, value, True) for name, path, value in repaired]
    cases.append(("stale_payload_hash", ("payload_sha256",), "0" * 64, False))
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c135-mutations-") as tmp:
        for name, path, value, repair in cases:
            data = deepcopy(source)
            set_path(data, path, value)
            if repair:
                data["payload_sha256"] = payload_hash(data)
            candidate = Path(tmp) / f"{name}.json"
            candidate.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            completed = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if completed.returncode == 0:
                raise AssertionError(f"checker accepted mutation: {name}")
            rejected.append(name)
    print(json.dumps({"status": "C135_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(cases), "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
