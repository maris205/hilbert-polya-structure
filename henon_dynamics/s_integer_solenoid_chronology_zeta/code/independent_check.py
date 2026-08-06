#!/usr/bin/env python3
"""Independent exact checker for the persisted HCS-C14 certificate.

This file deliberately does not import ``solenoid_zeta.py``.  It uses nested
matrix tuples, direct binary-word enumeration, and a characteristic-polynomial
recurrence for repetitions.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from itertools import product
from pathlib import Path


Matrix = tuple[tuple[int, int], tuple[int, int]]
EYE: Matrix = ((1, 0), (0, 1))
GEN_A: Matrix = ((3, 1), (1, 3))
GEN_B: Matrix = ((3, 2), (2, 4))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def determinant(matrix: Matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace(matrix: Matrix) -> int:
    return matrix[0][0] + matrix[1][1]


def ordered_product(word: str) -> Matrix:
    result = EYE
    for symbol in word:
        result = multiply(GEN_A if symbol == "a" else GEN_B, result)
    return result


def valuation_two(value: int) -> int:
    valuation = 0
    while value % 2 == 0:
        value //= 2
        valuation += 1
    return valuation


def fixed_data(matrix: Matrix) -> tuple[int, int, int]:
    fixed_determinant = 1 - trace(matrix) + determinant(matrix)
    valuation = valuation_two(fixed_determinant)
    return fixed_determinant, valuation, fixed_determinant >> valuation


def lucas(number: int) -> int:
    values = [2, 1]
    while len(values) <= number:
        values.append(values[-1] + values[-2])
    return values[number]


def cyclic_no_aa(word: str) -> bool:
    return all(
        not (word[index] == "a" and word[(index + 1) % len(word)] == "a")
        for index in range(len(word))
    )


def trace_power_recurrence(base_trace: int, base_det: int, exponent: int) -> int:
    if exponent == 0:
        return 2
    if exponent == 1:
        return base_trace
    previous, current = 2, base_trace
    for _ in range(2, exponent + 1):
        previous, current = current, base_trace * current - base_det * previous
    return current


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def mobius(number: int) -> int:
    """Return the Moebius function without using the producer."""
    remaining = number
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            prime_factors += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def divisors(number: int) -> list[int]:
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def zeta_coefficients(fixed_counts: dict[int, int]) -> dict[int, int]:
    """Recompute exp(sum N_n z^n/n) by its exact coefficient recurrence."""
    coefficients = {0: 1}
    for degree in range(1, max(fixed_counts) + 1):
        numerator = sum(
            fixed_counts[index] * coefficients[degree - index]
            for index in range(1, degree + 1)
        )
        if numerator % degree:
            raise AssertionError(f"nonintegral independent zeta coefficient at n={degree}")
        coefficients[degree] = numerator // degree
    return coefficients


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check(results_directory: Path, max_period: int) -> dict[str, object]:
    certificate_path = results_directory / "certificate.json"
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    periodic_csv = read_csv(results_directory / "periodic_counts.csv")
    persisted_rows = {int(row["period"]): row for row in periodic_csv}

    period_checks: list[dict[str, int | bool]] = []
    for period in range(1, max_period + 1):
        archimedean = 0
        solenoid = 0
        active = 0
        language = 0
        for symbols in product("ab", repeat=period):
            word = "".join(symbols)
            matrix = ordered_product(word)
            if determinant(matrix) != 8**period:
                raise AssertionError("independent determinant invariant failed")
            fixed_det, valuation, fixed = fixed_data(matrix)
            archimedean += fixed_det
            solenoid += fixed
            active += int(valuation > 0)
            language += int(cyclic_no_aa(word))
        row = persisted_rows[period]
        passed = (
            archimedean == int(row["archimedean_fixed_points"])
            and solenoid == int(row["solenoid_fixed_points"])
            and active == language == lucas(period)
        )
        if not passed:
            raise AssertionError(f"independent period check failed at n={period}")
        period_checks.append(
            {
                "period": period,
                "archimedean": archimedean,
                "solenoid": solenoid,
                "active_words": active,
                "passed": passed,
            }
        )

    witness_checks: list[dict[str, object]] = []
    for word, expected_trace, expected_det, expected_fixed in (
        ("aabbb", 2734, 30035, 30035),
        ("ababb", 2727, 30042, 15021),
    ):
        matrix = ordered_product(word)
        fixed_det, valuation, fixed = fixed_data(matrix)
        passed = trace(matrix) == expected_trace and fixed_det == expected_det and fixed == expected_fixed
        if not passed:
            raise AssertionError(f"independent witness check failed for {word}")
        witness_checks.append(
            {
                "word": word,
                "trace": trace(matrix),
                "fixed_determinant": fixed_det,
                "v2": valuation,
                "fixed_count": fixed,
                "passed": passed,
            }
        )

    repetition_checks: list[dict[str, int | bool]] = []
    rational_trace, boundary_trace, base_det = 2734, 2727, 32768
    for repetition in range(1, 21):
        rational_fixed = base_det**repetition - trace_power_recurrence(rational_trace, base_det, repetition) + 1
        boundary_fixed = base_det**repetition - trace_power_recurrence(boundary_trace, base_det, repetition) + 1
        rational_v2 = valuation_two(rational_fixed)
        boundary_v2 = valuation_two(boundary_fixed)
        expected = 1 if repetition % 2 else 3 + valuation_two(repetition)
        passed = rational_v2 == 0 and boundary_v2 == expected
        if not passed:
            raise AssertionError(f"independent repetition law failed at r={repetition}")
        repetition_checks.append(
            {
                "repetition": repetition,
                "rational_v2": rational_v2,
                "boundary_v2": boundary_v2,
                "expected_boundary_v2": expected,
                "passed": passed,
            }
        )

    # Cross-format checks cover the full persisted cutoff, independently of
    # the more expensive direct word enumeration cutoff above.
    fixed_counts = {
        period: int(row["solenoid_fixed_points"])
        for period, row in persisted_rows.items()
    }
    independent_zeta = zeta_coefficients(fixed_counts)
    periodic_cross_checks: list[dict[str, int | bool]] = []
    for period, row in sorted(persisted_rows.items()):
        exact_period_points = sum(
            mobius(divisor) * fixed_counts[period // divisor]
            for divisor in divisors(period)
        )
        if exact_period_points % period:
            raise AssertionError(f"independent Dold divisibility failed at n={period}")
        primitive_orbits = exact_period_points // period
        passed = (
            exact_period_points == int(row["exact_period_points"])
            and primitive_orbits == int(row["primitive_orbits"])
            and independent_zeta[period] == int(row["zeta_coefficient"])
            and int(row["valuation_correction"])
            == int(row["archimedean_fixed_points"]) - int(row["solenoid_fixed_points"])
            and row["valuation_identity_passed"] == "True"
        )
        if not passed or exact_period_points < 0:
            raise AssertionError(f"independent periodic cross-check failed at n={period}")
        periodic_cross_checks.append(
            {
                "period": period,
                "exact_period_points": exact_period_points,
                "primitive_orbits": primitive_orbits,
                "zeta_coefficient": independent_zeta[period],
                "passed": passed,
            }
        )

    valuation_rows = read_csv(results_directory / "valuation_distribution.csv")
    valuation_cross_checks: list[dict[str, int | bool]] = []
    for period, periodic_row in sorted(persisted_rows.items()):
        rows = [row for row in valuation_rows if int(row["period"]) == period]
        reconstructed = {
            "word_count": sum(int(row["word_count"]) for row in rows),
            "archimedean_mass": sum(int(row["archimedean_mass"]) for row in rows),
            "solenoid_mass": sum(int(row["solenoid_mass"]) for row in rows),
            "correction_mass": sum(int(row["correction_mass"]) for row in rows),
            "active_words": sum(int(row["word_count"]) for row in rows if int(row["v2"]) > 0),
        }
        passed = (
            reconstructed["word_count"] == 2**period
            and reconstructed["archimedean_mass"] == int(periodic_row["archimedean_fixed_points"])
            and reconstructed["solenoid_mass"] == int(periodic_row["solenoid_fixed_points"])
            and reconstructed["correction_mass"] == int(periodic_row["valuation_correction"])
            and reconstructed["active_words"] == int(periodic_row["active_even_words"])
        )
        if not passed:
            raise AssertionError(f"valuation-distribution reconstruction failed at n={period}")
        valuation_cross_checks.append({"period": period, **reconstructed, "passed": passed})

    congruence_rows = read_csv(results_directory / "congruence_tower.csv")
    congruence_passed = all(
        row["passed_nonnegative"] == "True"
        and row["passed_against_direct_enumeration"] == "True"
        and row["divisible_words"] == row["direct_divisible_words"]
        and row["divisible_archimedean_mass"] == row["direct_divisible_archimedean_mass"]
        for row in congruence_rows
    )
    if not congruence_passed:
        raise AssertionError("congruence-tower cross-format audit failed")

    certificate_periods = certificate["periodic_counts"]
    if len(certificate_periods) != len(periodic_csv):
        raise AssertionError("certificate/periodic CSV length mismatch")
    for certificate_row, csv_row in zip(certificate_periods, periodic_csv):
        for key, value in certificate_row.items():
            expected = str(value)
            if isinstance(value, bool):
                expected = str(value)
            if csv_row[key] != expected:
                raise AssertionError(f"certificate/periodic CSV mismatch at {key}")

    witness_file = json.loads(
        (results_directory / "chronology_witnesses.json").read_text(encoding="utf-8")
    )
    witness_matches_certificate = witness_file == certificate["chronology_analytic_type_witness"]
    if not witness_matches_certificate:
        raise AssertionError("certificate/witness JSON mismatch")

    return {
        "schema": "hcs-c14-independent-check-v2",
        "independent_of_producer_import": True,
        "certificate_schema_seen": certificate["schema"],
        "period_checks": period_checks,
        "witness_checks": witness_checks,
        "repetition_checks": repetition_checks,
        "cross_artifact_checks": {
            "periodic_rows": periodic_cross_checks,
            "valuation_rows": valuation_cross_checks,
            "congruence_rows_checked": len(congruence_rows),
            "congruence_rows_all_pass": congruence_passed,
            "certificate_periodic_csv_match": True,
            "certificate_witness_json_match": witness_matches_certificate,
        },
        "artifact_hashes_before_independent_output": {
            name: file_sha256(results_directory / name)
            for name in (
                "certificate.json",
                "periodic_counts.csv",
                "valuation_distribution.csv",
                "congruence_tower.csv",
                "chronology_witnesses.json",
                "recurrence_screen.json",
            )
        },
        "all_pass": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    parser.add_argument("--max-period", type=int, default=10)
    arguments = parser.parse_args()
    payload = check(arguments.results, arguments.max_period)
    output = arguments.results / "independent_check.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
