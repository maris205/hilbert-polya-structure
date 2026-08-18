#!/usr/bin/env python3
"""Build the canonical, atomized P46 mutation registry."""

from __future__ import annotations

import json
from pathlib import Path


def physical_receipts(consumers: list[str], code: str) -> dict[str, object]:
    receipts: dict[str, object] = {}
    for consumer in consumers:
        if consumer == "F":
            envelope = {
                "payload": {"code": code},
                "schema": "paper46-frozen-external-rejection-v1",
                "status": "REJECT",
            }
        else:
            envelope = {
                "payload": {"code": code, "consumer": consumer},
                "schema": "paper46-physical-validation-rejection-v1",
                "status": "REJECT",
            }
        receipts[consumer] = {"exit": 2, "stderr_bytes": 0, "stdout": envelope}
    return receipts


def row(identifier: str, family: str, domain: str, target: str,
        before: object, after: object, consumers: list[str], code: str,
        physical_case_id: str | None = None,
        physical_consumers: list[str] | None = None) -> dict[str, object]:
    result: dict[str, object] = {
        "consumers": consumers,
        "domain": domain,
        "expected_code": code,
        "expected_exit": 2,
        "family_id": family,
        "from": before,
        "instance_id": identifier,
        "target": target,
        "to": after,
    }
    if physical_case_id is not None:
        if physical_consumers is None:
            raise ValueError("physical consumers required")
        result["physical_case_id"] = physical_case_id
        result["physical_expected_receipts"] = physical_receipts(physical_consumers, code)
    return result


