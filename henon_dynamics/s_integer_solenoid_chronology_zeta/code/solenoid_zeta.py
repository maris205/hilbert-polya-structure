#!/usr/bin/env python3
"""Exact producer for HCS-C14.

The script studies a chronological two-letter skew product over the full
two-shift with fibre the dyadic two-solenoid

    X_2 = dual(Z[1/2]^2).

The two module matrices are

    A = [[3, 1], [1, 3]],   B = [[3, 2], [2, 4]].

Both determinants are 8, which is a unit of Z[1/2].  We use the convention
alpha_M = dual(M^T), so appending a later symbol multiplies its matrix on the
left.  No transition matrix is averaged before chronological word products
are formed.

Only the Python standard library is required.  All primary outputs are exact
integers, fractions, or finite exhaustive checks.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable


Matrix = tuple[int, int, int, int]

IDENTITY: Matrix = (1, 0, 0, 1)
A: Matrix = (3, 1, 1, 3)
B: Matrix = (3, 2, 2, 4)

# Uniform-sign rational-collapse control.
U: Matrix = (1, 1, 0, 1)
V: Matrix = (1, 0, 1, 1)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def mat_mul_mod(left: Matrix, right: Matrix, modulus: int) -> Matrix:
    return tuple(x % modulus for x in mat_mul(left, right))  # type: ignore[return-value]


def mat_trace(matrix: Matrix) -> int:
    return matrix[0] + matrix[3]


def mat_det(matrix: Matrix) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def mat_pow(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("negative matrix powers are not used")
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = mat_mul(base, result)
        base = mat_mul(base, base)
        power >>= 1
    return result


def return_matrix(word: str, first: Matrix = A, second: Matrix = B) -> Matrix:
    """Return M_{w[n-1]} ... M_{w[0]} (later symbols act on the left)."""

    result = IDENTITY
    for symbol in word:
        if symbol == "a":
            result = mat_mul(first, result)
        elif symbol == "b":
            result = mat_mul(second, result)
        else:
            raise ValueError(f"unknown symbol {symbol!r}")
    return result


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is only called on positive fixed-point determinants")
    valuation = 0
    while value % 2 == 0:
        value //= 2
        valuation += 1
    return valuation


def odd_part(value: int) -> int:
    return value >> v2(value)


def fixed_determinant(matrix: Matrix) -> int:
    """det(I-M), positive for every nonempty word in the frozen family."""

    return 1 - mat_trace(matrix) + mat_det(matrix)


def solenoid_fixed_count(matrix: Matrix) -> int:
    determinant = fixed_determinant(matrix)
    if determinant <= 0:
        raise AssertionError("the frozen expanding family must have det(I-M)>0")
    return odd_part(determinant)


def canonical_rotation(word: str) -> str:
    return min(word[index:] + word[:index] for index in range(len(word)))


def canonical_dihedral(word: str) -> str:
    reverse = word[::-1]
    rotations = [word[index:] + word[:index] for index in range(len(word))]
    rotations += [reverse[index:] + reverse[:index] for index in range(len(word))]
    return min(rotations)


def is_primitive_word(word: str) -> bool:
    length = len(word)
    for divisor in range(1, length):
        if length % divisor == 0 and word == word[:divisor] * (length // divisor):
            return False
    return True


def cyclic_no_aa(word: str) -> bool:
    return all(
        not (word[index] == "a" and word[(index + 1) % len(word)] == "a")
        for index in range(len(word))
    )


def lucas(number: int) -> int:
    if number == 0:
        return 2
    if number == 1:
        return 1
    previous, current = 2, 1
    for _ in range(2, number + 1):
        previous, current = current, previous + current
    return current


def fibonacci(number: int) -> int:
    previous, current = 0, 1
    for _ in range(number):
        previous, current = current, previous + current
    return previous


def mobius(number: int) -> int:
    if number == 1:
        return 1
    remaining = number
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_count += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def divisors(number: int) -> list[int]:
    result: list[int] = []
    for divisor in range(1, math.isqrt(number) + 1):
        if number % divisor == 0:
            result.append(divisor)
            if divisor * divisor != number:
                result.append(number // divisor)
    return sorted(result)


def primitive_ledger(counts: dict[int, int]) -> tuple[dict[int, int], dict[int, int]]:
    exact_points: dict[int, int] = {}
    primitive_orbits: dict[int, int] = {}
    for period in sorted(counts):
        exact = sum(mobius(period // divisor) * counts[divisor] for divisor in divisors(period))
        if exact < 0 or exact % period:
            raise AssertionError(f"Dold condition failed at period {period}")
        exact_points[period] = exact
        primitive_orbits[period] = exact // period
    return exact_points, primitive_orbits


def zeta_coefficients(counts: dict[int, int]) -> dict[int, int]:
    """Use n a_n = sum_{k=1}^n N_k a_{n-k}, with a_0=1."""

    coefficients = {0: 1}
    for degree in sorted(counts):
        numerator = sum(counts[index] * coefficients[degree - index] for index in range(1, degree + 1))
        if numerator % degree:
            raise AssertionError(f"zeta coefficient is nonintegral at degree {degree}")
        coefficients[degree] = numerator // degree
    return coefficients


def berlekamp_massey(sequence: list[int], prime: int) -> tuple[int, list[int]]:
    """Minimal recurrence over F_prime for a finite prefix (screening only)."""

    connection = [1]
    previous = [1]
    length = 0
    shift = 1
    discrepancy_scale = 1
    for index in range(len(sequence)):
        discrepancy = sequence[index] % prime
        for offset in range(1, length + 1):
            discrepancy = (discrepancy + connection[offset] * sequence[index - offset]) % prime
        if discrepancy == 0:
            shift += 1
            continue
        old_connection = connection[:]
        multiplier = discrepancy * pow(discrepancy_scale, -1, prime) % prime
        needed = len(previous) + shift
        if len(connection) < needed:
            connection.extend([0] * (needed - len(connection)))
        for offset, coefficient in enumerate(previous):
            connection[offset + shift] = (
                connection[offset + shift] - multiplier * coefficient
            ) % prime
        if 2 * length <= index:
            length = index + 1 - length
            previous = old_connection
            discrepancy_scale = discrepancy
            shift = 1
        else:
            shift += 1
    return length, connection


@dataclass
class ValuationRow:
    word_count: int = 0
    archimedean_mass: int = 0
    solenoid_mass: int = 0
    correction_mass: int = 0


@dataclass
class PeriodRow:
    solenoid_count: int = 0
    archimedean_count: int = 0
    valuations: dict[int, ValuationRow] = field(default_factory=lambda: defaultdict(ValuationRow))


def enumerate_periodic_counts(max_period: int) -> dict[int, PeriodRow]:
    rows = {period: PeriodRow() for period in range(1, max_period + 1)}

    def visit(depth: int, matrix: Matrix) -> None:
        if depth:
            if mat_det(matrix) != 8**depth:
                raise AssertionError("chronological determinant invariant failed")
            determinant = fixed_determinant(matrix)
            if determinant <= 0:
                raise AssertionError("a non-expanding return entered the frozen family")
            valuation = v2(determinant)
            fixed = determinant >> valuation
            row = rows[depth]
            row.archimedean_count += determinant
            row.solenoid_count += fixed
            valuation_row = row.valuations[valuation]
            valuation_row.word_count += 1
            valuation_row.archimedean_mass += determinant
            valuation_row.solenoid_mass += fixed
            valuation_row.correction_mass += determinant - fixed
        if depth == max_period:
            return
        visit(depth + 1, mat_mul(A, matrix))
        visit(depth + 1, mat_mul(B, matrix))

    visit(0, IDENTITY)
    return rows


def word_record(word: str) -> dict[str, object]:
    matrix = return_matrix(word)
    determinant = fixed_determinant(matrix)
    valuation = v2(determinant)
    return {
        "word": word,
        "length": len(word),
        "parikh": {"a": word.count("a"), "b": word.count("b")},
        "matrix": [[matrix[0], matrix[1]], [matrix[2], matrix[3]]],
        "trace": mat_trace(matrix),
        "matrix_determinant": mat_det(matrix),
        "fixed_determinant": determinant,
        "v2_fixed_determinant": valuation,
        "solenoid_fixed_count": determinant >> valuation,
        "primitive": is_primitive_word(word),
        "canonical_rotation": canonical_rotation(word),
        "canonical_dihedral": canonical_dihedral(word),
        "cyclic_no_aa": cyclic_no_aa(word),
        "fiber_zeta_type": "natural_boundary" if mat_trace(matrix) % 2 else "rational",
    }


def witness_package() -> dict[str, object]:
    rational_word = word_record("aabbb")
    boundary_word = word_record("ababb")
    if rational_word["parikh"] != boundary_word["parikh"]:
        raise AssertionError("witness Parikh vectors differ")
    if rational_word["canonical_dihedral"] == boundary_word["canonical_dihedral"]:
        raise AssertionError("witnesses are dihedrally equivalent")

    repetition_rows: list[dict[str, int]] = []
    rational_matrix = return_matrix("aabbb")
    boundary_matrix = return_matrix("ababb")
    for repetition in range(1, 13):
        rational_det = fixed_determinant(mat_pow(rational_matrix, repetition))
        boundary_det = fixed_determinant(mat_pow(boundary_matrix, repetition))
        expected_boundary_v2 = 1 if repetition % 2 else 3 + v2(repetition)
        if v2(rational_det) != 0 or v2(boundary_det) != expected_boundary_v2:
            raise AssertionError("repetition valuation law failed")
        repetition_rows.append(
            {
                "repetition": repetition,
                "rational_word_v2": v2(rational_det),
                "rational_word_fixed_count": odd_part(rational_det),
                "boundary_word_v2": v2(boundary_det),
                "boundary_word_expected_v2": expected_boundary_v2,
                "boundary_word_fixed_count": odd_part(boundary_det),
            }
        )

    return {
        "rational_word": rational_word,
        "natural_boundary_word": boundary_word,
        "same_parikh": True,
        "not_cyclic_or_dihedral_equivalent": True,
        "rational_subsystem_factor": {
            "variable": "t=z^5",
            "formula": "(1-2734*t+32768*t^2)/((1-t)*(1-32768*t))",
        },
        "natural_boundary_subsystem": {
            "fiber_radius": "1/32768",
            "skew_product_z_radius": "1/8",
            "source_theorem": "Bell-Miles-Ward Theorem 15 and Example 18",
        },
        "repetition_checks": repetition_rows,
    }


def parity_language_audit(max_period: int) -> dict[str, object]:
    rows: list[dict[str, int | bool]] = []
    all_pass = True
    for period in range(1, max_period + 1):
        active = 0
        language = 0
        mismatches = 0
        for symbols in product("ab", repeat=period):
            word = "".join(symbols)
            determinant_even = fixed_determinant(return_matrix(word)) % 2 == 0
            no_aa = cyclic_no_aa(word)
            active += int(determinant_even)
            language += int(no_aa)
            mismatches += int(determinant_even != no_aa)
        expected = lucas(period)
        passed = active == language == expected and mismatches == 0
        all_pass &= passed
        rows.append(
            {
                "period": period,
                "even_determinant_words": active,
                "cyclic_no_aa_words": language,
                "lucas_number": expected,
                "mismatches": mismatches,
                "passed": passed,
            }
        )
    return {"all_pass": all_pass, "rows": rows}


def control_package(max_period: int) -> dict[str, object]:
    checks: list[dict[str, int | bool]] = []
    for period in range(1, max_period + 1):
        observed = 0
        for symbols in product("ab", repeat=period):
            matrix = return_matrix("".join(symbols), U, V)
            numerator = 4**period - 2**period * mat_trace(matrix) + 1
            if numerator <= 0 or numerator % 2 == 0:
                raise AssertionError("uniform-sign control assumptions failed")
            observed += numerator
        expected = 8**period - 6**period
        checks.append(
            {
                "period": period,
                "observed_fixed_points": observed,
                "expected_8n_minus_6n": expected,
                "passed": observed == expected,
            }
        )
    first = word_record_control("aabbb")
    second = word_record_control("ababb")
    return {
        "matrices": {"U": [[1, 1], [0, 1]], "V": [[1, 0], [1, 1]], "denominator": 2},
        "zeta": "(1-6*z)/(1-8*z)",
        "aggregate_checks": checks,
        "primitive_same_parikh_witness": [first, second],
        "interpretation": "orbit chronology survives but the scalar zeta collapses exactly",
    }


def word_record_control(word: str) -> dict[str, object]:
    matrix = return_matrix(word, U, V)
    numerator = 4 ** len(word) - 2 ** len(word) * mat_trace(matrix) + 1
    return {
        "word": word,
        "trace": mat_trace(matrix),
        "fixed_count": numerator,
        "primitive": is_primitive_word(word),
        "parikh": {"a": word.count("a"), "b": word.count("b")},
    }


def congruence_tower_audit(max_period: int, max_level: int) -> list[dict[str, int | bool]]:
    """Independent finite-monoid recurrence for divisibility-layer masses."""

    output: list[dict[str, int | bool]] = []
    for level in range(1, max_level + 1):
        modulus = 2**level
        states: dict[Matrix, tuple[int, Matrix]] = {
            tuple(x % modulus for x in IDENTITY): (1, (1, 0, 0, 1))
        }
        for period in range(1, max_period + 1):
            next_counts: dict[Matrix, int] = defaultdict(int)
            next_sums: dict[Matrix, list[int]] = {}
            for residue, (count, matrix_sum) in states.items():
                for generator in (A, B):
                    target = mat_mul_mod(generator, residue, modulus)
                    lifted_sum = mat_mul(generator, matrix_sum)
                    next_counts[target] += count
                    if target not in next_sums:
                        next_sums[target] = [0, 0, 0, 0]
                    for index, value in enumerate(lifted_sum):
                        next_sums[target][index] += value
            states = {
                residue: (next_counts[residue], tuple(next_sums[residue]))  # type: ignore[arg-type]
                for residue in next_counts
            }
            layer_mass = 0
            divisible_words = 0
            det_power = 8**period
            for residue, (count, matrix_sum) in states.items():
                determinant_residue = (1 - mat_trace(residue) + det_power) % modulus
                if determinant_residue == 0:
                    divisible_words += count
                    layer_mass += count * (det_power + 1) - mat_trace(matrix_sum)
            output.append(
                {
                    "level": level,
                    "period": period,
                    "reachable_residue_states": len(states),
                    "divisible_words": divisible_words,
                    "divisible_archimedean_mass": layer_mass,
                    "passed_nonnegative": layer_mass >= 0,
                }
            )
    return output


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def produce(output_directory: Path, max_period: int, parity_period: int, tower_level: int) -> None:
    output_directory.mkdir(parents=True, exist_ok=True)
    rows = enumerate_periodic_counts(max_period)
    solenoid_counts = {period: row.solenoid_count for period, row in rows.items()}
    exact_points, primitive_orbits = primitive_ledger(solenoid_counts)
    zeta = zeta_coefficients(solenoid_counts)

    periodic_rows: list[dict[str, object]] = []
    valuation_rows: list[dict[str, object]] = []
    for period, row in rows.items():
        expected_arch = 16**period + 2**period - (
            # A+B has trace 13 and determinant 33.
            mat_trace(mat_pow(mat_add(A, B), period))
        )
        if row.archimedean_count != expected_arch:
            raise AssertionError(f"archimedean collapse failed at period {period}")
        active = sum(value.word_count for valuation, value in row.valuations.items() if valuation > 0)
        if active != lucas(period):
            raise AssertionError(f"Lucas parity count failed at period {period}")
        correction = row.archimedean_count - row.solenoid_count
        maximum_valuation = max(row.valuations)
        reconstructed = Fraction(row.archimedean_count, 1)
        for level in range(1, maximum_valuation + 1):
            divisible_mass = sum(
                value.archimedean_mass
                for valuation, value in row.valuations.items()
                if valuation >= level
            )
            reconstructed -= Fraction(divisible_mass, 2**level)
        if reconstructed.denominator != 1 or reconstructed.numerator != row.solenoid_count:
            raise AssertionError(f"valuation-layer identity failed at period {period}")
        periodic_rows.append(
            {
                "period": period,
                "solenoid_fixed_points": row.solenoid_count,
                "archimedean_fixed_points": row.archimedean_count,
                "valuation_correction": correction,
                "active_even_words": active,
                "lucas_number": lucas(period),
                "exact_period_points": exact_points[period],
                "primitive_orbits": primitive_orbits[period],
                "zeta_coefficient": zeta[period],
                "valuation_identity_passed": True,
            }
        )
        for valuation in sorted(row.valuations):
            value = row.valuations[valuation]
            valuation_rows.append(
                {
                    "period": period,
                    "v2": valuation,
                    "word_count": value.word_count,
                    "archimedean_mass": value.archimedean_mass,
                    "solenoid_mass": value.solenoid_mass,
                    "correction_mass": value.correction_mass,
                }
            )

    parity = parity_language_audit(min(parity_period, max_period))
    if not parity["all_pass"]:
        raise AssertionError("parity language audit failed")

    control = control_package(min(10, max_period))
    congruence = congruence_tower_audit(min(12, max_period), tower_level)
    for layer_row in congruence:
        period = int(layer_row["period"])
        level = int(layer_row["level"])
        direct_words = sum(
            value.word_count
            for valuation, value in rows[period].valuations.items()
            if valuation >= level
        )
        direct_mass = sum(
            value.archimedean_mass
            for valuation, value in rows[period].valuations.items()
            if valuation >= level
        )
        layer_row["direct_divisible_words"] = direct_words
        layer_row["direct_divisible_archimedean_mass"] = direct_mass
        layer_row["passed_against_direct_enumeration"] = (
            int(layer_row["divisible_words"]) == direct_words
            and int(layer_row["divisible_archimedean_mass"]) == direct_mass
        )
        if not layer_row["passed_against_direct_enumeration"]:
            raise AssertionError(
                f"congruence tower mismatch at level={level}, period={period}"
            )

    recurrence_primes = [1_000_003, 1_000_033, 1_000_037]
    recurrence_screen = []
    solenoid_sequence = [solenoid_counts[index] for index in range(1, max_period + 1)]
    correction_sequence = [
        rows[index].archimedean_count - rows[index].solenoid_count
        for index in range(1, max_period + 1)
    ]
    arch_sequence = [rows[index].archimedean_count for index in range(1, max_period + 1)]
    for label, sequence in (
        ("solenoid", solenoid_sequence),
        ("valuation_correction", correction_sequence),
        ("archimedean_control", arch_sequence),
    ):
        for prime in recurrence_primes:
            order, connection = berlekamp_massey(sequence, prime)
            recurrence_screen.append(
                {
                    "sequence": label,
                    "prime": prime,
                    "prefix_length": len(sequence),
                    "berlekamp_massey_order": order,
                    "connection": connection,
                    "evidence_label": "finite_prefix_screen_only",
                }
            )

    witnesses = witness_package()
    certificate = {
        "schema": "hcs-c14-solenoid-zeta-certificate-v1",
        "candidate_id": "HCS-C14",
        "generated_date": "2026-08-06",
        "phase_space": "Sigma_2 x dual(Z[1/2]^2)",
        "clock": "one chronological full-shift step",
        "dual_convention": "alpha_M=dual(M^T); later symbols multiply on the left",
        "matrices": {
            "A": [[3, 1], [1, 3]],
            "B": [[3, 2], [2, 4]],
            "determinants": [8, 8],
            "A_plus_B": [[6, 3], [3, 7]],
        },
        "fixed_point_formula": "#Fix(alpha_M)=det(I-M)*|det(I-M)|_2=oddpart(det(I-M))",
        "archimedean_zeta": "(1-13*z+33*z^2)/((1-2*z)*(1-16*z))",
        "solenoid_zeta": "exp(sum_{n>=1} N_n*z^n/n)",
        "global_continuation": {
            "primary_radius": "1/16",
            "primary_divisor": "simple pole at z=1/16",
            "correction_growth_rate": "8*phi",
            "zero_free_continuation_after_primary_pole": "|z|<1/(8*phi)",
            "first_circle_natural_boundary": False,
            "later_natural_boundary": "OPEN",
        },
        "periodic_counts": periodic_rows,
        "parity_language": parity,
        "chronology_analytic_type_witness": witnesses,
        "uniform_sign_collapse_control": control,
        "recurrence_screen": recurrence_screen,
        "congruence_tower": {
            "identity": "oddpart(d)=d*(1-sum_{k>=1}2^(-k)*1_{2^k|d})",
            "finite_monoid_rows": congruence,
        },
        "claim_boundaries": [
            "Bell-Miles-Ward is applied only to a single fibre return automorphism, not to the switching skew product globally.",
            "Individual natural-boundary factors do not prove a natural boundary for the infinite primitive-orbit product.",
            "The finite-prefix recurrence screen is numerical evidence, not a nonrationality theorem.",
            "No Riemann zeros, primes, or fitted target data are used.",
        ],
    }

    (output_directory / "certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_csv(
        output_directory / "periodic_counts.csv",
        [
            "period",
            "solenoid_fixed_points",
            "archimedean_fixed_points",
            "valuation_correction",
            "active_even_words",
            "lucas_number",
            "exact_period_points",
            "primitive_orbits",
            "zeta_coefficient",
            "valuation_identity_passed",
        ],
        periodic_rows,
    )
    write_csv(
        output_directory / "valuation_distribution.csv",
        [
            "period",
            "v2",
            "word_count",
            "archimedean_mass",
            "solenoid_mass",
            "correction_mass",
        ],
        valuation_rows,
    )
    write_csv(
        output_directory / "congruence_tower.csv",
        [
            "level",
            "period",
            "reachable_residue_states",
            "divisible_words",
            "divisible_archimedean_mass",
            "passed_nonnegative",
            "direct_divisible_words",
            "direct_divisible_archimedean_mass",
            "passed_against_direct_enumeration",
        ],
        congruence,
    )
    (output_directory / "chronology_witnesses.json").write_text(
        json.dumps(witnesses, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (output_directory / "recurrence_screen.json").write_text(
        json.dumps(recurrence_screen, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def mat_add(first: Matrix, second: Matrix) -> Matrix:
    return tuple(x + y for x, y in zip(first, second))  # type: ignore[return-value]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-period", type=int, default=20)
    parser.add_argument("--parity-period", type=int, default=12)
    parser.add_argument("--tower-level", type=int, default=8)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    if arguments.max_period < 1:
        raise SystemExit("--max-period must be positive")
    produce(
        arguments.output,
        arguments.max_period,
        arguments.parity_period,
        arguments.tower_level,
    )
    print(f"wrote HCS-C14 exact artifacts to {arguments.output}")


if __name__ == "__main__":
    main()
