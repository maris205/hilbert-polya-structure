#!/usr/bin/env python3
"""Hostile semantic and repaired-hash mutation suite for C248."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c248_rs_evidence.json"
CHECKER = ROOT / "code/c248_rs_checker.py"


def repair(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, change, repaired: bool = False) -> None:
        item = deepcopy(pristine)
        change(item)
        mutations.append((name, repair(item) if repaired else item))

    # Provenance/schema and frozen mathematical object.
    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-31"))
    add("source_commit", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("frozen_rule_repaired", lambda x: x["frozen_object"]["substitution"].__setitem__("a", "aa"), True)
    add("frozen_coding_repaired", lambda x: x["frozen_object"]["factor_coding"].__setitem__("a", -1), True)
    add("frozen_seed_repaired", lambda x: x["frozen_object"].__setitem__("seed", "b"), True)
    add("frozen_convention", lambda x: x["frozen_object"].__setitem__("sequence_convention", "periodic finite word"))
    # Substitution and frequency receipts.
    add("matrix_cell_repaired", lambda x: x["regression"]["substitution_matrix"][0].__setitem__(0, 9), True)
    add("matrix_power_repaired", lambda x: x["regression"]["matrix_power_3"][0].__setitem__(0, 9), True)
    add("primitive_power_repaired", lambda x: x["regression"].__setitem__("primitive_witness_power", 2), True)
    add("frequency_vector_repaired", lambda x: x["regression"]["frequency_vector"].__setitem__(0, "1/3"), True)
    add("frequency_row_repaired", lambda x: x["regression"]["frequency_rows"][4]["letter_counts"].__setitem__(0, 99), True)
    add("prefix_letter_repaired", lambda x: x["regression"].__setitem__("fixed_point_prefix_letters", "b" + x["regression"]["fixed_point_prefix_letters"][1:]), True)
    add("prefix_sign_repaired", lambda x: x["regression"]["fixed_point_prefix_signs"].__setitem__(0, -1), True)
    # Dyadic cocycle and exact energy.
    add("dyadic_p_repaired", lambda x: x["regression"]["dyadic_rows"][5]["P_coefficients"].__setitem__(3, 7), True)
    add("dyadic_q_repaired", lambda x: x["regression"]["dyadic_rows"][6]["Q_coefficients"].__setitem__(2, 7), True)
    add("dyadic_energy_repaired", lambda x: x["regression"]["dyadic_rows"][3].__setitem__("energy_sum", 1), True)
    add("dyadic_bound_repaired", lambda x: x["regression"]["dyadic_rows"][4].__setitem__("unit_circle_bound_squared", 1), True)
    add("theorem_energy", lambda x: x["theorem"].__setitem__("energy_identity", "energy is arbitrary"))
    add("identity_formula", lambda x: x["exact_identities"][1].__setitem__("formula", "wrong recursion"))
    # Laurent correlation cocycle and aperiodicity receipts.
    add("corr_R_repaired", lambda x: x["regression"]["correlation_rows"][2]["R"][3].__setitem__(1, 77), True)
    add("corr_T_repaired", lambda x: x["regression"]["correlation_rows"][3]["T"][4].__setitem__(1, -88), True)
    add("corr_selected_repaired", lambda x: x["regression"]["correlation_rows"][4]["selected_R_lags_0_to_8"].__setitem__(1, 44), True)
    add("corr_max_repaired", lambda x: x["regression"]["correlation_rows"][5].__setitem__("max_abs_R_off_zero", 0), True)
    add("aperiodicity_repaired", lambda x: x["regression"]["aperiodicity_rows"][7].__setitem__("first_mismatch_index", 0), True)
    add("aperiodicity_left_repaired", lambda x: x["regression"]["aperiodicity_rows"][8].__setitem__("left", "x"), True)
    add("grid_repaired", lambda x: x["regression"]["parameter_grid"][2].__setitem__("N", 99), True)
    add("row_count_repaired", lambda x: x["regression"]["row_counts"].__setitem__("correlation", 7), True)
    # Route, scope, citations, and structural attacks.
    add("route_tuple_repaired", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"), True)
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b_repaired", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True), True)
    add("scope_flag_repaired", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True), True)
    add("citation_doi_repaired", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"), True)
    add("citation_url", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("erratum_role_repaired", lambda x: x["citations"][2].__setitem__("role", "uncorrected source"), True)
    add("nonclaim_repaired", lambda x: x["nonclaims"].__setitem__(0, "we claim a target divisor"), True)
    add("unknown_key", lambda x: x["theorem"].__setitem__("unexpected", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64))
    add("dyadic_order_repaired", lambda x: x["regression"]["dyadic_rows"].reverse(), True)
    add("missing_corr", lambda x: x["regression"]["correlation_rows"].pop())

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c248-rs-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations) - set(caught)}"
    print(f"C248 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
