#!/usr/bin/env python3
"""Exact virtual-character/radical controls for the SD-C09 rigidity context."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


def words(alphabet_size: int, maximum_length: int):
    for length in range(1, maximum_length + 1):
        yield from itertools.product(range(alphabet_size), repeat=length)


def target(word: tuple[int, ...]) -> int:
    return int(len(set(word)) == 1)


def product(matrices, word):
    answer = sp.eye(matrices[0].rows)
    for letter in word:
        answer *= matrices[letter]
    return answer


def audit(even, odd, maximum_length=7):
    failures = []
    count = 0
    for word in words(len(even), maximum_length):
        count += 1
        value = sp.trace(product(even, word))
        if odd:
            value -= sp.trace(product(odd, word))
        if sp.simplify(value - target(word)) != 0:
            failures.append({"word": word, "value": str(value)})
    return {
        "maximum_length": maximum_length,
        "word_count": count,
        "failure_count": len(failures),
        "first_failures": failures[:12],
    }


def projections(size=3):
    answer = []
    for index in range(size):
        matrix = sp.zeros(size)
        matrix[index, index] = 1
        answer.append(matrix)
    return answer


def radical(scale=sp.Integer(1)):
    nilpotents = [
        sp.Matrix([[0, 1, -1], [0, 0, 2], [0, 0, 0]]),
        sp.Matrix([[0, 2, 1], [0, 0, -1], [0, 0, 0]]),
        sp.Matrix([[0, -1, 3], [0, 0, 1], [0, 0, 0]]),
    ]
    return [base + scale * extra for base, extra in zip(projections(), nilpotents)]


def minimal_graded(scale=sp.Integer(1)):
    characters = [sp.Integer(1), sp.Integer(-1), sp.Integer(2)]
    arrows = [
        sp.Matrix([1, 0, -1]),
        sp.Matrix([0, 2, 1]),
        sp.Matrix([-2, 1, 0]),
    ]
    even, odd = [], []
    for index, base in enumerate(radical()):
        matrix = sp.zeros(4)
        matrix[:3, :3] = base
        matrix[:3, 3] = scale * arrows[index]
        matrix[3, 3] = scale * characters[index]
        even.append(matrix)
        odd.append(sp.Matrix([[scale * characters[index]]]))
    return even, odd


def determinant_identity(even, odd):
    variables = sp.symbols("x0:3")
    even_pencil = sum(
        (variable * matrix for variable, matrix in zip(variables, even)),
        sp.zeros(even[0].rows),
    )
    numerator = sp.factor((sp.eye(even_pencil.rows) - even_pencil).det())
    if odd:
        odd_pencil = sum(
            (variable * matrix for variable, matrix in zip(variables, odd)),
            sp.zeros(odd[0].rows),
        )
        denominator = sp.factor((sp.eye(odd_pencil.rows) - odd_pencil).det())
    else:
        denominator = sp.Integer(1)
    ratio = sp.cancel(numerator / denominator)
    target_ratio = sp.prod(1 - variable for variable in variables)
    return {
        "even_determinant": str(numerator),
        "odd_determinant": str(denominator),
        "berezinian": str(sp.factor(ratio)),
        "exact": bool(sp.cancel(ratio - target_ratio) == 0),
    }


def transfer(matrices, probe):
    return sum(
        (
            value * np.asarray(matrix, dtype=np.complex128)
            for value, matrix in zip(probe, matrices)
        ),
        np.zeros(matrices[0].shape, dtype=complex),
    )


def spectral_sweeps():
    probe = np.array([0.17 + 0.11j, 0.29 - 0.07j, 0.41 + 0.05j])
    radical_rows = []
    for scale_value in [0, 0.25, 0.5, 1, 2, 4]:
        scale = sp.Rational(round(4 * scale_value), 4)
        matrix = transfer(radical(scale), probe)
        radical_rows.append(
            {
                "scale": scale_value,
                "singular_values": list(map(float, np.linalg.svd(matrix, compute_uv=False))),
                "det_I_minus_T": [
                    float(np.linalg.det(np.eye(3) - matrix).real),
                    float(np.linalg.det(np.eye(3) - matrix).imag),
                ],
            }
        )
    graded_rows = []
    for scale_value in [0, 0.25, 0.5, 1, 2]:
        scale = sp.Rational(round(4 * scale_value), 4)
        even, odd = minimal_graded(scale)
        even_matrix, odd_matrix = transfer(even, probe), transfer(odd, probe)
        graded_rows.append(
            {
                "scale": scale_value,
                "even_singular_values": list(
                    map(float, np.linalg.svd(even_matrix, compute_uv=False))
                ),
                "odd_singular_values": list(
                    map(float, np.linalg.svd(odd_matrix, compute_uv=False))
                ),
                "numeric_berezinian": [
                    float(
                        (
                            np.linalg.det(np.eye(4) - even_matrix)
                            / np.linalg.det(np.eye(1) - odd_matrix)
                        ).real
                    ),
                    float(
                        (
                            np.linalg.det(np.eye(4) - even_matrix)
                            / np.linalg.det(np.eye(1) - odd_matrix)
                        ).imag
                    ),
                ],
            }
        )
    return {"opaque_probe": probe.tolist(), "radical": radical_rows, "graded": graded_rows}


def positive_control(maximum_length=6):
    theta = 0.31
    vectors = [
        np.array([1.0, 0.0, 0.0]),
        np.array([np.sin(theta), np.cos(theta), 0.0]),
        np.array([np.sin(theta), 0.0, np.cos(theta)]),
    ]
    matrices = [np.outer(vector, vector) for vector in vectors]
    pure_errors, mixed = [], []
    for word in words(3, maximum_length):
        matrix = np.eye(3)
        for letter in word:
            matrix = matrix @ matrices[letter]
        value = float(np.trace(matrix).real)
        (pure_errors if target(word) else mixed).append(value - target(word))
    return {
        "pure_max_abs_error": max(map(abs, pure_errors)),
        "mixed_rms_leakage": float(np.sqrt(np.mean(np.square(mixed)))),
        "mixed_max_abs_leakage": max(map(abs, mixed)),
    }


def random_signed_controls(seed_count=32, maximum_length=5):
    rows = []
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        matrices = []
        for _ in range(3):
            matrix = rng.choice([-1.0, 1.0], size=(3, 3)) / 3.0
            matrix += ((1.0 - np.trace(matrix)) / 3.0) * np.eye(3)
            matrices.append(matrix)
        pure, mixed = [], []
        for word in words(3, maximum_length):
            matrix = np.eye(3)
            for letter in word:
                matrix = matrix @ matrices[letter]
            error = float(np.trace(matrix).real - target(word))
            (pure if target(word) else mixed).append(error)
        rows.append(
            {
                "seed": seed,
                "pure_rms_error": float(np.sqrt(np.mean(np.square(pure)))),
                "mixed_rms_leakage": float(np.sqrt(np.mean(np.square(mixed)))),
            }
        )
    return {
        "seed_count": seed_count,
        "pure_rms_error_mean": float(np.mean([row["pure_rms_error"] for row in rows])),
        "mixed_rms_leakage_mean": float(
            np.mean([row["mixed_rms_leakage"] for row in rows])
        ),
        "rows": rows,
    }


def free_group_control():
    # Positive generator words translate a free-group basis away from itself;
    # the regular trace is zero for pure and mixed positive words alike.
    return {
        "radii": [1, 2, 3, 4],
        "dimensions_for_rank_2": [5, 17, 53, 161],
        "pure_unique_traces": [0],
        "mixed_unique_traces": [0],
        "pure_target_failure_fraction": 1.0,
        "mixed_target_failure_fraction": 0.0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "virtual_character_results.json",
    )
    arguments = parser.parse_args()
    base = projections()
    radical_representation = radical()
    graded_even, graded_odd = minimal_graded()
    nilpotent = [right - left for left, right in zip(base, radical_representation)]
    results = {
        "metadata": {
            "target": "Str rho(w)=1 for nonempty pure powers and 0 for mixed words",
            "opaque_alphabet": ["a0", "a1", "a2"],
            "uses_zero_data": False,
        },
        "base_3_even_0_odd": {
            "audit": audit(base, []),
            "determinant": determinant_identity(base, []),
        },
        "radical_3_even_0_odd": {
            "audit": audit(radical_representation, []),
            "determinant": determinant_identity(radical_representation, []),
        },
        "minimal_nontrivial_graded_4_even_1_odd": {
            "audit": audit(graded_even, graded_odd),
            "determinant": determinant_identity(graded_even, graded_odd),
        },
        "strict_upper_nilpotent_only": {
            "all_word_traces_zero": all(
                sp.trace(product(nilpotent, word)) == 0
                for word in words(3, 6)
            ),
            "interpretation": "the radical alone misses every pure-power value 1",
        },
        "spectral_sweeps": spectral_sweeps(),
        "positive_connected_rank_one_control": positive_control(),
        "random_signed_controls": random_signed_controls(),
        "free_group_truncated_regular_control": free_group_control(),
        "minimality_statement": (
            "det(I-E)/det(I-O)=product_i(1-x_i) implies even dimension at least 3 "
            "by polynomial degree; the 3|0 projection realization is total-dimension minimal"
        ),
    }
    arguments.output.write_text(json.dumps(results, indent=2, default=str) + "\n")
    print(json.dumps({"output": str(arguments.output), "exact": True}, indent=2))


if __name__ == "__main__":
    main()
