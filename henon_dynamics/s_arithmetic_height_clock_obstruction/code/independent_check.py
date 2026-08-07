#!/usr/bin/env python3
"""Independent checker for the HCS-C16 compact certificates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Callable


PRODUCER_PRECISION = 80
CHECK_PRECISION = 120
EXPECTED_SAMPLES = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 2), (-6, 17)]
EXPECTED_BOX_COUNTS = {10: 48, 20: 191, 40: 742, 80: 2970, 160: 11841, 320: 47349}
EXPECTED_HEIGHT_COUNTS = {10: 10, 20: 36, 40: 144, 80: 577, 160: 2306, 320: 9211, 640: 36857}
HASHED_ARTIFACTS = {
    "exact_certificates.json",
    "near_wall.csv",
    "primitive_box_counts.csv",
    "primitive_height_counts.csv",
}
REQUIRED_INPUTS = HASHED_ARTIFACTS | {"artifact_hashes.json"}
CHECK_NAMES = (
    "required_files_and_manifest",
    "exact_schema",
    "quaternion_model_rederived",
    "generators_rederived",
    "joint_clock_rederived",
    "sample_invariants_fully_rederived",
    "embedded_tables_match_csv",
    "near_wall_records_rederived",
    "frozen_box_counts",
    "independent_box_rows",
    "frozen_height_counts",
    "independent_height_rows",
    "asymptotic_lattice_count",
    "asymptotic_height_count",
    "artifact_hashes",
    "numerical_precision_and_margins",
)

TOP_KEYS = {
    "candidate_id",
    "arithmetic_model",
    "generators",
    "joint_clock",
    "sample_elements",
    "near_wall_records",
    "primitive_box_counts",
    "primitive_height_counts",
    "data_boundary",
}
ARITHMETIC_KEYS = {
    "quaternion_algebra",
    "order",
    "localized_prime",
    "hilbert_symbols",
    "ramified_finite_places",
    "sqrt3_roots_mod_13",
}
GENERATOR_KEYS = {"a", "b", "norm", "signed_clock"}
CLOCK_KEYS = {"A", "C", "formula", "basis_determinant", "rank", "height_formula"}
SAMPLE_KEYS = {
    "m",
    "n",
    "element",
    "matrix",
    "trace",
    "norm",
    "predicted_norm",
    "discriminant",
    "v13_norm",
    "v13_discriminant",
    "real_signed",
    "real_length",
    "tree_signed",
    "tree_length",
    "tree_length_from_trace_norm",
    "primitive",
    "matrix_determinant_matches_norm",
    "norm_matches_13_power",
}
NEAR_WALL_KEYS = {
    "m",
    "n",
    "real_signed",
    "real_length",
    "tree_length",
    "height",
    "unweighted_log_local_factor_s1",
    "height_weight_log10_s1",
}
BOX_KEYS = {
    "real_bound",
    "tree_bound",
    "count_mod_inverse",
    "primitive_lattice_prediction",
    "observed_over_prediction",
    "minimum_boundary_gap",
    "decimal_precision_digits",
}
HEIGHT_KEYS = {
    "height_bound",
    "count_mod_inverse",
    "primitive_height_prediction",
    "observed_over_prediction",
    "minimum_boundary_gap",
    "decimal_precision_digits",
}
DATA_BOUNDARY_KEYS = {
    "prime_table_used",
    "zero_table_used",
    "fitted_parameters",
    "floating_point_scope",
    "decimal_precision_digits",
    "boundary_method",
    "near_wall_limit",
}


def qstr(value: Fraction) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def v13(value: Fraction) -> int:
    value = Fraction(value)
    if value == 0:
        raise ValueError("v13(0) is infinite")
    numerator = abs(value.numerator)
    denominator = value.denominator
    answer = 0
    while numerator % 13 == 0:
        numerator //= 13
        answer += 1
    while denominator % 13 == 0:
        denominator //= 13
        answer -= 1
    return answer


def multiply(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    a, b = x
    c, d = y
    return a * c + 3 * b * d, a * d + b * c


def inverse(x: tuple[Fraction, Fraction]):
    a, b = x
    norm = a * a - 3 * b * b
    if norm == 0:
        raise ZeroDivisionError
    return a / norm, -b / norm


def power(x: tuple[Fraction, Fraction], exponent: int):
    if exponent < 0:
        return power(inverse(x), -exponent)
    answer = (Fraction(1), Fraction(0))
    base = x
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        exponent //= 2
    return answer


def alpha(m: int, n: int):
    return multiply(power((Fraction(2), Fraction(1)), m), power((Fraction(4), Fraction(1)), n))


def exact_sample(m: int, n: int, real_unit: Decimal, split_unit: Decimal) -> dict[str, object]:
    a, b = alpha(m, n)
    norm = a * a - 3 * b * b
    trace = 2 * a
    discriminant = trace * trace - 4 * norm
    tree = max(0, v13(norm) - v13(discriminant))
    # The producer evaluates in Decimal, then serializes binary64 JSON values.
    with localcontext() as context:
        context.prec = CHECK_PRECISION
        signed_real = float(Decimal(m) * real_unit + Decimal(n) * split_unit)
    return {
        "m": m,
        "n": n,
        "element": {"a": qstr(a), "b": qstr(b)},
        "matrix": [[qstr(a), qstr(3 * b)], [qstr(b), qstr(a)]],
        "trace": qstr(trace),
        "norm": qstr(norm),
        "predicted_norm": qstr(Fraction(13) ** n),
        "discriminant": qstr(discriminant),
        "v13_norm": v13(norm),
        "v13_discriminant": v13(discriminant),
        "real_signed": signed_real,
        "real_length": abs(signed_real),
        "tree_signed": n,
        "tree_length": abs(n),
        "tree_length_from_trace_norm": tree,
        "primitive": math.gcd(abs(m), abs(n)) == 1,
        "matrix_determinant_matches_norm": True,
        "norm_matches_13_power": norm == Fraction(13) ** n,
    }


def rational_valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero")
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def legendre(value: int, prime: int) -> int:
    residue = pow(value % prime, (prime - 1) // 2, prime)
    return -1 if residue == prime - 1 else residue


def hilbert_odd(a: int, b: int, prime: int) -> int:
    av = rational_valuation(a, prime)
    bv = rational_valuation(b, prime)
    au = a // prime**av
    bu = b // prime**bv
    parity = av * bv * ((prime - 1) // 2)
    value = -1 if parity % 2 else 1
    if bv % 2:
        value *= legendre(au, prime)
    if av % 2:
        value *= legendre(bu, prime)
    return value


def hilbert_two_odd(a: int, b: int) -> int:
    exponent = ((a - 1) // 2) * ((b - 1) // 2)
    return -1 if exponent % 2 else 1


def checker_constants() -> tuple[Decimal, Decimal, Decimal]:
    with localcontext() as context:
        context.prec = CHECK_PRECISION
        root3 = Decimal(3).sqrt()
        real_unit = Decimal(2) * (Decimal(2) + root3).ln()
        split_unit = ((Decimal(4) + root3) / (Decimal(4) - root3)).ln()
        return +real_unit, +split_unit, +Decimal(13).ln()


def chudnovsky_pi() -> Decimal:
    """Independent high-precision pi calculation for prediction checks."""
    with localcontext() as context:
        context.prec = CHECK_PRECISION + 10
        multiplier = 1
        linear = 13591409
        power_term = 1
        k_value = 6
        series = Decimal(linear)
        for index in range(1, CHECK_PRECISION // 14 + 3):
            multiplier = multiplier * (k_value**3 - 16 * k_value) // index**3
            linear += 545140134
            power_term *= -262537412640768000
            series += Decimal(multiplier * linear) / Decimal(power_term)
            k_value += 12
        value = Decimal(426880) * Decimal(10005).sqrt() / series
        context.prec = CHECK_PRECISION
        return +value


def decimal_ceil(value: Decimal) -> int:
    return int(value.to_integral_value(rounding=ROUND_CEILING))


def decimal_floor(value: Decimal) -> int:
    return int(value.to_integral_value(rounding=ROUND_FLOOR))


def canonical_primitive(m: int, n: int) -> bool:
    return (n > 0 or (n == 0 and m > 0)) and math.gcd(abs(m), n) == 1


def brute_box_details(real_bound: int, tree_bound: int) -> tuple[int, Decimal]:
    with localcontext() as context:
        context.prec = CHECK_PRECISION
        real_unit, split_unit, _ = checker_constants()
        bound = Decimal(real_bound)
        max_m = decimal_ceil((bound + abs(split_unit) * tree_bound) / real_unit) + 3
        count = 0
        minimum_gap = Decimal("Infinity")
        for n in range(tree_bound + 1):
            shift = split_unit * n
            for m in range(-max_m, max_m + 1):
                if m == 0 and n == 0:
                    continue
                value = abs(Decimal(m) * real_unit + shift)
                minimum_gap = min(minimum_gap, abs(value - bound))
                if canonical_primitive(m, n) and value <= bound:
                    count += 1
        return count, minimum_gap


def brute_height_details(bound_value: int) -> tuple[int, Decimal]:
    with localcontext() as context:
        context.prec = CHECK_PRECISION
        real_unit, split_unit, log_p = checker_constants()
        bound = Decimal(bound_value)
        max_n = decimal_floor(bound / log_p)
        max_m = decimal_ceil((bound + abs(split_unit) * max_n) / real_unit) + 3
        count = 0
        minimum_gap = Decimal("Infinity")
        for n in range(max_n + 1):
            shift = split_unit * n
            for m in range(-max_m, max_m + 1):
                if m == 0 and n == 0:
                    continue
                value = abs(Decimal(m) * real_unit + shift) + log_p * n
                minimum_gap = min(minimum_gap, abs(value - bound))
                if canonical_primitive(m, n) and value <= bound:
                    count += 1
        return count, minimum_gap


def independent_near_wall(limit: int) -> list[dict[str, object]]:
    with localcontext() as context:
        context.prec = CHECK_PRECISION
        real_unit, split_unit, log_p = checker_constants()
        best = Decimal("Infinity")
        rows: list[dict[str, object]] = []
        for n in range(1, limit + 1):
            m = int(
                (-Decimal(n) * split_unit / real_unit).to_integral_value(
                    rounding=ROUND_HALF_EVEN
                )
            )
            if math.gcd(abs(m), n) != 1:
                continue
            signed = Decimal(m) * real_unit + Decimal(n) * split_unit
            length = abs(signed)
            if length < best:
                best = length
                height = length + log_p * n
                rows.append(
                    {
                        "m": m,
                        "n": n,
                        "real_signed": float(signed),
                        "real_length": float(length),
                        "tree_length": n,
                        "height": float(height),
                        "unweighted_log_local_factor_s1": float(
                            -(Decimal(1) - (-length).exp()).ln()
                        ),
                        "height_weight_log10_s1": float(-height / Decimal(10).ln()),
                    }
                )
        return rows


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            hasher.update(block)
    return hasher.hexdigest()


def require_keys(value: object, expected: set[str], label: str) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != expected:
        actual = set(value) if isinstance(value, dict) else type(value).__name__
        raise ValueError(f"{label} keys/type mismatch: {actual!r}")
    return value


def require_list(value: object, label: str) -> list[object]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a list")
    return value


def require_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer")
    return value


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{label} must be a boolean")
    return value


def require_string(value: object, label: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a string")
    return value


def require_finite(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def float_close(actual: object, expected: Decimal | float, label: str) -> bool:
    value = require_finite(actual, label)
    target = float(expected)
    return value == target


def load_json_strict(path: Path) -> object:
    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r} in {path.name}")
            result[key] = value
        return result

    def reject_constant(value: str) -> object:
        raise ValueError(f"non-finite JSON constant {value!r} in {path.name}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=reject_constant,
    )


def read_csv_strict(path: Path, headers: list[str], expected_rows: int) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != headers:
            raise ValueError(f"{path.name} header mismatch: {reader.fieldnames!r}")
        rows = list(reader)
    if len(rows) != expected_rows:
        raise ValueError(f"{path.name} row count mismatch")
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"{path.name} contains malformed rows")
    return rows


def validate_schema(
    certificate: object,
    box_rows: list[dict[str, str]],
    height_rows: list[dict[str, str]],
    near_rows: list[dict[str, str]],
) -> bool:
    cert = require_keys(certificate, TOP_KEYS, "certificate")
    require_string(cert["candidate_id"], "candidate_id")
    arithmetic = require_keys(cert["arithmetic_model"], ARITHMETIC_KEYS, "arithmetic_model")
    for field in ("quaternion_algebra", "order"):
        require_string(arithmetic[field], f"arithmetic_model.{field}")
    require_int(arithmetic["localized_prime"], "localized_prime")
    symbols = require_keys(arithmetic["hilbert_symbols"], {"at_2", "at_3", "at_13", "at_infinity"}, "hilbert_symbols")
    for field, value in symbols.items():
        require_int(value, f"hilbert_symbols.{field}")
    require_list(arithmetic["ramified_finite_places"], "ramified_finite_places")
    require_list(arithmetic["sqrt3_roots_mod_13"], "sqrt3_roots_mod_13")
    for value in arithmetic["ramified_finite_places"]:
        require_int(value, "ramified finite place")
    for value in arithmetic["sqrt3_roots_mod_13"]:
        require_int(value, "sqrt3 root")

    generators = require_keys(cert["generators"], {"epsilon", "pi"}, "generators")
    for name in ("epsilon", "pi"):
        generator = require_keys(generators[name], GENERATOR_KEYS, f"generator {name}")
        for field in ("a", "b", "norm"):
            require_string(generator[field], f"generator {name}.{field}")
        clock = require_list(generator["signed_clock"], f"generator {name} signed_clock")
        if len(clock) != 2:
            raise ValueError(f"generator {name} signed_clock length")
        require_finite(clock[0], f"generator {name} signed_clock[0]")
        require_int(clock[1], f"generator {name} signed_clock[1]")

    clock = require_keys(cert["joint_clock"], CLOCK_KEYS, "joint_clock")
    for field in ("A", "C", "basis_determinant"):
        require_finite(clock[field], f"joint_clock.{field}")
    require_int(clock["rank"], "joint_clock.rank")
    require_string(clock["formula"], "joint_clock.formula")
    require_string(clock["height_formula"], "joint_clock.height_formula")

    samples = require_list(cert["sample_elements"], "sample_elements")
    if len(samples) != len(EXPECTED_SAMPLES):
        raise ValueError("sample_elements must contain the exact required sample set")
    coordinates = []
    for index, raw in enumerate(samples):
        row = require_keys(raw, SAMPLE_KEYS, f"sample[{index}]")
        coordinates.append((require_int(row["m"], "sample m"), require_int(row["n"], "sample n")))
        require_keys(row["element"], {"a", "b"}, "sample element")
        for field in ("a", "b"):
            require_string(row["element"][field], f"sample.element.{field}")
        matrix = require_list(row["matrix"], "sample matrix")
        if len(matrix) != 2 or any(not isinstance(part, list) or len(part) != 2 for part in matrix):
            raise ValueError("sample matrix must be 2x2")
        for matrix_row in matrix:
            for value in matrix_row:
                require_string(value, "sample matrix entry")
        for field in ("trace", "norm", "predicted_norm", "discriminant"):
            require_string(row[field], f"sample.{field}")
        for field in (
            "v13_norm", "v13_discriminant", "tree_signed", "tree_length",
            "tree_length_from_trace_norm",
        ):
            require_int(row[field], f"sample.{field}")
        for field in ("primitive", "matrix_determinant_matches_norm", "norm_matches_13_power"):
            require_bool(row[field], f"sample.{field}")
        for field in ("real_signed", "real_length"):
            require_finite(row[field], f"sample.{field}")
    if coordinates != EXPECTED_SAMPLES:
        raise ValueError(f"sample coordinates mismatch: {coordinates!r}")

    near = require_list(cert["near_wall_records"], "near_wall_records")
    if not near:
        raise ValueError("near_wall_records must be nonempty")
    for index, raw in enumerate(near):
        row = require_keys(raw, NEAR_WALL_KEYS, f"near_wall[{index}]")
        require_int(row["m"], "near-wall m")
        require_int(row["n"], "near-wall n")
        require_int(row["tree_length"], "near-wall tree_length")
        for field in NEAR_WALL_KEYS - {"m", "n", "tree_length"}:
            require_finite(row[field], f"near_wall.{field}")

    box = require_list(cert["primitive_box_counts"], "primitive_box_counts")
    height = require_list(cert["primitive_height_counts"], "primitive_height_counts")
    if len(box) != len(EXPECTED_BOX_COUNTS) or len(height) != len(EXPECTED_HEIGHT_COUNTS):
        raise ValueError("embedded count row count mismatch")
    for index, raw in enumerate(box):
        row = require_keys(raw, BOX_KEYS, f"box[{index}]")
        for field in ("real_bound", "tree_bound", "count_mod_inverse", "decimal_precision_digits"):
            require_int(row[field], f"box.{field}")
        for field in BOX_KEYS - {"real_bound", "tree_bound", "count_mod_inverse", "decimal_precision_digits"}:
            require_finite(row[field], f"box.{field}")
    for index, raw in enumerate(height):
        row = require_keys(raw, HEIGHT_KEYS, f"height[{index}]")
        for field in ("height_bound", "count_mod_inverse", "decimal_precision_digits"):
            require_int(row[field], f"height.{field}")
        for field in HEIGHT_KEYS - {"height_bound", "count_mod_inverse", "decimal_precision_digits"}:
            require_finite(row[field], f"height.{field}")

    require_keys(cert["data_boundary"], DATA_BOUNDARY_KEYS, "data_boundary")
    boundary = cert["data_boundary"]
    require_bool(boundary["prime_table_used"], "data_boundary.prime_table_used")
    require_bool(boundary["zero_table_used"], "data_boundary.zero_table_used")
    require_list(boundary["fitted_parameters"], "data_boundary.fitted_parameters")
    require_string(boundary["floating_point_scope"], "data_boundary.floating_point_scope")
    require_int(boundary["decimal_precision_digits"], "data_boundary.decimal_precision_digits")
    require_string(boundary["boundary_method"], "data_boundary.boundary_method")
    require_int(boundary["near_wall_limit"], "data_boundary.near_wall_limit")
    if len(box_rows) != len(box) or len(height_rows) != len(height) or len(near_rows) != len(near):
        raise ValueError("CSV and embedded table lengths differ")
    return True


def json_rows_as_csv(rows: list[dict[str, object]], headers: list[str]) -> list[dict[str, str]]:
    return [{key: str(row[key]) for key in headers} for row in rows]


def rows_match(actual: list[dict[str, object]], expected: list[dict[str, object]]) -> bool:
    if len(actual) != len(expected):
        return False
    for row, target in zip(actual, expected):
        if set(row) != set(target):
            return False
        for key, value in target.items():
            if isinstance(value, float):
                if not float_close(row[key], value, f"row.{key}"):
                    return False
            elif row[key] != value:
                return False
    return True


def build_report(checks: dict[str, bool], errors: list[str]) -> dict[str, object]:
    return {
        "candidate_id": "HCS-C16",
        "checks": checks,
        "all_passed": all(checks.values()),
        "check_count": len(checks),
        "errors": errors,
        "independence_note": (
            "The checker reimplements exact quadratic arithmetic and Hilbert symbols, "
            "uses 120-digit Decimal brute-force enumeration against the producer's "
            "80-digit Decimal enumeration, and computes pi independently."
        ),
    }


def check(results: Path) -> dict[str, object]:
    checks = {name: False for name in CHECK_NAMES}
    errors: list[str] = []

    missing = sorted(name for name in REQUIRED_INPUTS if not (results / name).is_file())
    if missing:
        errors.append(f"missing required files: {missing!r}")
        return build_report(checks, errors)

    try:
        certificate = load_json_strict(results / "exact_certificates.json")
        hashes = load_json_strict(results / "artifact_hashes.json")
        if not isinstance(hashes, dict) or set(hashes) != HASHED_ARTIFACTS:
            raise ValueError("hash manifest must contain exactly the four producer artifacts")
        if any(not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes.values()):
            raise ValueError("hash manifest contains an invalid SHA-256 digest")
        checks["required_files_and_manifest"] = True

        # Sets describe schemas; CSV order is part of the release format.
        box_headers = [
            "real_bound", "tree_bound", "count_mod_inverse",
            "primitive_lattice_prediction", "observed_over_prediction",
            "minimum_boundary_gap", "decimal_precision_digits",
        ]
        height_headers = [
            "height_bound", "count_mod_inverse", "primitive_height_prediction",
            "observed_over_prediction", "minimum_boundary_gap", "decimal_precision_digits",
        ]
        near_headers = [
            "m", "n", "real_signed", "real_length", "tree_length", "height",
            "unweighted_log_local_factor_s1", "height_weight_log10_s1",
        ]
        box_rows = read_csv_strict(results / "primitive_box_counts.csv", box_headers, len(EXPECTED_BOX_COUNTS))
        height_rows = read_csv_strict(results / "primitive_height_counts.csv", height_headers, len(EXPECTED_HEIGHT_COUNTS))
        near_csv_rows = read_csv_strict(
            results / "near_wall.csv", near_headers,
            len(require_list(certificate.get("near_wall_records"), "near_wall_records"))
            if isinstance(certificate, dict) else 0,
        )
        checks["exact_schema"] = validate_schema(certificate, box_rows, height_rows, near_csv_rows)
    except Exception as error:  # malformed certificates should fail cleanly, never hang
        errors.append(f"structure: {error}")
        return build_report(checks, errors)

    assert isinstance(certificate, dict)
    arithmetic = certificate["arithmetic_model"]
    generators = certificate["generators"]
    clock = certificate["joint_clock"]
    data_boundary = certificate["data_boundary"]
    real_unit, split_unit, log_p = checker_constants()
    pi = chudnovsky_pi()

    def evaluate(name: str, operation: Callable[[], bool]) -> None:
        try:
            checks[name] = bool(operation())
            if not checks[name]:
                errors.append(f"{name}: validation returned false")
        except Exception as error:
            errors.append(f"{name}: {error}")

    evaluate(
        "quaternion_model_rederived",
        lambda: certificate["candidate_id"] == "HCS-C16"
        and arithmetic["quaternion_algebra"] == "(-1,3)_Q"
        and arithmetic["order"] == "Z[1,i,j,ij]"
        and arithmetic["localized_prime"] == 13
        and arithmetic["hilbert_symbols"]
        == {
            "at_2": hilbert_two_odd(-1, 3),
            "at_3": hilbert_odd(-1, 3, 3),
            "at_13": hilbert_odd(-1, 3, 13),
            "at_infinity": 1,
        }
        and arithmetic["ramified_finite_places"] == [2, 3]
        and arithmetic["sqrt3_roots_mod_13"] == [4, 9]
        and all((root * root - 3) % 13 == 0 for root in arithmetic["sqrt3_roots_mod_13"]),
    )

    evaluate(
        "generators_rederived",
        lambda: generators["epsilon"]["a"] == "2"
        and generators["epsilon"]["b"] == "1"
        and generators["epsilon"]["norm"] == "1"
        and float_close(generators["epsilon"]["signed_clock"][0], real_unit, "epsilon clock")
        and generators["epsilon"]["signed_clock"][1] == 0
        and generators["pi"]["a"] == "4"
        and generators["pi"]["b"] == "1"
        and generators["pi"]["norm"] == "13"
        and float_close(generators["pi"]["signed_clock"][0], split_unit, "pi clock")
        and generators["pi"]["signed_clock"][1] == 1,
    )

    evaluate(
        "joint_clock_rederived",
        lambda: float_close(clock["A"], real_unit, "clock A")
        and float_close(clock["C"], split_unit, "clock C")
        and clock["formula"] == "(m,n) -> (m*A+n*C,n)"
        and float_close(clock["basis_determinant"], real_unit, "basis determinant")
        and clock["rank"] == 2
        and clock["height_formula"] == "H=abs(m*A+n*C)+log(13)*abs(n)=2*h(r)",
    )

    expected_samples = [exact_sample(m, n, real_unit, split_unit) for m, n in EXPECTED_SAMPLES]
    evaluate(
        "sample_invariants_fully_rederived",
        lambda: rows_match(certificate["sample_elements"], expected_samples),
    )

    evaluate(
        "embedded_tables_match_csv",
        lambda: json_rows_as_csv(certificate["primitive_box_counts"], box_headers) == box_rows
        and json_rows_as_csv(certificate["primitive_height_counts"], height_headers) == height_rows
        and json_rows_as_csv(certificate["near_wall_records"], near_headers) == near_csv_rows,
    )

    expected_near = independent_near_wall(data_boundary["near_wall_limit"])
    evaluate(
        "near_wall_records_rederived",
        lambda: rows_match(certificate["near_wall_records"], expected_near),
    )

    box_bounds = [int(row["real_bound"]) for row in box_rows]
    height_bounds = [int(row["height_bound"]) for row in height_rows]
    evaluate(
        "frozen_box_counts",
        lambda: box_bounds == list(EXPECTED_BOX_COUNTS)
        and [int(row["tree_bound"]) for row in box_rows] == box_bounds
        and [int(row["count_mod_inverse"]) for row in box_rows] == list(EXPECTED_BOX_COUNTS.values()),
    )
    evaluate(
        "frozen_height_counts",
        lambda: height_bounds == list(EXPECTED_HEIGHT_COUNTS)
        and [int(row["count_mod_inverse"]) for row in height_rows] == list(EXPECTED_HEIGHT_COUNTS.values()),
    )

    def check_box_rows() -> bool:
        for raw in certificate["primitive_box_counts"]:
            bound = raw["real_bound"]
            count, margin = brute_box_details(bound, raw["tree_bound"])
            prediction = Decimal(12) * bound * raw["tree_bound"] / (pi**2 * real_unit)
            if count != raw["count_mod_inverse"]:
                return False
            if not float_close(raw["primitive_lattice_prediction"], prediction, "box prediction"):
                return False
            if not float_close(raw["observed_over_prediction"], Decimal(count) / prediction, "box ratio"):
                return False
            if not float_close(raw["minimum_boundary_gap"], margin, "box margin"):
                return False
        return True

    def check_height_rows() -> bool:
        for raw in certificate["primitive_height_counts"]:
            bound = raw["height_bound"]
            count, margin = brute_height_details(bound)
            prediction = Decimal(6) * bound * bound / (pi**2 * real_unit * log_p)
            if count != raw["count_mod_inverse"]:
                return False
            if not float_close(raw["primitive_height_prediction"], prediction, "height prediction"):
                return False
            if not float_close(raw["observed_over_prediction"], Decimal(count) / prediction, "height ratio"):
                return False
            if not float_close(raw["minimum_boundary_gap"], margin, "height margin"):
                return False
        return True

    evaluate("independent_box_rows", check_box_rows)
    evaluate("independent_height_rows", check_height_rows)
    evaluate(
        "asymptotic_lattice_count",
        lambda: abs(float(certificate["primitive_box_counts"][-1]["observed_over_prediction"]) - 1.0) < 0.01,
    )
    evaluate(
        "asymptotic_height_count",
        lambda: abs(float(certificate["primitive_height_counts"][-1]["observed_over_prediction"]) - 1.0) < 0.01,
    )
    evaluate(
        "artifact_hashes",
        lambda: set(hashes) == HASHED_ARTIFACTS
        and all(digest(results / filename) == hashes[filename] for filename in HASHED_ARTIFACTS),
    )
    evaluate(
        "numerical_precision_and_margins",
        lambda: data_boundary
        == {
            "prime_table_used": False,
            "zero_table_used": False,
            "fitted_parameters": [],
            "floating_point_scope": "serialization of Decimal logarithms and count diagnostics only",
            "decimal_precision_digits": PRODUCER_PRECISION,
            "boundary_method": "Decimal comparisons without epsilon; positive cutoff margins recorded",
            "near_wall_limit": data_boundary["near_wall_limit"],
        }
        and isinstance(data_boundary["near_wall_limit"], int)
        and data_boundary["near_wall_limit"] >= max(row["n"] for row in certificate["near_wall_records"])
        and all(row["decimal_precision_digits"] == PRODUCER_PRECISION for row in certificate["primitive_box_counts"])
        and all(row["decimal_precision_digits"] == PRODUCER_PRECISION for row in certificate["primitive_height_counts"])
        and all(row["minimum_boundary_gap"] > 10.0 ** (-PRODUCER_PRECISION // 2) for row in certificate["primitive_box_counts"])
        and all(row["minimum_boundary_gap"] > 10.0 ** (-PRODUCER_PRECISION // 2) for row in certificate["primitive_height_counts"]),
    )

    return build_report(checks, errors)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=Path("results"))
    parser.add_argument("--output", type=Path, default=Path("results/independent_check.json"))
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    report = check(arguments.results)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")
    if not report["all_passed"]:
        raise SystemExit(1)
