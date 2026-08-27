#!/usr/bin/env python3
import unittest

import round2_bianchi_ledger as ledger


class BianchiRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.elements = ledger.enumerate_word_ball()
        cls.rows, cls.controls, cls.metrics = ledger.build_payload()

    def test_generators_are_exact_level_three_sl2(self) -> None:
        for matrix in ledger.GENERATORS.values():
            self.assertEqual(ledger.mat_det(matrix), ledger.ONE)
            self.assertTrue(ledger.in_level_three(matrix))

    def test_every_enumerated_matrix_is_exact_level_three_sl2(self) -> None:
        for matrix in self.elements:
            self.assertEqual(ledger.mat_det(matrix), ledger.ONE)
            self.assertTrue(ledger.in_level_three(matrix))

    def test_inverse_closure_of_word_ball(self) -> None:
        for matrix in self.elements:
            self.assertIn(ledger.mat_inv(matrix), self.elements)

    def test_complex_length_reconstructs_trace(self) -> None:
        residuals = [
            float(row["trace_reconstruction_residual"])
            for row in self.rows
            if row["matrix_class"] == "LOXODROMIC"
        ]
        self.assertTrue(residuals)
        self.assertLess(max(residuals), 1e-8)

    def test_control_is_target_free_and_keeps_lengths(self) -> None:
        ledger_by_id = {row["row_id"]: row for row in self.rows}
        self.assertTrue(self.controls)
        for control in self.controls:
            source = ledger_by_id[control["row_id"]]
            self.assertEqual(control["target_data_used"], "false")
            self.assertEqual(control["complex_length_fixed"], source["complex_length_re"])
            self.assertEqual(
                control["repetition_exponent_fixed"], source["exact_power_exponent"]
            )

    def test_core_render_is_byte_deterministic(self) -> None:
        first, _ = ledger.core_outputs()
        second, _ = ledger.core_outputs()
        self.assertEqual(first, second)
        self.assertEqual(ledger.combined_hash(first), ledger.combined_hash(second))


if __name__ == "__main__":
    unittest.main()
