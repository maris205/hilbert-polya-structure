#!/usr/bin/env python3
"""Evaluator B: independent chain/Perron/Binet/cyclotomic route.

No project-local module is imported and no Evaluator A artifact is read.
"""

from __future__ import annotations

import argparse
import hashlib
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
    "MUT-NOSUB/d_equals_c": "PERRON_SUBTRACTION_MISSING",
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


def safe_raw_path(root: Path) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    relative_parts = ("preauthority", "RAW_INPUT_MANIFEST.json")
    cursor = root
    for part in relative_parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink input forbidden")
    resolved_root = root.resolve(strict=True)
    resolved = cursor.resolve(strict=True)
    if resolved != resolved_root / "preauthority" / "RAW_INPUT_MANIFEST.json":
        raise ValueError("input escaped root")
    return resolved


def mutation_rejection(instance_id: str) -> int:
    code = MUTATIONS.get(instance_id)
    if code is None:
        raise ValueError("mutation is not designated for Evaluator B")
    witness = {
        "MUT-Q1/q_equals_one": "valuation and chain histogram reject radix one",
        "MUT-A0/zero_2x2": "strong connectivity test fails",
        "MUT-APR/reducible_identity_2x2": "directed graph is not strongly connected",
        "MUT-APR/period_two_2x2": "cycle-length gcd is two",
        "MUT-EDGE/additive_n_plus_q": "closed q-chain histogram no longer represents source edges",
        "MUT-PREFIX/zero_based_half_open": "histogram vertex sum ceases to equal the declared cutoff",
        "MUT-NOSUB/d_equals_c": "nonzero Perron limit destroys absolute summability",
        "MUT-MODFLOOR/floor_quotient": "summation-by-parts coefficient fails at q=2,N=3,j=1",
        "MUT-MODFRAC/unnormalized_real_fractional_part": "residue coordinate is no longer an integer type",
        "MUT-REP/no_q_power": "zero digit stream produces a bounded representative",
        "MUT-RSIGN/positive_t": "positive-Binet-mode parity contradicts gamma_1",
        "MUT-LOGSIGN/positive_coefficients": "positive log series reverses the Binet coefficient",
        "MUT-TAIL/finite_samples_only": "Binet truncation lacks its geometric tail bound",
        "MUT-POLELEVEL/only_w_equals_v": "coefficient requires all w>=v levels",
        "MUT-RADIALXI/xi_over_one_minus_xi": "P_4(i)=-4/(1-i), not the superseded bracket",
    }[instance_id]
    sys.stdout.buffer.write(canonical({
        "payload": {
            "code": code,
            "consumer": "B",
            "instance_id": instance_id,
            "witness": witness,
        },
        "schema": "paper44-mutation-rejection-v1",
        "status": "REJECT",
    }))
    return 2


def reachable(flat: tuple[int, ...], dimension: int, reverse: bool) -> set[int]:
    seen = {0}
    stack = [0]
    while stack:
        source = stack.pop()
        for target in range(dimension):
            edge = flat[target * dimension + source] if reverse \
                else flat[source * dimension + target]
            if edge and target not in seen:
                seen.add(target)
                stack.append(target)
    return seen


def primitive_by_graph_period(flat: tuple[int, ...], dimension: int) -> bool:
    if len(reachable(flat, dimension, False)) != dimension \
            or len(reachable(flat, dimension, True)) != dimension:
        return False
    distance: list[int | None] = [None] * dimension
    distance[0] = 0
    queue = [0]
    for source in queue:
        for target in range(dimension):
            if flat[source * dimension + target] and distance[target] is None:
                distance[target] = distance[source] + 1  # type: ignore[operator]
                queue.append(target)
    period = 0
    for source in range(dimension):
        for target in range(dimension):
            if flat[source * dimension + target]:
                difference = int(distance[source]) + 1 - int(distance[target])
                period = math.gcd(period, abs(difference))
    return period == 1


def matrix_stream(configuration: dict[str, Any]) -> list[tuple[int, ...]]:
    dimension = configuration["dimension"]
    if configuration["generator"] == "explicit_matrix":
        value = tuple(configuration["matrix_row_major"])
        if len(value) != dimension * dimension:
            raise ValueError("explicit matrix shape")
        return [value]
    if configuration["generator"] != "all_primitive_zero_one_matrices_in_lexicographic_row_major_order":
        raise ValueError("matrix generator")
    width = dimension * dimension
    answer = []
    for encoded in range(2 ** width):
        value = tuple((encoded >> (width - index - 1)) & 1 for index in range(width))
        if primitive_by_graph_period(value, dimension):
            answer.append(value)
    return answer


