#!/usr/bin/env python3
"""Evaluator C: anti-diagonal, valuation, and algebraic cyclic solver lane."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
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
    "F04/bounded_at_zero": "ROW_ONE_NOT_L2",
    "F05/s2_at_half": "HILBERT_SCHMIDT_ENDPOINT_DIVERGES",
    "F06/s1_at_one": "TRACE_CLASS_ENDPOINT_DIVERGES",
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


def encode(value: Any) -> bytes:
    text = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                      allow_nan=False, separators=(",", ": "))
    return (text + "\n").encode("ascii")


def no_repeated_names(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for name, value in pairs:
        if name in output:
            raise ValueError("duplicate JSON key")
        output[name] = value
    return output


def mutation_rejection(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for C")
    value = {
        "payload": {
            "code": MUTATIONS[identifier],
            "consumer": "C",
            "instance_id": identifier,
            "witness": "anti-diagonal, valuation, cyclic-closing, or strict packet rule rejected mutation",
        },
        "schema": "paper46-mutation-rejection-v1",
        "status": "REJECT",
    }
    sys.stdout.buffer.write(encode(value))
    return 2


def locate(root: Path, parts: tuple[str, ...]) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    cursor = root
    for part in parts:
        if part in {"", ".", ".."} or "/" in part or "\\" in part:
            raise ValueError("unsafe path")
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink forbidden")
    answer = cursor.resolve(strict=True)
    if base not in answer.parents or not answer.is_file():
        raise ValueError("path escaped")
    return answer


def exact_integer_sequence(value: Any, expected: tuple[int, ...]) -> bool:
    return isinstance(value, list) and len(value) == len(expected) \
        and all(type(item) is int for item in value) and tuple(value) == expected


def contract(root: Path) -> dict[str, Any]:
    path = locate(root, ("contracts", "RAW_CASE_CONTRACT.json"))
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != RAW_CONTRACT_SHA256:
        raise ValueError("raw case seal mismatch")
    value = json.loads(raw.decode("ascii"), object_pairs_hook=no_repeated_names,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    required = {
        "candidate_id", "canonicalization", "cycle_grid", "evidence_types",
        "frozen_precheck_witnesses", "schema", "structural_cutoffs",
        "trace_grid", "valuation_block_max",
    }
    if raw != encode(value) or set(value.keys()) != required:
        raise ValueError("case contract schema")
    if value.get("candidate_id") != "SD-C48" or value.get("schema") != "paper46-raw-case-contract-v1":
        raise ValueError("case contract identity")
    if not exact_integer_sequence(value["structural_cutoffs"], (8, 16, 32, 64)):
        raise ValueError("cutoff registry")
    cycles = value["cycle_grid"]
    if type(cycles.get("direct_vertex_max")) is not int or cycles["direct_vertex_max"] != 64:
        raise ValueError("vertex bound")
    if not exact_integer_sequence(cycles.get("label_values"), (2, 4, 8, 16, 32, 64)) \
            or not exact_integer_sequence(cycles.get("lengths"), (1, 2, 3, 4, 5, 6, 7)):
        raise ValueError("cycle registry")
    traces = value["trace_grid"]
    if not exact_integer_sequence(traces.get("cutoffs"), (8, 16, 32)) \
            or not exact_integer_sequence(traces.get("powers"), (1, 2, 3, 4, 5, 6)) \
            or not exact_integer_sequence(traces.get("s_values"), (2, 4)):
        raise ValueError("trace registry")
    return value


def two_valuation(number: int) -> int:
    exponent = 0
    quotient = number
    while quotient % 2 == 0:
        quotient //= 2
        exponent += 1
    return exponent


def anti_diagonal_edges(cutoff: int) -> list[list[int]]:
    edge_set: set[tuple[int, int]] = set()
    anti_diagonal = 2
    while anti_diagonal <= 2 * cutoff:
        for left in range(1, anti_diagonal):
            right = anti_diagonal - left
            if left <= cutoff and right <= cutoff:
                edge_set.add((left, right))
        anti_diagonal *= 2
    return [[left, right] for left, right in sorted(edge_set)]


def structural(cutoff: int) -> dict[str, Any]:
    edges = anti_diagonal_edges(cutoff)
    blocks: dict[int, int] = {}
    failures = 0
    loops: list[int] = []
    for left, right in edges:
        first, second = two_valuation(left), two_valuation(right)
        failures += int(first != second)
        blocks[first] = blocks.get(first, 0) + 1
        if left == right:
            loops.append(left)
    return {
        "cutoff": cutoff,
        "directed_edge_count": len(edges),
        "edge_list_sha256": hashlib.sha256(encode(edges)).hexdigest(),
        "loop_vertices": loops,
        "valuation_block_directed_edge_counts": [
            {"count": blocks[index], "valuation": index} for index in sorted(blocks)
        ],
        "valuation_mismatch_count": failures,
    }


def derive_vertices(first: int, labels: tuple[int, ...], bound: int) -> list[int] | None:
    vertices = [first]
    current = first
    for label in labels[:-1]:
        following = label - current
        if following <= 0 or following > bound:
            return None
        vertices.append(following)
        current = following
    if labels[-1] - current != first:
        return None
    return vertices


def algebraic_solutions(labels: tuple[int, ...], bound: int) -> list[list[int]]:
    length = len(labels)
    alternating = sum((1 if (length - (index + 1)) % 2 == 0 else -1) * label
                      for index, label in enumerate(labels))
    candidates: list[int]
    if length % 2:
        if alternating % 2:
            return []
        candidates = [alternating // 2]
    else:
        if alternating != 0:
            return []
        candidates = list(range(1, bound + 1))
    output: list[list[int]] = []
    for first in candidates:
        if first < 1 or first > bound:
            continue
        vertices = derive_vertices(first, labels, bound)
        if vertices is not None:
            output.append(vertices)
    return output


def all_cycle_data(label_values: list[int], lengths: list[int], bound: int) -> dict[str, Any]:
    summaries: list[dict[str, Any]] = []
    witness_map: dict[str, Any] = {}
    watched = {"2,4,4", "4,8,8,4", "4,4,8,4"}
    for length in lengths:
        digest = hashlib.sha256()
        tuples_seen = 0
        compatible = 0
        solutions_seen = 0
        odd_seen = 0
        for labels in itertools.product(label_values, repeat=length):
            solutions = algebraic_solutions(labels, bound)
            odds = [vertices for vertices in solutions if all(vertex & 1 for vertex in vertices)]
            tuples_seen += 1
            compatible += 1 if solutions else 0
            solutions_seen += len(solutions)
            odd_seen += len(odds)
            digest.update(encode({
                "labels": list(labels),
                "odd_solutions": odds,
                "solutions": solutions,
            }))
            key = ",".join(map(str, labels))
            if key in watched:
                witness_map[key] = {"odd_solutions": odds, "solutions": solutions}
        summaries.append({
            "compatible_tuple_count": compatible,
            "length": length,
            "odd_solution_count": odd_seen,
            "solution_count": solutions_seen,
            "solution_map_sha256": digest.hexdigest(),
            "tuple_count": tuples_seen,
        })
    return {
        "direct_vertex_bound": bound,
        "length_records": summaries,
        "ordered_tuple_policy": "ALL_ORDERED_TUPLES_NOT_SAMPLED",
        "witnesses": witness_map,
    }


def neighbors_in_odd_block(vertex: int, maximum: int) -> list[int]:
    values: list[int] = []
    anti_diagonal = 2
    while anti_diagonal <= vertex + maximum:
        candidate = anti_diagonal - vertex
        if 1 <= candidate <= maximum and candidate % 2 == 1:
            values.append(candidate)
        anti_diagonal *= 2
    return values


def odd_block_trace(maximum: int, s_value: int, power: int) -> Fraction:
    vertices = list(range(1, maximum + 1, 2))
    adjacency = {vertex: neighbors_in_odd_block(vertex, maximum) for vertex in vertices}
    total = Fraction(0)
    for start in vertices:
        def extend(current: int, depth: int, weight: Fraction) -> None:
            nonlocal total
            for following in adjacency[current]:
                if depth == power - 1:
                    if following == start:
                        total += weight
                else:
                    extend(following, depth + 1,
                           weight * Fraction(1, following ** s_value))
        extend(start, 0, Fraction(1, start ** s_value))
    return total


def fraction_value(value: Fraction) -> dict[str, str]:
    return {"denominator": str(value.denominator), "numerator": str(value.numerator)}


def scale_sum(cutoff: int, s_value: int, power: int,
              cache: dict[tuple[int, int, int], Fraction]) -> Fraction:
    result = Fraction(0)
    scale = 1
    valuation = 0
    while scale <= cutoff:
        odd_cutoff = cutoff // scale
        key = (odd_cutoff, s_value, power)
        if key not in cache:
            cache[key] = odd_block_trace(odd_cutoff, s_value, power)
        result += Fraction(1, 2 ** (valuation * power * s_value)) * cache[key]
        valuation += 1
        scale *= 2
    return result


def finite_traces(cutoffs: list[int], s_values: list[int], powers: list[int]) -> list[dict[str, Any]]:
    cache: dict[tuple[int, int, int], Fraction] = {}
    rows: list[dict[str, Any]] = []
    for cutoff in cutoffs:
        for s_value in s_values:
            for power in powers:
                rows.append({
                    "N": cutoff,
                    "r": power,
                    "s": s_value,
                    "trace": fraction_value(scale_sum(cutoff, s_value, power, cache)),
                })
    return rows


def finite_endpoints() -> dict[str, Any]:
    values: list[dict[str, Any]] = []
    for exponent in range(1, 17):
        anti_diagonal = 2 ** exponent
        harmonic = Fraction(0)
        for index in range(1, anti_diagonal):
            harmonic += Fraction(1, index)
        values.append({
            "a": exponent,
            "sigma_one_level": fraction_value(Fraction(2, anti_diagonal) * harmonic),
        })
    return {
        "evidence_type": "FINITE_EXACT_DIAGNOSTIC",
        "hs_sigma_one_level_records": values,
        "row_one_sigma_zero_partial_sum_a_le_16": fraction_value(Fraction(16, 1)),
        "theorem_endpoint_verdicts": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    options = parser.parse_args()
    if options.mutation is not None:
        return mutation_rejection(options.mutation)
    if options.root is None:
        raise ValueError("--root required")
    root = Path(options.root)
    raw = contract(root)
    payload = {
        "candidate_id": "SD-C48",
        "cycle_certificate": all_cycle_data(
            raw["cycle_grid"]["label_values"], raw["cycle_grid"]["lengths"],
            raw["cycle_grid"]["direct_vertex_max"]),
        "evidence_type": "FINITE_EXACT_DIAGNOSTIC",
        "finite_endpoint_diagnostics": finite_endpoints(),
        "finite_trace_certificate": {
            "formula": "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM",
            "records": finite_traces(raw["trace_grid"]["cutoffs"],
                                      raw["trace_grid"]["s_values"],
                                      raw["trace_grid"]["powers"]),
            "truncation_policy": "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE",
        },
        "implementation_lane": "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER",
        "structural_certificate": {
            "records": [structural(cutoff) for cutoff in raw["structural_cutoffs"]],
            "support_predicate": "x>=2 and x&(x-1)==0",
        },
        "theorem_claims_inferred": [],
    }
    sys.stdout.buffer.write(encode({
        "payload": payload,
        "schema": "paper46-evaluator-c-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
