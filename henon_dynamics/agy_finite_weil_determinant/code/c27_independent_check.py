#!/usr/bin/env python3
"""Independent exact replay for HCS-C27.

This checker deliberately does not import :mod:`c27_producer`.  It starts
again from the frozen C24 and C26 certificates and implements its own
integer matrices, finite-field elimination, Thomas discriminants, quadratic
Gauss-basis arithmetic, Newton identities, Rauzy-graph traversal, and
chronological products.

The checked claims are:

* the exact Thomas invariants at p=3,5,7;
* all six local-polynomial coefficient hashes at p=3,5,7;
* the 328/248 C26 power-character census for odd p<=97 and 1<=r<=24;
* the complete p=43, period-925 Weil-fibre character/polynomial collision
  (not a collision of the full AGY Fredholm factors);
* the integral symplectic conjugacy C24-P076 ~ C24-P082;
* the 150 distinct first-return branch Legendre signatures through bridge
  length twelve.

No transition average, B-transpose substitution, or branchwise character
multiplication occurs anywhere in this file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Sequence


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPOSITORY_ROOT = HENON_ROOT.parent
DEFAULT_C24 = HENON_ROOT / "rauzy_metaplectic_obstruction" / "results" / "c24_certificate.json"
DEFAULT_C26 = HENON_ROOT / "agy_holomorphic_slice_obstruction" / "results" / "c26_certificate.json"
DEFAULT_RELEASE = PROJECT / "results" / "c27_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c27_independent_check.json"

EXPECTED_SOURCE_HASHES = {
    "C24": "4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778",
    "C26": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
}
EXPECTED_LOCAL_HASHES = {
    "3": {
        "three_forward": "77c8f89433b015e73877c5caab7b2c0118c54982b164063997f8bce80ac4a25b",
        "three_reverse": "1565b7a342d05194fe64f777216395adc17fb4ecc3605080bdfeea4869a0d889",
    },
    "5": {
        "three_forward": "26a11d78dd2e464a7a104fba2d4613e76a843a50c6099cb04ccbd563542c6efe",
        "three_reverse": "05d24ca6db4eebc25492cdbdc7fda48bd57c2f9ca6c27f8cb7bde488a3ab9c61",
    },
    "7": {
        "three_forward": "087b3cdec27e34e6d7bca631a19fa22e87bb5277a25dda5b0df8caa9223f47d1",
        "three_reverse": "1d86d5bce7c3caa7a3d0320ef6bdfcc6fecb55a9c51e34962951700ed041fd97",
    },
}
EXPECTED_RETURN_COUNTS = {1: 1, 3: 1, 5: 1, 6: 2, 7: 3, 8: 6, 9: 11, 10: 20, 11: 37, 12: 68}

J_C26 = (
    (0, -1, 0, 0),
    (1, 0, -1, 1),
    (0, 1, 0, -1),
    (0, -1, 1, 0),
)
C24_CONJUGATOR = (
    (0, 0, -1, 1),
    (-1, 0, 0, -1),
    (0, -2, 0, -1),
    (0, -1, 0, -1),
)
GAMMA_STAR = "t" * 64 + "tbttbtbb" * 8

Matrix = tuple[tuple[int, ...], ...]
Pair = tuple[Fraction, Fraction]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--c24", type=Path, default=DEFAULT_C24)
    parser.add_argument("--c26", type=Path, default=DEFAULT_C26)
    parser.add_argument("--release", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def portable_path(path: Path) -> str:
    """Serialize repository paths without embedding the clone location."""

    resolved = path.resolve()
    try:
        return resolved.relative_to(REPOSITORY_ROOT).as_posix()
    except ValueError:
        return f"external:{resolved.name}"


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def as_matrix(value: Sequence[Sequence[int]]) -> Matrix:
    return tuple(tuple(int(entry) for entry in row) for row in value)


def identity(size: int = 4) -> Matrix:
    return tuple(tuple(int(row == column) for column in range(size)) for row in range(size))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix))) for column in range(len(matrix[0])))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left[0])))
        for row in range(len(left))
    )


def scalar_identity(value: int, size: int = 4) -> Matrix:
    return tuple(tuple(value if row == column else 0 for column in range(size)) for row in range(size))


def reduce_matrix(matrix: Matrix, p: int) -> Matrix:
    return tuple(tuple(value % p for value in row) for row in matrix)


def matmul_mod(left: Matrix, right: Matrix, p: int) -> Matrix:
    return reduce_matrix(matmul(left, right), p)


def subtract_identity(matrix: Matrix, p: int | None = None) -> Matrix:
    result = tuple(
        tuple(matrix[row][column] - int(row == column) for column in range(len(matrix)))
        for row in range(len(matrix))
    )
    return reduce_matrix(result, p) if p is not None else result


def determinant_integer(matrix: Matrix) -> int:
    """Fraction-free Bareiss determinant, independent of SymPy."""

    size = len(matrix)
    if size == 0:
        return 1
    rows = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next((row for row in range(column, size) if rows[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign = -sign
        pivot_value = rows[column][column]
        for row in range(column + 1, size):
            for target in range(column + 1, size):
                numerator = rows[row][target] * pivot_value - rows[row][column] * rows[column][target]
                if numerator % previous:
                    raise AssertionError("Bareiss division ceased to be exact")
                rows[row][target] = numerator // previous
        previous = pivot_value
        for row in range(column + 1, size):
            rows[row][column] = 0
    return sign * rows[-1][-1]


def determinant_mod(matrix: Matrix, p: int) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    rows = [[value % p for value in row] for row in matrix]
    answer = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            answer = -answer
        pivot_value = rows[column][column] % p
        answer = answer * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(column + 1, size):
            multiplier = rows[row][column] * inverse % p
            rows[row] = [
                (rows[row][target] - multiplier * rows[column][target]) % p
                for target in range(size)
            ]
    return answer % p


def inverse_unimodular(matrix: Matrix) -> Matrix:
    size = len(matrix)
    augmented = [
        [Fraction(value) for value in matrix[row]]
        + [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column or not augmented[row][column]:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [
                augmented[row][target] - multiplier * augmented[column][target]
                for target in range(2 * size)
            ]
    inverse = [row[size:] for row in augmented]
    if any(value.denominator != 1 for row in inverse for value in row):
        raise AssertionError("declared unimodular matrix has a nonintegral inverse")
    return tuple(tuple(int(value) for value in row) for row in inverse)


def characteristic_coefficients(matrix: Matrix) -> list[int]:
    """Faddeev--LeVerrier coefficients in descending order."""

    size = len(matrix)
    auxiliary = identity(size)
    coefficients = [1]
    for index in range(1, size + 1):
        product = matmul(matrix, auxiliary)
        trace = sum(product[row][row] for row in range(size))
        if trace % index:
            raise AssertionError("LeVerrier coefficient is not integral")
        coefficient = -trace // index
        coefficients.append(coefficient)
        auxiliary = matrix_add(product, scalar_identity(coefficient, size))
    return coefficients


def pivot_columns(matrix: Matrix, p: int) -> list[int]:
    rows = [[value % p for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    pivots: list[int] = []
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, p)
        rows[pivot_row] = [(value * inverse) % p for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not rows[row][column]:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                (rows[row][target] - multiplier * rows[pivot_row][target]) % p
                for target in range(column_count)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivots


def legendre(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    residue = pow(value, (p - 1) // 2, p)
    if residue == 1:
        return 1
    if residue == p - 1:
        return -1
    raise AssertionError("Euler criterion failed")


def sigma_invariants(matrix: Matrix, form: Matrix, p: int) -> tuple[int, int, list[int]]:
    difference = subtract_identity(reduce_matrix(matrix, p), p)
    pivots = pivot_columns(difference, p)
    rank = len(pivots)
    quotient: list[tuple[int, ...]] = []
    for source_column in pivots:
        image = tuple(difference[row][source_column] for row in range(4))
        quotient.append(
            tuple(
                sum(image[row] * form[row][target_column] for row in range(4)) % p
                for target_column in pivots
            )
        )
    discriminant = determinant_mod(tuple(quotient), p) if rank else 1
    if discriminant == 0:
        raise AssertionError("Thomas quotient pairing is degenerate")
    return 4 - rank, discriminant, pivots


def character_pair(kernel_dimension: int, discriminant: int, p: int) -> tuple[int, int]:
    eta = legendre(discriminant, p)
    eta_minus = legendre(-1, p)
    return {
        0: (eta, 0),
        1: (0, eta * eta_minus),
        2: (eta * eta_minus * p, 0),
        3: (0, eta * p),
        4: (p * p, 0),
    }[kernel_dimension]


def thomas_record(matrix: Matrix, form: Matrix, p: int) -> dict[str, object]:
    kernel_dimension, discriminant, pivots = sigma_invariants(matrix, form, p)
    pair = character_pair(kernel_dimension, discriminant, p)
    return {
        "kernel_dimension": kernel_dimension,
        "sigma_discriminant_mod_p": discriminant,
        "sigma_quotient_pivot_columns": pivots,
        "legendre_sigma_discriminant": legendre(discriminant, p),
        "exact_pair_one_gauss": list(pair),
        "absolute_value_squared": p**kernel_dimension,
    }


def thomas_key(matrix: Matrix, form: Matrix, p: int) -> tuple[int, int]:
    kernel_dimension, discriminant, _ = sigma_invariants(matrix, form, p)
    return character_pair(kernel_dimension, discriminant, p)


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_multiply(left: Pair, right: Pair, p: int) -> Pair:
    gauss_square = legendre(-1, p) * p
    return (
        left[0] * right[0] + left[1] * right[1] * gauss_square,
        left[0] * right[1] + left[1] * right[0],
    )


def pair_conjugate(value: Pair, p: int) -> Pair:
    return value[0], legendre(-1, p) * value[1]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def serialize_pair(value: Pair) -> list[str]:
    return [fraction_text(value[0]), fraction_text(value[1])]


def local_polynomial(matrix: Matrix, form: Matrix, p: int) -> dict[str, object]:
    degree = p * p
    current = identity()
    reduced = reduce_matrix(matrix, p)
    traces: list[Pair] = []
    for _ in range(degree):
        current = matmul_mod(current, reduced, p)
        one, gauss = thomas_key(current, form, p)
        traces.append((Fraction(one), Fraction(gauss)))

    coefficients: list[Pair] = [(Fraction(1), Fraction(0))]
    for index in range(1, degree + 1):
        total: Pair = (Fraction(0), Fraction(0))
        for power in range(1, index + 1):
            total = pair_add(total, pair_multiply(coefficients[index - power], traces[power - 1], p))
        coefficients.append((-total[0] / index, -total[1] / index))

    reciprocal = all(
        coefficients[index]
        == tuple(-value for value in pair_conjugate(coefficients[degree - index], p))
        for index in range(degree + 1)
    )
    serialized = [serialize_pair(value) for value in coefficients]
    if coefficients[0] != (Fraction(1), Fraction(0)):
        raise AssertionError("local polynomial lost its constant coefficient")
    if coefficients[-1] != (Fraction(-1), Fraction(0)) or not reciprocal:
        raise AssertionError("local polynomial lost finite-Weil reciprocity")
    return {
        "degree": degree,
        "coefficient_sha256": canonical_sha256(serialized),
        "constant_coefficient": serialized[0],
        "leading_coefficient": serialized[-1],
        "conjugate_reciprocity_verified": reciprocal,
        "coefficients_one_gauss": serialized,
    }


def odd_primes(limit: int = 97) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(3, limit + 1, 2)
        if all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))
    )


def load_c26_matrices(c26: dict[str, object]) -> dict[str, Matrix]:
    source = c26["source_locked_branch"]
    periodic = c26["scalar_periodic_trace_gate"]
    two = periodic["chronological_two_return_witness"]
    three = periodic["three_return_spectral_chronology_witness"]
    return {
        "gamma_star": as_matrix(source["chronological_matrix_B"]),
        "second_branch": as_matrix(two["second_branch_chronological_matrix_B"]),
        "two_forward": as_matrix(two["two_return_chronological_matrix_B"]),
        "two_reverse": as_matrix(two["reversed_order_matrix_B"]),
        "third_branch": as_matrix(three["third_branch_chronological_matrix_B"]),
        "three_forward": as_matrix(three["forward_chronological_matrix_B"]),
        "three_reverse": as_matrix(three["reversed_chronological_matrix_B"]),
    }


def verify_c26_inputs(c26: dict[str, object], matrices: dict[str, Matrix]) -> dict[str, object]:
    crossing = as_matrix(c26["source_locked_branch"]["base_crossing_form"])
    inverse_crossing = inverse_unimodular(crossing)
    identities = {
        "source_crossing_inverse_is_checker_J": inverse_crossing == J_C26,
        "two_forward_is_second_times_gamma": matrices["two_forward"]
        == matmul(matrices["second_branch"], matrices["gamma_star"]),
        "two_reverse_is_gamma_times_second": matrices["two_reverse"]
        == matmul(matrices["gamma_star"], matrices["second_branch"]),
        "three_forward_is_third_second_gamma": matrices["three_forward"]
        == matmul(matrices["third_branch"], matmul(matrices["second_branch"], matrices["gamma_star"])),
        "three_reverse_is_gamma_second_third": matrices["three_reverse"]
        == matmul(matrices["gamma_star"], matmul(matrices["second_branch"], matrices["third_branch"])),
    }
    for name, matrix in matrices.items():
        identities[f"{name}_symplectic"] = matmul(transpose(matrix), matmul(J_C26, matrix)) == J_C26
    if not all(identities.values()):
        raise AssertionError(f"C26 source/chronology check failed: {identities}")
    return identities


def small_prime_check(
    matrices: dict[str, Matrix], release: dict[str, object]
) -> tuple[dict[str, object], dict[str, object]]:
    character_rows: dict[str, object] = {}
    polynomial_rows: dict[str, object] = {}
    for p in (3, 5, 7):
        prime = str(p)
        characters = {name: thomas_record(matrix, J_C26, p) for name, matrix in matrices.items()}
        released_characters = release["small_prime_exact_characters"][prime]["characters"]
        for name, record in characters.items():
            for field in (
                "kernel_dimension",
                "sigma_discriminant_mod_p",
                "sigma_quotient_pivot_columns",
                "legendre_sigma_discriminant",
                "exact_pair_one_gauss",
                "absolute_value_squared",
            ):
                if record[field] != released_characters[name][field]:
                    raise AssertionError(f"small-prime Thomas mismatch at p={p}, {name}, {field}")
        character_rows[prime] = {
            "characters": characters,
            "two_forward_equals_reverse": thomas_key(matrices["two_forward"], J_C26, p)
            == thomas_key(matrices["two_reverse"], J_C26, p),
            "three_forward_differs_from_reverse": thomas_key(matrices["three_forward"], J_C26, p)
            != thomas_key(matrices["three_reverse"], J_C26, p),
            "released_records_match": True,
        }

        polynomial_rows[prime] = {}
        for name in ("three_forward", "three_reverse"):
            polynomial = local_polynomial(matrices[name], J_C26, p)
            released = release["exact_local_weil_polynomials"][prime][name]
            expected_hash = EXPECTED_LOCAL_HASHES[prime][name]
            if polynomial["coefficient_sha256"] != expected_hash:
                raise AssertionError(f"hard-coded local hash mismatch at p={p}, {name}")
            if polynomial["coefficient_sha256"] != released["coefficient_sha256"]:
                raise AssertionError(f"released local hash mismatch at p={p}, {name}")
            if polynomial["coefficients_one_gauss"] != released["coefficients_one_gauss"]:
                raise AssertionError(f"released local coefficients mismatch at p={p}, {name}")
            polynomial_rows[prime][name] = {
                "degree": polynomial["degree"],
                "coefficient_sha256": polynomial["coefficient_sha256"],
                "constant_coefficient": polynomial["constant_coefficient"],
                "leading_coefficient": polynomial["leading_coefficient"],
                "conjugate_reciprocity_verified": polynomial["conjugate_reciprocity_verified"],
                "hard_coded_hash_match": True,
                "released_full_coefficients_match": True,
            }
        polynomial_rows[prime]["forward_reverse_hashes_different"] = (
            polynomial_rows[prime]["three_forward"]["coefficient_sha256"]
            != polynomial_rows[prime]["three_reverse"]["coefficient_sha256"]
        )
    return character_rows, polynomial_rows


def power_scan(left: Matrix, right: Matrix, release: dict[str, object]) -> dict[str, object]:
    equalities = 0
    differences = 0
    rows: dict[str, object] = {}
    first_difference: list[int] | None = None
    for p in odd_primes():
        left_power = identity()
        right_power = identity()
        left_mod = reduce_matrix(left, p)
        right_mod = reduce_matrix(right, p)
        equal_powers: list[int] = []
        different_powers: list[int] = []
        for exponent in range(1, 25):
            left_power = matmul_mod(left_power, left_mod, p)
            right_power = matmul_mod(right_power, right_mod, p)
            if thomas_key(left_power, J_C26, p) == thomas_key(right_power, J_C26, p):
                equalities += 1
                equal_powers.append(exponent)
            else:
                differences += 1
                different_powers.append(exponent)
                candidate = [p, exponent]
                if first_difference is None or candidate < first_difference:
                    first_difference = candidate
        released_row = release["c26_power_character_scan"]["per_prime"][str(p)]
        if equal_powers != released_row["equal_powers"] or different_powers != released_row["different_powers"]:
            raise AssertionError(f"power pattern mismatch at p={p}")
        rows[str(p)] = {
            "equal_powers": equal_powers,
            "different_powers": different_powers,
            "released_pattern_match": True,
        }
    result = {
        "prime_count": len(odd_primes()),
        "maximum_power": 24,
        "total_comparisons": 24 * len(odd_primes()),
        "equal_comparisons": equalities,
        "different_comparisons": differences,
        "first_difference_lexicographic_p_then_r": first_difference,
        "per_prime": rows,
    }
    if (equalities, differences, first_difference) != (248, 328, [3, 1]):
        raise AssertionError("328/248 power census changed")
    released_scan = release["c26_power_character_scan"]
    for field in (
        "prime_count",
        "maximum_power",
        "total_comparisons",
        "equal_comparisons",
        "different_comparisons",
        "first_difference_lexicographic_p_then_r",
    ):
        if result[field] != released_scan[field]:
            raise AssertionError(f"released power-scan mismatch in {field}")
    return result


def first_character_difference(left: Matrix, right: Matrix, p: int, search_cap: int) -> int | None:
    """Return the first exact character difference through ``search_cap``."""

    left_power = identity()
    right_power = identity()
    left_mod = reduce_matrix(left, p)
    right_mod = reduce_matrix(right, p)
    for exponent in range(1, search_cap + 1):
        left_power = matmul_mod(left_power, left_mod, p)
        right_power = matmul_mod(right_power, right_mod, p)
        if thomas_key(left_power, J_C26, p) != thomas_key(right_power, J_C26, p):
            return exponent
    return None


def post_window_controls(
    left: Matrix, right: Matrix, release: dict[str, object]
) -> dict[str, object]:
    """Independently replay the p=83 and p=89 late separations."""

    expected = {83: 41, 89: 30}
    records: dict[str, object] = {}
    released_records = release["c26_post_window_separation_controls"]
    for p, search_cap in expected.items():
        record = {
            "short_window_maximum_power": 24,
            "characters_equal_through_short_window": first_character_difference(
                left, right, p, 24
            )
            is None,
            "search_cap": search_cap,
            "first_different_power": first_character_difference(left, right, p, search_cap),
        }
        if record["first_different_power"] != search_cap or not record[
            "characters_equal_through_short_window"
        ]:
            raise AssertionError(f"late chronology control changed at p={p}: {record}")
        if record != released_records[str(p)]:
            raise AssertionError(f"released late chronology control mismatch at p={p}")
        records[str(p)] = record
    return records


def p43_collision(left: Matrix, right: Matrix, release: dict[str, object]) -> dict[str, object]:
    p = 43
    left_power = identity()
    right_power = identity()
    left_mod = reduce_matrix(left, p)
    right_mod = reduce_matrix(right, p)
    left_order = None
    right_order = None
    first_difference = None
    for exponent in range(1, 926):
        left_power = matmul_mod(left_power, left_mod, p)
        right_power = matmul_mod(right_power, right_mod, p)
        if left_order is None and left_power == identity():
            left_order = exponent
        if right_order is None and right_power == identity():
            right_order = exponent
        if first_difference is None and thomas_key(left_power, J_C26, p) != thomas_key(right_power, J_C26, p):
            first_difference = exponent
    left_characteristic = [value % p for value in characteristic_coefficients(left)]
    right_characteristic = [value % p for value in characteristic_coefficients(right)]
    result = {
        "p": p,
        "left_matrix_order": left_order,
        "right_matrix_order": right_order,
        "first_common_identity_power": 925 if left_power == identity() and right_power == identity() else None,
        "first_different_power": first_difference,
        "complete_period_proof": first_difference is None and left_order == right_order == 925,
        "left_base_characteristic_coefficients_mod_p": left_characteristic,
        "right_base_characteristic_coefficients_mod_p": right_characteristic,
        "base_characteristic_polynomials_different_mod_p": left_characteristic != right_characteristic,
    }
    expected = {
        "p": 43,
        "left_matrix_order": 925,
        "right_matrix_order": 925,
        "first_common_identity_power": 925,
        "first_different_power": None,
        "complete_period_proof": True,
        "left_base_characteristic_coefficients_mod_p": [1, 33, 9, 33, 1],
        "right_base_characteristic_coefficients_mod_p": [1, 11, 13, 11, 1],
        "base_characteristic_polynomials_different_mod_p": True,
    }
    if result != expected:
        raise AssertionError(f"p=43 complete collision changed: {result}")
    released = release["p43_complete_weil_fibre_polynomial_collision"]
    for field, value in result.items():
        if released[field] != value:
            raise AssertionError(f"released p=43 mismatch in {field}")
    return result


def c24_conjugacy(c24: dict[str, object], release: dict[str, object]) -> dict[str, object]:
    cycles = {str(row["id"]): row for row in c24["eventually_positive_cycles"]}
    left = as_matrix(cycles["C24-P076"]["base_trivialized_symplectic_matrix"])
    right = as_matrix(cycles["C24-P082"]["base_trivialized_symplectic_matrix"])
    form = as_matrix(c24["source_lock"]["J0"])
    inverse = inverse_unimodular(C24_CONJUGATOR)
    checks = {
        "det_X_is_one": determinant_integer(C24_CONJUGATOR) == 1,
        "X_inverse_is_integral": matmul(C24_CONJUGATOR, inverse) == identity(),
        "X_preserves_J0": matmul(transpose(C24_CONJUGATOR), matmul(form, C24_CONJUGATOR)) == form,
        "P082_X_equals_X_P076": matmul(right, C24_CONJUGATOR) == matmul(C24_CONJUGATOR, left),
        "P076_symplectic": matmul(transpose(left), matmul(form, left)) == form,
        "P082_symplectic": matmul(transpose(right), matmul(form, right)) == form,
    }
    if not all(checks.values()):
        raise AssertionError(f"C24 integral symplectic conjugacy failed: {checks}")
    released = release["c24_controls"]["integral_symplectic_conjugacy_collapse"]
    for field in ("det_X_is_one", "X_preserves_J0", "P082_X_equals_X_P076", "P076_symplectic", "P082_symplectic"):
        if released["checks"][field] != checks[field]:
            raise AssertionError(f"released C24 conjugacy mismatch in {field}")
    if as_matrix(released["conjugator_X"]) != C24_CONJUGATOR:
        raise AssertionError("released C24 conjugator changed")
    left_order = list(cycles["C24-P076"]["central_first_return_branches"])
    right_order = list(cycles["C24-P082"]["central_first_return_branches"])
    same_branch_multiset = sorted(left_order) == sorted(right_order)
    cyclic_rotations = [left_order[offset:] + left_order[:offset] for offset in range(len(left_order))]
    not_cyclic_rotations = right_order not in cyclic_rotations
    if not same_branch_multiset or not not_cyclic_rotations:
        raise AssertionError("independent C24 symbolic noncyclic-order control failed")
    if released["same_branch_multiset"] != same_branch_multiset or released[
        "not_cyclic_rotations"
    ] != not_cyclic_rotations:
        raise AssertionError("released C24 symbolic-order record changed")
    return {
        "left_id": "C24-P076",
        "right_id": "C24-P082",
        "conjugator_X": [list(row) for row in C24_CONJUGATOR],
        "conjugator_X_inverse": [list(row) for row in inverse],
        "checks": checks,
        "left_central_first_return_order": left_order,
        "right_central_first_return_order": right_order,
        "same_branch_multiset": same_branch_multiset,
        "not_cyclic_rotations": not_cyclic_rotations,
        "characteristic_coefficients_equal": characteristic_coefficients(left)
        == characteristic_coefficients(right),
        "all_prime_all_power_class_character_collapse": True,
        "released_record_match": True,
    }


def graph_edges(c26: dict[str, object]) -> dict[tuple[int, str], tuple[int, Matrix]]:
    edges: dict[tuple[int, str], tuple[int, Matrix]] = {}
    for row in c26["graph"]["edges"]:
        edges[(int(row["source"]), str(row["type"]))] = (
            int(row["target"]),
            as_matrix(row["chronological_matrix"]),
        )
    if len(edges) != 14:
        raise AssertionError("frozen C26 graph is not seven-state/two-arrow")
    return edges


def follow_word(
    start: int, word: str, edges: dict[tuple[int, str], tuple[int, Matrix]]
) -> tuple[int, Matrix]:
    state = start
    product = identity()
    for token in word:
        target, edge_matrix = edges[(state, token)]
        product = matmul(edge_matrix, product)
        state = target
    return state, product


def first_return_words(
    base: int, edges: dict[tuple[int, str], tuple[int, Matrix]], maximum_length: int
) -> list[str]:
    frontier = [(base, "")]
    returns: list[str] = []
    for _ in range(maximum_length):
        next_frontier: list[tuple[int, str]] = []
        for state, word in frontier:
            for token in ("t", "b"):
                target, _ = edges[(state, token)]
                extended = word + token
                if target == base:
                    returns.append(extended)
                else:
                    next_frontier.append((target, extended))
        frontier = next_frontier
    return returns


def branch_signature_scan(
    c26: dict[str, object], matrices: dict[str, Matrix], release: dict[str, object]
) -> dict[str, object]:
    edges = graph_edges(c26)
    gamma_end, gamma_matrix = follow_word(4, GAMMA_STAR, edges)
    if gamma_end != 4 or gamma_matrix != matrices["gamma_star"]:
        raise AssertionError("independent gamma_star graph replay failed")
    returns = first_return_words(4, edges, 12)
    primes = odd_primes()
    released_rows = {
        str(row["bridge_word"]): row for row in release["agy_branch_arithmetic_scan"]["rows"]
    }
    signature_keys: set[tuple[int, ...]] = set()
    discriminants: set[int] = set()
    characteristic_keys: set[tuple[int, ...]] = set()
    rows: list[dict[str, object]] = []
    for word in returns:
        bridge_end, bridge_matrix = follow_word(4, word, edges)
        if bridge_end != 4:
            raise AssertionError("enumerated bridge is not a return")
        branch = matmul(gamma_matrix, matmul(bridge_matrix, gamma_matrix))
        discriminant = determinant_integer(subtract_identity(branch))
        signature = tuple(
            0 if discriminant % p == 0 else legendre(discriminant, p) for p in primes
        )
        characteristic = tuple(characteristic_coefficients(branch))
        signature_keys.add(signature)
        discriminants.add(discriminant)
        characteristic_keys.add(characteristic)
        released = released_rows.get(word)
        if released is None:
            raise AssertionError(f"released branch row missing {word}")
        if released["det_I_minus_branch"] != discriminant:
            raise AssertionError(f"released branch discriminant mismatch for {word}")
        if tuple(released["legendre_signature_primes_3_to_97"]) != signature:
            raise AssertionError(f"released branch signature mismatch for {word}")
        if tuple(released["characteristic_coefficients"]) != characteristic:
            raise AssertionError(f"released branch characteristic mismatch for {word}")
        rows.append(
            {
                "bridge_word": word,
                "bridge_length": len(word),
                "det_I_minus_branch": discriminant,
                "legendre_signature_primes_3_to_97": list(signature),
            }
        )
    counts = dict(sorted(Counter(len(word) for word in returns).items()))
    summary = {
        "bridge_max_length": 12,
        "branch_count": len(returns),
        "count_by_bridge_length": {str(key): value for key, value in counts.items()},
        "distinct_discriminants": len(discriminants),
        "distinct_characteristic_polynomials": len(characteristic_keys),
        "distinct_legendre_signatures": len(signature_keys),
        "all_150_signatures_distinct": len(returns) == len(signature_keys) == 150,
        "signature_rows_sha256": canonical_sha256(rows),
        "released_full_rows_match": len(released_rows) == len(rows),
    }
    if counts != EXPECTED_RETURN_COUNTS:
        raise AssertionError(f"first-return length census changed: {counts}")
    for field, expected in {
        "branch_count": 150,
        "distinct_discriminants": 150,
        "distinct_characteristic_polynomials": 150,
        "distinct_legendre_signatures": 150,
        "all_150_signatures_distinct": True,
    }.items():
        if summary[field] != expected:
            raise AssertionError(f"branch signature gate failed in {field}")
        if release["agy_branch_arithmetic_scan"][field] != expected:
            raise AssertionError(f"released branch signature mismatch in {field}")
    if summary["count_by_bridge_length"] != release["agy_branch_arithmetic_scan"]["count_by_bridge_length"]:
        raise AssertionError("released first-return length census mismatch")
    return summary


def run(c24_path: Path, c26_path: Path, release_path: Path) -> dict[str, object]:
    source_hashes = {"C24": sha256(c24_path), "C26": sha256(c26_path)}
    if source_hashes != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"frozen source hashes changed: {source_hashes}")
    c24 = json.loads(c24_path.read_text(encoding="utf-8"))
    c26 = json.loads(c26_path.read_text(encoding="utf-8"))
    release = json.loads(release_path.read_text(encoding="utf-8"))
    matrices = load_c26_matrices(c26)
    chronology = verify_c26_inputs(c26, matrices)
    characters, local_polynomials = small_prime_check(matrices, release)
    scan = power_scan(matrices["three_forward"], matrices["three_reverse"], release)
    late_controls = post_window_controls(
        matrices["three_forward"], matrices["three_reverse"], release
    )
    collision = p43_collision(matrices["three_forward"], matrices["three_reverse"], release)
    conjugacy = c24_conjugacy(c24, release)
    signatures = branch_signature_scan(c26, matrices, release)
    checks = {
        "source_hashes": source_hashes == EXPECTED_SOURCE_HASHES,
        "chronology_and_symplectic_forms": all(chronology.values()),
        "small_prime_Thomas_invariants": all(
            bool(row["released_records_match"]) for row in characters.values()
        ),
        "six_local_polynomial_hashes": all(
            bool(local_polynomials[p][name]["hard_coded_hash_match"])
            and bool(local_polynomials[p][name]["released_full_coefficients_match"])
            for p in ("3", "5", "7")
            for name in ("three_forward", "three_reverse")
        ),
        "power_scan_328_248_and_late_controls": scan["different_comparisons"] == 328
        and scan["equal_comparisons"] == 248
        and all(
            bool(record["characters_equal_through_short_window"])
            and int(record["first_different_power"]) == int(record["search_cap"])
            for record in late_controls.values()
        ),
        "p43_complete_weil_fibre_polynomial_collision": bool(collision["complete_period_proof"]),
        "C24_integral_symplectic_conjugacy": all(conjugacy["checks"].values()),
        "all_150_branch_signatures_distinct": bool(signatures["all_150_signatures_distinct"]),
    }
    if not all(checks.values()):
        raise AssertionError(f"independent C27 release gate failed: {checks}")
    return {
        "schema": "HCS-C27-INDEPENDENT-CHECK-V1",
        "candidate_id": "HCS-C27",
        "status": "PASS",
        "independence": {
            "imports_c27_producer": False,
            "source_certificates": [portable_path(c24_path), portable_path(c26_path)],
            "released_certificate_compared": portable_path(release_path),
            "matrix_engine": "independent standard-library tuple matrices and Bareiss determinant",
            "finite_field_engine": "independent modular Gauss elimination",
            "character_engine": "Thomas invariants in exact basis (1,G_p)",
            "chronology_averaged": False,
        },
        "source_hashes": source_hashes,
        "checks": checks,
        "c26_input_replay": chronology,
        "small_prime_Thomas_invariants": characters,
        "local_polynomial_replay": local_polynomials,
        "c26_power_character_scan": scan,
        "c26_post_window_separation_controls": late_controls,
        "p43_complete_weil_fibre_polynomial_collision": collision,
        "c24_integral_symplectic_conjugacy": conjugacy,
        "agy_branch_signature_scan": signatures,
        "runtime": {
            "python": platform.python_version(),
            "checker_sha256": sha256(Path(__file__)),
        },
    }


def main() -> None:
    args = parse_args()
    report = run(args.c24, args.c26, args.release)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "status": report["status"],
                "checks_passed": sum(bool(value) for value in report["checks"].values()),
                "checks_total": len(report["checks"]),
                "power_differences": report["c26_power_character_scan"]["different_comparisons"],
                "power_equalities": report["c26_power_character_scan"]["equal_comparisons"],
                "p43_weil_fibre_polynomial_collision": report[
                    "p43_complete_weil_fibre_polynomial_collision"
                ]["complete_period_proof"],
                "branch_signatures": report["agy_branch_signature_scan"]["distinct_legendre_signatures"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
