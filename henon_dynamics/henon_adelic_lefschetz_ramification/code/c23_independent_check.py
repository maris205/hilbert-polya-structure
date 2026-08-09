#!/usr/bin/env python3
"""Independent checker for the first HCS-C23 arithmetic gate.

This file does not import the producer.  It reconstructs the four decisive
quotient algebras and uses SymPy's finite-field DomainMatrix rank rather than
the producer's custom modular Gauss--Jordan routine.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c23_first_gate_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c23_first_gate_independent_check.json"
PARAMETERS = {"0": 59, "1": 61}
PAIR7 = ("0000101", "0001001")
PAIR8 = ("00101011", "00101101")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cyclic_counts(word: str, width: int) -> dict[str, int]:
    counts: dict[str, int] = {}
    wrapped = word + word[: width - 1]
    for index in range(len(word)):
        gram = wrapped[index : index + width]
        counts[gram] = counts.get(gram, 0) + 1
    return dict(sorted(counts.items()))


def rotations(word: str) -> list[str]:
    return [word[index:] + word[:index] for index in range(len(word))]


def non_dihedral_pair(pair: tuple[str, str]) -> bool:
    first, second = pair
    return second not in rotations(first) and second not in rotations(first[::-1])


def trace_multiplication_matrix(word: str, prime: int) -> np.ndarray:
    """Reconstruct multiplication by tr(J_(n-1)...J_0)."""

    n, dimension = len(word), 1 << len(word)
    inverse_ten = pow(10, -1, prime)
    parameters = [PARAMETERS[letter] * inverse_ten % prime for letter in word]

    @lru_cache(None)
    def normal_form(exponents: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
        for index, exponent in enumerate(exponents):
            if exponent <= 1:
                continue
            base = list(exponents)
            base[index] -= 2
            inverse = pow(parameters[index], -1, prime)
            total: dict[int, int] = {}
            for sign, neighbor in (
                (1, None),
                (-1, (index - 1) % n),
                (-1, (index + 1) % n),
            ):
                child = base.copy()
                if neighbor is not None:
                    child[neighbor] += 1
                for mask, coefficient in normal_form(tuple(child)):
                    total[mask] = (
                        total.get(mask, 0) + sign * inverse * coefficient
                    ) % prime
            return tuple(sorted((mask, value) for mask, value in total.items() if value))
        mask = sum(1 << index for index, exponent in enumerate(exponents) if exponent)
        return ((mask, 1),)

    transitions = []
    for variable in range(n):
        columns = []
        for mask in range(dimension):
            exponents = [(mask >> index) & 1 for index in range(n)]
            exponents[variable] += 1
            columns.append(normal_form(tuple(exponents)))
        transitions.append(columns)

    def times_x(vector: np.ndarray, variable: int) -> np.ndarray:
        output = np.zeros(dimension, dtype=np.int64)
        for source in np.flatnonzero(vector):
            for target, coefficient in transitions[variable][int(source)]:
                output[target] = (
                    output[target] + int(vector[source]) * coefficient
                ) % prime
        return output

    zero = np.zeros(dimension, dtype=np.int64)
    one = zero.copy()
    one[0] = 1
    a00, a01, a10, a11 = one, zero.copy(), zero.copy(), one.copy()
    for index, parameter in enumerate(parameters):
        b00 = (-2 * parameter * times_x(a00, index) - a10) % prime
        b01 = (-2 * parameter * times_x(a01, index) - a11) % prime
        a00, a01, a10, a11 = b00, b01, a00, a01
    trace = (a00 + a11) % prime

    matrix = np.empty((dimension, dimension), dtype=np.int64)
    for mask in range(dimension):
        product = trace.copy()
        for variable in range(n):
            if (mask >> variable) & 1:
                product = times_x(product, variable)
        matrix[:, mask] = product
    return matrix % prime


def domain_nullity(matrix: np.ndarray, prime: int) -> int:
    lefschetz = (
        2 * np.eye(matrix.shape[0], dtype=np.int64) - matrix
    ) % prime
    domain = DomainMatrix.from_list(lefschetz.tolist(), sp.GF(prime))
    return matrix.shape[0] - domain.rank()


def direct_degenerate_points(word: str, prime: int) -> list[dict[str, object]]:
    inverse_ten = pow(10, -1, prime)
    parameters = [PARAMETERS[letter] * inverse_ten % prime for letter in word]
    result = []
    for q_initial in range(prime):
        for p_initial in range(prime):
            q, previous = q_initial, p_initial
            m00, m01, m10, m11 = 1, 0, 0, 1
            for parameter in parameters:
                j00, j01 = -2 * parameter * q % prime, -1 % prime
                m00, m01, m10, m11 = (
                    (j00 * m00 + j01 * m10) % prime,
                    (j00 * m01 + j01 * m11) % prime,
                    m00,
                    m01,
                )
                q, previous = (
                    (1 - parameter * q * q - previous) % prime,
                    q,
                )
            determinant = (
                (1 - m00) * (1 - m11) - m01 * m10
            ) % prime
            if (q, previous) == (q_initial, p_initial) and determinant == 0:
                result.append(
                    {
                        "q": q_initial,
                        "p": p_initial,
                        "trace": (m00 + m11) % prime,
                        "det_I_minus_M": determinant,
                        "monodromy": [[m00, m01], [m10, m11]],
                    }
                )
    return result


def structural_audit(certificate: dict[str, object]) -> dict[str, bool]:
    canonical = certificate.get("canonical_object", {})
    chronology = certificate.get("clock_and_chronology", {})
    controls = certificate.get("chronology_pair_controls", [])
    decisive = certificate.get("decisive_packet_norm_rows", [])
    symmetry = certificate.get("cyclic_and_reversal_controls", [])
    decisions = certificate.get("decisions", {})
    claim_boundary = certificate.get("claim_boundary", [])

    pair_rows = {row.get("id"): row for row in controls}
    decisive_rows = {row.get("pair"): row for row in decisive}
    expected_kernel = {
        "n7": ([1, 0], 11),
        "n8": ([0, 1], 3),
    }
    decisive_exact = set(decisive_rows) == {"n7", "n8"}
    if decisive_exact:
        for pair, (kernel, prime) in expected_kernel.items():
            row = decisive_rows[pair]
            decisive_exact &= row.get("prime") == prime
            decisive_exact &= [
                item.get("r1_multiplication_kernel_dimension")
                for item in row.get("evaluations", [])
            ] == kernel
            decisive_exact &= row.get("asymmetric_packet_norm_divisibility") is True

    return {
        "canonical_object": canonical.get("base_ring") == "R=Z[1/(2*5*59*61)]"
        and canonical.get("finite_free_rank") == "2^n"
        and canonical.get("compactification_choice") == "none"
        and canonical.get("multiplier_package")
        == "P_w(X)=Norm_(A_w/R)(X^2-t_w*X+1)"
        and canonical.get("cyclic_resultant_identity")
        == "Delta_(w,r)=Res_X(P_w(X),X^r-1)",
        "chronology_frozen": chronology.get("composition")
        == "F_w=H_(w[n-1]) composed through H_(w[0])"
        and chronology.get("averaging_used") is False
        and chronology.get("reversal") == "equality metadata retained; not quotiented",
        "pair_controls": pair_rows.get("C22_PERIOD7_SAME_BIGRAM", {}).get("words")
        == list(PAIR7)
        and pair_rows.get("C22_PERIOD7_SAME_BIGRAM", {}).get("matched") is True
        and pair_rows.get("C22_PERIOD7_SAME_BIGRAM", {}).get("non_dihedral_pair")
        is True
        and non_dihedral_pair(PAIR7)
        and pair_rows.get("C22_PERIOD8_SAME_TRIGRAM", {}).get("words")
        == list(PAIR8)
        and pair_rows.get("C22_PERIOD8_SAME_TRIGRAM", {}).get("matched") is True
        and pair_rows.get("C22_PERIOD8_SAME_TRIGRAM", {}).get("non_dihedral_pair")
        is True
        and non_dihedral_pair(PAIR8),
        "decisive_rows": decisive_exact,
        "symmetry_scope": bool(symmetry)
        and all(
            row.get("cyclic_rotation_invariant") is True
            and row.get("reversal_equality_control") is True
            and row.get("reversal_quotiented") is False
            for row in symmetry
        ),
        "decision_scope": decisions.get(
            "chronology_survives_galois_packet_norm_first_gate"
        )
        is True
        and decisions.get("strong_divisibility_zsigmondy_tower_pass") is False
        and decisions.get("fixed_word_cyclic_resultant_baseline") is True
        and decisions.get("novel_cross_word_cross_period_law_found") is False
        and decisions.get("euler_product_authorized") is False
        and decisions.get("candidate_status")
        == "CLOSED_AT_CYCLIC_RESULTANT_BASELINE"
        and decisions.get("next_gate")
        == "CHANGE_DYNAMICAL_FORM_UNLESS_AN_EXPLICIT_CROSS_WORD_THEOREM_IS_PROPOSED",
        "no_valuation_overclaim": any(
            "not identified with the ell-adic valuation" in text
            for text in claim_boundary
        ),
        "cyclic_resultant_novelty_boundary": any(
            "complete repetition tower is the cyclic-resultant sequence" in text
            for text in claim_boundary
        )
        and any(
            "matched reciprocal-polynomial controls" in text
            for text in claim_boundary
        ),
    }


def independent_recompute() -> dict[str, bool]:
    specs = [
        (PAIR7[0], 11, 1, [{"q": 8, "p": 6, "trace": 2, "det_I_minus_M": 0, "monodromy": [[1, 10], [0, 1]]}]),
        (PAIR7[1], 11, 0, []),
        (PAIR8[0], 3, 0, []),
        (PAIR8[1], 3, 1, [{"q": 1, "p": 1, "trace": 2, "det_I_minus_M": 0, "monodromy": [[0, 1], [2, 2]]}]),
    ]
    nullity_pass = True
    witness_pass = True
    for word, prime, expected_nullity, expected_points in specs:
        matrix = trace_multiplication_matrix(word, prime)
        nullity_pass &= domain_nullity(matrix, prime) == expected_nullity
        witness_pass &= direct_degenerate_points(word, prime) == expected_points
    return {
        "domainmatrix_nullities": nullity_pass,
        "direct_rational_witnesses": witness_pass,
        "period7_bigram_identity": cyclic_counts(PAIR7[0], 2)
        == cyclic_counts(PAIR7[1], 2),
        "period8_trigram_identity": cyclic_counts(PAIR8[0], 3)
        == cyclic_counts(PAIR8[1], 3),
    }


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    checks = structural_audit(certificate)
    checks.update(independent_recompute())
    output = {
        "material_passport": {
            "id": "HCS-C23-FIRST-GATE-INDEPENDENT-CHECK-V1",
            "type": "nonimporting_quotient_algebra_and_direct_orbit_checker",
            "determinism": "exact modular arithmetic; no random seed",
            "independent_linear_algebra": "SymPy DomainMatrix over GF(p)",
        },
        "certificate": str(args.certificate),
        "certificate_sha256": sha256(args.certificate),
        "checks": checks,
        "all_checks_pass": all(checks.values()),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["all_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
