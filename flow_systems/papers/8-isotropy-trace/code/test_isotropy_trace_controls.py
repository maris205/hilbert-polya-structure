#!/usr/bin/env python3
"""Regression tests for the deterministic Paper 8 control package."""

from __future__ import annotations

import json
import math
import shutil
import tempfile
import unittest
from pathlib import Path

from isotropy_trace_controls import (
    ARTIFACT_FILENAMES,
    EXPECTED_ACTIVE_TUPLE_HASHES,
    PEAK_INDICES,
    POISSON_LENGTHS,
    POISSON_THETAS,
    _clock_rows,
    _domain_rows,
    _linfinity_representative_rows,
    _nontrivial_phase_rows,
    _trace_scale_rows,
    _transverse_probability_rows,
    character_phase,
    exact_character_grid_average,
    numeric_character_grid_average,
    rank_one_peak_control,
    run,
    sha256,
    shifted_poisson_control,
    verify,
)


class ActiveConventionTests(unittest.TestCase):
    def test_active_tuple_matches_frozen_hashes(self) -> None:
        paper_dir = Path(__file__).resolve().parents[1]
        for relative, expected in EXPECTED_ACTIVE_TUPLE_HASHES.items():
            with self.subTest(relative=relative):
                self.assertEqual(sha256(paper_dir / relative), expected)

    def test_shifted_poisson_uses_minus_frequency_and_plus_return_phase(self) -> None:
        for length in POISSON_LENGTHS:
            for theta in POISSON_THETAS:
                with self.subTest(length=length, theta=theta):
                    control = shifted_poisson_control(length, theta)
                    self.assertLess(float(control["absolute_error"]), 2.0e-12)
                    self.assertLess(float(control["relative_error"]), 2.0e-12)
                    if theta not in (0.0, math.pi):
                        self.assertGreater(float(control["wrong_phase_error"]), 1.0e-4)

    def test_nontrivial_pi_over_two_phase_has_positive_imaginary_part(self) -> None:
        phase = character_phase(1, math.pi / 2.0)
        self.assertAlmostEqual(phase.real, 0.0, places=15)
        self.assertAlmostEqual(phase.imag, 1.0, places=15)
        witness = next(
            row
            for row in _nontrivial_phase_rows()
            if row["theta_name"] == "pi/2" and row["repetition"] == 1
        )
        self.assertEqual(witness["active_formula"], "exp(+i*r*theta)")
        self.assertEqual(witness["positive_sign_witness"], "true")


class CharacterGridTests(unittest.TestCase):
    def test_exact_modular_cancellation(self) -> None:
        for grid_size in (5, 7, 11):
            for repetition in range(-24, 25):
                expected = 1 if repetition % grid_size == 0 else 0
                with self.subTest(grid_size=grid_size, repetition=repetition):
                    self.assertEqual(
                        exact_character_grid_average(repetition, grid_size), expected
                    )
                    self.assertLess(
                        abs(
                            numeric_character_grid_average(repetition, grid_size)
                            - expected
                        ),
                        5.0e-15,
                    )

    def test_grid_larger_than_window_kills_every_nonzero_return_exactly(self) -> None:
        grid_size = 11
        repetition_window = range(-5, 6)
        self.assertEqual(exact_character_grid_average(0, grid_size), 1)
        self.assertTrue(
            all(
                exact_character_grid_average(repetition, grid_size) == 0
                for repetition in repetition_window
                if repetition != 0
            )
        )


class TraceScaleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = {row["profile"]: row for row in _trace_scale_rows()}

    def test_zero_time_is_exposed_by_regular_trace(self) -> None:
        row = self.rows["zero_only_compact_bump"]
        regular = float(row["regular_length_L_f0"])
        trivial = float(row["trivial_length_L_sum_r"])
        self.assertGreater(regular, 0.0)
        self.assertAlmostEqual(regular, trivial, places=15)
        self.assertEqual(row["positive_term_count"], 0)
        self.assertEqual(row["negative_term_count"], 0)

    def test_positive_time_removes_zero_and_negative_returns(self) -> None:
        row = self.rows["positive_only_compact_bump"]
        self.assertEqual(float(row["regular_length_L_f0"]), 0.0)
        self.assertEqual(row["negative_term_count"], 0)
        self.assertGreater(row["positive_term_count"], 0)
        self.assertAlmostEqual(
            float(row["trivial_length_L_sum_r"]),
            float(row["positive_length_L_sum_r_ge_1"]),
            places=15,
        )

    def test_regular_and_trivial_records_share_one_scale_change(self) -> None:
        for row in self.rows.values():
            with self.subTest(profile=row["profile"]):
                self.assertEqual(float(row["regular_common_scale_residual"]), 0.0)
                self.assertEqual(float(row["trivial_common_scale_residual"]), 0.0)
        row = self.rows["nonunit_length_two_sided"]
        length = float(row["length"])
        self.assertAlmostEqual(
            float(row["regular_length_L_f0"]),
            length * float(row["regular_probability_f0"]),
            places=15,
        )
        self.assertAlmostEqual(
            float(row["trivial_length_L_sum_r"]),
            length * float(row["trivial_probability_sum_r"]),
            places=15,
        )

    def test_trivial_and_regular_owners_are_not_conflated(self) -> None:
        row = self.rows["two_sided_compact_bump"]
        self.assertNotEqual(row["regular_owner"], row["trivial_owner"])
        self.assertNotAlmostEqual(
            float(row["regular_length_L_f0"]),
            float(row["trivial_length_L_sum_r"]),
            places=12,
        )


class FiniteCornerTests(unittest.TestCase):
    def test_shrinking_peaks_keep_character_value_and_lose_haar_mass(self) -> None:
        controls = [rank_one_peak_control(index) for index in PEAK_INDICES]
        self.assertEqual({control["point_value"] for control in controls}, {1.0})
        integrals = [float(control["haar_integral"]) for control in controls]
        self.assertTrue(
            all(left > right for left, right in zip(integrals, integrals[1:]))
        )
        self.assertLess(integrals[-1], 0.003)
        self.assertEqual(
            {control["linfinity_infimum_class"] for control in controls}, {0.0}
        )
        self.assertEqual(
            {control["pointwise_infimum_at_theta_zero"] for control in controls},
            {1.0},
        )

    def test_linfinity_representatives_have_same_class_but_different_point_values(self) -> None:
        zero, spike = _linfinity_representative_rows()
        self.assertEqual(zero["linfinity_class"], spike["linfinity_class"])
        self.assertEqual(zero["haar_integral"], spike["haar_integral"])
        self.assertNotEqual(
            zero["point_value_at_theta_zero"], spike["point_value_at_theta_zero"]
        )
        self.assertEqual(spike["differs_from_zero_only_on_null_set"], "true")
        self.assertEqual(
            spike["point_evaluation_well_defined_on_class"], "false"
        )


