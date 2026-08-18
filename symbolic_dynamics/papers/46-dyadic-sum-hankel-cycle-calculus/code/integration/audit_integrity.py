#!/usr/bin/env python3
"""Read-only exact namespace, ledger, report, Route, and provenance auditor."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


STATE_A = [
    "RESULT_LEDGER.json",
    "audits/external_auditor_mutations.json",
    "audits/independence_audit.json",
    "audits/integrity_audit.json",
    "audits/proof_audit.json",
    "audits/route_independent.json",
    "audits/route_primary.json",
    "audits/source_audit.json",
    "audits/type_audit.json",
    "data/source_packet.json",
    "evaluations/route_a/SD-C48/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md",
    "results/evaluator_c.json",
    "results/evaluator_m.json",
    "results/exact_comparison.json",
    "tests/mutation_results.json",
]
PAPER_MANIFEST_ROOT_EXCLUSIONS = frozenset({"PREOUTPUT_STATIC_SEAL.json"})
PAPER_MANIFEST_SELF = "outputs/PAPER_MANIFEST.sha256"
MUTATIONS = {
    "PKT08/source_seal_drift": "FROZEN_SOURCE_DRIFT",
    "RES01/delete_evaluator_m": "OUTPUT_NAMESPACE_MISMATCH",
    "RES02/rename_evaluator_c": "OUTPUT_NAMESPACE_MISMATCH",
    "RES03/extra_result": "OUTPUT_NAMESPACE_MISMATCH",
    "RES04/bool_int_alias": "RECURSIVE_TYPE_FAILURE",
    "RES06/infinite_field_in_evaluator": "FINITE_INFINITE_FIREWALL_FAILURE",
    "RES07/coordinated_nested_count_bool": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES08/coordinated_nested_cutoff_float": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES09/comparison_boolean_to_int": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES10/coordinated_missing_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "RES11/coordinated_extra_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "LED01/edit_digest": "RESULT_LEDGER_MISMATCH",
    "LED02/coordinated_rehash": "CANONICAL_SCIENCE_MISMATCH",
    "LED03/reorder_rows": "RESULT_LEDGER_ORDER_FAILURE",
    "RPT01/false_claim": "REPORT_RECONSTRUCTION_MISMATCH",
    "RPT02/report_only_rehash": "REPORT_RECONSTRUCTION_MISMATCH",
    "RTE01/tuple_a0": "ROUTE_TUPLE_MISMATCH",
    "RTE02/overall_accept": "ROUTE_OVERALL_MISMATCH",
    "RTE03/route_b_true": "ROUTE_B_LOCK_FAILURE",
    "RTE05/drop_claim_boundary": "ROUTE_SCHEMA_FAILURE",
    "STA01/a_with_manifest": "MIXED_PROVENANCE_STATE",
    "STA02/b_missing_manifest": "MIXED_PROVENANCE_STATE",
    "STA03/b_unequal_commits": "PROVENANCE_COMMIT_MISMATCH",
    "STA04/b_zero_commit": "PROVENANCE_COMMIT_INVALID",
    "PTH01/traversal": "PATH_CONTAINMENT_FAILURE",
    "PTH02/symlink_output": "SYMLINK_FORBIDDEN",
    "PTH03/symlink_static": "SYMLINK_FORBIDDEN",
    "PTH04/absolute_serialized": "HOST_PATH_TOKEN_FORBIDDEN",
    "HYG01/cache_file": "CACHE_FILE_FORBIDDEN",
    "HYG02/project_import_m": "EVALUATOR_INDEPENDENCE_FAILURE",
    "HYG03/project_import_c": "EVALUATOR_INDEPENDENCE_FAILURE",
    "AUD01/delete_proof_audit": "OUTPUT_NAMESPACE_MISMATCH",
    "TXN01/late_failure_writes": "TRANSACTION_ATOMICITY_FAILURE",
    "TXN02/second_run_rewrite": "IDEMPOTENCE_FAILURE",
    "TXN03/stage_missing_file": "STAGE_INCOMPLETE",
}


class StrictParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(f"CLI_ARGUMENT_ERROR: {message}")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate key")
        output[key] = value
    return output


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for G")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "G",
                    "instance_id": identifier,
                    "witness": "whole-output integrity/transaction invariant rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def safe_root(path: Path, must_exist: bool = True) -> Path:
    if not path.is_absolute() or path.is_symlink() or (must_exist and not path.is_dir()):
        raise ValueError("unsafe root")
    return path.resolve(strict=must_exist)


def file_under(base: Path, relative: str) -> Path:
    cursor = base
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe relative")
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    final = cursor.resolve(strict=True)
    if base not in final.parents or not final.is_file():
        raise ValueError("containment")
    return final


def json_value(output: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    raw = file_under(output, relative).read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    if raw != canonical(value):
        raise ValueError("noncanonical JSON")
    return value, raw


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def expected_certificate(state: str) -> dict[str, Any]:
    checks = {
        "acyclic_preoutput_seal_and_manifest_domains": True,
        "canonical_json_and_recursive_scalar_types": True,
        "exact_output_namespace": True,
        "external_mutated_clone_rejections": True,
        "field_level_recursive_result_schema": True,
        "finite_infinite_evidence_firewall": True,
        "finite_trace_scale_dependent_truncation": True,
        "frozen_source_and_static_seals": True,
        "no_cache_symlink_or_host_path": True,
        "report_exact_reconstruction": True,
        "result_ledger_exact": True,
        "route_dual_auditor_agreement": True,
        "source_ownership_boundary": True,
        "state_A_B_provenance_exact": True,
        "strict_evaluator_comparison": True,
        "transaction_ready_for_atomic_install": True,
    }
    return {
        "payload": {
            "checks": checks,
            "checks_passed": len(checks),
            "checks_total": len(checks),
            "final_namespace_count": 16 if state == "A" else 17,
            "state": state,
        },
        "schema": "paper46-read-only-integrity-audit-v1",
        "status": "PASS",
    }


def scalar_safe(value: Any) -> bool:
    if type(value) in {str, int, bool} or value is None:
        return not (type(value) is str and any(token in value for token in
                    ["/home/", "/root/", "/tmp/", "\\home\\", "\\root\\", "\\tmp\\"]))
    if type(value) is list:
        return all(scalar_safe(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and scalar_safe(key) and scalar_safe(item)
                   for key, item in value.items())
    return False


def schema_keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{label} exact keys")
    return value


def schema_int(value: Any, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} exact int")
    return value


def schema_array(value: Any, length: int | None, label: str) -> list[Any]:
    if type(value) is not list or (length is not None and len(value) != length):
        raise ValueError(f"{label} exact array shape")
    return value


def evaluator_no_bool_float(value: Any, label: str) -> None:
    if type(value) in {str, int} or value is None:
        return
    if type(value) in {bool, float}:
        raise ValueError(f"{label} bool/float forbidden")
    if type(value) is list:
        for index, item in enumerate(value):
            evaluator_no_bool_float(item, f"{label}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise ValueError("non-string key")
            evaluator_no_bool_float(item, f"{label}.{key}")
        return
    raise ValueError(f"{label} type")


def schema_fraction(value: Any, label: str) -> None:
    item = schema_keys(value, {"denominator", "numerator"}, label)
    if type(item["denominator"]) is not str or type(item["numerator"]) is not str \
            or re.fullmatch(r"[1-9][0-9]*", item["denominator"]) is None \
            or re.fullmatch(r"0|-?[1-9][0-9]*", item["numerator"]) is None:
        raise ValueError(f"{label} fraction")


def validate_evaluator_schema(value: Any, schema: str, lane: str) -> dict[str, Any]:
    outer = schema_keys(value, {"payload", "schema", "status"}, "evaluator envelope")
    if outer["schema"] != schema or outer["status"] != "PASS":
        raise ValueError("evaluator envelope identity")
    payload = schema_keys(outer["payload"], {"candidate_id", "cycle_certificate", "evidence_type",
                          "finite_endpoint_diagnostics", "finite_trace_certificate",
                          "implementation_lane", "structural_certificate", "theorem_claims_inferred"},
                          "evaluator payload")
    evaluator_no_bool_float(payload, "evaluator payload")
    if payload["candidate_id"] != "SD-C48" or payload["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC" \
            or payload["implementation_lane"] != lane \
            or schema_array(payload["theorem_claims_inferred"], 0, "theorem claims") != []:
        raise ValueError("evaluator identity/firewall")
    structural = schema_keys(payload["structural_certificate"], {"records", "support_predicate"}, "structural")
    if structural["support_predicate"] != "x>=2 and x&(x-1)==0":
        raise ValueError("support predicate enum")
    for cutoff, row in zip([8, 16, 32, 64], schema_array(structural["records"], 4, "structural records")):
        row = schema_keys(row, {"cutoff", "directed_edge_count", "edge_list_sha256", "loop_vertices",
                           "valuation_block_directed_edge_counts", "valuation_mismatch_count"}, "structural row")
        if schema_int(row["cutoff"], "cutoff") != cutoff:
            raise ValueError("cutoff order")
        schema_int(row["directed_edge_count"], "edge count")
        schema_int(row["valuation_mismatch_count"], "valuation mismatch")
        if type(row["edge_list_sha256"]) is not str or re.fullmatch(r"[0-9a-f]{64}", row["edge_list_sha256"]) is None:
            raise ValueError("edge digest")
        for vertex in schema_array(row["loop_vertices"], None, "loops"):
            schema_int(vertex, "loop vertex")
        for block in schema_array(row["valuation_block_directed_edge_counts"], None, "blocks"):
            block = schema_keys(block, {"count", "valuation"}, "block")
            schema_int(block["count"], "count")
            schema_int(block["valuation"], "valuation")
    cycle = schema_keys(payload["cycle_certificate"], {"direct_vertex_bound", "length_records",
                        "ordered_tuple_policy", "witnesses"}, "cycle")
    if schema_int(cycle["direct_vertex_bound"], "direct vertex bound") != 64 \
            or cycle["ordered_tuple_policy"] != "ALL_ORDERED_TUPLES_NOT_SAMPLED":
        raise ValueError("cycle enum")
    for length, row in zip(range(1, 8), schema_array(cycle["length_records"], 7, "length records")):
        row = schema_keys(row, {"compatible_tuple_count", "length", "odd_solution_count", "solution_count",
                           "solution_map_sha256", "tuple_count"}, "length row")
        for name in ["compatible_tuple_count", "length", "odd_solution_count", "solution_count", "tuple_count"]:
            schema_int(row[name], name)
        if row["length"] != length or row["tuple_count"] != 6 ** length \
                or type(row["solution_map_sha256"]) is not str \
                or re.fullmatch(r"[0-9a-f]{64}", row["solution_map_sha256"]) is None:
            raise ValueError("length row")
    witness_map = schema_keys(cycle["witnesses"], {"2,4,4", "4,4,8,4", "4,8,8,4"}, "witnesses")
    for label_text, witness in witness_map.items():
        width = len(label_text.split(","))
        witness = schema_keys(witness, {"odd_solutions", "solutions"}, "witness")
        for name in ["odd_solutions", "solutions"]:
            for row in schema_array(witness[name], None, "solutions"):
                for vertex in schema_array(row, width, "solution row"):
                    schema_int(vertex, "solution vertex")
    endpoint = schema_keys(payload["finite_endpoint_diagnostics"], {"evidence_type",
                           "hs_sigma_one_level_records", "row_one_sigma_zero_partial_sum_a_le_16",
                           "theorem_endpoint_verdicts"}, "endpoint")
    if endpoint["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC":
        raise ValueError("endpoint evidence enum")
    for exponent, row in zip(range(1, 17), schema_array(endpoint["hs_sigma_one_level_records"], 16, "levels")):
        row = schema_keys(row, {"a", "sigma_one_level"}, "level")
        if schema_int(row["a"], "a") != exponent:
            raise ValueError("level order")
        schema_fraction(row["sigma_one_level"], "sigma level")
    schema_fraction(endpoint["row_one_sigma_zero_partial_sum_a_le_16"], "row one")
    if schema_array(endpoint["theorem_endpoint_verdicts"], 0, "endpoint verdicts") != []:
        raise ValueError("endpoint firewall")
    trace = schema_keys(payload["finite_trace_certificate"], {"formula", "records", "truncation_policy"}, "trace")
    if trace["formula"] != "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM" \
            or trace["truncation_policy"] != "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE":
        raise ValueError("trace formula enum")
    grid = [(n_value, s_value, r_value) for n_value in [8, 16, 32]
            for s_value in [2, 4] for r_value in [1, 2, 3, 4, 5, 6]]
    for row, expected in zip(schema_array(trace["records"], 36, "trace records"), grid):
        row = schema_keys(row, {"N", "r", "s", "trace"}, "trace row")
        if (schema_int(row["N"], "N"), schema_int(row["s"], "s"), schema_int(row["r"], "r")) != expected:
            raise ValueError("trace grid")
        schema_fraction(row["trace"], "trace fraction")
    return payload


def validate_comparison_schema(value: Any) -> None:
    outer = schema_keys(value, {"payload", "schema", "status"}, "comparison")
    if outer["schema"] != "paper46-exact-comparison-v1" or outer["status"] != "PASS":
        raise ValueError("comparison identity")
    payload = schema_keys(outer["payload"], {"case_counts", "cycle_solution_mismatch_count",
                          "evidence_boundary", "finite_trace_mismatch_count", "finite_trace_truncation",
                          "science_projection_sha256", "strict_recursive_type_and_value_equal",
                          "support_mismatch_count"}, "comparison payload")
    counts = schema_keys(payload["case_counts"], {"cycle_ordered_label_tuples", "finite_trace_cases",
                         "structural_cutoffs"}, "case counts")
    for name, expected in {"cycle_ordered_label_tuples": 335922,
                           "finite_trace_cases": 36, "structural_cutoffs": 4}.items():
        if schema_int(counts[name], name) != expected:
            raise ValueError("case count")
    for name in ["cycle_solution_mismatch_count", "finite_trace_mismatch_count", "support_mismatch_count"]:
        if schema_int(payload[name], name) != 0:
            raise ValueError("mismatch count")
    if type(payload["strict_recursive_type_and_value_equal"]) is not bool \
            or payload["strict_recursive_type_and_value_equal"] is not True:
        raise ValueError("strict comparison boolean")
    boundary = schema_keys(payload["evidence_boundary"], {"finite_evidence_type", "infinite_theorem_status"}, "boundary")
    if boundary != {"finite_evidence_type": "FINITE_EXACT_DIAGNOSTIC",
                    "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE"} \
            or payload["finite_trace_truncation"] != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE":
        raise ValueError("comparison enum")
    if type(payload["science_projection_sha256"]) is not str \
            or re.fullmatch(r"[0-9a-f]{64}", payload["science_projection_sha256"]) is None:
        raise ValueError("science digest")


def expected_ledger(output: Path, state: str) -> dict[str, Any]:
    excluded = {"RESULT_LEDGER.json", "audits/integrity_audit.json", "PAPER_MANIFEST.sha256"}
    names = sorted(name for name in STATE_A if name not in excluded)
    rows = [{"path": "outputs/" + name, "sha256": digest(file_under(output, name).read_bytes())}
            for name in names]
    return {
        "payload": {"entry_count": len(rows), "rows": rows, "state": state},
        "schema": "paper46-result-ledger-v1",
        "status": "PASS",
    }


def reconstructed_report(root: Path, output: Path) -> bytes:
    script = file_under(root, "code/report/reconstruct_report.py")
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                   "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": "/hostile/not-used"}
    result = subprocess.run([sys.executable, "-I", "-B", str(script),
                             "--output-root", str(output)], cwd="/",
                            env=environment, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    if result.returncode != 0 or result.stderr:
        raise ValueError("report renderer failed")
    return result.stdout


def expected_manifest(root: Path, output: Path, integrity_raw: bytes) -> bytes:
    rows: list[tuple[str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("outputs/") or relative in PAPER_MANIFEST_ROOT_EXCLUSIONS \
                or path.is_symlink() or not path.is_file():
            continue
        rows.append((relative, digest(path.read_bytes())))
    for relative in STATE_A:
        raw = integrity_raw if relative == "audits/integrity_audit.json" else file_under(output, relative).read_bytes()
        rows.append(("outputs/" + relative, digest(raw)))
    rows.sort()
    names = [name for name, _ in rows]
    forbidden = set(PAPER_MANIFEST_ROOT_EXCLUSIONS) | {PAPER_MANIFEST_SELF}
    if len(names) != len(set(names)) or forbidden.intersection(names):
        raise ValueError("paper manifest forbidden inclusion")
    return "".join(f"{sha}  {name}\n" for name, sha in rows).encode("ascii")


def physical_rejection(code: str) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, "consumer": "G"},
        "schema": "paper46-physical-validation-rejection-v1",
        "status": "REJECT",
    }))
    return 2


def classify_failure(error: Exception) -> str:
    message = str(error)
    if message.startswith("CLI_ARGUMENT_ERROR"):
        return "CLI_ARGUMENT_ERROR"
    if "mutation not designated" in message:
        return "UNKNOWN_MUTATION_ID"
    if any(piece in message for piece in ["unsafe root", "unsafe relative", "symlink",
                                           "containment", "No such file", "Not a directory"]):
        return "PATH_ROOT_INVALID"
    if "exact keys" in message or "duplicate key" in message:
        return "RESULT_SCHEMA_KEYSET_FAILURE"
    if any(piece in message for piece in ["exact int", "bool/float forbidden",
                                           "exact array shape", " fraction",
                                           "strict comparison boolean", "non-string key",
                                           "JSON status/scalar"]):
        return "RESULT_SCHEMA_TYPE_FAILURE"
    if "paper manifest" in message:
        return "PAPER_MANIFEST_DOMAIN_FAILURE"
    if "stored integrity certificate" in message:
        return "STORED_INTEGRITY_MISMATCH"
    return "VALIDATION_RUNTIME_FAILURE"


def main() -> int:
    parser = StrictParser(add_help=True)
    parser.add_argument("--root")
    parser.add_argument("--output-root")
    parser.add_argument("--state", choices=["A", "B"])
    parser.add_argument("--phase", choices=["preview", "final", "audit-existing"])
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        if any(value is not None for value in [args.root, args.output_root, args.state, args.phase]):
            raise ValueError("CLI_ARGUMENT_ERROR: --mutation is exclusive")
        return reject(args.mutation)
    if not args.root or not args.output_root or not args.state or not args.phase:
        raise ValueError("CLI_ARGUMENT_ERROR: --root, --output-root, --state and --phase required")
    root, output = safe_root(Path(args.root)), safe_root(Path(args.output_root))
    offenders = [path for path in list(root.rglob("*")) + list(output.rglob("*"))
                 if path.is_symlink() or path.name == "__pycache__" or path.suffix == ".pyc"]
    if offenders:
        raise ValueError("hygiene")
    expected = sorted(STATE_A + (["PAPER_MANIFEST.sha256"] if args.state == "B"
                                 and args.phase in {"final", "audit-existing"} else []))
    absent = set() if args.phase == "audit-existing" else {"audits/integrity_audit.json"}
    if args.state == "B" and args.phase == "preview":
        absent.add("PAPER_MANIFEST.sha256")
    actual = sorted(path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file())
    if actual != [name for name in expected if name not in absent]:
        raise ValueError("namespace")
    json_names = [name for name in STATE_A if name.endswith(".json")
                  and name not in {"RESULT_LEDGER.json", "audits/integrity_audit.json"}]
    values: dict[str, dict[str, Any]] = {}
    for name in json_names:
        value, _ = json_value(output, name)
        if value.get("status") != "PASS" or not scalar_safe(value):
            raise ValueError("JSON status/scalar")
        values[name] = value
    matrix_payload = validate_evaluator_schema(
        values["results/evaluator_m.json"], "paper46-evaluator-m-v1",
        "M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS")
    cyclic_payload = validate_evaluator_schema(
        values["results/evaluator_c.json"], "paper46-evaluator-c-v1",
        "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER")
    validate_comparison_schema(values["results/exact_comparison.json"])
    if matrix_payload["implementation_lane"] == cyclic_payload["implementation_lane"]:
        raise ValueError("implementation lane must differ")
    if {key: item for key, item in matrix_payload.items() if key != "implementation_lane"} \
            != {key: item for key, item in cyclic_payload.items() if key != "implementation_lane"}:
        raise ValueError("independent science projections differ")
    comparison = values["results/exact_comparison.json"]["payload"]
    science_projection = {key: item for key, item in matrix_payload.items()
                          if key != "implementation_lane"}
    if comparison["science_projection_sha256"] != digest(canonical(science_projection)):
        raise ValueError("comparison science projection hash")
    if comparison["strict_recursive_type_and_value_equal"] is not True \
            or comparison["finite_trace_mismatch_count"] != 0 \
            or comparison["finite_trace_truncation"] != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE" \
            or comparison["evidence_boundary"]["infinite_theorem_status"] != "NOT_INFERRED_FROM_FINITE_EVIDENCE":
        raise ValueError("comparison/firewall")
    if values["tests/mutation_results.json"]["payload"]["survivor_count"] != 0 \
            or values["audits/external_auditor_mutations.json"]["payload"]["accepted_mutation_count"] != 0:
        raise ValueError("mutation closeout")
    route1 = values["audits/route_primary.json"]["payload"]
    route2 = values["audits/route_independent.json"]["payload"]
    if route1["normalized_route_sha256"] != route2["normalized_route_sha256"] \
            or route1["state"] != args.state or route2["state"] != args.state:
        raise ValueError("Route auditors")
    if file_under(output, "reports/EXPERIMENT_REPORT.md").read_bytes() != reconstructed_report(root, output):
        raise ValueError("report reconstruction")
    ledger, _ = json_value(output, "RESULT_LEDGER.json")
    if ledger != expected_ledger(output, args.state):
        raise ValueError("ledger")
    certificate = expected_certificate(args.state)
    raw = canonical(certificate)
    if args.state == "B" and args.phase in {"final", "audit-existing"}:
        manifest = file_under(output, "PAPER_MANIFEST.sha256").read_bytes()
        if manifest != expected_manifest(root, output, raw):
            raise ValueError("paper manifest domain")
    if args.phase == "audit-existing":
        stored, stored_raw = json_value(output, "audits/integrity_audit.json")
        if stored != certificate:
            raise ValueError("stored integrity certificate differs")
        raw = canonical({
            "payload": {
                "stored_integrity_exact": True,
                "stored_integrity_sha256": digest(stored_raw),
            },
            "schema": "paper46-integrity-existing-audit-v1",
            "status": "PASS",
        })
    sys.stdout.buffer.write(raw)
    return 0


def guarded_main() -> int:
    try:
        return main()
    except Exception as error:  # Totalized physical/CLI validation boundary.
        return physical_rejection(classify_failure(error))


if __name__ == "__main__":
    raise SystemExit(guarded_main())