ROWS = [
    row("F01/support_square", "F01", "science", "packet.support", "m+n=2^a", "m+n=a^2", ["M", "C"], "SOURCE_SUPPORT_CHANGED"),
    row("F02/delete_loop_one", "F02", "science", "packet.loops", "retained", "delete_at_1", ["M", "C"], "LOOP_CONVENTION_CHANGED"),
    row("F03/insert_edge_1_5", "F03", "science", "packet.edges", "dyadic_only", [1, 5], ["M", "C"], "SUPPORT_AND_VALUATION_FAILURE"),
    row("F04/bounded_at_zero", "F04", "infinite_theorem", "bounded_domain", "sigma>0", "sigma>=0", ["C", "P"], "ROW_ONE_NOT_L2"),
    row("F05/s2_at_half", "F05", "infinite_theorem", "S2_domain", "sigma>1/2", "sigma>=1/2", ["C", "P"], "HILBERT_SCHMIDT_ENDPOINT_DIVERGES"),
    row("F06/s1_at_one", "F06", "infinite_theorem", "S1_domain", "sigma>1", "sigma>=1", ["C", "P"], "TRACE_CLASS_ENDPOINT_DIVERGES"),
    row("F07/delete_odd_half", "F07", "science", "cycle.odd_formula", "alternating_sum/2", "alternating_sum", ["M", "C"], "ODD_CYCLE_FORMULA_FAILURE"),
    row("F08/accept_even_nonzero", "F08", "science", "cycle.even_compatibility", "alternating_sum=0", "always_true", ["M", "C"], "EVEN_CYCLE_COMPATIBILITY_FAILURE"),
    row("F09/ordinary_det_s2_strip", "F09", "type", "determinant.ordinary_domain", "sigma>1", "sigma>1/2", ["T"], "ORDINARY_DETERMINANT_OUTSIDE_S1"),
    row("F10/nonreal_hermitian", "F10", "type", "operator.nonreal_type", "complex_symmetric", "Hermitian", ["T"], "OPERATOR_TYPE_FAILURE"),
    row("F11/labels_are_primitives", "F11", "type", "primitive.type", "closed_vertex_cycle", "edge_label_tuple", ["T"], "PRIMITIVE_TYPE_FAILURE"),
    row("F12/cutoff_proves_endpoint", "F12", "infinite_theorem", "endpoint.quantifier", "proof_backed", "finite_SVD", ["P"], "FINITE_CUTOFF_LIMIT_FAILURE"),
    row("F13/swap_marker_weight", "F13", "type", "marker_and_weight", ["z", "2^(-krs)"], ["2^(-krs)", "z"], ["T"], "MARKER_WEIGHT_OWNERSHIP_FAILURE"),
    row("F14/prime_selector_claim", "F14", "route", "a0.rational_prime_support", False, True, ["R1", "R2"], "A0_PRIME_SELECTOR_FAILURE"),
    row("PKT01/missing_candidate", "PACKET", "packet", "source_packet.candidate_id", "SD-C48", None, ["M", "C", "S"], "PACKET_KEYSET_FAILURE"),
    row("PKT02/extra_key", "PACKET", "packet", "source_packet", "exact_keys", "extra", ["M", "C", "S"], "PACKET_KEYSET_FAILURE"),
    row("PKT03/reordered_cutoffs", "PACKET", "packet", "structural_cutoffs", [8, 16, 32, 64], [64, 32, 16, 8], ["M", "C"], "CASE_ORDER_FAILURE"),
    row("PKT04/duplicate_top_key", "PACKET", "packet", "raw_json", "unique", "duplicate candidate_id", ["M", "C", "S"], "DUPLICATE_JSON_KEY"),
    row("PKT05/duplicate_nested_key", "PACKET", "packet", "raw_json.trace_grid", "unique", "duplicate powers", ["M", "C"], "DUPLICATE_JSON_KEY"),
    row("PKT06/bool_for_cutoff", "PACKET", "packet", "structural_cutoffs[0]", 8, True, ["M", "C", "T"], "RECURSIVE_TYPE_FAILURE"),
    row("PKT07/float_for_power", "PACKET", "packet", "trace_grid.powers[1]", 2, "2.0", ["M", "C", "T"], "RECURSIVE_TYPE_FAILURE"),
    row("PKT08/source_seal_drift", "PACKET", "source", "preauthority_manifest_sha256", "fc132...bab", "00...00", ["S", "G", "F"], "FROZEN_SOURCE_DRIFT"),
    row("PKT09/cutoff_63", "PACKET", "packet", "structural_cutoffs[3]", 64, 63, ["M", "C"], "RAW_CASE_CONTRACT_DRIFT"),
    row("RES01/delete_evaluator_m", "RESULT", "result", "outputs/results/evaluator_m.json", "present", "deleted", ["X", "G", "F"], "OUTPUT_NAMESPACE_MISMATCH"),
    row("RES02/rename_evaluator_c", "RESULT", "result", "outputs/results/evaluator_c.json", "present", "evaluator_arithmetic.json", ["X", "G", "F"], "OUTPUT_NAMESPACE_MISMATCH"),
    row("RES03/extra_result", "RESULT", "result", "outputs/results", "exact_set", "extra.json", ["G", "F"], "OUTPUT_NAMESPACE_MISMATCH"),
    row("RES04/bool_int_alias", "RESULT", "result", "cycle_certificate.solution_count", 1, True, ["X", "T", "G"], "RECURSIVE_TYPE_FAILURE"),
    row("RES05/finite_trace_geometric_collapse", "RESULT", "science", "finite_trace_certificate.formula", "scale_dependent_sum", "finite_geometric_factor", ["M", "C", "X", "P"], "FINITE_TRACE_TRUNCATION_FAILURE"),
    row("RES06/infinite_field_in_evaluator", "RESULT", "type", "evaluator.theorem_claims_inferred", [], ["bounded_iff"], ["T", "P", "G"], "FINITE_INFINITE_FIREWALL_FAILURE"),
    row("RES07/coordinated_nested_count_bool", "RESULT", "result", "M_and_C.cycle_certificate.length_records[0].solution_count", 6, True, ["M", "C", "X", "T", "G", "F"], "RESULT_SCHEMA_TYPE_FAILURE", "EXT11_COORDINATED_NESTED_COUNT_INT_TO_BOOL", ["X", "T", "G", "F"]),
    row("RES08/coordinated_nested_cutoff_float", "RESULT", "result", "M_and_C.structural_certificate.records[0].cutoff", 8, "8.0", ["M", "C", "X", "T", "G", "F"], "RESULT_SCHEMA_TYPE_FAILURE", "EXT12_COORDINATED_NESTED_CUTOFF_INT_TO_FLOAT", ["X", "T", "G", "F"]),
    row("RES09/comparison_boolean_to_int", "RESULT", "result", "comparison.strict_recursive_type_and_value_equal", True, 1, ["X", "T", "G", "F"], "RESULT_SCHEMA_TYPE_FAILURE", "EXT13_COMPARISON_BOOLEAN_TO_INT", ["X", "T", "G", "F"]),
    row("RES10/coordinated_missing_nested_key", "RESULT", "result", "M_and_C.cycle_certificate.length_records[0].solution_count", 6, "MISSING", ["X", "T", "G", "F"], "RESULT_SCHEMA_KEYSET_FAILURE"),
    row("RES11/coordinated_extra_nested_key", "RESULT", "result", "M_and_C.cycle_certificate.length_records[0]", "EXACT_KEYS", "unexpected_count=6", ["X", "T", "G", "F"], "RESULT_SCHEMA_KEYSET_FAILURE"),
    row("LED01/edit_digest", "LEDGER", "ledger", "RESULT_LEDGER.rows[0].sha256", "actual", "zero", ["G", "F"], "RESULT_LEDGER_MISMATCH"),
    row("LED02/coordinated_rehash", "LEDGER", "ledger", "result_and_ledger", "sealed", "both_changed", ["G", "F"], "CANONICAL_SCIENCE_MISMATCH"),
    row("LED03/reorder_rows", "LEDGER", "ledger", "RESULT_LEDGER.rows", "C_sorted", "reverse", ["G", "F"], "RESULT_LEDGER_ORDER_FAILURE"),
    row("RPT01/false_claim", "REPORT", "report", "EXPERIMENT_REPORT.md", "finite_does_not_prove", "finite_proves_endpoint", ["G", "F"], "REPORT_RECONSTRUCTION_MISMATCH"),
    row("RPT02/report_only_rehash", "REPORT", "report", "report_and_ledger", "canonical", "edited_and_rehashed", ["G", "F"], "REPORT_RECONSTRUCTION_MISMATCH"),
    row("RTE01/tuple_a0", "ROUTE", "route", "route_tuple[0]", "A0_WEAK_ARITHMETIC_RELATION", "A0_PASS", ["R1", "R2", "G", "F"], "ROUTE_TUPLE_MISMATCH"),
    row("RTE02/overall_accept", "ROUTE", "route", "overall_verdict", "ROUTE_A_REJECTED", "ROUTE_A_ACCEPTED", ["R1", "R2", "G", "F"], "ROUTE_OVERALL_MISMATCH"),
    row("RTE03/route_b_true", "ROUTE", "route", "route_b_invocation_allowed", False, True, ["R1", "R2", "G", "F"], "ROUTE_B_LOCK_FAILURE"),
    row("RTE04/stop_duplicate_terminal", "ROUTE", "route", "terminal_codes", "strict_only", "STOP_DUPLICATE", ["R1", "R2", "S"], "ROUTE_TERMINAL_VOCABULARY_FAILURE"),
    row("RTE05/drop_claim_boundary", "ROUTE", "route", "claim_boundary", "present", None, ["R1", "R2", "G"], "ROUTE_SCHEMA_FAILURE"),
    row("STA01/a_with_manifest", "STATE", "provenance", "state_A.paper_manifest", "absent", "present", ["R1", "R2", "G", "F"], "MIXED_PROVENANCE_STATE"),
    row("STA02/b_missing_manifest", "STATE", "provenance", "state_B.paper_manifest", "present", "absent", ["R1", "R2", "G", "F"], "MIXED_PROVENANCE_STATE"),
    row("STA03/b_unequal_commits", "STATE", "provenance", "state_B.commit_fields", "equal", "unequal", ["R1", "R2", "G", "F"], "PROVENANCE_COMMIT_MISMATCH"),
    row("STA04/b_zero_commit", "STATE", "provenance", "state_B.commit", "nonzero_hex40", "zero_hex40", ["R1", "R2", "G", "F"], "PROVENANCE_COMMIT_INVALID"),
    row("PTH01/traversal", "PATH", "path", "output_root", "contained", "../escape", ["G", "F"], "PATH_CONTAINMENT_FAILURE"),
    row("PTH02/symlink_output", "PATH", "path", "outputs", "directory", "symlink", ["G", "F"], "SYMLINK_FORBIDDEN"),
    row("PTH03/symlink_static", "PATH", "path", "contracts/RAW_CASE_CONTRACT.json", "file", "symlink", ["M", "C", "G", "F"], "SYMLINK_FORBIDDEN"),
    row("PTH04/absolute_serialized", "PATH", "path", "result.payload.path", "relative", "/tmp/leak", ["T", "G", "F"], "HOST_PATH_TOKEN_FORBIDDEN"),
    row("HYG01/cache_file", "HYGIENE", "integrity", "tree", "no_cache", "__pycache__/x.pyc", ["I", "G", "F"], "CACHE_FILE_FORBIDDEN"),
    row("HYG02/project_import_m", "HYGIENE", "independence", "evaluator_m.imports", [], ["code.shared"], ["I", "G"], "EVALUATOR_INDEPENDENCE_FAILURE"),
    row("HYG03/project_import_c", "HYGIENE", "independence", "evaluator_c.imports", [], ["code.shared"], ["I", "G"], "EVALUATOR_INDEPENDENCE_FAILURE"),
    row("SRC01/fournier_credit", "SOURCE", "source", "Fournier-Wagner.novelty_credit", 0, 1, ["S"], "SOURCE_OWNERSHIP_FAILURE"),
    row("SRC02/delete_folding_owner", "SOURCE", "source", "Fournier-Wagner.ownership", "reflection_folding_alternating", "omitted", ["S"], "SOURCE_OWNERSHIP_FAILURE"),
    row("AUD01/delete_proof_audit", "AUDIT", "integrity", "outputs/audits/proof_audit.json", "present", "deleted", ["G", "F"], "OUTPUT_NAMESPACE_MISMATCH"),
    row("AUD02/tamper_integrity", "AUDIT", "integrity", "integrity_audit.status", "PASS", "PASS_WITH_EDIT", ["F"], "AUDIT_SELF_TAMPER"),
    row("TXN01/late_failure_writes", "TRANSACTION", "transaction", "late_failure", "zero_target_change", "partial_install", ["G", "F"], "TRANSACTION_ATOMICITY_FAILURE"),
    row("TXN02/second_run_rewrite", "TRANSACTION", "transaction", "second_run_writes", 0, 1, ["G", "F"], "IDEMPOTENCE_FAILURE"),
    row("TXN03/stage_missing_file", "TRANSACTION", "transaction", "stage_namespace", "complete", "one_missing", ["G", "F"], "STAGE_INCOMPLETE"),
]


