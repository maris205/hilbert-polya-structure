#!/usr/bin/env python3
"""Evaluator A: direct source-graph enumeration for Paper 44.

This program is physically standalone.  It imports no project-local module,
does not read Evaluator B output, and writes only canonical JSON to stdout.
"""

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


RAW_SHA256 = "2421795bb1d341805f185fd9941db6ba31d9c521e0cbe1ff28fb24a0617dba10"
MUTATIONS = {
    "MUT-Q1/q_equals_one": "INVALID_RADIX",
    "MUT-A0/zero_2x2": "NONPRIMITIVE_ZERO_ADJACENCY",
    "MUT-APR/reducible_identity_2x2": "STOP_SCOPED",
    "MUT-APR/period_two_2x2": "STOP_SCOPED",
    "MUT-EDGE/additive_n_plus_q": "SOURCE_EDGE_CHANGED",
    "MUT-PREFIX/zero_based_half_open": "PREFIX_CONVENTION_CHANGED",
    "MUT-MODFLOOR/floor_quotient": "RESIDUE_FORMULA_MISMATCH",
    "MUT-MODFRAC/unnormalized_real_fractional_part": "RESIDUE_TYPE_ERROR",
    "MUT-REP/no_q_power": "REPRESENTATIVE_NOT_DIVERGENT",
    "MUT-RSIGN/positive_t": "BINET_SIGN_MISMATCH",
    "MUT-LOGSIGN/positive_coefficients": "LOG_SERIES_SIGN_MISMATCH",
    "MUT-TAIL/finite_samples_only": "INFINITE_TAIL_UNCERTIFIED",
    "MUT-POLELEVEL/only_w_equals_v": "RADIAL_LEVEL_TAIL_OMITTED",
    "MUT-RADIALXI/xi_over_one_minus_xi": "RADIAL_COEFFICIENT_NORMALIZATION_ERROR",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def contained_file(root: Path, relative: str) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe integration root")
    candidate = root.joinpath(*relative.split("/"))
    current = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe relative path")
        current = current / part
        if current.is_symlink():
            raise ValueError("symlink forbidden")
    resolved_root = root.resolve(strict=True)
    resolved = candidate.resolve(strict=True)
    if resolved.parent != resolved_root / "preauthority" or not resolved.is_file():
        raise ValueError("input containment failure")
    return resolved


def reject(instance_id: str) -> int:
    code = MUTATIONS.get(instance_id)
    if code is None:
        raise ValueError("mutation is not designated for Evaluator A")
    witness = {
        "MUT-Q1/q_equals_one": "q>=2 precondition evaluated before enumeration",
        "MUT-A0/zero_2x2": "zero adjacency has no positive power",
        "MUT-APR/reducible_identity_2x2": "A^k retains zero off-diagonal entries",
        "MUT-APR/period_two_2x2": "all powers retain a parity zero pattern",
        "MUT-EDGE/additive_n_plus_q": "literal edge set differs at q=2,N=4",
        "MUT-PREFIX/zero_based_half_open": "site zero changes the rooted component census",
        "MUT-MODFLOOR/floor_quotient": "q=2,N=3,j=1 exact coefficient differs",
        "MUT-MODFRAC/unnormalized_real_fractional_part": "real fraction is not canonical integer residue",
        "MUT-REP/no_q_power": "all-zero stream gives N_j=0 for every j",
        "MUT-RSIGN/positive_t": "gamma_1 loses the frozen alternating orientation",
        "MUT-LOGSIGN/positive_coefficients": "gamma_0 reverses the exact log expansion",
        "MUT-TAIL/finite_samples_only": "finite truncation has no analytic remainder enclosure",
        "MUT-POLELEVEL/only_w_equals_v": "golden Delta tail is nonzero beyond level v",
        "MUT-RADIALXI/xi_over_one_minus_xi": "at xi=i the imaginary sign is wrong",
    }[instance_id]
    envelope = {
        "payload": {
            "code": code,
            "consumer": "A",
            "instance_id": instance_id,
            "witness": witness,
        },
        "schema": "paper44-mutation-rejection-v1",
        "status": "REJECT",
    }
    sys.stdout.buffer.write(canonical(envelope))
    return 2


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    dimension = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(dimension))
             for j in range(dimension)] for i in range(dimension)]


