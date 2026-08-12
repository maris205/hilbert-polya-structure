import unittest

import c02_experiment as c02


class TestC02PeriodicCensus(unittest.TestCase):
    def test_prime_square_witness_for_every_nonzero_small_word(self):
        for period in range(1, 9):
            row = c02.brute_candidate_fixed_points(period)
            self.assertEqual(row["fixed_points"], 1)
            self.assertTrue(row["all_witnesses_valid"])

    def test_finite_modulus_inclusion_exclusion_matches_brute(self):
        primes = c02.first_primes(3)
        for prime_count in (1, 2, 3):
            for period in range(1, 11):
                selected = primes[:prime_count]
                self.assertEqual(
                    c02.finite_modulus_fixed_points(period, selected),
                    c02.brute_finite_modulus_fixed_points(period, selected),
                )

    def test_parent_control_counts(self):
        self.assertEqual([c02.golden_mean_fixed_points(n) for n in range(1, 7)], [1, 3, 4, 7, 11, 18])
        self.assertEqual([2**n for n in range(1, 5)], [2, 4, 8, 16])

    def test_candidate_primitive_orbits(self):
        fixed = {n: 1 for n in range(1, 13)}
        primitive = c02.primitive_orbits_from_fixed_counts(fixed)
        self.assertEqual(primitive[1], 1)
        self.assertTrue(all(primitive[n] == 0 for n in range(2, 13)))


if __name__ == "__main__":
    unittest.main()
