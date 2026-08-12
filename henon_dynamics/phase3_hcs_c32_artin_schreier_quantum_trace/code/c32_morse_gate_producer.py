#!/usr/bin/env python3
"""Exact producer for the HCS-C32 Morse-local Hill-information gate.

Only Python's standard library is used.  Every dynamical and quadratic-form
calculation is exact over a prime field.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "HCS-C32-PHASE3-MORSE-GATE-1"
CANDIDATE_ID = "HCS-C32-MORSE-LOCAL-HILL-GATE"
PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
PERIODS = list(range(1, 6))

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[1]

SOURCE_PATHS = [
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/RESEARCH_QUESTION_BRIEF.md",
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/METHODOLOGY_BLUEPRINT.md",
    "henon_dynamics/phase1_hcs_c32_artin_schreier_quantum_trace/DEVILS_ADVOCATE_CHECKPOINT1.md",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SEARCH_STRATEGY.md",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_CORPUS_AND_ANNOTATED_BIBLIOGRAPHY.md",
    "henon_dynamics/phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_VERIFICATION_REPORT.md",
    "henon_dynamics/henon_frobenius_scheme_obstruction/DERIVATION_PACKAGE.md",
    "henon_dynamics/henon_frobenius_scheme_obstruction/results/c12a_certificate.json",
    "henon_dynamics/phase3_hcs_c32_artin_schreier_quantum_trace/EXACT_GATE_PROTOCOL.md",
]


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def matmul(a: list[list[int]], b: list[list[int]], p: int) -> list[list[int]]:
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(len(b))) % p
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def determinant_mod(a: list[list[int]], p: int) -> int:
    work = [[entry % p for entry in row] for row in a]
    det = 1
    n = len(work)
    for col in range(n):
        pivot = next(
            (row for row in range(col, n) if work[row][col] % p), None
        )
        if pivot is None:
            return 0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det = -det
        value = work[col][col] % p
        det = det * value % p
        inverse = pow(value, -1, p)
        for row in range(col + 1, n):
            coefficient = work[row][col] * inverse % p
            for j in range(col, n):
                work[row][j] = (
                    work[row][j] - coefficient * work[col][j]
                ) % p
    return det % p


def inverse_mod(a: list[list[int]], p: int) -> list[list[int]]:
    n = len(a)
    work = [
        [entry % p for entry in row] + identity(n)[i]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next(
            (row for row in range(col, n) if work[row][col] % p), None
        )
        if pivot is None:
            raise ValueError("singular matrix")
        work[col], work[pivot] = work[pivot], work[col]
        inverse = pow(work[col][col] % p, -1, p)
        work[col] = [(entry * inverse) % p for entry in work[col]]
        for row in range(n):
            if row == col:
                continue
            coefficient = work[row][col] % p
            work[row] = [
                (work[row][j] - coefficient * work[col][j]) % p
                for j in range(2 * n)
            ]
    return [row[n:] for row in work]


def quadratic_character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def least_square_root(value: int, p: int) -> int | None:
    value %= p
    return next((x for x in range(p) if x * x % p == value), None)


def rotate(word: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return word[shift:] + word[:shift]


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return sorted({rotate(word, shift) for shift in range(len(word))})


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def hessian_from_action(word: tuple[int, ...], p: int) -> list[list[int]]:
    n = len(word)
    hessian = [[0] * n for _ in range(n)]
    for i, value in enumerate(word):
        hessian[i][i] = (hessian[i][i] + 12 * value) % p
        j = (i + 1) % n
        # The action term x_i x_j contributes one derivative in each order.
        # This also gives the correct diagonal value 2 when n=1 and the
        # double mixed edge when n=2.
        hessian[i][j] = (hessian[i][j] + 1) % p
        hessian[j][i] = (hessian[j][i] + 1) % p
    return hessian


def action_value(word: tuple[int, ...], p: int) -> int:
    n = len(word)
    return sum(
        word[i] * word[(i + 1) % n] - word[i] + 2 * word[i] ** 3
        for i in range(n)
    ) % p


def critical_residuals(word: tuple[int, ...], p: int) -> list[int]:
    n = len(word)
    return [
        (word[(i - 1) % n] + word[(i + 1) % n] - 1 + 6 * word[i] ** 2)
        % p
        for i in range(n)
    ]


def derivative_factor(value: int, p: int) -> list[list[int]]:
    return [[(-12 * value) % p, (-1) % p], [1, 0]]


def monodromy(word: tuple[int, ...], p: int) -> list[list[int]]:
    product = identity(2)
    for value in word:
        product = matmul(derivative_factor(value, p), product, p)
    return product


def det_i_minus_2x2(matrix: list[list[int]], p: int) -> int:
    return (
        (1 - matrix[0][0]) * (1 - matrix[1][1])
        - matrix[0][1] * matrix[1][0]
    ) % p


def state_step(state: tuple[int, int], p: int) -> tuple[int, int]:
    q, previous = state
    return ((1 - 6 * q * q - previous) % p, q)


def least_state_period(state: tuple[int, int], p: int, limit: int) -> int | None:
    current = state
    for period in range(1, limit + 1):
        current = state_step(current, p)
        if current == state:
            return period
    return None


def word_from_state(state: tuple[int, int], n: int, p: int) -> tuple[int, ...]:
    current = state
    values: list[int] = []
    for _ in range(n):
        values.append(current[0])
        current = state_step(current, p)
    if current != state:
        raise ValueError("state is not periodic at requested length")
    return tuple(values)


def record_from_word(word: tuple[int, ...], p: int) -> dict[str, Any]:
    hessian = hessian_from_action(word, p)
    hessian_det = determinant_mod(hessian, p)
    derivative = monodromy(word, p)
    hill_det = det_i_minus_2x2(derivative, p)
    return {
        "q_word": list(word),
        "action": action_value(word, p),
        "critical_residuals": critical_residuals(word, p),
        "hessian_matrix": hessian,
        "hessian_det": hessian_det,
        "quadratic_character": quadratic_character(hessian_det, p),
        "monodromy_matrix": derivative,
        "monodromy_det": determinant_mod(derivative, p),
        "hill_det": hill_det,
        "hill_identity_rhs": ((-1) ** (len(word) + 1) * hill_det) % p,
    }


def primitive_records(p: int, n: int) -> list[dict[str, Any]]:
    records = []
    for q in range(p):
        for previous in range(p):
            state = (q, previous)
            if least_state_period(state, p, n) != n:
                continue
            word = word_from_state(state, n, p)
            record = record_from_word(word, p)
            record["state"] = [q, previous]
            record["canonical_word"] = list(canonical_rotation(word))
            records.append(record)
    return records


def all_fixed_state_count(p: int, n: int) -> int:
    count = 0
    for q in range(p):
        for previous in range(p):
            current = (q, previous)
            for _ in range(n):
                current = state_step(current, p)
            count += int(current == (q, previous))
    return count


def collision_classes(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[int, int], dict[tuple[int, ...], dict[str, Any]]] = {}
    for record in records:
        if record["hessian_det"] == 0:
            continue
        key = (record["action"], record["quadratic_character"])
        cycle = tuple(record["canonical_word"])
        grouped.setdefault(key, {})[cycle] = record
    output = []
    for key, cycles in sorted(grouped.items()):
        determinants = sorted({record["hessian_det"] for record in cycles.values()})
        if len(determinants) < 2:
            continue
        output.append(
            {
                "action": key[0],
                "quadratic_character": key[1],
                "cycle_count": len(cycles),
                "determinants": determinants,
                "canonical_words": [list(word) for word in sorted(cycles)],
            }
        )
    return output


def scan() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    first: dict[str, Any] | None = None
    for n in PERIODS:
        for p in PRIMES:
            records = primitive_records(p, n)
            collisions = collision_classes(records)
            row = {
                "p": p,
                "n": n,
                "all_fixed_states": all_fixed_state_count(p, n),
                "primitive_states": len(records),
                "primitive_morse_states": sum(
                    record["hessian_det"] != 0 for record in records
                ),
                "collision_groups": len(collisions),
            }
            rows.append(row)
            if collisions and first is None:
                first = {"p": p, "n": n, **collisions[0]}
    if first is None:
        raise RuntimeError("registered scan found no collision")
    return rows, first


def diagonalize_by_congruence(
    matrix: list[list[int]], p: int
) -> tuple[list[list[int]], list[list[int]]]:
    """Return D,P with P^T matrix P = D diagonal."""

    n = len(matrix)
    work = [[entry % p for entry in row] for row in matrix]
    transform = identity(n)

    def swap_columns(a: list[list[int]], i: int, j: int) -> None:
        for row in a:
            row[i], row[j] = row[j], row[i]

    for i in range(n):
        pivot = next((j for j in range(i, n) if work[j][j] % p), None)
        if pivot is None:
            pair = next(
                (
                    (j, k)
                    for j in range(i, n)
                    for k in range(j + 1, n)
                    if work[j][k] % p
                ),
                None,
            )
            if pair is None:
                raise ValueError("singular symmetric form")
            j, k = pair
            for row in range(n):
                work[row][j] = (work[row][j] + work[row][k]) % p
                transform[row][j] = (
                    transform[row][j] + transform[row][k]
                ) % p
            for col in range(n):
                work[j][col] = (work[j][col] + work[k][col]) % p
            pivot = j
        if pivot != i:
            swap_columns(work, i, pivot)
            work[i], work[pivot] = work[pivot], work[i]
            swap_columns(transform, i, pivot)
        inverse = pow(work[i][i] % p, -1, p)
        for j in range(i + 1, n):
            coefficient = work[i][j] * inverse % p
            for row in range(n):
                work[row][j] = (
                    work[row][j] - coefficient * work[row][i]
                ) % p
                transform[row][j] = (
                    transform[row][j] - coefficient * transform[row][i]
                ) % p
            for col in range(n):
                work[j][col] = (
                    work[j][col] - coefficient * work[i][col]
                ) % p
    return work, transform


def vector_matrix_product(
    matrix: list[list[int]], vector: list[int], p: int
) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % p for row in matrix]


def dot(left: list[int], right: list[int], p: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % p


def find_vector_of_norm(
    gram: list[list[int]], target: int, p: int
) -> list[int]:
    dimension = len(gram)
    for i in range(dimension):
        for x in range(1, p):
            vector = [0] * dimension
            vector[i] = x
            if dot(vector, vector_matrix_product(gram, vector, p), p) == target:
                return vector
    for i, j in combinations(range(dimension), 2):
        for x in range(p):
            for y in range(1, p):
                vector = [0] * dimension
                vector[i] = x
                vector[j] = y
                if (
                    dot(vector, vector_matrix_product(gram, vector, p), p)
                    == target
                ):
                    return vector
    raise ValueError("target norm was not represented in support at most two")


def congruence_between_diagonal_forms(
    gram: list[list[int]], targets: list[int], p: int
) -> list[list[int]]:
    dimension = len(gram)
    if dimension == 1:
        ratio = targets[0] * pow(gram[0][0], -1, p) % p
        root = least_square_root(ratio, p)
        if root is None or root == 0:
            raise ValueError("final one-dimensional forms are not congruent")
        return [[root]]

    vector = find_vector_of_norm(gram, targets[0], p)
    linear = vector_matrix_product(gram, vector, p)
    pivot = next(i for i, value in enumerate(linear) if value)
    pivot_inverse = pow(linear[pivot], -1, p)
    complement_columns = []
    for j in range(dimension):
        if j == pivot:
            continue
        column = [0] * dimension
        column[j] = 1
        column[pivot] = -linear[j] * pivot_inverse % p
        complement_columns.append(column)
    complement = [
        [complement_columns[j][i] for j in range(dimension - 1)]
        for i in range(dimension)
    ]
    restricted = matmul(
        matmul(transpose(complement), gram, p), complement, p
    )
    tail_coordinates = congruence_between_diagonal_forms(
        restricted, targets[1:], p
    )
    tail = matmul(complement, tail_coordinates, p)
    return [[vector[i]] + tail[i] for i in range(dimension)]


def congruence_witness(
    first: list[list[int]], second: list[list[int]], p: int
) -> list[list[int]]:
    diagonal_first, basis_first = diagonalize_by_congruence(first, p)
    diagonal_second, basis_second = diagonalize_by_congruence(second, p)
    targets = [diagonal_second[i][i] for i in range(len(second))]
    bridge = congruence_between_diagonal_forms(diagonal_first, targets, p)
    witness = matmul(
        matmul(basis_first, bridge, p), inverse_mod(basis_second, p), p
    )
    if matmul(matmul(transpose(witness), first, p), witness, p) != second:
        raise AssertionError("constructed congruence failed")
    return witness


def source_lock() -> list[dict[str, str]]:
    return [
        {"path": path, "sha256": sha256_file(REPO / path)}
        for path in SOURCE_PATHS
    ]


def build_payload() -> dict[str, Any]:
    rows, first = scan()
    if (first["n"], first["p"]) != (5, 61):
        raise AssertionError("post-pilot first-collision sentinel changed")
    canonical_words = [tuple(word) for word in first["canonical_words"]]
    if len(canonical_words) != 2:
        raise AssertionError("selected collision must contain exactly two cycles")
    orbit_records = [record_from_word(word, first["p"]) for word in canonical_words]
    for record in orbit_records:
        record["canonical_rotation"] = True
        record["primitive_state_period"] = first["n"]
        record["rotations"] = [list(word) for word in rotations(tuple(record["q_word"]))]
    hessian_a = orbit_records[0]["hessian_matrix"]
    hessian_b = orbit_records[1]["hessian_matrix"]
    congruence = congruence_witness(hessian_a, hessian_b, first["p"])
    det_a = orbit_records[0]["hessian_det"]
    det_b = orbit_records[1]["hessian_det"]
    ratio = det_a * pow(det_b, -1, first["p"]) % first["p"]
    square_root = least_square_root(ratio, first["p"])
    if square_root is None:
        raise AssertionError("collision determinant ratio is not a square")

    return {
        "material_passport": {
            "candidate_id": CANDIDATE_ID,
            "phase": 3,
            "artifact_kind": "exact_experiment_certificate",
            "evidence_status": "THEOREM_PLUS_EXACT_FINITE_FIELD_CERTIFICATE",
            "ai_assistance": True,
            "post_pilot_disclosure": "p=61,n=5 witness was discovered before protocol freeze and is not a preregistered prediction",
        },
        "source_lock": source_lock(),
        "conventions": {
            "map": "H6(q,p)=(1-6*q^2-p,q)",
            "action": "Phi_n=sum_i(x_i*x_(i+1)-x_i+2*x_i^3)",
            "chronology": "DH^n=A(x_(n-1))*...*A(x_0), later factors on the left",
            "hessian": "derived term-by-term; n=1 diagonal and n=2 double mixed edge preserved",
            "hill_identity": "det Hess(Phi_n)=(-1)^(n+1)*det(I-DH6^n)",
            "local_fourier_shift": "shifted Fourier-Deligne trace is -E; raw unshifted Fourier integral trace is E",
        },
        "theorem_bridge": {
            "formal_morse": {
                "source": "Deligne and Katz, SGA 7 II, Expose XV",
                "locator": "Theorem 1.2.6 and Corollary 1.3.2, journal pages 168-176",
                "hypotheses": "residue characteristic not 2 and isolated nondegenerate critical point",
                "conclusion": "the henselian germ is equivalent over the residue field to its nondegenerate quadratic model",
            },
            "quadratic_vanishing_cycles": {
                "source": "Fu, A Thom-Sebastiani Theorem in Characteristic p (2014)",
                "locator": "Example 2.3 and Corollary 2.4, published pages 104-105",
                "conclusion": "the vanishing-cycle representation of a nondegenerate quadratic germ is rank one and determined by the quadratic form through Kummer/Gauss data",
            },
            "local_fourier": {
                "source": "Laumon, Transformation de Fourier (1987)",
                "locator": "Definition 2.4.2.3, Theorem 2.4.3, and Proposition 2.5.3.1, pages 162-166",
                "conclusion": "local Fourier transform sends the quadratic Kummer character to its Gauss representation, with the stated shift conventions",
            },
            "application": "equal critical value plus the explicit F_61 Hessian congruence gives isomorphic henselian function germs and hence isomorphic Morse-local vanishing-cycle Frobenius representations",
            "infinity_boundary": "local stationary phase does not identify or eliminate the contribution at infinity of the global Fourier transform",
        },
        "registered_scan": {
            "ordering": "n_then_p_ascending",
            "primes": PRIMES,
            "periods": PERIODS,
            "rows": rows,
            "first_collision": first,
        },
        "witness": {
            "p": first["p"],
            "n": first["n"],
            "common_action": first["action"],
            "common_quadratic_character": first["quadratic_character"],
            "orbit_classes": orbit_records,
            "determinant_square_ratio": {
                "first_over_second": ratio,
                "least_square_root": square_root,
                "square_check": square_root * square_root % first["p"],
            },
            "quadratic_congruence": {
                "direction": "C^T*H_first*C=H_second mod p",
                "matrix": congruence,
                "matrix_det": determinant_mod(congruence, first["p"]),
                "verified": True,
            },
            "local_trace_equivalence": {
                "quadratic_sum_formula": "psi(t*c)*chi(t)^n*chi(det(H))*chi(2)^(-n)*G(psi)^n",
                "same_for_every_nonzero_t": True,
                "reason": "same c,n and discriminant square class; explicit Hessian congruence gives a finite-field bijection of quadratic models",
                "full_hill_values_distinguished": sorted(
                    {record["hill_det"] for record in orbit_records}
                ),
                "henselian_germs_isomorphic": True,
                "morse_local_vanishing_cycle_representations_isomorphic": True,
            },
        },
        "decisions": {
            "good_prime_morse_local_hill_information_gate": "STOP_THEOREM_EXACT_COLLISION",
            "computational_collision": "PROVED_EXACT",
            "global_artin_schreier_cohomology_no_go": False,
            "degenerate_or_bad_prime_no_go": False,
            "hilbert_polya_structure": "NOT_ESTABLISHED",
            "route_a_formal_status": "NOT_TESTABLE",
            "route_b_authorized": False,
        },
        "scope": {
            "proved_by_computation": "two primitive H6 period-5 classes over F_61 have identical Morse-local quadratic data and unequal Hill determinants",
            "requires_primary_theorem": "formal/etale Morse lemma and l-adic stationary phase identify the vanishing-cycle local representation with the quadratic model",
            "not_claimed": [
                "no global cohomological information",
                "no statement at degenerate critical points",
                "no statement at bad primes or at infinity",
                "no canonical global determinant or Hilbert-Polya operator",
            ],
        },
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": CANDIDATE_ID,
        "producer_status": "PRODUCER_ONLY_UNVERIFIED_UNTIL_INDEPENDENT_CHECKER",
        "payload": payload,
        "payload_sha256": sha256_bytes(canonical_bytes(payload)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    text = json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
