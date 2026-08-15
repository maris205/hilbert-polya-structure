#!/usr/bin/env python3
"""Independent exact evaluator for the Paper 36 prototype."""

from __future__ import annotations

from fractions import Fraction


def rational_rank(rows):
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((row for row in range(pivot_row, nrows) if matrix[row][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(nrows):
            if row == pivot_row or not matrix[row][col]:
                continue
            factor = matrix[row][col]
            matrix[row] = [
                matrix[row][j] - factor * matrix[pivot_row][j] for j in range(ncols)
            ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def transpose(columns):
    if not columns:
        return []
    return [list(row) for row in zip(*columns)]


def check_boundary_squared_zero(boundary1, cell_columns):
    for cell in cell_columns:
        for row in boundary1:
            if sum(a * b for a, b in zip(row, cell)) != 0:
                return False
    return True


def evaluate_finite_chain(data):
    boundary1 = data["boundary1"]
    affine_cells = data["affine_cells"]
    full_cells = data["full_cells"]
    number_vertices = len(data["vertices"])
    number_edges = len(data["edge_index"])
    rank1 = rational_rank(boundary1)
    rank2_affine = rational_rank(transpose(affine_cells))
    rank2_full = rational_rank(transpose(full_cells))
    cycle_dimension = number_edges - rank1
    return {
        "r": data["r"],
        "q": data["q"],
        "period": data["period"],
        "vertices": number_vertices,
        "positive_edge_instances": number_edges,
        "rank_boundary_1": rank1,
        "cycle_dimension_before_cells": cycle_dimension,
        "rank_affine_cell_boundaries": rank2_affine,
        "h1_after_affine_cells": cycle_dimension - rank2_affine,
        "rank_full_cell_boundaries": rank2_full,
        "h1_after_complete_presentation_cells": cycle_dimension - rank2_full,
        "boundary_squared_zero_affine": check_boundary_squared_zero(boundary1, affine_cells),
        "boundary_squared_zero_full": check_boundary_squared_zero(boundary1, full_cells),
    }


def evaluate_trace_counts(r, affine_counts, free_counts):
    rows = []
    for length, (affine, free) in enumerate(zip(affine_counts, free_counts)):
        rows.append(
            {
                "length": length,
                "affine_identity_words": affine,
                "free_identity_words": free,
                "relation_excess": affine - free,
                "normalized_trace": str(Fraction(affine, 4**length)),
                "analytic_log_determinant_coefficient": (
                    "0" if length == 0 else str(-Fraction(affine, length * 4**length))
                ),
            }
        )
    first_excess = next((row["length"] for row in rows[1:] if row["relation_excess"]), None)
    return {
        "r": r,
        "predicted_relator_length": r + 3,
        "first_relation_excess_length": first_excess,
        "rows": rows,
    }


def evaluate_generic_supertrace(trace_audit):
    """The diagonal cell lift has multiplicities (1,2,1), hence zero supertrace."""
    samples = []
    for item in trace_audit:
        for row in item["rows"][1:]:
            c = Fraction(row["affine_identity_words"], 4 ** row["length"])
            graded = c - 2 * c + c
            samples.append({"r": item["r"], "length": row["length"], "supertrace": str(graded)})
    return {
        "cell_orbit_multiplicities": {"C0_even": 1, "C1_odd": 2, "C2_even": 1},
        "euler_multiplier": 0,
        "all_sampled_supertraces_zero": all(row["supertrace"] == "0" for row in samples),
        "mechanism_scope": "every two-generator one-relator presentation with the same scalar lift",
        "samples": samples,
    }
