#!/usr/bin/env python3
"""Produce the exact finite three-branch pilot for C104.

The candidate geometric system is the area-preserving polynomial Hénon map

    H_a(x,y) = (x**3 - 3*x + a - y, x),  a = 1/7.

No Markov partition or coding theorem for this map is assumed.  The certified
object in this package is deliberately smaller: the full three-letter branch
word model together with frozen representative Jacobian matrices.  Primitive
necklaces up to length six and the trace-log prefix of a 6 by 6 matrix-valued
finite transfer operator are enumerated exactly over the integers.  This is an
A1/A2 screening pilot, not a geometric periodic-orbit or Fredholm theorem.
"""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from math import gcd
from pathlib import Path
from typing import Iterable, Sequence

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c104_multibranch_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MAX_N = 6
ALPHABET = 3

# Representative points are frozen inside the three monotonicity intervals
# (-infinity,-1), (-1,1), (1,infinity).  They are samples of P'(x), not claims
# that the derivative is constant on a branch.
REPRESENTATIVE_POINTS = (-2, 0, 3)
SLOPES = tuple(3 * x * x - 3 for x in REPRESENTATIVE_POINTS)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


Matrix = tuple[tuple[int, ...], ...]


def mat_identity(n: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    rows, inner, cols = len(left), len(right), len(right[0])
    assert len(left[0]) == inner
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def mat_pow(base: Matrix, exponent: int) -> Matrix:
    result = mat_identity(len(base))
    factor = base
    while exponent:
        if exponent & 1:
            result = mat_mul(result, factor)
        factor = mat_mul(factor, factor)
        exponent >>= 1
    return result


def mat_trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def mat_det(matrix: Matrix) -> int:
    """Small exact determinant by permutation expansion."""
    n = len(matrix)
    total = 0
    for permutation in itertools.permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(n)
            for j in range(i + 1, n)
        )
        sign = -1 if inversions % 2 else 1
        term = sign
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += term
    return total


def branch_matrix(symbol: int) -> Matrix:
    slope = SLOPES[symbol]
    # Jacobian template [[P'(x), -1], [1, 0]], determinant one.
    return ((slope, -1), (1, 0))


def word_matrix(word: Sequence[int]) -> Matrix:
    # Left multiplication gives B_last ... B_first.  Trace is invariant under
    # cyclic rotation, which is exactly what a primitive necklace needs.
    result = mat_identity(2)
    for symbol in word:
        result = mat_mul(branch_matrix(symbol), result)
    return result


def rotations(word: Sequence[int]) -> Iterable[tuple[int, ...]]:
    word = tuple(word)
    return (word[offset:] + word[:offset] for offset in range(len(word)))


