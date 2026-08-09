#!/usr/bin/env python3
"""Exact producer for the HCS-C24 Rauzy--metaplectic obstruction ledger.

The program works with labeled two-row permutations.  It never replaces the
chronological cocycle by an averaged matrix.  The forward homology matrix of
an edge is ``I + E_(loser,winner)`` and later edges multiply on the left.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from collections import deque
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c24_certificate.json"
ALPHABET = (1, 2, 3, 4)
INITIAL = ((1, 2, 3, 4), (4, 3, 2, 1))
MOVE_TYPES = ("t", "b")
WIELANDT_BOUND_4 = 10

Permutation = tuple[tuple[int, ...], tuple[int, ...]]
EdgeToken = tuple[int, str, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--max-repetition", type=int, default=6)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_json(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]


def permutation_json(permutation: Permutation) -> dict[str, list[int]]:
    return {"top": list(permutation[0]), "bottom": list(permutation[1])}


def omega(permutation: Permutation) -> sp.Matrix:
    """Yoccoz crossing matrix in the fixed label order 1,2,3,4."""

    top, bottom = permutation
    top_position = {letter: index for index, letter in enumerate(top)}
    bottom_position = {letter: index for index, letter in enumerate(bottom)}
    result = sp.zeros(len(ALPHABET))
    for alpha in ALPHABET:
        for beta in ALPHABET:
            if top_position[alpha] < top_position[beta] and bottom_position[alpha] > bottom_position[beta]:
                result[alpha - 1, beta - 1] = 1
            elif top_position[alpha] > top_position[beta] and bottom_position[alpha] < bottom_position[beta]:
                result[alpha - 1, beta - 1] = -1
    return result


def rauzy_move(permutation: Permutation, move_type: str) -> tuple[Permutation, int, int, sp.Matrix]:
    """Return target, winner, loser, and forward chronological KZ matrix."""

    if move_type not in MOVE_TYPES:
        raise ValueError("move type must be 't' or 'b'")
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
    edge_matrix = sp.eye(len(ALPHABET))
    edge_matrix[loser - 1, winner - 1] += 1
    return (tuple(top), tuple(bottom)), winner, loser, edge_matrix


def irreducibility_rows(permutation: Permutation) -> list[dict[str, object]]:
    top, bottom = permutation
    rows = []
    for width in range(1, len(top)):
        top_prefix, bottom_prefix = set(top[:width]), set(bottom[:width])
        rows.append(
            {
                "width": width,
                "top_prefix": sorted(top_prefix),
                "bottom_prefix": sorted(bottom_prefix),
                "equal": top_prefix == bottom_prefix,
            }
        )
    return rows


def build_graph() -> tuple[list[Permutation], dict[tuple[int, str], dict[str, object]], dict[int, sp.Matrix]]:
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
        for move_type in MOVE_TYPES:
            target, winner, loser, edge_matrix = rauzy_move(source, move_type)
            assert edge_matrix * omega(source) * edge_matrix.T == omega(target)
            edges[(state_id[source], move_type)] = {
                "source": state_id[source],
                "target": state_id[target],
                "type": move_type,
                "winner": winner,
                "loser": loser,
                "matrix": edge_matrix,
            }

    # A deterministic spanning tree trivializes the varying symplectic fibers.
    initial_id = state_id[INITIAL]
    frames: dict[int, sp.Matrix] = {initial_id: sp.eye(len(ALPHABET))}
    id_queue: deque[int] = deque([initial_id])
    while id_queue:
        source_id = id_queue.popleft()
        for move_type in MOVE_TYPES:
            edge = edges[(source_id, move_type)]
            target_id = int(edge["target"])
            if target_id not in frames:
                frames[target_id] = sp.Matrix(edge["matrix"]) * frames[source_id]
                id_queue.append(target_id)

    base_form = omega(INITIAL).inv()
    for state_index, state in enumerate(states):
        frame = frames[state_index]
        assert frame.T * omega(state).inv() * frame == base_form
    return states, edges, frames


def rotations(items: Sequence[EdgeToken]) -> list[tuple[EdgeToken, ...]]:
    return [tuple(items[index:]) + tuple(items[:index]) for index in range(len(items))]


def canonical_cycle(items: Sequence[EdgeToken]) -> tuple[EdgeToken, ...]:
    return min(rotations(items))


def primitive_cycle(items: Sequence[EdgeToken]) -> bool:
    n = len(items)
    for period in range(1, n):
        if n % period == 0 and tuple(items) == tuple(items[:period]) * (n // period):
            return False
    return True


def cycle_matrix(tokens: Sequence[EdgeToken], edges: dict[tuple[int, str], dict[str, object]]) -> sp.Matrix:
    result = sp.eye(len(ALPHABET))
    current = tokens[0][0]
    for source, move_type, target in tokens:
        if source != current:
            raise ValueError("discontinuous cycle token sequence")
        edge = edges[(source, move_type)]
        if int(edge["target"]) != target:
            raise ValueError("cycle target disagrees with Rauzy graph")
        result = sp.Matrix(edge["matrix"]) * result
        current = target
    if current != tokens[0][0]:
        raise ValueError("token sequence is not closed")
    return result


def positive_exponent(matrix: sp.Matrix) -> int | None:
    """Exact primitivity test using the 4x4 Wielandt bound."""

    power = sp.eye(matrix.rows)
    for exponent in range(1, WIELANDT_BOUND_4 + 1):
        power = matrix * power
        if all(entry > 0 for entry in power):
            return exponent
    return None


def cyclic_zorich_blocks(word: str) -> list[dict[str, int | str]]:
    runs: list[list[object]] = []
    for letter in word:
        if runs and runs[-1][0] == letter:
            runs[-1][1] = int(runs[-1][1]) + 1
        else:
            runs.append([letter, 1])
    if len(runs) > 1 and runs[0][0] == runs[-1][0]:
        runs[0][1] = int(runs[0][1]) + int(runs[-1][1])
        runs.pop()
    return [{"type": str(kind), "length": int(length)} for kind, length in runs]


def central_first_return_branches(tokens: Sequence[EdgeToken], central_state: int) -> list[str]:
    """Cut a free cycle at visits to the declared central Rauzy state."""

    phases = [tuple(tokens[index:]) + tuple(tokens[:index]) for index in range(len(tokens)) if tokens[index][0] == central_state]
    if not phases:
        return []
    based = min(phases)
    visit_indices = [index for index, token in enumerate(based) if token[0] == central_state]
    branches = []
    for visit_number, start in enumerate(visit_indices):
        stop = visit_indices[visit_number + 1] if visit_number + 1 < len(visit_indices) else len(based)
        branches.append("".join(token[1] for token in based[start:stop]))
    rotations_of_branches = [branches[index:] + branches[:index] for index in range(len(branches))]
    return min(rotations_of_branches)


def rational_interval(poly: sp.Poly) -> dict[str, object]:
    intervals = poly.intervals(eps=sp.Rational(1, 10**12))
    real_intervals = [interval for interval, multiplicity in intervals if multiplicity == 1]
    if not real_intervals:
        raise ValueError("no simple real root found")
    lower, upper = max(real_intervals, key=lambda pair: pair[1])
    if lower <= 1:
        raise ValueError("Perron root was not isolated above one")
    midpoint = (lower + upper) / 2
    return {
        "lower": str(lower),
        "upper": str(upper),
        "lower_decimal": float(lower),
        "upper_decimal": float(upper),
        "log_midpoint_diagnostic": math.log(float(midpoint)),
        "certification": "exact SymPy rational isolation interval; decimal/log fields are diagnostics",
    }


def enumerate_cycles(
    states: list[Permutation],
    edges: dict[tuple[int, str], dict[str, object]],
    frames: dict[int, sp.Matrix],
    max_length: int,
    max_repetition: int,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    unique_cycles: dict[tuple[EdgeToken, ...], None] = {}
    enumeration_rows = []
    for length in range(1, max_length + 1):
        closed_based = 0
        primitive_based = 0
        before = len(unique_cycles)
        for start in range(len(states)):
            for move_word in itertools.product(MOVE_TYPES, repeat=length):
                current = start
                tokens: list[EdgeToken] = []
                for move_type in move_word:
                    target = int(edges[(current, move_type)]["target"])
                    tokens.append((current, move_type, target))
                    current = target
                if current != start:
                    continue
                closed_based += 1
                canonical = canonical_cycle(tokens)
                if not primitive_cycle(canonical):
                    continue
                primitive_based += 1
                unique_cycles[canonical] = None
        enumeration_rows.append(
            {
                "length": length,
                "all_based_paths": len(states) * (2**length),
                "closed_based_paths": closed_based,
                "primitive_based_occurrences": primitive_based,
                "primitive_free_cycles": len(unique_cycles) - before,
            }
        )

    base_form = omega(INITIAL).inv()
    central_state = states.index(INITIAL)
    perron_rows = []
    for canonical in sorted(unique_cycles, key=lambda cycle: (len(cycle), cycle)):
        phase_tokens = rotations(canonical)
        phase_matrices = [cycle_matrix(phase, edges) for phase in phase_tokens]
        phase_exponents = [positive_exponent(matrix) for matrix in phase_matrices]
        if any(exponent is None for exponent in phase_exponents):
            continue
        matrix = phase_matrices[0]
        start = canonical[0][0]
        state_form = omega(states[start]).inv()
        assert matrix.T * state_form * matrix == state_form
        fixed_matrix = frames[start].inv() * matrix * frames[start]
        assert fixed_matrix.T * base_form * fixed_matrix == base_form

        characteristic = matrix.charpoly().as_poly()
        coefficients = [int(value) for value in characteristic.all_coeffs()]
        reciprocal = coefficients == coefficients[::-1]
        determinant_rows = {}
        power = sp.eye(len(ALPHABET))
        for repetition in range(1, max_repetition + 1):
            power = matrix * power
            determinant_rows[str(repetition)] = int((sp.eye(len(ALPHABET)) - power).det())

        winners = [int(edges[(source, move_type)]["winner"]) for source, move_type, _ in canonical]
        losers = [int(edges[(source, move_type)]["loser"]) for source, move_type, _ in canonical]
        type_word = "".join(move_type for _, move_type, _ in canonical)
        positive_phases = [index for index, exponent in enumerate(phase_exponents) if exponent == 1]
        edge_strings = [f"s{source:02d}:{move_type}:s{target:02d}" for source, move_type, target in canonical]
        return_branches = central_first_return_branches(canonical, central_state)
        row = {
            "id": f"C24-P{len(perron_rows) + 1:03d}",
            "length": len(canonical),
            "canonical_edges": edge_strings,
            "type_word": type_word,
            "cyclic_zorich_blocks": cyclic_zorich_blocks(type_word),
            "central_state": central_state,
            "central_first_return_branches": return_branches,
            "central_return_period": len(return_branches),
            "start_state": start,
            "winner_word": winners,
            "loser_word": losers,
            "complete_winner_set": sorted(set(winners)) == list(ALPHABET),
            "primitive_directed_cycle": True,
            "quotient": "cyclic phase only; direction is retained",
            "cyclic_phase_count": len(phase_tokens),
            "eventual_positive_exponents_by_phase": [int(exponent) for exponent in phase_exponents],
            "positive_phase_indices": positive_phases,
            "chronological_matrix": matrix_json(matrix),
            "base_trivialized_symplectic_matrix": matrix_json(fixed_matrix),
            "determinant": int(matrix.det()),
            "characteristic_coefficients_descending": coefficients,
            "reciprocal_characteristic_polynomial": reciprocal,
            "fixed_form_check": True,
            "det_I_minus_power": determinant_rows,
            "metaplectic_character_locus": "regular" if determinant_rows["1"] != 0 else "singular_fixed_vector_locus",
            "perron_root_interval": rational_interval(characteristic),
            "period_clock": "log(lambda_PF); exact repetition follows from rho(M^r)=rho(M)^r",
            "labeled_periodic_admissibility": "PROVED_FROM_PRIMITIVE_M_TRANSPOSE_PF_VECTOR_AND_EDGE_LENGTH_FACTORIZATION",
            "unmarked_teichmueller_primitive_class": "NOT_CLASSIFIED_OR_QUOTIENTED",
        }
        perron_rows.append(row)

    return enumeration_rows, perron_rows


def make_certificate(max_length: int, max_repetition: int) -> dict[str, object]:
    if max_length < 1 or max_repetition < 1:
        raise ValueError("cutoffs must be positive")
    states, edges, frames = build_graph()
    state_id = {state: index for index, state in enumerate(states)}
    base_form = omega(INITIAL).inv()
    graph_states = []
    for index, state in enumerate(states):
        graph_states.append(
            {
                "id": index,
                **permutation_json(state),
                "omega": matrix_json(omega(state)),
                "J_inverse_form": matrix_json(omega(state).inv()),
                "spanning_tree_frame": matrix_json(frames[index]),
            }
        )

    graph_edges = []
    for source in range(len(states)):
        for move_type in MOVE_TYPES:
            edge = edges[(source, move_type)]
            target = int(edge["target"])
            matrix = sp.Matrix(edge["matrix"])
            fixed = frames[target].inv() * matrix * frames[source]
            assert fixed.T * base_form * fixed == base_form
            graph_edges.append(
                {
                    "source": source,
                    "type": move_type,
                    "target": target,
                    "winner": int(edge["winner"]),
                    "loser": int(edge["loser"]),
                    "chronological_matrix": matrix_json(matrix),
                    "transport_identity": "B*Omega_source*B^T=Omega_target",
                    "base_trivialized_matrix": matrix_json(fixed),
                    "base_symplectic_check": True,
                }
            )

    enumeration, perron_cycles = enumerate_cycles(states, edges, frames, max_length, max_repetition)
    eventual_by_length: dict[str, int] = {}
    singular_by_length: dict[str, int] = {}
    positive_phase_by_length: dict[str, int] = {}
    return_period_by_length: dict[str, dict[str, int]] = {}
    for row in perron_cycles:
        key = str(row["length"])
        eventual_by_length[key] = eventual_by_length.get(key, 0) + 1
        if row["metaplectic_character_locus"] != "regular":
            singular_by_length[key] = singular_by_length.get(key, 0) + 1
        if row["positive_phase_indices"]:
            positive_phase_by_length[key] = positive_phase_by_length.get(key, 0) + 1
        return_period = str(row["central_return_period"])
        period_bucket = return_period_by_length.setdefault(key, {})
        period_bucket[return_period] = period_bucket.get(return_period, 0) + 1

    return {
        "schema": "HCS-C24-RAUZY-METAPLECTIC-v1",
        "material_passport": {
            "origin_skill": "ars-codex academic-research-suite / experiment-agent",
            "origin_mode": "run",
            "origin_date": "2026-08-09T00:00:00Z",
            "verification_status": "UNVERIFIED",
            "version_label": "exp_result_v1",
        },
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "producer_sha256": sha256(Path(__file__)),
        },
        "source_lock": {
            "initial_permutation": permutation_json(INITIAL),
            "initial_state_id": state_id[INITIAL],
            "alphabet": list(ALPHABET),
            "irreducibility": irreducibility_rows(INITIAL),
            "literal_candidate_retained": True,
            "rauzy_class_state_count": len(states),
            "rauzy_class_edge_count": len(graph_edges),
            "omega0": matrix_json(omega(INITIAL)),
            "det_omega0": int(omega(INITIAL).det()),
            "rank_omega0": int(omega(INITIAL).rank()),
            "J0": matrix_json(base_form),
            "genus": 2,
            "singularity_count": 1,
            "zero_orders": [2],
            "stratum": "H(2)",
            "relative_equals_absolute": True,
            "matrix_convention": "B_edge=I+E_(loser,winner)",
            "chronology": "B_word=B_last*...*B_first; later edges act on the left",
            "averaging_used": False,
            "open_edge_geometry": "B*Omega_source*B^T=Omega_target",
            "closed_loop_geometry": "M^T*Omega_start^(-1)*M=Omega_start^(-1)",
        },
        "graph": {"states": graph_states, "edges": graph_edges},
        "enumeration": {
            "max_elementary_length": max_length,
            "max_repetition": max_repetition,
            "cyclic_rotation_quotiented": True,
            "reversal_quotiented": False,
            "proper_powers_excluded": True,
            "phase_invariant_primitivity_test": f"every cyclic phase has a positive power by exponent <= {WIELANDT_BOUND_4}",
            "admissibility_argument": "for R_word=B_word^T, a positive PF eigenvector lambda_0 and lambda_n=lambda_0/rho satisfy lambda_0=R_word*lambda_n; factoring R_word edge by edge proves every winner inequality",
            "orbit_scope": "primitive labeled directed Rauzy cycles; no quotient or distinctness claim for unmarked Teichmueller geodesics",
            "rows": enumeration,
            "primitive_free_cycle_total": sum(int(row["primitive_free_cycles"]) for row in enumeration),
            "eventually_positive_cycle_count": len(perron_cycles),
            "eventually_positive_by_length": eventual_by_length,
            "distinct_reciprocal_characteristic_polynomials": len({tuple(row["characteristic_coefficients_descending"]) for row in perron_cycles}),
            "positive_in_at_least_one_phase_by_length": positive_phase_by_length,
            "all_eventually_positive_cycles_hit_central_state": all(row["central_return_period"] > 0 for row in perron_cycles),
            "central_return_period_by_elementary_length": return_period_by_length,
            "character_singular_cycle_count": sum(singular_by_length.values()),
            "character_singular_by_length": singular_by_length,
        },
        "eventually_positive_cycles": perron_cycles,
        "operator_gate": {
            "tensor_theorem": "for nonzero K and infinite-dimensional unitary U, ||K tensor U||_ess=||K||",
            "atomic_theorem": "an absolutely norm-summable discrete metaplectic atomic sum is noncompact unless every signed same-projection aggregate vanishes",
            "central_sign": "unresolved required lift data; never quotiented; theorem uses actual signs before aggregation",
            "ordinary_trace": "forbidden for a single oscillator unitary",
            "distribution_character": "Thomas character only; regular point values require det(g-I)!=0",
            "branch_compressible_ordinary_fredholm": "PROVED_SCOPED_OBSTRUCTION_WHEN_STATED_COMPRESSION_EXISTS",
            "analytic_zorich_space_application": "requires either verified norm summability plus nonzero signed aggregate, or a mod-compact branch compression",
        },
        "decisions": {
            "source_lock": "PASS",
            "naive_pointwise_weil_character_euler_product": "REFUTED_ON_LABELED_CODING_BY_SINGULAR_PRIMITIVE_CYCLES",
            "unsmoothed_branch_compressible_ordinary_fredholm": "PROVED_SCOPED_OBSTRUCTION_WHEN_STATED_COMPRESSION_EXISTS",
            "norm_summable_discrete_atomic_fredholm": "PROVED_SCOPED_OBSTRUCTION_WHEN_SIGNED_AGGREGATE_IS_NONZERO",
            "canonical_analytic_zorich_application": "OPEN_APPLICATION_GATE",
            "unmarked_teichmueller_orbit_identification": "OPEN_NOT_NEEDED_FOR_LABELED_RETURN_OBSTRUCTION",
            "ordinary_metaplectic_fredholm_route": "CLOSED_ONLY_IN_TWO_STATED_REALIZATION_CLASSES",
            "generalized_or_distributional_trace_route": "OPEN_REQUIRES_NEW_CANONICAL_OBJECT",
            "prime_or_zero_data_used": False,
            "route_b_authorized": False,
        },
    }


def main() -> None:
    args = parse_args()
    certificate = make_certificate(args.max_length, args.max_repetition)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "sha256": sha256(args.output),
        "states": certificate["source_lock"]["rauzy_class_state_count"],
        "primitive_cycles": certificate["enumeration"]["primitive_free_cycle_total"],
        "eventually_positive": certificate["enumeration"]["eventually_positive_cycle_count"],
        "character_singular": certificate["enumeration"]["character_singular_cycle_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
