#!/usr/bin/env python3
"""Produce the exact HCS-C26 AGY point-evaluation-slice certificate.

This program verifies one source-locked application witness.  It does not
reprove the C24 discrete-metaplectic-atom theorem, the C25 all-length Rauzy
decoder theorem, or boundedness on any proposed holomorphic function space.

The chronological convention is

    B_e = I + E_(loser,winner),
    B_(e_1...e_n) = B_(e_n) ... B_(e_1),
    R_gamma = B_gamma^T.

For the frozen AGY branch gamma_star and exact simplex point x0, the program
computes

    S_gamma(x0) = 1^T R_gamma x0,
    J_gamma(x0) = S_gamma(x0)^(-4),
    |w_(sigma+it,gamma)(x0)| = S_gamma(x0)^(-(sigma+4)).

Together with explicitly listed external theorems and candidate-space
assumptions, this is the machine-checkable input for the point-evaluation
slice lower bound.  The optional finite decoder replay is only a regression
sentinel and is never promoted to an all-length proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp
import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c26_certificate.json"

ALPHABET = (1, 2, 3, 4)
MOVE_TYPES = ("t", "b")
INITIAL = ((1, 2, 3, 4), (4, 3, 2, 1))
AGY_BASE = ((1, 3, 4, 2), (4, 3, 2, 1))
ETA = "tbttbtbb"
GAMMA_STAR = "t" * 64 + ETA * 8
RETURN_BRIDGE = ETA[1:]
SECOND_RETURN_BRANCH = GAMMA_STAR + RETURN_BRIDGE + GAMMA_STAR
TWO_RETURN_WORD = GAMMA_STAR + SECOND_RETURN_BRANCH
THIRD_RETURN_BRIDGE = "bbb"
THIRD_RETURN_BRANCH = GAMMA_STAR + THIRD_RETURN_BRIDGE + GAMMA_STAR
THREE_RETURN_WORD = GAMMA_STAR + SECOND_RETURN_BRANCH + THIRD_RETURN_BRANCH
REVERSED_THREE_RETURN_WORD = THIRD_RETURN_BRANCH + SECOND_RETURN_BRANCH + GAMMA_STAR
IDENTITY = tuple(tuple(int(row == column) for column in range(4)) for row in range(4))

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
IntMatrix = tuple[tuple[int, ...], ...]


REQUIRED_SLICE_HYPOTHESES = {
    "H1_LITERAL_TRANSFER": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H2_BOUNDED_CONSTANT_EMBEDDING": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H3_BOUNDED_POINT_EVALUATION": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H4_ABSOLUTE_POINTWISE_BRANCH_SUM": "EXTERNAL_C25_THEOREM_NOT_REPROVED",
    "H5_PROJECTED_BRANCH_INJECTIVITY": "EXTERNAL_C25_THEOREM_NOT_REPROVED",
    "H6_PATHWISE_UNITARY_LIFTS": "EXTERNAL_C25_INPUT_NOT_REPROVED",
    "H7_DISCRETE_ATOM_ESSENTIAL_NORM": "EXTERNAL_C24_THEOREM_NOT_REPROVED",
    "H8_NONZERO_GAMMA_STAR_COEFFICIENT": "EXACT_WITNESS_VERIFIED_HERE",
}

REQUIRED_SCOPE_FLAGS = {
    "c24_atomic_theorem_reproved": False,
    "c25_all_length_decoder_reproved": False,
    "finite_sentinel_is_proof": False,
    "finite_sentinel_is_branch_completeness_claim": False,
    "projected_matrix_collisions_ignored": False,
    "central_signs_averaged": False,
    "branch_chronology_averaged": False,
    "oscillator_truncated": False,
    "heat_regularizer_inserted": False,
    "candidate_holomorphic_space_boundedness_claimed_by_code": False,
    "ordinary_trace_of_isolated_unitary_claimed": False,
    "common_complex_domain_claimed_from_numerical_sampling": False,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sentinel-max-length", type=int, default=20)
    return parser.parse_args()


def matrix_json(matrix: IntMatrix | sp.Matrix) -> list[list[int]]:
    if isinstance(matrix, sp.MatrixBase):
        return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]
    return [list(row) for row in matrix]


def permutation_json(permutation: Permutation) -> dict[str, list[int]]:
    return {"top": list(permutation[0]), "bottom": list(permutation[1])}


def transpose(matrix: IntMatrix) -> IntMatrix:
    return tuple(tuple(matrix[column][row] for column in range(4)) for row in range(4))


def matmul(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(4)) for column in range(4))
        for row in range(4)
    )


def matrix_sum(matrix: IntMatrix) -> int:
    return sum(sum(row) for row in matrix)


def matrix_flat(matrix: IntMatrix) -> tuple[int, ...]:
    return tuple(value for row in matrix for value in row)


def determinant(matrix: IntMatrix) -> int:
    return int(sp.Matrix(matrix).det())


def elementary_matrix(winner: int, loser: int) -> IntMatrix:
    rows = [list(row) for row in IDENTITY]
    rows[loser - 1][winner - 1] += 1
    return tuple(tuple(row) for row in rows)


def crossing_form(permutation: Permutation) -> sp.Matrix:
    top, bottom = permutation
    top_position = {letter: index for index, letter in enumerate(top)}
    bottom_position = {letter: index for index, letter in enumerate(bottom)}
    result = sp.zeros(4)
    for alpha in ALPHABET:
        for beta in ALPHABET:
            if top_position[alpha] < top_position[beta] and bottom_position[alpha] > bottom_position[beta]:
                result[alpha - 1, beta - 1] = 1
            elif top_position[alpha] > top_position[beta] and bottom_position[alpha] < bottom_position[beta]:
                result[alpha - 1, beta - 1] = -1
    return result


def rauzy_move(permutation: Permutation, move_type: str) -> tuple[Permutation, int, int, IntMatrix]:
    top, bottom = [list(row) for row in permutation]
    if move_type == "t":
        winner, loser = top[-1], bottom[-1]
        bottom.remove(loser)
        bottom.insert(bottom.index(winner) + 1, loser)
    elif move_type == "b":
        winner, loser = bottom[-1], top[-1]
        top.remove(loser)
        top.insert(top.index(winner) + 1, loser)
    else:
        raise ValueError("Rauzy move must be 't' or 'b'")
    return (tuple(top), tuple(bottom)), winner, loser, elementary_matrix(winner, loser)


def build_graph() -> tuple[list[Permutation], dict[tuple[int, str], dict[str, object]]]:
    discovered = {INITIAL}
    pending: deque[Permutation] = deque([INITIAL])
    while pending:
        source = pending.popleft()
        for move_type in MOVE_TYPES:
            target, _, _, _ = rauzy_move(source, move_type)
            if target not in discovered:
                discovered.add(target)
                pending.append(target)

    states = sorted(discovered)
    state_id = {state: index for index, state in enumerate(states)}
    edges: dict[tuple[int, str], dict[str, object]] = {}
    for source in states:
        source_id = state_id[source]
        for move_type in MOVE_TYPES:
            target, winner, loser, matrix = rauzy_move(source, move_type)
            target_id = state_id[target]
            if sp.Matrix(matrix) * crossing_form(source) * sp.Matrix(matrix).T != crossing_form(target):
                raise AssertionError("elementary crossing-form transport failed")
            edges[(source_id, move_type)] = {
                "source": source_id,
                "type": move_type,
                "target": target_id,
                "winner": winner,
                "loser": loser,
                "matrix": matrix,
            }

    if len(states) != 7 or len(edges) != 14:
        raise AssertionError("literal Rauzy graph is not seven-state/fourteen-edge")
    if state_id[INITIAL] != 2 or state_id[AGY_BASE] != 4:
        raise AssertionError("sorted state labels no longer match the frozen source lock")
    return states, edges


def follow_word(
    start_state: int,
    word: str,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[int, IntMatrix, list[dict[str, int | str]]]:
    current = start_state
    product = IDENTITY
    tokens: list[dict[str, int | str]] = []
    for index, move_type in enumerate(word):
        edge = edges[(current, move_type)]
        edge_matrix = edge["matrix"]
        assert isinstance(edge_matrix, tuple)
        product = matmul(edge_matrix, product)
        target = int(edge["target"])
        tokens.append(
            {
                "index": index,
                "source": current,
                "type": move_type,
                "target": target,
                "winner": int(edge["winner"]),
                "loser": int(edge["loser"]),
            }
        )
        current = target
    return current, product, tokens


def decode_finite_witness(
    start_state: int,
    length_matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[str, int, IntMatrix]:
    """Replay row subtraction on one finite matrix; this is not a theorem proof."""

    current = start_state
    remaining = length_matrix
    decoded: list[str] = []
    while remaining != IDENTITY:
        admissible: list[tuple[str, int, int, tuple[int, ...]]] = []
        for move_type in MOVE_TYPES:
            edge = edges[(current, move_type)]
            winner, loser = int(edge["winner"]), int(edge["loser"])
            difference = tuple(remaining[winner - 1][column] - remaining[loser - 1][column] for column in range(4))
            if all(value >= 0 for value in difference):
                admissible.append((move_type, winner, loser, difference))
        if len(admissible) != 1:
            raise ValueError("finite decoder replay is ambiguous or invalid")
        move_type, winner, loser, difference = admissible[0]
        before = matrix_sum(remaining)
        loser_sum = sum(remaining[loser - 1])
        rows = [list(row) for row in remaining]
        rows[winner - 1] = list(difference)
        remaining = tuple(tuple(row) for row in rows)
        after = matrix_sum(remaining)
        if before - after != loser_sum or loser_sum <= 0:
            raise ValueError("finite decoder replay lost its strict descent invariant")
        current = int(edges[(current, move_type)]["target"])
        decoded.append(move_type)
        if len(decoded) > 100_000:
            raise ValueError("finite decoder replay did not terminate")
    return "".join(decoded), current, remaining


def fibonacci(index: int) -> int:
    if index <= 0:
        return 0
    first, second = 0, 1
    for _ in range(index):
        first, second = second, first + second
    return first


def finite_first_return_sentinel(
    central_state: int,
    edges: dict[tuple[int, str], dict[str, object]],
    max_length: int,
) -> dict[str, object]:
    """Finite C25-style matrix/decoder mutation sentinel, never a proof."""

    if max_length < 3 or max_length > 20:
        raise ValueError("sentinel length must lie between 3 and 20")
    stack: list[tuple[int, str, IntMatrix]] = [(central_state, "", IDENTITY)]
    returns: list[tuple[str, IntMatrix]] = []
    while stack:
        state, word, product = stack.pop()
        if len(word) == max_length:
            continue
        for move_type in reversed(MOVE_TYPES):
            edge = edges[(state, move_type)]
            edge_matrix = edge["matrix"]
            assert isinstance(edge_matrix, tuple)
            next_product = matmul(edge_matrix, product)
            next_word = word + move_type
            target = int(edge["target"])
            if target == central_state:
                returns.append((next_word, next_product))
            else:
                stack.append((target, next_word, next_product))

    returns.sort(key=lambda item: (len(item[0]), item[0]))
    counts: dict[str, int] = {}
    seen: dict[tuple[int, ...], str] = {}
    digest = hashlib.sha256()
    sample_rows = []
    for word, product in returns:
        counts[str(len(word))] = counts.get(str(len(word)), 0) + 1
        flat = matrix_flat(product)
        if flat in seen:
            raise AssertionError(f"finite sentinel collision: {seen[flat]} and {word}")
        seen[flat] = word
        decoded, end_state, terminal = decode_finite_witness(central_state, transpose(product), edges)
        if decoded != word or end_state != central_state or terminal != IDENTITY:
            raise AssertionError("finite sentinel decoder replay failed")
        digest.update(f"{word}|{','.join(str(value) for value in flat)}\n".encode("ascii"))
        if len(sample_rows) < 8:
            sample_rows.append({"word": word, "chronological_matrix_B": matrix_json(product)})

    expected = {str(length): 2 * fibonacci(length - 2) for length in range(3, max_length + 1)}
    if counts != expected:
        raise AssertionError("finite first-return count recurrence changed")
    return {
        "role": "NON_PROOF_MUTATION_AND_REGRESSION_SENTINEL_ONLY",
        "base_state": central_state,
        "base_permutation": permutation_json(INITIAL),
        "not_AGY_branch_enumeration": True,
        "max_elementary_length": max_length,
        "finite_enumeration_is_proof": False,
        "finite_enumeration_is_branch_completeness_claim": False,
        "all_length_decoder_dependency_replaced": False,
        "count_by_length": counts,
        "expected_count_formula": "2*F_(n-2), F_1=F_2=1",
        "total_first_returns": len(returns),
        "distinct_chronological_matrices": len(seen),
        "collision_count": len(returns) - len(seen),
        "canonical_word_matrix_sha256": digest.hexdigest(),
        "samples": sample_rows,
    }


def as_fraction(value: Fraction | sp.Rational | int) -> Fraction:
    if isinstance(value, Fraction):
        return value
    rational = sp.Rational(value)
    return Fraction(int(rational.p), int(rational.q))


def rational_json(value: Fraction | sp.Rational | int) -> dict[str, str]:
    exact = as_fraction(value)
    return {
        "numerator": str(exact.numerator),
        "denominator": str(exact.denominator),
        "exact": str(exact.numerator) if exact.denominator == 1 else f"{exact.numerator}/{exact.denominator}",
    }


def vector_rational_json(vector: Iterable[Fraction]) -> list[dict[str, str]]:
    return [rational_json(value) for value in vector]


def matrix_vector(matrix: IntMatrix, vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(
        sum((Fraction(matrix[row][column]) * vector[column] for column in range(4)), start=Fraction(0))
        for row in range(4)
    )


def normalize_integer_vector(vector: tuple[int, ...]) -> tuple[tuple[Fraction, ...], int]:
    scale = sum(vector)
    if scale <= 0:
        raise ValueError("normalization scale must be positive")
    return tuple(Fraction(value, scale) for value in vector), scale


def normalizer(length_matrix: IntMatrix, point: tuple[Fraction, ...]) -> Fraction:
    return sum(matrix_vector(length_matrix, point), start=Fraction(0))


def direct_projective_jacobian(length_matrix: IntMatrix, point: tuple[Fraction, ...]) -> Fraction:
    """Differentiate h(x)=Rx/(1^TRx) in three affine simplex coordinates."""

    r_matrix = sp.Matrix(length_matrix)
    x_vector = sp.Matrix([sp.Rational(value.numerator, value.denominator) for value in point])
    tangent = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    image = r_matrix * x_vector
    scale = sp.Rational(sum(image))
    derivative_image = r_matrix * tangent
    derivative_scale = sp.ones(1, 4) * derivative_image
    derivative = (derivative_image * scale - image * derivative_scale) / scale**2
    return as_fraction(sp.factor(derivative[:3, :].det()))


def slice_schema_valid(slice_theorem: dict[str, object]) -> bool:
    hypotheses = slice_theorem.get("hypotheses")
    if not isinstance(hypotheses, list):
        return False
    by_id = {row.get("id"): row for row in hypotheses if isinstance(row, dict)}
    if set(by_id) != set(REQUIRED_SLICE_HYPOTHESES):
        return False
    for hypothesis_id, status in REQUIRED_SLICE_HYPOTHESES.items():
        row = by_id[hypothesis_id]
        if row.get("required") is not True or row.get("status") != status:
            return False
    return (
        slice_theorem.get("claim_status") == "CONDITIONAL_THEOREM_APPLICATION_WITNESS"
        and slice_theorem.get("all_hypotheses_claimed_verified_by_code") is False
        and slice_theorem.get("external_theorems_reproved_here") is False
    )


def scope_firewall_valid(scope: dict[str, object]) -> bool:
    flags = scope.get("flags")
    return isinstance(flags, dict) and flags == REQUIRED_SCOPE_FLAGS


def signed_aggregate(terms: Iterable[tuple[int, Fraction]]) -> Fraction:
    """Central-sign-aware scalar aggregate used only by mutation tests."""

    return sum((sign * coefficient for sign, coefficient in terms), start=Fraction(0))


def positive_prefix_complex_cone_gate(prefix: IntMatrix) -> dict[str, object]:
    """Compute exact inputs for the positive-prefix complex-cone lemma.

    The finite computation proves positivity, a coordinate margin, and the
    Birkhoff contraction coefficient.  Existence of a common complex cone is
    the theorem-level consequence recorded below; it is not inferred from
    samples of complex points.
    """

    if any(value <= 0 for row in prefix for value in row):
        raise ValueError("the fixed prefix must be entrywise strictly positive")

    column_sums = tuple(sum(prefix[row][column] for row in range(4)) for column in range(4))
    normalized_columns = tuple(
        tuple(Fraction(prefix[row][column], column_sums[column]) for row in range(4))
        for column in range(4)
    )
    margin, margin_row, margin_column = min(
        (normalized_columns[column][row], row, column) for column in range(4) for row in range(4)
    )

    max_ratio = Fraction(0)
    ratio_witness: tuple[int, int, int, int] | None = None
    for row_i in range(4):
        for row_k in range(4):
            for column_j in range(4):
                for column_l in range(4):
                    ratio = Fraction(
                        prefix[row_i][column_j] * prefix[row_k][column_l],
                        prefix[row_i][column_l] * prefix[row_k][column_j],
                    )
                    if ratio > max_ratio:
                        max_ratio = ratio
                        ratio_witness = (row_i, row_k, column_j, column_l)
    if ratio_witness is None or max_ratio < 1:
        raise AssertionError("positive-prefix cross-ratio scan failed")

    theta = sp.Rational(max_ratio.numerator, max_ratio.denominator)
    delta_expression = sp.log(theta)
    q_expression = sp.simplify((sp.sqrt(theta) - 1) / (sp.sqrt(theta) + 1))
    if not (q_expression.is_positive and (1 - q_expression).is_positive):
        raise AssertionError("Birkhoff contraction bound is not strictly between zero and one")
    enclosure_scale = 10**24
    lower_numerator = int(sp.floor(q_expression * enclosure_scale))
    q_lower = Fraction(lower_numerator, enclosure_scale)
    q_upper = Fraction(lower_numerator + 1, enclosure_scale)
    if not bool(sp.simplify(q_expression - sp.Rational(q_lower.numerator, q_lower.denominator)) > 0):
        raise AssertionError("lower q enclosure failed")
    if not bool(sp.simplify(sp.Rational(q_upper.numerator, q_upper.denominator) - q_expression) > 0):
        raise AssertionError("upper q enclosure failed")

    normalized_payload = []
    for column, values in enumerate(normalized_columns):
        normalized_payload.append(
            {
                "column": column,
                "column_sum": column_sums[column],
                "normalized_column": vector_rational_json(values),
                "coordinate_sum_one": sum(values, start=Fraction(0)) == 1,
            }
        )

    return {
        "gate_status": "GO_BY_EXACT_POSITIVE_PREFIX_INPUTS_AND_COMPLEX_CONE_LEMMA",
        "fixed_positive_prefix": {
            "definition": "P=B_gamma_star^T=R_gamma_star",
            "matrix_P": matrix_json(prefix),
            "entrywise_strictly_positive": True,
            "branch_length_matrix_pattern": "P for gamma_star; P*Q*P for gamma_star*gamma_0*gamma_star",
            "intermediate_Q_scope": "Q is a nonnegative integral Rauzy length matrix; this branch grammar is an external AGY/C25 input",
        },
        "normalized_column_hull_K": {
            "definition": "K=conv{P[:,j]/sum_i P[i,j] : j=0,1,2,3}",
            "columns": normalized_payload,
            "coordinate_margin_delta": rational_json(margin),
            "margin_witness_zero_based": {
                "row": margin_row,
                "column": margin_column,
                "entry": prefix[margin_row][margin_column],
                "column_sum": column_sums[margin_column],
            },
            "strictly_inside_positive_simplex": margin > 0,
        },
        "birkhoff_projective_contraction": {
            "cross_ratio_definition": "theta=max_(i,k,j,l) P_ij*P_kl/(P_il*P_kj)",
            "theta": rational_json(max_ratio),
            "theta_witness_zero_based": {
                "row_i": ratio_witness[0],
                "row_k": ratio_witness[1],
                "column_j": ratio_witness[2],
                "column_l": ratio_witness[3],
            },
            "Delta_exact": f"log({max_ratio.numerator}/{max_ratio.denominator})",
            "Delta_decimal_30_digits": str(sp.N(delta_expression, 30)),
            "q_bound_exact": "(sqrt(theta)-1)/(sqrt(theta)+1)=tanh(Delta/4)",
            "q_bound_decimal_30_digits": str(sp.N(q_expression, 30)),
            "q_bound_rational_enclosure": {
                "lower_strict": rational_json(q_lower),
                "upper_strict": rational_json(q_upper),
            },
            "strict_contraction_q_less_than_one": True,
        },
        "complex_projective_metadata": {
            "real_cone_dimension": 4,
            "normalized_complex_projective_dimension": 3,
            "projective_jacobian_exponent": 4,
            "dimension_identity": "complex_projective_dimension=d-1=3 while J_h=S^(-d)=S^(-4)",
        },
        "principal_log_metadata": {
            "normalizer": "ell_gamma(z)=1^T R_gamma z",
            "half_plane": "Re(ell_gamma(z))>0 on the sufficiently small common complex cone/tube supplied by the lemma",
            "log_branch": "principal Log on the open right half-plane",
            "complex_weight": "ell_gamma(z)^(-(s+4))=exp(-(s+4)*Log(ell_gamma(z)))",
            "no_branchwise_log_choice": True,
        },
        "theorem_basis": {
            "name": "POSITIVE_PREFIX_COMPLEX_CONE_LEMMA",
            "logical_inputs_verified_here": [
                "P is entrywise strictly positive",
                "the normalized-column hull K has exact coordinate margin delta>0",
                "the exact Birkhoff cross-ratio is finite and q_bound<1",
                "the projective chart has complex dimension three",
            ],
            "theorem_consequence": "A sufficiently small branch-independent complex cone/tube is mapped strictly inside itself by every return branch with the fixed positive prefix; its normalizer remains in the principal right half-plane.",
            "numerical_sampling_used_as_proof": False,
            "finite_branch_cutoff_used_as_proof": False,
        },
    }


def evaluate_polynomial(coefficients: tuple[int, ...], value: mp.mpf) -> mp.mpf:
    result = mp.mpf("0")
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def evaluate_polynomial_derivative(coefficients: tuple[int, ...], value: mp.mpf) -> mp.mpf:
    degree = len(coefficients) - 1
    result = mp.mpf("0")
    for index, coefficient in enumerate(coefficients[:-1]):
        result = result * value + coefficient * (degree - index)
    return result


def perron_trace_specialization(
    label: str,
    word: str,
    return_count: int,
    chronological_matrix: IntMatrix,
) -> dict[str, object]:
    """Compute one exact charpoly and high-precision Perron trace atom."""

    length_matrix = transpose(chronological_matrix)
    if determinant(length_matrix) != 1 or any(value <= 0 for row in length_matrix for value in row):
        raise AssertionError("periodic trace specialization requires a positive determinant-one length matrix")
    variable = sp.Symbol("t")
    polynomial = sp.Matrix(length_matrix).charpoly(variable).as_poly()
    coefficients = tuple(int(value) for value in polynomial.all_coeffs())
    derivative_coefficients = tuple(int(value) for value in sp.diff(polynomial.as_expr(), variable).as_poly().all_coeffs())

    with mp.workdps(140):
        matrix_mp = mp.matrix([[mp.mpf(value) for value in row] for row in length_matrix])
        vector = mp.matrix([mp.mpf("0.25")] * 4)
        converged_step = None
        for step in range(10_000):
            image = matrix_mp * vector
            scale = mp.fsum(image)
            next_vector = image / scale
            error = max(abs(next_vector[index] - vector[index]) for index in range(4))
            vector = next_vector
            if error < mp.mpf("1e-120"):
                converged_step = step + 1
                break
        if converged_step is None:
            raise AssertionError("positive-matrix Perron iteration did not converge")
        image = matrix_mp * vector
        perron_root = mp.fsum(image)
        fixed_residual = max(abs(image[index] - perron_root * vector[index]) for index in range(4))

        chi_value = evaluate_polynomial(coefficients, perron_root)
        chi_scale = mp.fsum(
            abs(mp.mpf(coefficient)) * abs(perron_root) ** (len(coefficients) - 1 - index)
            for index, coefficient in enumerate(coefficients)
        )
        relative_chi_residual = abs(chi_value) / chi_scale
        chi_prime = evaluate_polynomial_derivative(coefficients, perron_root)
        chi_prime_from_coefficients = evaluate_polynomial(derivative_coefficients, perron_root)
        if abs(chi_prime - chi_prime_from_coefficients) > abs(chi_prime) * mp.mpf("1e-110"):
            raise AssertionError("two derivative evaluations disagree")

        tangent = mp.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
        derivative_image = matrix_mp * tangent
        derivative_scale = mp.matrix(
            [[mp.fsum(derivative_image[row, column] for row in range(4)) for column in range(3)]]
        )
        derivative = (derivative_image * perron_root - image * derivative_scale) / perron_root**2
        projective_derivative = mp.matrix([[derivative[row, column] for column in range(3)] for row in range(3)])
        direct_denominator = mp.det(mp.eye(3) - projective_derivative)
        characteristic_denominator = chi_prime / perron_root**3
        denominator_relative_error = abs(direct_denominator - characteristic_denominator) / abs(
            characteristic_denominator
        )
        if relative_chi_residual >= mp.mpf("1e-100"):
            raise AssertionError("Perron root does not satisfy the exact characteristic polynomial accurately enough")
        if denominator_relative_error >= mp.mpf("1e-100"):
            raise AssertionError("projective determinant and characteristic derivative disagree")

        registered_atoms = {}
        for sigma in (0, 1):
            raw_weight = perron_root ** (-(sigma + 4))
            atom = perron_root ** (-(sigma + 1)) / chi_prime
            quotient_atom = raw_weight / direct_denominator
            if abs(atom - quotient_atom) > abs(atom) * mp.mpf("1e-100"):
                raise AssertionError("periodic trace atom simplification failed")
            registered_atoms[str(sigma)] = {
                "raw_telescoped_weight_decimal_80_digits": mp.nstr(raw_weight, 80),
                "trace_atom_decimal_80_digits": mp.nstr(atom, 80),
                "quotient_check_relative_error": mp.nstr(abs(atom - quotient_atom) / abs(atom), 12),
            }

        return {
            "label": label,
            "role": "FINITE_EXACT_SPECIALIZATION_AND_HIGH_PRECISION_CHECK_NOT_GENERAL_PROOF",
            "return_count": return_count,
            "edge_word": word,
            "edge_word_sha256": hashlib.sha256(word.encode("ascii")).hexdigest(),
            "elementary_length": len(word),
            "chronological_matrix_B_word": matrix_json(chronological_matrix),
            "projective_length_matrix_A_word_equals_B_word_transpose": matrix_json(length_matrix),
            "determinant_A_word": determinant(length_matrix),
            "entrywise_positive_A_word": True,
            "characteristic_polynomial_variable": "t",
            "characteristic_polynomial_coefficients_descending": list(coefficients),
            "characteristic_polynomial": str(polynomial.as_expr()),
            "characteristic_derivative_coefficients_descending": list(derivative_coefficients),
            "perron_root_decimal_100_digits": mp.nstr(perron_root, 100),
            "perron_fixed_point_sum_one_decimal_80_digits": [mp.nstr(value, 80) for value in vector],
            "perron_iteration_steps": converged_step,
            "perron_fixed_point_residual": mp.nstr(fixed_residual, 12),
            "relative_characteristic_residual": mp.nstr(relative_chi_residual, 12),
            "chi_prime_at_perron_decimal_100_digits": mp.nstr(chi_prime, 100),
            "direct_det_I_minus_Dp_decimal_100_digits": mp.nstr(direct_denominator, 100),
            "chi_prime_over_lambda_cubed_decimal_100_digits": mp.nstr(characteristic_denominator, 100),
            "denominator_identity_relative_error": mp.nstr(denominator_relative_error, 12),
            "registered_real_s_atoms": registered_atoms,
        }


def scalar_periodic_trace_gate(
    base_state: int,
    gamma_matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    """Build trace examples plus a non-cyclic three-return order sentinel."""

    bridge_end, bridge_matrix, bridge_tokens = follow_word(base_state, RETURN_BRIDGE, edges)
    if bridge_end != base_state:
        raise AssertionError("the declared return bridge is not closed")
    if any(int(token["target"]) == base_state for token in bridge_tokens[:-1]):
        raise AssertionError("the declared bridge has an internal base-state return")

    second_end, second_matrix, _ = follow_word(base_state, SECOND_RETURN_BRANCH, edges)
    if second_end != base_state:
        raise AssertionError("the second AGY-pattern branch is not closed")
    expected_second = matmul(gamma_matrix, matmul(bridge_matrix, gamma_matrix))
    if second_matrix != expected_second:
        raise AssertionError("second branch chronology does not have B_gamma* B_bridge B_gamma*")

    two_end, two_matrix, _ = follow_word(base_state, TWO_RETURN_WORD, edges)
    if two_end != base_state:
        raise AssertionError("two-return word is not closed")
    expected_two = matmul(second_matrix, gamma_matrix)
    reversed_two = matmul(gamma_matrix, second_matrix)
    if two_matrix != expected_two or two_matrix == reversed_two:
        raise AssertionError("two-return later-on-the-left order is not detectable")

    two_charpoly = tuple(int(value) for value in sp.Matrix(transpose(two_matrix)).charpoly().all_coeffs())
    reversed_two_charpoly = tuple(
        int(value) for value in sp.Matrix(transpose(reversed_two)).charpoly().all_coeffs()
    )
    if two_charpoly != reversed_two_charpoly:
        raise AssertionError("AB and BA must have the same characteristic polynomial")

    third_bridge_end, third_bridge_matrix, third_bridge_tokens = follow_word(
        base_state, THIRD_RETURN_BRIDGE, edges
    )
    if third_bridge_end != base_state:
        raise AssertionError("the third return bridge is not closed")
    if any(int(token["target"]) == base_state for token in third_bridge_tokens[:-1]):
        raise AssertionError("the third return bridge has an internal base-state return")
    third_end, third_matrix, _ = follow_word(base_state, THIRD_RETURN_BRANCH, edges)
    expected_third = matmul(gamma_matrix, matmul(third_bridge_matrix, gamma_matrix))
    if third_end != base_state or third_matrix != expected_third:
        raise AssertionError("the third AGY-pattern branch chronology is invalid")

    three_end, three_matrix, _ = follow_word(base_state, THREE_RETURN_WORD, edges)
    reverse_three_end, reversed_three_matrix, _ = follow_word(
        base_state, REVERSED_THREE_RETURN_WORD, edges
    )
    expected_three = matmul(third_matrix, matmul(second_matrix, gamma_matrix))
    expected_reversed_three = matmul(gamma_matrix, matmul(second_matrix, third_matrix))
    if (
        three_end != base_state
        or reverse_three_end != base_state
        or three_matrix != expected_three
        or reversed_three_matrix != expected_reversed_three
        or three_matrix == reversed_three_matrix
    ):
        raise AssertionError("three-return forward/reverse chronology is invalid")
    three_charpoly = tuple(int(value) for value in sp.Matrix(transpose(three_matrix)).charpoly().all_coeffs())
    reversed_three_charpoly = tuple(
        int(value) for value in sp.Matrix(transpose(reversed_three_matrix)).charpoly().all_coeffs()
    )
    if three_charpoly == reversed_three_charpoly:
        raise AssertionError("three-return non-cyclic reversal must be spectrally detectable")

    examples = [
        perron_trace_specialization("gamma_star_one_return", GAMMA_STAR, 1, gamma_matrix),
        perron_trace_specialization("gamma_star_then_second_branch_two_returns", TWO_RETURN_WORD, 2, two_matrix),
        perron_trace_specialization(
            "gamma_star_then_second_then_third_three_returns", THREE_RETURN_WORD, 3, three_matrix
        ),
    ]
    return {
        "gate_status": "PASS_GENERAL_IDENTITY_METADATA_AND_THREE_EXACT_SPECIALIZATIONS",
        "theorem_basis": {
            "name": "PERRON_CHARACTERISTIC_POLYNOMIAL_PROJECTIVE_TRACE_IDENTITY",
            "scope": "For any strictly positive four-by-four determinant-one A with simple Perron root lambda, acting projectively by p_A(x)=Ax/(1^T A x).",
            "weight_telescope": "product of branch weights around the periodic word = lambda^(-(4+s))",
            "projective_denominator": "det_C(I-Dp_A)=chi_A'(lambda)/lambda^3",
            "trace_atom_simplification": "lambda^(-(4+s))/(chi_A'(lambda)/lambda^3)=lambda^(-(s+1))/chi_A'(lambda)",
            "complex_projective_dimension": 3,
            "jacobian_weight_exponent": 4,
            "general_identity_inferred_from_finite_examples": False,
            "proof_basis": "Perron eigenline splitting: non-Perron eigenvalues of Dp_A are mu_j/lambda, so chi_A'(lambda)=product_j(lambda-mu_j).",
        },
        "chronological_two_return_witness": {
            "role": "CONTRAVARIANT_MATRIX_ORDER_SENTINEL_NOT_SPECTRAL_CHRONOLOGY",
            "base_state": base_state,
            "return_bridge_word": RETURN_BRIDGE,
            "return_bridge_has_no_internal_base_return": True,
            "return_bridge_chronological_matrix_B": matrix_json(bridge_matrix),
            "second_branch_word": SECOND_RETURN_BRANCH,
            "second_branch_pattern": "gamma_star * return_bridge * gamma_star",
            "second_branch_chronological_matrix_B": matrix_json(second_matrix),
            "forward_Rauzy_return_order": ["gamma_star", "second_branch"],
            "forward_later_return_multiplies_on_left": True,
            "forward_matrix_identity": "B_two=B_second_branch*B_gamma_star",
            "inverse_projective_map_order": "h_two=h_gamma_star o h_second_branch",
            "operator_factor_order": ["second_branch", "gamma_star"],
            "operator_product_identity": "T_second_branch*T_gamma_star has A_two=A_gamma_star*A_second_branch=(B_second_branch*B_gamma_star)^T",
            "two_return_chronological_matrix_B": matrix_json(two_matrix),
            "reversed_order_matrix_B": matrix_json(reversed_two),
            "order_is_detectable_at_matrix_level": two_matrix != reversed_two,
            "characteristic_polynomial_is_cyclically_invariant": two_charpoly == reversed_two_charpoly,
            "characteristic_polynomial_coefficients_descending": list(two_charpoly),
        },
        "three_return_spectral_chronology_witness": {
            "role": "NONCYCLIC_FORWARD_REVERSAL_SPECTRAL_SENTINEL",
            "base_state": base_state,
            "third_return_bridge_word": THIRD_RETURN_BRIDGE,
            "third_return_bridge_has_no_internal_base_return": True,
            "third_return_bridge_chronological_matrix_B": matrix_json(third_bridge_matrix),
            "third_branch_word": THIRD_RETURN_BRANCH,
            "third_branch_chronological_matrix_B": matrix_json(third_matrix),
            "forward_Rauzy_return_order": ["gamma_star", "second_branch", "third_branch"],
            "forward_matrix_identity": "B_forward=B_third_branch*B_second_branch*B_gamma_star",
            "forward_operator_factor_order": ["third_branch", "second_branch", "gamma_star"],
            "forward_operator_identity": "T_third*T_second*T_gamma_star has A_forward=A_gamma_star*A_second*A_third",
            "forward_word": THREE_RETURN_WORD,
            "forward_elementary_length": len(THREE_RETURN_WORD),
            "forward_chronological_matrix_B": matrix_json(three_matrix),
            "forward_characteristic_polynomial_coefficients_descending": list(three_charpoly),
            "reversed_forward_Rauzy_return_order": ["third_branch", "second_branch", "gamma_star"],
            "reversed_forward_word": REVERSED_THREE_RETURN_WORD,
            "reversed_chronological_matrix_B": matrix_json(reversed_three_matrix),
            "reversed_characteristic_polynomial_coefficients_descending": list(reversed_three_charpoly),
            "noncyclic_reversal_changes_characteristic_polynomial": three_charpoly != reversed_three_charpoly,
        },
        "examples": examples,
    }


def graph_certificate(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    state_rows = []
    for state_id, permutation in enumerate(states):
        omega = crossing_form(permutation)
        state_rows.append(
            {
                "id": state_id,
                **permutation_json(permutation),
                "crossing_form": matrix_json(omega),
                "crossing_form_determinant": int(omega.det()),
            }
        )
    edge_rows = []
    for state_id in range(len(states)):
        for move_type in MOVE_TYPES:
            edge = edges[(state_id, move_type)]
            edge_rows.append(
                {
                    "source": state_id,
                    "type": move_type,
                    "target": int(edge["target"]),
                    "winner": int(edge["winner"]),
                    "loser": int(edge["loser"]),
                    "chronological_matrix": matrix_json(edge["matrix"]),
                    "transport_identity": "B_e*Omega_source*B_e^T=Omega_target",
                    "transport_verified": True,
                }
            )
    return {
        "seed_permutation": permutation_json(INITIAL),
        "state_count": len(state_rows),
        "edge_count": len(edge_rows),
        "states": state_rows,
        "edges": edge_rows,
    }


def make_slice_theorem(scale: Fraction, jacobian: Fraction) -> dict[str, object]:
    sigma_zero = scale ** -4
    sigma_one = scale ** -5
    if sigma_zero != jacobian:
        raise AssertionError("sigma=0 coefficient must equal the inverse Jacobian")
    hypotheses = [
        {
            "id": "H1_LITERAL_TRANSFER",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H1_LITERAL_TRANSFER"],
            "statement": "The candidate space X carries the literal bounded AGY metaplectic transfer L_s with chronological branch sum; no averaged matrix or finite branch surrogate is substituted.",
        },
        {
            "id": "H2_BOUNDED_CONSTANT_EMBEDDING",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H2_BOUNDED_CONSTANT_EMBEDDING"],
            "statement": "The constant-fibre map iota_const:F->X, (iota_const v)(z)=v, is bounded with finite nonzero norm C_const.",
        },
        {
            "id": "H3_BOUNDED_POINT_EVALUATION",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H3_BOUNDED_POINT_EVALUATION"],
            "statement": "Evaluation ev_x0:X->F at the released interior point x0 is bounded with finite nonzero norm C_eval.",
        },
        {
            "id": "H4_ABSOLUTE_POINTWISE_BRANCH_SUM",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H4_ABSOLUTE_POINTWISE_BRANCH_SUM"],
            "statement": "For Re(s)>-sigma_0, C25/AGY gives sum_gamma |w_(s,gamma)(x0)|<infinity, so the fibre slice is an absolutely summable discrete metaplectic atom series.",
        },
        {
            "id": "H5_PROJECTED_BRANCH_INJECTIVITY",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H5_PROJECTED_BRANCH_INJECTIVITY"],
            "statement": "C25 fixed-start all-length decoding makes distinct AGY return branches have distinct projected full symplectic matrices in this full-rank H(2) model.",
        },
        {
            "id": "H6_PATHWISE_UNITARY_LIFTS",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H6_PATHWISE_UNITARY_LIFTS"],
            "statement": "Chronological edge lifts are composed pathwise; every U_gamma is unitary and the actual metaplectic central sign is retained rather than averaged.",
        },
        {
            "id": "H7_DISCRETE_ATOM_ESSENTIAL_NORM",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H7_DISCRETE_ATOM_ESSENTIAL_NORM"],
            "statement": "The C24 discrete-metaplectic-atom theorem is invoked as an external theorem on the absolutely summable fibre slice.",
        },
        {
            "id": "H8_NONZERO_GAMMA_STAR_COEFFICIENT",
            "required": True,
            "status": REQUIRED_SLICE_HYPOTHESES["H8_NONZERO_GAMMA_STAR_COEFFICIENT"],
            "statement": "The released exact scale S_gamma_star(x0)>0 makes |w_(sigma+it,gamma_star)(x0)|=S^(-(sigma+4)) nonzero for every finite real sigma,t.",
        },
    ]
    result = {
        "claim_status": "CONDITIONAL_THEOREM_APPLICATION_WITNESS",
        "all_hypotheses_claimed_verified_by_code": False,
        "external_theorems_reproved_here": False,
        "hypotheses": hypotheses,
        "slice_identity": "ev_x0 * L_s * iota_const = sum_gamma w_(s,gamma)(x0) U_gamma",
        "external_C24_bound": "||ev_x0 L_s iota_const||_ess >= (sum_g |signed_aggregate_g|^2)^(1/2)",
        "external_C25_injective_specialization": "signed_aggregate_(g_gamma)=epsilon_gamma*w_(s,gamma)(x0), hence the l2 bound is at least the gamma_star term",
        "symbolic_gamma_star_coefficient_magnitude": "S_gamma_star(x0)^(-(sigma+4)), s=sigma+i*t",
        "compressed_slice_single_branch_floor": "||ev_x0 L_s iota_const||_ess >= |w_(s,gamma_star)(x0)| = S^(-(sigma+4))",
        "ambient_operator_floor": "||L_s||_ess >= S^(-(sigma+4))/(C_eval*C_const)",
        "normalized_map_corollary": "If C_eval=C_const=1, then ||L_s||_ess >= S^(-(sigma+4))",
        "exact_registered_sigmas": {
            "0": {
                "coefficient_magnitude": rational_json(sigma_zero),
                "identity": "S^(-4)=J_gamma_star(x0)",
                "nonzero": sigma_zero > 0,
            },
            "1": {
                "coefficient_magnitude": rational_json(sigma_one),
                "identity": "S^(-5)=J_gamma_star(x0)/S",
                "nonzero": sigma_one > 0,
            },
        },
        "parameter_domain": {
            "symbolic": "every finite s=sigma+i*t for which H1-H7 hold",
            "C25_source_half_plane": "Re(s)>-sigma_0",
            "registered_exact_sigma_values": [0, 1],
            "magnitude_independent_of_t": True,
        },
    }
    if not slice_schema_valid(result):
        raise AssertionError("slice theorem assumption schema is incomplete")
    return result


def make_certificate(sentinel_max_length: int) -> dict[str, object]:
    states, edges = build_graph()
    base_state = states.index(AGY_BASE)
    end_state, b_matrix, tokens = follow_word(base_state, GAMMA_STAR, edges)
    if end_state != base_state:
        raise AssertionError("gamma_star is not closed at the frozen state")
    r_matrix = transpose(b_matrix)
    if determinant(b_matrix) != 1 or any(value <= 0 for row in b_matrix for value in row):
        raise AssertionError("gamma_star matrix lost determinant one or strict positivity")
    base_omega = crossing_form(AGY_BASE)
    if sp.Matrix(b_matrix) * base_omega * sp.Matrix(b_matrix).T != base_omega:
        raise AssertionError("closed gamma_star matrix does not preserve the base crossing form")

    raw_x = tuple(sum(r_matrix[row]) for row in range(4))
    x0, x0_scale = normalize_integer_vector(raw_x)
    scale = normalizer(r_matrix, x0)
    if scale <= 0:
        raise AssertionError("projective normalizer must be positive")
    jacobian = scale ** -4
    direct_jacobian = direct_projective_jacobian(r_matrix, x0)
    if jacobian != direct_jacobian:
        raise AssertionError("direct affine derivative did not give S^(-4)")
    normalizer_coefficients = tuple(sum(r_matrix[row][column] for row in range(4)) for column in range(4))
    scale_from_coefficients = sum(
        (Fraction(normalizer_coefficients[index]) * x0[index] for index in range(4)),
        start=Fraction(0),
    )
    if scale_from_coefficients != scale:
        raise AssertionError("normalizer coefficient dot product changed")

    decoded_word, decoded_end, terminal = decode_finite_witness(base_state, r_matrix, edges)
    if decoded_word != GAMMA_STAR or decoded_end != base_state or terminal != IDENTITY:
        raise AssertionError("the finite gamma_star decoder witness did not replay")

    scope = {
        "flags": dict(REQUIRED_SCOPE_FLAGS),
        "positive_claim": "This machine certificate verifies the exact C25 gamma_star coefficient, cone inputs, and Perron identities used by the accompanying C26 theorems.",
        "not_claimed": [
            "a construction or boundedness theorem for a common holomorphic AGY space from finite arithmetic alone",
            "a new proof of the C24 discrete metaplectic atom theorem",
            "a new proof of the C25 all-length decoder theorem",
            "branch completeness or all-length injectivity from the finite sentinel",
            "an ordinary Hilbert trace of an isolated infinite-dimensional unitary",
            "an ordinary Fredholm determinant for the infinite oscillator twist, a Riemann divisor, or a Hilbert-Polya operator",
        ],
    }
    if not scope_firewall_valid(scope):
        raise AssertionError("scope firewall is malformed")

    sentinel = finite_first_return_sentinel(states.index(INITIAL), edges, sentinel_max_length)
    complex_cone_gate = positive_prefix_complex_cone_gate(r_matrix)
    periodic_trace_gate = scalar_periodic_trace_gate(base_state, b_matrix, edges)
    certificate = {
        "material_passport": {
            "origin": "HCS-C26 exact producer",
            "origin_mode": "experiment-bridge / exact application witness",
            "origin_date": "2026-08-10",
            "verification_status": "UNVERIFIED_UNTIL_INDEPENDENT_CHECK",
            "version_label": "c26_exact_certificate_v1",
        },
        "candidate_id": "HCS-C26",
        "candidate_name": "AGY holomorphic point-evaluation slice obstruction",
        "graph": graph_certificate(states, edges),
        "source_locked_branch": {
            "base_state": base_state,
            "base_permutation": permutation_json(AGY_BASE),
            "eta": ETA,
            "gamma_star_compressed": "t^64 (tbttbtbb)^8",
            "gamma_star_word": GAMMA_STAR,
            "gamma_star_word_sha256": hashlib.sha256(GAMMA_STAR.encode("ascii")).hexdigest(),
            "gamma_star_length": len(GAMMA_STAR),
            "start_state": base_state,
            "end_state": end_state,
            "closed": end_state == base_state,
            "edge_tokens": tokens,
            "chronology": "later elementary matrices multiply on the left",
            "chronological_matrix_B": matrix_json(b_matrix),
            "length_matrix_R_equals_B_transpose": matrix_json(r_matrix),
            "determinant_B": determinant(b_matrix),
            "entrywise_positive_B": all(value > 0 for row in b_matrix for value in row),
            "base_crossing_form": matrix_json(base_omega),
            "closed_path_form_identity": "B*Omega_base*B^T=Omega_base",
            "closed_path_form_identity_verified": True,
            "finite_gamma_star_decoder_replay": {
                "role": "FINITE_APPLICATION_WITNESS_REPLAY_NOT_ALL_LENGTH_PROOF",
                "decoded_word": decoded_word,
                "decoded_word_sha256": hashlib.sha256(decoded_word.encode("ascii")).hexdigest(),
                "decoded_steps": len(decoded_word),
                "end_state": decoded_end,
                "terminal_identity": terminal == IDENTITY,
            },
        },
        "projective_point_witness": {
            "branch_definition": "h_gamma(x)=R_gamma*x/S_gamma(x), R_gamma=B_gamma^T",
            "normalizer_definition": "S_gamma(x)=1^T*R_gamma*x",
            "normalizer_coefficients": list(normalizer_coefficients),
            "x0_definition": "normalize(R_gamma_star*1)",
            "x0_unnormalized": list(raw_x),
            "x0_normalization": x0_scale,
            "x0": vector_rational_json(x0),
            "x0_positive_simplex": all(value > 0 for value in x0) and sum(x0, start=Fraction(0)) == 1,
            "S_gamma_star_at_x0": rational_json(scale),
            "S_positive": scale > 0,
            "roof_at_x0": f"log({rational_json(scale)['exact']})",
            "jacobian_dimension": 4,
            "jacobian_formula": "J_gamma_star(x0)=det(R)/S_gamma_star(x0)^4=S^(-4)",
            "determinant_R": determinant(r_matrix),
            "J_gamma_star_at_x0": rational_json(jacobian),
            "direct_three_affine_coordinate_derivative_check": direct_jacobian == jacobian,
        },
        "common_complex_domain_gate": complex_cone_gate,
        "scalar_periodic_trace_gate": periodic_trace_gate,
        "point_evaluation_slice_theorem": make_slice_theorem(scale, jacobian),
        "finite_decoder_sentinel": sentinel,
        "scope_firewall": scope,
        "decisions": {
            "exact_gamma_star_input": "PASS",
            "common_complex_domain_gate": "GO_BY_POSITIVE_PREFIX_COMPLEX_CONE_LEMMA",
            "scalar_periodic_trace_gate": "PASS_PERRON_CHARACTERISTIC_SIMPLIFICATION",
            "point_evaluation_slice_chain": "CONDITIONAL_COMPLETE_WITH_EXTERNAL_C24_C25_DEPENDENCIES",
            "holomorphic_space_constructed_by_exact_code": False,
            "scalar_Bergman_theorem_status": "PROVED_IN_THEOREM_PACKAGE_NOT_BY_FINITE_CERTIFICATE",
            "ordinary_scalar_Fredholm_status": "PROVED_IN_THEOREM_PACKAGE_NOT_BY_FINITE_CERTIFICATE",
            "ordinary_holomorphic_metaplectic_Fredholm_authorized": False,
            "route_B_authorized": False,
        },
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "sentinel_max_length": sentinel_max_length,
        },
    }
    return certificate


def main() -> None:
    args = parse_args()
    certificate = make_certificate(args.sentinel_max_length)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    scale = certificate["projective_point_witness"]["S_gamma_star_at_x0"]["exact"]
    sigma_zero = certificate["point_evaluation_slice_theorem"]["exact_registered_sigmas"]["0"]["coefficient_magnitude"]["exact"]
    sigma_one = certificate["point_evaluation_slice_theorem"]["exact_registered_sigmas"]["1"]["coefficient_magnitude"]["exact"]
    complex_gate = certificate["common_complex_domain_gate"]
    trace_examples = certificate["scalar_periodic_trace_gate"]["examples"]
    print(
        json.dumps(
            {
                "states": certificate["graph"]["state_count"],
                "edges": certificate["graph"]["edge_count"],
                "base_state": certificate["source_locked_branch"]["base_state"],
                "gamma_length": certificate["source_locked_branch"]["gamma_star_length"],
                "S_x0": scale,
                "sigma_0_floor": sigma_zero,
                "sigma_1_floor": sigma_one,
                "complex_cone_delta": complex_gate["normalized_column_hull_K"]["coordinate_margin_delta"]["exact"],
                "birkhoff_theta": complex_gate["birkhoff_projective_contraction"]["theta"]["exact"],
                "birkhoff_q_bound": complex_gate["birkhoff_projective_contraction"]["q_bound_decimal_30_digits"],
                "periodic_trace_examples": len(trace_examples),
                "two_return_elementary_length": trace_examples[1]["elementary_length"],
                "three_return_elementary_length": trace_examples[2]["elementary_length"],
                "sentinel_first_returns": certificate["finite_decoder_sentinel"]["total_first_returns"],
                "sentinel_collisions": certificate["finite_decoder_sentinel"]["collision_count"],
            },
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
