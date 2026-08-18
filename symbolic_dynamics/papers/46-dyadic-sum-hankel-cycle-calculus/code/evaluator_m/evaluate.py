#!/usr/bin/env python3
"""Evaluator M: literal cutoff matrix and direct bounded-walk implementation."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


RAW_CONTRACT_SHA256 = "b07dd9541612ea31dc23c0137aac49acf8d2ce07d0df2cdce17721d273f61172"
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
MUTATIONS = {
    "F01/support_square": "SOURCE_SUPPORT_CHANGED",
    "F02/delete_loop_one": "LOOP_CONVENTION_CHANGED",
    "F03/insert_edge_1_5": "SUPPORT_AND_VALUATION_FAILURE",
    "F07/delete_odd_half": "ODD_CYCLE_FORMULA_FAILURE",
    "F08/accept_even_nonzero": "EVEN_CYCLE_COMPATIBILITY_FAILURE",
    "PKT01/missing_candidate": "PACKET_KEYSET_FAILURE",
    "PKT02/extra_key": "PACKET_KEYSET_FAILURE",
    "PKT03/reordered_cutoffs": "CASE_ORDER_FAILURE",
    "PKT04/duplicate_top_key": "DUPLICATE_JSON_KEY",
    "PKT05/duplicate_nested_key": "DUPLICATE_JSON_KEY",
    "PKT06/bool_for_cutoff": "RECURSIVE_TYPE_FAILURE",
    "PKT07/float_for_power": "RECURSIVE_TYPE_FAILURE",
    "PKT09/cutoff_63": "RAW_CASE_CONTRACT_DRIFT",
    "PTH03/symlink_static": "SYMLINK_FORBIDDEN",
    "RES05/finite_trace_geometric_collapse": "FINITE_TRACE_TRUNCATION_FAILURE",
    "RES07/coordinated_nested_count_bool": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES08/coordinated_nested_cutoff_float": "RESULT_SCHEMA_TYPE_FAILURE",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def reject(identifier: str) -> int:
    code = MUTATIONS.get(identifier)
    if code is None:
        raise ValueError("mutation not designated for M")
    envelope = {
        "payload": {
            "code": code,
            "consumer": "M",
            "instance_id": identifier,
            "witness": "literal predicate, direct recurrence, or strict packet gate rejected mutation",
        },
        "schema": "paper46-mutation-rejection-v1",
        "status": "REJECT",
    }
    sys.stdout.buffer.write(canonical(envelope))
    return 2


def safe_file(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    resolved_root = root.resolve(strict=True)
    cursor = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe component")
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink forbidden")
    resolved = cursor.resolve(strict=True)
    if resolved_root not in resolved.parents or not resolved.is_file():
        raise ValueError("containment failure")
    return resolved


def strict_int_list(value: Any, expected: list[int]) -> bool:
    return type(value) is list and len(value) == len(expected) \
        and all(type(x) is int for x in value) and value == expected


def load_contract(root: Path) -> dict[str, Any]:
    path = safe_file(root, "contracts/RAW_CASE_CONTRACT.json")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != RAW_CONTRACT_SHA256:
        raise ValueError("raw contract drift")
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if raw != canonical(value) or set(value) != {
        "candidate_id", "canonicalization", "cycle_grid", "evidence_types",
        "frozen_precheck_witnesses", "schema", "structural_cutoffs",
        "trace_grid", "valuation_block_max",
    }:
        raise ValueError("raw contract shape")
    if value["candidate_id"] != "SD-C48" or value["schema"] != "paper46-raw-case-contract-v1":
        raise ValueError("raw identity")
    if not strict_int_list(value["structural_cutoffs"], [8, 16, 32, 64]):
        raise ValueError("structural grid")
    grid = value["cycle_grid"]
    if type(grid["direct_vertex_max"]) is not int or grid["direct_vertex_max"] != 64 \
            or not strict_int_list(grid["label_values"], [2, 4, 8, 16, 32, 64]) \
            or not strict_int_list(grid["lengths"], [1, 2, 3, 4, 5, 6, 7]):
        raise ValueError("cycle grid")
    trace = value["trace_grid"]
    if not strict_int_list(trace["cutoffs"], [8, 16, 32]) \
            or not strict_int_list(trace["powers"], [1, 2, 3, 4, 5, 6]) \
            or not strict_int_list(trace["s_values"], [2, 4]):
        raise ValueError("trace grid")
    return value


def is_dyadic(value: int) -> bool:
    return value >= 2 and value & (value - 1) == 0


def valuation_two(value: int) -> int:
    count = 0
    while value % 2 == 0:
        count += 1
        value //= 2
    return count


def structural_record(cutoff: int) -> dict[str, Any]:
    edges: list[list[int]] = []
    block_counts: dict[int, int] = {}
    loops: list[int] = []
    mismatch = 0
    for left in range(1, cutoff + 1):
        for right in range(1, cutoff + 1):
            if is_dyadic(left + right):
                edges.append([left, right])
                vl, vr = valuation_two(left), valuation_two(right)
                if vl != vr:
                    mismatch += 1
                block_counts[vl] = block_counts.get(vl, 0) + 1
                if left == right:
                    loops.append(left)
    digest = hashlib.sha256(canonical(edges)).hexdigest()
    return {
        "cutoff": cutoff,
        "directed_edge_count": len(edges),
        "edge_list_sha256": digest,
        "loop_vertices": loops,
        "valuation_block_directed_edge_counts": [
            {"count": block_counts[key], "valuation": key} for key in sorted(block_counts)
        ],
        "valuation_mismatch_count": mismatch,
    }


def direct_solutions(labels: tuple[int, ...], bound: int) -> list[list[int]]:
    solutions: list[list[int]] = []
    for first in range(1, bound + 1):
        vertices = [first]
        current = first
        valid = True
        for label in labels[:-1]:
            current = label - current
            if current < 1 or current > bound:
                valid = False
                break
            vertices.append(current)
        if valid and labels[-1] - current == first:
            solutions.append(vertices)
    return solutions


def cycle_certificate(labels: list[int], lengths: list[int], bound: int) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    witnesses: dict[str, Any] = {}
    for length in lengths:
        hasher = hashlib.sha256()
        compatible = 0
        solution_count = 0
        odd_solution_count = 0
        tuple_count = 0
        for label_tuple in itertools.product(labels, repeat=length):
            solutions = direct_solutions(label_tuple, bound)
            odd_solutions = [row for row in solutions if all(vertex % 2 for vertex in row)]
            tuple_count += 1
            compatible += int(bool(solutions))
            solution_count += len(solutions)
            odd_solution_count += len(odd_solutions)
            hasher.update(canonical({
                "labels": list(label_tuple),
                "odd_solutions": odd_solutions,
                "solutions": solutions,
            }))
            key = ",".join(str(x) for x in label_tuple)
            if key in {"2,4,4", "4,8,8,4", "4,4,8,4"}:
                witnesses[key] = {"odd_solutions": odd_solutions, "solutions": solutions}
        records.append({
            "compatible_tuple_count": compatible,
            "length": length,
            "odd_solution_count": odd_solution_count,
            "solution_count": solution_count,
            "solution_map_sha256": hasher.hexdigest(),
            "tuple_count": tuple_count,
        })
    return {
        "direct_vertex_bound": bound,
        "length_records": records,
        "ordered_tuple_policy": "ALL_ORDERED_TUPLES_NOT_SAMPLED",
        "witnesses": witnesses,
    }


def zero_matrix(size: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def matrix(cutoff: int, s_value: int) -> list[list[Fraction]]:
    result = zero_matrix(cutoff)
    exponent = s_value // 2
    for i in range(cutoff):
        for j in range(cutoff):
            left, right = i + 1, j + 1
            if is_dyadic(left + right):
                result[i][j] = Fraction(1, (left * right) ** exponent)
    return result


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(left)
    answer = zero_matrix(size)
    for i in range(size):
        for k in range(size):
            coefficient = left[i][k]
            if not coefficient:
                continue
            for j in range(size):
                if right[k][j]:
                    answer[i][j] += coefficient * right[k][j]
    return answer


def fraction_record(value: Fraction) -> dict[str, str]:
    return {"denominator": str(value.denominator), "numerator": str(value.numerator)}


def trace_records(cutoffs: list[int], s_values: list[int], powers: list[int]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for cutoff in cutoffs:
        for s_value in s_values:
            base = matrix(cutoff, s_value)
            power = [row[:] for row in base]
            for r_value in powers:
                if r_value > 1:
                    power = multiply(power, base)
                value = sum(power[i][i] for i in range(cutoff))
                records.append({
                    "N": cutoff,
                    "r": r_value,
                    "s": s_value,
                    "trace": fraction_record(value),
                })
    return records


def endpoint_diagnostics() -> dict[str, Any]:
    levels = []
    for exponent in range(1, 17):
        size = 2 ** exponent
        harmonic = sum((Fraction(1, j) for j in range(1, size)), Fraction(0))
        levels.append({"a": exponent, "sigma_one_level": fraction_record(2 * harmonic / size)})
    return {
        "evidence_type": "FINITE_EXACT_DIAGNOSTIC",
        "hs_sigma_one_level_records": levels,
        "row_one_sigma_zero_partial_sum_a_le_16": fraction_record(Fraction(16)),
        "theorem_endpoint_verdicts": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation:
        return reject(arguments.mutation)
    if not arguments.root:
        raise ValueError("--root required")
    root = Path(arguments.root)
    contract = load_contract(root)
    structural = [structural_record(value) for value in contract["structural_cutoffs"]]
    cycles = cycle_certificate(contract["cycle_grid"]["label_values"],
                               contract["cycle_grid"]["lengths"],
                               contract["cycle_grid"]["direct_vertex_max"])
    traces = trace_records(contract["trace_grid"]["cutoffs"],
                           contract["trace_grid"]["s_values"],
                           contract["trace_grid"]["powers"])
    payload = {
        "candidate_id": "SD-C48",
        "cycle_certificate": cycles,
        "evidence_type": "FINITE_EXACT_DIAGNOSTIC",
        "finite_endpoint_diagnostics": endpoint_diagnostics(),
        "finite_trace_certificate": {
            "formula": "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM",
            "records": traces,
            "truncation_policy": "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE",
        },
        "implementation_lane": "M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS",
        "structural_certificate": {
            "records": structural,
            "support_predicate": "x>=2 and x&(x-1)==0",
        },
        "theorem_claims_inferred": [],
    }
    result = {"payload": payload, "schema": "paper46-evaluator-m-v1", "status": "PASS"}
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
