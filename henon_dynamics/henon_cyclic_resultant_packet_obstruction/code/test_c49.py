#!/usr/bin/env python3
"""Adversarial exact tests for HCS-P49."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import sympy as sp


MODULE_PATH = Path(__file__).with_name("c49_cyclic_packets.py")
SPEC = importlib.util.spec_from_file_location("c49_cyclic_packets", MODULE_PATH)
assert SPEC and SPEC.loader
C49 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C49)


class CyclicPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = C49.build_certificate(12)

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.certificate["dependency_locks"]), 8)

    def test_exact_counts(self) -> None:
        summary = self.certificate["finite_summary"]
        self.assertEqual(summary["orbit_count"], 3)
        self.assertEqual(summary["primitive_row_count"], 36)
        self.assertEqual(summary["square_theorem_row_count"], 30)
        self.assertEqual(summary["square_theorem_rows_verified"], 30)
        self.assertEqual(summary["level_two_nonsquare_controls"], 3)

    def test_polynomials_are_actual_minimal_polynomials(self) -> None:
        for orbit in self.certificate["orbits"].values():
            self.assertTrue(orbit["monic"])
            self.assertTrue(orbit["irreducible"])
            self.assertTrue(orbit["reciprocal"])
            self.assertEqual(orbit["constant_term"], 1)

    def test_divisor_factorization_and_square_norms(self) -> None:
        for orbit in self.certificate["orbits"].values():
            for row in orbit["rows"]:
                self.assertTrue(row["divisor_product_exact"])
                self.assertEqual(
                    row["cyclic_determinant_norm_abs"],
                    row["cyclic_resultant_abs"] ** 2,
                )
                if row["index"] > 2:
                    self.assertTrue(row["primitive_is_square"])
                    self.assertEqual(
                        row["canonical_half_norm"] ** 2,
                        row["primitive_cyclotomic_norm_abs"],
                    )

    def test_level_two_exception_is_real(self) -> None:
        for orbit in self.certificate["orbits"].values():
            row = orbit["rows"][1]
            self.assertEqual(row["index"], 2)
            self.assertFalse(row["primitive_is_square"])

    def test_signed_period_three_is_not_positive_modulus_mutation(self) -> None:
        control = self.certificate["signed_period_3_control"]
        self.assertTrue(control["mutation_detected"])
        self.assertTrue(control["signed_polynomial_equals_positive_polynomial_at_minus_X"])
        self.assertEqual(control["actual_signed_cyclotomic_norm_index_3"], 7451**2)
        self.assertEqual(control["positive_modulus_mutation_index_3"], 7299**2)

    def test_nonreciprocal_counterexample(self) -> None:
        control = self.certificate["symbolic_controls"]["nonreciprocal_unit_hypothesis_control"]
        self.assertEqual(control["primitive_norm_index_3"], 13)
        self.assertFalse(control["is_square"])

    def test_one_scalar_power_law_fails(self) -> None:
        for orbit in self.certificate["orbits"].values():
            control = orbit["one_scalar_power_law_control"]
            self.assertNotEqual(control["A_2"], control["A_1"] ** 2)
            self.assertFalse(control["A_2_equals_A_1_squared"])

    def test_selected_prime_and_composite_half_norms(self) -> None:
        selected = self.certificate["selected_half_norms"]
        self.assertTrue(sp.isprime(selected["period_1_index_3_prime_half"]))
        self.assertFalse(sp.isprime(selected["period_1_index_4_composite_half"]))
        self.assertTrue(sp.isprime(selected["period_3_index_3_prime_half"]))
        self.assertTrue(sp.isprime(selected["period_4_index_6_prime_half"]))

    def test_claim_boundary(self) -> None:
        ledger = self.certificate["theorem_ledger"]
        self.assertFalse(ledger["primitive_norm_is_prime_for_index_gt_2"])
        self.assertFalse(ledger["minimal_trace_field_determinant_norm_is_forced_square"])
        self.assertTrue(ledger["lehmer_pierce_sequence_survives"])
        self.assertFalse(ledger["half_norm_is_single_euler_label"])
        self.assertEqual(ledger["prime_ideal_packet_attachment"], "OPEN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
