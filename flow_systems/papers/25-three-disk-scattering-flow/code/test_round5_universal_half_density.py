#!/usr/bin/env python3
"""Independent standard-library tests for P25 Round 5."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

import mpmath as mp


MODULE_PATH = Path(__file__).with_name("round5_universal_half_density.py")
SPEC = importlib.util.spec_from_file_location("p25_round5_half_density", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Round-5 module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class UniversalHalfDensityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.project_root = MODULE_PATH.resolve().parents[1]
        cls.rows, cls.metrics = MODULE.build_ledger(cls.project_root)
        cls.summary = MODULE.build_summary(cls.rows)

    def test_01_frozen_inputs_and_owner_count(self) -> None:
        self.assertEqual(self.metrics["round2_input_sha256"], MODULE.ROUND2_SHA256)
        self.assertEqual(self.metrics["round3_input_sha256"], MODULE.ROUND3_SHA256)
        self.assertEqual(self.metrics["source_primitive_owner_rows"], 2241)

    def test_02_primitive_and_repetition_owners_are_separate(self) -> None:
        self.assertEqual(len(self.rows), 6723)
        self.assertEqual(self.metrics["primitive_branch_rows"], 2241)
        self.assertEqual(self.metrics["repetition_branch_rows"], 4482)
        owner_grids: dict[str, set[int]] = {}
        for row in self.rows:
            owner_grids.setdefault(row["primitive_owner_id"], set()).add(
                int(row["repetition_index"])
            )
        self.assertEqual(len(owner_grids), 2241)
        self.assertTrue(all(grid == {1, 2, 3} for grid in owner_grids.values()))

    def test_03_exact_symplectic_formula_for_both_signs(self) -> None:
        lam = mp.mpf("7.25")
        for sign in (-1, 1):
            for repetition in MODULE.REPETITIONS:
                formula = MODULE.exact_stability_amplitude(lam, sign, repetition)
                determinant = MODULE.determinant_amplitude_from_eigenvalues(
                    lam, sign, repetition
                )
                self.assertLess(MODULE.relative_residual(formula, determinant), mp.mpf("1e-95"))

    def test_04_half_density_is_the_universal_leading_factor(self) -> None:
        for row in self.rows:
            lam_power = mp.mpf(row["unstable_multiplier_power"])
            expected = 1 / mp.sqrt(lam_power)
            observed = mp.mpf(row["universal_half_density"])
            self.assertLess(MODULE.relative_residual(observed, expected), mp.mpf("1e-48"))
            self.assertLess(
                MODULE.relative_residual(
                    mp.mpf(row["relative_leading_factor_error"]), 1 / lam_power
                ),
                mp.mpf("1e-48"),
            )

    def test_05_physical_sign_and_repetition_parity_are_retained(self) -> None:
        self.assertGreater(self.metrics["negative_primitive_eigenvalue_sign_owners"], 0)
        for row in self.rows:
            primitive_sign = int(row["physical_primitive_eigenvalue_sign"])
            repetition = int(row["repetition_index"])
            self.assertEqual(
                int(row["physical_repetition_eigenvalue_sign"]),
                primitive_sign**repetition,
            )

    def test_06_correction_decreases_with_repetition(self) -> None:
        by_owner: dict[str, list[mp.mpf]] = {}
        for row in self.rows:
            by_owner.setdefault(row["primitive_owner_id"], []).append(
                mp.mpf(row["relative_leading_factor_error"])
            )
        self.assertTrue(all(values[0] > values[1] > values[2] for values in by_owner.values()))

    def test_07_source_half_density_replays(self) -> None:
        residual = mp.mpf(self.metrics["max_source_half_density_relative_residual"])
        self.assertLess(residual, mp.mpf("1e-12"))

    def test_08_all_formula_residuals_are_numerically_closed(self) -> None:
        self.assertLess(
            mp.mpf(self.metrics["max_positive_formula_relative_residual"]),
            mp.mpf("1e-90"),
        )
        self.assertLess(
            mp.mpf(self.metrics["max_physical_formula_relative_residual"]),
            mp.mpf("1e-90"),
        )

    def test_09_outputs_are_byte_deterministic(self) -> None:
        first = MODULE.build_outputs(self.project_root)
        second = MODULE.build_outputs(self.project_root)
        self.assertEqual(first, second)
        self.assertEqual(MODULE.combined_hash(first), MODULE.combined_hash(second))

    def test_10_route_and_target_firewalls_hold(self) -> None:
        self.assertEqual(self.metrics["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["a2_evaluation"], "NOT_RUN")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["prime_or_zero_tables_used"])
        self.assertEqual(
            self.metrics["paper_disposition"],
            "RETAIN_AS_METHODS_NEGATIVE_CONTROL_PAPER",
        )
        self.assertTrue(all(row["prime_or_zero_tables_used"] == "false" for row in self.rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