CONSUMERS = {
    "C": "code/evaluator_c/evaluate.py",
    "F": "external_auditor/frozen_auditor.py",
    "G": "code/integration/audit_integrity.py",
    "I": "code/auditors/independence_auditor.py",
    "M": "code/evaluator_m/evaluate.py",
    "P": "code/auditors/proof_auditor.py",
    "R1": "code/route/validate_route.py",
    "R2": "code/route/audit_route_independent.py",
    "S": "code/auditors/source_auditor.py",
    "T": "code/auditors/type_auditor.py",
    "X": "code/comparator/exact_compare.py",
}


PHYSICAL_CASE_SPECS = [
    ("EXT01_STATIC_BYTE_DRIFT", ["F"], "STATIC_INPUT_DRIFT", None),
    ("EXT02_OUTPUT_DELETE", ["F"], "OUTPUT_NAMESPACE_MISMATCH", "RES01/delete_evaluator_m"),
    ("EXT03_OUTPUT_EXTRA", ["F"], "OUTPUT_NAMESPACE_MISMATCH", "RES03/extra_result"),
    ("EXT04_OUTPUT_SYMLINK", ["F"], "SYMLINK_OR_CACHE_FORBIDDEN", "PTH02/symlink_output"),
    ("EXT05_CACHE_INJECTION", ["F"], "SYMLINK_OR_CACHE_FORBIDDEN", "HYG01/cache_file"),
    ("EXT06_RESULT_LEDGER_COORDINATED_EDIT", ["F"], "CANONICAL_SCIENCE_MISMATCH", "LED02/coordinated_rehash"),
    ("EXT07_REPORT_LEDGER_COORDINATED_EDIT", ["F"], "REPORT_RECONSTRUCTION_MISMATCH", "RPT02/report_only_rehash"),
    ("EXT08_ROUTE_EDIT", ["F"], "ROUTE_RECORD_MISMATCH", "RTE02/overall_accept"),
    ("EXT09_INTEGRITY_SELF_TAMPER", ["F"], "AUDIT_SELF_TAMPER", "AUD02/tamper_integrity"),
    ("EXT10_SOURCE_PACKET_LEDGER_COORDINATED_EDIT", ["F"], "FROZEN_SOURCE_DRIFT", "PKT08/source_seal_drift"),
    ("EXT11_COORDINATED_NESTED_COUNT_INT_TO_BOOL", ["X", "T", "G", "F"],
     "RESULT_SCHEMA_TYPE_FAILURE", "RES07/coordinated_nested_count_bool"),
    ("EXT12_COORDINATED_NESTED_CUTOFF_INT_TO_FLOAT", ["X", "T", "G", "F"],
     "RESULT_SCHEMA_TYPE_FAILURE", "RES08/coordinated_nested_cutoff_float"),
    ("EXT13_COMPARISON_BOOLEAN_TO_INT", ["X", "T", "G", "F"],
     "RESULT_SCHEMA_TYPE_FAILURE", "RES09/comparison_boolean_to_int"),
]


def main() -> None:
    families = sorted({entry["family_id"] for entry in ROWS})
    physical_cases = [
        {
            "case_id": case_id,
            "consumers": consumers,
            "expected_receipts": physical_receipts(consumers, code),
            "mutation_instance_id": mutation_id,
        }
        for case_id, consumers, code, mutation_id in PHYSICAL_CASE_SPECS
    ]
    value = {
        "consumer_contract": CONSUMERS,
        "expected_family_count": len(families),
        "expected_instance_count": len(ROWS),
        "instances": ROWS,
        "outcome_union": ["ACCEPT", "HARNESS_ERROR", "REJECT"],
        "physical_cases": physical_cases,
        "schema": "paper46-mutation-registry-v1",
        "survivor_semantics": "ANY_MISSING_EXTRA_ZERO_EXIT_WRONG_CODE_NONCANONICAL_EXCEPTION_OR_UNLISTED_CONSUMER_SURVIVES",
    }
    raw = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                      separators=(",", ": ")) + "\n").encode("ascii")
    Path(__file__).with_name("MUTATION_REGISTRY.json").write_bytes(raw)


if __name__ == "__main__":
    main()
