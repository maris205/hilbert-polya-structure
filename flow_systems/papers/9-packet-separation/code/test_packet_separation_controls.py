#!/usr/bin/env python3
"""Regression tests for the deterministic Paper 9 control package."""

from __future__ import annotations

import json
import os
import shutil
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from packet_separation_controls import (
    ARTIFACT_FILENAMES,
    EXPECTED_ACTIVE_TUPLE_HASHES,
    ILLEGAL_LEVELS,
    LEVELS,
    PRIMES,
    _action_sign_rows,
    _approximation_rows,
    _distinctness_rows,
    _finite_character_rows,
    _illegal_kernel_rows,
    _prime_summary_rows,
    _pz_circle_rows,
    _unit_normalization_rows,
    approximation_cases,
    cyclic_subgroup,
    is_fractional_power_of_prime,
    run,
    sha256,
    transverse_distinctness_witness,
    verify,
)


class ActiveLockTests(unittest.TestCase):
    def test_active_tuple_matches_frozen_hashes(self) -> None:
        paper_dir = Path(__file__).resolve().parents[1]
        for relative, expected in EXPECTED_ACTIVE_TUPLE_HASHES.items():
            with self.subTest(relative=relative):
                self.assertEqual(sha256(paper_dir / relative), expected)


class SimultaneousApproximationTests(unittest.TestCase):
    def test_every_q_residue_and_exact_real_bound(self) -> None:
        cases = approximation_cases()
        self.assertEqual(len(cases), len(PRIMES) * len(LEVELS))
        for case in cases:
            with self.subTest(prime=case["prime"], level=case["level"]):
                modulus = int(case["modulus"])
                denominator = int(case["denominator"])
                numerator = int(case["numerator"])
                target = int(case["target_residue"])
                self.assertEqual(
                    numerator * pow(denominator, -1, modulus) % modulus,
                    target,
                )
                self.assertEqual(
                    numerator % modulus,
                    target
                    * pow(int(case["prime"]), int(case["denominator_exponent"]), modulus)
                    % modulus,
                )
                self.assertLessEqual(case["real_error"], case["nearest_bound"])
                self.assertLessEqual(case["real_error"], case["error_goal"])
                self.assertGreater(numerator, 0)

    def test_q_residue_is_not_replaced_by_numerator_residue(self) -> None:
        rows = _approximation_rows()
        self.assertTrue(
            any(
                int(row["numerator_residue"])
                != int(row["target_rational_residue"])
                for row in rows
            )
        )
        self.assertEqual(
            {row["numerator_convergence_assumed"] for row in rows}, {"false"}
        )

    def test_error_goals_shrink_for_every_prime(self) -> None:
        cases = approximation_cases()
        for prime in PRIMES:
            selected = [case for case in cases if case["prime"] == prime]
            goals = [Fraction(case["error_goal"]) for case in selected]
            self.assertTrue(all(left > right for left, right in zip(goals, goals[1:])))
            self.assertLessEqual(selected[-1]["real_error"], Fraction(1, 10**9))


class FiniteCharacterTests(unittest.TestCase):
    def test_character_values_match_exactly_in_one_fixed_stage(self) -> None:
        rows = _finite_character_rows()
        self.assertEqual(len(rows), len(PRIMES) * sum(LEVELS))
        for row in rows:
            with self.subTest(prime=row["prime"], order=row["cyclic_order"]):
                self.assertEqual(row["character_match_exact"], "true")
                self.assertEqual(float(row["character_value_error"]), 0.0)
                self.assertEqual(int(row["kernel_on_cyclic_group"]), 1)
                self.assertGreaterEqual(int(row["global_kernel_order_prime_to_p"]), 1)
                self.assertEqual(row["global_kernel_finite"], "true")
                self.assertEqual(row["source_stage"], "one fixed initial p-fibre")

    def test_rational_denominator_is_invertible_on_each_cyclic_order(self) -> None:
        for case in approximation_cases():
            denominator = int(case["denominator"])
            for order in case["component_moduli"]:
                with self.subTest(prime=case["prime"], order=order):
                    self.assertEqual(
                        denominator * pow(denominator, -1, int(order)) % int(order),
                        1,
                    )


class ActionAndCircleTests(unittest.TestCase):
    def test_inverse_action_converges_to_v_and_wrong_sign_stays_separated(self) -> None:
        rows = _action_sign_rows()
        self.assertEqual(len(rows), len(PRIMES) * len(LEVELS))
        self.assertLess(max(float(row["correct_time_error"]) for row in rows), 5.0e-4)
        final = [row for row in rows if int(row["level"]) == max(LEVELS)]
        self.assertGreater(min(float(row["wrong_time_error"]) for row in final), 0.1)
        self.assertEqual(
            {row["active_action"] for row in rows},
            {"(P,u)q=(F_qP,q^-1u)"},
        )

    def test_correct_time_error_tightens_at_the_final_level(self) -> None:
        rows = _action_sign_rows()
        for prime in PRIMES:
            selected = [row for row in rows if int(row["prime"]) == prime]
            self.assertLess(
                float(selected[-1]["correct_time_error"]),
                float(selected[0]["correct_time_error"]),
            )

    def test_pz_only_control_has_exact_distinctness_and_positive_circle_distance(self) -> None:
        rows = _pz_circle_rows()
        self.assertEqual(len(rows), len(PRIMES))
        for row in rows:
            with self.subTest(prime=row["prime"]):
                ratio = Fraction(row["time_ratio_exact"])
                belongs, _ = is_fractional_power_of_prime(ratio, int(row["prime"]))
                self.assertFalse(belongs)
                self.assertEqual(row["ratio_in_pZ"], "false")
                self.assertGreater(float(row["standard_circle_distance"]), 0.0)
                self.assertEqual(row["away_p_approximation_channel"], "absent")
                self.assertIn("not prove Hausdorffness", row["scope"])


