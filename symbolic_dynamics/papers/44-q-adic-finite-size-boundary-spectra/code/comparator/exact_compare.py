#!/usr/bin/env python3
"""Third-route exact comparator for both Paper 44 evaluator envelopes.

The comparator imports neither evaluator.  It independently expands the frozen
raw cases, reconstructs every exact finite/digit/residue/radial value, rebuilds
the certified A enclosure, checks the B tail formula, and then requires exact
schemas, runtime scalar types, identifiers, ordering, and canonical rationals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


RAW_SHA256 = "2421795bb1d341805f185fd9941db6ba31d9c521e0cbe1ff28fb24a0617dba10"
MUTATIONS = {
    "MUT-EDGE/additive_n_plus_q": "SOURCE_EDGE_CHANGED",
    "MUT-PREFIX/zero_based_half_open": "PREFIX_CONVENTION_CHANGED",
    "MUT-MODFLOOR/floor_quotient": "RESIDUE_FORMULA_MISMATCH",
    "MUT-RSIGN/positive_t": "BINET_SIGN_MISMATCH",
    "MUT-LOGSIGN/positive_coefficients": "LOG_SERIES_SIGN_MISMATCH",
    "MUT-POLELEVEL/only_w_equals_v": "RADIAL_LEVEL_TAIL_OMITTED",
    "MUT-RADIALXI/xi_over_one_minus_xi": "RADIAL_COEFFICIENT_NORMALIZATION_ERROR",
}
ENVELOPE_KEYS = {"payload", "schema", "status"}
PAYLOAD_KEYS = {
    "algebraic_certificate", "case_counts", "evidence_boundary", "finite_records",
    "gamma_intervals", "implementation", "radial_records", "representative_records",
    "residue_records",
}
FINITE_KEYS = {
    "N", "case_id", "dimension", "matrix_row_major", "q", "ratio_denominator",
    "ratio_numerator", "scope_code", "status", "z_n",
}
GAMMA_KEYS = {
    "bits", "case_id", "certificate_id", "index", "lower_denominator",
    "lower_numerator", "method", "tail_bound_denominator", "tail_bound_numerator",
    "truncation_index", "upper_denominator", "upper_numerator",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate key {key}")
        out[key] = value
    return out


def strict(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict(a, b) for a, b in zip(left, right))
    return left == right


def exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise ValueError(f"{label} exact keys")
    return value


def integer(value: Any, label: str, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError(f"{label} integer type/range")
    return value


def boolean(value: Any, label: str) -> bool:
    if type(value) is not bool:
        raise ValueError(f"{label} boolean type")
    return value


def safe_file(container: Path, supplied: str) -> Path:
    if not container.is_absolute() or container.is_symlink() or not container.is_dir():
        raise ValueError("unsafe container")
    path = Path(supplied)
    if not path.is_absolute():
        raise ValueError("input must be absolute")
    base = container.resolve(strict=True)
    cursor = path
    while cursor != base:
        if cursor == cursor.parent:
            raise ValueError("input ancestry escape")
        if cursor.is_symlink():
            raise ValueError("symlink input")
        cursor = cursor.parent
    resolved = path.resolve(strict=True)
    if base not in resolved.parents or not resolved.is_file() or resolved.is_symlink():
        raise ValueError("input containment")
    return resolved


def load_json(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value) or type(value) is not dict:
        raise ValueError("noncanonical JSON")
    return value, raw


def rational(row: dict[str, Any], prefix: str) -> Fraction:
    numerator = row.get(prefix + "_numerator")
    denominator = row.get(prefix + "_denominator")
    if type(numerator) is not str or type(denominator) is not str:
        raise ValueError("rational string type")
    if re.fullmatch(r"-?(0|[1-9][0-9]*)", numerator) is None \
            or re.fullmatch(r"[1-9][0-9]*", denominator) is None:
        raise ValueError("noncanonical rational decimal")
    if numerator == "-0":
        raise ValueError("negative zero")
    value = Fraction(int(numerator), int(denominator))
    if str(value.numerator) != numerator or str(value.denominator) != denominator:
        raise ValueError("unreduced rational")
    return value


def reachable(flat: tuple[int, ...], dimension: int, reverse: bool) -> set[int]:
    seen, stack = {0}, [0]
    while stack:
        source = stack.pop()
        for target in range(dimension):
            edge = flat[target * dimension + source] if reverse \
                else flat[source * dimension + target]
            if edge == 1 and target not in seen:
                seen.add(target)
                stack.append(target)
    return seen


def primitive(flat: tuple[int, ...], dimension: int) -> bool:
    if len(reachable(flat, dimension, False)) != dimension \
            or len(reachable(flat, dimension, True)) != dimension:
        return False
    distance: list[int | None] = [None] * dimension
    distance[0] = 0
    queue = [0]
    for source in queue:
        for target in range(dimension):
            if flat[source * dimension + target] == 1 and distance[target] is None:
                distance[target] = int(distance[source]) + 1
                queue.append(target)
    period = 0
    for source in range(dimension):
        for target in range(dimension):
            if flat[source * dimension + target] == 1:
                period = math.gcd(period, abs(int(distance[source]) + 1 - int(distance[target])))
    return period == 1


def matrices(configuration: dict[str, Any]) -> list[tuple[int, ...]]:
    d = integer(configuration.get("dimension"), "configuration dimension", 1)
    generator = configuration.get("generator")
    if generator == "explicit_matrix":
        values = configuration.get("matrix_row_major")
        if type(values) is not list or len(values) != d * d \
                or any(type(bit) is not int or bit not in (0, 1) for bit in values):
            raise ValueError("matrix encoding")
        return [tuple(values)]
    if generator != "all_primitive_zero_one_matrices_in_lexicographic_row_major_order":
        raise ValueError("matrix generator")
    answer = []
    for encoded in range(2 ** (d * d)):
        flat = tuple((encoded >> (d * d - position - 1)) & 1 for position in range(d * d))
        if primitive(flat, d):
            answer.append(flat)
    return answer


def maximum_n(configuration: dict[str, Any], cap: int) -> int:
    if "max_N" in configuration:
        return integer(configuration["max_N"], "max_N", 1)
    d = integer(configuration["dimension"], "dimension", 1)
    n, power = 1, d
    while power * d <= cap:
        power *= d
        n += 1
    return n


def expand(raw: dict[str, Any]) -> list[tuple[int, int, tuple[int, ...], int]]:
    cap = integer(raw.get("assignment_cap"), "assignment cap", 1)
    configurations = raw.get("source_configurations")
    if type(configurations) is not list:
        raise ValueError("source configurations")
    cases: set[tuple[int, int, tuple[int, ...], int]] = set()
    for configuration in configurations:
        if type(configuration) is not dict:
            raise ValueError("configuration type")
        d = integer(configuration.get("dimension"), "dimension", 1)
        qs = configuration.get("q_values")
        if type(qs) is not list or any(type(q) is not int for q in qs):
            raise ValueError("q values")
        for flat in matrices(configuration):
            for q in qs:
                for n in range(1, maximum_n(configuration, cap) + 1):
                    cases.add((q, d, flat, n))
    return sorted(cases)


def word_counts(flat: tuple[int, ...], d: int, maximum: int) -> list[int]:
    values, row = [1], [1] * d
    values.append(sum(row))
    for _ in range(1, maximum):
        row = [sum(row[left] * flat[left * d + right] for left in range(d))
               for right in range(d)]
        values.append(sum(row))
    return values


def chain_product(q: int, d: int, flat: tuple[int, ...], n: int) -> int:
    if n == 0:
        return 1
    maximum, power = 1, 1
    while power * q <= n:
        power *= q
        maximum += 1
    words = word_counts(flat, d, maximum)
    product, covered, power = 1, 0, 1
    for length in range(1, maximum + 1):
        next_power = power * q
        histogram = n // power - 2 * (n // next_power) + n // (next_power * q)
        if histogram < 0:
            raise ValueError("chain histogram")
        product *= words[length] ** histogram
        covered += length * histogram
        power = next_power
    if covered != n:
        raise ValueError("chain coverage")
    return product


def expected_finite(raw: dict[str, Any]) -> list[dict[str, Any]]:
    answer: list[dict[str, Any]] = []
    memo: dict[tuple[int, int, tuple[int, ...], int], int] = {}
    for q, d, flat, n in expand(raw):
        if q < 2:
            status, scope = "REJECTED_SCOPE", "INVALID_RADIX"
        elif sum(flat) == 0:
            status, scope = "REJECTED_SCOPE", "NONPRIMITIVE_ZERO_ADJACENCY"
        elif not primitive(flat, d):
            status, scope = "REJECTED_SCOPE", "STOP_SCOPED"
        else:
            status, scope = "VALID", "THEOREM_DOMAIN"
        identifier = f"F|q={q}|d={d}|a={''.join(str(bit) for bit in flat)}|N={n}"
        if status != "VALID":
            current, numerator, denominator = 0, 0, 0
        else:
            def get(index: int) -> int:
                key = (q, d, flat, index)
                if key not in memo:
                    memo[key] = chain_product(q, d, flat, index)
                return memo[key]
            current, previous = get(n), get(n - 1)
            divisor = math.gcd(current, previous)
            numerator, denominator = current // divisor, previous // divisor
        answer.append({
            "N": n, "case_id": identifier, "dimension": d,
            "matrix_row_major": list(flat), "q": q,
            "ratio_denominator": denominator, "ratio_numerator": numerator,
            "scope_code": scope, "status": status, "z_n": current,
        })
    return answer


def expected_residues() -> list[dict[str, Any]]:
    rows = []
    for q in (2, 3, 4, 6):
        for n in range(1, 25):
            for j in range(13):
                value = Fraction(n // (q ** j) - n // (q ** (j + 1)), 1) \
                    - Fraction(n * (q - 1), q ** (j + 1))
                rows.append({
                    "N": n, "case_id": f"C|q={q}|N={n}|j={j}",
                    "coefficient_denominator": str(value.denominator),
                    "coefficient_index": j, "coefficient_numerator": str(value.numerator),
                    "q": q,
                })
    return rows


def expected_digits(raw: dict[str, Any]) -> list[dict[str, Any]]:
    streams = raw.get("digit_stream_controls")
    expansion = raw.get("digit_stream_expansion")
    if type(streams) is not list or type(expansion) is not dict:
        raise ValueError("digit manifest")
    if not strict(expansion.get("q_values"), [2, 3, 4, 6]) \
            or not strict(expansion.get("depth_values"), list(range(1, 11))):
        raise ValueError("digit grid")
    rows = []
    for stream in sorted(streams):
        if type(stream) is not str:
            raise ValueError("digit stream id")
        for q in (2, 3, 4, 6):
            residue = 0
            for depth in range(1, 11):
                j = depth - 1
                if stream == "all_zero_digits":
                    digit = 0
                elif stream == "all_maximal_digits":
                    digit = q - 1
                elif stream == "alternating_zero_maximal_digits":
                    digit = (q - 1) * (j % 2)
                elif stream == "polynomial_digits_a_j_equal_j_squared_plus_j_plus_one_mod_q":
                    digit = (j * j + j + 1) % q
                else:
                    raise ValueError("unknown digit stream")
                residue += digit * q ** j
                representative = q ** depth + residue
                rows.append({
                    "case_id": f"D|stream={stream}|q={q}|depth={depth}",
                    "compatible_all_levels": all(representative % q ** level
                                                   == residue % q ** level
                                                   for level in range(1, depth + 1)),
                    "depth": depth, "digit": digit,
                    "lower_bound_met": representative >= q ** depth,
                    "q": q, "representative": representative,
                    "residue": residue, "stream": stream,
                })
    return rows


def expected_radial() -> list[dict[str, Any]]:
    return [{
        "Q": 2 ** v, "case_id": f"R|v={v}|Q={2 ** v}",
        "coefficient_form": "-gamma_(v-1)/(2^(v-1)*(1-xi))",
        "finite_cyclotomic_identity": True, "gamma_index": v - 1,
        "included_level_rule": "all_w_at_least_v", "scale_denominator": 2 ** (v - 1),
        "v": v,
    } for v in range(1, 11)]


def log_enclosure(value: Fraction, bits: int) -> tuple[Fraction, Fraction]:
    y = (value - 1) / (value + 1)
    term, total = y, Fraction(0)
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
            raise ValueError("log enclosure convergence")
    total *= 2
    return total - remainder, total + remainder


def fibonacci(maximum: int) -> list[int]:
    values = [1, 2]
    while len(values) <= maximum:
        values.append(values[-1] + values[-2])
    return values


def reference_gamma(index: int, bits: int) -> tuple[Fraction, Fraction, Fraction]:
    truncation = bits // 2 + 18
    words = fibonacci(truncation + 1)
    lower, upper = Fraction(0), Fraction(0)
    for v in range(index + 1, truncation + 1):
        ratio = Fraction(words[v + 1] * words[v - 1], words[v] ** 2)
        delta_lower, delta_upper = log_enclosure(ratio, bits)
        weight = -Fraction(2 ** index, 2 ** v)
        lower += weight * delta_upper
        upper += weight * delta_lower
    analytic_tail = Fraction(7 * 2 ** index, 6 * 5 ** (truncation + 1))
    denominator = 2 ** (bits + 16)
    rounded_lower = Fraction(((lower - analytic_tail).numerator * denominator)
                             // (lower - analytic_tail).denominator, denominator)
    rounded_upper = Fraction(-((-((upper + analytic_tail).numerator * denominator))
                               // (upper + analytic_tail).denominator), denominator)
    rounded_tail = Fraction(-((-analytic_tail.numerator * denominator)
                              // analytic_tail.denominator), denominator)
    return rounded_lower, rounded_upper, rounded_tail


def b_tail_serialized(index: int, bits: int) -> Fraction:
    scale = 2 ** (bits + 48)
    def down(value: Fraction) -> Fraction:
        return Fraction((value.numerator * scale) // value.denominator, scale)
    def up(value: Fraction) -> Fraction:
        return Fraction(-((-value.numerator * scale) // value.denominator), scale)
    digits = bits * 30103 // 100000 + 14
    decimal_scale = 10 ** digits
    floor_sqrt = math.isqrt(5 * decimal_scale * decimal_scale)
    sqrt_lower = Fraction(floor_sqrt, decimal_scale)
    t_upper = up((Fraction(3) - sqrt_lower) / 2)
    def multiply(left: Fraction, right: Fraction) -> Fraction:
        return up(left * right)
    def power(value: Fraction, exponent: int) -> Fraction:
        result, base, remaining = Fraction(1), up(value), exponent
        while remaining:
            if remaining & 1:
                result = multiply(result, base)
            base = multiply(base, base)
            remaining //= 2
        return result
    truncation = bits // 2 + 20
    tail_power = power(t_upper, (truncation + 1) * (index + 2))
    short_power = power(t_upper, index + 2)
    tail = up(Fraction(2) * tail_power / (Fraction(truncation + 1) * (1 - short_power)))
    serial_scale = 2 ** (bits + 16)
    return Fraction(-((-tail.numerator * serial_scale) // tail.denominator), serial_scale)


def validate_common(payload: dict[str, Any], expected: dict[str, Any], label: str) -> None:
    exact_keys(payload, PAYLOAD_KEYS, label + " payload")
    for name in ("algebraic_certificate", "case_counts", "evidence_boundary",
                 "finite_records", "radial_records", "representative_records", "residue_records"):
        if not strict(payload[name], expected[name]):
            raise ValueError(f"{label} independently reconstructed {name}")
    records = payload["finite_records"]
    if type(records) is not list or len(records) != 580:
        raise ValueError(label + " finite list")
    for row in records:
        exact_keys(row, FINITE_KEYS, label + " finite record")
        for name in ("N", "dimension", "q", "ratio_denominator", "ratio_numerator", "z_n"):
            integer(row[name], label + " finite " + name)
        if type(row["matrix_row_major"]) is not list \
                or any(type(bit) is not int or bit not in (0, 1) for bit in row["matrix_row_major"]):
            raise ValueError(label + " finite matrix type")


def validate_gamma(rows: Any, label: str) -> list[dict[str, Any]]:
    if type(rows) is not list or len(rows) != 33:
        raise ValueError(label + " gamma list")
    overlaps = []
    position = 0
    for bits in (128, 256, 512):
        for index in range(11):
            row = rows[position]
            position += 1
            exact_keys(row, GAMMA_KEYS, label + " gamma record")
            integer(row["bits"], label + " gamma bits")
            integer(row["index"], label + " gamma index", 0)
            integer(row["truncation_index"], label + " truncation", 1)
            expected_id = f"G|k={index}|bits={bits}"
            if row["case_id"] != expected_id or row["bits"] != bits or row["index"] != index:
                raise ValueError(label + " gamma identifier/grid")
            if label == "A":
                expected_method = "direct_fibonacci_ratio_log_interval"
                expected_certificate = "A_FIBONACCI_RATIO_ATANH_PLUS_PERRON_TAIL"
                expected_truncation = bits // 2 + 18
            else:
                expected_method = "positive_binet_interval"
                expected_certificate = "B_POSITIVE_BINET_Q_SQRT5_GEOMETRIC_TAIL"
                expected_truncation = bits // 2 + 20
            if row["method"] != expected_method or row["certificate_id"] != expected_certificate \
                    or row["truncation_index"] != expected_truncation:
                raise ValueError(label + " gamma method/certificate/truncation")
            lower, upper, tail = rational(row, "lower"), rational(row, "upper"), rational(row, "tail_bound")
            reference_lower, reference_upper, reference_tail = reference_gamma(index, bits)
            if (lower, upper, tail) != (reference_lower, reference_upper, reference_tail):
                raise ValueError(label + " gamma outward enclosure/tail truth")
            if label == "B" and tail != b_tail_serialized(index, bits):
                raise ValueError("B gamma geometric tail formula")
            if lower > upper or (index % 2 == 0 and lower <= 0) \
                    or (index % 2 == 1 and upper >= 0):
                raise ValueError(label + " gamma interval orientation/sign")
            overlaps.append({"bits": bits, "case_id": expected_id, "index": index, "overlap": True})
    return overlaps


def mutation(instance_id: str) -> int:
    code = MUTATIONS.get(instance_id)
    if code is None:
        raise ValueError("not a comparator mutation")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, "consumer": "X", "instance_id": instance_id,
                    "witness": "independent exact reconstruction rejects the frozen mutation"},
        "schema": "paper44-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--stage")
    parser.add_argument("--a")
    parser.add_argument("--b")
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return mutation(args.mutation)
    if not args.root or not args.stage or not args.a or not args.b:
        raise ValueError("root, stage, and evaluator paths required")
    root, stage = Path(args.root), Path(args.stage)
    raw_path = safe_file(root, str(root / "preauthority/RAW_INPUT_MANIFEST.json"))
    raw_bytes = raw_path.read_bytes()
    if hashlib.sha256(raw_bytes).hexdigest() != RAW_SHA256:
        raise ValueError("frozen raw manifest hash")
    raw = json.loads(raw_bytes.decode("ascii"), object_pairs_hook=unique)
    expected = {
        "algebraic_certificate": {
            "difference_denominator": 220, "difference_rational_part": 6557,
            "difference_sqrt5_coefficient": -2929, "square_difference": 99044,
            "strictly_positive": True,
        },
        "case_counts": {"finite_rejected_scope": 32, "finite_total": 580, "finite_valid": 548},
        "evidence_boundary": {
            "finite_evidence_class": "FINITE_EXACT_OR_CERTIFIED_DIAGNOSTIC",
            "infinite_theorem_claimed": False, "infinite_theorem_owner": "P",
        },
        "finite_records": expected_finite(raw),
        "radial_records": expected_radial(),
        "representative_records": expected_digits(raw),
        "residue_records": expected_residues(),
    }
    left, left_raw = load_json(safe_file(stage, args.a))
    right, right_raw = load_json(safe_file(stage, args.b))
    exact_keys(left, ENVELOPE_KEYS, "A envelope")
    exact_keys(right, ENVELOPE_KEYS, "B envelope")
    if left["schema"] != "paper44-evaluator-a-v1" or right["schema"] != "paper44-evaluator-b-v1" \
            or left["status"] != "PASS" or right["status"] != "PASS":
        raise ValueError("evaluator envelope values")
    left_payload, right_payload = left["payload"], right["payload"]
    validate_common(left_payload, expected, "A")
    validate_common(right_payload, expected, "B")
    if not strict(left_payload["implementation"], {
        "algorithm": "literal_source_graph_component_enumeration",
        "fixture_expander": "itertools_lexicographic_and_positive_power_primitivity",
        "project_local_imports": [],
    }):
        raise ValueError("A implementation identity")
    if not strict(right_payload["implementation"], {
        "algorithm": "closed_chain_histogram_integer_word_counts",
        "fixture_expander": "integer_bitstream_and_graph_period_primitivity",
        "project_local_imports": [],
    }):
        raise ValueError("B implementation identity")
    overlaps_a = validate_gamma(left_payload["gamma_intervals"], "A")
    overlaps_b = validate_gamma(right_payload["gamma_intervals"], "B")
    if not strict(overlaps_a, overlaps_b):
        raise ValueError("gamma grid disagreement")
    for name in ("finite_records", "radial_records", "representative_records", "residue_records"):
        if not strict(left_payload[name], right_payload[name]):
            raise ValueError("strict cross-evaluator projection " + name)
    hashes = {name: hashlib.sha256(canonical(expected[name])).hexdigest()
              for name in ("finite_records", "radial_records", "representative_records", "residue_records")}
    output = {
        "payload": {
            "case_counts": expected["case_counts"],
            "evaluator_output_sha256": {
                "A": hashlib.sha256(left_raw).hexdigest(), "B": hashlib.sha256(right_raw).hexdigest(),
            },
            "evidence_boundary": {
                "finite_evidence_status": "PASS",
                "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE",
                "proof_owner": "P",
            },
            "finite_projection_sha256": hashes["finite_records"],
            "gamma_overlap": {"all_overlap": True, "case_count": 33, "records": overlaps_a},
            "positive_controls": {
                "golden_W4": "PASS_10_ROWS", "one_symbol": "PASS", "full_shifts": "PASS",
                "w8_square_difference": 99044,
            },
            "radial_projection_sha256": hashes["radial_records"],
            "representative_projection_sha256": hashes["representative_records"],
            "residue_projection_sha256": hashes["residue_records"],
            "strict_recursive_type_and_value_equal": True,
        },
        "schema": "paper44-exact-comparison-v1", "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
