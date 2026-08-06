#!/usr/bin/env python3
"""Independent verifier for the persisted HCS-C13 exact certificate.

This checker deliberately does not import :mod:`trace_map_audit`.  It uses a
separate, ascending-coefficient polynomial implementation to reconstruct the
Fibonacci trace recurrence.  It performs four checks:

1. direct chronological 2-by-2 matrix products through level 5;
2. strict schema and row-set validation of the persisted CSV and JSON;
3. all 48 gcd tests both at the persisted prime and at a second prime; and
4. the 30 tests with k <= 5 directly over Q using ``Fraction`` coefficients.

Only exact integer, finite-field, and rational arithmetic is used.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, TypeVar


PERSISTED_PRIME = 1_000_003
SECOND_PRIME = 1_000_033
MAX_K = 8
RATIONAL_MAX_K = 5

CSV_COLUMNS = [
    "k",
    "q_k",
    "degree_d_k",
    "section",
    "section_value_d",
    "return_clock",
    "return_time",
    "simultaneous_gcd_degree_mod_p",
    "prime",
]

SECTIONS = (
    ("discriminant_zero", 0),
    ("positive_band_edge", 2),
    ("negative_band_edge", -2),
)

RENORMALIZATION_CLOCK = "renormalization_m_equals_k"
PHYSICAL_CLOCK = "physical_m_equals_qk"

Scalar = TypeVar("Scalar", int, Fraction)
Polynomial = tuple[Scalar, ...]


def trim(poly: Polynomial[Scalar]) -> Polynomial[Scalar]:
    """Return the canonical ascending-coefficient representation."""

    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (0,)


def add(left: Polynomial[Scalar], right: Polynomial[Scalar]) -> Polynomial[Scalar]:
    size = max(len(left), len(right))
    zero = left[0] * 0
    return trim(
        tuple(
            (left[i] if i < len(left) else zero)
            + (right[i] if i < len(right) else zero)
            for i in range(size)
        )
    )


def negate(poly: Polynomial[Scalar]) -> Polynomial[Scalar]:
    return trim(tuple(-coefficient for coefficient in poly))


def subtract(left: Polynomial[Scalar], right: Polynomial[Scalar]) -> Polynomial[Scalar]:
    return add(left, negate(right))


def multiply(left: Polynomial[Scalar], right: Polynomial[Scalar]) -> Polynomial[Scalar]:
    zero = left[0] * 0
    result = [zero] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] += left_coefficient * right_coefficient
    return trim(tuple(result))


def integer_trace_polynomials(max_k: int) -> dict[int, Polynomial[int]]:
    """Reconstruct d[k+1] = d[k] d[k-1] - d[k-2] over Z[E]."""

    traces: dict[int, Polynomial[int]] = {
        -2: (2,),
        -1: (0, 1),
        0: (-1, 1),
    }
    for k in range(max_k):
        traces[k + 1] = subtract(multiply(traces[k], traces[k - 1]), traces[k - 2])
    return traces


def fibonacci_words(max_k: int) -> dict[int, str]:
    words = {-1: "b", 0: "a"}
    for k in range(max_k):
        words[k + 1] = words[k] + words[k - 1]
    return words


def fibonacci_lengths(max_k: int) -> dict[int, int]:
    lengths = {-1: 1, 0: 1}
    for k in range(max_k):
        lengths[k + 1] = lengths[k] + lengths[k - 1]
    return lengths


IntegerMatrix = tuple[
    tuple[Polynomial[int], Polynomial[int]],
    tuple[Polynomial[int], Polynomial[int]],
]


def matrix_multiply(left: IntegerMatrix, right: IntegerMatrix) -> IntegerMatrix:
    return (
        (
            add(multiply(left[0][0], right[0][0]), multiply(left[0][1], right[1][0])),
            add(multiply(left[0][0], right[0][1]), multiply(left[0][1], right[1][1])),
        ),
        (
            add(multiply(left[1][0], right[0][0]), multiply(left[1][1], right[1][0])),
            add(multiply(left[1][0], right[0][1]), multiply(left[1][1], right[1][1])),
        ),
    )


def chronological_trace(word: str) -> Polynomial[int]:
    identity: IntegerMatrix = (((1,), (0,)), ((0,), (1,)))
    product = identity
    for letter in word:
        potential = 1 if letter == "a" else 0
        site: IntegerMatrix = (((( -potential, 1)), (-1,)), ((1,), (0,)))
        # Later physical sites multiply on the left.
        product = matrix_multiply(site, product)
    return add(product[0][0], product[1][1])


def verify_chronology(traces: dict[int, Polynomial[int]], through_k: int = 5) -> list[dict[str, object]]:
    words = fibonacci_words(through_k)
    rows: list[dict[str, object]] = []
    for k in range(-1, through_k + 1):
        observed = chronological_trace(words[k])
        if observed != traces[k]:
            raise AssertionError(f"independent chronological product mismatch at k={k}")
        rows.append(
            {
                "k": k,
                "word": words[k],
                "physical_length": len(words[k]),
                "degree": len(observed) - 1,
            }
        )
    return rows


def finite_field_ops(prime: int) -> tuple[
    Callable[[Polynomial[int]], Polynomial[int]],
    Callable[[Polynomial[int], Polynomial[int]], Polynomial[int]],
    Callable[[Polynomial[int], Polynomial[int]], Polynomial[int]],
    Callable[[Polynomial[int], Polynomial[int]], Polynomial[int]],
]:
    """Build canonical reduction, product, remainder, and gcd over GF(prime)."""

    def normalize(poly: Polynomial[int]) -> Polynomial[int]:
        return trim(tuple(int(coefficient) % prime for coefficient in poly))

    def product(left: Polynomial[int], right: Polynomial[int]) -> Polynomial[int]:
        return normalize(multiply(normalize(left), normalize(right)))

    def remainder(dividend: Polynomial[int], divisor: Polynomial[int]) -> Polynomial[int]:
        numerator = list(normalize(dividend))
        denominator = normalize(divisor)
        if denominator == (0,):
            raise ZeroDivisionError("polynomial division by zero")
        inverse_lead = pow(denominator[-1], -1, prime)
        while len(numerator) >= len(denominator) and any(numerator):
            shift = len(numerator) - len(denominator)
            factor = numerator[-1] * inverse_lead % prime
            for index, coefficient in enumerate(denominator):
                numerator[index + shift] = (numerator[index + shift] - factor * coefficient) % prime
            while len(numerator) > 1 and numerator[-1] == 0:
                numerator.pop()
        return normalize(tuple(numerator))

    def gcd(left: Polynomial[int], right: Polynomial[int]) -> Polynomial[int]:
        a, b = normalize(left), normalize(right)
        while b != (0,):
            a, b = b, remainder(a, b)
        if a == (0,):
            return a
        inverse_lead = pow(a[-1], -1, prime)
        return normalize(tuple(coefficient * inverse_lead for coefficient in a))

    return normalize, product, remainder, gcd


def rational_ops() -> tuple[
    Callable[[Polynomial[Fraction]], Polynomial[Fraction]],
    Callable[[Polynomial[Fraction], Polynomial[Fraction]], Polynomial[Fraction]],
    Callable[[Polynomial[Fraction], Polynomial[Fraction]], Polynomial[Fraction]],
    Callable[[Polynomial[Fraction], Polynomial[Fraction]], Polynomial[Fraction]],
]:
    """Build canonical reduction, product, remainder, and gcd over Q."""

    def normalize(poly: Polynomial[Fraction]) -> Polynomial[Fraction]:
        return trim(tuple(Fraction(coefficient) for coefficient in poly))

    def product(left: Polynomial[Fraction], right: Polynomial[Fraction]) -> Polynomial[Fraction]:
        return normalize(multiply(normalize(left), normalize(right)))

    def remainder(dividend: Polynomial[Fraction], divisor: Polynomial[Fraction]) -> Polynomial[Fraction]:
        numerator = list(normalize(dividend))
        denominator = normalize(divisor)
        if denominator == (Fraction(0),):
            raise ZeroDivisionError("polynomial division by zero")
        while len(numerator) >= len(denominator) and any(numerator):
            shift = len(numerator) - len(denominator)
            factor = numerator[-1] / denominator[-1]
            for index, coefficient in enumerate(denominator):
                numerator[index + shift] -= factor * coefficient
            while len(numerator) > 1 and numerator[-1] == 0:
                numerator.pop()
        return normalize(tuple(numerator))

    def gcd(left: Polynomial[Fraction], right: Polynomial[Fraction]) -> Polynomial[Fraction]:
        a, b = normalize(left), normalize(right)
        while b != (Fraction(0),):
            a, b = b, remainder(a, b)
        if a == (Fraction(0),):
            return a
        return normalize(tuple(coefficient / a[-1] for coefficient in a))

    return normalize, product, remainder, gcd


def simultaneous_gcd_degree_finite_field(
    traces: dict[int, Polynomial[int]],
    k: int,
    section_value: int,
    return_time: int,
    prime: int,
) -> int:
    normalize, product, remainder, gcd = finite_field_ops(prime)
    hit = normalize(subtract(traces[k], (section_value,)))

    reduced: dict[int, Polynomial[int]] = {
        -2: remainder((2,), hit),
        -1: remainder((0, 1), hit),
        0: remainder((-1, 1), hit),
    }
    for j in range(return_time):
        recurrence_value = subtract(product(reduced[j], reduced[j - 1]), reduced[j - 2])
        reduced[j + 1] = remainder(normalize(recurrence_value), hit)

    targets = (
        subtract(reduced[return_time], reduced[0]),
        subtract(reduced[return_time - 1], reduced[-1]),
        subtract(reduced[return_time - 2], reduced[-2]),
    )
    common = hit
    for target in targets:
        common = gcd(common, normalize(target))
    return len(common) - 1


def simultaneous_gcd_degree_rational(
    traces: dict[int, Polynomial[int]],
    k: int,
    section_value: int,
    return_time: int,
) -> int:
    normalize, product, remainder, gcd = rational_ops()
    hit = normalize(tuple(Fraction(coefficient) for coefficient in subtract(traces[k], (section_value,))))

    reduced: dict[int, Polynomial[Fraction]] = {
        -2: remainder((Fraction(2),), hit),
        -1: remainder((Fraction(0), Fraction(1)), hit),
        0: remainder((Fraction(-1), Fraction(1)), hit),
    }
    for j in range(return_time):
        recurrence_value = subtract(product(reduced[j], reduced[j - 1]), reduced[j - 2])
        reduced[j + 1] = remainder(normalize(recurrence_value), hit)

    targets = (
        subtract(reduced[return_time], reduced[0]),
        subtract(reduced[return_time - 1], reduced[-1]),
        subtract(reduced[return_time - 2], reduced[-2]),
    )
    common = hit
    for target in targets:
        common = gcd(common, normalize(target))
    return len(common) - 1


def expected_cases(max_k: int) -> list[dict[str, int | str]]:
    lengths = fibonacci_lengths(max_k)
    cases: list[dict[str, int | str]] = []
    for k in range(1, max_k + 1):
        for section, section_value in SECTIONS:
            for return_clock, return_time in (
                (RENORMALIZATION_CLOCK, k),
                (PHYSICAL_CLOCK, lengths[k]),
            ):
                cases.append(
                    {
                        "k": k,
                        "q_k": lengths[k],
                        "degree_d_k": lengths[k],
                        "section": section,
                        "section_value_d": section_value,
                        "return_clock": return_clock,
                        "return_time": return_time,
                    }
                )
    return cases


def case_key(row: dict[str, int | str]) -> tuple[int, int, str]:
    return (int(row["k"]), int(row["section_value_d"]), str(row["return_clock"]))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_csv(path: Path) -> tuple[list[dict[str, int | str]], dict[str, object]]:
    integer_columns = {
        "k",
        "q_k",
        "degree_d_k",
        "section_value_d",
        "return_time",
        "simultaneous_gcd_degree_mod_p",
        "prime",
    }
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != CSV_COLUMNS:
            raise AssertionError(f"unexpected CSV columns: {reader.fieldnames!r}")
        rows: list[dict[str, int | str]] = []
        for raw in reader:
            row = {
                key: int(value) if key in integer_columns else value
                for key, value in raw.items()
            }
            rows.append(row)

    expected = {case_key(row): row for row in expected_cases(MAX_K)}
    observed: dict[tuple[int, int, str], dict[str, int | str]] = {}
    for row in rows:
        key = case_key(row)
        if key in observed:
            raise AssertionError(f"duplicate CSV case: {key}")
        observed[key] = row
    if set(observed) != set(expected):
        missing = sorted(set(expected) - set(observed))
        extra = sorted(set(observed) - set(expected))
        raise AssertionError(f"CSV case-set mismatch: missing={missing}, extra={extra}")

    for key, baseline in expected.items():
        row = observed[key]
        for field, value in baseline.items():
            if row[field] != value:
                raise AssertionError(f"CSV field mismatch for {key}: {field}={row[field]!r}, expected {value!r}")
        if row["prime"] != PERSISTED_PRIME:
            raise AssertionError(f"CSV prime mismatch for {key}")
        if row["simultaneous_gcd_degree_mod_p"] != 0:
            raise AssertionError(f"persisted nonzero gcd degree for {key}")

    return rows, {
        "path": str(path),
        "sha256": sha256(path),
        "columns_exact": True,
        "row_count": len(rows),
        "row_set_exact": True,
        "unique_cases": len(observed),
        "persisted_prime": PERSISTED_PRIME,
        "persisted_degrees_all_zero": True,
    }


def require_mapping(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise AssertionError(f"{label} must be a JSON object")
    return value


def validate_certificate(path: Path) -> tuple[dict[str, object], dict[str, object]]:
    with path.open(encoding="utf-8") as handle:
        certificate = require_mapping(json.load(handle), "certificate")

    required_top_level = {
        "arithmetic",
        "candidate",
        "chronological_product_checks",
        "decision",
        "definitions",
        "first_nontrivial_approximant",
        "logical_type",
        "modular_gcd_summary",
    }
    missing = required_top_level - set(certificate)
    if missing:
        raise AssertionError(f"certificate missing keys: {sorted(missing)}")
    if certificate["candidate"] != "HCS-C13":
        raise AssertionError("unexpected certificate candidate")
    if not isinstance(certificate["decision"], str) or not certificate["decision"]:
        raise AssertionError("certificate decision must be a nonempty string")

    definitions = require_mapping(certificate["definitions"], "definitions")
    expected_definitions = {
        "trace_map": "T(x,y,z)=(2*x*y-z,x,y)",
        "initial_line": "ell_lambda(E)=((E-lambda)/2,E/2,1)",
        "fricke_invariant_on_line": "lambda**2/4",
        "discriminant_recurrence": "d[k+1]=d[k]*d[k-1]-d[k-2]",
    }
    for key, value in expected_definitions.items():
        if definitions.get(key) != value:
            raise AssertionError(f"certificate definition mismatch: {key}")

    summary = require_mapping(certificate["modular_gcd_summary"], "modular_gcd_summary")
    expected_summary = {
        "max_k": MAX_K,
        "prime": PERSISTED_PRIME,
        "tests": 48,
        "all_gcd_degrees_zero": True,
    }
    for key, value in expected_summary.items():
        if summary.get(key) != value:
            raise AssertionError(f"certificate summary mismatch: {key}")

    chronology = require_mapping(certificate["chronological_product_checks"], "chronological_product_checks")
    checks = chronology.get("checks")
    if not isinstance(checks, list) or len(checks) != 7:
        raise AssertionError("certificate must contain seven chronology checks for k=-1,...,5")
    if [row.get("k") for row in checks if isinstance(row, dict)] != list(range(-1, 6)):
        raise AssertionError("certificate chronology row set/order mismatch")
    if not all(isinstance(row, dict) and row.get("verified") is True for row in checks):
        raise AssertionError("certificate chronology contains an unverified row")

    return certificate, {
        "path": str(path),
        "sha256": sha256(path),
        "required_top_level_keys_present": True,
        "definitions_match": True,
        "summary_matches": True,
        "chronology_row_set_matches": True,
        "decision_is_nonempty_string": True,
    }


def prime_is_valid(prime: int) -> bool:
    if prime < 2:
        return False
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            return False
        divisor += 1 if divisor == 2 else 2
    return True


def run_modular_cases(
    traces: dict[int, Polynomial[int]],
    prime: int,
    cases: list[dict[str, int | str]],
) -> list[dict[str, int | str]]:
    if not prime_is_valid(prime):
        raise AssertionError(f"{prime} is not prime")
    rows: list[dict[str, int | str]] = []
    for case in cases:
        degree = simultaneous_gcd_degree_finite_field(
            traces=traces,
            k=int(case["k"]),
            section_value=int(case["section_value_d"]),
            return_time=int(case["return_time"]),
            prime=prime,
        )
        row = dict(case)
        row.update({"prime": prime, "simultaneous_gcd_degree": degree})
        rows.append(row)
    return rows


def run_rational_cases(
    traces: dict[int, Polynomial[int]],
    cases: list[dict[str, int | str]],
) -> list[dict[str, int | str]]:
    rows: list[dict[str, int | str]] = []
    for case in cases:
        if int(case["k"]) > RATIONAL_MAX_K:
            continue
        degree = simultaneous_gcd_degree_rational(
            traces=traces,
            k=int(case["k"]),
            section_value=int(case["section_value_d"]),
            return_time=int(case["return_time"]),
        )
        row = dict(case)
        row.update({"field": "Q", "simultaneous_gcd_degree": degree})
        rows.append(row)
    return rows


def compact_outcomes(rows: list[dict[str, int | str]]) -> list[dict[str, int | str]]:
    return [
        {
            "k": row["k"],
            "section_value_d": row["section_value_d"],
            "return_clock": row["return_clock"],
            "return_time": row["return_time"],
            "simultaneous_gcd_degree": row["simultaneous_gcd_degree"],
        }
        for row in rows
    ]


def build_report(results_dir: Path) -> dict[str, object]:
    csv_path = results_dir / "modular_gcd_audit.csv"
    certificate_path = results_dir / "certificate.json"
    csv_rows, csv_validation = validate_csv(csv_path)
    certificate, certificate_validation = validate_certificate(certificate_path)

    traces = integer_trace_polynomials(MAX_K)
    lengths = fibonacci_lengths(MAX_K)
    for k in range(-1, MAX_K + 1):
        if len(traces[k]) - 1 != lengths[k]:
            raise AssertionError(f"independent degree/length mismatch at k={k}")
    chronology = verify_chronology(traces, through_k=5)

    cases = expected_cases(MAX_K)
    first_prime_rows = run_modular_cases(traces, PERSISTED_PRIME, cases)
    second_prime_rows = run_modular_cases(traces, SECOND_PRIME, cases)
    rational_rows = run_rational_cases(traces, cases)

    persisted_by_key = {case_key(row): row for row in csv_rows}
    for row in first_prime_rows:
        persisted_degree = persisted_by_key[case_key(row)]["simultaneous_gcd_degree_mod_p"]
        if row["simultaneous_gcd_degree"] != persisted_degree:
            raise AssertionError(f"independent persisted-prime mismatch for {case_key(row)}")

    if not all(row["simultaneous_gcd_degree"] == 0 for row in first_prime_rows):
        raise AssertionError("persisted-prime independent audit found a positive-degree gcd")
    if not all(row["simultaneous_gcd_degree"] == 0 for row in second_prime_rows):
        raise AssertionError("second-prime audit found a positive-degree gcd")
    if not all(row["simultaneous_gcd_degree"] == 0 for row in rational_rows):
        raise AssertionError("rational audit found a positive-degree gcd")

    return {
        "checker": {
            "name": "HCS-C13 independent exact checker",
            "imports_trace_map_audit": False,
            "polynomial_representation": "independent ascending-coefficient tuples",
            "arithmetic": "pure exact integer, Fraction, and finite-field arithmetic",
        },
        "decision_seen_in_certificate": certificate["decision"],
        "persisted_artifacts": {
            "csv": csv_validation,
            "certificate": certificate_validation,
        },
        "independent_chronology": {
            "method": "direct left-ordered products of 2-by-2 site matrices",
            "tests": len(chronology),
            "all_match_reconstructed_recurrence": True,
            "checks": chronology,
        },
        "degree_length_check": {
            "range": "k=-1,...,8",
            "tests": MAX_K + 2,
            "all_degree_d_k_equal_q_k": True,
        },
        "persisted_prime_recomputation": {
            "prime": PERSISTED_PRIME,
            "tests": len(first_prime_rows),
            "all_gcd_degrees_zero": True,
            "all_degrees_match_persisted_csv": True,
            "outcomes": compact_outcomes(first_prime_rows),
        },
        "second_prime_recomputation": {
            "prime": SECOND_PRIME,
            "tests": len(second_prime_rows),
            "all_gcd_degrees_zero": True,
            "outcomes": compact_outcomes(second_prime_rows),
        },
        "rational_recomputation": {
            "field": "Q",
            "range": "k=1,...,5",
            "tests": len(rational_rows),
            "all_gcd_degrees_zero": True,
            "outcomes": compact_outcomes(rational_rows),
        },
        "overall_pass": True,
    }


def main() -> None:
    project_dir = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, default=project_dir / "results")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    output = args.output or args.results_dir / "independent_check.json"
    report = build_report(args.results_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(
        "independent HCS-C13 check passed: "
        "48 persisted-prime + 48 second-prime + 30 rational gcd tests; "
        f"wrote {output}"
    )


if __name__ == "__main__":
    main()