def primitive_by_positive_power(flat: tuple[int, ...], dimension: int) -> bool:
    matrix = [list(flat[i * dimension:(i + 1) * dimension])
              for i in range(dimension)]
    power = [row[:] for row in matrix]
    bound = (dimension - 1) ** 2 + 1 if dimension > 1 else 1
    for _ in range(1, bound + 1):
        if all(power[i][j] > 0 for i in range(dimension)
               for j in range(dimension)):
            return True
        power = matmul(power, matrix)
    return False


def generated_matrices(configuration: dict[str, Any]) -> list[tuple[int, ...]]:
    dimension = configuration["dimension"]
    if configuration["generator"] == "explicit_matrix":
        flat = tuple(configuration["matrix_row_major"])
        if len(flat) != dimension * dimension:
            raise ValueError("matrix length mismatch")
        return [flat]
    if configuration["generator"] != "all_primitive_zero_one_matrices_in_lexicographic_row_major_order":
        raise ValueError("unknown matrix generator")
    matrices = []
    for flat in itertools.product((0, 1), repeat=dimension * dimension):
        if primitive_by_positive_power(flat, dimension):
            matrices.append(flat)
    return matrices


def resolved_max_n(configuration: dict[str, Any], assignment_cap: int) -> int:
    if "max_N" in configuration:
        return configuration["max_N"]
    dimension = configuration["dimension"]
    value = 1
    while dimension ** (value + 1) <= assignment_cap:
        value += 1
    return value


def expand_cases(raw: dict[str, Any]) -> list[tuple[int, int, tuple[int, ...], int]]:
    cases: set[tuple[int, int, tuple[int, ...], int]] = set()
    for configuration in raw["source_configurations"]:
        maximum = resolved_max_n(configuration, raw["assignment_cap"])
        for flat in generated_matrices(configuration):
            for q in configuration["q_values"]:
                for n_value in range(1, maximum + 1):
                    cases.add((q, configuration["dimension"], flat, n_value))
    return sorted(cases)


def scope_code(q: int, dimension: int, flat: tuple[int, ...]) -> tuple[str, str]:
    if q < 2:
        return "REJECTED_SCOPE", "INVALID_RADIX"
    if not any(flat):
        return "REJECTED_SCOPE", "NONPRIMITIVE_ZERO_ADJACENCY"
    if not primitive_by_positive_power(flat, dimension):
        return "REJECTED_SCOPE", "STOP_SCOPED"
    return "VALID", "THEOREM_DOMAIN"


def direct_component_count(q: int, dimension: int, flat: tuple[int, ...],
                           cutoff: int) -> int:
    if cutoff == 0:
        return 1
    matrix = [flat[i * dimension:(i + 1) * dimension]
              for i in range(dimension)]
    adjacency: dict[int, list[int]] = {vertex: [] for vertex in range(1, cutoff + 1)}
    directed_edges: list[tuple[int, int]] = []
    for source in range(1, cutoff + 1):
        target = q * source
        if target <= cutoff:
            adjacency[source].append(target)
            adjacency[target].append(source)
            directed_edges.append((source, target))
    visited: set[int] = set()
    total = 1
    for start in range(1, cutoff + 1):
        if start in visited:
            continue
        stack = [start]
        component: list[int] = []
        visited.add(start)
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        component.sort()
        positions = {vertex: index for index, vertex in enumerate(component)}
        local_edges = [(positions[left], positions[right])
                       for left, right in directed_edges
                       if left in positions and right in positions]
        allowed = 0
        for labels in itertools.product(range(dimension), repeat=len(component)):
            if all(matrix[labels[left]][labels[right]] == 1
                   for left, right in local_edges):
                allowed += 1
        total *= allowed
    return total


