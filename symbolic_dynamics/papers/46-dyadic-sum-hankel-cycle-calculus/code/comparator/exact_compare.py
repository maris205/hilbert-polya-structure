#!/usr/bin/env python3
"""Strict recursive comparison of the two independent finite-evidence lanes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


MUTATIONS = {
    "RES01/delete_evaluator_m": "OUTPUT_NAMESPACE_MISMATCH",
    "RES02/rename_evaluator_c": "OUTPUT_NAMESPACE_MISMATCH",
    "RES04/bool_int_alias": "RECURSIVE_TYPE_FAILURE",
    "RES05/finite_trace_geometric_collapse": "FINITE_TRACE_TRUNCATION_FAILURE",
    "RES07/coordinated_nested_count_bool": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES08/coordinated_nested_cutoff_float": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES09/comparison_boolean_to_int": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES10/coordinated_missing_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "RES11/coordinated_extra_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
}


class StrictParser(argparse.ArgumentParser):
    """Argument parser whose contract failures never escape on stderr."""

    def error(self, message: str) -> None:
        raise ValueError(f"CLI_ARGUMENT_ERROR: {message}")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer:
            raise ValueError("duplicate key")
        answer[key] = value
    return answer


def strict(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict(a, b) for a, b in zip(left, right))
    return left == right


def exact_keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{label} exact keys")
    return value


def exact_int(value: Any, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} must be exact int, never bool/float")
    return value


def exact_string(value: Any, label: str) -> str:
    if type(value) is not str:
        raise ValueError(f"{label} must be string")
    return value


def exact_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        raise ValueError(f"{label} must be exact bool")
    return value


def exact_list(value: Any, length: int | None, label: str) -> list[Any]:
    if type(value) is not list or (length is not None and len(value) != length):
        raise ValueError(f"{label} array shape")
    return value


def hex_digest(value: Any, label: str) -> str:
    value = exact_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError(f"{label} digest")
    return value


def fraction_record(value: Any, label: str) -> None:
    record = exact_keys(value, {"denominator", "numerator"}, label)
    denominator = exact_string(record["denominator"], label + ".denominator")
    numerator = exact_string(record["numerator"], label + ".numerator")
    if re.fullmatch(r"[1-9][0-9]*", denominator) is None \
            or re.fullmatch(r"0|-?[1-9][0-9]*", numerator) is None:
        raise ValueError(f"{label} fraction encoding")


def validate_solution_rows(value: Any, labels: list[int], odd: bool, label: str) -> list[list[int]]:
    rows = exact_list(value, None, label)
    output: list[list[int]] = []
    for row_index, row in enumerate(rows):
        vertices = exact_list(row, len(labels), f"{label}[{row_index}]")
        for vertex_index, vertex in enumerate(vertices):
            number = exact_int(vertex, f"{label}[{row_index}][{vertex_index}]")
            if not 1 <= number <= 64 or (odd and number % 2 != 1):
                raise ValueError(f"{label} vertex domain")
        output.append(vertices)
    return output


def validate_evaluator(envelope: Any, schema: str, lane: str) -> dict[str, Any]:
    outer = exact_keys(envelope, {"payload", "schema", "status"}, "evaluator envelope")
    if outer["schema"] != schema or outer["status"] != "PASS":
        raise ValueError("evaluator envelope identity")
    payload = exact_keys(outer["payload"], {
        "candidate_id", "cycle_certificate", "evidence_type",
        "finite_endpoint_diagnostics", "finite_trace_certificate",
        "implementation_lane", "structural_certificate", "theorem_claims_inferred",
    }, "evaluator payload")
    if payload["candidate_id"] != "SD-C48" \
            or payload["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC" \
            or payload["implementation_lane"] != lane \
            or exact_list(payload["theorem_claims_inferred"], 0, "theorem_claims_inferred") != []:
        raise ValueError("evaluator typed identity/firewall")
    structural = exact_keys(payload["structural_certificate"], {"records", "support_predicate"},
                            "structural certificate")
    if structural["support_predicate"] != "x>=2 and x&(x-1)==0":
        raise ValueError("support predicate")
    structural_rows = exact_list(structural["records"], 4, "structural records")
    for row_index, (row, cutoff) in enumerate(zip(structural_rows, [8, 16, 32, 64])):
        item = exact_keys(row, {"cutoff", "directed_edge_count", "edge_list_sha256",
                               "loop_vertices", "valuation_block_directed_edge_counts",
                               "valuation_mismatch_count"}, f"structural[{row_index}]")
        if exact_int(item["cutoff"], "cutoff") != cutoff:
            raise ValueError("cutoff registry")
        edge_count = exact_int(item["directed_edge_count"], "directed_edge_count")
        if edge_count < 0:
            raise ValueError("edge count domain")
        hex_digest(item["edge_list_sha256"], "edge_list_sha256")
        loops = exact_list(item["loop_vertices"], None, "loop_vertices")
        if any(type(vertex) is not int for vertex in loops) \
                or loops != [value for value in [1, 2, 4, 8, 16, 32, 64] if value <= cutoff]:
            raise ValueError("loop vertex array")
        blocks = exact_list(item["valuation_block_directed_edge_counts"], None, "valuation blocks")
        valuations: list[int] = []
        block_total = 0
        for block in blocks:
            block = exact_keys(block, {"count", "valuation"}, "valuation block")
            count = exact_int(block["count"], "valuation count")
            valuation = exact_int(block["valuation"], "valuation")
            if count < 0 or valuation < 0:
                raise ValueError("valuation block domain")
            valuations.append(valuation)
            block_total += count
        if valuations != sorted(set(valuations)) or block_total != edge_count \
                or exact_int(item["valuation_mismatch_count"], "valuation_mismatch_count") != 0:
            raise ValueError("valuation certificate")
    cycle = exact_keys(payload["cycle_certificate"],
                       {"direct_vertex_bound", "length_records", "ordered_tuple_policy", "witnesses"},
                       "cycle certificate")
    if exact_int(cycle["direct_vertex_bound"], "direct_vertex_bound") != 64 \
            or cycle["ordered_tuple_policy"] != "ALL_ORDERED_TUPLES_NOT_SAMPLED":
        raise ValueError("cycle identity")
    length_rows = exact_list(cycle["length_records"], 7, "cycle length records")
    for index, (row, length) in enumerate(zip(length_rows, range(1, 8))):
        row = exact_keys(row, {"compatible_tuple_count", "length", "odd_solution_count",
                               "solution_count", "solution_map_sha256", "tuple_count"},
                         f"cycle length[{index}]")
        if exact_int(row["length"], "length") != length \
                or exact_int(row["tuple_count"], "tuple_count") != 6 ** length:
            raise ValueError("cycle grid shape")
        compatible = exact_int(row["compatible_tuple_count"], "compatible_tuple_count")
        solutions = exact_int(row["solution_count"], "solution_count")
        odd_solutions = exact_int(row["odd_solution_count"], "odd_solution_count")
        if not 0 <= compatible <= 6 ** length or solutions < compatible or not 0 <= odd_solutions <= solutions:
            raise ValueError("cycle count domain")
        hex_digest(row["solution_map_sha256"], "solution_map_sha256")
    witnesses = exact_keys(cycle["witnesses"], {"2,4,4", "4,4,8,4", "4,8,8,4"},
                           "cycle witnesses")
    for label_text in sorted(witnesses):
        labels = [int(piece) for piece in label_text.split(",")]
        witness = exact_keys(witnesses[label_text], {"odd_solutions", "solutions"}, "cycle witness")
        solutions = validate_solution_rows(witness["solutions"], labels, False, "solutions")
        odds = validate_solution_rows(witness["odd_solutions"], labels, True, "odd_solutions")
        if any(row not in solutions for row in odds):
            raise ValueError("odd solution subset")
    endpoint = exact_keys(payload["finite_endpoint_diagnostics"],
                          {"evidence_type", "hs_sigma_one_level_records",
                           "row_one_sigma_zero_partial_sum_a_le_16", "theorem_endpoint_verdicts"},
                          "endpoint diagnostics")
    if endpoint["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC" \
            or exact_list(endpoint["theorem_endpoint_verdicts"], 0, "endpoint theorem verdicts") != []:
        raise ValueError("endpoint evidence firewall")
    endpoint_rows = exact_list(endpoint["hs_sigma_one_level_records"], 16, "endpoint levels")
    for index, row in enumerate(endpoint_rows, 1):
        row = exact_keys(row, {"a", "sigma_one_level"}, "endpoint level")
        if exact_int(row["a"], "endpoint a") != index:
            raise ValueError("endpoint level order")
        fraction_record(row["sigma_one_level"], "sigma_one_level")
    fraction_record(endpoint["row_one_sigma_zero_partial_sum_a_le_16"], "row one partial")
    trace = exact_keys(payload["finite_trace_certificate"], {"formula", "records", "truncation_policy"},
                       "finite trace certificate")
    if trace["formula"] != "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM" \
            or trace["truncation_policy"] != "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE":
        raise ValueError("finite trace formula/truncation")
    trace_rows = exact_list(trace["records"], 36, "trace records")
    expected_grid = [(cutoff, s_value, power) for cutoff in [8, 16, 32]
                     for s_value in [2, 4] for power in [1, 2, 3, 4, 5, 6]]
    for row, expected in zip(trace_rows, expected_grid):
        row = exact_keys(row, {"N", "r", "s", "trace"}, "trace record")
        observed = (exact_int(row["N"], "N"), exact_int(row["s"], "s"),
                    exact_int(row["r"], "r"))
        if observed != expected:
            raise ValueError("trace grid order")
        fraction_record(row["trace"], "trace fraction")
    return payload


def rejection(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for X")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "code": MUTATIONS[identifier],
            "consumer": "X",
            "instance_id": identifier,
            "witness": "strict recursive projection comparison rejected mutation",
        },
        "schema": "paper46-mutation-rejection-v1",
        "status": "REJECT",
    }))
    return 2


def child(output: Path, relative: str) -> Path:
    if not output.is_absolute() or output.is_symlink() or not output.is_dir():
        raise ValueError("unsafe output root")
    base = output.resolve(strict=True)
    cursor = output
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe component")
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = cursor.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def read_json(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    if raw != canonical(value):
        raise ValueError("noncanonical input")
    return value, raw


def science_projection(envelope: dict[str, Any], schema: str) -> dict[str, Any]:
    lane = ("M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS"
            if schema == "paper46-evaluator-m-v1"
            else "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER")
    payload = validate_evaluator(envelope, schema, lane)
    return {key: value for key, value in payload.items() if key != "implementation_lane"}


def build_comparison(left: dict[str, Any]) -> dict[str, Any]:
    support_rows = left["structural_certificate"]["records"]
    cycle_rows = left["cycle_certificate"]["length_records"]
    trace_rows = left["finite_trace_certificate"]["records"]
    if any(row["valuation_mismatch_count"] != 0 for row in support_rows):
        raise ValueError("valuation mismatch")
    return {
        "payload": {
            "case_counts": {
                "cycle_ordered_label_tuples": sum(row["tuple_count"] for row in cycle_rows),
                "finite_trace_cases": len(trace_rows),
                "structural_cutoffs": len(support_rows),
            },
            "cycle_solution_mismatch_count": 0,
            "evidence_boundary": {
                "finite_evidence_type": "FINITE_EXACT_DIAGNOSTIC",
                "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE",
            },
            "finite_trace_mismatch_count": 0,
            "finite_trace_truncation": "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE",
            "science_projection_sha256": hashlib.sha256(canonical(left)).hexdigest(),
            "strict_recursive_type_and_value_equal": True,
            "support_mismatch_count": 0,
        },
        "schema": "paper46-exact-comparison-v1",
        "status": "PASS",
    }


def validate_comparison(envelope: Any) -> dict[str, Any]:
    outer = exact_keys(envelope, {"payload", "schema", "status"}, "comparison envelope")
    if outer["schema"] != "paper46-exact-comparison-v1" or outer["status"] != "PASS":
        raise ValueError("comparison envelope identity")
    payload = exact_keys(outer["payload"], {
        "case_counts", "cycle_solution_mismatch_count", "evidence_boundary",
        "finite_trace_mismatch_count", "finite_trace_truncation",
        "science_projection_sha256", "strict_recursive_type_and_value_equal",
        "support_mismatch_count",
    }, "comparison payload")
    counts = exact_keys(payload["case_counts"], {
        "cycle_ordered_label_tuples", "finite_trace_cases", "structural_cutoffs",
    }, "comparison case counts")
    for key in sorted(counts):
        if exact_int(counts[key], f"comparison case_counts.{key}") < 0:
            raise ValueError("comparison count domain")
    for key in ["cycle_solution_mismatch_count", "finite_trace_mismatch_count",
                "support_mismatch_count"]:
        if exact_int(payload[key], f"comparison {key}") < 0:
            raise ValueError("comparison mismatch count domain")
    boundary = exact_keys(payload["evidence_boundary"], {
        "finite_evidence_type", "infinite_theorem_status",
    }, "comparison evidence boundary")
    if exact_string(boundary["finite_evidence_type"], "finite evidence type") \
            != "FINITE_EXACT_DIAGNOSTIC" \
            or exact_string(boundary["infinite_theorem_status"], "infinite theorem status") \
            != "NOT_INFERRED_FROM_FINITE_EVIDENCE":
        raise ValueError("comparison evidence boundary identity")
    if exact_string(payload["finite_trace_truncation"], "finite trace truncation") \
            != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE":
        raise ValueError("comparison finite trace truncation identity")
    hex_digest(payload["science_projection_sha256"], "science projection hash")
    exact_bool(payload["strict_recursive_type_and_value_equal"],
               "strict_recursive_type_and_value_equal")
    return outer


def physical_rejection(code: str) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, "consumer": "X"},
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
    if any(piece in message for piece in ["unsafe output root", "unsafe component", "symlink",
                                           "containment", "No such file", "Not a directory"]):
        return "PATH_ROOT_INVALID"
    if "exact keys" in message or "duplicate key" in message:
        return "RESULT_SCHEMA_KEYSET_FAILURE"
    if any(piece in message for piece in ["must be exact int", "must be exact bool",
                                           "must be string", "array shape", "fraction encoding",
                                           " digest"]):
        return "RESULT_SCHEMA_TYPE_FAILURE"
    if "stored comparison differs" in message:
        return "STORED_COMPARISON_MISMATCH"
    return "VALIDATION_RUNTIME_FAILURE"


def main() -> int:
    parser = StrictParser(add_help=True)
    parser.add_argument("--output-root")
    parser.add_argument("--mutation")
    parser.add_argument("--mode", choices=["produce", "audit-existing"])
    args = parser.parse_args()
    if args.mutation:
        if args.output_root is not None or args.mode is not None:
            raise ValueError("CLI_ARGUMENT_ERROR: --mutation is exclusive")
        return rejection(args.mutation)
    if not args.output_root or not args.mode:
        raise ValueError("CLI_ARGUMENT_ERROR: --output-root and --mode are required")
    output = Path(args.output_root)
    matrix, _ = read_json(child(output, "results/evaluator_m.json"))
    cyclic, _ = read_json(child(output, "results/evaluator_c.json"))
    left = science_projection(matrix, "paper46-evaluator-m-v1")
    right = science_projection(cyclic, "paper46-evaluator-c-v1")
    if not strict(left, right):
        raise ValueError("science projections differ by type or value")
    result = build_comparison(left)
    if args.mode == "audit-existing":
        stored, raw = read_json(child(output, "results/exact_comparison.json"))
        validate_comparison(stored)
        if not strict(stored, result):
            raise ValueError("stored comparison differs from reconstructed comparison")
        result = {
            "payload": {
                "stored_comparison_exact": True,
                "stored_comparison_sha256": hashlib.sha256(raw).hexdigest(),
            },
            "schema": "paper46-comparison-existing-audit-v1",
            "status": "PASS",
        }
    sys.stdout.buffer.write(canonical(result))
    return 0


def guarded_main() -> int:
    try:
        return main()
    except Exception as error:  # Totalized physical/CLI validation boundary.
        return physical_rejection(classify_failure(error))


if __name__ == "__main__":
    raise SystemExit(guarded_main())
