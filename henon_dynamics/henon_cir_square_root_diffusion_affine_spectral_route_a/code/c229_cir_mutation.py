#!/usr/bin/env python3
"""Hostile mutation suite for the C229 evidence schema."""
from __future__ import annotations
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c229_cir_evidence.json"
CHECKER = ROOT / "code/c229_cir_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c229_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)


def repaired(d: dict) -> dict:
    d["payload_sha256"] = checker.payload_hash(d); return d


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text()); muts: list[tuple[str, dict]] = []
    d = deepcopy(pristine); d["payload_sha256"] = "0"*64; muts.append(("stale_hash", d))
    d = deepcopy(pristine); d["unknown_top"] = 1; muts.append(("unknown_top", repaired(d)))
    d = deepcopy(pristine); d["regression"]["unknown"] = 2; muts.append(("unknown_regression", repaired(d)))
    d = deepcopy(pristine); d["regression"]["boundary_rows"][0]["oops"] = 2; muts.append(("unknown_boundary_key", repaired(d)))
    d = deepcopy(pristine); d["source_commit"] = "0"*40; muts.append(("source_lock", repaired(d)))
    d = deepcopy(pristine); d["evaluator"]["sha256"] = "0"*64; muts.append(("evaluator_lock", repaired(d)))
    d = deepcopy(pristine); d["scope_flags"]["claims_euler_factors"] = True; muts.append(("scope_flag", repaired(d)))
    d = deepcopy(pristine); d["route_a"]["tuple"][4] = "A4_NATURAL_QUANTIZATION"; muts.append(("route_tuple", repaired(d)))
    d = deepcopy(pristine); d["theorem"]["feller_atlas"] = "all boundaries inaccessible"; muts.append(("theorem_drift", repaired(d)))
    d = deepcopy(pristine); d["regression"]["boundary_rows"][1]["feller_left_2kappa_theta"] = "5"; muts.append(("bad_feller_left", repaired(d)))
    d = deepcopy(pristine); d["regression"]["boundary_rows"][2]["boundary_class"] = "entrance_inaccessible"; muts.append(("bad_boundary_class", repaired(d)))
    d = deepcopy(pristine); d["regression"]["transform_rows"][0]["phi"] = "0"; muts.append(("bad_phi", repaired(d)))
    d = deepcopy(pristine); d["regression"]["transform_rows"].pop(); d["regression"]["transform_row_count"] = 6; muts.append(("truncated_transform", repaired(d)))
    d = deepcopy(pristine); d["regression"]["stationary_rows"][0]["mean"] = "999"; muts.append(("bad_gamma_mean", repaired(d)))
    d = deepcopy(pristine); d["regression"]["laguerre_rows"][3]["eigenvalue"] = "-99"; muts.append(("bad_eigenvalue", repaired(d)))
    d = deepcopy(pristine); d["regression"]["gap_rows"][0]["variance_factor"] = "1"; muts.append(("bad_gap", repaired(d)))
    d = deepcopy(pristine); d["regression"]["atom_rows"][0]["atom_at_zero"] = "0.9"; muts.append(("bad_atom", repaired(d)))
    d = deepcopy(pristine); d["exact_identities"][0]["name"] = "made_up"; muts.append(("identity_drift", repaired(d)))
    d = deepcopy(pristine); d["citations"][0]["doi"] = "10.invalid/example"; muts.append(("citation_drift", repaired(d)))
    d = deepcopy(pristine); d["nonclaims"].pop(); muts.append(("nonclaim_truncation", repaired(d)))
    rejected = 0; failures = []
    for name, mutant in muts:
        try: checker.validate(mutant)
        except Exception: rejected += 1
        else: failures.append(name)
    if failures: raise AssertionError(f"accepted hostile mutations: {failures}")
    print(f"C229 hostile mutation rejection: PASS {rejected}/{len(muts)}")


if __name__ == "__main__": main()
