#!/usr/bin/env python3
"""Independent standard-library tests for P26 Round 5."""

from __future__ import annotations

from collections import defaultdict
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name("round5_zeta_variation.py")
SPEC = importlib.util.spec_from_file_location("p26_round5", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round5_zeta_variation.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ZetaVariationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cycle_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER)
        cls.period_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_PERIOD_SUMMARY)
        cls.grouped = MODULE.grouped_cycle_rows(cls.cycle_rows)
        cls.periods = MODULE.period_summary_map(cls.period_rows)
        cls.repetition_rows = MODULE.build_repetition_ledger(cls.cycle_rows)
        cls.moment_rows = MODULE.build_degree_moment_ledger(
            cls.grouped, cls.periods
        )
        cls.variation_rows = MODULE.build_hecke_variation_ledger(
            cls.grouped, cls.periods
        )

    def test_round4_inputs_are_source_locked_and_valid(self) -> None:
        self.assertEqual(len(self.cycle_rows), 138)
        self.assertEqual(len(self.period_rows), 55)
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER),
            "f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662",
        )
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_PERIOD_SUMMARY),
            "c5de5c16c86d8db6ce7438c122deddb927d934bf0198fe3f72af4cbaf1233679",
        )
        self.assertEqual(
            MODULE.validate_round4_inputs(self.cycle_rows, self.period_rows), []
        )

    def test_cycle_degree_sets_length_but_not_zeta_repetition(self) -> None:
        degrees = set()
        repetitions = set()
        for row in self.repetition_rows:
            degrees.add(int(row["hecke_cycle_degree_d"]))
            repetitions.add(int(row["zeta_repetition_r"]))
            expected = (
                int(row["zeta_repetition_r"])
                * float(row["primitive_base_length"])
            )
            self.assertAlmostEqual(float(row["repeated_base_length"]), expected)
        self.assertEqual(repetitions, {1, 2, 3, 4})
        self.assertIn(13, degrees)
        self.assertTrue(
            all(
                row["primitive_in_gamma0_11_exact"] == "true"
                for row in self.repetition_rows
            )
        )

    def test_log_weight_cancels_repetition_factor_in_derivative(self) -> None:
        self.assertEqual(len(self.repetition_rows), 1104)
        self.assertLessEqual(
            max(float(row["ruelle_formula_residual"]) for row in self.repetition_rows),
            1.0e-15,
        )
        self.assertLessEqual(
            max(float(row["selberg_formula_residual"]) for row in self.repetition_rows),
            1.0e-15,
        )

    def test_inverse_orientation_pairs_cancel_exactly(self) -> None:
        paired: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
        for row in self.repetition_rows:
            key = (
                row["word"],
                row["hecke_prime"],
                row["cycle_id"],
                row["zeta_repetition_r"],
            )
            paired[key].append(row)
        self.assertEqual(len(paired), 138 * MODULE.FROZEN_REPETITION_CUTOFF)
        for rows in paired.values():
            self.assertEqual({int(row["orientation_sign"]) for row in rows}, {-1, 1})
            self.assertEqual(
                sum(float(row["ruelle_direct_first_variation"]) for row in rows),
                0.0,
            )
            self.assertEqual(
                sum(float(row["selberg_direct_first_variation"]) for row in rows),
                0.0,
            )

    def test_individual_first_variation_matches_central_difference(self) -> None:
        row = self.cycle_rows[17]
        length = int(row["cycle_degree"]) * MODULE.primitive_length(row["word"])
        period = float(row["period_real"])
        s_value = 0.25
        repetition = 3
        step = 1.0e-6

        def term(epsilon: float, kind: str) -> float:
            value = math.exp(
                -s_value * repetition * (length + epsilon * period)
            ) / repetition
            if kind == "selberg":
                value /= 1.0 - math.exp(-repetition * length)
            return value

        for kind in ("ruelle", "selberg"):
            finite_difference = (term(step, kind) - term(-step, kind)) / (2 * step)
            denominator = (
                1.0
                if kind == "ruelle"
                else 1.0 - math.exp(-repetition * length)
            )
            formula = (
                -s_value
                * period
                * math.exp(-s_value * repetition * length)
                / denominator
            )
            self.assertAlmostEqual(finite_difference, formula, places=11)

    def test_unweighted_hecke_period_relation_still_passes(self) -> None:
        one_per_group = self.variation_rows[:: len(MODULE.FROZEN_S_VALUES)]
        self.assertEqual(len(one_per_group), 55)
        self.assertTrue(
            all(
                float(row["unweighted_alpha_residual"])
                <= MODULE.NUMERICAL_TOLERANCE
                for row in one_per_group
            )
        )

    def test_degree_moment_criterion_is_stronger_than_total_sum(self) -> None:
        target = 7.0
        satisfying = {1: target, 2: 0.0, 5: 0.0}
        for exponent in range(1, 41):
            self.assertEqual(
                MODULE.dirichlet_degree_coefficient(satisfying, exponent),
                complex(target),
            )

        # The same unweighted total can violate the q^1 coefficient.  Thus the
        # Hecke period sum alone cannot determine the zeta kernel sum.
        same_total = {1: target - 2.0, 2: 2.0}
        self.assertEqual(sum(same_total.values()), target)
        self.assertNotEqual(
            MODULE.dirichlet_degree_coefficient(same_total, 1), complex(target)
        )

    def test_finite_one_sided_naive_recurrence_fails_153_of_165(self) -> None:
        self.assertEqual(len(self.variation_rows), 165)
        ruelle_failures = sum(
            row["ruelle_naive_recurrence_status"]
            == "FAILS_NAIVE_HECKE_RECURRENCE"
            for row in self.variation_rows
        )
        selberg_failures = sum(
            row["selberg_naive_recurrence_status"]
            == "FAILS_NAIVE_HECKE_RECURRENCE"
            for row in self.variation_rows
        )
        self.assertEqual(ruelle_failures, 153)
        self.assertEqual(selberg_failures, 153)
        self.assertEqual(
            {row["degree_profile_type"] for row in self.variation_rows},
            {"MIXED_DEGREES", "UNIFORM_NONUNIT"},
        )

    def test_degree_moments_fail_for_newform_and_same_owner_control(self) -> None:
        alpha_failures, alpha_passes = MODULE.group_moment_status_counts(
            self.moment_rows, "alpha_moment_residual"
        )
        control_failures, control_passes = MODULE.group_moment_status_counts(
            self.moment_rows, "closed_control_moment_residual"
        )
        self.assertEqual((alpha_failures, alpha_passes), (51, 4))
        self.assertEqual((control_failures, control_passes), (53, 2))
        self.assertEqual(len(self.moment_rows), 110)

    def test_two_generated_trees_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p26-round5-test-") as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            command_prefix = [sys.executable, str(MODULE_PATH), "--output"]
            subprocess.run(command_prefix + [str(first)], check=True, capture_output=True)
            subprocess.run(command_prefix + [str(second)], check=True, capture_output=True)
            first_files = sorted(path.name for path in first.iterdir())
            second_files = sorted(path.name for path in second.iterdir())
            self.assertEqual(first_files, second_files)
            for name in first_files:
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())

    def test_summary_preserves_stage_and_route_boundary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p26-round5-scope-") as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "--output", str(output)],
                check=True,
                capture_output=True,
            )
            summary = json.loads(
                (output / "round5_summary.json").read_text(encoding="utf-8")
            )
        boundary = summary["claim_boundary"]
        self.assertFalse(boundary["a2_dynamical_zeta_evaluation_run"])
        self.assertEqual(boundary["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(boundary["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(boundary["route_b_invocation_allowed"])
        self.assertFalse(boundary["prime_target_table_used"])
        self.assertFalse(boundary["riemann_zero_data_used"])
        self.assertFalse(
            summary["analytic_results"][
                "hecke_period_relation_implies_zeta_recurrence"
            ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
