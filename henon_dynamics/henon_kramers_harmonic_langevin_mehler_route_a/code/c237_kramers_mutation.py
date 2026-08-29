#!/usr/bin/env python3
"""Hostile schema, provenance and numerical mutation suite for C237."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c237_kramers_evidence.json"
CHECKER = ROOT / "code/c237_kramers_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c237_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repaired(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    mutations: list[tuple[str, dict]] = []

    def add(name: str, data: dict, fix_hash: bool = True) -> None:
        mutations.append((name, repaired(data) if fix_hash else data))

    d = deepcopy(pristine); d["payload_sha256"] = "0" * 64; add("stale_hash", d, False)
    d = deepcopy(pristine); d["unknown_top"] = 1; add("unknown_top", d)
    d = deepcopy(pristine); d["regression"]["unknown"] = 1; add("unknown_regression", d)
    d = deepcopy(pristine); d["regression"]["regime_rows"][0]["oops"] = 1; add("unknown_matrix_key", d)
    d = deepcopy(pristine); d["regression"]["transition_rows"][0]["oops"] = 1; add("unknown_transition_key", d)
    d = deepcopy(pristine); d["source_commit"] = "0" * 40; add("source_lock", d)
    d = deepcopy(pristine); d["evaluator"]["sha256"] = "0" * 64; add("evaluator_lock", d)
    d = deepcopy(pristine); d["scope_literal"] = "UNSCOPED"; add("scope_literal", d)
    d = deepcopy(pristine); d["scope_flags"]["claims_euler_factors"] = True; add("scope_flag", d)
    d = deepcopy(pristine); d["route_a"]["tuple"][4] = "A4_NATURAL_QUANTIZATION"; add("route_tuple", d)
    d = deepcopy(pristine); d["route_a"]["route_b_invocation_allowed"] = True; add("route_b", d)
    d = deepcopy(pristine); d["theorem"]["matrix_exponential"] = "wrong flow"; add("matrix_theorem_drift", d)
    d = deepcopy(pristine); d["theorem"]["l2_boundary"] = "full spectrum proved"; add("l2_overclaim", d)
    d = deepcopy(pristine); d["exact_identities"][0]["name"] = "invented"; add("identity_drift", d)
    d = deepcopy(pristine); d["citations"][0]["doi"] = "10.invalid/example"; add("citation_drift", d)
    d = deepcopy(pristine); d["nonclaims"].pop(); add("nonclaim_truncation", d)
    d = deepcopy(pristine); d["regression"]["regime_rows"][0]["m11"] = "999"; add("bad_matrix", d)
    d = deepcopy(pristine); d["regression"]["transition_rows"][2]["cov_det"] = "0"; add("bad_covariance", d)
    d = deepcopy(pristine); d["regression"]["correlation_rows"][0]["rho_QP"] = "0"; add("bad_correlation", d)
    d = deepcopy(pristine); d["regression"]["rate_rows"][4]["rate"] = "999"; add("bad_rate", d)
    d = deepcopy(pristine); d["regression"]["rate_rows"][3]["critical_polynomial_prefactor"] = False; add("bad_critical_flag", d)
    d = deepcopy(pristine); d["regression"]["kalman_rows"][1]["controllability_rank"] = 0; add("bad_kalman_rank", d)
    d = deepcopy(pristine); d["regression"]["gibbs_rows"][0]["variance_Q"] = "0"; add("bad_gibbs_variance", d)
    # Every boundary sentinel is semantically locked by the checker.  These
    # repaired-hash mutants specifically exercise the four rows that were
    # previously covered only by a length/key smoke test.
    d = deepcopy(pristine); d["regression"]["boundary_rows"][0]["classification"] = "confining_hypoelliptic_overdamped"; add("boundary_under_classification", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][1]["stationary_law"] = "many_invariant_energy_measures"; add("boundary_critical_stationarity", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][2]["mixing"] = "no_mixing"; add("boundary_over_mixing", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][3]["position_variance"] = "infinite"; add("boundary_zero_gamma_variance", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][0]["omega"] = "9"; add("boundary_under_parameter", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][1]["case_id"] = "boundary_under"; add("boundary_critical_id", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][-1]["position_variance"] = "finite"; add("bad_boundary", d)
    d = deepcopy(pristine); d["regression"]["transition_rows"].pop(); add("truncated_transition", d)
    d = deepcopy(pristine); d["regression"]["boundary_rows"][-1]["classification"] = "confining_hypoelliptic"; add("boundary_class_drift", d)

    rejected = 0
    failures: list[str] = []
    for name, mutant in mutations:
        try:
            checker.validate(mutant)
        except Exception:
            rejected += 1
        else:
            failures.append(name)
    if failures:
        raise AssertionError(f"accepted hostile mutations: {failures}")
    print(f"C237 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
