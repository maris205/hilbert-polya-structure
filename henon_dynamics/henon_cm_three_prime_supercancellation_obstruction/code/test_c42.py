import unittest
from fractions import Fraction

from code.c42_rigidity_checker import certificate, determinant3, first_log_coefficient, solve3, trace_fp


class RigidityTests(unittest.TestCase):
    def test_sentinel_traces(self) -> None:
        self.assertEqual((trace_fp(5), trace_fp(7), trace_fp(11)), (0, -4, 0))

    def test_linear_system(self) -> None:
        matrix = [[1, 0, 5], [1, -4, 7], [1, 0, 11]]
        self.assertEqual(determinant3(matrix), -24)
        self.assertEqual(solve3(matrix, [1, 1, 1]), (Fraction(1), Fraction(0), Fraction(0)))

    def test_nontrivial_cm_factor_fails(self) -> None:
        self.assertNotEqual(first_log_coefficient(1, 1, 0, 7), 1)
        self.assertEqual(first_log_coefficient(1, 0, 0, 7), 1)

    def test_certificate(self) -> None:
        result = certificate(5)
        self.assertEqual(result["integer_matches"], [[1, 0, 0]])


if __name__ == "__main__":
    unittest.main()
