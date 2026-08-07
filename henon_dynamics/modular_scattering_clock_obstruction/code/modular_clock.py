#!/usr/bin/env python3
"""Exact and high-precision audit for the HCS-C17 modular cusp clock.

The exact core uses integer matrices.  ``mpmath`` is used only for frozen
high-precision illustrations of identities that are proved separately.
No prime table or Riemann-zero table is read.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable, Iterator, Sequence

import mpmath as mp


CANDIDATE_ID = "HCS-C17"
SCHEMA_VERSION = 1
DEFAULT_PRECISION = 80


@dataclass(frozen=True, slots=True)
class Mat2:
    """A 2 by 2 integer matrix, stored by rows."""

    a: int
    b: int
    c: int
    d: int

    def __matmul__(self, other: "Mat2") -> "Mat2":
        return Mat2(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d,
        )

    @property
    def det(self) -> int:
        return self.a * self.d - self.b * self.c

    @property
    def trace(self) -> int:
        return self.a + self.d

    def inverse(self) -> "Mat2":
        if self.det not in (-1, 1):
            raise ValueError("inverse is integral only for determinant +/-1")
        q = self.det
        return Mat2(self.d // q, -self.b // q, -self.c // q, self.a // q)

    def power(self, exponent: int) -> "Mat2":
        if exponent < 0:
            return self.inverse().power(-exponent)
        result = IDENTITY
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result @ base
            base = base @ base
            n >>= 1
        return result

    def conjugate_by(self, change: "Mat2") -> "Mat2":
        return change.inverse() @ self @ change

    def to_rows(self) -> list[list[int]]:
        return [[self.a, self.b], [self.c, self.d]]


IDENTITY = Mat2(1, 0, 0, 1)
T = Mat2(1, 1, 0, 1)
S = Mat2(0, -1, 1, 0)


def euler_phi(n: int) -> int:
    if n < 1:
        raise ValueError("Euler phi expects a positive integer")
    result = n
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            while value % p == 0:
                value //= p
            result -= result // p
        p += 1
    if value > 1:
        result -= result // value
    return result


def phi_sieve(limit: int) -> list[int]:
    if limit < 1:
        raise ValueError("limit must be positive")
    phi = list(range(limit + 1))
    phi[1] = 1
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def cusp_double_coset_representatives(c: int) -> list[Mat2]:
    """Represent oriented big-cell double cosets with lower-left entry c.

    For c > 1, d runs through (Z/cZ)^x and a is its inverse modulo c.
    For c = 1 the unique residue is represented by S.
    """

    if c < 1:
        raise ValueError("c must be positive")
    if c == 1:
        return [S]
    representatives: list[Mat2] = []
    for d in range(1, c):
        if math.gcd(c, d) != 1:
            continue
        a = pow(d, -1, c)
        b = (a * d - 1) // c
        matrix = Mat2(a, b, c, d)
        if matrix.det != 1:
            raise AssertionError("double-coset representative lost determinant one")
        representatives.append(matrix)
    return representatives


def cusp_double_coset_key(matrix: Mat2) -> tuple[int, int]:
    """Return the (positive c, d mod c) key in PSL sign convention."""

    if matrix.det != 1 or matrix.c == 0:
        raise ValueError("matrix must lie in SL2(Z) and in the big Bruhat cell")
    c = matrix.c
    d = matrix.d
    if c < 0:
        c, d = -c, -d
    return c, d % c


def chebyshev_trace_factor(trace: int, exponent: int) -> int:
    """Return U_{exponent-1}(trace/2) by its integral recurrence."""

    if exponent < 1:
        raise ValueError("exponent must be at least one")
    if exponent == 1:
        return 1
    previous, current = 1, trace
    for _ in range(2, exponent):
        previous, current = current, trace * current - previous
    return current


def gauss_branch(digit: int) -> Mat2:
    """The standard inverse-branch matrix A_a = [[0,1],[1,a]]."""

    if digit < 1:
        raise ValueError("Gauss digits are positive")
    return Mat2(0, 1, 1, digit)


def word_product(word: Sequence[int]) -> Mat2:
    matrix = IDENTITY
    for digit in word:
        matrix = matrix @ gauss_branch(digit)
    return matrix


def rotations(word: Sequence[int], step: int = 1) -> Iterator[tuple[int, ...]]:
    frozen = tuple(word)
    for offset in range(0, len(frozen), step):
        yield frozen[offset:] + frozen[:offset]


def is_primitive_word(word: Sequence[int]) -> bool:
    frozen = tuple(word)
    n = len(frozen)
    for block_length in range(1, n):
        if n % block_length == 0 and frozen == frozen[:block_length] * (n // block_length):
            return False
    return True


def canonical_even_rotation(word: Sequence[int]) -> tuple[int, ...]:
    if len(word) % 2:
        raise ValueError("two-step PSL coding requires even word length")
    return min(rotations(word, step=2))


def positive_hyperbolic_family(m: int, n: int) -> Mat2:
    """gamma_{m,n} = [[1,m],[n,1+mn]], used in the F-rigidity proof."""

    if m < 1 or n < 1:
        raise ValueError("m and n must be positive")
    matrix = Mat2(1, m, n, 1 + m * n)
    if matrix.det != 1 or matrix.trace <= 2:
        raise AssertionError("rigidity family must be positive hyperbolic in SL2(Z)")
    return matrix


def mp_string(value: mp.mpf | mp.mpc, digits: int = 70) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False)


def complex_record(value: mp.mpc, digits: int = 70) -> dict[str, str]:
    return {
        "real": mp_string(mp.re(value), digits),
        "imag": mp_string(mp.im(value), digits),
    }


def translation_length(matrix: Mat2) -> mp.mpf:
    trace = abs(matrix.trace)
    if matrix.det != 1 or trace <= 2:
        raise ValueError("translation length requires a hyperbolic SL2 matrix")
    lam = (mp.mpf(trace) + mp.sqrt(trace * trace - 4)) / 2
    return 2 * mp.log(lam)


def stable_defect_formula(matrix: Mat2, exponent: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return literal height, formula prediction, and translation length."""

    if matrix.c == 0:
        raise ValueError("lower-left entry must be nonzero")
    trace = abs(matrix.trace)
    if matrix.det != 1 or trace <= 2:
        raise ValueError("matrix must be hyperbolic in SL2")
    power = matrix.power(exponent)
    literal = 2 * mp.log(abs(power.c))
    lam = (mp.mpf(trace) + mp.sqrt(trace * trace - 4)) / 2
    length = 2 * mp.log(lam)
    predicted = (
        exponent * length
        + 2 * mp.log(mp.mpf(abs(matrix.c)) / mp.sqrt(trace * trace - 4))
        + 2 * mp.log(1 - lam ** (-2 * exponent))
    )
    return literal, predicted, length


