#!/usr/bin/env python3
"""Unit tests for the deterministic Paper-26 Round-2 experiment."""

from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

import round2_experiment as experiment


class ExactLedgerTests(unittest.TestCase):
    def test_eta_product_initial_coefficients(self) -> None:
        coefficients = experiment.level11_eta_product_coefficients(12)
        self.assertEqual(
            coefficients,
            [0, 1, -2, -1, 2, 1, 2, -2, 0, -2, -2, 1, -2],
        )

    def test_positive_parent_and_gamma0_11_counts(self) -> None:
        self.assertEqual(len(experiment.primitive_positive_necklaces(9)), 125)
        self.assertEqual(
            experiment.gamma0_11_positive_necklaces(9),
            [
                "LRRLRRR",
                "LLRLLRLR",
                "LLRRLRRR",
                "LLRRRLRR",
                "LRLRRRRR",
                "LLLRLLRLR",
                "LLLRLRLLR",
                "LLLRRLRRR",
                "LLLRRRLRR",
                "LLRLRRRRR",
                "LLRRRRRLR",
            ],
        )

    def test_matrix_owner_and_membership_are_exact(self) -> None:
        first = experiment.matrix_from_word("LRRLRRR")
        self.assertEqual(first, (15, 4, 11, 3))
        for word in experiment.gamma0_11_positive_necklaces(9):
            matrix = experiment.matrix_from_word(word)
            root, exponent = experiment.primitive_root(word)
            self.assertEqual(experiment.determinant(matrix), 1)
            self.assertEqual(matrix[2] % 11, 0)
            self.assertGreater(experiment.trace(matrix), 2)
            self.assertEqual(experiment.canonical_rotation(word), word)
            self.assertEqual((root, exponent), (word, 1))

    def test_axis_and_exact_repetition_geometry(self) -> None:
        matrix = experiment.matrix_from_word("LRRLRRR")
        geometry = experiment.axis_geometry(matrix)
        basepoint = geometry.point(geometry.length / 2.0)
        endpoint = geometry.point(-geometry.length / 2.0)
        self.assertLess(abs(experiment.mobius(matrix, basepoint) - endpoint), 1.0e-14)
        repeated = experiment.matrix_power(matrix, 2)
        self.assertLess(
            abs(experiment.geodesic_length(repeated) - 2.0 * geometry.length),
            1.0e-13,
        )


class NumericalProxyTests(unittest.TestCase):
    def test_axis_period_orientation_and_basepoint(self) -> None:
        matrix = experiment.matrix_from_word("LRRLRRR")
        coefficients = experiment.level11_eta_product_coefficients(96)
        forward = experiment.axis_one_form_period(matrix, coefficients, 128)
        reverse = experiment.axis_one_form_period(
            matrix, coefficients, 128, reverse_orientation=True
        )
        shifted = experiment.axis_one_form_period(
            matrix, coefficients, 128, basepoint_shift=0.125
        )
        self.assertAlmostEqual(forward, -0.634604652139776, places=13)
        self.assertLess(abs(forward + reverse), 1.0e-13)
        self.assertLess(abs(forward - shifted), 1.0e-13)

    def test_bounded_j_control_is_psl2z_invariant(self) -> None:
        z = complex(0.23, 1.17)
        translation = (1, 1, 0, 1)
        inversion = (0, -1, 1, 0)
        baseline = experiment.bounded_j_observable(z)
        self.assertLess(
            abs(baseline - experiment.bounded_j_observable(experiment.mobius(translation, z))),
            1.0e-12,
        )
        self.assertLess(
            abs(baseline - experiment.bounded_j_observable(experiment.mobius(inversion, z))),
            1.0e-12,
        )
        self.assertLessEqual(abs(baseline), 0.5)

    def test_two_small_runs_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as first_directory, tempfile.TemporaryDirectory() as second_directory:
            kwargs = {
                "max_word_length": 7,
                "q_cutoff": 64,
                "q_comparison_cutoff": 32,
                "quadrature_panels": 64,
                "repeat_q_cutoff": 512,
                "repeat_q_comparison_cutoff": 256,
                "repeat_quadrature_panels": 64,
            }
            first = Path(first_directory)
            second = Path(second_directory)
            experiment.build_outputs(first, **kwargs)
            experiment.build_outputs(second, **kwargs)
            first_files = sorted(path.name for path in first.iterdir())
            second_files = sorted(path.name for path in second.iterdir())
            self.assertEqual(first_files, second_files)
            for filename in first_files:
                self.assertEqual(
                    (first / filename).read_bytes(),
                    (second / filename).read_bytes(),
                    filename,
                )
            with (first / "newform_timechange_variation_ledger.csv").open(
                encoding="utf-8", newline=""
            ) as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue(rows)
            for row in rows:
                coefficient = float(
                    row["first_variation_coefficient_dT_depsilon_at_0"]
                )
                self.assertEqual(
                    coefficient, float(row["newform_axis_period_proxy"])
                )
                expected_sign = "POSITIVE" if coefficient > 0.0 else "NEGATIVE"
                self.assertEqual(row["first_variation_sign"], expected_sign)


if __name__ == "__main__":
    unittest.main(verbosity=2)
