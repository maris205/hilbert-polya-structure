#!/usr/bin/env python3
"""Independent verifier for the HCS-C25 exact certificate.

This file deliberately does not import the producer.  It rederives the
seven labeled Rauzy states, chronological products, decoder trace, AGY
section witness, projective Jacobian, and the optional length-22 stress
digest from its own implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c25_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c25_independent_check.json"
LETTERS = (1, 2, 3, 4)
TYPES = ("t", "b")
SEED = ((1, 2, 3, 4), (4, 3, 2, 1))
SECTION_BASE = ((1, 3, 4, 2), (4, 3, 2, 1))
ETA_WORD = "tbttbtbb"
SECTION_WORD = "t" * 64 + ETA_WORD * 8
EYE = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
IntMatrix = tuple[tuple[int, ...], ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def portable(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def matrix_list(matrix: IntMatrix | sp.Matrix) -> list[list[int]]:
    if isinstance(matrix, sp.MatrixBase):
        return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]
    return [list(row) for row in matrix]


def transpose(matrix: IntMatrix) -> IntMatrix:
    return tuple(tuple(matrix[column][row] for column in range(4)) for row in range(4))


def multiply(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(4)) for column in range(4))
        for row in range(4)
    )


def total(matrix: IntMatrix) -> int:
    return sum(sum(row) for row in matrix)


def elementary(winner: int, loser: int) -> IntMatrix:
    value = [list(row) for row in EYE]
    value[loser - 1][winner - 1] += 1
    return tuple(tuple(row) for row in value)


def crossing(permutation: Permutation) -> sp.Matrix:
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


def independent_graph() -> tuple[list[Permutation], dict[tuple[int, str], dict[str, object]]]:
    pending = [SEED]
    found = {SEED}
    while pending:
        source = pending.pop()
        for kind in TYPES:
            target, _, _, _ = arrow(source, kind)
            if target not in found:
                found.add(target)
                pending.append(target)
    states = sorted(found)
    ids = {state: index for index, state in enumerate(states)}
    edges: dict[tuple[int, str], dict[str, object]] = {}
    for source in states:
        for kind in TYPES:
            target, winner, loser, matrix = arrow(source, kind)
            edges[(ids[source], kind)] = {
                "source": ids[source],
                "type": kind,
                "target": ids[target],
                "winner": winner,
                "loser": loser,
                "matrix": matrix,
            }
    if len(states) != 7 or len(edges) != 14 or ids[SEED] != 2 or ids[SECTION_BASE] != 4:
        raise AssertionError("independent seven-state source lock failed")
    return states, edges


def independent_fixed_fiber_trivialization(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[sp.Matrix, dict[int, sp.Matrix], dict[int, tuple[int, str] | None], list[dict[str, object]]]:
    """Rebuild the state-4 BFS frames without consulting the producer."""

    base = states.index(SECTION_BASE)
    base_form = crossing(states[base]).inv()
    frames: dict[int, sp.Matrix] = {base: sp.eye(4)}
    parents: dict[int, tuple[int, str] | None] = {base: None}
    queue = [base]
    cursor = 0
    while cursor < len(queue):
        source = queue[cursor]
        cursor += 1
        for kind in TYPES:
            edge = edges[(source, kind)]
            target = int(edge["target"])
            if target in frames:
                continue
            frames[target] = sp.Matrix(edge["matrix"]) * frames[source]
            parents[target] = (source, kind)
            queue.append(target)
    if set(frames) != set(range(7)):
        raise AssertionError("independent frame tree did not cover all states")

    fixed_edges = []
    for source in range(7):
        for kind in TYPES:
            edge = edges[(source, kind)]
            target = int(edge["target"])
            fixed = frames[target].inv() * sp.Matrix(edge["matrix"]) * frames[source]
            fixed_edges.append(
                {
                    "source": source,
                    "type": kind,
                    "target": target,
                    "matrix": fixed,
                    "determinant": int(fixed.det()),
                    "integral": all(sp.denom(entry) == 1 for entry in fixed),
                    "tree": parents[target] == (source, kind),
                    "identity": fixed == sp.eye(4),
                    "symplectic": fixed.T * base_form * fixed == base_form,
                }
            )
    return base_form, frames, parents, fixed_edges


def walk(
    start: int,
    word: str,
    edges: dict[tuple[int, str], dict[str, object]],
) -> tuple[int, IntMatrix, list[dict[str, int | str]]]:
    state = start
    product = EYE
    tokens: list[dict[str, int | str]] = []
    for index, kind in enumerate(word):
        edge = edges[(state, kind)]
        edge_matrix = edge["matrix"]
        assert isinstance(edge_matrix, tuple)
        product = multiply(edge_matrix, product)
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
    return state, product, tokens


def independent_decode(
    start: int,
    length_matrix: IntMatrix,
    edges: dict[tuple[int, str], dict[str, object]],
    *,
    matrices: bool,
) -> dict[str, object]:
    state = start
    remaining = length_matrix
    letters: list[str] = []
    trace: list[dict[str, object]] = []
    while remaining != EYE:
        tests = []
        for kind in TYPES:
            edge = edges[(state, kind)]
            winner, loser = int(edge["winner"]), int(edge["loser"])
            difference = tuple(remaining[winner - 1][j] - remaining[loser - 1][j] for j in range(4))
            tests.append(
                {
                    "type": kind,
                    "winner": winner,
                    "loser": loser,
                    "difference_winner_minus_loser": list(difference),
                    "componentwise_dominance": min(difference) >= 0,
                }
            )
        allowed = [candidate for candidate in tests if candidate["componentwise_dominance"]]
        if len(allowed) != 1:
            raise ValueError(f"independent decoder found {len(allowed)} choices")
        selected = allowed[0]
        kind = str(selected["type"])
        winner, loser = int(selected["winner"]), int(selected["loser"])
        before = total(remaining)
        loser_sum = sum(remaining[loser - 1])
        rows = [list(row) for row in remaining]
        rows[winner - 1] = list(selected["difference_winner_minus_loser"])
        after_matrix = tuple(tuple(row) for row in rows)
        after = total(after_matrix)
        target = int(edges[(state, kind)]["target"])
        row: dict[str, object] = {
            "step": len(letters),
            "state_before": state,
            "candidate_tests": tests,
            "chosen_type": kind,
            "winner": winner,
            "loser": loser,
            "state_after": target,
            "sum_before": before,
            "sum_after": after,
            "strict_drop": before - after,
            "loser_row_sum": loser_sum,
            "nonnegative_after": min(value for matrix_row in after_matrix for value in matrix_row) >= 0,
        }
        if matrices:
            row["matrix_before"] = matrix_list(remaining)
            row["matrix_after"] = matrix_list(after_matrix)
        if not (row["nonnegative_after"] and before - after == loser_sum > 0):
            raise ValueError("independent decoder invariant failed")
        trace.append(row)
        letters.append(kind)
        state = target
        remaining = after_matrix
        if len(letters) > 100_000:
            raise ValueError("independent decoder failed to terminate")
    return {
        "decoded_word": "".join(letters),
        "end_state": state,
        "steps": len(letters),
        "terminal_matrix": matrix_list(remaining),
        "trace": trace,
    }


def rational_from_json(value: dict[str, object]) -> sp.Rational:
    result = sp.Rational(int(value["numerator"]), int(value["denominator"]))
    if str(result) != value["exact"]:
        raise AssertionError("rational string does not match numerator/denominator")
    return result


def vector_from_json(values: list[dict[str, object]]) -> sp.Matrix:
    return sp.Matrix([rational_from_json(value) for value in values])


def initial_run(word: str) -> int:
    if not word:
        return 0
    return next((index for index, letter in enumerate(word) if letter != word[0]), len(word))


def jacobian_at(length_matrix: sp.Matrix, point: sp.Matrix) -> sp.Rational:
    tangent = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    image = length_matrix * point
    scale = sp.Rational(sum(image))
    linear = length_matrix * tangent
    dscale = sp.ones(1, 4) * linear
    derivative = (linear * scale - image * dscale) / scale**2
    return sp.factor(derivative[:3, :].det())


def first_return_rational_series(
    states: list[Permutation], edges: dict[tuple[int, str], dict[str, object]], central: int
) -> sp.Expr:
    z = sp.symbols("z")
    noncentral = [state for state in range(7) if state != central]
    at = {state: index for index, state in enumerate(noncentral)}
    q = sp.zeros(6)
    enter = sp.zeros(6, 1)
    leave = sp.zeros(6, 1)
    direct = 0
    for kind in TYPES:
        target = int(edges[(central, kind)]["target"])
        if target == central:
            direct += 1
        else:
            enter[at[target], 0] += 1
    for source in noncentral:
        for kind in TYPES:
            target = int(edges[(source, kind)]["target"])
            if target == central:
                leave[at[source], 0] += 1
            else:
                q[at[source], at[target]] += 1
    return sp.factor(direct * z + z**2 * (enter.T * (sp.eye(6) - z * q).inv() * leave)[0])


def fib(index: int) -> int:
    left, right = 0, 1
    for _ in range(index):
        left, right = right, left + right
    return left


def stress_replay(
    central: int,
    edges: dict[tuple[int, str], dict[str, object]],
    max_length: int,
) -> dict[str, object]:
    pending: list[tuple[int, str, IntMatrix]] = [(central, "", EYE)]
    returns: list[tuple[str, IntMatrix]] = []
    while pending:
        state, word, product = pending.pop()
        if len(word) >= max_length:
            continue
        for kind in ("b", "t"):
            edge = edges[(state, kind)]
            matrix = edge["matrix"]
            assert isinstance(matrix, tuple)
            next_product = multiply(matrix, product)
            next_word = word + kind
            target = int(edge["target"])
            if target == central:
                returns.append((next_word, next_product))
            else:
                pending.append((target, next_word, next_product))
    returns.sort(key=lambda row: (len(row[0]), row[0]))
    counts: dict[str, int] = {}
    seen: set[tuple[int, ...]] = set()
    digest = hashlib.sha256()
    for word, product in returns:
        counts[str(len(word))] = counts.get(str(len(word)), 0) + 1
        flat = tuple(value for row in product for value in row)
        if flat in seen:
            raise AssertionError("independent stress replay found a matrix collision")
        seen.add(flat)
        decoded = independent_decode(central, transpose(product), edges, matrices=False)
        if decoded["decoded_word"] != word or decoded["end_state"] != central:
            raise AssertionError("independent stress decoder mismatch")
        digest.update(f"{word}|{','.join(str(value) for value in flat)}\n".encode("ascii"))
    expected = {str(n): 2 * fib(n - 2) for n in range(3, max_length + 1)}
    if counts != expected:
        raise AssertionError("independent first-return counts violate the Fibonacci recurrence")
    return {
        "count_by_length": counts,
        "total_first_returns": len(returns),
        "decoded_exactly": len(returns),
        "distinct_forward_matrices": len(seen),
        "collision_count": len(returns) - len(seen),
        "canonical_word_matrix_sha256": digest.hexdigest(),
    }


def verify(certificate: dict[str, object]) -> tuple[dict[str, bool], dict[str, object]]:
    states, edges = independent_graph()
    graph = certificate["graph"]
    source = certificate["source_lock"]
    state_rows = graph["states"]
    edge_rows = {(int(row["source"]), str(row["type"])): row for row in graph["edges"]}

    graph_ok = graph["state_count"] == 7 and graph["edge_count"] == 14
    graph_ok &= source["literal_seed"] == {"top": [1, 2, 3, 4], "bottom": [4, 3, 2, 1]}
    for state_id, state in enumerate(states):
        row = state_rows[state_id]
        graph_ok &= row["id"] == state_id
        graph_ok &= row["top"] == list(state[0]) and row["bottom"] == list(state[1])
        graph_ok &= row["omega"] == matrix_list(crossing(state))
        graph_ok &= row["omega_determinant"] == int(crossing(state).det()) == 1
        for kind in TYPES:
            edge = edges[(state_id, kind)]
            released = edge_rows[(state_id, kind)]
            target = int(edge["target"])
            matrix = edge["matrix"]
            assert isinstance(matrix, tuple)
            graph_ok &= released["target"] == target
            graph_ok &= released["winner"] == edge["winner"] and released["loser"] == edge["loser"]
            graph_ok &= released["chronological_matrix"] == matrix_list(matrix)
            graph_ok &= sp.Matrix(matrix) * crossing(state) * sp.Matrix(matrix).T == crossing(states[target])

    trivialization = certificate["statewise_symplectic_trivialization"]
    fixed_base_form, frames, parents, fixed_edges = independent_fixed_fiber_trivialization(states, edges)
    released_frames = {int(row["state"]): row for row in trivialization["state_frames"]}
    released_fixed_edges = {
        (int(row["source"]), str(row["type"])): row for row in trivialization["fixed_fiber_edges"]
    }
    trivialization_ok = (
        trivialization["base_state"] == 4
        and trivialization["base_form_J0"] == matrix_list(fixed_base_form)
        and len(released_frames) == 7
        and len(released_fixed_edges) == 14
        and "S_target=B_edge*S_source" in trivialization["construction"]
        and trivialization["fixed_fiber_edge_definition"] == "g_e=S_target^(-1)*B_e*S_source"
    )
    for state in range(7):
        frame = frames[state]
        released = released_frames[state]
        parent = parents[state]
        expected_parent = None if parent is None else {"source": parent[0], "type": parent[1], "target": state}
        trivialization_ok &= released["frame_S"] == matrix_list(frame)
        trivialization_ok &= released["determinant"] == int(frame.det()) == 1
        trivialization_ok &= released["integral"] is True
        trivialization_ok &= released["parent_tree_edge"] == expected_parent
        trivialization_ok &= frame.T * crossing(states[state]).inv() * frame == fixed_base_form
        trivialization_ok &= released["frame_identity_verified"] is True
    identity_count = 0
    for computed in fixed_edges:
        key = (int(computed["source"]), str(computed["type"]))
        released = released_fixed_edges[key]
        trivialization_ok &= released["target"] == computed["target"]
        trivialization_ok &= released["g_edge_equals_S_target_inverse_B_edge_S_source"] == matrix_list(computed["matrix"])
        trivialization_ok &= released["determinant"] == computed["determinant"] == 1
        trivialization_ok &= released["integral"] is computed["integral"] is True
        trivialization_ok &= released["spanning_tree_edge"] is computed["tree"]
        trivialization_ok &= released["identity_matrix"] is computed["identity"]
        trivialization_ok &= released["fixed_form_identity_verified"] is computed["symplectic"] is True
        trivialization_ok &= not computed["tree"] or computed["identity"]
        identity_count += int(bool(computed["identity"]))
    trivialization_ok &= trivialization["counts"] == {
        "state_frames": 7,
        "fixed_fiber_edges": 14,
        "identity_fixed_edges": identity_count,
        "nonidentity_fixed_edges": 14 - identity_count,
    }
    lift_scope = trivialization["metaplectic_lift_scope"]
    trivialization_ok &= identity_count == 6
    trivialization_ok &= "two metaplectic lifts" in lift_scope["proved"]
    trivialization_ok &= "no numerical choice" in lift_scope["not_done"]
    trivialization_ok &= "no global multiplicative section" in lift_scope["group_section_not_claimed"]

    base = states.index(SECTION_BASE)
    eta_end, eta_matrix, eta_tokens = walk(base, ETA_WORD, edges)
    gamma_end, gamma_matrix, gamma_tokens = walk(base, SECTION_WORD, edges)
    witness = certificate["agy_section_witness"]
    eta = witness["eta"]
    gamma = witness["gamma_star"]
    word_ok = (
        witness["base_state"] == base == 4
        and eta["word"] == ETA_WORD
        and eta["closed"] is True
        and eta_end == base
        and eta["edge_tokens"] == eta_tokens
        and eta["chronological_matrix"] == matrix_list(eta_matrix)
        and gamma["word"] == SECTION_WORD
        and gamma["length"] == 128
        and gamma["closed"] is True
        and gamma_end == base
        and gamma["edge_tokens"] == gamma_tokens
        and gamma["word_sha256"] == hashlib.sha256(SECTION_WORD.encode("ascii")).hexdigest()
    )

    boundaries = [(0, 72)] + [(64 + block * 8, 64 + (block + 1) * 8) for block in range(1, 8)]
    computed_blocks = []
    for index, (start, stop) in enumerate(boundaries, start=1):
        winners = sorted({int(token["winner"]) for token in gamma_tokens[start:stop]})
        computed_blocks.append(
            {
                "block": index,
                "start_inclusive": start,
                "stop_exclusive": stop,
                "word": SECTION_WORD[start:stop],
                "winner_set": winners,
                "complete": winners == list(LETTERS),
            }
        )
    criterion = gamma["strong_positivity_criterion"]
    complete_ok = (
        eta["winner_set"] == list(LETTERS)
        and eta["complete"] is True
        and gamma["complete_blocks"] == computed_blocks
        and all(row["complete"] for row in computed_blocks)
        and gamma["k_complete"] == 8
        and criterion["threshold_3d_minus_4"] == 8
        and criterion["k"] == 8
        and criterion["criterion_met"] is True
    )
    borders = [length for length in range(1, 128) if SECTION_WORD[:length] == SECTION_WORD[-length:]]
    neat = gamma["neatness"]
    neat_ok = (
        borders == []
        and neat["proper_border_lengths"] == borders
        and neat["initial_constant_run_length"] == initial_run(SECTION_WORD) == 65
        and "maximal prefix scan" in neat["initial_constant_run_computation"]
        and neat["at_least_half_of_word"] is True
        and neat["terminal_type"] == "b"
        and neat["terminal_differs_from_initial"] is True
        and neat["neat_certificate_passed"] is True
    )

    b = sp.Matrix(gamma_matrix)
    r = b.T
    omega_base = crossing(SECTION_BASE)
    form_ok = (
        gamma["chronological_matrix_B"] == matrix_list(gamma_matrix)
        and gamma["length_matrix_R_equals_B_transpose"] == matrix_list(transpose(gamma_matrix))
        and int(b.det()) == gamma["determinant"] == 1
        and all(entry > 0 for entry in b)
        and gamma["entrywise_positive"] is True
        and b * omega_base * b.T == omega_base
        and b.T * omega_base.inv() * b == omega_base.inv()
        and gamma["form_transport"]["omega_base"] == matrix_list(omega_base)
        and gamma["form_transport"]["inverse_form_J"] == matrix_list(omega_base.inv())
    )

    branch = witness["projective_inverse_branch"]
    ones = sp.ones(4, 1)
    raw_x = r * ones
    x_scale = sp.Rational(sum(raw_x))
    x0 = raw_x / x_scale
    raw_y = r * x0
    roof_scale = sp.Rational(sum(raw_y))
    y0 = raw_y / roof_scale
    direct_jacobian = jacobian_at(r, x0)
    released_jacobian = rational_from_json(branch["jacobian"]["at_x0"])
    s_coefficients = [int(value) for value in (sp.ones(1, 4) * r).T]
    branch_ok = (
        branch["x0_unnormalized"] == [int(value) for value in raw_x]
        and branch["x0_normalization"] == int(x_scale)
        and vector_from_json(branch["x0"]) == x0
        and vector_from_json(branch["y0"]) == y0
        and rational_from_json(branch["roof"]["exp_r_at_x0"]) == roof_scale
        and branch["normalizer_coefficients_on_simplex"] == s_coefficients
        and branch["normalizer_essential_range_open_simplex"]
        == {"infimum": min(s_coefficients), "supremum": max(s_coefficients)}
        and direct_jacobian == released_jacobian == roof_scale ** (-4)
        and branch["jacobian"]["dimension_d"] == 4
        and branch["jacobian"]["at_x0_power_certificate"]["power"] == 4
        and branch["x0_positive_simplex"] is True
        and branch["y0_positive_simplex"] is True
    )

    decoded = independent_decode(base, transpose(gamma_matrix), edges, matrices=True)
    theorem = certificate["all_length_decoder_theorem"]
    reversal_pairs = all(
        int(edges[(state, "t")]["winner"]) == int(edges[(state, "b")]["loser"])
        and int(edges[(state, "t")]["loser"]) == int(edges[(state, "b")]["winner"])
        for state in range(7)
    )
    decoder_ok = (
        decoded == gamma["decoder"]
        and decoded["decoded_word"] == SECTION_WORD
        and decoded["end_state"] == base
        and decoded["steps"] == 128
        and all(row["strict_drop"] == row["loser_row_sum"] > 0 for row in decoded["trace"])
        and all(sum(bool(test["componentwise_dominance"]) for test in row["candidate_tests"]) == 1 for row in decoded["trace"])
        and reversal_pairs
        and theorem["status"] == "EXACT_INDUCTIVE_THEOREM_CERTIFICATE"
        and theorem["finite_enumeration_is_proof_basis"] is False
        and "fixed labeled" in theorem["statement"]
        and all(int(crossing(state).det()) == 1 for state in states)
        and "full rank" in theorem["projection_scope"]["current_absolute_homology_application"]
        and "does not follow" in theorem["projection_scope"]["general_warning"]
    )

    z = sp.symbols("z")
    series = first_return_rational_series(states, edges, states.index(SEED))
    language = certificate["central_first_return_language"]
    language_ok = (
        sp.cancel(series - 2 * z**3 / (1 - z - z**2)) == 0
        and language["generating_function"] == str(series)
        and language["generating_function_canonical"] == "2*z^3/(1-z-z^2)"
        and language["top_family_regex"] == "t (b t* b)* t b* t"
        and language["bottom_family_regex"] == "b (t b* t)* b t* b"
    )

    released_stress = certificate["finite_stress_test"]
    replay = stress_replay(states.index(SEED), edges, int(released_stress["max_elementary_length"]))
    stress_ok = all(released_stress[key] == value for key, value in replay.items())
    stress_ok &= released_stress["role"] == "NON_PROOF_DIAGNOSTIC_AND_MUTATION_SENTINEL"
    stress_ok &= released_stress["logical_basis"].startswith("the all-length decoder theorem")
    stress_ok &= replay["total_first_returns"] == 35420 and replay["collision_count"] == 0

    toy = certificate["central_return_toy"]
    toy_end, toy_matrix, toy_tokens = walk(states.index(SEED), "ttt", edges)
    toy_ok = (
        toy_end == states.index(SEED)
        and toy["edge_tokens"] == toy_tokens
        and toy["chronological_matrix_B"] == matrix_list(toy_matrix)
        and toy["length_matrix_R"] == matrix_list(transpose(toy_matrix))
        and toy["canonical_AGY_application_claimed"] is False
        and toy["scope"] == "TOY_CENTRAL_RETURN_SANITY_CHECK_NOT_THE_AGY_GAMMA_STAR_SECTION_BRANCH"
        and toy["word"] != SECTION_WORD
    )

    application = certificate["operator_application"]
    claims_ok = (
        source["averaged_transition_matrix_used"] is False
        and source["cutoff_or_heat_smoothing_used"] is False
        and certificate["decisions"]["finite_length_13_ledger_used"] is False
        and certificate["decisions"]["route_b_authorized"] is False
        and "gamma_star" in application["canonical_map"]
        and "not identified with the toy ttt" in application["normalized_L2_application"]
        and application["ordinary_fredholm_determinant"].startswith("REJECTED_ON_THE_REGISTERED")
        and "remain open" in application["remaining_scope"]
        and "no central signs are selected numerically" in application["metaplectic_edge_lifts"]
    )

    checks = {
        "literal_seven_state_graph_and_edge_transport": bool(graph_ok),
        "statewise_integer_symplectic_trivialization": bool(trivialization_ok),
        "source_locked_AGY_word_closed_and_neat": bool(word_ok and neat_ok),
        "eight_complete_3d_minus_4_strong_positivity": bool(complete_ok),
        "later_left_matrix_determinant_positivity_and_form": bool(form_ok),
        "projective_x0_y0_roof_and_exp_minus_4r_jacobian": bool(branch_ok),
        "all_length_decoder_gamma_trace_and_theorem_invariants": bool(decoder_ok),
        "central_first_return_rational_language": bool(language_ok),
        "length_22_nonproof_stress_replay": bool(stress_ok),
        "toy_ttt_and_AGY_section_scope_separation": bool(toy_ok),
        "operator_claim_boundary_no_averaging_no_smoothing": bool(claims_ok),
    }
    summary = {
        "base_state": base,
        "eta": ETA_WORD,
        "gamma_star_compressed": "t^64 (tbttbtbb)^8",
        "gamma_length": len(SECTION_WORD),
        "gamma_matrix": matrix_list(gamma_matrix),
        "gamma_determinant": int(b.det()),
        "gamma_entrywise_positive": all(entry > 0 for entry in b),
        "state_frame_count": len(frames),
        "fixed_fiber_edge_count": len(fixed_edges),
        "identity_fixed_fiber_edges": identity_count,
        "nonidentity_fixed_fiber_edges": len(fixed_edges) - identity_count,
        "decoder_steps": decoded["steps"],
        "stress_max_length": released_stress["max_elementary_length"],
        "stress_first_returns": replay["total_first_returns"],
        "stress_distinct_matrices": replay["distinct_forward_matrices"],
        "stress_digest": replay["canonical_word_matrix_sha256"],
        "exp_r_at_x0": str(roof_scale),
        "jacobian_at_x0": str(direct_jacobian),
    }
    return checks, summary


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    checks, summary = verify(certificate)
    passed = all(checks.values())
    output = {
        "schema": "HCS-C25-INDEPENDENT-CHECK-v2",
        "material_passport": {
            "origin": "independent implementation; producer import forbidden",
            "origin_mode": "validate",
            "origin_date": "2026-08-10T00:00:00Z",
            "verification_status": "VERIFIED" if passed else "UNVERIFIED",
            "version_label": "c25_independent_validation_v2",
        },
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "checker_sha256": sha256(Path(__file__)),
        },
        "certificate": portable(args.certificate),
        "certificate_sha256": sha256(args.certificate),
        "checks": checks,
        "summary": summary,
        "passed": passed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
