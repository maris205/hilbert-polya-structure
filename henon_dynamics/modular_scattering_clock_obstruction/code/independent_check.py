#!/usr/bin/env python3
"""Independent verifier for the frozen HCS-C17 result artifacts.

This module deliberately does not import ``modular_clock``.  Matrix arithmetic,
Euler's totient, Gauss words, the power formula, and the scattering coefficient
are implemented again here.  The checker recomputes every mathematical row in
the five result files produced by the frozen default run.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

import mpmath as mp


CANDIDATE_ID = "HCS-C17"
SCHEMA_VERSION = 1
CHECK_PRECISION = 110
DOUBLE_COSET_CUTOFF = 80
RIGIDITY_CUTOFF = 20
WORD_MAX_LENGTH = 6
WORD_MAX_DIGIT = 3
MAX_POWER = 24
DIRICHLET_CUTOFF = 50_000
NUMERIC_RTOL = mp.mpf("1e-65")
NUMERIC_ATOL = mp.mpf("1e-69")
ROUNDING_RESIDUAL_LIMIT = mp.mpf("1e-65")


class VerificationError(ValueError):
    """Raised when a result artifact does not match independent computation."""


@dataclass(frozen=True, slots=True)
class Matrix2:
    x00: int
    x01: int
    x10: int
    x11: int

    def multiply(self, right: "Matrix2") -> "Matrix2":
        return Matrix2(
            self.x00 * right.x00 + self.x01 * right.x10,
            self.x00 * right.x01 + self.x01 * right.x11,
            self.x10 * right.x00 + self.x11 * right.x10,
            self.x10 * right.x01 + self.x11 * right.x11,
        )

    def determinant(self) -> int:
        return self.x00 * self.x11 - self.x01 * self.x10

    def trace(self) -> int:
        return self.x00 + self.x11

    def inverse(self) -> "Matrix2":
        determinant = self.determinant()
        require(determinant in (-1, 1), "matrix inverse is not integral")
        return Matrix2(
            self.x11 // determinant,
            -self.x01 // determinant,
            -self.x10 // determinant,
            self.x00 // determinant,
        )

    def power(self, exponent: int) -> "Matrix2":
        if exponent < 0:
            return self.inverse().power(-exponent)
        result = IDENTITY
        base = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result.multiply(base)
            base = base.multiply(base)
            remaining >>= 1
        return result

    def rows(self) -> list[list[int]]:
        return [[self.x00, self.x01], [self.x10, self.x11]]


IDENTITY = Matrix2(1, 0, 0, 1)
PARABOLIC = Matrix2(1, 1, 0, 1)
INVERSION = Matrix2(0, -1, 1, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def require_keys(value: dict[str, Any], expected: Iterable[str], context: str) -> None:
    expected_set = set(expected)
    actual_set = set(value)
    require(
        actual_set == expected_set,
        f"{context}: key mismatch; expected {sorted(expected_set)}, got {sorted(actual_set)}",
    )


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise VerificationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    require(path.is_file(), f"missing result file: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_pairs)
    except (OSError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot read {path}: {error}") from error
    require(isinstance(value, dict), f"{path.name}: top level must be an object")
    return value


def read_csv(path: Path, fields: Sequence[str]) -> list[dict[str, str]]:
    require(path.is_file(), f"missing result file: {path}")
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            require(reader.fieldnames == list(fields), f"{path.name}: CSV header mismatch")
            rows = list(reader)
    except OSError as error:
        raise VerificationError(f"cannot read {path}: {error}") from error
    require(bool(rows), f"{path.name}: CSV must not be empty")
    for number, row in enumerate(rows, start=2):
        require(None not in row, f"{path.name}:{number}: excess CSV field")
        require(all(value is not None for value in row.values()), f"{path.name}:{number}: missing field")
    return rows


def integer(text: str, context: str) -> int:
    require(text.strip() == text and text not in ("", "+0", "-0"), f"{context}: noncanonical integer")
    try:
        value = int(text)
    except ValueError as error:
        raise VerificationError(f"{context}: invalid integer {text!r}") from error
    require(str(value) == text, f"{context}: noncanonical integer {text!r}")
    return value


def boolean(text: str, context: str) -> bool:
    require(text in ("True", "False"), f"{context}: invalid Boolean {text!r}")
    return text == "True"


def number(text: str, context: str) -> mp.mpf:
    try:
        value = mp.mpf(text)
    except (ValueError, TypeError) as error:
        raise VerificationError(f"{context}: invalid real number {text!r}") from error
    require(mp.isfinite(value), f"{context}: nonfinite number")
    return value


def close(actual: mp.mpf | mp.mpc, expected: mp.mpf | mp.mpc, context: str) -> None:
    error = abs(actual - expected)
    scale = max(mp.mpf(1), abs(expected))
    require(error <= NUMERIC_ATOL + NUMERIC_RTOL * scale, f"{context}: numerical mismatch ({mp.nstr(error, 8)})")


def matrix_from_json(value: Any, context: str) -> Matrix2:
    require(
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(row, list) and len(row) == 2 for row in value),
        f"{context}: expected a 2 by 2 matrix",
    )
    entries = [entry for row in value for entry in row]
    require(all(type(entry) is int for entry in entries), f"{context}: matrix entries must be integers")
    return Matrix2(*entries)


def matrix_from_csv(text: str, context: str) -> Matrix2:
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        raise VerificationError(f"{context}: invalid matrix JSON") from error
    return matrix_from_json(value, context)


def totient(n: int) -> int:
    require(n >= 1, "totient argument must be positive")
    count = 0
    for residue in range(1, n + 1):
        count += math.gcd(residue, n) == 1
    return count


def totient_table(limit: int) -> list[int]:
    require(limit >= 1, "totient-table limit must be positive")
    values = [0] * (limit + 1)
    values[1] = 1
    for n in range(2, limit + 1):
        candidate = n
        divisor = 2
        remaining = n
        while divisor * divisor <= remaining:
            if remaining % divisor == 0:
                candidate -= candidate // divisor
                while remaining % divisor == 0:
                    remaining //= divisor
            divisor += 1
        if remaining > 1:
            candidate -= candidate // remaining
        values[n] = candidate
    return values


def double_coset_representatives(level: int) -> list[Matrix2]:
    require(level >= 1, "double-coset level must be positive")
    if level == 1:
        return [INVERSION]
    representatives: list[Matrix2] = []
    for lower_right in range(1, level):
        if math.gcd(level, lower_right) != 1:
            continue
        upper_left = pow(lower_right, -1, level)
        upper_right = (upper_left * lower_right - 1) // level
        matrix = Matrix2(upper_left, upper_right, level, lower_right)
        require(matrix.determinant() == 1, "reconstructed representative is not in SL2(Z)")
        representatives.append(matrix)
    return representatives


def double_coset_key(matrix: Matrix2) -> tuple[int, int]:
    require(matrix.determinant() == 1 and matrix.x10 != 0, "invalid big-cell matrix")
    c, d = matrix.x10, matrix.x11
    if c < 0:
        c, d = -c, -d
    return c, d % c


def gauss_matrix(digit: int) -> Matrix2:
    require(digit >= 1, "Gauss digit must be positive")
    return Matrix2(0, 1, 1, digit)


def gauss_product(word: Sequence[int]) -> Matrix2:
    result = IDENTITY
    for digit in word:
        result = result.multiply(gauss_matrix(digit))
    return result


def rotations(word: Sequence[int], step: int) -> Iterator[tuple[int, ...]]:
    frozen = tuple(word)
    for offset in range(0, len(frozen), step):
        yield frozen[offset:] + frozen[:offset]


def primitive(word: Sequence[int]) -> bool:
    frozen = tuple(word)
    for block_length in range(1, len(frozen)):
        if len(frozen) % block_length == 0 and frozen == frozen[:block_length] * (len(frozen) // block_length):
            return False
    return True


def trace_factor(trace: int, exponent: int) -> int:
    require(exponent >= 1, "trace-factor exponent must be positive")
    previous, current = 1, trace
    if exponent == 1:
        return previous
    for _ in range(2, exponent):
        previous, current = current, trace * current - previous
    return current


def hyperbolic_length(matrix: Matrix2) -> mp.mpf:
    trace = abs(matrix.trace())
    require(matrix.determinant() == 1 and trace > 2, "length requires hyperbolic SL2 matrix")
    eigenvalue = (mp.mpf(trace) + mp.sqrt(trace * trace - 4)) / 2
    return 2 * mp.log(eigenvalue)


def scattering(s: mp.mpc) -> mp.mpc:
    return (
        mp.sqrt(mp.pi)
        * mp.gamma(s - mp.mpf("0.5"))
        * mp.zeta(2 * s - 1)
        / (mp.gamma(s) * mp.zeta(2 * s))
    )


def verify_double_cosets(results: Path, exact: dict[str, Any], summary: dict[str, Any]) -> int:
    fields = ("c", "enumerated", "euler_phi")
    rows = read_csv(results / "double_coset_counts.csv", fields)
    require(len(rows) == DOUBLE_COSET_CUTOFF, "double-coset row count mismatch")
    action_pairs = ((-2, 3), (1, -1), (4, 2))
    for level, row in enumerate(rows, start=1):
        context = f"double_coset_counts.csv:{level + 1}"
        require(integer(row["c"], context) == level, f"{context}: level mismatch")
        representatives = double_coset_representatives(level)
        expected_phi = totient(level)
        require(integer(row["enumerated"], context) == len(representatives), f"{context}: count mismatch")
        require(integer(row["euler_phi"], context) == expected_phi, f"{context}: phi mismatch")
        require(len(representatives) == expected_phi, f"{context}: independent phi theorem failed")
        keys = [double_coset_key(matrix) for matrix in representatives]
        require(len(keys) == len(set(keys)), f"{context}: duplicate double-coset key")
        for matrix in representatives:
            key = double_coset_key(matrix)
            for left, right in action_pairs:
                moved = PARABOLIC.power(left).multiply(matrix).multiply(PARABOLIC.power(right))
                require(double_coset_key(moved) == key, f"{context}: parabolic action changed key")

    expected_audit = {
        "cutoff": DOUBLE_COSET_CUTOFF,
        "all_counts_match": True,
        "all_keys_unique": True,
        "parabolic_left_right_actions_preserve_key": True,
    }
    require(exact["double_coset_finite_audit"] == expected_audit, "exact JSON double-coset summary mismatch")
    require(summary["double_coset"] == expected_audit, "summary JSON double-coset summary mismatch")
    return len(rows)


def verify_exact_certificates(exact: dict[str, Any], summary: dict[str, Any]) -> tuple[int, int]:
    require_keys(
        exact,
        (
            "schema_version", "candidate_id", "source_lock", "double_coset_theorem",
            "conjugacy_witness", "psl_gauss_cyclic_witness", "denominator_rigidity",
            "chebyshev_power_identity", "stable_closure", "divisor_no_go",
            "double_coset_finite_audit",
        ),
        "exact_certificates.json",
    )
    require(exact["schema_version"] == SCHEMA_VERSION, "exact schema version mismatch")
    require(exact["candidate_id"] == CANDIDATE_ID, "exact candidate ID mismatch")

    source_lock = exact["source_lock"]
    require(isinstance(source_lock, dict), "source_lock must be an object")
    require(source_lock == {
        "group": "PSL2(Z) with explicit SL2(Z) lifts",
        "cusp_subgroup": "P=<T>, T=[[1,1],[0,1]]",
        "oriented_double_coset_convention": "choose lower-left entry c>0",
        "closed_clock_scope": "final-monodromy denominator-only F(alpha*abs(c))",
        "allowed_data": ["exact integer matrices", "primary literature"],
        "forbidden_data": ["prime tables", "Riemann-zero tables", "fitted scales"],
    }, "source-lock metadata mismatch")
    require(exact["double_coset_theorem"] == {
        "level_parameter": "(c, d mod c), c>=1, gcd(c,d)=1",
        "oriented_level_multiplicity": "EulerPhi(c)",
        "dirichlet_identity": "sum phi(c)c^(-2s)=zeta(2s-1)/zeta(2s), Re(s)>1",
        "full_scattering_factor": "sqrt(pi)Gamma(s-1/2)/Gamma(s) times the Dirichlet identity",
    }, "double-coset theorem metadata mismatch")

    witness = exact["conjugacy_witness"]
    require_keys(witness, ("matrix", "conjugator", "conjugate", "trace_pair", "absolute_c_pair", "pass"), "conjugacy witness")
    matrix = matrix_from_json(witness["matrix"], "conjugacy matrix")
    conjugator = matrix_from_json(witness["conjugator"], "conjugator")
    conjugate = conjugator.inverse().multiply(matrix).multiply(conjugator)
    require(matrix == Matrix2(2, 1, 3, 2), "unexpected frozen conjugacy matrix")
    require(conjugator == INVERSION, "unexpected frozen conjugator")
    require(matrix_from_json(witness["conjugate"], "conjugate") == conjugate, "conjugate mismatch")
    require(witness["trace_pair"] == [matrix.trace(), conjugate.trace()], "conjugacy trace pair mismatch")
    require(witness["absolute_c_pair"] == [abs(matrix.x10), abs(conjugate.x10)], "conjugacy c pair mismatch")
    require(witness["pass"] is True and matrix.trace() == conjugate.trace() and abs(matrix.x10) != abs(conjugate.x10), "conjugacy witness failed")

    gauss = exact["psl_gauss_cyclic_witness"]
    require_keys(gauss, ("word", "two_digit_shift", "matrix", "shifted_matrix", "sl2_conjugator", "trace_pair", "absolute_c_pair", "pass"), "Gauss witness")
    word = (1, 1, 1, 2)
    shifted = (1, 2, 1, 1)
    base = gauss_product(word)
    shifted_matrix = gauss_product(shifted)
    prefix = gauss_product((1, 1))
    require(gauss["word"] == list(word) and gauss["two_digit_shift"] == list(shifted), "Gauss words mismatch")
    require(matrix_from_json(gauss["matrix"], "Gauss matrix") == base, "Gauss matrix mismatch")
    require(matrix_from_json(gauss["shifted_matrix"], "shifted Gauss matrix") == shifted_matrix, "shifted Gauss matrix mismatch")
    require(matrix_from_json(gauss["sl2_conjugator"], "Gauss conjugator") == prefix, "Gauss conjugator mismatch")
    require(prefix.inverse().multiply(base).multiply(prefix) == shifted_matrix, "Gauss conjugacy independently failed")
    require(gauss["trace_pair"] == [base.trace(), shifted_matrix.trace()], "Gauss trace pair mismatch")
    require(gauss["absolute_c_pair"] == [abs(base.x10), abs(shifted_matrix.x10)], "Gauss c pair mismatch")
    require(gauss["pass"] is True and base.trace() == shifted_matrix.trace() and abs(base.x10) != abs(shifted_matrix.x10), "Gauss witness failed")

    rigidity = exact["denominator_rigidity"]
    require_keys(rigidity, ("theorem", "positive_family", "family_rows", "proof_relations", "all_family_identities_pass"), "denominator rigidity")
    require(rigidity["positive_family"] == "gamma_mn=[[1,m],[n,1+mn]]", "rigidity family metadata mismatch")
    family_rows = rigidity["family_rows"]
    require(isinstance(family_rows, list) and len(family_rows) == RIGIDITY_CUTOFF ** 2, "rigidity row count mismatch")
    position = 0
    for m in range(1, RIGIDITY_CUTOFF + 1):
        for n in range(1, RIGIDITY_CUTOFF + 1):
            row = family_rows[position]
            position += 1
            context = f"rigidity row {position}"
            require_keys(row, ("m", "n", "matrix", "c", "trace", "c_square", "expected_c_square", "identity_pass"), context)
            expected_matrix = Matrix2(1, m, n, 1 + m * n)
            squared_c = expected_matrix.power(2).x10
            require(row == {
                "m": m, "n": n, "matrix": expected_matrix.rows(), "c": n,
                "trace": expected_matrix.trace(), "c_square": squared_c,
                "expected_c_square": n * (2 + m * n), "identity_pass": True,
            }, f"{context}: exact family row mismatch")
    require(rigidity["all_family_identities_pass"] is True, "rigidity aggregate flag failed")
    require(isinstance(rigidity["theorem"], str) and rigidity["theorem"].startswith("For alpha>0"), "rigidity theorem text mismatch")
    require(rigidity["proof_relations"] == {
        "n_equals_1": "F(alpha*(m+2))=2F(alpha), all m>=1",
        "n_equals_r_m_equals_1": "F(alpha*r*(r+2))=2F(alpha*r), r>=3",
        "deduction": "F(alpha)=0, then F(alpha*r)=0 for r=1 and r>=3",
        "remaining_r_equals_2": "F(8alpha)=2F(2alpha), hence F(2alpha)=0",
    }, "rigidity proof-relation metadata mismatch")

    chebyshev = exact["chebyshev_power_identity"]
    require_keys(chebyshev, ("formula", "rows", "all_pass"), "Chebyshev certificate")
    require(chebyshev["formula"] == "c(g^n)=c(g)U_(n-1)(tr(g)/2)", "Chebyshev formula metadata mismatch")
    expected_matrices = [Matrix2(2, 1, 3, 2), gauss_product((1, 1)), base, Matrix2(1, 3, 5, 16)]
    rows = chebyshev["rows"]
    require(isinstance(rows, list) and len(rows) == 48, "Chebyshev row count mismatch")
    position = 0
    for sample in expected_matrices:
        for exponent in range(1, 13):
            row = rows[position]
            position += 1
            factor = trace_factor(sample.trace(), exponent)
            actual_c = sample.power(exponent).x10
            require(row == {
                "matrix": sample.rows(), "trace": sample.trace(), "exponent": exponent,
                "actual_c": actual_c, "trace_factor": factor,
                "predicted_c": sample.x10 * factor, "identity_pass": True,
            }, f"Chebyshev row {position}: mismatch")
    require(chebyshev["all_pass"] is True, "Chebyshev aggregate flag failed")
    require(exact["stable_closure"] == {
        "formula": "2log|c(g^n)|=n*ell(g)+2log(|c(g)|/sqrt(t^2-4))+2log(1-lambda^(-2n))",
        "limit": "lim_n 2log|c(g^n)|/n=ell(g)=2log(lambda)",
    }, "stable-closure metadata mismatch")
    require(exact["divisor_no_go"] == {
        "Lambda": "pi^(-u/2)Gamma(u/2)zeta(u)",
        "Phi": "Lambda(2s-1)/Lambda(2s)",
        "nontrivial_poles": "s=rho/2",
        "nontrivial_zeros": "s=(1+rho)/2",
        "allowed_normalization": "nonconstant affine reparametrization and entire zero-free prefactor",
        "excluded_compensator": "any factor carrying a zeta-zero divisor",
    }, "divisor no-go metadata mismatch")
    require(summary["rigidity_family_rows"] == len(family_rows), "summary rigidity row count mismatch")
    require(summary["chebyshev_rows"] == len(rows), "summary Chebyshev row count mismatch")
    return len(family_rows), len(rows)


def expected_gauss_words() -> Iterator[tuple[int, ...]]:
    for length in range(2, WORD_MAX_LENGTH + 1, 2):
        for word in product(range(1, WORD_MAX_DIGIT + 1), repeat=length):
            if primitive(word) and word == min(rotations(word, 2)):
                yield word


def verify_gauss_csv(results: Path, summary: dict[str, Any]) -> int:
    fields = (
        "word", "length", "matrix", "trace", "cyclic_trace_invariant",
        "cyclic_c_values", "cyclic_c_invariant", "c_square", "c_squared",
        "literal_denominator_power_additive",
    )
    rows = read_csv(results / "gauss_word_clock_audit.csv", fields)
    words = list(expected_gauss_words())
    require(len(rows) == len(words) == 274, "Gauss audit row count mismatch")
    cyclic_variation = 0
    additive = 0
    for index, (row, word) in enumerate(zip(rows, words, strict=True), start=2):
        context = f"gauss_word_clock_audit.csv:{index}"
        require(row["word"] == " ".join(map(str, word)), f"{context}: word mismatch")
        require(integer(row["length"], context) == len(word), f"{context}: length mismatch")
        matrix = gauss_product(word)
        require(matrix_from_csv(row["matrix"], context) == matrix, f"{context}: matrix mismatch")
        require(integer(row["trace"], context) == matrix.trace(), f"{context}: trace mismatch")
        cyclic = [gauss_product(rotation) for rotation in rotations(word, 2)]
        traces = [item.trace() for item in cyclic]
        c_values = [abs(item.x10) for item in cyclic]
        trace_invariant = len(set(traces)) == 1
        c_invariant = len(set(c_values)) == 1
        require(boolean(row["cyclic_trace_invariant"], context) == trace_invariant, f"{context}: cyclic trace flag mismatch")
        require(row["cyclic_c_values"] == " ".join(map(str, c_values)), f"{context}: cyclic c values mismatch")
        require(boolean(row["cyclic_c_invariant"], context) == c_invariant, f"{context}: cyclic c flag mismatch")
        square_c = abs(matrix.power(2).x10)
        c_squared = abs(matrix.x10) ** 2
        power_additive = square_c == c_squared
        require(integer(row["c_square"], context) == square_c, f"{context}: square c mismatch")
        require(integer(row["c_squared"], context) == c_squared, f"{context}: c squared mismatch")
        require(boolean(row["literal_denominator_power_additive"], context) == power_additive, f"{context}: additivity flag mismatch")
        cyclic_variation += not c_invariant
        additive += power_additive
    require(summary["gauss_word_rows"] == len(rows), "summary Gauss row count mismatch")
    require(summary["gauss_words_with_cyclic_denominator_variation"] == cyclic_variation, "summary cyclic-variation count mismatch")
    require(summary["gauss_words_passing_literal_denominator_square_additivity"] == additive, "summary additivity count mismatch")
    return len(rows)


def verify_homogenization(results: Path, summary: dict[str, Any]) -> int:
    fields = (
        "sample", "matrix", "trace", "base_c", "power", "power_c",
        "two_log_power_c", "formula_prediction", "formula_residual",
        "normalized_height", "translation_length", "limit_error",
    )
    rows = read_csv(results / "homogenization.csv", fields)
    samples = (
        ("conjugacy_witness", Matrix2(2, 1, 3, 2)),
        ("gauss_112", gauss_product((1, 1))),
        ("gauss_cyclic_witness", gauss_product((1, 1, 1, 2))),
        ("positive_family_3_5", Matrix2(1, 3, 5, 16)),
    )
    require(len(rows) == len(samples) * MAX_POWER, "homogenization row count mismatch")
    final_errors: dict[str, mp.mpf] = {}
    reported_residuals: list[mp.mpf] = []
    position = 0
    for label, matrix in samples:
        trace = abs(matrix.trace())
        discriminant_root = mp.sqrt(trace * trace - 4)
        eigenvalue = (mp.mpf(trace) + discriminant_root) / 2
        length = 2 * mp.log(eigenvalue)
        for exponent in range(1, MAX_POWER + 1):
            row = rows[position]
            position += 1
            context = f"homogenization.csv:{position + 1}"
            power_c = abs(matrix.power(exponent).x10)
            literal = 2 * mp.log(power_c)
            prediction = (
                exponent * length
                + 2 * mp.log(mp.mpf(abs(matrix.x10)) / discriminant_root)
                + 2 * mp.log(1 - eigenvalue ** (-2 * exponent))
            )
            normalized = literal / exponent
            limit_error = abs(normalized - length)
            require(row["sample"] == label, f"{context}: sample mismatch")
            require(matrix_from_csv(row["matrix"], context) == matrix, f"{context}: matrix mismatch")
            require(integer(row["trace"], context) == matrix.trace(), f"{context}: trace mismatch")
            require(integer(row["base_c"], context) == abs(matrix.x10), f"{context}: base c mismatch")
            require(integer(row["power"], context) == exponent, f"{context}: exponent mismatch")
            require(integer(row["power_c"], context) == power_c, f"{context}: power c mismatch")
            close(number(row["two_log_power_c"], context), literal, f"{context}: literal")
            close(number(row["formula_prediction"], context), prediction, f"{context}: prediction")
            residual = number(row["formula_residual"], context)
            require(0 <= residual <= ROUNDING_RESIDUAL_LIMIT, f"{context}: formula residual too large")
            reported_residuals.append(residual)
            close(number(row["normalized_height"], context), normalized, f"{context}: normalized height")
            close(number(row["translation_length"], context), length, f"{context}: translation length")
            close(number(row["limit_error"], context), limit_error, f"{context}: limit error")
            if exponent == MAX_POWER:
                final_errors[label] = limit_error

    block = summary["homogenization"]
    require_keys(block, ("max_power", "max_formula_residual", "final_limit_errors"), "summary homogenization")
    require(block["max_power"] == MAX_POWER, "summary max power mismatch")
    require(number(block["max_formula_residual"], "summary homogenization residual") == max(reported_residuals), "summary max residual mismatch")
    require(set(block["final_limit_errors"]) == set(final_errors), "summary final-error labels mismatch")
    for label, expected in final_errors.items():
        close(number(block["final_limit_errors"][label], f"summary final error {label}"), expected, f"summary final error {label}")
    return len(rows)


def verify_dirichlet(results: Path, summary: dict[str, Any]) -> int:
    fields = (
        "point", "s_real", "s_imag", "cutoff", "partial_real", "partial_imag",
        "target_real", "target_imag", "absolute_error", "absolute_tail_bound",
        "within_tail_bound",
    )
    rows = read_csv(results / "dirichlet_convergence.csv", fields)
    points = (
        ("real_5_over_4", mp.mpc(mp.mpf(5) / 4, 0)),
        ("complex_3_over_2", mp.mpc(mp.mpf(3) / 2, mp.mpf(2) / 5)),
        ("real_2", mp.mpc(2, 0)),
    )
    cutoffs = (100, 1_000, 10_000, DIRICHLET_CUTOFF)
    require(len(rows) == len(points) * len(cutoffs), "Dirichlet row count mismatch")
    phi = totient_table(DIRICHLET_CUTOFF)
    position = 0
    all_within = True
    for label, s in points:
        target = mp.zeta(2 * s - 1) / mp.zeta(2 * s)
        partial = mp.mpc(0)
        cutoff_position = 0
        for level in range(1, DIRICHLET_CUTOFF + 1):
            partial += phi[level] * mp.power(level, -2 * s)
            if level != cutoffs[cutoff_position]:
                continue
            row = rows[position]
            position += 1
            context = f"dirichlet_convergence.csv:{position + 1}"
            sigma = mp.re(s)
            error = abs(target - partial)
            bound = mp.power(level, 2 - 2 * sigma) / (2 * sigma - 2)
            within = error <= bound
            all_within &= within
            require(row["point"] == label, f"{context}: point mismatch")
            close(number(row["s_real"], context), mp.re(s), f"{context}: s real")
            close(number(row["s_imag"], context), mp.im(s), f"{context}: s imag")
            require(integer(row["cutoff"], context) == level, f"{context}: cutoff mismatch")
            close(number(row["partial_real"], context), mp.re(partial), f"{context}: partial real")
            close(number(row["partial_imag"], context), mp.im(partial), f"{context}: partial imag")
            close(number(row["target_real"], context), mp.re(target), f"{context}: target real")
            close(number(row["target_imag"], context), mp.im(target), f"{context}: target imag")
            close(number(row["absolute_error"], context), error, f"{context}: error")
            close(number(row["absolute_tail_bound"], context), bound, f"{context}: tail bound")
            require(boolean(row["within_tail_bound"], context) == within, f"{context}: tail flag mismatch")
            cutoff_position += 1
            if cutoff_position == len(cutoffs):
                break

    block = summary["dirichlet"]
    require_keys(block, ("limit", "all_actual_errors_within_elementary_tail_bound", "physical_line_checks", "max_unitarity_residual", "max_functional_equation_residual"), "summary Dirichlet")
    require(block["limit"] == DIRICHLET_CUTOFF, "summary Dirichlet limit mismatch")
    require(block["all_actual_errors_within_elementary_tail_bound"] is all_within is True, "summary Dirichlet tail flag mismatch")
    physical = block["physical_line_checks"]
    require(isinstance(physical, list) and len(physical) == 3, "physical-line row count mismatch")
    reported_modulus: list[mp.mpf] = []
    reported_functional: list[mp.mpf] = []
    for row, t in zip(physical, (mp.mpf("0.7"), mp.mpf("2"), mp.mpf("7")), strict=True):
        require_keys(row, ("t", "coefficient", "modulus_residual", "functional_equation_residual"), "physical-line row")
        close(number(row["t"], "physical t"), t, "physical t")
        coefficient = scattering(mp.mpc(mp.mpf("0.5"), t))
        stored = row["coefficient"]
        require_keys(stored, ("real", "imag"), "physical coefficient")
        close(number(stored["real"], "coefficient real"), mp.re(coefficient), "coefficient real")
        close(number(stored["imag"], "coefficient imag"), mp.im(coefficient), "coefficient imag")
        modulus = number(row["modulus_residual"], "modulus residual")
        functional = number(row["functional_equation_residual"], "functional residual")
        require(0 <= modulus <= ROUNDING_RESIDUAL_LIMIT, "unitarity residual too large")
        require(0 <= functional <= ROUNDING_RESIDUAL_LIMIT, "functional-equation residual too large")
        reported_modulus.append(modulus)
        reported_functional.append(functional)
    require(number(block["max_unitarity_residual"], "max unitarity residual") == max(reported_modulus), "max unitarity residual summary mismatch")
    require(number(block["max_functional_equation_residual"], "max functional residual") == max(reported_functional), "max functional residual summary mismatch")
    return len(rows)


def verify_summary_schema(summary: dict[str, Any]) -> None:
    require_keys(
        summary,
        (
            "schema_version", "candidate_id", "precision_decimal_digits",
            "no_prime_or_zero_tables_used", "double_coset", "rigidity_family_rows",
            "chebyshev_rows", "gauss_word_rows",
            "gauss_words_with_cyclic_denominator_variation",
            "gauss_words_passing_literal_denominator_square_additivity",
            "homogenization", "dirichlet", "formal_route_a_signal",
        ),
        "summary.json",
    )
    require(summary["schema_version"] == SCHEMA_VERSION, "summary schema version mismatch")
    require(summary["candidate_id"] == CANDIDATE_ID, "summary candidate ID mismatch")
    require(summary["precision_decimal_digits"] == 80, "summary precision mismatch")
    require(summary["no_prime_or_zero_tables_used"] is True, "summary target-data flag mismatch")
    require(summary["formal_route_a_signal"] == {
        "open_arithmetic": "PROVED_CLASSICAL_INPUT",
        "denominator_only_closed_clock": "REFUTED",
        "stable_closed_clock": "SELBERG_TRANSLATION_LENGTH",
        "single_xi_by_zero_free_normalization": "REFUTED",
        "hilbert_polya_operator": "NOT_CONSTRUCTED",
    }, "formal Route-A signal mismatch")


def verify_results(results: Path) -> dict[str, Any]:
    """Verify the frozen result directory, returning a compact pass report."""

    mp.mp.dps = CHECK_PRECISION
    results = results.resolve()
    exact = read_json(results / "exact_certificates.json")
    summary = read_json(results / "summary.json")
    verify_summary_schema(summary)
    rigidity_rows, chebyshev_rows = verify_exact_certificates(exact, summary)
    double_coset_rows = verify_double_cosets(results, exact, summary)
    gauss_rows = verify_gauss_csv(results, summary)
    homogenization_rows = verify_homogenization(results, summary)
    dirichlet_rows = verify_dirichlet(results, summary)
    return {
        "candidate_id": CANDIDATE_ID,
        "checker_precision_decimal_digits": CHECK_PRECISION,
        "independent_of_producer_import": True,
        "status": "PASS",
        "verified_files": [
            "exact_certificates.json", "double_coset_counts.csv",
            "gauss_word_clock_audit.csv", "homogenization.csv",
            "dirichlet_convergence.csv", "summary.json",
        ],
        "verified_rows": {
            "rigidity_family": rigidity_rows,
            "chebyshev": chebyshev_rows,
            "double_coset": double_coset_rows,
            "gauss_word": gauss_rows,
            "homogenization": homogenization_rows,
            "dirichlet": dirichlet_rows,
        },
    }


def parse_args() -> argparse.Namespace:
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=project / "results")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="optional path for the machine-readable verification report",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    try:
        report = verify_results(arguments.results)
    except VerificationError as error:
        raise SystemExit(f"FAIL: {error}") from error
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        with arguments.output.open("w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, sort_keys=True)
            handle.write("\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
