#!/usr/bin/env python3
"""Hostile mutation suite for HCS-C228."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c228_coagulation_evidence.json"
CHECKER = ROOT / "code/c228_coagulation_checker.py"
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("c228_checker", CHECKER)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def repaired(data: dict) -> dict:
    data["payload_sha256"] = checker.payload_hash(data)
    return data


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    cases: list[tuple[str, dict]] = []
    x = deepcopy(original); x["coefficient_ledger"]["rows"][4]["a_k"] = "1"; cases.append(("stale_hash", x))
    x = deepcopy(original); x["coefficient_ledger"]["rows"][4]["a_k"] = "1"; cases.append(("repaired_coefficient", repaired(x)))
    x = deepcopy(original); x["unknown_top"] = 1; cases.append(("unknown_top", repaired(x)))
    x = deepcopy(original); x["coefficient_ledger"]["rows"][0]["unknown_nested"] = 1; cases.append(("unknown_nested", repaired(x)))
    x = deepcopy(original); x["theorem"]["unknown_nested"] = "x"; cases.append(("unknown_theorem", repaired(x)))
    x = deepcopy(original); x["source_commit"] = "0" * 40; cases.append(("source_commit", repaired(x)))
    x = deepcopy(original); x["evaluator"]["sha256"] = "0" * 64; cases.append(("evaluator_hash", repaired(x)))
    x = deepcopy(original); x["headline"] = "target zeros from an Euler product"; cases.append(("headline_claim", repaired(x)))
    x = deepcopy(original); x["frozen_object"]["forbidden_data"] = "none"; cases.append(("forbidden_data", repaired(x)))
    x = deepcopy(original); x["theorem"]["pregel_moments"] = "M2 stays finite"; cases.append(("theorem_text", repaired(x)))
    x = deepcopy(original); x["route_a"]["tuple"][4] = "A4_NATURAL_QUANTIZATION"; cases.append(("route_inflation", repaired(x)))
    x = deepcopy(original); x["route_a"]["strongest_positive"] = "target determinant proved"; cases.append(("route_text", repaired(x)))
    x = deepcopy(original); x["scope_flags"]["claims_euler_factors"] = True; cases.append(("scope_inflation", repaired(x)))
    x = deepcopy(original); x["coefficient_ledger"]["rows"][9]["recurrence_rhs"] = "0"; cases.append(("Cayley_recurrence", repaired(x)))
    x = deepcopy(original); x["regression"]["pregel_and_critical_rows"][2]["second_moment_M2"] = "3"; cases.append(("pregel_moment", repaired(x)))
    x = deepcopy(original); x["regression"]["pregel_and_critical_rows"][4]["regime"] = "pregel"; cases.append(("critical_label", repaired(x)))
    x = deepcopy(original); x["regression"]["smoluchowski_postgel_rows"][1]["sol_mass_M1"] = "0.4"; cases.append(("Stockmayer_mass", repaired(x)))
    x = deepcopy(original); x["regression"]["smoluchowski_postgel_rows"][0]["coefficients_k1_to_20"][3] = "0"; cases.append(("Stockmayer_coefficient", repaired(x)))
    x = deepcopy(original); x["regression"]["flory_postgel_rows"][1]["sol_mass_q"] = "0.5"; cases.append(("Flory_root", repaired(x)))
    x = deepcopy(original); x["regression"]["flory_postgel_rows"][2]["loss_mass_used"] = "0.2"; cases.append(("Flory_loss", repaired(x)))
    x = deepcopy(original); x["regression"]["flory_postgel_rows"][0]["branch"] = "Smoluchowski_Stockmayer"; cases.append(("branch_swap", repaired(x)))
    x = deepcopy(original); x["regression"]["critical_tail_rows"][4]["scaled_tail_ratio"] = "1.2"; cases.append(("critical_tail", repaired(x)))
    x = deepcopy(original); x["exact_identities"][7]["name"] = "branches_equal"; cases.append(("identity_mutation", repaired(x)))
    x = deepcopy(original); x["exact_identities"][0]["formula"] = "(k-1)a_k=0"; cases.append(("identity_formula", repaired(x)))
    x = deepcopy(original); x["citations"][3]["doi"] = "10.invalid/example"; cases.append(("citation", repaired(x)))
    x = deepcopy(original); x["citations"][3]["role"] = "proves target automorphy"; cases.append(("citation_role", repaired(x)))
    x = deepcopy(original); x["nonclaims"][0] = "All results are new."; cases.append(("nonclaim_text", repaired(x)))
    x = deepcopy(original); x["coefficient_ledger"]["rows"].pop(); x["coefficient_ledger"]["row_count"] = 39; cases.append(("truncated_ledger", repaired(x)))

    rejected = 0
    accepted: list[str] = []
    for name, mutant in cases:
        try:
            checker.validate(mutant)
        except Exception:
            rejected += 1
        else:
            accepted.append(name)
    if accepted:
        raise AssertionError(f"accepted hostile mutations: {accepted}")
    print(f"C228 hostile mutation rejection: PASS {rejected}/{len(cases)}")


if __name__ == "__main__":
    main()