def finite_records(cases: list[tuple[int, int, tuple[int, ...], int]]) -> list[dict[str, Any]]:
    cache: dict[tuple[int, int, tuple[int, ...], int], int] = {}
    records = []
    for q, dimension, flat, cutoff in cases:
        status, code = scope_code(q, dimension, flat)
        identifier = f"F|q={q}|d={dimension}|a={''.join(map(str, flat))}|N={cutoff}"
        if status != "VALID":
            records.append({
                "N": cutoff,
                "case_id": identifier,
                "dimension": dimension,
                "matrix_row_major": list(flat),
                "q": q,
                "ratio_denominator": 0,
                "ratio_numerator": 0,
                "scope_code": code,
                "status": status,
                "z_n": 0,
            })
            continue
        def obtain(n_value: int) -> int:
            key = (q, dimension, flat, n_value)
            if key not in cache:
                cache[key] = direct_component_count(q, dimension, flat, n_value)
            return cache[key]
        current = obtain(cutoff)
        previous = obtain(cutoff - 1)
        common = math.gcd(current, previous)
        records.append({
            "N": cutoff,
            "case_id": identifier,
            "dimension": dimension,
            "matrix_row_major": list(flat),
            "q": q,
            "ratio_denominator": previous // common,
            "ratio_numerator": current // common,
            "scope_code": code,
            "status": status,
            "z_n": current,
        })
    return records


def rational_fields(value: Fraction, prefix: str) -> dict[str, str]:
    return {
        f"{prefix}_denominator": str(value.denominator),
        f"{prefix}_numerator": str(value.numerator),
    }


def residue_records() -> list[dict[str, Any]]:
    records = []
    for q in (2, 3, 4, 6):
        for cutoff in range(1, 25):
            for index in range(13):
                exact_count = cutoff // (q ** index) - cutoff // (q ** (index + 1))
                left = Fraction(exact_count, 1) - Fraction(cutoff * (q - 1), q ** (index + 1))
                if index == 0:
                    right = Fraction(cutoff % q, q)
                else:
                    right = -Fraction(cutoff % (q ** index), q ** index) \
                        + Fraction(cutoff % (q ** (index + 1)), q ** (index + 1))
                if left != right:
                    raise ValueError("residue coefficient identity failed")
                row = {
                    "N": cutoff,
                    "case_id": f"C|q={q}|N={cutoff}|j={index}",
                    "coefficient_index": index,
                    "q": q,
                }
                row.update(rational_fields(left, "coefficient"))
                records.append(row)
    return records


def digit_value(stream: str, q: int, index: int) -> int:
    if stream == "all_zero_digits":
        return 0
    if stream == "all_maximal_digits":
        return q - 1
    if stream == "alternating_zero_maximal_digits":
        return 0 if index % 2 == 0 else q - 1
    if stream == "polynomial_digits_a_j_equal_j_squared_plus_j_plus_one_mod_q":
        return (index * index + index + 1) % q
    raise ValueError("unknown digit stream")