def maximum_n(configuration: dict[str, Any], cap: int) -> int:
    explicit = configuration.get("max_N")
    if explicit is not None:
        return explicit
    dimension = configuration["dimension"]
    current_power = dimension
    cutoff = 1
    while current_power * dimension <= cap:
        current_power *= dimension
        cutoff += 1
    return cutoff


def expand(raw: dict[str, Any]) -> list[tuple[int, int, tuple[int, ...], int]]:
    table: dict[tuple[int, int, tuple[int, ...], int], None] = {}
    for configuration in raw["source_configurations"]:
        dimension = configuration["dimension"]
        for matrix in matrix_stream(configuration):
            for q in configuration["q_values"]:
                for cutoff in range(1, maximum_n(configuration, raw["assignment_cap"]) + 1):
                    table[(q, dimension, matrix, cutoff)] = None
    return sorted(table)


def classify(q: int, dimension: int, matrix: tuple[int, ...]) -> tuple[str, str]:
    if q < 2:
        return "REJECTED_SCOPE", "INVALID_RADIX"
    if sum(matrix) == 0:
        return "REJECTED_SCOPE", "NONPRIMITIVE_ZERO_ADJACENCY"
    if not primitive_by_graph_period(matrix, dimension):
        return "REJECTED_SCOPE", "STOP_SCOPED"
    return "VALID", "THEOREM_DOMAIN"


def word_counts(matrix: tuple[int, ...], dimension: int, maximum_length: int) -> list[int]:
    counts = [1]
    row = [1] * dimension
    counts.append(sum(row))
    for _ in range(1, maximum_length):
        next_row = [sum(row[left] * matrix[left * dimension + right]
                        for left in range(dimension))
                    for right in range(dimension)]
        row = next_row
        counts.append(sum(row))
    return counts


def chain_product(q: int, dimension: int, matrix: tuple[int, ...], cutoff: int) -> int:
    if cutoff == 0:
        return 1
    maximum_length = 1
    power = 1
    while power * q <= cutoff:
        power *= q
        maximum_length += 1
    words = word_counts(matrix, dimension, maximum_length)
    total = 1
    vertex_check = 0
    q_power = 1
    for length in range(1, maximum_length + 1):
        next_power = q_power * q
        next_next = next_power * q
        histogram = cutoff // q_power - 2 * (cutoff // next_power) \
            + cutoff // next_next
        if histogram < 0:
            raise ValueError("negative chain histogram")
        total *= words[length] ** histogram
        vertex_check += length * histogram
        q_power = next_power
    if vertex_check != cutoff:
        raise ValueError("chain histogram vertex count")
    return total


def make_finite(cases: list[tuple[int, int, tuple[int, ...], int]]) -> list[dict[str, Any]]:
    memo: dict[tuple[int, int, tuple[int, ...], int], int] = {}
    answer = []
    for q, dimension, matrix, cutoff in cases:
        status, scope = classify(q, dimension, matrix)
        identifier = f"F|q={q}|d={dimension}|a={''.join(str(bit) for bit in matrix)}|N={cutoff}"
        if status != "VALID":
            answer.append({
                "N": cutoff, "case_id": identifier, "dimension": dimension,
                "matrix_row_major": list(matrix), "q": q,
                "ratio_denominator": 0, "ratio_numerator": 0,
                "scope_code": scope, "status": status, "z_n": 0,
            })
            continue
        def lookup(index: int) -> int:
            key = (q, dimension, matrix, index)
            if key not in memo:
                memo[key] = chain_product(q, dimension, matrix, index)
            return memo[key]
        current, previous = lookup(cutoff), lookup(cutoff - 1)
        divisor = math.gcd(current, previous)
        answer.append({
            "N": cutoff, "case_id": identifier, "dimension": dimension,
            "matrix_row_major": list(matrix), "q": q,
            "ratio_denominator": previous // divisor,
            "ratio_numerator": current // divisor,
            "scope_code": scope, "status": status, "z_n": current,
        })
    return answer


def residues() -> list[dict[str, Any]]:
    output = []
    for q in [2, 3, 4, 6]:
        for cutoff in list(range(1, 25)):
            for index in list(range(0, 13)):
                quotient = cutoff // (q ** index)
                next_quotient = cutoff // (q ** (index + 1))
                left = Fraction(quotient - next_quotient, 1) \
                    - Fraction(cutoff * (q - 1), q ** (index + 1))
                residue_here = cutoff - quotient * (q ** index)
                residue_next = cutoff - next_quotient * (q ** (index + 1))
                right = Fraction(residue_next, q) if index == 0 else \
                    -Fraction(residue_here, q ** index) \
                    + Fraction(residue_next, q ** (index + 1))
                if left != right:
                    raise ValueError("independent residue identity")
                output.append({
                    "N": cutoff,
                    "case_id": f"C|q={q}|N={cutoff}|j={index}",
                    "coefficient_denominator": str(left.denominator),
                    "coefficient_index": index,
                    "coefficient_numerator": str(left.numerator),
                    "q": q,
                })
    return output