def scattering_coefficient(s: mp.mpc) -> mp.mpc:
    return (
        mp.sqrt(mp.pi)
        * mp.gamma(s - mp.mpf("0.5"))
        / mp.gamma(s)
        * mp.zeta(2 * s - 1)
        / mp.zeta(2 * s)
    )


def build_double_coset_audit(cutoff: int) -> tuple[list[dict[str, int]], dict[str, object]]:
    rows: list[dict[str, int]] = []
    all_counts_match = True
    all_keys_unique = True
    all_actions_preserve_key = True
    for c in range(1, cutoff + 1):
        representatives = cusp_double_coset_representatives(c)
        keys = [cusp_double_coset_key(matrix) for matrix in representatives]
        expected = euler_phi(c)
        all_counts_match &= len(representatives) == expected
        all_keys_unique &= len(set(keys)) == len(keys)
        for matrix in representatives:
            key = cusp_double_coset_key(matrix)
            for left_power, right_power in ((-2, 3), (1, -1), (4, 2)):
                moved = T.power(left_power) @ matrix @ T.power(right_power)
                all_actions_preserve_key &= cusp_double_coset_key(moved) == key
        rows.append({"c": c, "enumerated": len(representatives), "euler_phi": expected})
    summary = {
        "cutoff": cutoff,
        "all_counts_match": all_counts_match,
        "all_keys_unique": all_keys_unique,
        "parabolic_left_right_actions_preserve_key": all_actions_preserve_key,
    }
    return rows, summary