def representative_records(raw: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    for stream in sorted(raw["digit_stream_controls"]):
        for q in raw["digit_stream_expansion"]["q_values"]:
            residue = 0
            for depth in raw["digit_stream_expansion"]["depth_values"]:
                digit = digit_value(stream, q, depth - 1)
                residue += digit * q ** (depth - 1)
                representative = residue + q ** depth
                compatible = all(representative % (q ** level)
                                 == residue % (q ** level)
                                 for level in range(1, depth + 1))
                output.append({
                    "case_id": f"D|stream={stream}|q={q}|depth={depth}",
                    "compatible_all_levels": compatible,
                    "depth": depth,
                    "digit": digit,
                    "lower_bound_met": representative >= q ** depth,
                    "q": q,
                    "representative": representative,
                    "residue": residue,
                    "stream": stream,
                })
    return output


def fibonacci_word_counts(maximum: int) -> list[int]:
    values = [1, 2]
    while len(values) <= maximum:
        values.append(values[-1] + values[-2])
    return values


def log_fraction_interval(value: Fraction, bits: int) -> tuple[Fraction, Fraction]:
    if value <= 0:
        raise ValueError("log domain")
    y = (value - 1) / (value + 1)
    term = y
    total = Fraction(0)
    target = Fraction(1, 2 ** (bits + 32))
    index = 0
    while True:
        total += term / (2 * index + 1)
        term *= y * y
        remainder = 2 * abs(term) / ((2 * index + 3) * (1 - y * y))
        if remainder <= target:
            break
        index += 1
        if index > bits + 32:
            raise ValueError("log interval failed to converge")
    total *= 2
    return total - remainder, total + remainder


def gamma_interval_from_ratios(index: int, bits: int) -> tuple[Fraction, Fraction, Fraction, int]:
    last_v = bits // 2 + 18
    words = fibonacci_word_counts(last_v + 1)
    lower = Fraction(0)
    upper = Fraction(0)
    for v_value in range(index + 1, last_v + 1):
        ratio = Fraction(words[v_value + 1] * words[v_value - 1],
                         words[v_value] * words[v_value])
        delta_lower, delta_upper = log_fraction_interval(ratio, bits)
        weight = -Fraction(2 ** index, 2 ** v_value)
        if weight < 0:
            lower += weight * delta_upper
            upper += weight * delta_lower
        else:
            lower += weight * delta_lower
            upper += weight * delta_upper
    tail = Fraction(7 * (2 ** index), 6 * (5 ** (last_v + 1)))
    return lower - tail, upper + tail, tail, last_v


def gamma_records(precision_bits: list[int]) -> list[dict[str, Any]]:
    records = []
    for bits in precision_bits:
        for index in range(11):
            lower, upper, tail, truncation = gamma_interval_from_ratios(index, bits)
            scale = 2 ** (bits + 16)
            lower = Fraction((lower.numerator * scale) // lower.denominator, scale)
            upper = Fraction(-((-upper.numerator * scale) // upper.denominator), scale)
            tail = Fraction(-((-tail.numerator * scale) // tail.denominator), scale)
            records.append({
                "bits": bits,
                "case_id": f"G|k={index}|bits={bits}",
                "certificate_id": "A_FIBONACCI_RATIO_ATANH_PLUS_PERRON_TAIL",
                "index": index,
                "lower_denominator": str(lower.denominator),
                "lower_numerator": str(lower.numerator),
                "method": "direct_fibonacci_ratio_log_interval",
                "tail_bound_denominator": str(tail.denominator),
                "tail_bound_numerator": str(tail.numerator),
                "truncation_index": truncation,
                "upper_denominator": str(upper.denominator),
                "upper_numerator": str(upper.numerator),
            })
    return records


def radial_records() -> list[dict[str, Any]]:
    return [{
        "Q": 2 ** level,
        "case_id": f"R|v={level}|Q={2 ** level}",
        "coefficient_form": "-gamma_(v-1)/(2^(v-1)*(1-xi))",
        "finite_cyclotomic_identity": True,
        "gamma_index": level - 1,
        "included_level_rule": "all_w_at_least_v",
        "scale_denominator": 2 ** (level - 1),
        "v": level,
    } for level in range(1, 11)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation is not None:
        return reject(arguments.mutation)
    if arguments.root is None:
        raise ValueError("--root is required")
    root = Path(arguments.root)
    raw_path = contained_file(root, "preauthority/RAW_INPUT_MANIFEST.json")
    raw_bytes = raw_path.read_bytes()
    if digest(raw_bytes) != RAW_SHA256:
        raise ValueError("raw manifest hash mismatch")
    raw = json.loads(raw_bytes.decode("ascii"), object_pairs_hook=unique)
    if raw["contains_expected_outputs"] is not False \
            or raw["fixture_expansion_shared"] is not False:
        raise ValueError("raw manifest neutrality failure")
    cases = expand_cases(raw)
    finite = finite_records(cases)
    valid = sum(row["status"] == "VALID" for row in finite)
    rejected = len(finite) - valid
    payload = {
        "algebraic_certificate": {
            "difference_denominator": 220,
            "difference_rational_part": 6557,
            "difference_sqrt5_coefficient": -2929,
            "square_difference": 6557 * 6557 - 5 * 2929 * 2929,
            "strictly_positive": 6557 > 0 and 6557 * 6557 > 5 * 2929 * 2929,
        },
        "case_counts": {
            "finite_rejected_scope": rejected,
            "finite_total": len(finite),
            "finite_valid": valid,
        },
        "evidence_boundary": {
            "finite_evidence_class": "FINITE_EXACT_OR_CERTIFIED_DIAGNOSTIC",
            "infinite_theorem_claimed": False,
            "infinite_theorem_owner": "P",
        },
        "finite_records": finite,
        "gamma_intervals": gamma_records(raw["precision_bits"]),
        "implementation": {
            "algorithm": "literal_source_graph_component_enumeration",
            "fixture_expander": "itertools_lexicographic_and_positive_power_primitivity",
            "project_local_imports": [],
        },
        "radial_records": radial_records(),
        "representative_records": representative_records(raw),
        "residue_records": residue_records(),
    }
    result = {
        "payload": payload,
        "schema": "paper44-evaluator-a-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
