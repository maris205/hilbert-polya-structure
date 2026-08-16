#!/usr/bin/env python3
import cmath
import sys
import unittest
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c77_ownership_firewall as c77  # noqa: E402


class OwnershipFirewallTests(unittest.TestCase):
    def test_channel_coefficient_identity(self):
        for m in range(1, 129):
            self.assertEqual(c77.c_divisor(m), c77.c_euler(m))
            self.assertNotEqual(c77.c_euler(m), 0)
            self.assertLessEqual(abs(c77.c_euler(m)), 1)

    def test_channel_trace_norm_samples(self):
        for q, z in ((0.5, 0.6), (1.0, 0.75), (2.0, 0.4)):
            entries = c77.channel_entries(complex(z), q, 192)
            self.assertTrue(all(value == value for value in entries))
            self.assertLess(abs(entries[-1]), 1e-15)
            self.assertLess(sum(abs(value) for value in entries), 100)

    def test_trace_exponential_determinant(self):
        for q, z in ((0.5, 0.5), (1.0, 0.8), (2.0, 0.46)):
            entries = c77.channel_entries(complex(z), q)
            left = cmath.exp(sum(entries, 0j))
            right = 1 + 0j
            for value in entries:
                right *= cmath.exp(value)
            self.assertLess(abs(left - right), 2e-11)

    def test_universal_rank_one(self):
        for value in (cmath.exp(0.2j), 2 + 3j, cmath.exp(-0.4 + 0.1j)):
            self.assertEqual(c77.universal_rank_one_determinant(value), value)

    def test_singleton_words(self):
        for n in range(3, 50, 2):
            word = c77.singleton_word(n)
            self.assertTrue(c77.is_reflection_fixed(word))
            self.assertEqual(c77.least_period(word), n)
            self.assertEqual(c77.symmetry_energy(word), n - 2)

    def test_exact_block_determinants(self):
        for q in (Fraction(1, 2), Fraction(1), Fraction(2)):
            for n in range(3, 16, 2):
                word = c77.singleton_word(n)
                weights = c77.block_weights(word, q)
                block = c77.weighted_cyclic_matrix(weights)
                z = Fraction(1, 5)
                observed = c77.determinant_fraction(c77.identity_minus_scaled(block, z))
                expected = 1 - z ** n * q ** (n - 2)
                self.assertEqual(observed, expected)

    def test_full_turn_power(self):
        for q in (Fraction(2, 3), Fraction(3, 2)):
            for n in (3, 5, 7, 9):
                weights = c77.block_weights(c77.singleton_word(n), q)
                block = c77.weighted_cyclic_matrix(weights)
                self.assertEqual(
                    c77.matrix_power(block, n),
                    c77.scalar_identity(n, q ** (n - 2)),
                )

    def test_singular_value_ledger(self):
        for q in (Fraction(1, 3), Fraction(1), Fraction(3)):
            for n in range(3, 20, 2):
                weights = c77.block_weights(c77.singleton_word(n), q)
                self.assertEqual(weights.count(Fraction(1)), 2 if q != 1 else n)
                self.assertTrue(all(min(Fraction(1), q) <= value <= max(Fraction(1), q) for value in weights))

    def test_graded_power_ledger(self):
        weights = c77.block_weights(c77.singleton_word(7), Fraction(2, 3))
        self.assertEqual(c77.graded_block_diagonal_sum(weights, 3), 0)
        self.assertEqual(c77.graded_block_diagonal_sum(weights, 7), Fraction(7) * Fraction(2, 3) ** 5)
        self.assertEqual(c77.graded_block_diagonal_sum(weights, 14), Fraction(7) * Fraction(2, 3) ** 10)

    def test_dependency_locks(self):
        self.assertEqual(len(c77.dependency_locks()), 6)

    def test_status_firewall(self):
        status = c77.core_payload()["claim_status"]
        self.assertEqual(status["punctured_analytic_determinant"], "PROVED_TAUTOLOGICAL")
        self.assertEqual(status["source_native_direct_sum_trace_class"], "REFUTED")
        self.assertEqual(status["genuine_transfer_owner"], "OPEN")
        self.assertEqual(status["arithmetic_advance"], "NO")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c77.mutation_audit(c77.core_payload())
        self.assertEqual(audit["attempted"], 38)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
