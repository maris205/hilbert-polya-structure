#!/usr/bin/env python3
"""Independent checker for the HCS-C16 compact certificates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


EXPECTED_BOX_COUNTS = {10: 48, 20: 191, 40: 742, 80: 2970, 160: 11841, 320: 47349}
EXPECTED_HEIGHT_COUNTS = {10: 10, 20: 36, 40: 144, 80: 577, 160: 2306, 320: 9211, 640: 36857}


def v13(value: Fraction) -> int:
    value = Fraction(value)
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


def exact_invariants(m: int, n: int):
    a, b = alpha(m, n)
    norm = a * a - 3 * b * b
    trace = 2 * a
    discriminant = trace * trace - 4 * norm
    tree = max(0, v13(norm) - v13(discriminant))
    return norm, trace, discriminant, tree


def brute_box(bound: int) -> int:
    root3 = math.sqrt(3.0)
    a = 2.0 * math.log(2.0 + root3)
    c = math.log((4.0 + root3) / (4.0 - root3))
    max_m = math.ceil((bound + abs(c) * bound) / a) + 2
    count = 0
    for n in range(bound + 1):
        for m in range(-max_m, max_m + 1):
            if not (n > 0 or (n == 0 and m > 0)):
                continue
            if math.gcd(abs(m), n) != 1:
                continue
            if abs(m * a + n * c) <= bound:
                count += 1
    return count


def brute_height(bound: int) -> int:
    root3 = math.sqrt(3.0)
    a = 2.0 * math.log(2.0 + root3)
    c = math.log((4.0 + root3) / (4.0 - root3))
    log_p = math.log(13.0)
    max_n = math.floor(bound / log_p)
    max_m = math.ceil((bound + abs(c) * max_n) / a) + 2
    count = 0
    for n in range(max_n + 1):
        for m in range(-max_m, max_m + 1):
            if not (n > 0 or (n == 0 and m > 0)):
                continue
            if math.gcd(abs(m), n) != 1:
                continue
            if abs(m * a + n * c) + log_p * n <= bound:
                count += 1
    return count


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            hasher.update(block)
    return hasher.hexdigest()


def check(results: Path) -> dict[str, object]:
    with (results / "exact_certificates.json").open(encoding="utf-8") as handle:
        certificate = json.load(handle)
    with (results / "primitive_box_counts.csv").open(encoding="utf-8") as handle:
        box_rows = list(csv.DictReader(handle))
    with (results / "primitive_height_counts.csv").open(encoding="utf-8") as handle:
        height_rows = list(csv.DictReader(handle))

    checks: dict[str, bool] = {}
    checks["quaternion_ramification_signature"] = certificate["arithmetic_model"][
        "hilbert_symbols"
    ] == {"at_13": 1, "at_2": -1, "at_3": -1, "at_infinity": 1}
    checks["generator_norms"] = (
        certificate["generators"]["epsilon"]["norm"] == "1"
        and certificate["generators"]["pi"]["norm"] == "13"
    )

    sample_ok = True
    for row in certificate["sample_elements"]:
        m, n = int(row["m"]), int(row["n"])
        norm, trace, discriminant, tree = exact_invariants(m, n)
        sample_ok &= norm == Fraction(13) ** n
        sample_ok &= str(trace) == row["trace"]
        sample_ok &= str(discriminant) == row["discriminant"]
        sample_ok &= tree == abs(n) == int(row["tree_length"])
        sample_ok &= bool(row["primitive"]) == (math.gcd(abs(m), abs(n)) == 1)
    checks["sample_invariants_rederived"] = sample_ok

    expected_from_file = {int(row["real_bound"]): int(row["count_mod_inverse"]) for row in box_rows}
    checks["frozen_box_counts"] = expected_from_file == EXPECTED_BOX_COUNTS
    checks["independent_bruteforce_counts"] = all(
        brute_box(bound) == expected for bound, expected in EXPECTED_BOX_COUNTS.items()
    )
    expected_heights_from_file = {
        int(row["height_bound"]): int(row["count_mod_inverse"]) for row in height_rows
    }
    checks["frozen_height_counts"] = expected_heights_from_file == EXPECTED_HEIGHT_COUNTS
    checks["independent_height_counts"] = all(
        brute_height(bound) == expected for bound, expected in EXPECTED_HEIGHT_COUNTS.items()
    )

    records = certificate["near_wall_records"]
    tail = [row for row in records if int(row["n"]) >= 3]
    checks["near_wall_is_primitive"] = all(
        math.gcd(abs(int(row["m"])), int(row["n"])) == 1 for row in tail
    )
    checks["near_wall_record_lengths_decrease"] = all(
        float(tail[index + 1]["real_length"]) < float(tail[index]["real_length"])
        for index in range(len(tail) - 1)
    )
    checks["near_wall_tree_lengths_increase"] = all(
        int(tail[index + 1]["tree_length"]) > int(tail[index]["tree_length"])
        for index in range(len(tail) - 1)
    )
    checks["unweighted_factor_diverges_along_records"] = all(
        float(tail[index + 1]["unweighted_log_local_factor_s1"])
        > float(tail[index]["unweighted_log_local_factor_s1"])
        for index in range(len(tail) - 1)
    )
    checks["height_is_proper_along_records"] = all(
        float(tail[index + 1]["height"]) > float(tail[index]["height"])
        for index in range(len(tail) - 1)
    )
    checks["rank_two_clock"] = abs(
        float(certificate["joint_clock"]["basis_determinant"])
        - 2.0 * math.log(2.0 + math.sqrt(3.0))
    ) < 1e-14
    checks["asymptotic_lattice_count"] = abs(
        float(box_rows[-1]["observed_over_prediction"]) - 1.0
    ) < 0.01
    checks["asymptotic_height_count"] = abs(
        float(height_rows[-1]["observed_over_prediction"]) - 1.0
    ) < 0.01

    with (results / "artifact_hashes.json").open(encoding="utf-8") as handle:
        hashes = json.load(handle)
    checks["artifact_hashes"] = all(
        digest(results / filename) == expected for filename, expected in hashes.items()
    )

    return {
        "candidate_id": "HCS-C16",
        "checks": checks,
        "all_passed": all(checks.values()),
        "check_count": len(checks),
        "independence_note": (
            "The checker reimplements quadratic multiplication, valuations, "
            "and box enumeration without importing the producer."
        ),
    }


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
