#!/usr/bin/env python3
"""Regression tests for the exact HCS-C14 producer."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solenoid_zeta.py")
SPEC = importlib.util.spec_from_file_location("solenoid_zeta", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load solenoid_zeta.py")
SZ = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SZ
SPEC.loader.exec_module(SZ)


class MatrixAndIndexTests(unittest.TestCase):
    def test_frozen_matrices(self) -> None:
        self.assertEqual(SZ.mat_det(SZ.A), 8)
        self.assertEqual(SZ.mat_det(SZ.B), 8)
        self.assertNotEqual(SZ.mat_mul(SZ.A, SZ.B), SZ.mat_mul(SZ.B, SZ.A))

    def test_chronological_determinant(self) -> None:
        for word in ("a", "b", "ab", "aabbb", "ababb", "babaabaa"):
            matrix = SZ.return_matrix(word)
            self.assertEqual(SZ.mat_det(matrix), 8 ** len(word))
            self.assertGreater(SZ.fixed_determinant(matrix), 0)

    def test_index_is_odd_part(self) -> None:
        for word in ("aabbb", "ababb", "abab", "bbbbbb"):
            matrix = SZ.return_matrix(word)
            determinant = SZ.fixed_determinant(matrix)
            self.assertEqual(SZ.solenoid_fixed_count(matrix), determinant >> SZ.v2(determinant))


class ChronologyTests(unittest.TestCase):
    def test_period_five_analytic_type_witness(self) -> None:
        package = SZ.witness_package()
        rational = package["rational_word"]
        boundary = package["natural_boundary_word"]
        self.assertEqual(rational["fixed_determinant"], 30035)
        self.assertEqual(rational["solenoid_fixed_count"], 30035)
        self.assertEqual(boundary["fixed_determinant"], 30042)
        self.assertEqual(boundary["solenoid_fixed_count"], 15021)
        self.assertEqual(rational["parikh"], boundary["parikh"])
        self.assertTrue(rational["primitive"])
        self.assertTrue(boundary["primitive"])
        self.assertNotEqual(rational["canonical_dihedral"], boundary["canonical_dihedral"])

    def test_repetition_valuation_law(self) -> None:
        package = SZ.witness_package()
        for row in package["repetition_checks"]:
            self.assertEqual(row["rational_word_v2"], 0)
            self.assertEqual(row["boundary_word_v2"], row["boundary_word_expected_v2"])

    def test_mod_two_language(self) -> None:
        audit = SZ.parity_language_audit(11)
        self.assertTrue(audit["all_pass"])
        self.assertEqual([row["even_determinant_words"] for row in audit["rows"][:7]], [1, 3, 4, 7, 11, 18, 29])


class ZetaTests(unittest.TestCase):
    def test_archimedean_closed_form(self) -> None:
        rows = SZ.enumerate_periodic_counts(10)
        matrix_sum = SZ.mat_add(SZ.A, SZ.B)
        for period, row in rows.items():
            expected = 16**period + 2**period - SZ.mat_trace(SZ.mat_pow(matrix_sum, period))
            self.assertEqual(row.archimedean_count, expected)

    def test_exact_period_dold_conditions(self) -> None:
        rows = SZ.enumerate_periodic_counts(10)
        counts = {period: row.solenoid_count for period, row in rows.items()}
        exact, orbits = SZ.primitive_ledger(counts)
        self.assertEqual(orbits[1], 4)
        for period in orbits:
            self.assertGreaterEqual(exact[period], 0)
            self.assertEqual(exact[period], period * orbits[period])

    def test_integral_zeta_coefficients(self) -> None:
        rows = SZ.enumerate_periodic_counts(10)
        counts = {period: row.solenoid_count for period, row in rows.items()}
        coefficients = SZ.zeta_coefficients(counts)
        self.assertEqual([coefficients[index] for index in range(0, 6)], [1, 4, 36, 938, 12514, 227292])

    def test_uniform_sign_collapse_control(self) -> None:
        control = SZ.control_package(8)
        self.assertTrue(all(row["passed"] for row in control["aggregate_checks"]))
        first, second = control["primitive_same_parikh_witness"]
        self.assertEqual(first["fixed_count"], 769)
        self.assertEqual(second["fixed_count"], 705)


if __name__ == "__main__":
    unittest.main()