def build_exact_certificates(rigidity_cutoff: int) -> dict[str, object]:
    conjugacy_matrix = Mat2(2, 1, 3, 2)
    conjugate = conjugacy_matrix.conjugate_by(S)

    gauss_word = (1, 1, 1, 2)
    shifted_word = (1, 2, 1, 1)
    gauss_matrix = word_product(gauss_word)
    shifted_matrix = word_product(shifted_word)
    prefix = word_product((1, 1))
    if gauss_matrix.conjugate_by(prefix) != shifted_matrix:
        raise AssertionError("frozen PSL Gauss cyclic witness is not conjugate")

    family_rows: list[dict[str, object]] = []
    for m in range(1, rigidity_cutoff + 1):
        for n in range(1, rigidity_cutoff + 1):
            matrix = positive_hyperbolic_family(m, n)
            square = matrix.power(2)
            expected = n * (2 + m * n)
            family_rows.append(
                {
                    "m": m,
                    "n": n,
                    "matrix": matrix.to_rows(),
                    "c": matrix.c,
                    "trace": matrix.trace,
                    "c_square": square.c,
                    "expected_c_square": expected,
                    "identity_pass": square.c == expected,
                }
            )

    chebyshev_samples = [
        Mat2(2, 1, 3, 2),
        word_product((1, 1)),
        word_product((1, 1, 1, 2)),
        positive_hyperbolic_family(3, 5),
    ]
    chebyshev_rows: list[dict[str, object]] = []
    for matrix in chebyshev_samples:
        for exponent in range(1, 13):
            actual = matrix.power(exponent).c
            factor = chebyshev_trace_factor(matrix.trace, exponent)
            predicted = matrix.c * factor
            chebyshev_rows.append(
                {
                    "matrix": matrix.to_rows(),
                    "trace": matrix.trace,
                    "exponent": exponent,
                    "actual_c": actual,
                    "trace_factor": factor,
                    "predicted_c": predicted,
                    "identity_pass": actual == predicted,
                }
            )

    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "source_lock": {
            "group": "PSL2(Z) with explicit SL2(Z) lifts",
            "cusp_subgroup": "P=<T>, T=[[1,1],[0,1]]",
            "oriented_double_coset_convention": "choose lower-left entry c>0",
            "closed_clock_scope": "final-monodromy denominator-only F(alpha*abs(c))",
            "allowed_data": ["exact integer matrices", "primary literature"],
            "forbidden_data": ["prime tables", "Riemann-zero tables", "fitted scales"],
        },
        "double_coset_theorem": {
            "level_parameter": "(c, d mod c), c>=1, gcd(c,d)=1",
            "oriented_level_multiplicity": "EulerPhi(c)",
            "dirichlet_identity": "sum phi(c)c^(-2s)=zeta(2s-1)/zeta(2s), Re(s)>1",
            "full_scattering_factor": "sqrt(pi)Gamma(s-1/2)/Gamma(s) times the Dirichlet identity",
        },
        "conjugacy_witness": {
            "matrix": conjugacy_matrix.to_rows(),
            "conjugator": S.to_rows(),
            "conjugate": conjugate.to_rows(),
            "trace_pair": [conjugacy_matrix.trace, conjugate.trace],
            "absolute_c_pair": [abs(conjugacy_matrix.c), abs(conjugate.c)],
            "pass": conjugacy_matrix.trace == conjugate.trace
            and abs(conjugacy_matrix.c) != abs(conjugate.c),
        },
        "psl_gauss_cyclic_witness": {
            "word": list(gauss_word),
            "two_digit_shift": list(shifted_word),
            "matrix": gauss_matrix.to_rows(),
            "shifted_matrix": shifted_matrix.to_rows(),
            "sl2_conjugator": prefix.to_rows(),
            "trace_pair": [gauss_matrix.trace, shifted_matrix.trace],
            "absolute_c_pair": [abs(gauss_matrix.c), abs(shifted_matrix.c)],
            "pass": gauss_matrix.trace == shifted_matrix.trace
            and abs(gauss_matrix.c) != abs(shifted_matrix.c),
        },
        "denominator_rigidity": {
            "theorem": (
                "For alpha>0, if F(alpha*|c(g^2)|)=2F(alpha*|c(g)|) "
                "for every entry-positive hyperbolic g in SL2(Z), then F vanishes on alpha*N."
            ),
            "positive_family": "gamma_mn=[[1,m],[n,1+mn]]",
            "family_rows": family_rows,
            "proof_relations": {
                "n_equals_1": "F(alpha*(m+2))=2F(alpha), all m>=1",
                "n_equals_r_m_equals_1": "F(alpha*r*(r+2))=2F(alpha*r), r>=3",
                "deduction": "F(alpha)=0, then F(alpha*r)=0 for r=1 and r>=3",
                "remaining_r_equals_2": "F(8alpha)=2F(2alpha), hence F(2alpha)=0",
            },
            "all_family_identities_pass": all(row["identity_pass"] for row in family_rows),
        },
        "chebyshev_power_identity": {
            "formula": "c(g^n)=c(g)U_(n-1)(tr(g)/2)",
            "rows": chebyshev_rows,
            "all_pass": all(row["identity_pass"] for row in chebyshev_rows),
        },
        "stable_closure": {
            "formula": (
                "2log|c(g^n)|=n*ell(g)+2log(|c(g)|/sqrt(t^2-4))"
                "+2log(1-lambda^(-2n))"
            ),
            "limit": "lim_n 2log|c(g^n)|/n=ell(g)=2log(lambda)",
        },
        "divisor_no_go": {
            "Lambda": "pi^(-u/2)Gamma(u/2)zeta(u)",
            "Phi": "Lambda(2s-1)/Lambda(2s)",
            "nontrivial_poles": "s=rho/2",
            "nontrivial_zeros": "s=(1+rho)/2",
            "allowed_normalization": "nonconstant affine reparametrization and entire zero-free prefactor",
            "excluded_compensator": "any factor carrying a zeta-zero divisor",
        },
    }


