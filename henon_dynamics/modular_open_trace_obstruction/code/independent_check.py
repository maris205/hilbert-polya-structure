#!/usr/bin/env python3
"""Independent, strict verifier for the frozen HCS-C18 artifacts.

No producer module is imported.  Totients and square roots of -1 use prime
factorization rather than the producer's residue enumeration; L(s,chi_-4)
uses Hurwitz zeta rather than the producer's Dirichlet routine.  Endpoint and
scattering calculations are independently implemented below.
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


CANDIDATE = "HCS-C18"
SCHEMA = 1
Q_LIMIT = 2000
LEVELS = (2, 6, 30, 210)
CHECK_DPS = 110
RTOL = mp.mpf("1e-60")
ATOL = mp.mpf("1e-68")
RESIDUAL_LIMIT = mp.mpf("1e-65")


class CheckFailure(ValueError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def exact_keys(value: dict[str, Any], keys: Iterable[str], context: str) -> None:
    expected = set(keys)
    ensure(set(value) == expected, f"{context}: schema mismatch: {sorted(set(value) ^ expected)}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        ensure(key not in result, f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    ensure(path.is_file(), f"missing {path.name}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, json.JSONDecodeError) as error:
        raise CheckFailure(f"cannot parse {path.name}: {error}") from error
    ensure(isinstance(value, dict), f"{path.name}: top level is not an object")
    return value


def load_csv(path: Path, fields: Sequence[str]) -> list[dict[str, str]]:
    ensure(path.is_file(), f"missing {path.name}")
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            ensure(reader.fieldnames == list(fields), f"{path.name}: header mismatch")
            rows = list(reader)
    except OSError as error:
        raise CheckFailure(f"cannot read {path.name}: {error}") from error
    ensure(bool(rows), f"{path.name}: empty")
    for line, row in enumerate(rows, 2):
        ensure(None not in row and all(item is not None for item in row.values()), f"{path.name}:{line}: malformed row")
    return rows


def parse_int(text: str, context: str) -> int:
    try:
        value = int(text)
    except ValueError as error:
        raise CheckFailure(f"{context}: invalid integer") from error
    ensure(str(value) == text, f"{context}: noncanonical integer")
    return value


def parse_bool(text: str, context: str) -> bool:
    ensure(text in ("True", "False"), f"{context}: invalid Boolean")
    return text == "True"


def parse_real(text: str, context: str) -> mp.mpf:
    try:
        value = mp.mpf(text)
    except (TypeError, ValueError) as error:
        raise CheckFailure(f"{context}: invalid real") from error
    ensure(mp.isfinite(value), f"{context}: nonfinite real")
    return value


def parse_complex(value: Any, context: str) -> mp.mpc:
    ensure(isinstance(value, dict), f"{context}: complex record is not an object")
    exact_keys(value, ("real", "imag"), context)
    return mp.mpc(parse_real(value["real"], context), parse_real(value["imag"], context))


def close(actual: mp.mpf | mp.mpc, expected: mp.mpf | mp.mpc, context: str) -> None:
    difference = abs(actual - expected)
    ensure(difference <= ATOL + RTOL * max(mp.mpf(1), abs(expected)), f"{context}: numerical mismatch {mp.nstr(difference, 8)}")


@dataclass(frozen=True, slots=True)
class ZMat:
    aa: int
    ab: int
    ba: int
    bb: int

    def times(self, other: "ZMat") -> "ZMat":
        return ZMat(
            self.aa * other.aa + self.ab * other.ba,
            self.aa * other.ab + self.ab * other.bb,
            self.ba * other.aa + self.bb * other.ba,
            self.ba * other.ab + self.bb * other.bb,
        )

    def det(self) -> int:
        return self.aa * self.bb - self.ab * self.ba

    def inv(self) -> "ZMat":
        determinant = self.det()
        ensure(determinant in (-1, 1), "nonunimodular inverse")
        return ZMat(self.bb // determinant, -self.ab // determinant, -self.ba // determinant, self.aa // determinant)

    def pow(self, exponent: int) -> "ZMat":
        if exponent < 0:
            return self.inv().pow(-exponent)
        answer = ZIDENTITY
        base = self
        n = exponent
        while n:
            if n & 1:
                answer = answer.times(base)
            base = base.times(base)
            n //= 2
        return answer

    def rows(self) -> list[list[int]]:
        return [[self.aa, self.ab], [self.ba, self.bb]]


ZIDENTITY = ZMat(1, 0, 0, 1)
ZTRANSLATION = ZMat(1, 1, 0, 1)
ZINVERSION = ZMat(0, -1, 1, 0)


def factorization(number: int) -> dict[int, int]:
    result: dict[int, int] = {}
    remaining = number
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            result[prime] = result.get(prime, 0) + 1
            remaining //= prime
        prime += 1
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def independent_phi(q: int) -> int:
    answer = q
    for prime in factorization(q):
        answer -= answer // prime
    return answer


def independent_sqrt_minus_one_count(q: int) -> int:
    factors = factorization(q)
    if factors.get(2, 0) >= 2:
        return 0
    count = 1
    for prime in factors:
        if prime == 2:
            continue
        if prime % 4 == 3:
            return 0
        count *= 2
    return count


def beta_via_hurwitz(s: mp.mpc) -> mp.mpc:
    return mp.power(4, -s) * (mp.zeta(s, mp.mpf(1) / 4) - mp.zeta(s, mp.mpf(3) / 4))


def closed_open_series(s: mp.mpc) -> mp.mpc:
    return (
        mp.zeta(2 * s - 1) / mp.zeta(2 * s)
        + mp.zeta(2 * s) * beta_via_hurwitz(2 * s) / mp.zeta(4 * s)
    ) / 2


def verify_arithmetic(results: Path, summary: dict[str, Any]) -> tuple[int, int]:
    fields = ("q", "euler_phi", "sqrt_minus_one_count", "unoriented_open_count")
    rows = load_csv(results / "arithmetic_counts.csv", fields)
    ensure(len(rows) == Q_LIMIT, "arithmetic row count mismatch")
    counts: list[int] = []
    for q, row in enumerate(rows, 1):
        context = f"arithmetic_counts.csv:{q + 1}"
        ensure(parse_int(row["q"], context) == q, f"{context}: q mismatch")
        phi = independent_phi(q)
        roots = independent_sqrt_minus_one_count(q)
        ensure(parse_int(row["euler_phi"], context) == phi, f"{context}: phi mismatch")
        ensure(parse_int(row["sqrt_minus_one_count"], context) == roots, f"{context}: root count mismatch")
        ensure((phi + roots) % 2 == 0, f"{context}: nonintegral Burnside count")
        count = (phi + roots) // 2
        ensure(parse_int(row["unoriented_open_count"], context) == count, f"{context}: open count mismatch")
        counts.append(count)

    fields_series = (
        "point", "s_real", "s_imag", "cutoff", "partial_real", "partial_imag",
        "target_real", "target_imag", "absolute_error", "elementary_tail_bound",
        "within_tail_bound",
    )
    series = load_csv(results / "open_series.csv", fields_series)
    points = (
        ("real_5_over_4", mp.mpc(mp.mpf(5) / 4, 0)),
        ("complex_3_over_2", mp.mpc(mp.mpf(3) / 2, mp.mpf(2) / 5)),
        ("real_2", mp.mpc(2, 0)),
    )
    cutoffs = (100, 500, 1000, Q_LIMIT)
    ensure(len(series) == 12, "open-series row count mismatch")
    position = 0
    for label, s in points:
        target = closed_open_series(s)
        partial = mp.mpc(0)
        cutoff_index = 0
        for q, count in enumerate(counts, 1):
            partial += count * mp.power(q, -2 * s)
            if q != cutoffs[cutoff_index]:
                continue
            row = series[position]
            position += 1
            context = f"open_series.csv:{position + 1}"
            error = abs(target - partial)
            sigma = mp.re(s)
            bound = mp.power(q, 2 - 2 * sigma) / (2 * sigma - 2)
            ensure(row["point"] == label, f"{context}: label mismatch")
            close(parse_real(row["s_real"], context), mp.re(s), f"{context}: s real")
            close(parse_real(row["s_imag"], context), mp.im(s), f"{context}: s imag")
            ensure(parse_int(row["cutoff"], context) == q, f"{context}: cutoff mismatch")
            close(parse_real(row["partial_real"], context), mp.re(partial), f"{context}: partial real")
            close(parse_real(row["partial_imag"], context), mp.im(partial), f"{context}: partial imag")
            close(parse_real(row["target_real"], context), mp.re(target), f"{context}: target real")
            close(parse_real(row["target_imag"], context), mp.im(target), f"{context}: target imag")
            close(parse_real(row["absolute_error"], context), error, f"{context}: error")
            close(parse_real(row["elementary_tail_bound"], context), bound, f"{context}: bound")
            ensure(parse_bool(row["within_tail_bound"], context) == (error <= bound), f"{context}: tail flag")
            cutoff_index += 1
            if cutoff_index == len(cutoffs):
                break
    ensure(summary["arithmetic_rows"] == len(rows), "summary arithmetic count mismatch")
    ensure(summary["open_series_rows"] == len(series), "summary series count mismatch")
    ensure(summary["all_open_series_errors_within_tail_bound"] is True, "summary tail flag failed")
    return len(rows), len(series)


def parse_matrix(text: str, context: str) -> ZMat:
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        raise CheckFailure(f"{context}: bad matrix JSON") from error
    return matrix_value(value, context)


def matrix_value(value: Any, context: str) -> ZMat:
    ensure(isinstance(value, list) and len(value) == 2 and all(isinstance(row, list) and len(row) == 2 for row in value), f"{context}: bad 2x2 matrix")
    entries = [entry for row in value for entry in row]
    ensure(all(type(entry) is int for entry in entries), f"{context}: noninteger matrix")
    return ZMat(*entries)


def endpoint_image(matrix: ZMat, numerator: int, denominator: int) -> tuple[int, int, int, Fraction]:
    raw_numerator = matrix.aa * numerator + matrix.ab * denominator
    raw_denominator = matrix.ba * numerator + matrix.bb * denominator
    ensure(raw_denominator != 0, "endpoint image infinity")
    sign = 1 if raw_denominator > 0 else -1
    image_numerator = sign * raw_numerator
    image_denominator = sign * raw_denominator
    ensure(math.gcd(image_numerator, image_denominator) == 1, "endpoint image nonprimitive")
    return image_numerator, image_denominator, sign, Fraction(image_denominator, denominator)


def verify_endpoint(results: Path, exact: dict[str, Any], summary: dict[str, Any]) -> int:
    fields = (
        "matrix_label", "matrix", "endpoint_numerator", "endpoint_denominator",
        "image_numerator", "image_denominator", "primitive_automorphy",
        "primitive_absolute", "affine_num", "affine_den", "coboundary_num",
        "coboundary_den", "affine_equals_coboundary",
    )
    rows = load_csv(results / "endpoint_ledger.csv", fields)
    matrices = (
        ("T", ZTRANSLATION), ("S", ZINVERSION), ("H", ZMat(2, 1, 1, 1)),
        ("G", ZMat(1, 2, 2, 5)), ("R", ZMat(1, -1, 1, 0)),
    )
    endpoints = ((-3, 5), (-1, 2), (1, 3), (2, 5), (3, 2), (5, 3))
    expected: list[tuple[str, ZMat, int, int]] = []
    for label, matrix in matrices:
        for numerator, denominator in endpoints:
            if matrix.ba * numerator + matrix.bb * denominator:
                expected.append((label, matrix, numerator, denominator))
    ensure(len(rows) == len(expected) == 30, "endpoint ledger row count mismatch")
    for line, (row, item) in enumerate(zip(rows, expected, strict=True), 2):
        label, matrix, numerator, denominator = item
        context = f"endpoint_ledger.csv:{line}"
        image_numerator, image_denominator, sign, ratio = endpoint_image(matrix, numerator, denominator)
        ensure(row["matrix_label"] == label and parse_matrix(row["matrix"], context) == matrix, f"{context}: matrix mismatch")
        ensure(parse_int(row["endpoint_numerator"], context) == numerator, f"{context}: endpoint numerator")
        ensure(parse_int(row["endpoint_denominator"], context) == denominator, f"{context}: endpoint denominator")
        ensure(parse_int(row["image_numerator"], context) == image_numerator, f"{context}: image numerator")
        ensure(parse_int(row["image_denominator"], context) == image_denominator, f"{context}: image denominator")
        ensure(parse_int(row["primitive_automorphy"], context) == sign, f"{context}: primitive automorphy")
        ensure(parse_int(row["primitive_absolute"], context) == 1, f"{context}: primitive absolute")
        ensure(parse_int(row["affine_num"], context) == ratio.numerator and parse_int(row["affine_den"], context) == ratio.denominator, f"{context}: affine ratio")
        ensure(parse_int(row["coboundary_num"], context) == ratio.numerator and parse_int(row["coboundary_den"], context) == ratio.denominator, f"{context}: coboundary ratio")
        ensure(parse_bool(row["affine_equals_coboundary"], context), f"{context}: equality flag")

    composition_count = 0
    for _, left in matrices:
        for _, right in matrices:
            for numerator, denominator in endpoints:
                try:
                    rn, rd, rs, rr = endpoint_image(right, numerator, denominator)
                    _, _, ls, lr = endpoint_image(left, rn, rd)
                    _, _, ps, pr = endpoint_image(left.times(right), numerator, denominator)
                except CheckFailure as error:
                    if "infinity" in str(error):
                        continue
                    raise
                ensure(lr * rr == pr and ls * rs == ps, "endpoint composition identity failed")
                composition_count += 1
    endpoint = exact["endpoint_section"]
    exact_keys(endpoint, (
        "primitive_formula", "primitive_absolute_formula", "affine_formula", "log_coboundary",
        "closed_loop_consequence", "ledger_rows", "primitive_absolute_one",
        "affine_is_endpoint_denominator_coboundary", "composition_checks",
        "all_composition_checks_pass",
    ), "endpoint_section")
    ensure(endpoint["ledger_rows"] == len(rows), "exact endpoint row count")
    ensure(endpoint["primitive_formula"] == "g*v_x=j_prim(g,x)*v_(gx), j_prim in {+1,-1}", "primitive formula metadata")
    ensure(endpoint["primitive_absolute_formula"] == "abs(j_prim(g,x))=1", "primitive absolute metadata")
    ensure(endpoint["affine_formula"] == "abs(c*x+d)=den(gx)/den(x)", "affine formula metadata")
    ensure(endpoint["log_coboundary"] == "log(abs(c*x+d))=log den(gx)-log den(x)", "coboundary metadata")
    ensure(endpoint["closed_loop_consequence"] == "the affine denominator cocycle sums to zero on a closed endpoint loop", "closed-loop metadata")
    ensure(endpoint["primitive_absolute_one"] is True and endpoint["affine_is_endpoint_denominator_coboundary"] is True, "exact endpoint flags")
    ensure(endpoint["composition_checks"] == composition_count == 147, "endpoint composition count")
    ensure(endpoint["all_composition_checks_pass"] is True, "endpoint composition flag")
    ensure(summary["endpoint_rows"] == len(rows) and summary["endpoint_composition_checks"] == composition_count, "summary endpoint counts")
    return len(rows)


def dc_rep(c: int, d: int) -> ZMat:
    if c == 1:
        return ZINVERSION
    a = pow(d, -1, c)
    return ZMat(a, (a * d - 1) // c, c, d)


def dc_key(matrix: ZMat) -> tuple[int, int]:
    ensure(matrix.det() == 1 and matrix.ba != 0, "invalid double-coset matrix")
    c, d = matrix.ba, matrix.bb
    if c < 0:
        c, d = -c, -d
    return c, d % c


def verify_exact(exact: dict[str, Any], summary: dict[str, Any]) -> int:
    exact_keys(exact, ("schema_version", "candidate_id", "source_lock", "open_series_residue", "endpoint_section", "double_coset_multiplication", "squarefree_scattering"), "exact_certificates.json")
    ensure(exact["schema_version"] == SCHEMA and exact["candidate_id"] == CANDIDATE, "exact identity mismatch")
    ensure(exact["source_lock"] == {
        "open_count": "n_q=(phi(q)+#{x mod q:x^2=-1})/2",
        "open_series": "T0^(-2s)/2[zeta(2s-1)/zeta(2s)+zeta(2s)L(2s,chi_-4)/zeta(4s)]",
        "endpoint_categories": ["primitive homogeneous section", "affine rational section"],
        "squarefree_levels": list(LEVELS),
        "forbidden_data": ["prime tables", "Riemann-zero tables", "fitted scales"],
    }, "source lock mismatch")
    residue = exact["open_series_residue"]
    exact_keys(residue, ("pole", "T0", "formula", "numeric"), "residue")
    ensure(residue["pole"] == "s=1" and residue["T0"] == "1", "residue convention mismatch")
    ensure(residue["formula"] == "Res_(s=1) Z_sc(s)=T0^(-2)/(4*zeta(2))=3/(2*pi^2*T0^2)", "residue formula mismatch")
    close(parse_real(residue["numeric"], "residue numeric"), mp.mpf(3) / (2 * mp.pi**2), "residue numeric")

    block = exact["double_coset_multiplication"]
    exact_keys(block, ("ruling", "witnesses", "all_witnesses_pass"), "double coset block")
    ensure(block["ruling"] == "P\\SL2(Z)/P has no representative-independent multiplication", "double-coset ruling mismatch")
    specifications = (((2, 1), (2, 1), -2), ((2, 1), (3, 1), -2), ((2, 1), (3, 2), -2))
    ensure(isinstance(block["witnesses"], list) and len(block["witnesses"]) == 3, "witness count")
    for index, (row, spec) in enumerate(zip(block["witnesses"], specifications, strict=True), 1):
        exact_keys(row, ("first_key", "second_key", "right_parabolic_shift", "first_representative", "equivalent_first_representative", "second_representative", "first_input_keys_equal", "product", "variant_product", "product_key", "variant_product_key", "product_keys_differ"), f"witness {index}")
        first_key, second_key, shift = spec
        first = dc_rep(*first_key)
        variant = first.times(ZTRANSLATION.pow(shift))
        second = dc_rep(*second_key)
        product = first.times(second)
        variant_product = variant.times(second)
        ensure(row == {
            "first_key": list(first_key), "second_key": list(second_key),
            "right_parabolic_shift": shift, "first_representative": first.rows(),
            "equivalent_first_representative": variant.rows(), "second_representative": second.rows(),
            "first_input_keys_equal": True, "product": product.rows(),
            "variant_product": variant_product.rows(), "product_key": list(dc_key(product)),
            "variant_product_key": list(dc_key(variant_product)), "product_keys_differ": True,
        }, f"double-coset witness {index} mismatch")
        ensure(dc_key(first) == dc_key(variant) and dc_key(product) != dc_key(variant_product), f"witness {index} independently failed")
    ensure(block["all_witnesses_pass"] is True, "witness aggregate flag")
    scattering = exact["squarefree_scattering"]
    exact_keys(scattering, ("formula", "functional_equation", "physical_line_unitarity", "walsh_basis", "channel_formula", "determinant_formula", "frozen_product_ruling", "projector_scope"), "squarefree scattering metadata")
    ensure(scattering == {
        "formula": "Phi_N(s)=Lambda(2s-1)/Lambda(2s) times tensor_(p|N) M_p(s)",
        "functional_equation": "Phi_N(s)Phi_N(1-s)=I",
        "physical_line_unitarity": "Phi_N(1/2+it)Phi_N(1/2+it)^*=I",
        "walsh_basis": "W_N[c,e]=2^(-omega(N)/2)(-1)^(<bits(c),bits(e)>)",
        "channel_formula": "lambda_e(s)=Lambda(2s-1)/Lambda(2s)*product_(p|N) mu_(p,e_p)(s)",
        "determinant_formula": "det Phi_N(s)=product_(e|N) lambda_e(s)",
        "frozen_product_ruling": "bare scattering matrices have a fixed Walsh basis, so products at different spectral parameters are permutation-invariant",
        "projector_scope": "rank-one cusp projectors leave this commutative algebra; the finite witness establishes assignment and path sensitivity, not intrinsic chronology",
    }, "squarefree scattering metadata mismatch")
    ensure(summary["double_coset_multiplication_witnesses"] == 3, "summary witness count")
    return 3


def primes_of(level: int) -> list[int]:
    return list(factorization(level))


def divisors_of(level: int) -> list[int]:
    return [d for d in range(1, level + 1) if level % d == 0]


def bits(divisor: int, primes: Sequence[int]) -> tuple[int, ...]:
    return tuple(int(divisor % prime == 0) for prime in primes)


def base_scattering(s: mp.mpc) -> mp.mpc:
    completed_numerator = mp.power(mp.pi, -(2 * s - 1) / 2) * mp.gamma((2 * s - 1) / 2) * mp.zeta(2 * s - 1)
    completed_denominator = mp.power(mp.pi, -s) * mp.gamma(s) * mp.zeta(2 * s)
    return completed_numerator / completed_denominator


def p_block(p: int, s: mp.mpc) -> mp.matrix:
    denominator = mp.power(p, 2 * s) - 1
    return mp.matrix([
        [(p - 1) / denominator, (mp.power(p, s) - mp.power(p, 1 - s)) / denominator],
        [(mp.power(p, s) - mp.power(p, 1 - s)) / denominator, (p - 1) / denominator],
    ])


def p_channel(p: int, minus: bool, s: mp.mpc) -> mp.mpc:
    sign = -1 if minus else 1
    return (mp.power(p, 1 - s) + sign) / (mp.power(p, s) + sign)


def full_matrix(level: int, s: mp.mpc) -> mp.matrix:
    primes = primes_of(level)
    divisors = divisors_of(level)
    local = {p: p_block(p, s) for p in primes}
    answer = mp.matrix(len(divisors), len(divisors))
    scalar = base_scattering(s)
    for row, first in enumerate(divisors):
        first_bits = bits(first, primes)
        for column, second in enumerate(divisors):
            second_bits = bits(second, primes)
            value = scalar
            for index, p in enumerate(primes):
                value *= local[p][first_bits[index], second_bits[index]]
            answer[row, column] = value
    return answer


def channel_value(level: int, channel: int, s: mp.mpc) -> mp.mpc:
    primes = primes_of(level)
    value = base_scattering(s)
    for bit, p in zip(bits(channel, primes), primes):
        value *= p_channel(p, bool(bit), s)
    return value


def walsh(level: int) -> mp.matrix:
    primes = primes_of(level)
    divisors = divisors_of(level)
    answer = mp.matrix(len(divisors), len(divisors))
    scale = mp.power(2, -mp.mpf(len(primes)) / 2)
    for row, cusp in enumerate(divisors):
        left = bits(cusp, primes)
        for column, channel in enumerate(divisors):
            right = bits(channel, primes)
            answer[row, column] = scale * (-1 if sum(a * b for a, b in zip(left, right)) % 2 else 1)
    return answer


def maxnorm(matrix: mp.matrix) -> mp.mpf:
    return max(abs(matrix[row, column]) for row in range(matrix.rows) for column in range(matrix.cols))


def diag(values: Sequence[mp.mpc]) -> mp.matrix:
    answer = mp.matrix(len(values), len(values))
    for index, value in enumerate(values):
        answer[index, index] = value
    return answer


def verify_scattering(data: dict[str, Any], summary: dict[str, Any]) -> int:
    exact_keys(data, ("schema_version", "candidate_id", "precision_decimal_digits", "local_block_formula", "local_walsh_eigenvalues", "level_checks", "projector_resolved_paths", "global_max_pure_scattering_residual"), "scattering_checks.json")
    ensure(data["schema_version"] == SCHEMA and data["candidate_id"] == CANDIDATE and data["precision_decimal_digits"] == 80, "scattering identity mismatch")
    ensure(data["local_block_formula"] == "M_p(s)=(p^(2s)-1)^(-1)[[p-1,p^s-p^(1-s)],[p^s-p^(1-s),p-1]]", "local block metadata")
    ensure(data["local_walsh_eigenvalues"] == {"plus": "(p^(1-s)+1)/(p^s+1)", "minus": "(p^(1-s)-1)/(p^s-1)"}, "local eigenvalue metadata")
    points = (
        ("physical_0p7", mp.mpc(mp.mpf("0.5"), mp.mpf("0.7")), True),
        ("physical_1p3", mp.mpc(mp.mpf("0.5"), mp.mpf("1.3")), True),
        ("physical_2p1", mp.mpc(mp.mpf("0.5"), mp.mpf("2.1")), True),
        ("off_line_1p2_0p4", mp.mpc(mp.mpf("1.2"), mp.mpf("0.4")), False),
        ("off_line_0p83_1p7", mp.mpc(mp.mpf("0.83"), mp.mpf("1.7")), False),
    )
    physical_labels = tuple(row[0] for row in points[:3])
    ensure(isinstance(data["level_checks"], list) and len(data["level_checks"]) == 4, "level check count")
    reported_residuals: list[mp.mpf] = []
    cache: dict[tuple[int, str], mp.matrix] = {}
    for level_row, level in zip(data["level_checks"], LEVELS, strict=True):
        exact_keys(level_row, ("level", "primes", "cusp_divisors", "dimension", "point_checks", "commutator_checks", "ordered_product_rearrangements"), f"level {level}")
        divisors = divisors_of(level)
        ensure(level_row["level"] == level and level_row["primes"] == primes_of(level), f"level {level}: identity")
        ensure(level_row["cusp_divisors"] == divisors and level_row["dimension"] == len(divisors), f"level {level}: cusps")
        ensure(len(level_row["point_checks"]) == 5, f"level {level}: point count")
        w = walsh(level)
        for record, (label, s, physical) in zip(level_row["point_checks"], points, strict=True):
            exact_keys(record, ("point", "s", "physical_line", "functional_equation_residual", "unitarity_residual", "walsh_diagonalization_residual", "determinant_direct", "determinant_from_channels", "determinant_residual", "eigenchannels"), f"level {level} point {label}")
            ensure(record["point"] == label and record["physical_line"] is physical, f"level {level} {label}: metadata")
            close(parse_complex(record["s"], "stored s"), s, f"level {level} {label}: s")
            matrix = full_matrix(level, s)
            cache[(level, label)] = matrix
            channels = [channel_value(level, channel, s) for channel in divisors]
            ensure(len(record["eigenchannels"]) == len(divisors), f"level {level} {label}: channel count")
            for channel_record, channel, expected in zip(record["eigenchannels"], divisors, channels, strict=True):
                exact_keys(channel_record, ("channel_divisor", "eigenvalue"), "eigenchannel")
                ensure(channel_record["channel_divisor"] == channel, "channel divisor mismatch")
                close(parse_complex(channel_record["eigenvalue"], "eigenchannel"), expected, f"level {level} {label} channel {channel}")
            direct_det = mp.det(matrix)
            channel_det = mp.fprod(channels)
            close(parse_complex(record["determinant_direct"], "direct determinant"), direct_det, f"level {level} {label}: determinant")
            close(parse_complex(record["determinant_from_channels"], "channel determinant"), channel_det, f"level {level} {label}: channel determinant")
            ensure(maxnorm(w.T * matrix * w - diag(channels)) <= mp.mpf("1e-90"), f"level {level} {label}: independent Walsh failure")
            for key in ("functional_equation_residual", "walsh_diagonalization_residual", "determinant_residual"):
                residual = parse_real(record[key], f"level {level} {label} {key}")
                ensure(0 <= residual <= RESIDUAL_LIMIT, f"level {level} {label}: residual too large")
                reported_residuals.append(residual)
            if physical:
                ensure(record["unitarity_residual"] is not None, f"level {level} {label}: missing unitarity")
                residual = parse_real(record["unitarity_residual"], "unitarity residual")
                ensure(0 <= residual <= RESIDUAL_LIMIT, f"level {level} {label}: unitarity too large")
                reported_residuals.append(residual)
            else:
                ensure(record["unitarity_residual"] is None, f"level {level} {label}: unexpected unitarity")
        expected_pairs = [(physical_labels[i], physical_labels[j]) for i in range(3) for j in range(i + 1, 3)]
        ensure(len(level_row["commutator_checks"]) == 3, f"level {level}: commutator count")
        for record, pair in zip(level_row["commutator_checks"], expected_pairs, strict=True):
            exact_keys(record, ("first", "second", "commutator_residual"), "commutator")
            ensure((record["first"], record["second"]) == pair, "commutator labels")
            independent = maxnorm(cache[(level, pair[0])] * cache[(level, pair[1])] - cache[(level, pair[1])] * cache[(level, pair[0])])
            ensure(independent <= mp.mpf("1e-90"), f"level {level}: independent commutator")
            residual = parse_real(record["commutator_residual"], "commutator residual")
            ensure(0 <= residual <= RESIDUAL_LIMIT, f"level {level}: reported commutator")
            reported_residuals.append(residual)
        orders = list(permutations(physical_labels))
        ensure(len(level_row["ordered_product_rearrangements"]) == 6, f"level {level}: reorder count")
        canonical = mp.eye(len(divisors))
        for label in physical_labels:
            canonical *= cache[(level, label)]
        for record, order in zip(level_row["ordered_product_rearrangements"], orders, strict=True):
            exact_keys(record, ("order", "product_residual"), "order record")
            ensure(record["order"] == list(order), "order labels")
            candidate = mp.eye(len(divisors))
            for label in order:
                candidate *= cache[(level, label)]
            ensure(maxnorm(candidate - canonical) <= mp.mpf("1e-90"), f"level {level}: independent reorder")
            residual = parse_real(record["product_residual"], "product residual")
            ensure(0 <= residual <= RESIDUAL_LIMIT, f"level {level}: reported reorder")
            reported_residuals.append(residual)

    projector = data["projector_resolved_paths"]
    exact_keys(projector, ("level", "cusp_divisors", "formula", "baseline", "assignment_changed", "path_changed", "parameter_to_edge_assignment_sensitive", "path_sensitive", "intrinsic_chronology_claimed"), "projector paths")
    ensure(projector["level"] == 6 and projector["cusp_divisors"] == [1, 2, 3, 6], "projector level convention")
    ensure(projector["formula"] == "tr(P_a Phi(s1) P_b Phi(s2) P_c Phi(s3))=Phi(s1)[a,b]Phi(s2)[b,c]Phi(s3)[c,a]", "projector formula metadata")
    ensure(projector["parameter_to_edge_assignment_sensitive"] is True and projector["path_sensitive"] is True, "projector sensitivity flags")
    ensure(projector["intrinsic_chronology_claimed"] is False, "projector chronology scope")
    positions = {value: index for index, value in enumerate(projector["cusp_divisors"])}
    matrices = {label: cache[(6, label)] for label in physical_labels}
    def amplitude(itinerary: Sequence[int], order: Sequence[str]) -> mp.mpc:
        ensure(len(itinerary) == len(order) == 3, "projector path length")
        a, b, c = (positions[item] for item in itinerary)
        return matrices[order[0]][a, b] * matrices[order[1]][b, c] * matrices[order[2]][c, a]
    base = projector["baseline"]
    exact_keys(base, ("itinerary", "edge_parameter_assignment", "amplitude"), "projector baseline")
    base_value = amplitude(base["itinerary"], base["edge_parameter_assignment"])
    close(parse_complex(base["amplitude"], "baseline amplitude"), base_value, "baseline amplitude")
    for key in ("assignment_changed", "path_changed"):
        record = projector[key]
        exact_keys(record, ("itinerary", "edge_parameter_assignment", "amplitude", "difference_from_baseline"), key)
        value = amplitude(record["itinerary"], record["edge_parameter_assignment"])
        difference = abs(value - base_value)
        close(parse_complex(record["amplitude"], f"{key} amplitude"), value, f"{key} amplitude")
        close(parse_real(record["difference_from_baseline"], f"{key} difference"), difference, f"{key} difference")
        ensure(difference > mp.mpf("1e-6"), f"{key}: no material assignment/path sensitivity")
    stored_max = parse_real(data["global_max_pure_scattering_residual"], "global residual")
    ensure(stored_max == max(reported_residuals), "global residual summary mismatch")
    ensure(summary["global_max_pure_scattering_residual"] == data["global_max_pure_scattering_residual"], "summary global residual")
    ensure(summary["projector_assignment_difference"] == projector["assignment_changed"]["difference_from_baseline"], "summary assignment difference")
    ensure(summary["projector_path_difference"] == projector["path_changed"]["difference_from_baseline"], "summary path difference")
    return len(data["level_checks"])


def verify_summary(summary: dict[str, Any]) -> None:
    exact_keys(summary, (
        "schema_version", "candidate_id", "precision_decimal_digits", "q_max",
        "arithmetic_rows", "open_series_rows", "all_open_series_errors_within_tail_bound",
        "endpoint_rows", "endpoint_composition_checks", "double_coset_multiplication_witnesses",
        "squarefree_levels", "global_max_pure_scattering_residual",
        "projector_assignment_difference", "projector_path_difference",
        "no_prime_or_zero_tables_used", "formal_signal",
    ), "summary.json")
    ensure(summary["schema_version"] == SCHEMA and summary["candidate_id"] == CANDIDATE, "summary identity")
    ensure(summary["precision_decimal_digits"] == 80 and summary["q_max"] == Q_LIMIT, "summary frozen parameters")
    ensure(summary["squarefree_levels"] == list(LEVELS), "summary levels")
    ensure(summary["no_prime_or_zero_tables_used"] is True, "summary data firewall")
    ensure(summary["formal_signal"] == {
        "unoriented_open_series": "PROVED_CLASSICAL_CLOSED_FORM",
        "primitive_endpoint_clock": "TRIVIAL_ABSOLUTE_AUTOMORPHY",
        "affine_endpoint_clock": "ALGEBRAIC_ENDPOINT_COBOUNDARY_ONLY",
        "double_coset_product": "NOT_WELL_DEFINED",
        "bare_scattering_product": "FROZEN_SPECTRAL_PARAMETER_PRODUCT_IS_PERMUTATION_INVARIANT",
        "projector_resolved_paths": "SURVIVES_ASSIGNMENT_AND_PATH_SENSITIVITY_TEST_ONLY",
        "hilbert_polya_operator": "NOT_CONSTRUCTED",
    }, "summary formal signal")


def verify_results(results: Path) -> dict[str, Any]:
    mp.mp.dps = CHECK_DPS
    results = results.resolve()
    summary = load_json(results / "summary.json")
    exact = load_json(results / "exact_certificates.json")
    scattering = load_json(results / "scattering_checks.json")
    verify_summary(summary)
    witnesses = verify_exact(exact, summary)
    arithmetic, series = verify_arithmetic(results, summary)
    endpoint = verify_endpoint(results, exact, summary)
    levels = verify_scattering(scattering, summary)
    return {
        "schema_version": SCHEMA,
        "candidate_id": CANDIDATE,
        "status": "PASS",
        "checker_precision_decimal_digits": CHECK_DPS,
        "independent_of_producer_import": True,
        "verified_files": [
            "arithmetic_counts.csv", "open_series.csv", "endpoint_ledger.csv",
            "exact_certificates.json", "scattering_checks.json", "summary.json",
        ],
        "verified_counts": {
            "arithmetic_rows": arithmetic,
            "open_series_rows": series,
            "endpoint_rows": endpoint,
            "double_coset_witnesses": witnesses,
            "squarefree_levels": levels,
        },
        "projector_paths_outside_bare_product_no_go": True,
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=project / "results")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    try:
        report = verify_results(arguments.results)
    except CheckFailure as error:
        raise SystemExit(f"FAIL: {error}") from error
    if arguments.output is not None:
        write_report(arguments.output, report)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
