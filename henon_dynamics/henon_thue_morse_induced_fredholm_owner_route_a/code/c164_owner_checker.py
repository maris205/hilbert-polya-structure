#!/usr/bin/env python3
"""Producer-independent standard-library checker for HCS-C164."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c164_fredholm_owner_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def parity(n: int) -> int:
    result = 0
    while n:
        result ^= n & 1
        n >>= 1
    return result


def product(left: list[int], right: list[int], limit: int) -> list[int]:
    answer = [0] * (limit + 1)
    for i in range(limit + 1):
        for j in range(limit + 1 - i):
            answer[i + j] += left[i] * right[j]
    return answer


def fraction(record: dict) -> Fraction:
    require(set(record) == {"numerator", "denominator"}, "fraction closure")
    return Fraction(record["numerator"], record["denominator"])


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(claimed == sha256(encoded).hexdigest(), "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "induced_owner_theorem", "uninduced_no_go_theorem",
        "continuation_obstruction", "finite_replay", "progress_and_boundary",
        "route_a", "scope_flags", "nonclaims", "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C164-v1", "schema")
    require(data["candidate_id"] == "HCS-C164", "candidate")
    require(data["date_utc"] == "2026-08-25", "date")
    require(data["source_commit"] == "4342893ce5e2516924181744bfacc01c12e4959d", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "clock", "normalization", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock closure")
    require("C159" in lock["object"] and "t_s=1" in lock["object"], "source object")
    require("first-return code branches" in lock["family"] and "uninduced" in lock["family"], "family separation")
    require(lock["clock"] == "one left shift on X_S; a first-return branch 10^s has source duration s+1", "clock")
    require("zeta_X(z)^(-1)=(1-z)(1-F(z))" in lock["normalization"], "normalization")
    require("all-parameter theorems" in lock["cutoff"] and "degree 48" in lock["cutoff"], "cutoff")
    require(lock["precision"].startswith("exact integer"), "precision")
    require("Thue--Morse" in lock["allowed_data"], "allowed")
    require("Route-B inputs" in lock["forbidden_data"], "forbidden")

    owner = data["induced_owner_theorem"]
    require(set(owner) == {
        "hilbert_space", "gauge", "functional", "branch_resolution", "operator_family",
        "trace_norm_holomorphy", "rank_and_trace", "fredholm_identity",
        "gauge_invariance", "owner_status",
    }, "owner closure")
    require(owner["hilbert_space"] == "H=l2(S) with its standard orthonormal branch basis e_s", "space")
    require(owner["gauge"] == "q_s=exp(-sqrt(s+1)); u=(q_s)_{s in S}", "gauge")
    require(owner["functional"].startswith("ell_z(f)=sum"), "functional")
    require("B_s(z)" in owner["branch_resolution"] and "K_z=sum" in owner["branch_resolution"], "branch resolution")
    require(owner["operator_family"] == "K_z f=ell_z(f)u; L_z=[z] direct_sum K_z", "operator family")
    require("uniformly on |z|<=rho" in owner["trace_norm_holomorphy"] and "<infinity" in owner["trace_norm_holomorphy"], "holomorphy bound")
    require(owner["rank_and_trace"] == "rank(K_z)<=1, Tr(K_z^m)=F(z)^m for every m>=1 and |z|<1", "trace powers")
    require(owner["fredholm_identity"] == "det_F(I-L_z)=(1-z)(1-F(z))=zeta_X(z)^(-1)", "Fredholm identity")
    require("subexponential diagonal gauge" in owner["gauge_invariance"] and "same branch traces" in owner["gauge_invariance"], "gauge invariance")
    require("first-return" in owner["owner_status"] and "not the uninduced" in owner["owner_status"] and "not evidence from a scalar" in owner["owner_status"], "owner boundary")

    nogo = data["uninduced_no_go_theorem"]
    require(set(nogo) == {
        "adjacency", "normalized_basis_law", "weak_null_test", "shift_consequence",
        "return_consequence", "contradiction", "nonempty_control",
    }, "no-go closure")
    require(nogo["adjacency"] == "A delta_n=delta_(n+1)+t_n delta_0 on l2(N0,w)", "adjacency")
    require("sqrt(w_(n+1)/w_n)" in nogo["normalized_basis_law"] and "sqrt(w_0/w_n)" in nogo["normalized_basis_law"], "basis law")
    require("weakly null orthonormal basis" in nogo["weak_null_test"], "weak-null test")
    require("w_n->0" in nogo["shift_consequence"] and "w_(n+1)<=w_n/4" in nogo["shift_consequence"], "shift contradiction half")
    require("infinite set S" in nogo["return_consequence"] and "w_n->infinity" in nogo["return_consequence"], "return contradiction half")
    require("noncompact" in nogo["contradiction"] and "no Schatten class" in nogo["contradiction"], "Schatten no-go")
    require(nogo["nonempty_control"].startswith("w_n=2^n makes A bounded"), "bounded nonempty control")

    continuation = data["continuation_obstruction"]
    require(set(continuation) == {"input", "trace_transfer", "conclusion", "tautological_scalar_boundary"}, "continuation closure")
    require("C159 proves" in continuation["input"] and "no meromorphic continuation" in continuation["input"], "boundary input")
    require("trace-class meromorphic extension" in continuation["trace_transfer"] and "scalar trace" in continuation["trace_transfer"], "trace transfer")
    require("exactly on the open unit disk" in continuation["conclusion"] and "no trace-class meromorphic extension" in continuation["conclusion"], "operator boundary")
    require("scalar determinant is not operator ownership" in continuation["tautological_scalar_boundary"], "scalar nonowner")

    replay = data["finite_replay"]
    require(set(replay) == {
        "tm_prefix_length", "tm_prefix", "s_prefix", "series_limit", "F_coefficients",
        "trace_power_limit", "trace_power_rows", "determinant_coefficients",
        "branch_rows", "truncation_rows", "bounded_weight_control", "dyadic_boundary_rows",
    }, "replay closure")
    require(replay["tm_prefix_length"] == 128 and len(replay["tm_prefix"]) == 128, "prefix extent")
    expected_tm = []
    for n, observed in enumerate(replay["tm_prefix"]):
        bit = parity(n)
        expected_tm.append(bit)
        require(observed == bit, f"tm {n}")
    expected_s = [n for n, bit in enumerate(expected_tm) if bit]
    require(replay["s_prefix"] == expected_s, "S prefix")

    limit = replay["series_limit"]
    require(limit == 48, "series limit")
    expected_f = [0] + [parity(n - 1) for n in range(1, limit + 1)]
    require(replay["F_coefficients"] == expected_f, "F coefficients")
    for n, value in enumerate(replay["F_coefficients"]):
        require(value == expected_f[n], f"F cell {n}")
    require(replay["trace_power_limit"] == 6 and len(replay["trace_power_rows"]) == 6, "trace extent")
    current = [1] + [0] * limit
    for power_index, row in enumerate(replay["trace_power_rows"], 1):
        require(set(row) == {"power", "coefficients"}, f"trace row closure {power_index}")
        require(row["power"] == power_index, f"trace power {power_index}")
        current = product(current, expected_f, limit)
        require(len(row["coefficients"]) == limit + 1, f"trace length {power_index}")
        for n in range(limit + 1):
            require(row["coefficients"][n] == current[n], f"trace {power_index},{n}")

    expected_det = [0] * (limit + 1)
    expected_det[0] = 1
    for n in range(1, limit + 1):
        expected_det[n] = -expected_f[n] - (1 if n == 1 else 0) + expected_f[n - 1]
    require(replay["determinant_coefficients"] == expected_det, "determinant coefficients")
    for n, observed in enumerate(replay["determinant_coefficients"]):
        require(observed == expected_det[n], f"det cell {n}")

    require(len(replay["branch_rows"]) == 32, "branch row extent")
    for index, row in enumerate(replay["branch_rows"]):
        s = expected_s[index]
        require(row == {
            "branch_index": index,
            "gap_s": s,
            "code_length": s + 1,
            "rank_one_trace": f"z^{s + 1}",
        }, f"branch row {index}")
    require([row["gap_cutoff"] for row in replay["truncation_rows"]] == [8, 16, 32, 64, 128], "truncation cutoffs")
    for row in replay["truncation_rows"]:
        require(set(row) == {"gap_cutoff", "active_branches", "first_gap", "last_gap", "trace_polynomial_degrees"}, "truncation closure")
        active = [s for s in range(row["gap_cutoff"]) if parity(s)]
        require(row["active_branches"] == len(active), "active branches")
        require(row["first_gap"] == active[0] and row["last_gap"] == active[-1], "truncation endpoints")
        require(row["trace_polynomial_degrees"] == [s + 1 for s in active], "truncation degrees")

    control = replay["bounded_weight_control"]
    require(set(control) == {"weight", "shift_ratio_squared", "return_row_squared_norm_partial_128", "return_row_squared_norm_tail_upper"}, "control closure")
    require(control["weight"] == "w_n=2^n" and control["shift_ratio_squared"] == 2, "bounded weight")
    partial = sum(Fraction(parity(n), 2**n) for n in range(128))
    require(fraction(control["return_row_squared_norm_partial_128"]) == partial, "return row partial")
    require(fraction(control["return_row_squared_norm_tail_upper"]) == Fraction(1, 2**127), "return row tail")
    require(partial + Fraction(1, 2**127) < 2, "return functional bounded")

    require(len(replay["dyadic_boundary_rows"]) == 8, "dyadic extent")
    for level, row in enumerate(replay["dyadic_boundary_rows"], 1):
        require(row == {
            "level": level,
            "root_order": 2**level,
            "vanishing_factor": f"1-z^{2**level}",
            "operator_trace_consequence": "a trace-class meromorphic arc extension would continue F",
        }, f"dyadic row {level}")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction"}, "progress closure")
    require("closes C159's operator-owner gate" in progress["progress"] and "universal compactness obstruction" in progress["progress"], "clear progress")
    require("induced and nonunitary" in progress["route_a_obstruction"] and "no target divisor" in progress["route_a_obstruction"], "honest boundary")
    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"], "route tuple")
    require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    require("SOURCE_BRANCH_TRANSFER_OWNER" in route["A1_qualification"], "A1 qualification")
    require("NO_TARGET_DIVISOR" in route["A2_qualification"], "A2 qualification")
    require("UNIT_CIRCLE_EXTENSION_OBSTRUCTION_ONLY" in route["A3_qualification"], "A3 qualification")
    require("NO_SELF_ADJOINT_LIFT" in route["A4_qualification"], "A4 qualification")
    require(route["route_b_invocation_allowed"] is False, "Route B")
    require(data["scope_flags"] == {
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "uses_prime_table": False,
        "uses_zero_table": False,
        "claims_arithmetic_euler_factors": False,
        "claims_root_number": False,
        "claims_automorphy": False,
        "claims_hilbert_polya": False,
        "uses_route_b_inputs": False,
    }, "scope flags")
    require(data["nonclaims"] == [
        "that the induced first-return family is the uninduced time-one adjacency",
        "that a scalar determinant identity alone establishes operator ownership",
        "a target divisor, functional equation, counting-law match, or arithmetic local factorization",
        "a unitary, Hamiltonian, natural self-adjoint, or Hilbert--Polya operator",
        "Route-B authorization or a solution of the larger program",
    ], "nonclaims")
    print(json.dumps({"status": "C164_CHECKER_PASS", "assertions": checks, "payload_sha256": claimed}, sort_keys=True))


if __name__ == "__main__":
    main()
