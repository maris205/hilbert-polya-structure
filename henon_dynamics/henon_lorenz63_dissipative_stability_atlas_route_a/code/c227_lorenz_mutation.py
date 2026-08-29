#!/usr/bin/env python3
"""Hostile mutation tests for the HCS-C227 evidence schema."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c227_lorenz_evidence.json"
CHECKER = ROOT / "code/c227_lorenz_checker.py"

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c227_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repaired(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    item = deepcopy(pristine); item["regression"]["main_rows"][0]["divergence"] = "-99"; mutations.append(("stale_payload_hash", item))
    item = deepcopy(pristine); item["regression"]["main_rows"][0]["divergence"] = "-99"; mutations.append(("repaired_bad_divergence", repaired(item)))
    item = deepcopy(pristine); item["unknown_top"] = 1; mutations.append(("repaired_unknown_top", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_rows"][0]["unknown_nested"] = 1; mutations.append(("repaired_unknown_row_key", repaired(item)))
    item = deepcopy(pristine); item["theorem"]["unknown_nested"] = "x"; mutations.append(("repaired_unknown_theorem_key", repaired(item)))
    item = deepcopy(pristine); item["source_commit"] = "0" * 40; mutations.append(("repaired_source_commit", repaired(item)))
    item = deepcopy(pristine); item["evaluator"]["sha256"] = "0" * 64; mutations.append(("repaired_evaluator_hash", repaired(item)))
    item = deepcopy(pristine); item["route_a"]["tuple"][4] = "A4_NATURAL_QUANTIZATION"; mutations.append(("repaired_route_tuple", repaired(item)))
    item = deepcopy(pristine); item["scope_flags"]["claims_hilbert_polya_operator"] = True; mutations.append(("repaired_scope_flag", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_rows"][3]["rho"] = "25"; mutations.append(("repaired_hopf_input", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_rows"][3]["rho_h"] = "25"; mutations.append(("repaired_rho_h", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_rows"][5]["wing_characteristic_polynomial"][2] = "999"; mutations.append(("repaired_wing_polynomial", repaired(item)))
    item = deepcopy(pristine); item["regression"]["dissipation_rows"][2]["Vdot_square_ledger"] = "0"; mutations.append(("repaired_square_ledger", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_row_count"] = 9; mutations.append(("repaired_row_count", repaired(item)))
    item = deepcopy(pristine); item["exact_identities"][3]["name"] = "hopf_guess"; mutations.append(("repaired_identity_name", repaired(item)))
    item = deepcopy(pristine); item["citations"][0]["doi"] = "10.invalid/example"; mutations.append(("repaired_citation", repaired(item)))
    item = deepcopy(pristine); item["regression"]["main_rows"].pop(); item["regression"]["main_row_count"] = 9; mutations.append(("repaired_truncated_ledger", repaired(item)))

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
    print(f"C227 hostile mutation rejection: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
