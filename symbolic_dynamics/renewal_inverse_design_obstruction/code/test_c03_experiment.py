import unittest
from fractions import Fraction

import c03_experiment as c03


class TestC03InverseDesign(unittest.TestCase):
    def test_arbitrary_rational_germ_reconstructs_exactly(self):
        target = [Fraction(1), Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13)]
        weights = c03.inverse_design(target)
        self.assertEqual(c03.renewal_determinant_coefficients(weights), target)

    def test_seeded_on_and_off_circle_targets(self):
        for seed, on_circle in ((c03.ON_CIRCLE_SEED, True), (c03.OFF_CIRCLE_SEED, False)):
            factors, target = c03.seeded_target_factors(seed, on_circle)
            self.assertEqual(len(target) - 1, c03.TARGET_DEGREE)
            self.assertEqual(c03.renewal_determinant_coefficients(c03.inverse_design(target)), target)
            self.assertTrue(all(factor[0] == 1 for factor in factors))

    def test_mixed_coefficient_obstructs_positive_representation(self):
        result = c03.target_result("on", c03.ON_CIRCLE_SEED, True, 50)
        obstruction = result["positive_renewal_obstruction"]
        self.assertGreater(obstruction["violation_count"], 0)
        self.assertFalse(obstruction["positive_representation_possible"])

    def test_positive_crossing_and_random_phase_controls(self):
        _, target = c03.seeded_target_factors(c03.OFF_CIRCLE_SEED, False)
        crossing = c03.positive_crossing_control(target, 50)
        self.assertLess(float(crossing["determinant_residual"]), 1e-40)
        randomized = c03.random_phase_control(target, c03.MASTER_SEED)
        self.assertFalse(randomized["target_reconstructed"])
        self.assertGreater(randomized["max_target_coefficient_error"], 0)


if __name__ == "__main__":
    unittest.main()