class FalsificationAndDomainTests(unittest.TestCase):
    def test_arbitrary_copy_and_composite_clocks_compile(self) -> None:
        rows = {row["clock_system"]: row for row in _clock_rows()}
        self.assertEqual(
            {row["analytic_mechanism_compiles"] for row in rows.values()}, {"true"}
        )
        self.assertEqual(
            float(rows["copied_clock_threefold"]["copy_additivity_residual"]),
            0.0,
        )
        self.assertIn(
            "provenance fails",
            str(rows["composite_augmented_clocks"]["arithmetic_provenance"]),
        )
        self.assertEqual(
            {row["fitting_used"] for row in rows.values()}, {"false"}
        )

    def test_transverse_probabilities_hide_from_time_only_but_not_full_observable(self) -> None:
        rows = _transverse_probability_rows()
        self.assertEqual({row["total_probability_exact"] for row in rows}, {"1"})
        self.assertEqual(
            {float(row["time_only_residual_from_unit_mass"]) for row in rows},
            {0.0},
        )
        three_atom = [row for row in rows if row["measure_model"] != "singleton"]
        self.assertEqual(
            len({row["full_observable_expectation_exact"] for row in three_atom}),
            3,
        )
        self.assertEqual(
            {row["full_trace_selected_canonically"] for row in rows}, {"false"}
        )

    def test_local_finite_and_positive_time_domains_stay_separate(self) -> None:
        rows = {row["domain_id"]: row for row in _domain_rows()}
        self.assertEqual(len(rows), 3)
        self.assertEqual(
            rows["local_one_orbit_two_sided"]["zero_time_included"], "true"
        )
        self.assertEqual(
            rows["local_one_orbit_two_sided"]["negative_time_included"], "true"
        )
        self.assertEqual(
            rows["finite_prime_support_positive"]["finite_prime_support"], "true"
        )
        positive = rows["all_prime_positive_time_distribution"]
        self.assertEqual(positive["zero_time_included"], "false")
        self.assertEqual(positive["negative_time_included"], "false")
        self.assertEqual(positive["locally_finite"], "true")
        self.assertGreater(positive["component_count"], 0)
        self.assertGreater(positive["return_term_count"], 0)
        self.assertEqual(
            {row["global_operator_asserted"] for row in rows.values()}, {"false"}
        )
        self.assertEqual(
            {row["cstar_trace_asserted"] for row in rows.values()}, {"false"}
        )


class ReproductionTests(unittest.TestCase):
    def test_outputs_manifest_and_two_generations_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as first_tmp, tempfile.TemporaryDirectory() as second_tmp:
            first = Path(first_tmp)
            second = Path(second_tmp)
            first_manifest = run(first)
            second_manifest = run(second)
            self.assertEqual(first_manifest, second_manifest)
            self.assertEqual(first_manifest["regression_status"], "PASS")
            self.assertEqual(set(first_manifest["artifacts"]), set(ARTIFACT_FILENAMES))
            for filename in (*ARTIFACT_FILENAMES, "isotropy_trace_manifest.json"):
                self.assertEqual((first / filename).read_bytes(), (second / filename).read_bytes())
            self.assertEqual(verify(first), first_manifest)
            self.assertEqual(verify(second), second_manifest)

    def test_manifest_detects_artifact_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            target = output / ARTIFACT_FILENAMES[0]
            target.write_bytes(target.read_bytes() + b"tamper\n")
            with self.assertRaisesRegex(ValueError, "artifact SHA-256 mismatch"):
                verify(output)

    def test_manifest_validates_implementation_hashes(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper8-copy"
            for directory in ("code", "experiments", "results"):
                shutil.copytree(
                    source_paper / directory,
                    copied_paper / directory,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
                )
            (copied_paper / "notes").mkdir()
            for relative in EXPECTED_ACTIVE_TUPLE_HASHES:
                source = source_paper / relative
                shutil.copy2(source, copied_paper / relative)
            output = copied_paper / "results"
            manifest = run(output, paper_dir=copied_paper)
            self.assertEqual(verify(output, paper_dir=copied_paper), manifest)
            readme = copied_paper / "code" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\ntampered copy\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                ValueError, "implementation SHA-256 mismatch"
            ):
                verify(output, paper_dir=copied_paper)

    def test_manifest_contains_no_timestamp_or_external_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            manifest = json.loads(
                (output / "isotropy_trace_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            determinism = manifest["determinism"]
            self.assertFalse(determinism["timestamps"])
            self.assertFalse(determinism["network"])
            self.assertFalse(determinism["randomness"])
            self.assertFalse(determinism["target_zero_data"])
            self.assertFalse(determinism["fitting"])
            self.assertEqual(
                determinism["python_dependencies"], "standard_library_only"
            )
            self.assertIn("not mathematical proofs", manifest["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
