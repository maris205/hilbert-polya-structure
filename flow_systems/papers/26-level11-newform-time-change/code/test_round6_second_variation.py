#!/usr/bin/env python3
"""Independent standard-library tests for P26 Round 6."""

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


MODULE_PATH = Path(__file__).with_name("round6_second_variation.py")
SPEC = importlib.util.spec_from_file_location("p26_round6", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round6_second_variation.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SecondVariationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cycle_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER)
        cls.period_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_PERIOD_SUMMARY)
        cls.grouped = MODULE.grouped_cycle_rows(cls.cycle_rows)
        cls.periods = MODULE.period_summary_map(cls.period_rows)
        cls.pair_rows = MODULE.build_pair_ledger(cls.cycle_rows)
        cls.moment_rows = MODULE.build_quadratic_moment_ledger(
            cls.grouped, cls.periods
        )
        cls.variation_rows = MODULE.build_variation_ledger(
            cls.grouped, cls.periods, cls.moment_rows
        )

    def test_round4_inputs_are_hash_locked_and_valid(self) -> None:
        self.assertEqual(len(self.cycle_rows), 138)
        self.assertEqual(len(self.period_rows), 55)
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER),
            MODULE.EXPECTED_CYCLE_SHA256,
        )
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_PERIOD_SUMMARY),
            MODULE.EXPECTED_PERIOD_SHA256,
        )
        self.assertEqual(
            MODULE.validate_inputs(
                MODULE.DEFAULT_ROUND4_CYCLE_LEDGER,
                MODULE.DEFAULT_ROUND4_PERIOD_SUMMARY,
                self.cycle_rows,
                self.period_rows,
            ),
            [],
        )

    def test_pair_ledger_has_expected_scope_and_formula_residuals(self) -> None:
        self.assertEqual(len(self.pair_rows), 552)
        self.assertTrue(
            all(float(row["canonical_pair_first_variation"]) == 0.0 for row in self.pair_rows)
        )
        self.assertLessEqual(
            max(float(row["ruelle_pair_formula_residual"]) for row in self.pair_rows),
            1.0e-15,
        )
        self.assertLessEqual(
            max(float(row["selberg_pair_formula_residual"]) for row in self.pair_rows),
            1.0e-15,
        )

    def test_inverse_pair_second_variation_adds_instead_of_cancelling(self) -> None:
        positive_period_rows = [
            row
            for row in self.pair_rows
            if float(row["primitive_alpha_period_squared"]) > 1.0e-20
        ]
        self.assertTrue(positive_period_rows)
        self.assertTrue(
            all(
                float(row["ruelle_pair_second_variation_formula"]) > 0.0
                for row in positive_period_rows
            )
        )
        self.assertEqual(
            {row["orientation_pair_second_variation_status"] for row in self.pair_rows},
            {"PROVED_ADDS_AND_IS_ORIENTATION_EVEN"},
        )

    def test_individual_pair_second_variation_matches_central_difference(self) -> None:
        row = self.cycle_rows[17]
        degree = int(row["cycle_degree"])
        length = degree * MODULE.ROUND5.primitive_length(row["word"])
        period = float(row["period_real"])
        s_value = 0.25
        repetition = 3
        step = 2.0e-4

        def pair_term(epsilon: float, kind: str) -> float:
            value = (
                math.exp(-s_value * repetition * (length + epsilon * period))
                + math.exp(-s_value * repetition * (length - epsilon * period))
            ) / repetition
            if kind == "selberg":
                value /= 1.0 - math.exp(-repetition * length)
            return value

        for kind in ("ruelle", "selberg"):
            finite_difference = (
                pair_term(step, kind)
                - 2.0 * pair_term(0.0, kind)
                + pair_term(-step, kind)
            ) / (step * step)
            denominator = (
                1.0
                if kind == "ruelle"
                else 1.0 - math.exp(-repetition * length)
            )
            formula = (
                2.0
                * s_value
                * s_value
                * repetition
                * period
                * period
                * math.exp(-s_value * repetition * length)
                / denominator
            )
            self.assertAlmostEqual(finite_difference, formula, delta=2.0e-8)

    def test_second_derivative_leaves_r_after_log_weight(self) -> None:
        for row in self.pair_rows:
            repetition = int(row["zeta_repetition_r"])
            self.assertEqual(
                int(row["second_derivative_repetition_factor_r"]), repetition
            )
            self.assertAlmostEqual(
                float(row["repeated_alpha_period_squared"]),
                repetition
                * repetition
                * float(row["primitive_alpha_period_squared"]),
            )

    def test_hecke_degree_remains_distinct_from_zeta_repetition(self) -> None:
        degrees = {int(row["hecke_cycle_degree_d"]) for row in self.pair_rows}
        repetitions = {int(row["zeta_repetition_r"]) for row in self.pair_rows}
        self.assertIn(13, degrees)
        self.assertEqual(repetitions, {1, 2, 3, 4})
        self.assertTrue(
            all(
                row["hecke_degree_is_zeta_repetition"] == "false"
                for row in self.variation_rows
            )
        )

    def test_quadratic_mobius_criterion_positive_and_counterexample(self) -> None:
        target = 7.0
        satisfying = {1: target, 2: 0.0, 5: 0.0}
        for exponent in range(1, 41):
            self.assertAlmostEqual(
                MODULE.quadratic_dirichlet_coefficient(satisfying, exponent), target
            )
        same_unweighted_total = {1: target - 2.0, 2: 2.0}
        self.assertEqual(sum(same_unweighted_total.values()), target)
        self.assertNotEqual(
            MODULE.quadratic_dirichlet_coefficient(same_unweighted_total, 1),
            target,
        )

    def test_quadratic_degree_moment_counts_and_survivors(self) -> None:
        self.assertEqual(len(self.moment_rows), 110)
        a_p = MODULE.group_moment_statuses(self.moment_rows, "a_p")
        a_p_squared = MODULE.group_moment_statuses(self.moment_rows, "a_p_squared")
        self.assertEqual(sum(value.startswith("FAILS_") for value in a_p.values()), 51)
        self.assertEqual(
            sum(value.startswith("FAILS_") for value in a_p_squared.values()), 51
        )
        survivors = {
            key
            for key, value in a_p_squared.items()
            if value == "PASS_NUMERICAL_OBSERVATION"
        }
        self.assertEqual(
            survivors,
            {
                ("LRRLRRR", 5),
                ("LLRLLRLR", 5),
                ("LLLRLLRLR", 5),
                ("LLLRLRLLR", 5),
            },
        )

    def test_a_p_and_a_p_squared_finite_rows_fail_153_of_165(self) -> None:
        self.assertEqual(len(self.variation_rows), 165)
        for field in (
            "ruelle_lambda_a_p_status",
            "selberg_lambda_a_p_status",
            "ruelle_lambda_a_p_squared_status",
            "selberg_lambda_a_p_squared_status",
        ):
            self.assertEqual(
                sum(str(row[field]).startswith("FAILS_") for row in self.variation_rows),
                153,
            )

    def test_secondary_negative_control_fails_all_rows(self) -> None:
        for field in (
            "ruelle_secondary_a_p_squared_minus_p_status",
            "selberg_secondary_a_p_squared_minus_p_status",
        ):
            self.assertEqual(
                sum(str(row[field]).startswith("FAILS_") for row in self.variation_rows),
                165,
            )
        self.assertEqual(
            {row["secondary_control_role"] for row in self.moment_rows},
            {
                "A_P_SQUARED_MINUS_P_IS_AN_EXPLICIT_SECONDARY_NEGATIVE_"
                "CONTROL_NOT_THE_THEORETICAL_TARGET"
            },
        )

    def test_two_generated_trees_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p26-round6-test-") as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            prefix = [sys.executable, str(MODULE_PATH), "--output"]
            subprocess.run(prefix + [str(first)], check=True, capture_output=True)
            subprocess.run(prefix + [str(second)], check=True, capture_output=True)
            names = sorted(path.name for path in first.iterdir())
            self.assertEqual(names, sorted(path.name for path in second.iterdir()))
            for name in names:
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())

    def test_summary_preserves_local_non_a2_boundary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p26-round6-scope-") as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "--output", str(output)],
                check=True,
                capture_output=True,
            )
            summary = json.loads(
                (output / "round6_summary.json").read_text(encoding="utf-8")
            )
        boundary = summary["claim_boundary"]
        self.assertTrue(boundary["finite_local_log_product_audit_only"])
        self.assertFalse(boundary["a2_dynamical_zeta_evaluation_run"])
        self.assertFalse(boundary["root_count_or_zero_matching_run"])
        self.assertEqual(boundary["formal_route_a_tuple"], MODULE.FORMAL_TUPLE)
        self.assertEqual(boundary["formal_a1_verdict"], "A1_WEAK")
        self.assertEqual(boundary["formal_a2_a4_verdicts"], "FAIL_NOT_TESTABLE")
        self.assertEqual(boundary["overall_route_a_status"], "ROUTE_A_EXPLORATORY")
        self.assertEqual(boundary["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(boundary["route_b_invocation_allowed"])
        self.assertFalse(boundary["prime_target_table_used"])
        self.assertFalse(boundary["riemann_zero_data_used"])
        self.assertEqual(
            summary["analytic_results"]["a_p_squared_minus_p_role"],
            "SECONDARY_NEGATIVE_CONTROL_ONLY",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
