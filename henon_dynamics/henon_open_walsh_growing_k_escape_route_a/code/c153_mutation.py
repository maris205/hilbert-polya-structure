#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash mutations for C153."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c153_walsh_escape_evidence.json"
CHECKER = ROOT / "code/c153_walsh_escape_checker.py"


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
    with tempfile.TemporaryDirectory(prefix="c153-mut-") as temporary:
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
        (("source_lock", "source_commit"), "WORKTREE"),
        (("source_lock", "object"), "reversed shift"),
        (("source_lock", "one_qutrit_gate"), "A=P F3^*"),
        (("source_lock", "clock"), "k applications"),
        (("source_lock", "normalization"), "2^(-k)"),
        (("source_lock", "rank_cutoff", "k_max"), 23),
        (("source_lock", "fixed_period_cluster_cutoff"), 19),
        (("source_lock", "alpha_ratios", 1), "1/3"),
        (("one_qutrit_theorem", "tau_q_sqrt3_i_sqrt3i", 1), "0"),
        (("one_qutrit_theorem", "q0_q_sqrt3_i_sqrt3i", 0), "0"),
        (("one_qutrit_theorem", "q0_is_nonzero"), False),
        (("one_qutrit_theorem", "zero_eigenvalue_is_simple"), False),
        (("one_qutrit_theorem", "rank_A_power_m"), "rank three"),
        (("all_parameter_rank_theorem", "statement"), "rank=2^n"),
        (("all_parameter_rank_theorem", "initial_boundary"), "rank two"),
        (("all_parameter_rank_theorem", "ledger_rows", 0, "rank_Bk_power_n"), 2),
        (("all_parameter_rank_theorem", "ledger_rows", 20, "q"), 99),
        (("all_parameter_rank_theorem", "ledger_rows", 100, "kernel_dimension"), 0),
        (("all_parameter_rank_theorem", "ledger_rows", 300, "rank_fraction"), "1/1"),
        (("macroscopic_escape_theorem", "time_scale"), "n=alpha"),
        (("macroscopic_escape_theorem", "signed_log_survival_limit"), "zero"),
        (("macroscopic_escape_theorem", "positive_escape_exponent"), "zero"),
        (("macroscopic_escape_theorem", "alpha_zero_boundary"), "undefined"),
        (("macroscopic_escape_theorem", "finite_ratio_ledger", 40, "n_floor_alpha_k"), 99),
        (("macroscopic_escape_theorem", "finite_ratio_ledger", 80, "rank"), 0),
        (("macroscopic_escape_theorem", "finite_ratio_ledger", 120, "finite_k_log_survival_coefficient"), "9"),
        (("fixed_period_trace_theorem", "trace_formula"), "Tr=t_n^k"),
        (("fixed_period_trace_theorem", "normalized_limit"), "does not vanish"),
        (("fixed_period_trace_theorem", "periods", 1, "divisor_classes", 0, "trace_value_q_sqrt3_i_sqrt3i", 0), "0"),
        (("fixed_period_trace_theorem", "periods", 5, "divisor_classes", 1, "d"), 5),
        (("fixed_period_trace_theorem", "periods", 7, "distinct_cluster_value_count"), 99),
        (("fixed_period_trace_theorem", "periods", 9, "merged_cluster_values", 0, "divisor_classes"), [99]),
        (("unnormalized_nonconvergence_witness", "fixed_period"), 3),
        (("unnormalized_nonconvergence_witness", "odd_k_trace_t2_q_sqrt3_i_sqrt3i", 0), "0"),
        (("unnormalized_nonconvergence_witness", "difference_t2_minus_tau_squared_q_sqrt3_i_sqrt3i", 3), "0"),
        (("controls", "closed_parent", "projector"), "P=0"),
        (("controls", "closed_parent", "result"), "escape exponent is positive"),
        (("controls", "projector_order", "gate"), "not similar"),
        (("controls", "hole_position", "one_site_characteristic_polynomial"), "lambda^3"),
        (("controls", "hole_position", "rank_result"), "rank collapses"),
        (("controls", "hole_position", "trace_result"), "trace cluster values can never change"),
        (("route_a", "tuple"), ["A1_PASS", "A2_PASS", "A3_PASS", "A4_ROUTE_B_READY"]),
        (("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("claim_boundary", "full_secular_limit"), True),
        (("claim_boundary", "euler_factors"), True),
        (("claim_boundary", "hilbert_polya_operator"), True),
        (("nonclaims", 5), "authorization granted"),
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
    stale["all_parameter_rank_theorem"]["ledger_rows"][0]["rank_Bk_power_n"] = 1
    if not rejected(stale):
        raise SystemExit("stale-hash mutant survived")
    print(
        json.dumps(
            {
                "status": "C153_MUTATION_PASS",
                "repaired_hash_rejections": repaired,
                "stale_hash_rejections": 1,
                "total": repaired + 1,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
