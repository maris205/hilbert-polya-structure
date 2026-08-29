#!/usr/bin/env python3
"""Hostile mutation suite for the C230 evidence contract."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c230_open_toda_evidence.json"
CHECKER = ROOT / "code/c230_open_toda_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c230_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)


def repair(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text()); mutations: list[tuple[str, dict]] = []
    x = deepcopy(pristine); x["regression"]["lax_rows"][0]["b"][0] = "999"; mutations.append(("stale_lax_value", x))
    x = deepcopy(pristine); x["regression"]["lax_rows"][0]["b"][0] = "999"; mutations.append(("repaired_lax_value", repair(x)))
    x = deepcopy(pristine); x["theorem"]["scattering"] = "all trajectories periodic"; mutations.append(("repaired_theorem", repair(x)))
    x = deepcopy(pristine); x["headline"] = "target zeros"; mutations.append(("repaired_headline", repair(x)))
    x = deepcopy(pristine); x["source_commit"] = "0" * 40; mutations.append(("repaired_source", repair(x)))
    x = deepcopy(pristine); x["evaluator"]["sha256"] = "0" * 64; mutations.append(("repaired_evaluator", repair(x)))
    x = deepcopy(pristine); x["scope_literal"] = "BAD"; mutations.append(("repaired_scope_literal", repair(x)))
    x = deepcopy(pristine); x["route_a"]["tuple"][0] = "A0_PASS"; mutations.append(("repaired_route_tuple", repair(x)))
    x = deepcopy(pristine); x["route_a"]["route_b_invocation_allowed"] = True; mutations.append(("repaired_route_b", repair(x)))
    x = deepcopy(pristine); x["scope_flags"]["claims_hilbert_polya_operator"] = True; mutations.append(("repaired_scope_flag", repair(x)))
    x = deepcopy(pristine); x["unknown_top_level"] = 1; mutations.append(("unknown_top", repair(x)))
    x = deepcopy(pristine); x["regression"]["lax_rows"][0]["unknown_nested"] = 1; mutations.append(("unknown_nested", repair(x)))
    x = deepcopy(pristine); x["summary"]["lax_row_count"] = 29; mutations.append(("repaired_count", repair(x)))
    x = deepcopy(pristine); x["regression"]["parameter_rows"][0]["a0"] = ["0"]; mutations.append(("repaired_initial_data", repair(x)))
    x = deepcopy(pristine); x["regression"]["parameter_rows"][0]["eigenvalues_desc"][0] = "0"; mutations.append(("repaired_parameter_spectrum", repair(x)))
    x = deepcopy(pristine); x["regression"]["n2_exact_rows"][0]["a_exact"] = "0"; mutations.append(("repaired_n2_formula", repair(x)))
    x = deepcopy(pristine); x["regression"]["action_angle_rows"][0]["rho_pred"][0] = "0"; mutations.append(("repaired_norming_flow", repair(x)))
    x = deepcopy(pristine); x["regression"]["boundary_rows"][2]["boundary_id"] = "regular_root"; mutations.append(("repaired_boundary", repair(x)))
    x = deepcopy(pristine); x["regression"]["boundary_rows"][0]["statement"] = "all roots repeated"; mutations.append(("repaired_boundary_statement", repair(x)))
    x = deepcopy(pristine); x["citations"][0]["persistent_url"] = "https://example.invalid"; mutations.append(("repaired_citation", repair(x)))
    x = deepcopy(pristine); x["nonclaims"][0] = "claim priority"; mutations.append(("repaired_nonclaim", repair(x)))
    x = deepcopy(pristine); x["regression"]["scattering_rows"][0]["status"] = "exact limit"; mutations.append(("repaired_scope_status", repair(x)))
    rejected = 0; failures: list[str] = []
    for name, mutant in mutations:
        try:
            checker.validate(mutant)
        except Exception:
            rejected += 1
        else:
            failures.append(name)
    if failures:
        raise AssertionError(f"accepted hostile mutations: {failures}")
    print(f"C230 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
