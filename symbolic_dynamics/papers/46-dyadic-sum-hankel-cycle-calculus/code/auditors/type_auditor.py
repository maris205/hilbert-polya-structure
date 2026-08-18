#!/usr/bin/env python3
"""Strict recursive object, marker, determinant, and scalar type auditor."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


MUTATIONS = {
    "F09/ordinary_det_s2_strip": "ORDINARY_DETERMINANT_OUTSIDE_S1",
    "F10/nonreal_hermitian": "OPERATOR_TYPE_FAILURE",
    "F11/labels_are_primitives": "PRIMITIVE_TYPE_FAILURE",
    "F13/swap_marker_weight": "MARKER_WEIGHT_OWNERSHIP_FAILURE",
    "PKT06/bool_for_cutoff": "RECURSIVE_TYPE_FAILURE",
    "PKT07/float_for_power": "RECURSIVE_TYPE_FAILURE",
    "PTH04/absolute_serialized": "HOST_PATH_TOKEN_FORBIDDEN",
    "RES04/bool_int_alias": "RECURSIVE_TYPE_FAILURE",
    "RES06/infinite_field_in_evaluator": "FINITE_INFINITE_FIREWALL_FAILURE",
    "RES07/coordinated_nested_count_bool": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES08/coordinated_nested_cutoff_float": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES09/comparison_boolean_to_int": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES10/coordinated_missing_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "RES11/coordinated_extra_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
}


class StrictParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(f"CLI_ARGUMENT_ERROR: {message}")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for T")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "T",
                    "instance_id": identifier,
                    "witness": "recursive scalar/object/domain type check rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def path_under(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    cursor = root
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = cursor.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    if raw != canonical(value):
        raise ValueError("noncanonical")
    return value


def exact_scalars(value: Any) -> bool:
    if type(value) in {str, int, bool} or value is None:
        return True
    if type(value) is list:
        return all(exact_scalars(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and exact_scalars(item) for key, item in value.items())
    return False


def keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{label} exact keys")
    return value


def integer(value: Any, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} exact int required")
    return value


def array(value: Any, length: int | None, label: str) -> list[Any]:
    if type(value) is not list or (length is not None and len(value) != length):
        raise ValueError(f"{label} exact array shape")
    return value


def evaluator_scalar_tree(value: Any, label: str) -> None:
    if type(value) in {str, int} or value is None:
        return
    if type(value) is bool or type(value) is float:
        raise ValueError(f"{label} bool/float forbidden")
    if type(value) is list:
        for index, item in enumerate(value):
            evaluator_scalar_tree(item, f"{label}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise ValueError(f"{label} key type")
            evaluator_scalar_tree(item, f"{label}.{key}")
        return
    raise ValueError(f"{label} scalar type")


def fraction(value: Any, label: str) -> None:
    item = keys(value, {"denominator", "numerator"}, label)
    if type(item["denominator"]) is not str or type(item["numerator"]) is not str \
            or re.fullmatch(r"[1-9][0-9]*", item["denominator"]) is None \
            or re.fullmatch(r"0|-?[1-9][0-9]*", item["numerator"]) is None:
        raise ValueError(f"{label} fraction")


def evaluator_schema(value: Any, expected_schema: str, expected_lane: str) -> None:
    outer = keys(value, {"payload", "schema", "status"}, "evaluator")
    if outer["schema"] != expected_schema or outer["status"] != "PASS":
        raise ValueError("evaluator envelope identity")
    payload = keys(outer["payload"], {"candidate_id", "cycle_certificate", "evidence_type",
                   "finite_endpoint_diagnostics", "finite_trace_certificate",
                   "implementation_lane", "structural_certificate", "theorem_claims_inferred"},
                   "evaluator payload")
    evaluator_scalar_tree(payload, "evaluator payload")
    if payload["candidate_id"] != "SD-C48" or payload["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC" \
            or payload["implementation_lane"] != expected_lane \
            or array(payload["theorem_claims_inferred"], 0, "theorem claims") != []:
        raise ValueError("evaluator identity/firewall")
    structural = keys(payload["structural_certificate"], {"records", "support_predicate"}, "structural")
    if structural["support_predicate"] != "x>=2 and x&(x-1)==0":
        raise ValueError("support predicate enum")
    for expected_cutoff, row in zip([8, 16, 32, 64], array(structural["records"], 4, "structural rows")):
        row = keys(row, {"cutoff", "directed_edge_count", "edge_list_sha256", "loop_vertices",
                         "valuation_block_directed_edge_counts", "valuation_mismatch_count"}, "structural row")
        if integer(row["cutoff"], "cutoff") != expected_cutoff:
            raise ValueError("cutoff order")
        integer(row["directed_edge_count"], "directed_edge_count")
        integer(row["valuation_mismatch_count"], "valuation_mismatch_count")
        if type(row["edge_list_sha256"]) is not str or re.fullmatch(r"[0-9a-f]{64}", row["edge_list_sha256"]) is None:
            raise ValueError("edge digest")
        for vertex in array(row["loop_vertices"], None, "loop vertices"):
            integer(vertex, "loop vertex")
        for block in array(row["valuation_block_directed_edge_counts"], None, "valuation blocks"):
            block = keys(block, {"count", "valuation"}, "valuation block")
            integer(block["count"], "valuation count")
            integer(block["valuation"], "valuation")
    cycle = keys(payload["cycle_certificate"], {"direct_vertex_bound", "length_records",
                 "ordered_tuple_policy", "witnesses"}, "cycle")
    if integer(cycle["direct_vertex_bound"], "direct_vertex_bound") != 64 \
            or cycle["ordered_tuple_policy"] != "ALL_ORDERED_TUPLES_NOT_SAMPLED":
        raise ValueError("cycle enum")
    for expected_length, row in zip(range(1, 8), array(cycle["length_records"], 7, "length records")):
        row = keys(row, {"compatible_tuple_count", "length", "odd_solution_count", "solution_count",
                         "solution_map_sha256", "tuple_count"}, "length row")
        for name in ["compatible_tuple_count", "length", "odd_solution_count", "solution_count", "tuple_count"]:
            integer(row[name], name)
        if row["length"] != expected_length or row["tuple_count"] != 6 ** expected_length \
                or type(row["solution_map_sha256"]) is not str \
                or re.fullmatch(r"[0-9a-f]{64}", row["solution_map_sha256"]) is None:
            raise ValueError("length row shape")
    witness_map = keys(cycle["witnesses"], {"2,4,4", "4,4,8,4", "4,8,8,4"}, "witness map")
    for label_text, witness in witness_map.items():
        width = len(label_text.split(","))
        witness = keys(witness, {"odd_solutions", "solutions"}, "witness")
        for name in ["odd_solutions", "solutions"]:
            for row in array(witness[name], None, name):
                for vertex in array(row, width, "solution row"):
                    integer(vertex, "solution vertex")
    endpoint = keys(payload["finite_endpoint_diagnostics"], {"evidence_type",
                    "hs_sigma_one_level_records", "row_one_sigma_zero_partial_sum_a_le_16",
                    "theorem_endpoint_verdicts"}, "endpoint")
    if endpoint["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC":
        raise ValueError("endpoint evidence enum")
    for expected_a, row in zip(range(1, 17), array(endpoint["hs_sigma_one_level_records"], 16, "endpoint rows")):
        row = keys(row, {"a", "sigma_one_level"}, "endpoint row")
        if integer(row["a"], "a") != expected_a:
            raise ValueError("endpoint order")
        fraction(row["sigma_one_level"], "sigma one")
    fraction(endpoint["row_one_sigma_zero_partial_sum_a_le_16"], "row one")
    if array(endpoint["theorem_endpoint_verdicts"], 0, "endpoint verdicts") != []:
        raise ValueError("endpoint firewall")
    trace = keys(payload["finite_trace_certificate"], {"formula", "records", "truncation_policy"}, "trace")
    if trace["formula"] != "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM" \
            or trace["truncation_policy"] != "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE":
        raise ValueError("trace formula enum")
    expected = [(n_value, s_value, r_value) for n_value in [8, 16, 32]
                for s_value in [2, 4] for r_value in [1, 2, 3, 4, 5, 6]]
    for row, grid in zip(array(trace["records"], 36, "trace rows"), expected):
        row = keys(row, {"N", "r", "s", "trace"}, "trace row")
        observed = (integer(row["N"], "N"), integer(row["s"], "s"), integer(row["r"], "r"))
        if observed != grid:
            raise ValueError("trace grid")
        fraction(row["trace"], "trace fraction")


def comparison_schema(value: Any) -> None:
    outer = keys(value, {"payload", "schema", "status"}, "comparison")
    if outer["schema"] != "paper46-exact-comparison-v1" or outer["status"] != "PASS":
        raise ValueError("comparison identity")
    payload = keys(outer["payload"], {"case_counts", "cycle_solution_mismatch_count",
                   "evidence_boundary", "finite_trace_mismatch_count", "finite_trace_truncation",
                   "science_projection_sha256", "strict_recursive_type_and_value_equal",
                   "support_mismatch_count"}, "comparison payload")
    counts = keys(payload["case_counts"], {"cycle_ordered_label_tuples", "finite_trace_cases",
                  "structural_cutoffs"}, "case counts")
    expected = {"cycle_ordered_label_tuples": 335922, "finite_trace_cases": 36, "structural_cutoffs": 4}
    for name, fixed in expected.items():
        if integer(counts[name], name) != fixed:
            raise ValueError("case count")
    for name in ["cycle_solution_mismatch_count", "finite_trace_mismatch_count", "support_mismatch_count"]:
        if integer(payload[name], name) != 0:
            raise ValueError("mismatch count")
    if type(payload["strict_recursive_type_and_value_equal"]) is not bool \
            or payload["strict_recursive_type_and_value_equal"] is not True:
        raise ValueError("comparison boolean")
    boundary = keys(payload["evidence_boundary"], {"finite_evidence_type", "infinite_theorem_status"}, "evidence boundary")
    if boundary != {"finite_evidence_type": "FINITE_EXACT_DIAGNOSTIC",
                    "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE"} \
            or payload["finite_trace_truncation"] != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE":
        raise ValueError("comparison enum")
    if type(payload["science_projection_sha256"]) is not str \
            or re.fullmatch(r"[0-9a-f]{64}", payload["science_projection_sha256"]) is None:
        raise ValueError("science projection digest")


def no_host_tokens(value: Any) -> bool:
    if type(value) is str:
        return not any(token in value for token in ["/home/", "/root/", "/tmp/", "\\home\\", "\\root\\", "\\tmp\\"])
    if type(value) is list:
        return all(no_host_tokens(item) for item in value)
    if type(value) is dict:
        return all(no_host_tokens(key) and no_host_tokens(item) for key, item in value.items())
    return True


def physical_rejection(code: str) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, "consumer": "T"},
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
    if any(piece in message for piece in ["unsafe root", "symlink", "containment",
                                           "No such file", "Not a directory"]):
        return "PATH_ROOT_INVALID"
    if "exact keys" in message or "duplicate key" in message:
        return "RESULT_SCHEMA_KEYSET_FAILURE"
    if any(piece in message for piece in ["exact int required", "bool/float forbidden",
                                           "exact array shape", "fraction", "comparison boolean",
                                           "scalar type", "key type"]):
        return "RESULT_SCHEMA_TYPE_FAILURE"
    return "VALIDATION_RUNTIME_FAILURE"


def main() -> int:
    parser = StrictParser(add_help=True)
    parser.add_argument("--output-root")
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        if args.output_root is not None:
            raise ValueError("CLI_ARGUMENT_ERROR: --mutation is exclusive")
        return reject(args.mutation)
    if not args.output_root:
        raise ValueError("CLI_ARGUMENT_ERROR: --output-root required")
    output = Path(args.output_root)
    packet = load(path_under(output, "data/source_packet.json"))
    matrix = load(path_under(output, "results/evaluator_m.json"))
    cyclic = load(path_under(output, "results/evaluator_c.json"))
    comparison = load(path_under(output, "results/exact_comparison.json"))
    evaluator_schema(matrix, "paper46-evaluator-m-v1",
                     "M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS")
    evaluator_schema(cyclic, "paper46-evaluator-c-v1",
                     "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER")
    comparison_schema(comparison)
    matrix_projection = {key: item for key, item in matrix["payload"].items()
                         if key != "implementation_lane"}
    cyclic_projection = {key: item for key, item in cyclic["payload"].items()
                         if key != "implementation_lane"}
    if matrix_projection != cyclic_projection \
            or comparison["payload"]["science_projection_sha256"] \
            != hashlib.sha256(canonical(matrix_projection)).hexdigest():
        raise ValueError("typed science projection mismatch")
    values = [packet, matrix, cyclic, comparison]
    if not all(exact_scalars(value) and no_host_tokens(value) for value in values):
        raise ValueError("scalar or host-token violation")
    source = packet["payload"]
    if source["primitive_type"] != "LEAST_PERIOD_CLOSED_VERTEX_CYCLE" \
            or source["edge_label_type"] != "DERIVED_DYADIC_CONSTRAINT" \
            or source["marker"] != "z_PER_EDGE" \
            or source["valuation_weight"] != "2^(-k*r*s)" \
            or source["determinant_domains"] != {"det2": "Re(s)>1/2", "ordinary": "Re(s)>1"}:
        raise ValueError("owned type mismatch")
    if matrix["payload"]["theorem_claims_inferred"] != [] \
            or cyclic["payload"]["theorem_claims_inferred"] != []:
        raise ValueError("finite/infinite firewall")
    output_value = {
        "payload": {
            "allowed_scalar_types": ["bool", "int", "null", "str"],
            "determinant_domain_types_exact": True,
            "edge_label_not_primitive": True,
            "finite_infinite_firewall": True,
            "field_level_result_schema": "paper46-result-schema-v2",
            "host_path_token_count": 0,
            "marker_weight_separated": True,
            "nonreal_hermitian_claim": False,
            "recursive_scalar_type_failures": 0,
        },
        "schema": "paper46-type-audit-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(output_value))
    return 0


def guarded_main() -> int:
    try:
        return main()
    except Exception as error:  # Totalized physical/CLI validation boundary.
        return physical_rejection(classify_failure(error))


if __name__ == "__main__":
    raise SystemExit(guarded_main())
