#!/usr/bin/env python3
"""Exact first-gate producer for the HCS-C23 ramification spectrum.

The finite fixed algebra is represented in its square-free monomial basis.
All calculations are exact over finite prime fields.  Chronological Hénon
letters act in their original order; no transition or multiplier is averaged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import numpy as np
import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c23_first_gate_certificate.json"
BAD_PRIMES = {2, 5, 59, 61}
PARAMETER_NUMERATORS = {"0": 59, "1": 61}
PAIR7 = ("0000101", "0001001")
PAIR8 = ("00101011", "00101101")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prime-bound", type=int, default=43)
    parser.add_argument("--max-repetition", type=int, default=12)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rotations(word: str) -> list[str]:
    return [word[index:] + word[:index] for index in range(len(word))]


def primitive(word: str) -> bool:
    return all(word != word[:period] * (len(word) // period) for period in range(1, len(word)) if len(word) % period == 0)


def dihedrally_equivalent(first: str, second: str) -> bool:
    return second in rotations(first) or second in rotations(first[::-1])


def cyclic_gram_counts(word: str, width: int) -> dict[str, int]:
    counts: dict[str, int] = {}
    doubled = word + word[: width - 1]
    for index in range(len(word)):
        gram = doubled[index : index + width]
        counts[gram] = counts.get(gram, 0) + 1
    return dict(sorted(counts.items()))


class FixedAlgebraModP:
    """Square-free quotient algebra for one chronological word over F_p."""

    def __init__(self, word: str, prime: int):
        if len(word) < 3:
            raise ValueError("the first gate uses periods n>=3")
        if prime in BAD_PRIMES or not sp.isprime(prime):
            raise ValueError("prime is not degree-good for the localized family")
        self.word = word
        self.p = prime
        self.n = len(word)
        self.dimension = 1 << self.n
        inverse_ten = pow(10, -1, prime)
        self.parameters = [
            PARAMETER_NUMERATORS[letter] * inverse_ten % prime for letter in word
        ]
        self._transitions = self._build_variable_transitions()

    def _build_variable_transitions(self) -> list[list[tuple[tuple[int, int], ...]]]:
        p, n, parameters = self.p, self.n, self.parameters

        @lru_cache(None)
        def reduce_exponents(exponents: tuple[int, ...]) -> dict[int, int]:
            for index, exponent in enumerate(exponents):
                if exponent < 2:
                    continue
                base = list(exponents)
                base[index] -= 2
                inverse_parameter = pow(parameters[index], -1, p)
                output: dict[int, int] = {}
                # a_i*x_i^2 + x_(i-1) + x_(i+1) - 1 = 0.
                for coefficient, neighbor in (
                    (1, None),
                    (-1, (index - 1) % n),
                    (-1, (index + 1) % n),
                ):
                    child = base.copy()
                    if neighbor is not None:
                        child[neighbor] += 1
                    for mask, value in reduce_exponents(tuple(child)).items():
                        output[mask] = (
                            output.get(mask, 0)
                            + coefficient * inverse_parameter * value
                        ) % p
                return {mask: value for mask, value in output.items() if value}
            mask = sum(
                1 << index for index, exponent in enumerate(exponents) if exponent
            )
            return {mask: 1}

        transitions: list[list[tuple[tuple[int, int], ...]]] = []
        for variable in range(n):
            columns = []
            for mask in range(self.dimension):
                exponents = [(mask >> index) & 1 for index in range(n)]
                exponents[variable] += 1
                columns.append(tuple(sorted(reduce_exponents(tuple(exponents)).items())))
            transitions.append(columns)
        return transitions

    def multiply_variable(self, vector: np.ndarray, variable: int) -> np.ndarray:
        output = np.zeros(self.dimension, dtype=np.int64)
        for source in np.flatnonzero(vector):
            value = int(vector[source])
            for target, coefficient in self._transitions[variable][int(source)]:
                output[target] = (
                    output[target] + value * coefficient
                ) % self.p
        return output

    def basis_vector(self, mask: int) -> np.ndarray:
        vector = np.zeros(self.dimension, dtype=np.int64)
        vector[mask] = 1
        return vector

    def relation_check(self) -> bool:
        for variable, parameter in enumerate(self.parameters):
            left_neighbor = (variable - 1) % self.n
            right_neighbor = (variable + 1) % self.n
            for mask in range(self.dimension):
                basis = self.basis_vector(mask)
                residual = (
                    parameter
                    * self.multiply_variable(
                        self.multiply_variable(basis, variable), variable
                    )
                    + self.multiply_variable(basis, left_neighbor)
                    + self.multiply_variable(basis, right_neighbor)
                    - basis
                ) % self.p
                if np.any(residual):
                    return False
        return True

    def trace_element(self) -> np.ndarray:
        """Trace of J_(n-1)...J_0 as an element of the quotient algebra."""

        zero = np.zeros(self.dimension, dtype=np.int64)
        one = self.basis_vector(0)
        m00, m01, m10, m11 = one, zero.copy(), zero.copy(), one.copy()
        for index, parameter in enumerate(self.parameters):
            new00 = (
                -2 * parameter * self.multiply_variable(m00, index) - m10
            ) % self.p
            new01 = (
                -2 * parameter * self.multiply_variable(m01, index) - m11
            ) % self.p
            m00, m01, m10, m11 = new00, new01, m00, m01
        return (m00 + m11) % self.p

    def multiplication_matrix(self, element: np.ndarray) -> np.ndarray:
        matrix = np.empty(
            (self.dimension, self.dimension), dtype=np.int64
        )
        for mask in range(self.dimension):
            product = element.copy()
            for variable in range(self.n):
                if (mask >> variable) & 1:
                    product = self.multiply_variable(product, variable)
            matrix[:, mask] = product
        return matrix % self.p

    def trace_multiplication_matrix(self) -> np.ndarray:
        return self.multiplication_matrix(self.trace_element())


def rank_mod_prime(matrix: np.ndarray, prime: int) -> int:
    """Exact Gauss--Jordan rank; vectorized arithmetic stays below int64."""

    work = matrix.copy() % prime
    rows, columns = work.shape
    rank = 0
    for column in range(columns):
        nonzero = np.flatnonzero(work[rank:, column])
        if not len(nonzero):
            continue
        pivot = rank + int(nonzero[0])
        work[[rank, pivot]] = work[[pivot, rank]]
        work[rank] = (
            work[rank] * pow(int(work[rank, column]), -1, prime)
        ) % prime
        affected = np.flatnonzero(work[:, column])
        affected = affected[affected != rank]
        for start in range(0, len(affected), 32):
            batch = affected[start : start + 32]
            work[batch] = (
                work[batch]
                - work[batch, column, None] * work[rank]
            ) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def repetition_nullities(
    trace_matrix: np.ndarray, prime: int, max_repetition: int
) -> list[dict[str, object]]:
    """Kernel dimensions of multiplication by 2-2*T_r(t/2)."""

    dimension = trace_matrix.shape[0]
    identity = np.eye(dimension, dtype=np.int64)
    s_previous = (2 * identity) % prime  # 2*T_0(t/2)
    s_current = trace_matrix.copy() % prime  # 2*T_1(t/2)
    rows = []
    event_repetitions: list[int] = []
    for repetition in range(1, max_repetition + 1):
        if repetition == 1:
            s_value = s_current
        else:
            s_next = (
                trace_matrix @ s_current - s_previous
            ) % prime
            s_previous, s_current = s_current, s_next
            s_value = s_current
        lefschetz = (2 * identity - s_value) % prime
        nullity = dimension - rank_mod_prime(lefschetz, prime)
        if nullity:
            event_repetitions.append(repetition)
        rows.append(
            {
                "repetition": repetition,
                "multiplication_kernel_dimension": nullity,
                "packet_norm_divisible": nullity > 0,
            }
        )

    divisibility_control = all(
        multiple in event_repetitions
        for repetition in event_repetitions
        for multiple in range(repetition, max_repetition + 1, repetition)
    )
    return [
        {
            "rows": rows,
            "event_repetitions": event_repetitions,
            "divisor_closed_control": divisibility_control,
        }
    ]


def monodromy_and_image(
    word: str, prime: int, q: int, previous: int
) -> tuple[int, int, tuple[tuple[int, int], tuple[int, int]]]:
    inverse_ten = pow(10, -1, prime)
    parameters = [
        PARAMETER_NUMERATORS[letter] * inverse_ten % prime for letter in word
    ]
    m00, m01, m10, m11 = 1, 0, 0, 1
    current, old = q, previous
    for parameter in parameters:
        j00, j01 = -2 * parameter * current % prime, -1 % prime
        m00, m01, m10, m11 = (
            (j00 * m00 + j01 * m10) % prime,
            (j00 * m01 + j01 * m11) % prime,
            m00,
            m01,
        )
        current, old = (
            (1 - parameter * current * current - old) % prime,
            current,
        )
    return current, old, ((m00, m01), (m10, m11))


def rational_fixed_points(word: str, prime: int) -> dict[str, object]:
    fixed = []
    degenerate = []
    for q in range(prime):
        for previous in range(prime):
            image_q, image_previous, matrix = monodromy_and_image(
                word, prime, q, previous
            )
            if (image_q, image_previous) != (q, previous):
                continue
            trace = (matrix[0][0] + matrix[1][1]) % prime
            det_i_minus = (
                (1 - matrix[0][0]) * (1 - matrix[1][1])
                - matrix[0][1] * matrix[1][0]
            ) % prime
            row = {
                "q": q,
                "p": previous,
                "trace": trace,
                "det_I_minus_M": det_i_minus,
                "monodromy": [list(matrix[0]), list(matrix[1])],
            }
            fixed.append(row)
            if det_i_minus == 0:
                degenerate.append(row)
    return {
        "rational_fixed_count": len(fixed),
        "rational_degenerate_count": len(degenerate),
        "rational_degenerate_points": degenerate,
    }


def evaluate(word: str, prime: int) -> dict[str, object]:
    algebra = FixedAlgebraModP(word, prime)
    trace_matrix = algebra.trace_multiplication_matrix()
    identity = 2 * np.eye(algebra.dimension, dtype=np.int64)
    nullity = algebra.dimension - rank_mod_prime(
        (identity - trace_matrix) % prime, prime
    )
    return {
        "word": word,
        "period": len(word),
        "prime": prime,
        "fixed_algebra_rank": algebra.dimension,
        "relations_pass": algebra.relation_check(),
        "r1_multiplication_kernel_dimension": nullity,
        "r1_packet_norm_divisible": nullity > 0,
        "rational_points": rational_fixed_points(word, prime),
        "trace_matrix": trace_matrix,
    }


def public_evaluation(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "trace_matrix"}


def main() -> None:
    args = parse_args()
    if args.prime_bound < 11:
        raise ValueError("prime-bound must include the decisive prime 11")
    if args.max_repetition < 2 or args.max_repetition > 16:
        raise ValueError("max-repetition must lie in [2,16]")

    pair_metadata = [
        {
            "id": "C22_PERIOD7_SAME_BIGRAM",
            "words": list(PAIR7),
            "period": 7,
            "matched_width": 2,
            "gram_ledger": cyclic_gram_counts(PAIR7[0], 2),
            "matched": cyclic_gram_counts(PAIR7[0], 2)
            == cyclic_gram_counts(PAIR7[1], 2),
            "primitive": all(primitive(word) for word in PAIR7),
            "non_dihedral_pair": not dihedrally_equivalent(*PAIR7),
        },
        {
            "id": "C22_PERIOD8_SAME_TRIGRAM",
            "words": list(PAIR8),
            "period": 8,
            "matched_width": 3,
            "gram_ledger": cyclic_gram_counts(PAIR8[0], 3),
            "matched": cyclic_gram_counts(PAIR8[0], 3)
            == cyclic_gram_counts(PAIR8[1], 3),
            "primitive": all(primitive(word) for word in PAIR8),
            "non_dihedral_pair": not dihedrally_equivalent(*PAIR8),
        },
    ]

    scan_rows = []
    for prime in sp.primerange(3, args.prime_bound + 1):
        if prime in BAD_PRIMES:
            continue
        for pair_id, pair in (("n7", PAIR7), ("n8", PAIR8)):
            evaluations = [evaluate(word, int(prime)) for word in pair]
            scan_rows.append(
                {
                    "pair": pair_id,
                    "prime": int(prime),
                    "words": list(pair),
                    "kernel_dimensions": [
                        row["r1_multiplication_kernel_dimension"]
                        for row in evaluations
                    ],
                    "norm_divisibility": [
                        row["r1_packet_norm_divisible"] for row in evaluations
                    ],
                    "distinguishes_divisibility": evaluations[0][
                        "r1_packet_norm_divisible"
                    ]
                    != evaluations[1]["r1_packet_norm_divisible"],
                }
            )

    decisive_specs = [
        ("n7", 11, PAIR7),
        ("n8", 3, PAIR8),
    ]
    decisive_rows = []
    repetition_rows = []
    symmetry_rows = []
    for pair_id, prime, pair in decisive_specs:
        evaluations = [evaluate(word, prime) for word in pair]
        decisive_rows.append(
            {
                "pair": pair_id,
                "prime": prime,
                "residue_degree_witness": 1,
                "evaluations": [public_evaluation(row) for row in evaluations],
                "asymmetric_packet_norm_divisibility": evaluations[0][
                    "r1_packet_norm_divisible"
                ]
                != evaluations[1]["r1_packet_norm_divisible"],
            }
        )
        for row in evaluations:
            repetition_rows.append(
                {
                    "pair": pair_id,
                    "word": row["word"],
                    "prime": prime,
                    "max_repetition": args.max_repetition,
                    **repetition_nullities(
                        row["trace_matrix"], prime, args.max_repetition
                    )[0],
                }
            )

        for word in pair:
            rotation_values = [
                evaluate(rotated, prime)["r1_multiplication_kernel_dimension"]
                for rotated in rotations(word)
            ]
            reverse_value = evaluate(word[::-1], prime)[
                "r1_multiplication_kernel_dimension"
            ]
            symmetry_rows.append(
                {
                    "word": word,
                    "prime": prime,
                    "rotation_kernel_dimensions": rotation_values,
                    "cyclic_rotation_invariant": len(set(rotation_values)) == 1,
                    "reverse_kernel_dimension": reverse_value,
                    "reversal_equality_control": reverse_value
                    == rotation_values[0],
                    "reversal_quotiented": False,
                }
            )

    all_relations = all(
        evaluation["relations_pass"]
        for row in decisive_rows
        for evaluation in row["evaluations"]
    )
    chronology_survives = all(
        row["asymmetric_packet_norm_divisibility"] for row in decisive_rows
    )
    symmetry_pass = all(
        row["cyclic_rotation_invariant"]
        and row["reversal_equality_control"]
        and row["reversal_quotiented"] is False
        for row in symmetry_rows
    )

    output = {
        "material_passport": {
            "id": "HCS-C23-ADELIC-LEFSCHETZ-FIRST-GATE-V1",
            "type": "exact_finite_flat_theorem_and_modular_ramification_pilot",
            "version": "1.0.0",
            "status": "VERIFIED_BY_PRODUCER_PENDING_INDEPENDENT_CHECK",
            "determinism": "exact modular arithmetic; no random seed",
            "lineage": "HCS-C22G analytic denominator cancellation -> C23 arithmetic denominator ramification",
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
            "integer_overflow_bound": "all modular dense products use n<=256 and p<=43 in this release",
        },
        "canonical_object": {
            "base_ring": "R=Z[1/(2*5*59*61)]",
            "fixed_algebra": "A_w=R[x_0,...,x_(n-1)]/(a_i*x_i^2+x_(i-1)+x_(i+1)-1)",
            "basis": "square-free monomials product x_i^(epsilon_i), epsilon_i in {0,1}",
            "finite_free_rank": "2^n",
            "monodromy": "M_w=J_(n-1)...J_0, J_i=[[-2*a_i*x_i,-1],[1,0]]",
            "lefschetz_element": "L_(w,r)=det(I-M_w^r)=2-2*T_r(trace(M_w)/2)",
            "packet_norm": "Delta_(w,r)=Norm_(A_w/R)(L_(w,r))",
            "multiplier_package": "P_w(X)=Norm_(A_w/R)(X^2-t_w*X+1)",
            "cyclic_resultant_identity": "Delta_(w,r)=Res_X(P_w(X),X^r-1)",
            "prime_event": "ell divides Delta iff L is a nonunit in A_w tensor F_ell iff a geometric fixed point has an r-return multiplier 1",
            "compactification_choice": "none",
        },
        "clock_and_chronology": {
            "clock": "one Hénon letter",
            "composition": "F_w=H_(w[n-1]) composed through H_(w[0])",
            "parameter_zero": "59/10",
            "parameter_one": "61/10",
            "cyclic_rotations": "conjugacy invariance checked",
            "reversal": "equality metadata retained; not quotiented",
            "averaging_used": False,
        },
        "protocol": {
            "prime_scan_bound": args.prime_bound,
            "degree_bad_primes_excluded": sorted(BAD_PRIMES),
            "max_repetition_selected_primes": args.max_repetition,
            "full_registered_gate": "primitive necklaces n<=10, repetitions r<=12, degree-good primes<=251",
            "this_release_scope": "mandatory C22 chronology pairs; r=1 scan through the stated bound; r<=max_repetition at decisive primes",
            "target_zeros_or_prime_fitting_used": False,
        },
        "chronology_pair_controls": pair_metadata,
        "r1_prime_scan": scan_rows,
        "decisive_packet_norm_rows": decisive_rows,
        "selected_repetition_fingerprints": repetition_rows,
        "cyclic_and_reversal_controls": symmetry_rows,
        "decisions": {
            "canonical_finite_flat_object_pass": True,
            "quotient_relations_pass": all_relations,
            "chronology_survives_galois_packet_norm_first_gate": chronology_survives,
            "period7_same_bigram_distinguished": decisive_rows[0][
                "asymmetric_packet_norm_divisibility"
            ],
            "period8_same_trigram_distinguished": decisive_rows[1][
                "asymmetric_packet_norm_divisibility"
            ],
            "cyclic_rotation_and_reversal_controls_pass": symmetry_pass,
            "strong_divisibility_zsigmondy_tower_pass": False,
            "strong_divisibility_zsigmondy_tower_status": "FIXED_WORD_TOWER_IS_CLASSICAL_CYCLIC_RESULTANT_BASELINE; CROSS_WORD_LAW_OPEN",
            "fixed_word_cyclic_resultant_baseline": True,
            "novel_cross_word_cross_period_law_found": False,
            "euler_product_authorized": False,
            "candidate_status": "CLOSED_AT_CYCLIC_RESULTANT_BASELINE",
            "next_gate": "CHANGE_DYNAMICAL_FORM_UNLESS_AN_EXPLICIT_CROSS_WORD_THEOREM_IS_PROPOSED",
            "all_release_checks_pass": all_relations
            and chronology_survives
            and symmetry_pass,
        },
        "claim_boundary": [
            "A distinguishing prime event proves chronology survives packet norm; it does not prove a cross-period Zsigmondy law.",
            "Multiplication-kernel dimension modulo ell is not identified with the ell-adic valuation of the integral norm.",
            "The divisor-closed repetition event is an expected single-multiplier cyclotomic control, not novelty evidence.",
            "For fixed w, the complete repetition tower is the cyclic-resultant sequence Res_X(P_w(X),X^r-1), so it is a classical baseline rather than a paper claim.",
            "No such cross-word law is presently frozen, so the unrestricted ledger is cancelled and C23 closes at the arithmetic chronology certificate.",
            "A successor may reopen this object only by first stating a falsifiable cross-word, cross-period theorem that matched reciprocal-polynomial controls cannot force.",
            "No Euler product, Riemann divisor, functional equation, or Hilbert-Polya operator is claimed.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(f"sha256 {sha256(args.output)}")


if __name__ == "__main__":
    main()