def digits(raw: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    formulas = {
        "all_zero_digits": lambda q, j: 0,
        "all_maximal_digits": lambda q, j: q - 1,
        "alternating_zero_maximal_digits": lambda q, j: (q - 1) * (j % 2),
        "polynomial_digits_a_j_equal_j_squared_plus_j_plus_one_mod_q":
            lambda q, j: (j * j + j + 1) - q * ((j * j + j + 1) // q),
    }
    for name in sorted(formulas):
        for q in [2, 3, 4, 6]:
            prefix: list[int] = []
            for depth in range(1, 11):
                next_digit = formulas[name](q, depth - 1)
                prefix.append(next_digit)
                residue = sum(value * q ** position for position, value in enumerate(prefix))
                representative = q ** depth + residue
                compatibility = True
                for level in range(1, depth + 1):
                    compatibility = compatibility and \
                        representative % (q ** level) == \
                        sum(prefix[position] * q ** position
                            for position in range(level))
                output.append({
                    "case_id": f"D|stream={name}|q={q}|depth={depth}",
                    "compatible_all_levels": compatibility,
                    "depth": depth,
                    "digit": next_digit,
                    "lower_bound_met": representative >= q ** depth,
                    "q": q,
                    "representative": representative,
                    "residue": residue,
                    "stream": name,
                })
    return output


Interval = tuple[Fraction, Fraction]


def iadd(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def ineg(value: Interval) -> Interval:
    return -value[1], -value[0]


def isub(left: Interval, right: Interval) -> Interval:
    return iadd(left, ineg(right))


def imul(left: Interval, right: Interval) -> Interval:
    choices = [left[0] * right[0], left[0] * right[1],
               left[1] * right[0], left[1] * right[1]]
    return min(choices), max(choices)


def idiv(left: Interval, right: Interval) -> Interval:
    if right[0] <= 0 <= right[1]:
        raise ValueError("interval division by zero")
    return imul(left, (1 / right[1], 1 / right[0]))


def ipow(value: Interval, exponent: int) -> Interval:
    result: Interval = (Fraction(1), Fraction(1))
    base = value
    power = exponent
    while power:
        if power & 1:
            result = imul(result, base)
        base = imul(base, base)
        power //= 2
    return result


def sqrt5_bounds(bits: int) -> Interval:
    digits_count = bits * 30103 // 100000 + 14
    scale = 10 ** digits_count
    lower_integer = math.isqrt(5 * scale * scale)
    lower = Fraction(lower_integer, scale)
    upper = Fraction(lower_integer + 1, scale)
    if not lower * lower <= 5 < upper * upper:
        raise ValueError("sqrt bracket")
    return lower, upper


def gamma_binet_interval(index: int, bits: int) -> tuple[Fraction, Fraction, Fraction, int]:
    scale = 2 ** (bits + 48)

    def down(value: Fraction) -> Fraction:
        return Fraction((value.numerator * scale) // value.denominator, scale)

    def up(value: Fraction) -> Fraction:
        return Fraction(-((-value.numerator * scale) // value.denominator), scale)

    def quantize(value: Interval) -> Interval:
        return down(value[0]), up(value[1])

    def add(left: Interval, right: Interval) -> Interval:
        return quantize((left[0] + right[0], left[1] + right[1]))

    def subtract(left: Interval, right: Interval) -> Interval:
        return quantize((left[0] - right[1], left[1] - right[0]))

    def multiply(left: Interval, right: Interval) -> Interval:
        choices = [left[0] * right[0], left[0] * right[1],
                   left[1] * right[0], left[1] * right[1]]
        return quantize((min(choices), max(choices)))

    def divide(left: Interval, right: Interval) -> Interval:
        if right[0] <= 0 <= right[1]:
            raise ValueError("interval division by zero")
        return multiply(left, (1 / right[1], 1 / right[0]))

    def power(value: Interval, exponent_value: int) -> Interval:
        result: Interval = (Fraction(1), Fraction(1))
        base = quantize(value)
        remaining = exponent_value
        while remaining:
            if remaining & 1:
                result = multiply(result, base)
            base = multiply(base, base)
            remaining //= 2
        return result

    sqrt_lower, sqrt_upper = sqrt5_bounds(bits)
    t: Interval = quantize(((Fraction(3) - sqrt_upper) / 2,
                            (Fraction(3) - sqrt_lower) / 2))
    r: Interval = (-t[1], -t[0])
    truncation = bits // 2 + 20
    total: Interval = (Fraction(0), Fraction(0))
    one: Interval = (Fraction(1), Fraction(1))
    two: Interval = (Fraction(2), Fraction(2))
    for mode in range(1, truncation + 1):
        r_mode = power(r, mode)
        numerator = power(subtract(one, r_mode), 2)
        denominator = multiply((Fraction(mode), Fraction(mode)), subtract(two, r_mode))
        coefficient = divide(numerator, denominator)
        total = add(total, multiply(coefficient, power(r_mode, index + 2)))
    t_upper = t[1]
    exponent = (truncation + 1) * (index + 2)
    tail_power = power((t_upper, t_upper), exponent)[1]
    short_power = power((t_upper, t_upper), index + 2)[1]
    tail = up(Fraction(2) * tail_power
              / (Fraction(truncation + 1) * (1 - short_power)))
    return total[0] - tail, total[1] + tail, tail, truncation


def gamma_rows(bits_values: list[int]) -> list[dict[str, Any]]:
    rows = []
    for bits in bits_values:
        for index in range(11):
            lower, upper, tail, truncation = gamma_binet_interval(index, bits)
            scale = 2 ** (bits + 16)
            lower = Fraction((lower.numerator * scale) // lower.denominator, scale)
            upper = Fraction(-((-upper.numerator * scale) // upper.denominator), scale)
            tail = Fraction(-((-tail.numerator * scale) // tail.denominator), scale)
            rows.append({
                "bits": bits,
                "case_id": f"G|k={index}|bits={bits}",
                "certificate_id": "B_POSITIVE_BINET_Q_SQRT5_GEOMETRIC_TAIL",
                "index": index,
                "lower_denominator": str(lower.denominator),
                "lower_numerator": str(lower.numerator),
                "method": "positive_binet_interval",
                "tail_bound_denominator": str(tail.denominator),
                "tail_bound_numerator": str(tail.numerator),
                "truncation_index": truncation,
                "upper_denominator": str(upper.denominator),
                "upper_numerator": str(upper.numerator),
            })
    return rows


def cyclotomic_identity(order: int) -> bool:
    half = order // 2
    polynomial = [0] * (order + 1)
    polynomial[0] += order
    for exponent in range(order):
        polynomial[exponent] += exponent
        polynomial[exponent + 1] -= exponent
    reduced = [0] * half
    for exponent, coefficient in enumerate(polynomial):
        quotient, remainder = divmod(exponent, half)
        reduced[remainder] += coefficient if quotient % 2 == 0 else -coefficient
    return all(value == 0 for value in reduced)


def radial() -> list[dict[str, Any]]:
    output = []
    for level in range(1, 11):
        order = 2 ** level
        output.append({
            "Q": order,
            "case_id": f"R|v={level}|Q={order}",
            "coefficient_form": "-gamma_(v-1)/(2^(v-1)*(1-xi))",
            "finite_cyclotomic_identity": cyclotomic_identity(order),
            "gamma_index": level - 1,
            "included_level_rule": "all_w_at_least_v",
            "scale_denominator": 2 ** (level - 1),
            "v": level,
        })
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation is not None:
        return mutation_rejection(arguments.mutation)
    if arguments.root is None:
        raise ValueError("--root required")
    path = safe_raw_path(Path(arguments.root))
    raw_bytes = path.read_bytes()
    if digest(raw_bytes) != RAW_SHA256:
        raise ValueError("raw hash")
    raw = json.loads(raw_bytes.decode("ascii"), object_pairs_hook=unique)
    if raw.get("contains_expected_outputs") is not False \
            or raw.get("fixture_expansion_shared") is not False:
        raise ValueError("nonneutral raw manifest")
    finite = make_finite(expand(raw))
    valid = sum(1 for row in finite if row["status"] == "VALID")
    rejected = len(finite) - valid
    value = {
        "payload": {
            "algebraic_certificate": {
                "difference_denominator": 220,
                "difference_rational_part": 6557,
                "difference_sqrt5_coefficient": -2929,
                "square_difference": pow(6557, 2) - 5 * pow(2929, 2),
                "strictly_positive": pow(6557, 2) - 5 * pow(2929, 2) > 0,
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
            "gamma_intervals": gamma_rows(raw["precision_bits"]),
            "implementation": {
                "algorithm": "closed_chain_histogram_integer_word_counts",
                "fixture_expander": "integer_bitstream_and_graph_period_primitivity",
                "project_local_imports": [],
            },
            "radial_records": radial(),
            "representative_records": digits(raw),
            "residue_records": residues(),
        },
        "schema": "paper44-evaluator-b-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
