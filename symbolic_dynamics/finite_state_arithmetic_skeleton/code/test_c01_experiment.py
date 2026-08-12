import unittest

import c01_experiment as c01


class TestC01ExactArithmetic(unittest.TestCase):
    def test_binary_necklace_known_prefix(self):
        expected = [2, 1, 2, 3, 6, 9]
        observed = [c01.primitive_necklace_formula(2, n) for n in range(1, 7)]
        self.assertEqual(observed, expected)

    def test_necklace_and_irreducible_independent_counts(self):
        for q in (2, 3, 5):
            for n in range(1, 5):
                formula = c01.primitive_necklace_formula(q, n)
                self.assertEqual(c01.brute_aperiodic_necklace_count(q, n), formula)
                self.assertEqual(c01.brute_monic_irreducible_count(q, n), formula)

    def test_euler_product_and_repetition_ledger(self):
        degree = 9
        for q in (2, 3, 5):
            self.assertEqual(c01.euler_product_coefficients(q, degree, False), [1, -q] + [0] * (degree - 1))
            self.assertEqual(c01.euler_product_coefficients(q, degree, True), [q**n for n in range(degree + 1)])
            self.assertTrue(all(row["matches"] for row in c01.repetition_ledger(q, degree)))

    def test_lattice_unitary_is_unitary_and_linear_counted(self):
        control = c01.lattice_unitary_control()
        self.assertLess(max(control["unitarity_residuals"]), 1e-12)
        counts = [row["root_count"] for row in control["root_counts"]]
        self.assertEqual(counts, sorted(counts))
        self.assertGreater(counts[-1], counts[0])


if __name__ == "__main__":
    unittest.main()