class NormalizationAndDistinctnessTests(unittest.TestCase):
    def test_unit_normalization_preserves_exponent_and_time_exactly(self) -> None:
        rows = _unit_normalization_rows()
        self.assertEqual(len(rows), len(PRIMES) * 4)
        for row in rows:
            with self.subTest(prime=row["prime"], factor=row["finite_kernel_factor_nu"]):
                self.assertEqual(int(row["unit_gcd_with_modulus"]), 1)
                self.assertEqual(row["time_match_exact"], "true")
                self.assertEqual(row["exponent_match_exact"], "true")
                self.assertEqual(
                    int(row["exponent_after_action"]),
                    int(row["target_finite_exponent"]),
                )

    def test_transverse_witness_is_outside_finite_p_power_image(self) -> None:
        for prime in PRIMES:
            witness = transverse_distinctness_witness(prime)
            subgroup = cyclic_subgroup(prime % int(witness["modulus"]), int(witness["modulus"]))
            self.assertNotIn(int(witness["witness"]), subgroup)

    def test_distinctness_rows_separate_positive_and_negative_controls(self) -> None:
        rows = _distinctness_rows()
        self.assertEqual(len(rows), len(PRIMES) * 3)
        for prime in PRIMES:
            selected = {
                row["witness_type"]: row
                for row in rows
                if int(row["prime"]) == prime
            }
            self.assertEqual(selected["time_distinct"]["distinct_exact"], "true")
            self.assertEqual(selected["transverse_distinct"]["distinct_exact"], "true")
            self.assertEqual(
                selected["galois_equivalent_control"]["equivalent_under_locked_relation"],
                "true",
            )
            self.assertEqual(
                selected["galois_equivalent_control"]["distinct_exact"], "false"
            )


class IllegalKernelAndPrimeUniformityTests(unittest.TestCase):
    def test_illegal_prefix_kernel_lower_bound_grows(self) -> None:
        rows = _illegal_kernel_rows()
        self.assertEqual(len(rows), len(PRIMES) * len(ILLEGAL_LEVELS) * 2)
        for prime in PRIMES:
            illegal = [
                row
                for row in rows
                if int(row["prime"]) == prime
                and row["profile"] == "illegal_uniformizer_components"
            ]
            bounds = [int(row["kernel_lower_bound"]) for row in illegal]
            self.assertTrue(all(left < right for left, right in zip(bounds, bounds[1:])))
            self.assertEqual({row["full_endpoint_in_Ef"] for row in illegal}, {"false"})
            self.assertEqual({row["finite_prefix_only"] for row in illegal}, {"true"})

    def test_unit_prefix_control_has_no_component_kernel_growth(self) -> None:
        legal = [
            row
            for row in _illegal_kernel_rows()
            if row["profile"] == "legal_unit_components"
        ]
        self.assertEqual({int(row["kernel_lower_bound"]) for row in legal}, {1})
        self.assertEqual({row["full_endpoint_in_Ef"] for row in legal}, {"true"})

    def test_same_control_family_runs_for_several_primes_without_statistical_claim(self) -> None:
        rows = _prime_summary_rows()
        self.assertEqual([int(row["prime"]) for row in rows], list(PRIMES))
        self.assertEqual({row["all_rational_residues_match"] for row in rows}, {"true"})
        self.assertEqual({row["all_character_values_match"] for row in rows}, {"true"})
        self.assertEqual({row["all_unit_normalizations_match"] for row in rows}, {"true"})
        self.assertEqual({row["theorem_uniformity_claimed"] for row in rows}, {"false"})
        self.assertEqual({row["statistical_evidence_claimed"] for row in rows}, {"false"})


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
            for filename in (*ARTIFACT_FILENAMES, "packet_separation_manifest.json"):
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
            copied_paper = Path(tmp) / "paper9-copy"
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
            with self.assertRaisesRegex(ValueError, "implementation SHA-256 mismatch"):
                verify(output, paper_dir=copied_paper)

    def test_manifest_has_exact_rows_metrics_and_no_hidden_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = run(output)
            self.assertEqual(manifest["metrics"]["total_csv_rows"], 240)
            self.assertEqual(manifest["metrics"]["max_finite_character_value_error"], "0")
            self.assertTrue(manifest["metrics"]["all_rational_residues_match"])
            self.assertTrue(manifest["metrics"]["all_finite_character_values_match"])
            determinism = manifest["determinism"]
            for key in (
                "network",
                "randomness",
                "external_datasets",
                "target_zero_data",
                "fitting",
                "timestamps",
            ):
                self.assertFalse(determinism[key])
            self.assertEqual(determinism["python_dependencies"], "standard_library_only")
            self.assertIn("not mathematical proofs", manifest["interpretation_boundary"])
            serialized = json.dumps(manifest, sort_keys=True).lower()
            self.assertNotIn("riemann zero value", serialized)

    def test_bytecode_is_disabled_in_reproduction_environment(self) -> None:
        self.assertEqual(os.environ.get("PYTHONDONTWRITEBYTECODE"), "1")


if __name__ == "__main__":
    unittest.main()
