#!/usr/bin/env python3
"""Unit and exact-identity tests for the HCS-C03 census."""

from __future__ import annotations

import sys
import unittest
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import c03_finite_field as ff  # noqa: E402


class FiniteFieldHenonTests(unittest.TestCase):
    def test_prime_sieve(self) -> None:
        self.assertEqual(ff.primes_up_to(13), [2, 3, 5, 7, 11, 13])

    def test_henon_is_bijective_with_exact_inverse(self) -> None:
        for prime in [2, 3, 5, 7, 11, 13]:
            permutation = ff.build_henon_permutation(prime)
            checks = ff.validate_henon_permutation(permutation, prime)
            self.assertTrue(all(checks.values()))
            self.assertEqual(len(set(permutation)), prime * prime)

    def test_reversor_formula(self) -> None:
        for prime in [2, 3, 5, 7, 11]:
            for state in range(prime * prime):
                lhs = ff.swap_index(
                    ff.henon_image_index(ff.swap_index(state, prime), prime), prime
                )
                self.assertEqual(lhs, ff.henon_inverse_index(state, prime))

    def test_known_permutation_decomposition(self) -> None:
        permutation = [1, 0, 3, 4, 2, 5]
        result = ff.decompose_permutation(permutation, short_threshold=2)
        self.assertEqual(result["cycle_counts"], Counter({2: 1, 3: 1, 1: 1}))
        self.assertEqual(result["metrics"]["num_cycles"], 3)
        self.assertEqual(result["metrics"]["short_point_mass"], 3)

    def test_fix_and_mobius_identities(self) -> None:
        cycle_counts = Counter({1: 2, 2: 3, 5: 1})
        fixed = ff.fixed_counts_from_cycles(cycle_counts, 10)
        self.assertEqual(fixed[0], 2)
        self.assertEqual(fixed[1], 8)
        self.assertEqual(fixed[4], 7)
        for n in range(1, 11):
            primitive = sum(
                ff.mobius(d) * fixed[n // d - 1] for d in ff.divisors(n)
            )
            self.assertEqual(primitive, n * cycle_counts.get(n, 0))

    def test_fixed_prediction(self) -> None:
        for prime in ff.primes_up_to(47):
            permutation = ff.build_henon_permutation(prime)
            cycles = ff.decompose_permutation(permutation, prime)["cycle_counts"]
            self.assertEqual(
                cycles.get(1, 0), ff.fixed_point_prediction(prime)["predicted_count"]
            )

    def test_reversibility_factorization(self) -> None:
        for prime in [2, 3, 5, 7, 11, 13]:
            permutation = ff.build_henon_permutation(prime)
            reversor = [ff.swap_index(i, prime) for i in range(prime * prime)]
            result = ff.decompose_permutation(permutation, prime, reversor)
            raw = result["cycle_counts"]
            symmetric = result["symmetric_cycle_counts"]
            paired = result["paired_pair_cycle_counts"]
            for length in set(raw) | set(symmetric) | set(paired):
                self.assertEqual(
                    raw[length], symmetric[length] + 2 * paired[length]
                )
            metrics = result["metrics"]
            self.assertEqual(
                metrics["symmetric_degree"] + 2 * metrics["paired_base_degree"],
                prime * prime,
            )
            second_involution = [
                permutation[reversor[i]] for i in range(prime * prime)
            ]
            self.assertEqual(
                2 * metrics["symmetric_cycle_count"],
                sum(reversor[i] == i for i in range(prime * prime))
                + sum(second_involution[i] == i for i in range(prime * prime)),
            )

    def test_cyclotomic_degree(self) -> None:
        for prime in [5, 7, 11]:
            cycles = ff.decompose_permutation(
                ff.build_henon_permutation(prime), prime
            )["cycle_counts"]
            cyclotomic = ff.cyclotomic_multiplicities(cycles)
            self.assertEqual(
                sum(ff.totient(d) * count for d, count in cyclotomic.items()),
                prime * prime,
            )

    def test_rng_and_involution_are_reproducible(self) -> None:
        self.assertEqual(ff.random_permutation(50, 1234), ff.random_permutation(50, 1234))
        involution = ff.random_involution(25, 5, 4321)
        self.assertEqual(sum(involution[i] == i for i in range(25)), 5)
        self.assertTrue(all(involution[involution[i]] == i for i in range(25)))

    def test_end_to_end_small_prime(self) -> None:
        record, controls = ff.run_prime(
            prime=5,
            random_replicates=2,
            master_seed=ff.DEFAULT_MASTER_SEED,
            fix_n_max=16,
            direct_fix_n_max=8,
        )
        self.assertEqual(record["n_points"], 25)
        self.assertTrue(all(record["self_checks"].values()))
        self.assertEqual(len(controls), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)

