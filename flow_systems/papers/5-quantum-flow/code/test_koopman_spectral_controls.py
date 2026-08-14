#!/usr/bin/env python3
import csv
import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from koopman_spectral_controls import (
    affine_irreducible_count_f2,
    fixed_point_count_p1_f2,
    frequency_witnesses,
    integer_divisors,
    moebius,
    positivity_lower_bound_numerator,
    projective_closed_point_count,
    recovered_fixed_point_count,
    run,
    weighted_unitary_control,
)


class ArithmeticDegreeTest(unittest.TestCase):
    def test_divisors_and_moebius(self) -> None:
        self.assertEqual(integer_divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(
            [moebius(value) for value in range(1, 11)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
        )

    def test_known_closed_point_counts(self) -> None:
        expected_affine = [2, 1, 2, 3, 6, 9, 18, 30, 56, 99]
        observed_affine = [
            affine_irreducible_count_f2(degree) for degree in range(1, 11)
        ]
        self.assertEqual(observed_affine, expected_affine)
        self.assertEqual(projective_closed_point_count(1), 3)
        self.assertEqual(
            [projective_closed_point_count(degree) for degree in range(2, 11)],
            expected_affine[1:],
        )

    def test_positivity_bound(self) -> None:
        for degree in range(2, 65):
            self.assertGreater(positivity_lower_bound_numerator(degree), 0)
            self.assertGreater(projective_closed_point_count(degree), 0)

    def test_fixed_point_reconstruction(self) -> None:
        counts = {
            degree: projective_closed_point_count(degree)
            for degree in range(1, 25)
        }
        for extension_degree in range(1, 25):
            self.assertEqual(
                recovered_fixed_point_count(extension_degree, counts),
                fixed_point_count_p1_f2(extension_degree),
            )


class FrequencyMultiplicityTest(unittest.TestCase):
    def test_positive_negative_and_zero_witnesses(self) -> None:
        for rational_frequency in (
            Fraction(0, 1),
            Fraction(1, 2),
            Fraction(-2, 3),
            Fraction(5, 4),
        ):
            rows = frequency_witnesses(rational_frequency, 20)
            self.assertEqual(len(rows), 20)
            self.assertEqual(len({row["degree"] for row in rows}), 20)
            self.assertTrue(all(row["frequency_match"] for row in rows))
            self.assertTrue(all(row["closed_point_exists"] for row in rows))

    def test_nonzero_witnesses_survive_kernel_deletion(self) -> None:
        rows = frequency_witnesses(Fraction(1, 2), 30)
        self.assertTrue(all(row["fourier_mode"] != 0 for row in rows))
        self.assertTrue(all(row["mode_over_degree"] == "1/2" for row in rows))


class WeightEquivalenceTest(unittest.TestCase):
    def test_finite_fourier_regression(self) -> None:
        rows, summary = weighted_unitary_control()
        self.assertEqual(len(rows), 4)
        self.assertLess(summary["norm_error"], 1e-14)
        self.assertLess(summary["max_intertwiner_error"], 1e-14)


class ArtifactTest(unittest.TestCase):
    def test_run_writes_self_consistent_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output_dir = Path(temporary)
            manifest = run(output_dir, max_degree=16, witness_count=8)
            self.assertTrue(manifest["all_closed_point_counts_positive"])
            self.assertTrue(manifest["all_positivity_bounds_positive"])
            self.assertTrue(manifest["all_fixed_point_ledgers_match"])
            self.assertTrue(manifest["all_frequency_witnesses_match"])
            self.assertTrue(manifest["all_frequency_witness_degrees_exist"])
            self.assertTrue(
                manifest["nonzero_frequency_control_survives_kernel_deletion"]
            )
            self.assertTrue(manifest["weight_unitary_control_pass"])
            self.assertEqual(
                manifest["limited_route_b"]["b1"],
                "B1_COMPLETE_OPERATOR_DEFINITION",
            )
            self.assertEqual(
                manifest["limited_route_b"]["b2"], "B2_SELF_ADJOINT"
            )
            self.assertEqual(manifest["limited_route_b"]["b3"], "B3_FAIL")
            self.assertFalse(manifest["b4_b5_invoked"])
            self.assertFalse(manifest["target_zero_data_used"])
            self.assertNotIn("b4", manifest["limited_route_b"])
            self.assertNotIn("b5", manifest["limited_route_b"])

            for artifact_name, expected_hash in manifest["artifacts"].items():
                artifact_path = output_dir / artifact_name
                self.assertTrue(artifact_path.is_file())
                self.assertEqual(len(expected_hash), 64)

            stored = json.loads(
                (output_dir / "koopman_spectral_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(stored, manifest)

            with (output_dir / "closed_point_degree_controls.csv").open(
                newline="", encoding="utf-8"
            ) as handle:
                closed_rows = list(csv.DictReader(handle))
            self.assertEqual(len(closed_rows), 16)
            self.assertTrue(all(row["positive"] == "True" for row in closed_rows))
            self.assertTrue(
                all(row["fixed_point_match"] == "True" for row in closed_rows)
            )


if __name__ == "__main__":
    unittest.main()