def build_gauss_word_audit(max_length: int, max_digit: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in range(2, max_length + 1, 2):
        for word in product(range(1, max_digit + 1), repeat=length):
            if not is_primitive_word(word) or tuple(word) != canonical_even_rotation(word):
                continue
            matrices = [word_product(rotation) for rotation in rotations(word, step=2)]
            traces = [matrix.trace for matrix in matrices]
            c_values = [abs(matrix.c) for matrix in matrices]
            matrix = matrices[0]
            square = matrix.power(2)
            rows.append(
                {
                    "word": " ".join(map(str, word)),
                    "length": length,
                    "matrix": json.dumps(matrix.to_rows(), separators=(",", ":")),
                    "trace": matrix.trace,
                    "cyclic_trace_invariant": len(set(traces)) == 1,
                    "cyclic_c_values": " ".join(map(str, c_values)),
                    "cyclic_c_invariant": len(set(c_values)) == 1,
                    "c_square": abs(square.c),
                    "c_squared": abs(matrix.c) ** 2,
                    "literal_denominator_power_additive": abs(square.c) == abs(matrix.c) ** 2,
                }
            )
    return rows


def build_homogenization_rows(max_power: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    samples = {
        "conjugacy_witness": Mat2(2, 1, 3, 2),
        "gauss_112": word_product((1, 1)),
        "gauss_cyclic_witness": word_product((1, 1, 1, 2)),
        "positive_family_3_5": positive_hyperbolic_family(3, 5),
    }
    rows: list[dict[str, object]] = []
    max_formula_residual = mp.mpf("0")
    final_limit_errors: dict[str, str] = {}
    for label, matrix in samples.items():
        for exponent in range(1, max_power + 1):
            literal, predicted, length = stable_defect_formula(matrix, exponent)
            residual = abs(literal - predicted)
            max_formula_residual = max(max_formula_residual, residual)
            limit_error = abs(literal / exponent - length)
            if exponent == max_power:
                final_limit_errors[label] = mp_string(limit_error)
            rows.append(
                {
                    "sample": label,
                    "matrix": json.dumps(matrix.to_rows(), separators=(",", ":")),
                    "trace": matrix.trace,
                    "base_c": abs(matrix.c),
                    "power": exponent,
                    "power_c": abs(matrix.power(exponent).c),
                    "two_log_power_c": mp_string(literal),
                    "formula_prediction": mp_string(predicted),
                    "formula_residual": mp_string(residual),
                    "normalized_height": mp_string(literal / exponent),
                    "translation_length": mp_string(length),
                    "limit_error": mp_string(limit_error),
                }
            )
    summary = {
        "max_power": max_power,
        "max_formula_residual": mp_string(max_formula_residual),
        "final_limit_errors": final_limit_errors,
    }
    return rows, summary


def build_dirichlet_rows(limit: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    phi = phi_sieve(limit)
    frozen_points = [
        ("real_5_over_4", mp.mpc(mp.mpf(5) / 4, 0)),
        ("complex_3_over_2", mp.mpc(mp.mpf(3) / 2, mp.mpf(2) / 5)),
        ("real_2", mp.mpc(2, 0)),
    ]
    candidate_cutoffs = [100, 1_000, 10_000, limit]
    cutoffs = sorted({value for value in candidate_cutoffs if value <= limit})
    rows: list[dict[str, object]] = []
    all_within_tail_bound = True
    for label, s in frozen_points:
        target = mp.zeta(2 * s - 1) / mp.zeta(2 * s)
        partial = mp.mpc(0)
        cutoff_index = 0
        for c in range(1, limit + 1):
            partial += mp.mpf(phi[c]) * mp.power(c, -2 * s)
            if cutoff_index < len(cutoffs) and c == cutoffs[cutoff_index]:
                sigma = mp.re(s)
                tail_bound = mp.power(c, 2 - 2 * sigma) / (2 * sigma - 2)
                actual_error = abs(target - partial)
                within = actual_error <= tail_bound
                all_within_tail_bound &= bool(within)
                rows.append(
                    {
                        "point": label,
                        "s_real": mp_string(mp.re(s)),
                        "s_imag": mp_string(mp.im(s)),
                        "cutoff": c,
                        "partial_real": mp_string(mp.re(partial)),
                        "partial_imag": mp_string(mp.im(partial)),
                        "target_real": mp_string(mp.re(target)),
                        "target_imag": mp_string(mp.im(target)),
                        "absolute_error": mp_string(actual_error),
                        "absolute_tail_bound": mp_string(tail_bound),
                        "within_tail_bound": bool(within),
                    }
                )
                cutoff_index += 1
    physical_rows: list[dict[str, object]] = []
    max_unitarity_residual = mp.mpf("0")
    max_functional_residual = mp.mpf("0")
    for t in (mp.mpf("0.7"), mp.mpf("2"), mp.mpf("7")):
        s = mp.mpc(mp.mpf("0.5"), t)
        coefficient = scattering_coefficient(s)
        modulus_residual = abs(abs(coefficient) - 1)
        functional_residual = abs(coefficient * scattering_coefficient(1 - s) - 1)
        max_unitarity_residual = max(max_unitarity_residual, modulus_residual)
        max_functional_residual = max(max_functional_residual, functional_residual)
        physical_rows.append(
            {
                "t": mp_string(t),
                "coefficient": complex_record(coefficient),
                "modulus_residual": mp_string(modulus_residual),
                "functional_equation_residual": mp_string(functional_residual),
            }
        )
    summary = {
        "limit": limit,
        "all_actual_errors_within_elementary_tail_bound": all_within_tail_bound,
        "physical_line_checks": physical_rows,
        "max_unitarity_residual": mp_string(max_unitarity_residual),
        "max_functional_equation_residual": mp_string(max_functional_residual),
    }
    return rows, summary


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"cannot write empty CSV: {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def generate_results(
    output: Path,
    double_coset_cutoff: int,
    rigidity_cutoff: int,
    word_max_length: int,
    word_max_digit: int,
    max_power: int,
    dirichlet_cutoff: int,
    precision: int,
) -> dict[str, object]:
    mp.mp.dps = precision
    output.mkdir(parents=True, exist_ok=True)

    exact_certificates = build_exact_certificates(rigidity_cutoff)
    double_coset_rows, double_coset_summary = build_double_coset_audit(double_coset_cutoff)
    word_rows = build_gauss_word_audit(word_max_length, word_max_digit)
    homogenization_rows, homogenization_summary = build_homogenization_rows(max_power)
    dirichlet_rows, dirichlet_summary = build_dirichlet_rows(dirichlet_cutoff)

    exact_certificates["double_coset_finite_audit"] = double_coset_summary
    write_json(output / "exact_certificates.json", exact_certificates)
    write_csv(output / "double_coset_counts.csv", double_coset_rows)
    write_csv(output / "gauss_word_clock_audit.csv", word_rows)
    write_csv(output / "homogenization.csv", homogenization_rows)
    write_csv(output / "dirichlet_convergence.csv", dirichlet_rows)

    cyclic_variation_count = sum(not bool(row["cyclic_c_invariant"]) for row in word_rows)
    literal_additivity_count = sum(
        bool(row["literal_denominator_power_additive"]) for row in word_rows
    )
    summary = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "precision_decimal_digits": precision,
        "no_prime_or_zero_tables_used": True,
        "double_coset": double_coset_summary,
        "rigidity_family_rows": len(exact_certificates["denominator_rigidity"]["family_rows"]),
        "chebyshev_rows": len(exact_certificates["chebyshev_power_identity"]["rows"]),
        "gauss_word_rows": len(word_rows),
        "gauss_words_with_cyclic_denominator_variation": cyclic_variation_count,
        "gauss_words_passing_literal_denominator_square_additivity": literal_additivity_count,
        "homogenization": homogenization_summary,
        "dirichlet": dirichlet_summary,
        "formal_route_a_signal": {
            "open_arithmetic": "PROVED_CLASSICAL_INPUT",
            "denominator_only_closed_clock": "REFUTED",
            "stable_closed_clock": "SELBERG_TRANSLATION_LENGTH",
            "single_xi_by_zero_free_normalization": "REFUTED",
            "hilbert_polya_operator": "NOT_CONSTRUCTED",
        },
    }
    write_json(output / "summary.json", summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument("--double-coset-cutoff", type=int, default=80)
    parser.add_argument("--rigidity-cutoff", type=int, default=20)
    parser.add_argument("--word-max-length", type=int, default=6)
    parser.add_argument("--word-max-digit", type=int, default=3)
    parser.add_argument("--max-power", type=int, default=24)
    parser.add_argument("--dirichlet-cutoff", type=int, default=50_000)
    parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = generate_results(
        output=args.output,
        double_coset_cutoff=args.double_coset_cutoff,
        rigidity_cutoff=args.rigidity_cutoff,
        word_max_length=args.word_max_length,
        word_max_digit=args.word_max_digit,
        max_power=args.max_power,
        dirichlet_cutoff=args.dirichlet_cutoff,
        precision=args.precision,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
