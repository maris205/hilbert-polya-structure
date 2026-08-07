#!/usr/bin/env python3
"""Produce exact and 80-digit certificates for HCS-C18.

The package tests three sharply typed objects: an unoriented open-channel
Dirichlet series, rational-endpoint section cocycles, and the squarefree
Gamma_0(N) scattering algebra.  It reads no prime or Riemann-zero table.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from typing import Any, Iterable, Sequence

import mpmath as mp


CANDIDATE_ID = "HCS-C18"
SCHEMA_VERSION = 1
PRECISION = 80
Q_MAX = 2000
LEVELS = (2, 6, 30, 210)
T0 = mp.mpf(1)
PRINT_DIGITS = 70


@dataclass(frozen=True, slots=True)
class IntMatrix:
    a: int
    b: int
    c: int
    d: int

    def multiply(self, other: "IntMatrix") -> "IntMatrix":
        return IntMatrix(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d,
        )

    def determinant(self) -> int:
        return self.a * self.d - self.b * self.c

    def inverse(self) -> "IntMatrix":
        det = self.determinant()
        if det not in (-1, 1):
            raise ValueError("integral inverse requires determinant +/-1")
        return IntMatrix(self.d // det, -self.b // det, -self.c // det, self.a // det)

    def power(self, exponent: int) -> "IntMatrix":
        if exponent < 0:
            return self.inverse().power(-exponent)
        result = IDENTITY
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result.multiply(base)
            base = base.multiply(base)
            n >>= 1
        return result

    def rows(self) -> list[list[int]]:
        return [[self.a, self.b], [self.c, self.d]]


IDENTITY = IntMatrix(1, 0, 0, 1)
T = IntMatrix(1, 1, 0, 1)
S = IntMatrix(0, -1, 1, 0)


def mp_string(value: mp.mpf, digits: int = PRINT_DIGITS) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False)


def complex_record(value: mp.mpc) -> dict[str, str]:
    return {"real": mp_string(mp.re(value)), "imag": mp_string(mp.im(value))}


def prime_factors(number: int) -> list[int]:
    factors: list[int] = []
    remaining = number
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def euler_phi_direct(q: int) -> int:
    return sum(math.gcd(x, q) == 1 for x in range(1, q + 1))


def roots_minus_one_direct(q: int) -> int:
    return sum((x * x + 1) % q == 0 for x in range(q))


def arithmetic_rows() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for q in range(1, Q_MAX + 1):
        phi = euler_phi_direct(q)
        roots = roots_minus_one_direct(q)
        if (phi + roots) % 2:
            raise AssertionError("Burnside count is not integral")
        rows.append(
            {
                "q": q,
                "euler_phi": phi,
                "sqrt_minus_one_count": roots,
                "unoriented_open_count": (phi + roots) // 2,
            }
        )
    return rows


def chi_minus_four_l(value: mp.mpc) -> mp.mpc:
    return mp.dirichlet(value, [0, 1, 0, -1])


def open_series_closed(s: mp.mpc) -> mp.mpc:
    first = mp.zeta(2 * s - 1) / mp.zeta(2 * s)
    second = mp.zeta(2 * s) * chi_minus_four_l(2 * s) / mp.zeta(4 * s)
    return mp.power(T0, -2 * s) * (first + second) / 2


def build_open_series_rows(counts: Sequence[dict[str, int]]) -> list[dict[str, Any]]:
    points = (
        ("real_5_over_4", mp.mpc(mp.mpf(5) / 4, 0)),
        ("complex_3_over_2", mp.mpc(mp.mpf(3) / 2, mp.mpf(2) / 5)),
        ("real_2", mp.mpc(2, 0)),
    )
    cutoffs = (100, 500, 1000, Q_MAX)
    rows: list[dict[str, Any]] = []
    for label, s in points:
        target = open_series_closed(s)
        partial = mp.mpc(0)
        cutoff_index = 0
        for row in counts:
            q = row["q"]
            partial += row["unoriented_open_count"] * mp.power(q, -2 * s)
            if q != cutoffs[cutoff_index]:
                continue
            sigma = mp.re(s)
            error = abs(target - partial)
            tail_bound = mp.power(q, 2 - 2 * sigma) / (2 * sigma - 2)
            rows.append(
                {
                    "point": label,
                    "s_real": mp_string(mp.re(s)),
                    "s_imag": mp_string(mp.im(s)),
                    "cutoff": q,
                    "partial_real": mp_string(mp.re(partial)),
                    "partial_imag": mp_string(mp.im(partial)),
                    "target_real": mp_string(mp.re(target)),
                    "target_imag": mp_string(mp.im(target)),
                    "absolute_error": mp_string(error),
                    "elementary_tail_bound": mp_string(tail_bound),
                    "within_tail_bound": bool(error <= tail_bound),
                }
            )
            cutoff_index += 1
            if cutoff_index == len(cutoffs):
                break
    return rows


def canonical_endpoint(numerator: int, denominator: int) -> tuple[int, int, int]:
    if denominator == 0:
        raise ValueError("endpoint is infinity")
    common = math.gcd(numerator, denominator)
    numerator //= common
    denominator //= common
    sign = 1
    if denominator < 0:
        numerator, denominator, sign = -numerator, -denominator, -1
    return numerator, denominator, sign


def endpoint_action(matrix: IntMatrix, numerator: int, denominator: int) -> dict[str, Any]:
    if matrix.determinant() != 1 or math.gcd(numerator, denominator) != 1 or denominator <= 0:
        raise ValueError("invalid endpoint action input")
    raw_numerator = matrix.a * numerator + matrix.b * denominator
    raw_denominator = matrix.c * numerator + matrix.d * denominator
    if raw_denominator == 0:
        raise ValueError("image endpoint is infinity")
    image_numerator, image_denominator, primitive_sign = canonical_endpoint(
        raw_numerator, raw_denominator
    )
    if (raw_numerator, raw_denominator) != (
        primitive_sign * image_numerator,
        primitive_sign * image_denominator,
    ):
        raise AssertionError("unimodular action did not preserve primitivity")
    affine = Fraction(abs(raw_denominator), denominator)
    coboundary = Fraction(image_denominator, denominator)
    return {
        "image_numerator": image_numerator,
        "image_denominator": image_denominator,
        "primitive_automorphy": primitive_sign,
        "affine": affine,
        "coboundary": coboundary,
    }


def build_endpoint_rows() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    matrices = (
        ("T", T),
        ("S", S),
        ("H", IntMatrix(2, 1, 1, 1)),
        ("G", IntMatrix(1, 2, 2, 5)),
        ("R", IntMatrix(1, -1, 1, 0)),
    )
    endpoints = ((-3, 5), (-1, 2), (1, 3), (2, 5), (3, 2), (5, 3))
    rows: list[dict[str, Any]] = []
    for label, matrix in matrices:
        for numerator, denominator in endpoints:
            try:
                action = endpoint_action(matrix, numerator, denominator)
            except ValueError as error:
                if "infinity" in str(error):
                    continue
                raise
            affine = action["affine"]
            coboundary = action["coboundary"]
            rows.append(
                {
                    "matrix_label": label,
                    "matrix": json.dumps(matrix.rows(), separators=(",", ":")),
                    "endpoint_numerator": numerator,
                    "endpoint_denominator": denominator,
                    "image_numerator": action["image_numerator"],
                    "image_denominator": action["image_denominator"],
                    "primitive_automorphy": action["primitive_automorphy"],
                    "primitive_absolute": 1,
                    "affine_num": affine.numerator,
                    "affine_den": affine.denominator,
                    "coboundary_num": coboundary.numerator,
                    "coboundary_den": coboundary.denominator,
                    "affine_equals_coboundary": affine == coboundary,
                }
            )

    cocycle_checks = 0
    for _, left in matrices:
        for _, right in matrices:
            product = left.multiply(right)
            for numerator, denominator in endpoints:
                try:
                    right_action = endpoint_action(right, numerator, denominator)
                    left_action = endpoint_action(
                        left,
                        right_action["image_numerator"],
                        right_action["image_denominator"],
                    )
                    product_action = endpoint_action(product, numerator, denominator)
                except ValueError as error:
                    if "infinity" in str(error):
                        continue
                    raise
                if left_action["affine"] * right_action["affine"] != product_action["affine"]:
                    raise AssertionError("affine section cocycle identity failed")
                if (
                    left_action["primitive_automorphy"]
                    * right_action["primitive_automorphy"]
                    != product_action["primitive_automorphy"]
                ):
                    raise AssertionError("primitive section cocycle identity failed")
                cocycle_checks += 1
    summary = {
        "ledger_rows": len(rows),
        "primitive_absolute_one": all(row["primitive_absolute"] == 1 for row in rows),
        "affine_is_endpoint_denominator_coboundary": all(
            row["affine_equals_coboundary"] for row in rows
        ),
        "composition_checks": cocycle_checks,
        "all_composition_checks_pass": True,
    }
    return rows, summary


def double_coset_representative(c: int, d: int) -> IntMatrix:
    if c == 1:
        return S
    if c < 1 or not 0 <= d < c or math.gcd(c, d) != 1:
        raise ValueError("invalid double-coset key")
    a = pow(d, -1, c)
    matrix = IntMatrix(a, (a * d - 1) // c, c, d)
    if matrix.determinant() != 1:
        raise AssertionError("representative is not in SL2(Z)")
    return matrix


def double_coset_key(matrix: IntMatrix) -> tuple[int, int]:
    if matrix.determinant() != 1 or matrix.c == 0:
        raise ValueError("matrix is outside the big cell")
    c, d = matrix.c, matrix.d
    if c < 0:
        c, d = -c, -d
    return c, d % c


def build_double_coset_witnesses() -> list[dict[str, Any]]:
    specifications = (((2, 1), (2, 1), -2), ((2, 1), (3, 1), -2), ((2, 1), (3, 2), -2))
    witnesses: list[dict[str, Any]] = []
    for first_key, second_key, shift in specifications:
        first = double_coset_representative(*first_key)
        variant = first.multiply(T.power(shift))
        second = double_coset_representative(*second_key)
        product = first.multiply(second)
        variant_product = variant.multiply(second)
        if double_coset_key(first) != double_coset_key(variant):
            raise AssertionError("right parabolic shift changed input double coset")
        if double_coset_key(product) == double_coset_key(variant_product):
            raise AssertionError("frozen multiplication witness did not separate")
        witnesses.append(
            {
                "first_key": list(first_key),
                "second_key": list(second_key),
                "right_parabolic_shift": shift,
                "first_representative": first.rows(),
                "equivalent_first_representative": variant.rows(),
                "second_representative": second.rows(),
                "first_input_keys_equal": True,
                "product": product.rows(),
                "variant_product": variant_product.rows(),
                "product_key": list(double_coset_key(product)),
                "variant_product_key": list(double_coset_key(variant_product)),
                "product_keys_differ": True,
            }
        )
    return witnesses


def completed_modular_ratio(s: mp.mpc) -> mp.mpc:
    return (
        mp.sqrt(mp.pi)
        * mp.gamma(s - mp.mpf("0.5"))
        * mp.zeta(2 * s - 1)
        / (mp.gamma(s) * mp.zeta(2 * s))
    )


def local_block(prime: int, s: mp.mpc) -> mp.matrix:
    denominator = mp.power(prime, 2 * s) - 1
    diagonal = mp.mpf(prime - 1) / denominator
    off_diagonal = (mp.power(prime, s) - mp.power(prime, 1 - s)) / denominator
    return mp.matrix([[diagonal, off_diagonal], [off_diagonal, diagonal]])


def local_eigenvalue(prime: int, sign: int, s: mp.mpc) -> mp.mpc:
    if sign == 1:
        return (mp.power(prime, 1 - s) + 1) / (mp.power(prime, s) + 1)
    if sign == -1:
        return (mp.power(prime, 1 - s) - 1) / (mp.power(prime, s) - 1)
    raise ValueError("Walsh sign must be +/-1")


def cusp_divisors(level: int) -> list[int]:
    primes = prime_factors(level)
    if math.prod(primes) != level:
        raise ValueError("level must be squarefree")
    return sorted(
        divisor
        for divisor in range(1, level + 1)
        if level % divisor == 0
    )


def bit_vector(divisor: int, primes: Sequence[int]) -> tuple[int, ...]:
    return tuple(int(divisor % prime == 0) for prime in primes)


def scattering_matrix(level: int, s: mp.mpc) -> mp.matrix:
    primes = prime_factors(level)
    divisors = cusp_divisors(level)
    blocks = {prime: local_block(prime, s) for prime in primes}
    scalar = completed_modular_ratio(s)
    matrix = mp.matrix(len(divisors), len(divisors))
    for row, source in enumerate(divisors):
        source_bits = bit_vector(source, primes)
        for column, target in enumerate(divisors):
            target_bits = bit_vector(target, primes)
            value = scalar
            for index, prime in enumerate(primes):
                value *= blocks[prime][source_bits[index], target_bits[index]]
            matrix[row, column] = value
    return matrix


def walsh_matrix(level: int) -> mp.matrix:
    primes = prime_factors(level)
    divisors = cusp_divisors(level)
    scale = mp.power(2, -mp.mpf(len(primes)) / 2)
    matrix = mp.matrix(len(divisors), len(divisors))
    for row, cusp in enumerate(divisors):
        cusp_bits = bit_vector(cusp, primes)
        for column, channel in enumerate(divisors):
            channel_bits = bit_vector(channel, primes)
            parity = sum(left * right for left, right in zip(cusp_bits, channel_bits))
            matrix[row, column] = scale * (-1 if parity % 2 else 1)
    return matrix


def channel_eigenvalue(level: int, channel: int, s: mp.mpc) -> mp.mpc:
    primes = prime_factors(level)
    channel_bits = bit_vector(channel, primes)
    value = completed_modular_ratio(s)
    for bit, prime in zip(channel_bits, primes):
        value *= local_eigenvalue(prime, -1 if bit else 1, s)
    return value


def identity(size: int) -> mp.matrix:
    return mp.eye(size)


def conjugate_transpose(matrix: mp.matrix) -> mp.matrix:
    return matrix.transpose_conj()


def max_abs(matrix: mp.matrix) -> mp.mpf:
    return max(abs(matrix[row, column]) for row in range(matrix.rows) for column in range(matrix.cols))


def diagonal_matrix(values: Sequence[mp.mpc]) -> mp.matrix:
    matrix = mp.matrix(len(values), len(values))
    for index, value in enumerate(values):
        matrix[index, index] = value
    return matrix


def build_scattering_checks() -> tuple[dict[str, Any], mp.mpf]:
    points = (
        ("physical_0p7", mp.mpc(mp.mpf("0.5"), mp.mpf("0.7")), True),
        ("physical_1p3", mp.mpc(mp.mpf("0.5"), mp.mpf("1.3")), True),
        ("physical_2p1", mp.mpc(mp.mpf("0.5"), mp.mpf("2.1")), True),
        ("off_line_1p2_0p4", mp.mpc(mp.mpf("1.2"), mp.mpf("0.4")), False),
        ("off_line_0p83_1p7", mp.mpc(mp.mpf("0.83"), mp.mpf("1.7")), False),
    )
    physical = points[:3]
    level_records: list[dict[str, Any]] = []
    global_max = mp.mpf(0)
    cached: dict[tuple[int, str], mp.matrix] = {}
    for level in LEVELS:
        divisors = cusp_divisors(level)
        walsh = walsh_matrix(level)
        point_records: list[dict[str, Any]] = []
        for label, s, is_physical in points:
            matrix = scattering_matrix(level, s)
            cached[(level, label)] = matrix
            inverse_residual = max_abs(matrix * scattering_matrix(level, 1 - s) - identity(len(divisors)))
            unitarity_residual = (
                max_abs(matrix * conjugate_transpose(matrix) - identity(len(divisors)))
                if is_physical
                else None
            )
            eigenvalues = [channel_eigenvalue(level, channel, s) for channel in divisors]
            transformed = walsh.T * matrix * walsh
            walsh_residual = max_abs(transformed - diagonal_matrix(eigenvalues))
            determinant_direct = mp.det(matrix)
            determinant_channels = mp.fprod(eigenvalues)
            determinant_residual = abs(determinant_direct - determinant_channels)
            residuals = [inverse_residual, walsh_residual, determinant_residual]
            if unitarity_residual is not None:
                residuals.append(unitarity_residual)
            global_max = max(global_max, *residuals)
            point_records.append(
                {
                    "point": label,
                    "s": complex_record(s),
                    "physical_line": is_physical,
                    "functional_equation_residual": mp_string(inverse_residual),
                    "unitarity_residual": None if unitarity_residual is None else mp_string(unitarity_residual),
                    "walsh_diagonalization_residual": mp_string(walsh_residual),
                    "determinant_direct": complex_record(determinant_direct),
                    "determinant_from_channels": complex_record(determinant_channels),
                    "determinant_residual": mp_string(determinant_residual),
                    "eigenchannels": [
                        {"channel_divisor": channel, "eigenvalue": complex_record(value)}
                        for channel, value in zip(divisors, eigenvalues)
                    ],
                }
            )

        pair_records: list[dict[str, Any]] = []
        for first_index in range(len(physical)):
            for second_index in range(first_index + 1, len(physical)):
                first_label = physical[first_index][0]
                second_label = physical[second_index][0]
                first_matrix = cached[(level, first_label)]
                second_matrix = cached[(level, second_label)]
                residual = max_abs(first_matrix * second_matrix - second_matrix * first_matrix)
                global_max = max(global_max, residual)
                pair_records.append(
                    {
                        "first": first_label,
                        "second": second_label,
                        "commutator_residual": mp_string(residual),
                    }
                )
        canonical_order = tuple(item[0] for item in physical)
        canonical_product = identity(len(divisors))
        for label in canonical_order:
            canonical_product *= cached[(level, label)]
        reorder_records: list[dict[str, Any]] = []
        for order in permutations(canonical_order):
            product_matrix = identity(len(divisors))
            for label in order:
                product_matrix *= cached[(level, label)]
            residual = max_abs(product_matrix - canonical_product)
            global_max = max(global_max, residual)
            reorder_records.append({"order": list(order), "product_residual": mp_string(residual)})
        level_records.append(
            {
                "level": level,
                "primes": prime_factors(level),
                "cusp_divisors": divisors,
                "dimension": len(divisors),
                "point_checks": point_records,
                "commutator_checks": pair_records,
                "ordered_product_rearrangements": reorder_records,
            }
        )

    # Positive scope boundary: rank-one cusp projectors interrupt the
    # commutative scattering algebra.  The finite diagnostic below establishes
    # parameter-to-edge assignment and path sensitivity, not a source-derived
    # dynamical time law for the spectral parameter.
    level = 6
    divisors = cusp_divisors(level)
    positions = {divisor: index for index, divisor in enumerate(divisors)}
    labels = tuple(item[0] for item in physical)
    matrices = {label: cached[(level, label)] for label in labels}

    def projector_amplitude(itinerary: tuple[int, int, int], order: tuple[str, str, str]) -> mp.mpc:
        a, b, c = (positions[value] for value in itinerary)
        return matrices[order[0]][a, b] * matrices[order[1]][b, c] * matrices[order[2]][c, a]

    baseline_itinerary = (1, 2, 6)
    alternate_itinerary = (1, 2, 3)
    baseline_order = labels
    reordered = (labels[1], labels[0], labels[2])
    baseline = projector_amplitude(baseline_itinerary, baseline_order)
    assignment_changed = projector_amplitude(baseline_itinerary, reordered)
    path_changed = projector_amplitude(alternate_itinerary, baseline_order)
    assignment_difference = abs(baseline - assignment_changed)
    path_difference = abs(baseline - path_changed)
    if assignment_difference == 0 or path_difference == 0:
        raise AssertionError("projector-resolved scope witness vanished")
    projector_record = {
        "level": level,
        "cusp_divisors": divisors,
        "formula": "tr(P_a Phi(s1) P_b Phi(s2) P_c Phi(s3))=Phi(s1)[a,b]Phi(s2)[b,c]Phi(s3)[c,a]",
        "baseline": {
            "itinerary": list(baseline_itinerary),
            "edge_parameter_assignment": list(baseline_order),
            "amplitude": complex_record(baseline),
        },
        "assignment_changed": {
            "itinerary": list(baseline_itinerary),
            "edge_parameter_assignment": list(reordered),
            "amplitude": complex_record(assignment_changed),
            "difference_from_baseline": mp_string(assignment_difference),
        },
        "path_changed": {
            "itinerary": list(alternate_itinerary),
            "edge_parameter_assignment": list(baseline_order),
            "amplitude": complex_record(path_changed),
            "difference_from_baseline": mp_string(path_difference),
        },
        "parameter_to_edge_assignment_sensitive": True,
        "path_sensitive": True,
        "intrinsic_chronology_claimed": False,
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "precision_decimal_digits": PRECISION,
        "local_block_formula": "M_p(s)=(p^(2s)-1)^(-1)[[p-1,p^s-p^(1-s)],[p^s-p^(1-s),p-1]]",
        "local_walsh_eigenvalues": {
            "plus": "(p^(1-s)+1)/(p^s+1)",
            "minus": "(p^(1-s)-1)/(p^s-1)",
        },
        "level_checks": level_records,
        "projector_resolved_paths": projector_record,
        "global_max_pure_scattering_residual": mp_string(global_max),
    }, global_max


def build_exact_certificates(endpoint_summary: dict[str, Any]) -> dict[str, Any]:
    residue = mp.mpf(3) / (2 * mp.pi**2 * T0**2)
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "source_lock": {
            "open_count": "n_q=(phi(q)+#{x mod q:x^2=-1})/2",
            "open_series": "T0^(-2s)/2[zeta(2s-1)/zeta(2s)+zeta(2s)L(2s,chi_-4)/zeta(4s)]",
            "endpoint_categories": ["primitive homogeneous section", "affine rational section"],
            "squarefree_levels": list(LEVELS),
            "forbidden_data": ["prime tables", "Riemann-zero tables", "fitted scales"],
        },
        "open_series_residue": {
            "pole": "s=1",
            "T0": "1",
            "formula": "Res_(s=1) Z_sc(s)=T0^(-2)/(4*zeta(2))=3/(2*pi^2*T0^2)",
            "numeric": mp_string(residue),
        },
        "endpoint_section": {
            "primitive_formula": "g*v_x=j_prim(g,x)*v_(gx), j_prim in {+1,-1}",
            "primitive_absolute_formula": "abs(j_prim(g,x))=1",
            "affine_formula": "abs(c*x+d)=den(gx)/den(x)",
            "log_coboundary": "log(abs(c*x+d))=log den(gx)-log den(x)",
            "closed_loop_consequence": "the affine denominator cocycle sums to zero on a closed endpoint loop",
            **endpoint_summary,
        },
        "double_coset_multiplication": {
            "ruling": "P\\SL2(Z)/P has no representative-independent multiplication",
            "witnesses": build_double_coset_witnesses(),
            "all_witnesses_pass": True,
        },
        "squarefree_scattering": {
            "formula": "Phi_N(s)=Lambda(2s-1)/Lambda(2s) times tensor_(p|N) M_p(s)",
            "functional_equation": "Phi_N(s)Phi_N(1-s)=I",
            "physical_line_unitarity": "Phi_N(1/2+it)Phi_N(1/2+it)^*=I",
            "walsh_basis": "W_N[c,e]=2^(-omega(N)/2)(-1)^(<bits(c),bits(e)>)",
            "channel_formula": "lambda_e(s)=Lambda(2s-1)/Lambda(2s)*product_(p|N) mu_(p,e_p)(s)",
            "determinant_formula": "det Phi_N(s)=product_(e|N) lambda_e(s)",
            "frozen_product_ruling": "bare scattering matrices have a fixed Walsh basis, so products at different spectral parameters are permutation-invariant",
            "projector_scope": "rank-one cusp projectors leave this commutative algebra; the finite witness establishes assignment and path sensitivity, not intrinsic chronology",
        },
    }


def write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"cannot write empty CSV {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: Any) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def generate(output: Path) -> dict[str, Any]:
    mp.mp.dps = PRECISION
    output.mkdir(parents=True, exist_ok=True)
    counts = arithmetic_rows()
    series_rows = build_open_series_rows(counts)
    endpoint_rows, endpoint_summary = build_endpoint_rows()
    exact = build_exact_certificates(endpoint_summary)
    scattering, max_residual = build_scattering_checks()
    summary = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "precision_decimal_digits": PRECISION,
        "q_max": Q_MAX,
        "arithmetic_rows": len(counts),
        "open_series_rows": len(series_rows),
        "all_open_series_errors_within_tail_bound": all(row["within_tail_bound"] for row in series_rows),
        "endpoint_rows": len(endpoint_rows),
        "endpoint_composition_checks": endpoint_summary["composition_checks"],
        "double_coset_multiplication_witnesses": len(exact["double_coset_multiplication"]["witnesses"]),
        "squarefree_levels": list(LEVELS),
        "global_max_pure_scattering_residual": mp_string(max_residual),
        "projector_assignment_difference": scattering["projector_resolved_paths"]["assignment_changed"]["difference_from_baseline"],
        "projector_path_difference": scattering["projector_resolved_paths"]["path_changed"]["difference_from_baseline"],
        "no_prime_or_zero_tables_used": True,
        "formal_signal": {
            "unoriented_open_series": "PROVED_CLASSICAL_CLOSED_FORM",
            "primitive_endpoint_clock": "TRIVIAL_ABSOLUTE_AUTOMORPHY",
            "affine_endpoint_clock": "ALGEBRAIC_ENDPOINT_COBOUNDARY_ONLY",
            "double_coset_product": "NOT_WELL_DEFINED",
            "bare_scattering_product": "FROZEN_SPECTRAL_PARAMETER_PRODUCT_IS_PERMUTATION_INVARIANT",
            "projector_resolved_paths": "SURVIVES_ASSIGNMENT_AND_PATH_SENSITIVITY_TEST_ONLY",
            "hilbert_polya_operator": "NOT_CONSTRUCTED",
        },
    }
    write_csv(output / "arithmetic_counts.csv", counts)
    write_csv(output / "open_series.csv", series_rows)
    write_csv(output / "endpoint_ledger.csv", endpoint_rows)
    write_json(output / "exact_certificates.json", exact)
    write_json(output / "scattering_checks.json", scattering)
    write_json(output / "summary.json", summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent.parent / "results")
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    print(json.dumps(generate(arguments.output), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
