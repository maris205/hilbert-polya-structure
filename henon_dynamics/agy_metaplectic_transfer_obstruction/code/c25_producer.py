#!/usr/bin/env python3
"""Produce the exact HCS-C25 AGY source-lock and Rauzy decoder certificate.

The script rebuilds the labeled seven-state Rauzy class from the literal
permutation.  It keeps every elementary arrow and uses the AGY convention

    B_e = I + E_(loser,winner),
    B_(e_1...e_n) = B_(e_n) ... B_(e_1).

No transition matrix is averaged.  The length matrix is R=B^T, so the first
arrow acts on the left of R and is peeled by an exact winner-row subtraction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from collections import deque
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c25_certificate.json"
ALPHABET = (1, 2, 3, 4)
MOVE_TYPES = ("t", "b")
INITIAL = ((1, 2, 3, 4), (4, 3, 2, 1))
AGY_BASE = ((1, 3, 4, 2), (4, 3, 2, 1))
ETA = "tbttbtbb"
GAMMA_STAR = "t" * 64 + ETA * 8
STRONG_POSITIVITY_THRESHOLD = 3 * len(ALPHABET) - 4
IDENTITY = tuple(tuple(int(row == column) for column in range(4)) for row in range(4))

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
IntMatrix = tuple[tuple[int, ...], ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--stress-max-length", type=int, default=22)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_json(matrix: IntMatrix | sp.Matrix) -> list[list[int]]:
    if isinstance(matrix, sp.MatrixBase):
        return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]
    return [list(row) for row in matrix]


def as_sympy(matrix: IntMatrix) -> sp.Matrix:
    return sp.Matrix(matrix)


def transpose(matrix: IntMatrix) -> IntMatrix:
    return tuple(tuple(matrix[column][row] for column in range(4)) for row in range(4))


def matmul(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(4)) for column in range(4))
        for row in range(4)
    )


def matrix_sum(matrix: IntMatrix) -> int:
    return sum(sum(row) for row in matrix)


def edge_matrix(winner: int, loser: int) -> IntMatrix:
    rows = [list(row) for row in IDENTITY]
    rows[loser - 1][winner - 1] += 1
    return tuple(tuple(row) for row in rows)


def rational_json(value: sp.Rational) -> dict[str, int | str]:
    value = sp.Rational(value)
    return {
        "numerator": int(value.p),
        "denominator": int(value.q),
        "exact": str(value),
    }


def vector_rational_json(vector: sp.Matrix) -> list[dict[str, int | str]]:
    return [rational_json(sp.Rational(value)) for value in vector]


def normalize(vector: sp.Matrix) -> tuple[sp.Matrix, sp.Rational]:
    scale = sp.Rational(sum(vector))
    if scale <= 0:
        raise ValueError("normalization scale must be positive")
    return vector / scale, scale


def permutation_json(permutation: Permutation) -> dict[str, list[int]]:
    return {"top": list(permutation[0]), "bottom": list(permutation[1])}


def omega(permutation: Permutation) -> sp.Matrix:
    """Yoccoz crossing form in the fixed label order."""

    top, bottom = permutation
    top_at = {letter: index for index, letter in enumerate(top)}
    bottom_at = {letter: index for index, letter in enumerate(bottom)}
    result = sp.zeros(4)
    for alpha in ALPHABET:
        for beta in ALPHABET:
            if top_at[alpha] < top_at[beta] and bottom_at[alpha] > bottom_at[beta]:
                result[alpha - 1, beta - 1] = 1
            elif top_at[alpha] > top_at[beta] and bottom_at[alpha] < bottom_at[beta]:
                result[alpha - 1, beta - 1] = -1
    return result


def rauzy_move(permutation: Permutation, move_type: str) -> tuple[Permutation, int, int, IntMatrix]:
    if move_type not in MOVE_TYPES:
        raise ValueError("move type must be t or b")
    top, bottom = [list(row) for row in permutation]
    top_right, bottom_right = top[-1], bottom[-1]
    if move_type == "t":
        winner, loser = top_right, bottom_right
        bottom.remove(loser)
        bottom.insert(bottom.index(winner) + 1, loser)
    else:
        winner, loser = bottom_right, top_right
        top.remove(loser)
        top.insert(top.index(winner) + 1, loser)
    return (tuple(top), tuple(bottom)), winner, loser, edge_matrix(winner, loser)


def build_graph() -> tuple[list[Permutation], dict[tuple[int, str], dict[str, object]]]:
    discovered = {INITIAL}
    queue: deque[Permutation] = deque([INITIAL])
    while queue:
        source = queue.popleft()
        for move_type in MOVE_TYPES:
            target, _, _, _ = rauzy_move(source, move_type)
            if target not in discovered:
                discovered.add(target)
                queue.append(target)

    states = sorted(discovered)
    state_id = {state: index for index, state in enumerate(states)}
    edges: dict[tuple[int, str], dict[str, object]] = {}
    for source in states:
        source_id = state_id[source]
        for move_type in MOVE_TYPES:
            target, winner, loser, matrix = rauzy_move(source, move_type)
            target_id = state_id[target]
            assert as_sympy(matrix) * omega(source) * as_sympy(matrix).T == omega(target)
            edges[(source_id, move_type)] = {
                "source": source_id,
                "type": move_type,
                "target": target_id,
                "winner": winner,
                "loser": loser,
                "matrix": matrix,
            }
    assert len(states) == 7 and len(edges) == 14
    assert state_id[INITIAL] == 2 and state_id[AGY_BASE] == 4
    return states, edges


def follow_word(
    start_state: int,
    word: str,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[int, IntMatrix, list[dict[str, int | str]]]:
    current = start_state
    matrix = IDENTITY
    tokens: list[dict[str, int | str]] = []
    for index, move_type in enumerate(word):
        edge = edges[(current, move_type)]
        edge_value = edge["matrix"]
        assert isinstance(edge_value, tuple)
        matrix = matmul(edge_value, matrix)
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
    return current, matrix, tokens


def row_difference(matrix: IntMatrix, winner: int, loser: int) -> tuple[int, ...]:
    return tuple(matrix[winner - 1][column] - matrix[loser - 1][column] for column in range(4))


def candidate_row_tests(
    state: int,
    matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
) -> list[dict[str, object]]:
    tests = []
    for move_type in MOVE_TYPES:
        edge = edges[(state, move_type)]
        winner, loser = int(edge["winner"]), int(edge["loser"])
        difference = row_difference(matrix, winner, loser)
        tests.append(
            {
                "type": move_type,
                "winner": winner,
                "loser": loser,
                "difference_winner_minus_loser": list(difference),
                "componentwise_dominance": all(value >= 0 for value in difference),
            }
        )
    return tests


def decode_length_matrix(
    start_state: int,
    matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
    *,
    include_matrices: bool,
    max_steps: int = 100_000,
) -> dict[str, object]:
    """Invert R_word=B_word^T by winner-row subtraction."""

    current = start_state
    remaining = matrix
    decoded: list[str] = []
    trace: list[dict[str, object]] = []
    while remaining != IDENTITY:
        if len(decoded) >= max_steps:
            raise ValueError("decoder exceeded the certified step bound")
        tests = candidate_row_tests(current, remaining, edges)
        admissible = [row for row in tests if bool(row["componentwise_dominance"])]
        if len(admissible) != 1:
            raise ValueError(f"decoder ambiguity/failure at state {current}: {tests}")
        chosen = admissible[0]
        move_type = str(chosen["type"])
        winner, loser = int(chosen["winner"]), int(chosen["loser"])
        before_sum = matrix_sum(remaining)
        loser_row_sum = sum(remaining[loser - 1])
        rows = [list(row) for row in remaining]
        rows[winner - 1] = list(chosen["difference_winner_minus_loser"])
        peeled = tuple(tuple(row) for row in rows)
        after_sum = matrix_sum(peeled)
        edge = edges[(current, move_type)]
        target = int(edge["target"])
        if any(value < 0 for row in peeled for value in row):
            raise ValueError("row peel left the nonnegative cone")
        if not (before_sum > after_sum and before_sum - after_sum == loser_row_sum > 0):
            raise ValueError("matrix-entry sum did not decrease by the loser-row sum")
        row: dict[str, object] = {
            "step": len(decoded),
            "state_before": current,
            "candidate_tests": tests,
            "chosen_type": move_type,
            "winner": winner,
            "loser": loser,
            "state_after": target,
            "sum_before": before_sum,
            "sum_after": after_sum,
            "strict_drop": before_sum - after_sum,
            "loser_row_sum": loser_row_sum,
            "nonnegative_after": True,
        }
        if include_matrices:
            row["matrix_before"] = matrix_json(remaining)
            row["matrix_after"] = matrix_json(peeled)
        trace.append(row)
        decoded.append(move_type)
        current = target
        remaining = peeled
    return {
        "decoded_word": "".join(decoded),
        "end_state": current,
        "steps": len(decoded),
        "terminal_matrix": matrix_json(remaining),
        "trace": trace,
    }


def proper_border_lengths(word: str) -> list[int]:
    return [length for length in range(1, len(word)) if word[:length] == word[-length:]]


def initial_constant_run_length(word: str) -> int:
    if not word:
        return 0
    first = word[0]
    return next((index for index, letter in enumerate(word) if letter != first), len(word))


def winner_set_for_subword(tokens: Sequence[dict[str, int | str]], start: int, stop: int) -> list[int]:
    return sorted({int(token["winner"]) for token in tokens[start:stop]})


def first_return_series(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
    central_state: int,
) -> sp.Expr:
    z = sp.symbols("z")
    internal = [state for state in range(len(states)) if state != central_state]
    position = {state: index for index, state in enumerate(internal)}
    q = sp.zeros(len(internal))
    outgoing = sp.zeros(len(internal), 1)
    incoming = sp.zeros(len(internal), 1)
    direct = 0
    for move_type in MOVE_TYPES:
        target = int(edges[(central_state, move_type)]["target"])
        if target == central_state:
            direct += 1
        else:
            outgoing[position[target], 0] += 1
    for source in internal:
        for move_type in MOVE_TYPES:
            target = int(edges[(source, move_type)]["target"])
            if target == central_state:
                incoming[position[source], 0] += 1
            else:
                q[position[source], position[target]] += 1
    return sp.factor(direct * z + z**2 * (outgoing.T * (sp.eye(len(internal)) - z * q).inv() * incoming)[0])


def fibonacci(index: int) -> int:
    if index <= 0:
        return 0
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def first_return_stress(
    central_state: int,
    edges: dict[tuple[int, str], dict[str, object]],
    max_length: int,
) -> dict[str, object]:
    if max_length < 3:
        raise ValueError("stress maximum must include the shortest returns")
    stack: list[tuple[int, str, IntMatrix]] = [(central_state, "", IDENTITY)]
    rows: list[tuple[str, IntMatrix]] = []
    while stack:
        state, word, matrix = stack.pop()
        if len(word) == max_length:
            continue
        for move_type in reversed(MOVE_TYPES):
            edge = edges[(state, move_type)]
            edge_value = edge["matrix"]
            assert isinstance(edge_value, tuple)
            next_matrix = matmul(edge_value, matrix)
            next_word = word + move_type
            target = int(edge["target"])
            if target == central_state:
                rows.append((next_word, next_matrix))
            else:
                stack.append((target, next_word, next_matrix))

    rows.sort(key=lambda item: (len(item[0]), item[0]))
    counts: dict[str, int] = {}
    matrix_to_word: dict[tuple[int, ...], str] = {}
    digest = hashlib.sha256()
    decoded_count = 0
    samples = []
    for word, forward in rows:
        counts[str(len(word))] = counts.get(str(len(word)), 0) + 1
        length_matrix = transpose(forward)
        flat = tuple(value for row in forward for value in row)
        if flat in matrix_to_word:
            raise AssertionError(f"stress-test matrix collision: {matrix_to_word[flat]} and {word}")
        matrix_to_word[flat] = word
        decoded = decode_length_matrix(central_state, length_matrix, edges, include_matrices=False)
        if decoded["decoded_word"] != word or decoded["end_state"] != central_state:
            raise AssertionError(f"decoder stress failure for {word}")
        decoded_count += 1
        line = f"{word}|{','.join(str(value) for value in flat)}\n"
        digest.update(line.encode("ascii"))
        if len(samples) < 12:
            samples.append({"word": word, "forward_matrix": matrix_json(forward)})

    expected = {str(length): 2 * fibonacci(length - 2) for length in range(3, max_length + 1)}
    if counts != expected:
        raise AssertionError(f"first-return recurrence mismatch: {counts} != {expected}")
    return {
        "role": "NON_PROOF_DIAGNOSTIC_AND_MUTATION_SENTINEL",
        "logical_basis": "the all-length decoder theorem, not this finite stress window",
        "max_elementary_length": max_length,
        "count_by_length": counts,
        "expected_count_formula": "2*F_(n-2), F_1=F_2=1",
        "total_first_returns": len(rows),
        "decoded_exactly": decoded_count,
        "distinct_forward_matrices": len(matrix_to_word),
        "collision_count": len(rows) - len(matrix_to_word),
        "canonical_word_matrix_sha256": digest.hexdigest(),
        "samples": samples,
    }


def projective_jacobian_at(length_matrix: sp.Matrix, point: sp.Matrix) -> sp.Rational:
    """Exact 3-coordinate simplex Jacobian of x -> R x / |R x|_1."""

    tangent = sp.Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [-1, -1, -1],
        ]
    )
    numerator = length_matrix * point
    scale = sp.Rational(sum(numerator))
    derivative_numerator = length_matrix * tangent
    derivative_scale = sp.ones(1, 4) * derivative_numerator
    derivative = (derivative_numerator * scale - numerator * derivative_scale) / scale**2
    return sp.factor(derivative[:3, :].det())


def graph_certificate(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    state_rows = []
    for state_id, state in enumerate(states):
        state_rows.append(
            {
                "id": state_id,
                **permutation_json(state),
                "omega": matrix_json(omega(state)),
                "omega_determinant": int(omega(state).det()),
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
    return {"state_count": len(state_rows), "edge_count": len(edge_rows), "states": state_rows, "edges": edge_rows}


def symplectic_trivialization(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    """Trivialize all state fibers over the state-4 inverse crossing form."""

    base_state = states.index(AGY_BASE)
    base_form = omega(states[base_state]).inv()
    frames: dict[int, sp.Matrix] = {base_state: sp.eye(4)}
    parents: dict[int, tuple[int, str] | None] = {base_state: None}
    queue: deque[int] = deque([base_state])
    while queue:
        source = queue.popleft()
        for move_type in MOVE_TYPES:
            edge = edges[(source, move_type)]
            target = int(edge["target"])
            if target in frames:
                continue
            matrix = sp.Matrix(edge["matrix"])
            frames[target] = matrix * frames[source]
            parents[target] = (source, move_type)
            queue.append(target)
    if set(frames) != set(range(len(states))):
        raise AssertionError("deterministic spanning tree did not reach every state")

    frame_rows = []
    for state in range(len(states)):
        frame = frames[state]
        state_form = omega(states[state]).inv()
        parent = parents[state]
        integral = all(sp.denom(entry) == 1 for entry in frame)
        determinant = int(frame.det())
        verified = frame.T * state_form * frame == base_form
        assert integral and determinant == 1 and verified
        parent_row = None
        if parent is not None:
            parent_source, parent_type = parent
            parent_row = {
                "source": parent_source,
                "type": parent_type,
                "target": state,
            }
        frame_rows.append(
            {
                "state": state,
                "frame_S": matrix_json(frame),
                "determinant": determinant,
                "integral": integral,
                "parent_tree_edge": parent_row,
                "frame_identity": "S_pi^T*J_pi*S_pi=J0",
                "frame_identity_verified": verified,
            }
        )

    fixed_edges = []
    identity_count = 0
    for source in range(len(states)):
        for move_type in MOVE_TYPES:
            edge = edges[(source, move_type)]
            target = int(edge["target"])
            matrix = sp.Matrix(edge["matrix"])
            fixed = frames[target].inv() * matrix * frames[source]
            integral = all(sp.denom(entry) == 1 for entry in fixed)
            determinant = int(fixed.det())
            verified = fixed.T * base_form * fixed == base_form
            is_identity = fixed == sp.eye(4)
            is_tree_edge = parents[target] == (source, move_type)
            assert integral and determinant == 1 and verified
            if is_tree_edge:
                assert is_identity
            identity_count += int(is_identity)
            fixed_edges.append(
                {
                    "source": source,
                    "type": move_type,
                    "target": target,
                    "g_edge_equals_S_target_inverse_B_edge_S_source": matrix_json(fixed),
                    "determinant": determinant,
                    "integral": integral,
                    "spanning_tree_edge": is_tree_edge,
                    "identity_matrix": is_identity,
                    "fixed_form_identity": "g_e^T*J0*g_e=J0",
                    "fixed_form_identity_verified": verified,
                }
            )

    return {
        "base_state": base_state,
        "base_permutation": permutation_json(states[base_state]),
        "base_form_J0": matrix_json(base_form),
        "state_form_definition": "J_pi=Omega_pi^(-1)",
        "frame_direction": "S_pi maps fixed base coordinates to the state-pi coordinates",
        "frame_identity": "S_pi^T*J_pi*S_pi=J0",
        "construction": "deterministic breadth-first spanning tree rooted at state 4; outgoing move order t,b; S_target=B_edge*S_source",
        "state_frames": frame_rows,
        "fixed_fiber_edge_definition": "g_e=S_target^(-1)*B_e*S_source",
        "fixed_fiber_edges": fixed_edges,
        "counts": {
            "state_frames": len(frame_rows),
            "fixed_fiber_edges": len(fixed_edges),
            "identity_fixed_edges": identity_count,
            "nonidentity_fixed_edges": len(fixed_edges) - identity_count,
        },
        "metaplectic_lift_scope": {
            "proved": "every released integral fixed-fiber edge matrix g_e is symplectic and therefore has two metaplectic lifts; choosing one lift for each labeled directed edge and multiplying in chronology defines pathwise coherent lifts",
            "not_done": "the certificate makes no numerical choice of either central lift and never identifies the two signs",
            "group_section_not_claimed": "no global multiplicative section Sp(4,Z)->Mp(4,R) is asserted",
        },
    }


def agy_witness(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    state_id = {state: index for index, state in enumerate(states)}
    base = state_id[AGY_BASE]
    eta_end, eta_matrix, eta_tokens = follow_word(base, ETA, edges)
    gamma_end, gamma_matrix, gamma_tokens = follow_word(base, GAMMA_STAR, edges)
    assert eta_end == base and gamma_end == base

    boundaries = [(0, 64 + len(ETA))] + [
        (64 + block * len(ETA), 64 + (block + 1) * len(ETA)) for block in range(1, 8)
    ]
    complete_blocks = []
    for index, (start, stop) in enumerate(boundaries, start=1):
        winners = winner_set_for_subword(gamma_tokens, start, stop)
        complete_blocks.append(
            {
                "block": index,
                "start_inclusive": start,
                "stop_exclusive": stop,
                "word": GAMMA_STAR[start:stop],
                "winner_set": winners,
                "complete": winners == list(ALPHABET),
            }
        )
    assert len(complete_blocks) == 8 and all(bool(row["complete"]) for row in complete_blocks)

    borders = proper_border_lengths(GAMMA_STAR)
    initial_run = initial_constant_run_length(GAMMA_STAR)
    assert not borders
    assert initial_run == 65
    b_matrix = as_sympy(gamma_matrix)
    r_matrix = b_matrix.T
    base_omega = omega(AGY_BASE)
    inverse_form = base_omega.inv()
    assert b_matrix.det() == 1
    assert all(value > 0 for value in b_matrix)
    assert b_matrix * base_omega * b_matrix.T == base_omega
    assert b_matrix.T * inverse_form * b_matrix == inverse_form

    ones = sp.ones(4, 1)
    x_raw = r_matrix * ones
    x0, x_scale = normalize(x_raw)
    y_raw = r_matrix * x0
    y0, roof_scale = normalize(y_raw)
    jacobian = projective_jacobian_at(r_matrix, x0)
    expected_jacobian = sp.factor(roof_scale ** (-4))
    assert jacobian == expected_jacobian
    s_coefficients = sp.Matrix((sp.ones(1, 4) * r_matrix).T)
    coefficient_values = [int(value) for value in s_coefficients]

    decoded = decode_length_matrix(base, transpose(gamma_matrix), edges, include_matrices=True)
    assert decoded["decoded_word"] == GAMMA_STAR
    assert decoded["end_state"] == base

    eta_winners = sorted({int(token["winner"]) for token in eta_tokens})
    eta_losers = sorted({int(token["loser"]) for token in eta_tokens})
    return {
        "base_state": base,
        "base_permutation": permutation_json(AGY_BASE),
        "eta": {
            "word": ETA,
            "length": len(ETA),
            "closed": eta_end == base,
            "edge_tokens": eta_tokens,
            "winner_set": eta_winners,
            "loser_set": eta_losers,
            "complete": eta_winners == list(ALPHABET),
            "chronological_matrix": matrix_json(eta_matrix),
        },
        "gamma_star": {
            "compressed_word": "t^64 (tbttbtbb)^8",
            "word": GAMMA_STAR,
            "word_sha256": hashlib.sha256(GAMMA_STAR.encode("ascii")).hexdigest(),
            "length": len(GAMMA_STAR),
            "start_state": base,
            "end_state": gamma_end,
            "closed": gamma_end == base,
            "edge_tokens": gamma_tokens,
            "complete_block_count": len(complete_blocks),
            "complete_blocks": complete_blocks,
            "k_complete": 8,
            "strong_positivity_criterion": {
                "criterion": "AGY: k-complete with k >= 3*d-4 is strongly positive",
                "alphabet_size_d": len(ALPHABET),
                "threshold_3d_minus_4": STRONG_POSITIVITY_THRESHOLD,
                "k": 8,
                "criterion_met": 8 >= STRONG_POSITIVITY_THRESHOLD,
                "direct_entrywise_positive_matrix_check": True,
            },
            "neatness": {
                "declared_AGY_sufficient_shape": "initial constant-type run has at least half the word length and terminal type differs",
                "initial_type": "t",
                "initial_constant_run_length": initial_run,
                "initial_constant_run_computation": "maximal prefix scan of the released word; eta begins with t, so t^64 extends to 65",
                "at_least_half_of_word": initial_run * 2 >= len(GAMMA_STAR),
                "terminal_type": GAMMA_STAR[-1],
                "terminal_differs_from_initial": GAMMA_STAR[-1] != GAMMA_STAR[0],
                "proper_border_lengths": borders,
                "no_nonempty_proper_border": not borders,
                "neat_certificate_passed": initial_run * 2 >= len(GAMMA_STAR) and GAMMA_STAR[-1] != GAMMA_STAR[0] and not borders,
            },
            "chronological_matrix_B": matrix_json(gamma_matrix),
            "length_matrix_R_equals_B_transpose": matrix_json(transpose(gamma_matrix)),
            "determinant": int(b_matrix.det()),
            "entrywise_positive": all(value > 0 for value in b_matrix),
            "form_transport": {
                "omega_base": matrix_json(base_omega),
                "inverse_form_J": matrix_json(inverse_form),
                "homology_identity": "B*Omega_base*B^T=Omega_base",
                "homology_identity_verified": True,
                "inverse_form_identity": "B^T*J*B=J",
                "inverse_form_identity_verified": True,
            },
            "decoder": decoded,
        },
        "projective_inverse_branch": {
            "definition": "h_gamma(x)=R*x/S_gamma(x), R=B_gamma^T",
            "normalizer": "S_gamma(x)=1^T*R*x",
            "normalizer_coefficients_on_simplex": coefficient_values,
            "normalizer_essential_range_open_simplex": {
                "infimum": min(coefficient_values),
                "supremum": max(coefficient_values),
            },
            "x0_definition": "normalize(B_gamma^T*1)",
            "x0_unnormalized": [int(value) for value in x_raw],
            "x0_normalization": int(x_scale),
            "x0": vector_rational_json(x0),
            "y0_definition": "h_gamma(x0)=normalize(B_gamma^T*x0)",
            "y0": vector_rational_json(y0),
            "x0_positive_simplex": all(value > 0 for value in x0) and sum(x0) == 1,
            "y0_positive_simplex": all(value > 0 for value in y0) and sum(y0) == 1,
            "roof": {
                "definition": "r_gamma(x)=log(S_gamma(x))",
                "exp_r_at_x0": rational_json(roof_scale),
                "r_at_x0": f"log({roof_scale})",
            },
            "jacobian": {
                "dimension_d": 4,
                "formula": "J_gamma(x)=det(R)/S_gamma(x)^4=exp(-4*r_gamma(x))",
                "det_R": int(r_matrix.det()),
                "at_x0": rational_json(jacobian),
                "at_x0_power_certificate": {
                    "base_numerator": int(sp.Rational(1 / roof_scale).p),
                    "base_denominator": int(sp.Rational(1 / roof_scale).q),
                    "power": 4,
                },
                "direct_three_coordinate_derivative_check": True,
            },
        },
    }


def toy_ttt(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> dict[str, object]:
    central = states.index(INITIAL)
    end, forward, tokens = follow_word(central, "ttt", edges)
    assert end == central
    length_matrix = transpose(forward)
    expected = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 1, 1, 1),
    )
    assert length_matrix == expected
    return {
        "scope": "TOY_CENTRAL_RETURN_SANITY_CHECK_NOT_THE_AGY_GAMMA_STAR_SECTION_BRANCH",
        "start_state": central,
        "word": "ttt",
        "closed": end == central,
        "edge_tokens": tokens,
        "chronological_matrix_B": matrix_json(forward),
        "length_matrix_R": matrix_json(length_matrix),
        "normalizer_on_simplex": "S_ttt(x)=2-x_4",
        "inverse_branch": "h_ttt(x)=(x_1,x_2,x_3,1)/(2-x_4)",
        "cylinder": "{y in Delta: y_4>1/2}",
        "jacobian": "(2-x_4)^(-4)=exp(-4*r_ttt)",
        "canonical_AGY_application_claimed": False,
    }


def decoder_theorem_metadata() -> dict[str, object]:
    return {
        "name": "FIXED_START_ALL_LENGTH_RAUZY_MATRIX_INJECTIVITY",
        "status": "EXACT_INDUCTIVE_THEOREM_CERTIFICATE",
        "statement": "For a fixed labeled starting permutation, every finite directed Rauzy path is uniquely determined by its chronological matrix B.",
        "length_matrix_convention": "R=B^T=R_first*...*R_last with R_e=I+E_(winner,loser)",
        "first_edge_invariant": "For the true first edge, row_w(R)-row_l(R)=row_w(R_rest), componentwise nonnegative and nonzero.",
        "uniqueness_argument": "The two candidates reverse the same rightmost label pair. If both winner rows dominated, the two rows would be equal; an image matrix is unimodular, so this is impossible.",
        "peel_operation": "Replace row_w by row_w-row_l, equivalently R <- R_e^(-1) R, then advance the labeled permutation.",
        "cone_invariant": "The peeled matrix is a nonnegative integral unimodular path matrix.",
        "termination_measure": "The sum of all entries drops by the strictly positive loser-row sum at every peel and ends at sum(I)=4.",
        "proof_method": "Induction on the entry sum; the algorithm is a two-sided inverse on the image of the fixed-start path-matrix map.",
        "scope": "fixed labeled start state and the full labeled Rauzy matrix are required; neither the state nor chronology may be discarded",
        "projection_scope": {
            "full_matrix_theorem": "injectivity is first proved for the full four-by-four labeled Rauzy matrix B",
            "current_absolute_homology_application": "at every state of this H(2) class det(Omega)=1, hence Omega has full rank and relative homology equals absolute homology; a fixed symplectic basis change loses no matrix information",
            "general_warning": "for a Rauzy class with a nontrivial relative-homology kernel, injectivity after projection to absolute homology does not follow from this decoder",
        },
        "consequences": [
            "all finite fixed-start path matrices are collision-free",
            "central first-return matrices are pairwise distinct at every length",
            "concatenated central return branches decode and segment uniquely",
            "the central-return matrix monoid is free on its countable first-return generators",
            "in this full-rank four-letter H(2) class, same-absolute-homology-matrix metaplectic cancellation cannot occur between distinct fixed-start branches",
        ],
        "finite_enumeration_is_proof_basis": False,
    }


def make_certificate(stress_max_length: int) -> dict[str, object]:
    states, edges = build_graph()
    state_id = {state: index for index, state in enumerate(states)}
    central = state_id[INITIAL]
    series = first_return_series(states, edges, central)
    z = sp.symbols("z")
    expected_series = 2 * z**3 / (1 - z - z**2)
    assert sp.cancel(series - expected_series) == 0
    witness = agy_witness(states, edges)
    stress = first_return_stress(central, edges, stress_max_length)
    return {
        "schema": "HCS-C25-AGY-METAPLECTIC-SOURCE-LOCK-v2",
        "material_passport": {
            "origin": "HCS-C25 frozen experiment plan",
            "origin_mode": "exact_producer",
            "origin_date": "2026-08-10T00:00:00Z",
            "verification_status": "UNVERIFIED_UNTIL_INDEPENDENT_CHECK",
            "version_label": "c25_exact_certificate_v2",
        },
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "producer_sha256": sha256(Path(__file__)),
        },
        "source_lock": {
            "alphabet": list(ALPHABET),
            "literal_seed": permutation_json(INITIAL),
            "central_state": central,
            "agy_base_state": state_id[AGY_BASE],
            "agy_base_permutation": permutation_json(AGY_BASE),
            "matrix_convention": "B_e=I+E_(loser,winner)",
            "chronology": "B_word=B_last*...*B_first; later arrows multiply on the left",
            "length_matrix": "R_word=B_word^T=R_first*...*R_last",
            "averaged_transition_matrix_used": False,
            "prime_or_riemann_zero_data_used": False,
            "cutoff_or_heat_smoothing_used": False,
        },
        "graph": graph_certificate(states, edges),
        "statewise_symplectic_trivialization": symplectic_trivialization(states, edges),
        "all_length_decoder_theorem": decoder_theorem_metadata(),
        "central_first_return_language": {
            "top_family_regex": "t (b t* b)* t b* t",
            "bottom_family_regex": "b (t b* t)* b t* b",
            "union_prefix_free": True,
            "generating_function": str(series),
            "generating_function_canonical": "2*z^3/(1-z-z^2)",
            "coefficient_formula": "number at elementary length n is 2*F_(n-2)",
            "derivation": "exact Schur-complement/state-elimination of the six noncentral states",
        },
        "agy_section_witness": witness,
        "central_return_toy": toy_ttt(states, edges),
        "finite_stress_test": stress,
        "operator_application": {
            "canonical_map": "source-locked AGY first-return section determined by gamma_star",
            "raw_C1_branch_scalar_at_x0": "exp(-(s+4)*r_gamma(x0)); nonzero for every finite complex s",
            "raw_C1_exact_compression": "C1 bump inside the gamma cylinder plus evaluation isolates the scalar times the infinite-dimensional metaplectic unitary",
            "normalized_L2_application": "uses the AGY invariant-density branch probabilities; it is not identified with the toy ttt Lebesgue half-density formula",
            "bounded_or_noncompact_dichotomy": "in the registered bounded AGY realizations, one nonzero unitary branch compression forbids compactness and nuclearity",
            "collision_escape": "closed by the fixed-start all-length decoder theorem",
            "metaplectic_edge_lifts": "after the verified statewise trivialization, every labeled fixed-fiber symplectic edge admits two lifts; edge choices may be composed pathwise, but no central signs are selected numerically",
            "ordinary_fredholm_determinant": "REJECTED_ON_THE_REGISTERED_UNSMOOTHED_C1_AND_NORMALIZED_L2_REALIZATIONS",
            "remaining_scope": "holomorphic/anisotropic spaces without bounded branch localizers, generalized traces, semifinite determinants, or geometrically forced continuous smoothing remain open",
        },
        "decisions": {
            "source_lock": "PASS_PENDING_INDEPENDENT_REPLAY",
            "agy_gamma_star_closed_complete_positive_neat": "PASS_PENDING_INDEPENDENT_REPLAY",
            "all_length_matrix_collision_escape": "REFUTED_BY_EXACT_DECODER_THEOREM",
            "finite_length_13_ledger_used": False,
            "route_b_authorized": False,
        },
    }


def main() -> None:
    args = parse_args()
    certificate = make_certificate(args.stress_max_length)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": sha256(args.output),
                "states": certificate["graph"]["state_count"],
                "gamma_length": certificate["agy_section_witness"]["gamma_star"]["length"],
                "gamma_positive": certificate["agy_section_witness"]["gamma_star"]["entrywise_positive"],
                "state_frames": certificate["statewise_symplectic_trivialization"]["counts"]["state_frames"],
                "fixed_fiber_edges": certificate["statewise_symplectic_trivialization"]["counts"]["fixed_fiber_edges"],
                "identity_fixed_fiber_edges": certificate["statewise_symplectic_trivialization"]["counts"]["identity_fixed_edges"],
                "stress_first_returns": certificate["finite_stress_test"]["total_first_returns"],
                "stress_collisions": certificate["finite_stress_test"]["collision_count"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
