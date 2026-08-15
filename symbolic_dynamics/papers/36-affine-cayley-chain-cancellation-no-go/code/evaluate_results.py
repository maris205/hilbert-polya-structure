#!/usr/bin/env python3
"""Independently reconstruct and evaluate every exact SD-C38 source row."""

from __future__ import annotations

import argparse
from collections import defaultdict
import csv
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from independent_evaluator import (
    check_boundary_squared_zero,
    evaluate_generic_supertrace,
    evaluate_trace_counts,
    rational_rank,
    transpose,
)


MAIN_R = (2, 3, 4, 5)
MAX_LENGTH = 12
INVERSE = {"u": "U", "U": "u", "v": "V", "V": "v"}
PROTOTYPE_HASHES = {
    "source_core.py": "041b8a1ee487eddafb1a4e935a015eaedf44aff1c32c6d26443c5a05e6cf94bd",
    "independent_evaluator.py": "d2cbd2bf5174b90a96135670b8022c94a4de2e9ba9404860ff49725ed41e28ce",
    "run_exact.py": "ee0a345bde7e3f57e42d4da41ab2297771a6527177e30abaf4993d3cd7ca2fc5",
    "results/scientific_results.json": "499b1a5b0647e9a9999dbfdfc881a8edc0877875102d91607c10e041f69f5221",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def scale(r: int, k: int) -> Fraction:
    if k >= 0:
        return Fraction(r**k)
    return Fraction(1, r ** (-k))


def affine_step(r: int, state: tuple[Fraction, int], symbol: str):
    x, k = state
    if symbol == "u":
        return x + scale(r, k), k
    if symbol == "U":
        return x - scale(r, k), k
    if symbol == "v":
        return x, k + 1
    if symbol == "V":
        return x, k - 1
    raise ValueError(symbol)


def evaluate_word(r: int, word: tuple[str, ...]):
    state = (Fraction(0), 0)
    for symbol in word:
        state = affine_step(r, state, symbol)
    return state


def affine_counts(r: int, maximum: int) -> list[int]:
    distribution = {(Fraction(0), 0): 1}
    values = [1]
    for _ in range(maximum):
        next_distribution: defaultdict[tuple[Fraction, int], int] = defaultdict(int)
        for state, multiplicity in distribution.items():
            for symbol in ("u", "U", "v", "V"):
                next_distribution[affine_step(r, state, symbol)] += multiplicity
        distribution = dict(next_distribution)
        values.append(distribution.get((Fraction(0), 0), 0))
    return values


def append_reduced(word: tuple[str, ...], symbol: str) -> tuple[str, ...]:
    if word and word[-1] == INVERSE[symbol]:
        return word[:-1]
    return word + (symbol,)


def free_counts(maximum: int) -> list[int]:
    distribution: dict[tuple[str, ...], int] = {(): 1}
    values = [1]
    for _ in range(maximum):
        next_distribution: defaultdict[tuple[str, ...], int] = defaultdict(int)
        for word, multiplicity in distribution.items():
            for symbol in ("u", "U", "v", "V"):
                next_distribution[append_reduced(word, symbol)] += multiplicity
        distribution = dict(next_distribution)
        values.append(distribution.get((), 0))
    return values


def primitive_word(word: tuple[str, ...]) -> bool:
    length = len(word)
    for period in range(1, length):
        if length % period == 0 and word == word[:period] * (length // period):
            return False
    return True


def cyclically_nonbacktracking(word: tuple[str, ...]) -> bool:
    return all(
        word[(index + 1) % len(word)] != INVERSE[word[index]]
        for index in range(len(word))
    )


def marker_row(r: int) -> dict[str, object]:
    word = tuple(["v", "u", "V"] + ["U"] * r)
    exponent_sum = r * (r + 1) // 2 + 2 * r + 5
    weight = Fraction(1, 2) ** (2 * exponent_sum)
    return {
        "r": r,
        "relation_word": "".join(word),
        "relation_side_lengths": [2, r + 1],
        "cycle_length": r + 3,
        "unit_step_marker_descends": r == 1,
        "damping_theta": "1/2",
        "origin_exponent_sum": exponent_sum,
        "one_oriented_cycle_trace_weight": str(weight),
    }


def finite_step(r: int, q: int, period: int, vertex, symbol: str):
    b, k = vertex
    multiplier = pow(r, k, q)
    if symbol == "u":
        return (b + multiplier) % q, k
    if symbol == "U":
        return (b - multiplier) % q, k
    if symbol == "v":
        return b, (k + 1) % period
    if symbol == "V":
        return b, (k - 1) % period
    raise ValueError(symbol)


def finite_data(r: int, q: int, period: int) -> dict[str, object]:
    vertices = [(b, k) for k in range(period) for b in range(q)]
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
    edges = [
        (vertex, label) for vertex in vertices for label in ("u", "v")
    ]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    boundary_1 = [[0 for _ in edges] for _ in vertices]
    for column, (origin, label) in enumerate(edges):
        target = finite_step(r, q, period, origin, label)
        boundary_1[vertex_index[origin]][column] -= 1
        boundary_1[vertex_index[target]][column] += 1

    def closed_path_column(origin, word: tuple[str, ...]) -> list[int]:
        column = [0 for _ in edges]
        current = origin
        for symbol in word:
            if symbol in ("u", "v"):
                column[edge_index[(current, symbol)]] += 1
                current = finite_step(r, q, period, current, symbol)
            else:
                previous = finite_step(r, q, period, current, symbol)
                column[edge_index[(previous, symbol.lower())]] -= 1
                current = previous
        if current != origin:
            raise AssertionError((origin, word, current))
        return column

    relation = tuple(["v", "u", "V"] + ["U"] * r)
    u_relation = tuple(["u"] * q)
    v_relation = tuple(["v"] * period)
    affine_columns = [closed_path_column(vertex, relation) for vertex in vertices]
    complete_columns = affine_columns.copy()
    complete_columns.extend(
        closed_path_column(vertex, u_relation) for vertex in vertices
    )
    complete_columns.extend(
        closed_path_column(vertex, v_relation) for vertex in vertices
    )
    return {
        "r": r,
        "q": q,
        "period": period,
        "vertices": [list(vertex) for vertex in vertices],
        "edges": [
            {"index": index, "origin": list(origin), "label": label}
            for index, (origin, label) in enumerate(edges)
        ],
        "boundary_1": boundary_1,
        "affine_cell_columns": affine_columns,
        "complete_cell_columns": complete_columns,
        "relation_word": "".join(relation),
    }


def finite_summary(data: dict[str, object]) -> dict[str, object]:
    boundary = data["boundary_1"]
    affine = data["affine_cell_columns"]
    complete = data["complete_cell_columns"]
    number_vertices = len(data["vertices"])
    number_edges = len(data["edges"])
    rank_1 = rational_rank(boundary)
    rank_affine = rational_rank(transpose(affine))
    rank_complete = rational_rank(transpose(complete))
    cycles = number_edges - rank_1
    return {
        "r": data["r"],
        "q": data["q"],
        "period": data["period"],
        "vertices": number_vertices,
        "positive_edge_instances": number_edges,
        "rank_boundary_1": rank_1,
        "cycle_dimension_before_cells": cycles,
        "rank_affine_cell_boundaries": rank_affine,
        "h1_after_affine_cells": cycles - rank_affine,
        "rank_complete_cell_boundaries": rank_complete,
        "h1_after_complete_presentation_cells": cycles - rank_complete,
        "boundary_squared_zero_affine": check_boundary_squared_zero(
            boundary, affine
        ),
        "boundary_squared_zero_complete": check_boundary_squared_zero(
            boundary, complete
        ),
    }


def add_check(checks: list[dict[str, object]], name: str, passed: bool) -> None:
    checks.append({"name": name, "pass": bool(passed)})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    result_dir = Path(arguments.result_dir)
    raw = json.loads((result_dir / "source_raw.json").read_text(encoding="utf-8"))

    independent_free = free_counts(MAX_LENGTH)
    independent_counts = {
        r: affine_counts(r, MAX_LENGTH) for r in (1, *MAIN_R)
    }
    trace_items = [
        evaluate_trace_counts(r, independent_counts[r], independent_free)
        for r in MAIN_R
    ]
    markers = {r: marker_row(r) for r in (1, *MAIN_R)}
    finite_independent = [
        finite_data(row["r"], row["q"], row["period"])
        for row in raw["finite_chain_data"]
    ]
    finite_summaries = [finite_summary(row) for row in finite_independent]
    graded = evaluate_generic_supertrace(trace_items)

    prototype_checks: list[dict[str, object]] = []
    integration_checks: list[dict[str, object]] = []
    for item in trace_items:
        r = item["r"]
        relation = tuple(["v", "u", "V"] + ["U"] * r)
        add_check(
            prototype_checks,
            f"relator_evaluates_to_identity_r{r}",
            evaluate_word(r, relation) == (Fraction(0), 0),
        )
        add_check(
            prototype_checks,
            f"first_relation_excess_at_relator_length_r{r}",
            item["first_relation_excess_length"] == r + 3,
        )
        add_check(
            prototype_checks,
            f"unit_marker_does_not_descend_r{r}",
            not markers[r]["unit_step_marker_descends"],
        )
        add_check(
            integration_checks,
            f"relation_is_primitive_r{r}",
            primitive_word(relation),
        )
        add_check(
            integration_checks,
            f"relation_is_cyclically_nonbacktracking_r{r}",
            cyclically_nonbacktracking(relation),
        )

    balanced_trace = evaluate_trace_counts(
        1, independent_counts[1], independent_free
    )
    add_check(
        prototype_checks,
        "balanced_commutation_first_excess_at_square_length",
        balanced_trace["first_relation_excess_length"] == 4,
    )
    add_check(
        prototype_checks,
        "balanced_commutation_unit_marker_descends",
        markers[1]["unit_step_marker_descends"],
    )

    for row in finite_summaries:
        tag = f"r{row['r']}_q{row['q']}"
        add_check(
            prototype_checks,
            f"boundary_squared_zero_{tag}",
            row["boundary_squared_zero_affine"]
            and row["boundary_squared_zero_complete"],
        )
        add_check(
            prototype_checks,
            f"complete_presentation_h1_zero_{tag}",
            row["h1_after_complete_presentation_cells"] == 0,
        )
        add_check(
            prototype_checks,
            f"affine_only_leaves_quotient_cycles_{tag}",
            row["h1_after_affine_cells"] > 0,
        )
    add_check(
        prototype_checks,
        "generic_two_generator_one_relator_scalar_lift_cancels_everything",
        graded["all_sampled_supertraces_zero"],
    )

    add_check(
        integration_checks,
        "source_free_counts_agree",
        independent_free == raw["free_identity_counts"],
    )
    for r in (1, *MAIN_R):
        add_check(
            integration_checks,
            f"source_affine_counts_agree_r{r}",
            independent_counts[r] == raw["affine_identity_counts"][str(r)],
        )
        add_check(
            integration_checks,
            f"source_marker_data_agree_r{r}",
            markers[r] == raw["marker_data"][str(r)],
        )
    for source_row, evaluator_row in zip(
        raw["finite_chain_data"], finite_independent
    ):
        add_check(
            integration_checks,
            f"source_finite_matrices_agree_r{source_row['r']}_q{source_row['q']}",
            source_row == evaluator_row,
        )

    expected_excess = {2: 10, 3: 12, 4: 14, 5: 32}
    for item in trace_items:
        first = item["first_relation_excess_length"]
        row = item["rows"][first]
        add_check(
            integration_checks,
            f"first_relation_excess_count_r{item['r']}",
            row["relation_excess"] == expected_excess[item["r"]],
        )
    add_check(
        integration_checks,
        "baseline_cycle_weight_exact",
        markers[4]["one_oriented_cycle_trace_weight"]
        == "1/70368744177664",
    )
    add_check(
        integration_checks,
        "prototype_semantic_check_count_exact",
        len(prototype_checks) == 33,
    )

    prototype_root = Path("/tmp/paper36_exact_prototype")
    prototype_rows = []
    for relative, expected_hash in PROTOTYPE_HASHES.items():
        path = prototype_root / relative
        actual_hash = digest(path) if path.is_file() else None
        prototype_rows.append(
            {
                "path": relative,
                "expected_sha256": expected_hash,
                "actual_sha256": actual_hash,
                "match": actual_hash == expected_hash,
            }
        )
        add_check(
            integration_checks,
            f"prototype_hash_{relative.replace('/', '_')}",
            actual_hash == expected_hash,
        )

    trace_rows: list[dict[str, object]] = []
    for item in trace_items:
        for row in item["rows"]:
            trace_rows.append(
                {
                    "r": item["r"],
                    "length": row["length"],
                    "affine_identity_words": row["affine_identity_words"],
                    "free_identity_words": row["free_identity_words"],
                    "relation_excess": row["relation_excess"],
                    "normalized_trace": row["normalized_trace"],
                    "analytic_log_determinant_coefficient": row[
                        "analytic_log_determinant_coefficient"
                    ],
                }
            )
    write_csv(
        result_dir / "trace_audit.csv",
        [
            "r",
            "length",
            "affine_identity_words",
            "free_identity_words",
            "relation_excess",
            "normalized_trace",
            "analytic_log_determinant_coefficient",
        ],
        trace_rows,
    )

    marker_rows = [
        {
            "r": r,
            "relation_word": markers[r]["relation_word"],
            "left_length": markers[r]["relation_side_lengths"][0],
            "right_length": markers[r]["relation_side_lengths"][1],
            "cycle_length": markers[r]["cycle_length"],
            "unit_step_marker_descends": str(
                markers[r]["unit_step_marker_descends"]
            ).lower(),
            "primitive": str(
                primitive_word(tuple(markers[r]["relation_word"]))
            ).lower(),
            "cyclically_nonbacktracking": str(
                cyclically_nonbacktracking(tuple(markers[r]["relation_word"]))
            ).lower(),
        }
        for r in (1, *MAIN_R)
    ]
    write_csv(
        result_dir / "marker_audit.csv",
        [
            "r",
            "relation_word",
            "left_length",
            "right_length",
            "cycle_length",
            "unit_step_marker_descends",
            "primitive",
            "cyclically_nonbacktracking",
        ],
        marker_rows,
    )

    operator_rows = []
    for r in (1, *MAIN_R):
        weight = Fraction(markers[r]["one_oriented_cycle_trace_weight"])
        operator_rows.append(
            {
                "r": r,
                "theta": "1/2",
                "cycle_length": markers[r]["cycle_length"],
                "origin_exponent_sum": markers[r]["origin_exponent_sum"],
                "one_cycle_weight": str(weight),
                "trace_lower_bound": str(markers[r]["cycle_length"] * weight),
                "strictly_positive": "true",
            }
        )
    write_csv(
        result_dir / "operator_cycle_audit.csv",
        [
            "r",
            "theta",
            "cycle_length",
            "origin_exponent_sum",
            "one_cycle_weight",
            "trace_lower_bound",
            "strictly_positive",
        ],
        operator_rows,
    )
    write_csv(
        result_dir / "finite_chain_audit.csv",
        list(finite_summaries[0]),
        finite_summaries,
    )

    generic_controls = [
        {
            "presentation": "affine_vu_equals_u_power_v",
            "cell_orbits": [1, 2, 1],
            "euler_multiplier": 0,
        },
        {
            "presentation": "balanced_commutation",
            "cell_orbits": [1, 2, 1],
            "euler_multiplier": 0,
        },
        {
            "presentation": "matched_arbitrary_two_generator_one_relator",
            "cell_orbits": [1, 2, 1],
            "euler_multiplier": 0,
        },
    ]
    graded["matched_generic_controls"] = generic_controls
    write_json(result_dir / "graded_control.json", graded)

    control_summary = {
        "schema": "SD-C38-control-summary-v1",
        "balanced_control": {
            "marker_descends": markers[1]["unit_step_marker_descends"],
            "first_relation_excess_length": balanced_trace[
                "first_relation_excess_length"
            ],
            "complete_finite_h1": finite_summaries[0][
                "h1_after_complete_presentation_cells"
            ],
        },
        "exponent_mutations": [
            {
                "r": r,
                "side_lengths": markers[r]["relation_side_lengths"],
                "marker_descends": markers[r]["unit_step_marker_descends"],
            }
            for r in MAIN_R
        ],
        "generic_presentations": generic_controls,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(result_dir / "control_summary.json", control_summary)

    all_checks = prototype_checks + integration_checks
    evaluation = {
        "schema": "SD-C38-independent-evaluation-v1",
        "candidate_id": "SD-C38",
        "prototype_semantic_checks": prototype_checks,
        "prototype_semantic_passed": sum(
            bool(row["pass"]) for row in prototype_checks
        ),
        "prototype_semantic_total": len(prototype_checks),
        "integration_checks": integration_checks,
        "integration_passed": sum(bool(row["pass"]) for row in integration_checks),
        "integration_total": len(integration_checks),
        "all_checks_pass": all(bool(row["pass"]) for row in all_checks),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    bridge = {
        "schema": "SD-C38-prototype-bridge-certificate-v1",
        "prototype_role": "research reference only; authority regenerated independently",
        "prototype_files": prototype_rows,
        "all_prototype_hashes_match": all(row["match"] for row in prototype_rows),
        "prototype_semantic_checks_passed": evaluation[
            "prototype_semantic_passed"
        ],
        "prototype_semantic_checks_total": evaluation[
            "prototype_semantic_total"
        ],
        "semantic_bridge_pass": evaluation["prototype_semantic_passed"]
        == evaluation["prototype_semantic_total"]
        == 33,
    }
    bridge["pass"] = bridge["all_prototype_hashes_match"] and bridge[
        "semantic_bridge_pass"
    ]
    write_json(result_dir / "evaluation.json", evaluation)
    write_json(result_dir / "prototype_bridge_certificate.json", bridge)
    print(
        json.dumps(
            {
                "all_checks_pass": evaluation["all_checks_pass"],
                "candidate_id": "SD-C38",
                "integration": f"{evaluation['integration_passed']}/{evaluation['integration_total']}",
                "prototype": f"{evaluation['prototype_semantic_passed']}/{evaluation['prototype_semantic_total']}",
            },
            sort_keys=True,
        )
    )
    return 0 if evaluation["all_checks_pass"] and bridge["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
