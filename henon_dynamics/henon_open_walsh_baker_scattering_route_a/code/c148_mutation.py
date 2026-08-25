#!/usr/bin/env python3
"""Semantic hostile mutations for the C148 evidence/checker boundary."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c148_walsh_baker_evidence.json"
CHECKER = ROOT / "code/c148_walsh_baker_checker.py"


def repair(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def rejected(data):
    with tempfile.TemporaryDirectory(prefix="c148-mut-") as temporary:
        path = Path(temporary) / "mutant.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(path), "--mutation-fast"],
            capture_output=True,
            text=True,
        )
        return result.returncode != 0


def main():
    baseline = json.loads(EVIDENCE.read_text())
    cases = [
        (("schema",), "bad-schema"),
        (("candidate_id",), "HCS-X"),
        (("evaluation_date",), "2026-08-24"),
        (("scope_literal",), "BAD"),
        (("source_lock", "basis_order"), "reverse lexicographic"),
        (("source_lock", "fourier"), "unnormalized DFT"),
        (("source_lock", "projector"), "P=diag(1,1,0)"),
        (("source_lock", "one_qutrit_gate"), "A=P F3^*"),
        (("source_lock", "shift_gate"), "A acts on v_(k-1)"),
        (("source_lock", "clock"), "k applications"),
        (("source_lock", "determinant_convention"), "1/D_k"),
        (("source_lock", "direct_trace_sentinel"), 11),
        (("one_qutrit_receipt", "trace_A_q_sqrt3_i_sqrt3i", 1), "0"),
        (("one_qutrit_receipt", "rank_A"), 3),
        (("rank_correction_and_escape_ledger", "rejected_statement"), "rank(B_k)=2*3^(k-1)"),
        (("rank_correction_and_escape_ledger", "correct_statement"), "rank(B_k)=2^k"),
        (("rank_correction_and_escape_ledger", "rows", 4, "rank_Bk"), 32),
        (("rank_correction_and_escape_ledger", "rows", 3, "rank_Bk_power_k"), 81),
        (("all_period_theorem", "trace_formula"), "Tr(B^n)=Tr(A^n)^k"),
        (("all_period_theorem", "k_step_identity"), "B_k^k=I"),
        (("all_period_theorem", "primitive_product"), "D=product(1+weight)"),
        (("all_period_theorem", "formal_status"), "entire raw product"),
        (("trace_ledgers", "5", 10, "trace_Bk_power_q_sqrt3_i_sqrt3i", 0), "1"),
        (("trace_ledgers", "3", 5, "rooted_nonzero_closed_walks"), 0),
        (("characteristic_polynomials_k1_to_k5", "5", "secular_coefficients_ascending", 32, 0), "0"),
        (("characteristic_polynomials_k1_to_k5", "4", "nonzero_coefficient_degrees"), [0, 1]),
        (("primitive_path_ledger", "rows", 7, "primitive_cycle_count"), 0),
        (("primitive_path_ledger", "finite_prefix_is_not_theorem_cutoff"), False),
        (("subunitarity_defect", "rank_each"), "2^k"),
        (("controls", "closed_control", "result"), "closed gate is contractive"),
        (("controls", "projector_order_control", "similarity"), "not similar"),
        (("controls", "hole_position_control", "alternative_linear_coefficient_q_sqrt3_i_sqrt3i", 2), "0"),
        (("controls", "antiunitary_symmetry"), "PROVED"),
        (("route_a", "tuple"), ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_ROUTE_B_READY"]),
        (("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("claim_boundary", "target_divisor_matching"), True),
        (("claim_boundary", "euler_factors"), True),
        (("claim_boundary", "root_numbers"), True),
        (("claim_boundary", "self_adjoint_hilbert_polya"), True),
    ]
    repaired = 0
    for path, value in cases:
        mutant = deepcopy(baseline)
        set_path(mutant, path, value)
        repair(mutant)
        if not rejected(mutant):
            raise SystemExit(f"repaired-hash mutant survived: {path}")
        repaired += 1
    stale = deepcopy(baseline)
    stale["rank_correction_and_escape_ledger"]["rows"][0]["rank_Bk"] = 1
    if not rejected(stale):
        raise SystemExit("stale-hash mutant survived")
    print(
        json.dumps(
            {
                "status": "PASS",
                "repaired_hash_rejections": repaired,
                "stale_hash_rejections": 1,
                "total": repaired + 1,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
