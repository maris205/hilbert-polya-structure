#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C156."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c156_primary_module_evidence.json"
CHECKER = ROOT / "code/c156_primary_module_checker.py"


def payload_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main():
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("date", ("evaluation_date",), "2026-08-24"),
        ("scope", ("scope_literal",), "BAD"),
        ("commit", ("source_commit",), "0" * 40),
        ("source_matrix", ("source_lock", "matrix_A", 0, 0), 3),
        ("upstream", ("source_lock", "upstream_c151_evidence_sha256"), "0" * 64),
        ("cutoff", ("source_lock", "cutoff", "exact_primary_component_enumeration"), 13),
        ("precision", ("source_lock", "precision"), "floating point"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("odd_smith", ("matrix_power_factorization", "odd_smith_type"), "cyclic"),
        ("even_smith", ("matrix_power_factorization", "even_smith_type"), "cyclic"),
        ("all_iterates", ("matrix_power_factorization", "all_iterates"), False),
        ("actual_iterate", ("canonical_cocycle_and_denominator", "actual_iterate"), "q_n=q_B"),
        ("uniform_bound", ("canonical_cocycle_and_denominator", "uniform_bound"), "2D^2 only"),
        ("alln_sharp", ("canonical_cocycle_and_denominator", "sharpness_claimed_all_n"), True),
        ("orthogonal", ("primary_decomposition_theorem", "orthogonal_split"), "not orthogonal"),
        ("polarization", ("primary_decomposition_theorem", "polarization"), "wrong"),
        ("terminology", ("primary_decomposition_theorem", "terminology_boundary"), "Euler factors"),
        ("power", ("iterate_ledger", 10, "A_power", 0, 0), 99),
        ("matrix_M", ("iterate_ledger", 9, "M=A_power-I", 0, 0), 99),
        ("branch", ("iterate_ledger", 8, "factorization_branch"), "WRONG"),
        ("scalar", ("iterate_ledger", 7, "factor_scalar"), 1),
        ("cofactor", ("iterate_ledger", 6, "cofactor_matrix", 0, 0), 1),
        ("cofactor_det", ("iterate_ledger", 5, "cofactor_determinant"), 1),
        ("smith", ("iterate_ledger", 13, "smith_invariants", 1), 1),
        ("order", ("iterate_ledger", 12, "horizontal_group_order"), 1),
        ("exponent", ("iterate_ledger", 11, "horizontal_group_exponent_h"), 1),
        ("hnf", ("iterate_ledger", 10, "column_hnf", 0, 0), 1),
        ("qB", ("iterate_ledger", 9, "canonical_q_B_coefficients", 0), "1/999"),
        ("drift", ("iterate_ledger", 8, "iterate_linear_drift", 0), 0),
        ("prime", ("iterate_ledger", 13, "primary_components", 0, "prime"), 7),
        ("prime_exponent", ("iterate_ledger", 11, "primary_components", 0, "exponent_power"), 1),
        ("projector_order", ("iterate_ledger", 11, "primary_components", 0, "cyclic_projector_order"), 1),
        ("idempotent", ("iterate_ledger", 13, "primary_components", 1, "crt_idempotent_mod_h"), 1),
        ("local_order", ("iterate_ledger", 12, "primary_components", 0, "group_order"), 1),
        ("enumerated", ("iterate_ledger", 10, "primary_components", 0, "enumerated_element_count"), 1),
        ("support", ("iterate_ledger", 9, "primary_components", 0, "rotation_support_size"), 1),
        ("local_lcm", ("iterate_ledger", 8, "primary_components", 0, "observed_denominator_lcm"), 1),
        ("local_zero", ("iterate_ledger", 7, "primary_components", 0, "zero_count"), 2),
        ("projector_numerator", ("iterate_ledger", 6, "primary_components", 0, "root_of_unity_projector_numerator"), 1),
        ("hist_rotation", ("iterate_ledger", 5, "primary_components", 0, "histogram", 0, "rotation"), "1/999"),
        ("hist_mass", ("iterate_ledger", 4, "primary_components", 0, "histogram", 0, "multiplicity"), 999),
        ("orthogonality_receipt", ("iterate_ledger", 13, "orthogonality_pair_checks"), 1),
        ("global_lcm", ("iterate_ledger", 12, "global_denominator_lcm_from_components"), 1),
        ("global_zero", ("iterate_ledger", 11, "fixed_circle_component_count"), 1),
        ("product_flag", ("iterate_ledger", 10, "zero_count_product_verified"), False),
        ("unitary", ("formal_lift_hint", "unitary"), False),
        ("trace_formula", ("formal_lift_hint", "primary_projector_is_operator_trace_formula"), True),
        ("route_tuple", ("route_a", "tuple", 0), "A1_WEAK"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("claim_flag", ("claim_boundary", "arithmetic_local_data"), True),
        ("extra", ("route_a", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c156-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            output = Path(temporary) / f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(output), "--quick"],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        output = Path(temporary) / "stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(output), "--quick"],
                                capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale payload hash")
    print(json.dumps({
        "status": "C156_MUTATION_PASS",
        "repaired_hash_rejected": len(rejected),
        "stale_hash_rejected": 1,
        "total": len(rejected) + 1,
        "names": rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
