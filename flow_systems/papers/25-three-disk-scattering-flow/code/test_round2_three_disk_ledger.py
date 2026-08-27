#!/usr/bin/env python3
import math
import unittest

import round2_three_disk_ledger as ledger


class ThreeDiskRound2Tests(unittest.TestCase):
    def test_symbolic_enumeration_is_exact_and_primitive(self) -> None:
        words = ledger.primitive_oriented_cyclic_words()
        self.assertEqual(len(words), 747)
        self.assertEqual(len(set(words)), len(words))
        for word in words:
            self.assertEqual(word, ledger.canonical_rotation(word))
            self.assertTrue(ledger.is_symbolically_primitive(word))
            self.assertTrue(
                all(word[index] != word[(index + 1) % len(word)] for index in range(len(word)))
            )

    def test_two_disk_bounce_is_actual_not_center_proxy(self) -> None:
        solution = ledger.solve_orbit((0, 1), 6.0)
        self.assertTrue(solution["reliable"])
        self.assertAlmostEqual(solution["length"], 8.0, places=9)
        self.assertAlmostEqual(solution["center_proxy_length"], 12.0, places=9)
        self.assertLess(solution["reflection_residual"], 1e-10)

    def test_two_disk_stability_trace_matches_closed_form(self) -> None:
        solution = ledger.solve_orbit((0, 1), 6.0)
        stability = ledger.stability_from_orbit(solution)
        self.assertAlmostEqual(stability["trace"], 98.0, places=8)
        self.assertLess(stability["determinant_high_precision_residual"], 1e-60)
        self.assertLess(stability["double_trace_relative_residual"], 1e-14)
        self.assertGreater(stability["unstable_multiplier"], 1.0)
        self.assertGreater(stability["half_density"], 0.0)
        self.assertLess(stability["half_density"], 1.0)

    def test_long_unstable_product_uses_high_precision_determinant(self) -> None:
        word = tuple(int(symbol) for symbol in "012020121021")
        solution = ledger.solve_orbit(word, 6.2)
        self.assertTrue(solution["reliable"])
        stability = ledger.stability_from_orbit(solution)
        self.assertGreater(stability["trace"], 1e12)
        self.assertLess(stability["determinant_high_precision_residual"], 1e-50)
        self.assertLess(stability["double_trace_relative_residual"], 1e-14)

    def test_hash_controls_use_no_external_target_data(self) -> None:
        first = ledger.hash_uniform("fixed-label")
        second = ledger.hash_uniform("fixed-label")
        self.assertEqual(first, second)
        self.assertGreaterEqual(first, 0.0)
        self.assertLess(first, 1.0)

    def test_no_eclipse_grid_is_strict(self) -> None:
        for distance in ledger.DISTANCE_RATIOS:
            self.assertGreater(math.sqrt(3.0) * distance / 2.0, 2.0)


if __name__ == "__main__":
    unittest.main()