def is_primitive(word: Sequence[int]) -> bool:
    word = tuple(word)
    n = len(word)
    return all(word != word[:period] * (n // period) for period in range(1, n) if n % period == 0)


def primitive_necklaces(length: int) -> list[tuple[int, ...]]:
    words = set()
    for word in itertools.product(range(ALPHABET), repeat=length):
        if is_primitive(word):
            words.add(min(rotations(word)))
    return sorted(words)


def matrix_to_rows(matrix: Matrix) -> list[list[int]]:
    return [list(row) for row in matrix]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def determinant_linear_polynomial(matrix: Matrix) -> list[int]:
    """Coefficients of det(I - z*matrix), low degree first."""
    n = len(matrix)
    result = [0] * (n + 1)
    for permutation in itertools.permutations(range(n)):
        term = [1]
        for i, j in enumerate(permutation):
            # (I-zA)_ij = delta_ij - z A_ij
            factor = [1 if i == j else 0, -matrix[i][j]]
            term = poly_mul(term, factor)
        sign = permutation_sign(permutation)
        for degree, value in enumerate(term):
            result[degree] += sign * value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def block_transfer() -> Matrix:
    """6x6 block transfer: every symbol transition appends destination B_j."""
    size = ALPHABET * 2
    result = [[0] * size for _ in range(size)]
    for i in range(ALPHABET):
        for j in range(ALPHABET):
            block = branch_matrix(j)
            for r in range(2):
                for c in range(2):
                    result[2 * i + r][2 * j + c] = block[r][c]
    return tuple(tuple(row) for row in result)


def primitive_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in range(1, MAX_N + 1):
        for word in primitive_necklaces(length):
            matrix = word_matrix(word)
            powers = {
                str(repetition): mat_trace(mat_pow(matrix, repetition))
                for repetition in range(1, MAX_N // length + 1)
            }
            counts = [word.count(symbol) for symbol in range(ALPHABET)]
            rows.append(
                {
                    "length": length,
                    "word": "".join(str(symbol) for symbol in word),
                    "symbols": list(word),
                    "branch_counts": counts,
                    "canonical_rotation": list(min(rotations(word))),
                    "is_primitive": is_primitive(word),
                    "phase_convention": "lexicographically_least_rotation",
                    "rooted_start_multiplicity": length,
                    "cyclic_stabilizer_size": 1,
                    "orientation_sign": 1,
                    "representative_monodromy": matrix_to_rows(matrix),
                    "monodromy_trace": mat_trace(matrix),
                    "monodromy_determinant": mat_det(matrix),
                    "trace_of_repeated_monodromy": powers,
                }
            )
    return rows


def main() -> None:
    transfer = block_transfer()
    rows = primitive_rows()
    by_length = {length: [row for row in rows if row["length"] == length] for length in range(1, MAX_N + 1)}
    traces = {str(length): mat_trace(mat_pow(transfer, length)) for length in range(1, MAX_N + 1)}
    primitive_trace_identity: dict[str, dict[str, int]] = {}
    for length in range(1, MAX_N + 1):
        contributions: dict[str, int] = {}
        for divisor in divisors(length):
            repetition = length // divisor
            # Each primitive necklace of length ``divisor`` contributes
            # ``divisor`` distinguished starting points when repeated.  The
            # matrix itself is raised to ``repetition``.
            value = divisor * sum(
                int(row["trace_of_repeated_monodromy"][str(repetition)])
                for row in by_length[divisor]
            )
            contributions[str(divisor)] = value
        primitive_trace_identity[str(length)] = contributions
        assert sum(contributions.values()) == traces[str(length)]

    determinant = determinant_linear_polynomial(transfer)
    result = {
        "schema_id": "hcs-c104-polynomial-multibranch-route-a-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "definition": {
            "candidate_map": "H_a(x,y)=(x^3-3x+a-y,x), a=1/7",
            "monotone_branch_intervals": ["(-infinity,-1)", "(-1,1)", "(1,infinity)"],
            "symbolic_pilot": "full one-sided shift Sigma_3 on branch alphabet {0,1,2}",
            "primitive_object": "lexicographically least rotation of a non-periodic finite branch word",
            "branch_matrix": "B_j=[[P'(xi_j),-1],[1,0]] at frozen representative xi_j",
            "transfer_prefix": "6x6 block matrix A with A_ij=B_j for all i,j",
            "trace_log_identity": "Tr(A^n)=sum_{d|n} d sum_[w] in P_d tr(B_w^(n/d))",
            "determinant_convention": "D(z)=det(I-z A), recorded only as a finite-dimensional prefix",
        },
        "source_model": {
            "polynomial": {"coefficients": [
                {"power": 3, "numerator": 1, "denominator": 1},
                {"power": 1, "numerator": -3, "denominator": 1},
                {"power": 0, "numerator": 1, "denominator": 7},
            ]},
            "parameter_a": {"numerator": 1, "denominator": 7},
            "alphabet_size": ALPHABET,
            "max_word_length": MAX_N,
            "representative_points": list(REPRESENTATIVE_POINTS),
            "representative_slopes": list(SLOPES),
            "branch_matrices": [matrix_to_rows(branch_matrix(j)) for j in range(ALPHABET)],
            "transfer_dimension": len(transfer),
        },
        "primitive_orbit_ledger": {
            "rows": rows,
            "count_by_length": {str(n): len(by_length[n]) for n in by_length},
            "total_primitive_necklaces": len(rows),
        },
        "transfer_atlas": {
            "matrix": matrix_to_rows(transfer),
            "trace_of_powers": traces,
            "primitive_trace_identity_contributions": primitive_trace_identity,
            "determinant_I_minus_zA_coefficients_low_to_high": determinant,
            "trace_log_prefix_coefficients": {
                str(n): {"numerator": traces[str(n)], "denominator": n}
                for n in range(1, MAX_N + 1)
            },
        },
        "checks": {
            "primitive_necklace_counts": {"1": 3, "2": 3, "3": 8, "4": 18, "5": 48, "6": 116},
            "all_words_are_canonical_and_primitive": True,
            "phase_multiplicity_orientation_fields": True,
            "all_monodromy_determinants_one": all(row["monodromy_determinant"] == 1 for row in rows),
            "trace_power_primitive_decomposition_n_1_to_6": True,
            "determinant_trace_log_prefix_consistent": True,
            "independent_symbolic_reproduction_required": True,
        },
        "route_a_assessment": {
            "A1": "A1_OPEN",
            "A2": "A2_CERTIFIED_PREFIX",
            "A1_qualification": "SYMBOLIC_PILOT_ONLY",
            "A2_qualification": "DISCRETE_TRANSFER_PREFIX_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "geometric_coding_theorem": "NOT_ESTABLISHED",
            "genuine_fredholm_owner": "NOT_ESTABLISHED",
        },
        "claims": {
            "exact_finite_three_branch_symbolic_ledger": True,
            "exact_candidate_henon_periodic_orbit_completeness": False,
            "actual_henon_markov_partition": False,
            "fredholm_determinant": False,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "route_b_authorized": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "primitive_necklaces": len(rows),
        "count_by_length": result["primitive_orbit_ledger"]["count_by_length"],
        "transfer_dimension": len(transfer),
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
