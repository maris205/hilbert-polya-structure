#!/usr/bin/env python3
"""Independent verifier for the HCS-C26 point-evaluation-slice certificate.

The checker deliberately does not import the producer.  It reconstructs the
Rauzy graph, frozen word, chronological matrices, projective point, exact
normalizer, Jacobian, registered coefficient floors, and optional finite
sentinel with separate code.  It validates the conditional-assumption and
claim-scope firewalls but does not claim to verify those external theorems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c26_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c26_independent_check.json"

LETTERS = (1, 2, 3, 4)
KINDS = ("t", "b")
SEED = ((1, 2, 3, 4), (4, 3, 2, 1))
SECTION = ((1, 3, 4, 2), (4, 3, 2, 1))
ETA_WORD = "tbttbtbb"
SECTION_WORD = "t" * 64 + ETA_WORD * 8
BRIDGE_WORD = ETA_WORD[1:]
SECOND_BRANCH_WORD = SECTION_WORD + BRIDGE_WORD + SECTION_WORD
ORDERED_TWO_RETURN_WORD = SECTION_WORD + SECOND_BRANCH_WORD
THIRD_BRIDGE_WORD = "bbb"
THIRD_BRANCH_WORD = SECTION_WORD + THIRD_BRIDGE_WORD + SECTION_WORD
ORDERED_THREE_RETURN_WORD = SECTION_WORD + SECOND_BRANCH_WORD + THIRD_BRANCH_WORD
REVERSED_THREE_RETURN_WORD = THIRD_BRANCH_WORD + SECOND_BRANCH_WORD + SECTION_WORD
EYE = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))

EXPECTED_HYPOTHESES = {
    "H1_LITERAL_TRANSFER": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H2_BOUNDED_CONSTANT_EMBEDDING": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H3_BOUNDED_POINT_EVALUATION": "CANDIDATE_SPACE_ASSUMPTION_NOT_VERIFIED_BY_CODE",
    "H4_ABSOLUTE_POINTWISE_BRANCH_SUM": "EXTERNAL_C25_THEOREM_NOT_REPROVED",
    "H5_PROJECTED_BRANCH_INJECTIVITY": "EXTERNAL_C25_THEOREM_NOT_REPROVED",
    "H6_PATHWISE_UNITARY_LIFTS": "EXTERNAL_C25_INPUT_NOT_REPROVED",
    "H7_DISCRETE_ATOM_ESSENTIAL_NORM": "EXTERNAL_C24_THEOREM_NOT_REPROVED",
    "H8_NONZERO_GAMMA_STAR_COEFFICIENT": "EXACT_WITNESS_VERIFIED_HERE",
}

EXPECTED_SCOPE_FLAGS = {
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

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
IntMatrix = tuple[tuple[int, ...], ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def portable(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def digest_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_list(matrix: IntMatrix | sp.Matrix) -> list[list[int]]:
    if isinstance(matrix, sp.MatrixBase):
        return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]
    return [list(row) for row in matrix]


def permutation_list(permutation: Permutation) -> dict[str, list[int]]:
    return {"top": list(permutation[0]), "bottom": list(permutation[1])}


def transposed(matrix: IntMatrix) -> IntMatrix:
    return tuple(tuple(matrix[column][row] for column in range(4)) for row in range(4))


def product(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(4)) for column in range(4))
        for row in range(4)
    )


def total(matrix: IntMatrix) -> int:
    return sum(sum(row) for row in matrix)


def flatten(matrix: IntMatrix) -> tuple[int, ...]:
    return tuple(value for row in matrix for value in row)


def elementary(winner: int, loser: int) -> IntMatrix:
    rows = [list(row) for row in EYE]
    rows[loser - 1][winner - 1] += 1
    return tuple(tuple(row) for row in rows)


def form(permutation: Permutation) -> sp.Matrix:
    top, bottom = permutation
    top_at = {letter: index for index, letter in enumerate(top)}
    bottom_at = {letter: index for index, letter in enumerate(bottom)}
    result = sp.zeros(4)
    for alpha in LETTERS:
        for beta in LETTERS:
            inversion = (top_at[alpha] - top_at[beta]) * (bottom_at[alpha] - bottom_at[beta])
            if inversion < 0:
                result[alpha - 1, beta - 1] = 1 if top_at[alpha] < top_at[beta] else -1
    return result


def arrow(permutation: Permutation, kind: str) -> tuple[Permutation, int, int, IntMatrix]:
    top, bottom = [list(row) for row in permutation]
    if kind == "t":
        winner, loser = top[-1], bottom[-1]
        bottom.remove(loser)
        bottom.insert(bottom.index(winner) + 1, loser)
    elif kind == "b":
        winner, loser = bottom[-1], top[-1]
        top.remove(loser)
        top.insert(top.index(winner) + 1, loser)
    else:
        raise ValueError("unknown Rauzy arrow")
    return (tuple(top), tuple(bottom)), winner, loser, elementary(winner, loser)


def rebuild_graph() -> tuple[list[Permutation], dict[tuple[int, str], dict[str, object]]]:
    pending = [SEED]
    found = {SEED}
    while pending:
        source = pending.pop()
        for kind in KINDS:
            target, _, _, _ = arrow(source, kind)
            if target not in found:
                found.add(target)
                pending.append(target)
    states = sorted(found)
    ids = {state: index for index, state in enumerate(states)}
    edges: dict[tuple[int, str], dict[str, object]] = {}
    for source in states:
        source_id = ids[source]
        for kind in KINDS:
            target, winner, loser, matrix = arrow(source, kind)
            if sp.Matrix(matrix) * form(source) * sp.Matrix(matrix).T != form(target):
                raise AssertionError("independent edge transport failed")
            edges[(source_id, kind)] = {
                "source": source_id,
                "type": kind,
                "target": ids[target],
                "winner": winner,
                "loser": loser,
                "matrix": matrix,
            }
    if len(states) != 7 or len(edges) != 14 or ids[SEED] != 2 or ids[SECTION] != 4:
        raise AssertionError("independent source graph lock failed")
    return states, edges


def graph_payload(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    state_rows = []
    for state_id, permutation in enumerate(states):
        omega = form(permutation)
        state_rows.append(
            {
                "id": state_id,
                **permutation_list(permutation),
                "crossing_form": matrix_list(omega),
                "crossing_form_determinant": int(omega.det()),
            }
        )
    edge_rows = []
    for state_id in range(7):
        for kind in KINDS:
            edge = edges[(state_id, kind)]
            edge_rows.append(
                {
                    "source": state_id,
                    "type": kind,
                    "target": int(edge["target"]),
                    "winner": int(edge["winner"]),
                    "loser": int(edge["loser"]),
                    "chronological_matrix": matrix_list(edge["matrix"]),
                    "transport_identity": "B_e*Omega_source*B_e^T=Omega_target",
                    "transport_verified": True,
                }
            )
    return {
        "seed_permutation": permutation_list(SEED),
        "state_count": 7,
        "edge_count": 14,
        "states": state_rows,
        "edges": edge_rows,
    }


def walk(
    start: int,
    word: str,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[int, IntMatrix, list[dict[str, int | str]]]:
    state = start
    matrix = EYE
    tokens: list[dict[str, int | str]] = []
    for index, kind in enumerate(word):
        edge = edges[(state, kind)]
        edge_matrix = edge["matrix"]
        assert isinstance(edge_matrix, tuple)
        matrix = product(edge_matrix, matrix)
        target = int(edge["target"])
        tokens.append(
            {
                "index": index,
                "source": state,
                "type": kind,
                "target": target,
                "winner": int(edge["winner"]),
                "loser": int(edge["loser"]),
            }
        )
        state = target
    return state, matrix, tokens


def replay_decoder(
    start: int,
    length_matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[str, int, IntMatrix]:
    state = start
    remainder = length_matrix
    letters: list[str] = []
    while remainder != EYE:
        choices = []
        for kind in KINDS:
            edge = edges[(state, kind)]
            winner, loser = int(edge["winner"]), int(edge["loser"])
            difference = tuple(remainder[winner - 1][j] - remainder[loser - 1][j] for j in range(4))
            if min(difference) >= 0:
                choices.append((kind, winner, loser, difference))
        if len(choices) != 1:
            raise ValueError("independent finite decoder did not have one choice")
        kind, winner, loser, difference = choices[0]
        before = total(remainder)
        loser_sum = sum(remainder[loser - 1])
        rows = [list(row) for row in remainder]
        rows[winner - 1] = list(difference)
        remainder = tuple(tuple(row) for row in rows)
        if before - total(remainder) != loser_sum or loser_sum <= 0:
            raise ValueError("independent decoder descent failed")
        state = int(edges[(state, kind)]["target"])
        letters.append(kind)
        if len(letters) > 100_000:
            raise ValueError("independent finite decoder did not terminate")
    return "".join(letters), state, remainder


def fib(index: int) -> int:
    a, b = 0, 1
    for _ in range(max(index, 0)):
        a, b = b, a + b
    return a


def sentinel_replay(
    central: int,
    edges: dict[tuple[int, str], dict[str, object]],
    max_length: int,
) -> dict[str, object]:
    pending: list[tuple[int, str, IntMatrix]] = [(central, "", EYE)]
    rows: list[tuple[str, IntMatrix]] = []
    while pending:
        state, word, matrix = pending.pop()
        if len(word) == max_length:
            continue
        for kind in reversed(KINDS):
            edge = edges[(state, kind)]
            edge_matrix = edge["matrix"]
            assert isinstance(edge_matrix, tuple)
            next_matrix = product(edge_matrix, matrix)
            next_word = word + kind
            target = int(edge["target"])
            if target == central:
                rows.append((next_word, next_matrix))
            else:
                pending.append((target, next_word, next_matrix))
    rows.sort(key=lambda item: (len(item[0]), item[0]))

    counts: dict[str, int] = {}
    matrices: dict[tuple[int, ...], str] = {}
    digest = hashlib.sha256()
    samples = []
    for word, matrix in rows:
        counts[str(len(word))] = counts.get(str(len(word)), 0) + 1
        flat = flatten(matrix)
        if flat in matrices:
            raise AssertionError("independent sentinel found a matrix collision")
        matrices[flat] = word
        decoded, end, terminal = replay_decoder(central, transposed(matrix), edges)
        if decoded != word or end != central or terminal != EYE:
            raise AssertionError("independent sentinel decoder mismatch")
        digest.update(f"{word}|{','.join(str(value) for value in flat)}\n".encode("ascii"))
        if len(samples) < 8:
            samples.append({"word": word, "chronological_matrix_B": matrix_list(matrix)})

    expected = {str(length): 2 * fib(length - 2) for length in range(3, max_length + 1)}
    if counts != expected:
        raise AssertionError("independent sentinel recurrence mismatch")
    return {
        "role": "NON_PROOF_MUTATION_AND_REGRESSION_SENTINEL_ONLY",
        "base_state": central,
        "base_permutation": permutation_list(SEED),
        "not_AGY_branch_enumeration": True,
        "max_elementary_length": max_length,
        "finite_enumeration_is_proof": False,
        "finite_enumeration_is_branch_completeness_claim": False,
        "all_length_decoder_dependency_replaced": False,
        "count_by_length": counts,
        "expected_count_formula": "2*F_(n-2), F_1=F_2=1",
        "total_first_returns": len(rows),
        "distinct_chronological_matrices": len(matrices),
        "collision_count": len(rows) - len(matrices),
        "canonical_word_matrix_sha256": digest.hexdigest(),
        "samples": samples,
    }


def fraction_record(value: dict[str, object]) -> Fraction:
    numerator = int(str(value["numerator"]))
    denominator = int(str(value["denominator"]))
    result = Fraction(numerator, denominator)
    expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    if value["exact"] != expected:
        raise AssertionError("rational exact string does not match numerator/denominator")
    return result


def vector_record(values: list[dict[str, object]]) -> tuple[Fraction, ...]:
    return tuple(fraction_record(value) for value in values)


def apply_matrix(matrix: IntMatrix, vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(
        sum((Fraction(matrix[i][j]) * vector[j] for j in range(4)), start=Fraction(0)) for i in range(4)
    )


def projective_jacobian(length_matrix: IntMatrix, point: tuple[Fraction, ...]) -> Fraction:
    r = sp.Matrix(length_matrix)
    x = sp.Matrix([sp.Rational(value.numerator, value.denominator) for value in point])
    tangent = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    image = r * x
    scale = sp.Rational(sum(image))
    derivative_image = r * tangent
    derivative_scale = sp.ones(1, 4) * derivative_image
    derivative = (derivative_image * scale - image * derivative_scale) / scale**2
    value = sp.Rational(sp.factor(derivative[:3, :].det()))
    return Fraction(int(value.p), int(value.q))


def theorem_schema_ok(theorem: dict[str, object]) -> bool:
    rows = theorem.get("hypotheses")
    if not isinstance(rows, list):
        return False
    by_id = {row.get("id"): row for row in rows if isinstance(row, dict)}
    if set(by_id) != set(EXPECTED_HYPOTHESES):
        return False
    for hypothesis_id, status in EXPECTED_HYPOTHESES.items():
        if by_id[hypothesis_id].get("required") is not True or by_id[hypothesis_id].get("status") != status:
            return False
    return (
        theorem.get("claim_status") == "CONDITIONAL_THEOREM_APPLICATION_WITNESS"
        and theorem.get("all_hypotheses_claimed_verified_by_code") is False
        and theorem.get("external_theorems_reproved_here") is False
        and theorem.get("symbolic_gamma_star_coefficient_magnitude")
        == "S_gamma_star(x0)^(-(sigma+4)), s=sigma+i*t"
        and theorem.get("compressed_slice_single_branch_floor")
        == "||ev_x0 L_s iota_const||_ess >= |w_(s,gamma_star)(x0)| = S^(-(sigma+4))"
        and theorem.get("ambient_operator_floor")
        == "||L_s||_ess >= S^(-(sigma+4))/(C_eval*C_const)"
    )


def independent_complex_cone_gate(prefix: IntMatrix, released: dict[str, object]) -> tuple[bool, dict[str, str]]:
    if any(value <= 0 for row in prefix for value in row):
        return False, {}
    column_sums = tuple(sum(prefix[row][column] for row in range(4)) for column in range(4))
    normalized_columns = tuple(
        tuple(Fraction(prefix[row][column], column_sums[column]) for row in range(4))
        for column in range(4)
    )
    margin, margin_row, margin_column = min(
        (normalized_columns[column][row], row, column) for column in range(4) for row in range(4)
    )
    theta = Fraction(0)
    theta_witness = None
    for row_i in range(4):
        for row_k in range(4):
            for column_j in range(4):
                for column_l in range(4):
                    value = Fraction(
                        prefix[row_i][column_j] * prefix[row_k][column_l],
                        prefix[row_i][column_l] * prefix[row_k][column_j],
                    )
                    if value > theta:
                        theta = value
                        theta_witness = (row_i, row_k, column_j, column_l)
    if theta_witness is None:
        return False, {}
    theta_sp = sp.Rational(theta.numerator, theta.denominator)
    delta_expression = sp.log(theta_sp)
    q_expression = sp.simplify((sp.sqrt(theta_sp) - 1) / (sp.sqrt(theta_sp) + 1))

    hull = released["normalized_column_hull_K"]
    released_columns = hull["columns"]
    columns_ok = len(released_columns) == 4
    for column in range(4):
        columns_ok &= released_columns[column]["column"] == column
        columns_ok &= released_columns[column]["column_sum"] == column_sums[column]
        columns_ok &= vector_record(released_columns[column]["normalized_column"]) == normalized_columns[column]
        columns_ok &= released_columns[column]["coordinate_sum_one"] is True
    margin_witness = hull["margin_witness_zero_based"]
    margin_ok = (
        fraction_record(hull["coordinate_margin_delta"]) == margin
        and margin_witness
        == {
            "row": margin_row,
            "column": margin_column,
            "entry": prefix[margin_row][margin_column],
            "column_sum": column_sums[margin_column],
        }
        and hull["strictly_inside_positive_simplex"] is True
        and margin > 0
    )

    contraction = released["birkhoff_projective_contraction"]
    witness = contraction["theta_witness_zero_based"]
    lower = fraction_record(contraction["q_bound_rational_enclosure"]["lower_strict"])
    upper = fraction_record(contraction["q_bound_rational_enclosure"]["upper_strict"])
    contraction_ok = (
        fraction_record(contraction["theta"]) == theta
        and witness
        == {
            "row_i": theta_witness[0],
            "row_k": theta_witness[1],
            "column_j": theta_witness[2],
            "column_l": theta_witness[3],
        }
        and contraction["Delta_exact"] == f"log({theta.numerator}/{theta.denominator})"
        and contraction["Delta_decimal_30_digits"] == str(sp.N(delta_expression, 30))
        and contraction["q_bound_decimal_30_digits"] == str(sp.N(q_expression, 30))
        and sp.Rational(lower.numerator, lower.denominator) < q_expression
        and q_expression < sp.Rational(upper.numerator, upper.denominator)
        and contraction["strict_contraction_q_less_than_one"] is True
        and 0 < q_expression < 1
    )
    prefix_block = released["fixed_positive_prefix"]
    dimensions = released["complex_projective_metadata"]
    logarithm = released["principal_log_metadata"]
    theorem = released["theorem_basis"]
    metadata_ok = (
        released["gate_status"] == "GO_BY_EXACT_POSITIVE_PREFIX_INPUTS_AND_COMPLEX_CONE_LEMMA"
        and prefix_block["definition"] == "P=B_gamma_star^T=R_gamma_star"
        and prefix_block["matrix_P"] == matrix_list(prefix)
        and prefix_block["entrywise_strictly_positive"] is True
        and prefix_block["branch_length_matrix_pattern"]
        == "P for gamma_star; P*Q*P for gamma_star*gamma_0*gamma_star"
        and dimensions["real_cone_dimension"] == 4
        and dimensions["normalized_complex_projective_dimension"] == 3
        and dimensions["projective_jacobian_exponent"] == 4
        and logarithm["half_plane"].startswith("Re(ell_gamma(z))>0")
        and logarithm["log_branch"] == "principal Log on the open right half-plane"
        and logarithm["no_branchwise_log_choice"] is True
        and theorem["name"] == "POSITIVE_PREFIX_COMPLEX_CONE_LEMMA"
        and theorem["numerical_sampling_used_as_proof"] is False
        and theorem["finite_branch_cutoff_used_as_proof"] is False
    )
    return bool(columns_ok and margin_ok and contraction_ok and metadata_ok), {
        "coordinate_margin_delta": str(margin),
        "birkhoff_cross_ratio_theta": str(theta),
        "birkhoff_q_bound": str(sp.N(q_expression, 30)),
    }


def mp_polynomial(coefficients: tuple[int, ...], value: mp.mpf) -> mp.mpf:
    result = mp.mpf("0")
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def independent_perron_trace_check(
    released: dict[str, object],
    label: str,
    word: str,
    return_count: int,
    chronological_matrix: IntMatrix,
) -> tuple[bool, dict[str, str]]:
    length_matrix = transposed(chronological_matrix)
    variable = sp.Symbol("t")
    polynomial = sp.Matrix(length_matrix).charpoly(variable).as_poly()
    coefficients = tuple(int(value) for value in polynomial.all_coeffs())
    derivative_coefficients = tuple(
        int(value) for value in sp.diff(polynomial.as_expr(), variable).as_poly().all_coeffs()
    )
    exact_ok = (
        released["label"] == label
        and released["role"] == "FINITE_EXACT_SPECIALIZATION_AND_HIGH_PRECISION_CHECK_NOT_GENERAL_PROOF"
        and released["return_count"] == return_count
        and released["edge_word"] == word
        and released["edge_word_sha256"] == hashlib.sha256(word.encode("ascii")).hexdigest()
        and released["elementary_length"] == len(word)
        and released["chronological_matrix_B_word"] == matrix_list(chronological_matrix)
        and released["projective_length_matrix_A_word_equals_B_word_transpose"] == matrix_list(length_matrix)
        and released["determinant_A_word"] == int(sp.Matrix(length_matrix).det()) == 1
        and released["entrywise_positive_A_word"] is True
        and min(flatten(length_matrix)) > 0
        and released["characteristic_polynomial_coefficients_descending"] == list(coefficients)
        and released["characteristic_polynomial"] == str(polynomial.as_expr())
        and released["characteristic_derivative_coefficients_descending"] == list(derivative_coefficients)
    )

    with mp.workdps(160):
        matrix_mp = mp.matrix([[mp.mpf(value) for value in row] for row in length_matrix])
        vector = mp.matrix([mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.3"), mp.mpf("0.4")])
        for _ in range(10_000):
            image = matrix_mp * vector
            scale = mp.fsum(image)
            next_vector = image / scale
            if max(abs(next_vector[index] - vector[index]) for index in range(4)) < mp.mpf("1e-135"):
                vector = next_vector
                break
            vector = next_vector
        else:
            return False, {}
        image = matrix_mp * vector
        perron = mp.fsum(image)
        chi_prime = mp_polynomial(derivative_coefficients, perron)
        characteristic_scale = mp.fsum(
            abs(mp.mpf(coefficient)) * abs(perron) ** (len(coefficients) - 1 - index)
            for index, coefficient in enumerate(coefficients)
        )
        characteristic_residual = abs(mp_polynomial(coefficients, perron)) / characteristic_scale

        coordinates = mp.matrix([vector[0], vector[1], vector[2]])

        def projective_map(first_three: mp.matrix) -> mp.matrix:
            full = mp.matrix(
                [first_three[0], first_three[1], first_three[2], 1 - mp.fsum(first_three)]
            )
            mapped = matrix_mp * full
            mapped_scale = mp.fsum(mapped)
            return mp.matrix([mapped[0] / mapped_scale, mapped[1] / mapped_scale, mapped[2] / mapped_scale])

        step = mp.mpf("1e-45")
        finite_difference = mp.matrix(3, 3)
        for column in range(3):
            plus = mp.matrix(coordinates)
            minus = mp.matrix(coordinates)
            plus[column] += step
            minus[column] -= step
            difference = (projective_map(plus) - projective_map(minus)) / (2 * step)
            for row in range(3):
                finite_difference[row, column] = difference[row]
        finite_difference_denominator = mp.det(mp.eye(3) - finite_difference)
        characteristic_denominator = chi_prime / perron**3
        denominator_error = abs(finite_difference_denominator - characteristic_denominator) / abs(
            characteristic_denominator
        )

        released_perron = mp.mpf(released["perron_root_decimal_100_digits"])
        released_chi_prime = mp.mpf(released["chi_prime_at_perron_decimal_100_digits"])
        released_direct = mp.mpf(released["direct_det_I_minus_Dp_decimal_100_digits"])
        released_characteristic = mp.mpf(released["chi_prime_over_lambda_cubed_decimal_100_digits"])
        numeric_ok = (
            abs(released_perron - perron) / abs(perron) < mp.mpf("1e-95")
            and abs(released_chi_prime - chi_prime) / abs(chi_prime) < mp.mpf("1e-95")
            and abs(released_direct - finite_difference_denominator) / abs(characteristic_denominator)
            < mp.mpf("1e-85")
            and abs(released_characteristic - characteristic_denominator) / abs(characteristic_denominator)
            < mp.mpf("1e-95")
            and characteristic_residual < mp.mpf("1e-115")
            and denominator_error < mp.mpf("1e-85")
        )
        atom_ok = True
        for sigma in (0, 1):
            released_atom = released["registered_real_s_atoms"][str(sigma)]
            raw_weight = perron ** (-(sigma + 4))
            atom = perron ** (-(sigma + 1)) / chi_prime
            atom_ok &= abs(mp.mpf(released_atom["raw_telescoped_weight_decimal_80_digits"]) - raw_weight) / abs(
                raw_weight
            ) < mp.mpf("1e-75")
            atom_ok &= abs(mp.mpf(released_atom["trace_atom_decimal_80_digits"]) - atom) / abs(atom) < mp.mpf(
                "1e-75"
            )
    return bool(exact_ok and numeric_ok and atom_ok), {
        "label": label,
        "perron_root": released["perron_root_decimal_100_digits"],
        "chi_prime_at_perron": released["chi_prime_at_perron_decimal_100_digits"],
        "finite_difference_denominator_relative_error": mp.nstr(denominator_error, 12),
    }


def independent_periodic_trace_gate(
    base: int,
    gamma_matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
    released: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    bridge_end, bridge_matrix, bridge_tokens = walk(base, BRIDGE_WORD, edges)
    second_end, second_matrix, _ = walk(base, SECOND_BRANCH_WORD, edges)
    two_end, two_matrix, _ = walk(base, ORDERED_TWO_RETURN_WORD, edges)
    expected_second = product(gamma_matrix, product(bridge_matrix, gamma_matrix))
    expected_two = product(second_matrix, gamma_matrix)
    reversed_two = product(gamma_matrix, second_matrix)
    witness = released["chronological_two_return_witness"]
    two_charpoly = [int(value) for value in sp.Matrix(transposed(two_matrix)).charpoly().all_coeffs()]
    reversed_two_charpoly = [
        int(value) for value in sp.Matrix(transposed(reversed_two)).charpoly().all_coeffs()
    ]
    order_ok = (
        bridge_end == second_end == two_end == base
        and all(int(token["target"]) != base for token in bridge_tokens[:-1])
        and second_matrix == expected_second
        and two_matrix == expected_two
        and two_matrix != reversed_two
        and witness["base_state"] == base
        and witness["return_bridge_word"] == BRIDGE_WORD
        and witness["return_bridge_has_no_internal_base_return"] is True
        and witness["return_bridge_chronological_matrix_B"] == matrix_list(bridge_matrix)
        and witness["second_branch_word"] == SECOND_BRANCH_WORD
        and witness["second_branch_chronological_matrix_B"] == matrix_list(second_matrix)
        and witness["forward_Rauzy_return_order"] == ["gamma_star", "second_branch"]
        and witness["forward_later_return_multiplies_on_left"] is True
        and witness["forward_matrix_identity"] == "B_two=B_second_branch*B_gamma_star"
        and witness["inverse_projective_map_order"] == "h_two=h_gamma_star o h_second_branch"
        and witness["operator_factor_order"] == ["second_branch", "gamma_star"]
        and witness["operator_product_identity"]
        == "T_second_branch*T_gamma_star has A_two=A_gamma_star*A_second_branch=(B_second_branch*B_gamma_star)^T"
        and witness["two_return_chronological_matrix_B"] == matrix_list(two_matrix)
        and witness["reversed_order_matrix_B"] == matrix_list(reversed_two)
        and witness["order_is_detectable_at_matrix_level"] is True
        and witness["role"] == "CONTRAVARIANT_MATRIX_ORDER_SENTINEL_NOT_SPECTRAL_CHRONOLOGY"
        and witness["characteristic_polynomial_is_cyclically_invariant"] is True
        and witness["characteristic_polynomial_coefficients_descending"] == two_charpoly
        and two_charpoly == reversed_two_charpoly
    )

    third_bridge_end, third_bridge_matrix, third_bridge_tokens = walk(base, THIRD_BRIDGE_WORD, edges)
    third_end, third_matrix, _ = walk(base, THIRD_BRANCH_WORD, edges)
    three_end, three_matrix, _ = walk(base, ORDERED_THREE_RETURN_WORD, edges)
    reverse_three_end, reversed_three_matrix, _ = walk(base, REVERSED_THREE_RETURN_WORD, edges)
    expected_third = product(gamma_matrix, product(third_bridge_matrix, gamma_matrix))
    expected_three = product(third_matrix, product(second_matrix, gamma_matrix))
    expected_reversed_three = product(gamma_matrix, product(second_matrix, third_matrix))
    three_charpoly = [int(value) for value in sp.Matrix(transposed(three_matrix)).charpoly().all_coeffs()]
    reversed_three_charpoly = [
        int(value) for value in sp.Matrix(transposed(reversed_three_matrix)).charpoly().all_coeffs()
    ]
    spectral = released["three_return_spectral_chronology_witness"]
    spectral_order_ok = (
        third_bridge_end == third_end == three_end == reverse_three_end == base
        and all(int(token["target"]) != base for token in third_bridge_tokens[:-1])
        and third_matrix == expected_third
        and three_matrix == expected_three
        and reversed_three_matrix == expected_reversed_three
        and three_matrix != reversed_three_matrix
        and three_charpoly != reversed_three_charpoly
        and spectral["role"] == "NONCYCLIC_FORWARD_REVERSAL_SPECTRAL_SENTINEL"
        and spectral["base_state"] == base
        and spectral["third_return_bridge_word"] == THIRD_BRIDGE_WORD
        and spectral["third_return_bridge_has_no_internal_base_return"] is True
        and spectral["third_return_bridge_chronological_matrix_B"] == matrix_list(third_bridge_matrix)
        and spectral["third_branch_word"] == THIRD_BRANCH_WORD
        and spectral["third_branch_chronological_matrix_B"] == matrix_list(third_matrix)
        and spectral["forward_Rauzy_return_order"] == ["gamma_star", "second_branch", "third_branch"]
        and spectral["forward_matrix_identity"]
        == "B_forward=B_third_branch*B_second_branch*B_gamma_star"
        and spectral["forward_operator_factor_order"] == ["third_branch", "second_branch", "gamma_star"]
        and spectral["forward_operator_identity"]
        == "T_third*T_second*T_gamma_star has A_forward=A_gamma_star*A_second*A_third"
        and spectral["forward_word"] == ORDERED_THREE_RETURN_WORD
        and spectral["forward_elementary_length"] == len(ORDERED_THREE_RETURN_WORD) == 650
        and spectral["forward_chronological_matrix_B"] == matrix_list(three_matrix)
        and spectral["forward_characteristic_polynomial_coefficients_descending"] == three_charpoly
        and spectral["reversed_forward_Rauzy_return_order"]
        == ["third_branch", "second_branch", "gamma_star"]
        and spectral["reversed_forward_word"] == REVERSED_THREE_RETURN_WORD
        and spectral["reversed_chronological_matrix_B"] == matrix_list(reversed_three_matrix)
        and spectral["reversed_characteristic_polynomial_coefficients_descending"]
        == reversed_three_charpoly
        and spectral["noncyclic_reversal_changes_characteristic_polynomial"] is True
    )
    theorem = released["theorem_basis"]
    theorem_ok = (
        released["gate_status"] == "PASS_GENERAL_IDENTITY_METADATA_AND_THREE_EXACT_SPECIALIZATIONS"
        and theorem["name"] == "PERRON_CHARACTERISTIC_POLYNOMIAL_PROJECTIVE_TRACE_IDENTITY"
        and theorem["weight_telescope"]
        == "product of branch weights around the periodic word = lambda^(-(4+s))"
        and theorem["projective_denominator"] == "det_C(I-Dp_A)=chi_A'(lambda)/lambda^3"
        and theorem["trace_atom_simplification"]
        == "lambda^(-(4+s))/(chi_A'(lambda)/lambda^3)=lambda^(-(s+1))/chi_A'(lambda)"
        and theorem["complex_projective_dimension"] == 3
        and theorem["jacobian_weight_exponent"] == 4
        and theorem["general_identity_inferred_from_finite_examples"] is False
    )
    examples = released["examples"]
    if len(examples) != 3:
        return False, {}
    one_ok, one_summary = independent_perron_trace_check(
        examples[0], "gamma_star_one_return", SECTION_WORD, 1, gamma_matrix
    )
    two_ok, two_summary = independent_perron_trace_check(
        examples[1], "gamma_star_then_second_branch_two_returns", ORDERED_TWO_RETURN_WORD, 2, two_matrix
    )
    three_ok, three_summary = independent_perron_trace_check(
        examples[2],
        "gamma_star_then_second_then_third_three_returns",
        ORDERED_THREE_RETURN_WORD,
        3,
        three_matrix,
    )
    return bool(order_ok and spectral_order_ok and theorem_ok and one_ok and two_ok and three_ok), {
        "return_bridge_word": BRIDGE_WORD,
        "two_return_elementary_length": len(ORDERED_TWO_RETURN_WORD),
        "two_return_matrix_order_detectable": two_matrix != reversed_two,
        "two_return_charpoly_cyclically_invariant": two_charpoly == reversed_two_charpoly,
        "three_return_elementary_length": len(ORDERED_THREE_RETURN_WORD),
        "three_return_charpoly_order_detectable": three_charpoly != reversed_three_charpoly,
        "examples": [one_summary, two_summary, three_summary],
    }


def verify(certificate: dict[str, object]) -> tuple[dict[str, bool], dict[str, object]]:
    states, edges = rebuild_graph()
    graph_ok = certificate["graph"] == graph_payload(states, edges)

    branch = certificate["source_locked_branch"]
    base = states.index(SECTION)
    end, b_matrix, tokens = walk(base, SECTION_WORD, edges)
    r_matrix = transposed(b_matrix)
    gamma_decode, gamma_decode_end, gamma_terminal = replay_decoder(base, r_matrix, edges)
    gamma_ok = (
        branch["base_state"] == base == 4
        and branch["base_permutation"] == permutation_list(SECTION)
        and branch["eta"] == ETA_WORD
        and branch["gamma_star_word"] == SECTION_WORD
        and branch["gamma_star_word_sha256"] == hashlib.sha256(SECTION_WORD.encode("ascii")).hexdigest()
        and branch["gamma_star_length"] == 128
        and branch["start_state"] == branch["end_state"] == end == base
        and branch["closed"] is True
        and branch["edge_tokens"] == tokens
        and branch["chronology"] == "later elementary matrices multiply on the left"
        and branch["chronological_matrix_B"] == matrix_list(b_matrix)
        and branch["length_matrix_R_equals_B_transpose"] == matrix_list(r_matrix)
        and branch["determinant_B"] == int(sp.Matrix(b_matrix).det()) == 1
        and branch["entrywise_positive_B"] is True
        and min(flatten(b_matrix)) > 0
        and sp.Matrix(b_matrix) * form(SECTION) * sp.Matrix(b_matrix).T == form(SECTION)
        and branch["base_crossing_form"] == matrix_list(form(SECTION))
        and branch["closed_path_form_identity_verified"] is True
    )
    finite_gamma = branch["finite_gamma_star_decoder_replay"]
    gamma_decoder_ok = (
        finite_gamma["role"] == "FINITE_APPLICATION_WITNESS_REPLAY_NOT_ALL_LENGTH_PROOF"
        and gamma_decode == SECTION_WORD
        and finite_gamma["decoded_word"] == gamma_decode
        and finite_gamma["decoded_word_sha256"] == hashlib.sha256(gamma_decode.encode("ascii")).hexdigest()
        and finite_gamma["decoded_steps"] == len(gamma_decode) == 128
        and finite_gamma["end_state"] == gamma_decode_end == base
        and finite_gamma["terminal_identity"] is True
        and gamma_terminal == EYE
    )

    point = certificate["projective_point_witness"]
    raw_x = tuple(sum(r_matrix[row]) for row in range(4))
    x_scale = sum(raw_x)
    x0 = tuple(Fraction(value, x_scale) for value in raw_x)
    image = apply_matrix(r_matrix, x0)
    scale = sum(image, start=Fraction(0))
    coefficients = tuple(sum(r_matrix[row][column] for row in range(4)) for column in range(4))
    scale_from_coefficients = sum(
        (Fraction(coefficients[index]) * x0[index] for index in range(4)), start=Fraction(0)
    )
    jacobian = projective_jacobian(r_matrix, x0)
    point_ok = (
        point["branch_definition"] == "h_gamma(x)=R_gamma*x/S_gamma(x), R_gamma=B_gamma^T"
        and point["normalizer_definition"] == "S_gamma(x)=1^T*R_gamma*x"
        and point["normalizer_coefficients"] == list(coefficients)
        and point["x0_definition"] == "normalize(R_gamma_star*1)"
        and point["x0_unnormalized"] == list(raw_x)
        and point["x0_normalization"] == x_scale
        and vector_record(point["x0"]) == x0
        and point["x0_positive_simplex"] is True
        and min(x0) > 0
        and sum(x0, start=Fraction(0)) == 1
        and fraction_record(point["S_gamma_star_at_x0"]) == scale == scale_from_coefficients
        and point["S_positive"] is True
        and point["roof_at_x0"] == f"log({point['S_gamma_star_at_x0']['exact']})"
        and point["jacobian_dimension"] == 4
        and point["determinant_R"] == int(sp.Matrix(r_matrix).det()) == 1
        and fraction_record(point["J_gamma_star_at_x0"]) == jacobian == scale ** -4
        and point["direct_three_affine_coordinate_derivative_check"] is True
    )

    complex_cone_ok, complex_cone_summary = independent_complex_cone_gate(
        r_matrix, certificate["common_complex_domain_gate"]
    )
    periodic_trace_ok, periodic_trace_summary = independent_periodic_trace_gate(
        base, b_matrix, edges, certificate["scalar_periodic_trace_gate"]
    )

    theorem = certificate["point_evaluation_slice_theorem"]
    theorem_schema = theorem_schema_ok(theorem)
    sigma_zero = fraction_record(theorem["exact_registered_sigmas"]["0"]["coefficient_magnitude"])
    sigma_one = fraction_record(theorem["exact_registered_sigmas"]["1"]["coefficient_magnitude"])
    coefficient_ok = (
        sigma_zero == scale ** -4 == jacobian
        and sigma_one == scale ** -5 == jacobian / scale
        and theorem["exact_registered_sigmas"]["0"]["identity"] == "S^(-4)=J_gamma_star(x0)"
        and theorem["exact_registered_sigmas"]["1"]["identity"] == "S^(-5)=J_gamma_star(x0)/S"
        and theorem["exact_registered_sigmas"]["0"]["nonzero"] is True
        and theorem["exact_registered_sigmas"]["1"]["nonzero"] is True
        and theorem["parameter_domain"]["registered_exact_sigma_values"] == [0, 1]
        and theorem["parameter_domain"]["magnitude_independent_of_t"] is True
        and theorem["parameter_domain"]["C25_source_half_plane"] == "Re(s)>-sigma_0"
    )

    scope = certificate["scope_firewall"]
    scope_ok = (
        scope["flags"] == EXPECTED_SCOPE_FLAGS
        and len(scope["not_claimed"]) >= 6
        and certificate["decisions"]["holomorphic_space_constructed_by_exact_code"] is False
        and certificate["decisions"]["scalar_Bergman_theorem_status"]
        == "PROVED_IN_THEOREM_PACKAGE_NOT_BY_FINITE_CERTIFICATE"
        and certificate["decisions"]["ordinary_scalar_Fredholm_status"]
        == "PROVED_IN_THEOREM_PACKAGE_NOT_BY_FINITE_CERTIFICATE"
        and certificate["decisions"]["ordinary_holomorphic_metaplectic_Fredholm_authorized"] is False
        and certificate["decisions"]["route_B_authorized"] is False
    )

    released_sentinel = certificate["finite_decoder_sentinel"]
    replayed_sentinel = sentinel_replay(states.index(SEED), edges, int(released_sentinel["max_elementary_length"]))
    sentinel_ok = (
        released_sentinel == replayed_sentinel
        and released_sentinel["max_elementary_length"] <= 20
        and released_sentinel["finite_enumeration_is_proof"] is False
        and released_sentinel["finite_enumeration_is_branch_completeness_claim"] is False
        and released_sentinel["all_length_decoder_dependency_replaced"] is False
        and released_sentinel["collision_count"] == 0
    )

    checks = {
        "literal_seven_state_fourteen_edge_graph": bool(graph_ok),
        "state4_gamma_star_later_left_B_and_transposed_R": bool(gamma_ok),
        "finite_gamma_star_decoder_application_witness_only": bool(gamma_decoder_ok),
        "exact_x0_normalizer_and_dimension_four_jacobian": bool(point_ok),
        "positive_prefix_column_hull_margin_and_birkhoff_ratio": bool(complex_cone_ok),
        "complex_dimension_three_principal_right_half_plane_metadata": bool(
            complex_cone_ok
            and certificate["common_complex_domain_gate"]["complex_projective_metadata"]
            ["normalized_complex_projective_dimension"]
            == 3
            and certificate["common_complex_domain_gate"]["principal_log_metadata"]["no_branchwise_log_choice"]
            is True
        ),
        "one_two_and_spectral_three_return_characteristic_polynomials": bool(periodic_trace_ok),
        "perron_projective_denominator_and_trace_atom_simplification": bool(periodic_trace_ok),
        "sigma_zero_and_one_single_branch_coefficient_floors": bool(coefficient_ok),
        "conditional_slice_assumption_chain_complete": bool(theorem_schema),
        "external_C24_C25_theorems_not_claimed_reproved": bool(
            theorem["external_theorems_reproved_here"] is False
            and scope["flags"]["c24_atomic_theorem_reproved"] is False
            and scope["flags"]["c25_all_length_decoder_reproved"] is False
        ),
        "no_collision_or_central_sign_averaging": bool(
            scope["flags"]["projected_matrix_collisions_ignored"] is False
            and scope["flags"]["central_signs_averaged"] is False
            and scope["flags"]["branch_chronology_averaged"] is False
        ),
        "finite_length_20_sentinel_replayed_as_nonproof": bool(sentinel_ok),
        "claim_scope_firewall": bool(scope_ok),
    }
    summary = {
        "state_count": len(states),
        "edge_count": len(edges),
        "base_state": base,
        "gamma_star_length": len(SECTION_WORD),
        "S_gamma_star_at_x0": str(scale),
        "J_gamma_star_at_x0": str(jacobian),
        "sigma_0_floor": str(sigma_zero),
        "sigma_1_floor": str(sigma_one),
        "common_complex_domain_gate": complex_cone_summary,
        "scalar_periodic_trace_gate": periodic_trace_summary,
        "sentinel_max_length": released_sentinel["max_elementary_length"],
        "sentinel_first_returns": released_sentinel["total_first_returns"],
        "sentinel_distinct_matrices": released_sentinel["distinct_chronological_matrices"],
        "sentinel_digest": released_sentinel["canonical_word_matrix_sha256"],
    }
    return checks, summary


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    checks, summary = verify(certificate)
    passed = all(checks.values())
    result = {
        "material_passport": {
            "origin": "independent HCS-C26 checker",
            "origin_mode": "validate",
            "origin_date": "2026-08-10",
            "verification_status": "VERIFIED" if passed else "FAILED",
            "version_label": "c26_independent_check_v1",
        },
        "certificate": portable(args.certificate),
        "certificate_sha256": digest_file(args.certificate),
        "producer_imported": False,
        "external_theorems_reproved": False,
        "passed": passed,
        "checks": checks,
        "summary": summary,
        "runtime": {"python": platform.python_version(), "sympy": sp.__version__},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"passed": passed, "checks": checks, "summary": summary}, separators=(",", ":")))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
