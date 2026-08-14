#!/usr/bin/env python3
"""Unit and adversarial tests for HCS-P50."""

from __future__ import annotations

import copy
import unittest

import sympy as sp

import c50_tagged_packets as c50


class TaggedPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = c50.build_certificate()

    def test_dependency_locks(self) -> None:
        self.assertEqual(set(self.certificate["dependency_locks"]), set(c50.DEPENDENCIES))

    def test_trace_polynomials(self) -> None:
        self.assertEqual(c50.beta_trace_polynomial(3), c50.T + 1)
        self.assertEqual(c50.beta_trace_polynomial(4), c50.T)
        self.assertEqual(c50.beta_trace_polynomial(5), c50.T**2 + c50.T - 1)
        self.assertEqual(c50.beta_trace_polynomial(6), c50.T - 1)

    def test_all_norm_pushforwards(self) -> None:
        self.assertEqual(self.certificate["finite_summary"]["p49_half_norm_crosschecks"], 30)
        for row in self.certificate["rows"]:
            self.assertTrue(row["norm_pushforward_exact"])
            reconstructed: dict[str, int] = {}
            for atom in row["prime_ideal_atoms"]:
                key = str(atom["rational_prime"])
                reconstructed[key] = reconstructed.get(key, 0) + atom["norm_exponent"]
            self.assertEqual(reconstructed, row["rational_factorization"])

    def test_every_good_residue_order(self) -> None:
        for row in self.certificate["rows"]:
            for prime, control in row["multiplier_order_controls"].items():
                if row["cyclotomic_index"] % int(prime):
                    self.assertTrue(control["exact_order_verified"])
                    self.assertEqual(control["exact_order"], row["cyclotomic_index"])
                else:
                    self.assertFalse(control["exact_order_verified"])
                    self.assertIsNone(control["exact_order"])

    def test_multi_order_collision_checksum(self) -> None:
        self.assertEqual(
            self.certificate["multi_order_collision_primes"],
            {
                "11": [5, 12],
                "19": [3, 10, 20],
                "29": [7, 14, 15],
                "79": [8, 16],
                "131": [5, 12],
                "307": [11, 17],
                "38039": [13, 19],
            },
        )

    def test_p29_three_clock_obstruction(self) -> None:
        atoms = self.certificate["collision_ledger"]["29"]
        self.assertEqual(
            sorted(atom["residue_order"] for atom in atoms if atom["residue_order_certified"]),
            [7, 14, 15],
        )
        self.assertEqual({atom["orbit"] for atom in atoms}, {"period_1", "period_3"})

    def test_three_tags_are_independently_necessary(self) -> None:
        atoms = self.certificate["collision_ledger"]["109"]
        self.assertEqual({atom["orbit"] for atom in atoms}, {"period_1", "period_3"})
        period_one = [atom for atom in atoms if atom["orbit"] == "period_1"]
        self.assertEqual(len(period_one), 2)
        self.assertEqual(len({atom["prime_ideal"] for atom in period_one}), 2)
        self.assertEqual({atom["cyclotomic_index"] for atom in atoms}, {11})

        p19 = self.certificate["collision_ledger"]["19"]
        self.assertTrue({3, 10, 19, 20}.issubset({atom["cyclotomic_index"] for atom in p19}))

    def test_rational_pushforward_kernel_rank(self) -> None:
        summary = self.certificate["finite_summary"]
        self.assertEqual(
            summary["rational_pushforward_kernel_rank"],
            summary["tagged_prime_ideal_atom_count"] - summary["distinct_rational_prime_count"],
        )
        self.assertGreater(summary["rational_pushforward_kernel_rank"], 0)

    def test_signed_period_three_mutation_changes_packet(self) -> None:
        correct = c50.trace_element("period_3", 3)["absolute_norm"]
        polynomial = c50.beta_trace_polynomial(3)
        wrong_value = sp.expand(polynomial.subs(c50.T, 38 + 42 * sp.sqrt(5)))
        wrong_a = wrong_value.coeff(sp.sqrt(5), 0)
        wrong_b = wrong_value.coeff(sp.sqrt(5))
        wrong_u, wrong_v = int(wrong_a - wrong_b), int(2 * wrong_b)
        wrong_norm = abs(wrong_u * wrong_u + wrong_u * wrong_v - wrong_v * wrong_v)
        self.assertEqual(correct, 7451)
        self.assertNotEqual(correct, wrong_norm)

    def test_prime_only_key_is_lossy_mutation(self) -> None:
        atoms = [
            atom
            for collision_atoms in self.certificate["collision_ledger"].values()
            for atom in collision_atoms
        ]
        prime_only = {atom["rational_prime"] for atom in atoms}
        tagged = {
            (atom["orbit"], atom["cyclotomic_index"], atom["prime_ideal"])
            for atom in atoms
        }
        self.assertLess(len(prime_only), len(tagged))

    def test_claim_boundary_rejects_promotions(self) -> None:
        promoted = copy.deepcopy(self.certificate["theorem_ledger"])
        for forbidden in [
            "pressure_weighted_all_orbit_limit",
            "von_mangoldt_trace",
            "analytic_continuation",
            "hilbert_polya_operator",
        ]:
            self.assertEqual(promoted[forbidden], "OPEN")
        self.assertFalse(promoted["rational_prime_pushforward_injective"])


if __name__ == "__main__":
    unittest.main(verbosity=2, warnings="ignore")
