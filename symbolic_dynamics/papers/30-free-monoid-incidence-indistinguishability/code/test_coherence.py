#!/usr/bin/env python3
"""Unit tests for the exact SD-C32 coherence prototype."""

from __future__ import annotations

from fractions import Fraction
import math
import unittest

from coherence_core import (
    FreeCommutativeMonoid,
    analytic_gram,
    canonical_statistic,
    divisibility_inventory,
    divisibility_poset,
    exact_projector_checks,
    finite_poset_record,
    formal_divisibility_record,
    formal_free_record,
    gamma_length,
    generic_dag_poset,
    mutated_cover_poset,
    permute_poset,
    predicate_mask_rows,
    random_inventory_poset,
    random_permutation,
    tail_certificates,
)


class CoherenceFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baselines = [formal_divisibility_record(cutoff) for cutoff in (12, 18, 30)]
        cls.controls = [
            finite_poset_record(mutated_cover_poset()),
            finite_poset_record(
                divisibility_inventory((1, 4, 6, 9, 12, 18, 36), "composite_only")
            ),
            finite_poset_record(generic_dag_poset()),
            finite_poset_record(random_inventory_poset()),
        ]

    def test_source_atoms_come_from_covers(self) -> None:
        poset = divisibility_poset(12)
        self.assertEqual(tuple(poset.roof_weights[i] for i in poset.atoms()), (2, 3, 5, 7, 11))

    def test_incidence_compiler(self) -> None:
        self.assertTrue(exact_projector_checks(divisibility_poset(12))["all_pass"])

    def test_mutated_compiler(self) -> None:
        self.assertTrue(exact_projector_checks(mutated_cover_poset())["all_pass"])

    def test_baseline_pair_counts(self) -> None:
        self.assertEqual([row["qualified_pairs"] for row in self.baselines], [10, 21, 45])

    def test_baseline_triple_counts(self) -> None:
        self.assertEqual([row["qualified_triples"] for row in self.baselines], [10, 35, 120])

    def test_every_baseline_predicate(self) -> None:
        self.assertTrue(
            all(
                all(pair["coherence"]["predicates"].values())
                for record in self.baselines
                for pair in record["pair_rows"]
            )
        )

    def test_baseline_statistics_nonzero(self) -> None:
        self.assertTrue(
            all(
                record["C2_nonzero"]
                and record["theta3_nonzero"]
                and record["auxiliary_e3_nonzero"]
                for record in self.baselines
            )
        )

    def test_mutated_pair_minimal_counterexample(self) -> None:
        survivors = [
            row["atom_weights"]
            for row in self.controls[0]["pair_rows"]
            if row["coherence"]["full"]
        ]
        self.assertEqual(survivors, [[2, 5], [2, 7], [3, 5]])

    def test_mutated_has_no_full_triple(self) -> None:
        self.assertEqual(self.controls[0]["qualified_triples"], 0)

    def test_other_finite_controls_zero(self) -> None:
        self.assertTrue(
            all(
                record["qualified_pairs"] == record["qualified_triples"] == 0
                for record in self.controls[1:]
            )
        )

    def test_all_four_finite_triple_controls_zero(self) -> None:
        self.assertTrue(all(record["qualified_triples"] == 0 for record in self.controls))

    def test_generic_relabel(self) -> None:
        poset = generic_dag_poset()
        order = random_permutation(poset.size, 30331)
        copy = permute_poset(poset, order, "copy")
        self.assertEqual(
            canonical_statistic(finite_poset_record(poset)),
            canonical_statistic(finite_poset_record(copy)),
        )

    def test_transported_free_clone_pair(self) -> None:
        base = self.baselines[0]
        clone = formal_free_record(base["atom_weights"], "clone")
        self.assertEqual(canonical_statistic(base), canonical_statistic(clone))

    def test_transported_free_clone_triple(self) -> None:
        base = self.baselines[-1]
        clone = formal_free_record(
            base["atom_weights"], "clone_relabel", relabel_seed=31030
        )
        self.assertEqual(canonical_statistic(base), canonical_statistic(clone))

    def test_polynomial_UFD_alias(self) -> None:
        base = self.baselines[1]
        clone = formal_free_record(
            base["atom_weights"], "poly", alias="polynomial_UFD_monomials"
        )
        self.assertEqual(canonical_statistic(base), canonical_statistic(clone))

    def test_free_monoid_all_pairs_and_triples(self) -> None:
        monoid = FreeCommutativeMonoid(
            "M", ("a", "b", "c", "d"), (10, 14, 21, 25), 2
        )
        self.assertTrue(
            all(
                monoid.coherence(subset)["full"]
                for size in (2, 3)
                for subset in __import__("itertools").combinations(range(4), size)
            )
        )

    def test_free_monoid_element_count(self) -> None:
        monoid = FreeCommutativeMonoid("M", ("a", "b", "c"), (2, 3, 5), 3)
        self.assertEqual(monoid.element_count, 64)

    def test_free_monoid_mobius_squarefree(self) -> None:
        monoid = FreeCommutativeMonoid("M", ("a", "b"), (2, 3), 2)
        self.assertEqual(monoid.mobius_from_bottom((1, 1)), 1)
        self.assertEqual(monoid.mobius_from_bottom((2, 0)), 0)

    def test_analytic_gram_pair(self) -> None:
        gram = analytic_gram((2, 3))
        self.assertEqual(gram[0][1], Fraction(1, 17 * 82))

    def test_auxiliary_e2_negative(self) -> None:
        self.assertLess(
            Fraction(
                self.baselines[-1]["auxiliary_det_e2"]["numerator"],
                self.baselines[-1]["auxiliary_det_e2"]["denominator"],
            ),
            0,
        )

    def test_connected_theta_positive(self) -> None:
        self.assertGreater(
            Fraction(
                self.baselines[-1]["theta3"]["numerator"],
                self.baselines[-1]["theta3"]["denominator"],
            ),
            0,
        )

    def test_pair_tail_decreases(self) -> None:
        first = tail_certificates(12)["C2_absolute_tail_bound_over_C_eta"]
        last = tail_certificates(30)["C2_absolute_tail_bound_over_C_eta"]
        self.assertLess(
            Fraction(last["numerator"], last["denominator"]),
            Fraction(first["numerator"], first["denominator"]),
        )

    def test_triangle_tail_formula(self) -> None:
        row = tail_certificates(12)["triangle_absolute_tail_bound_over_C_eta_cubed"]
        self.assertEqual(
            Fraction(row["numerator"], row["denominator"]),
            Fraction(25, 16_777_216 * 12**8),
        )

    def test_pair_marker(self) -> None:
        row = self.baselines[0]["pair_rows"][0]
        p, q = row["atom_weights"]
        self.assertEqual(row["marker_exponent"], gamma_length(p) + gamma_length(q))

    def test_triple_marker(self) -> None:
        row = self.baselines[0]["triple_rows"][0]
        self.assertEqual(
            row["marker_exponent"],
            2 * sum(gamma_length(value) for value in row["atom_weights"]),
        )

    def test_predicate_masks_cannot_fix_mutated_pair(self) -> None:
        rows = predicate_mask_rows(
            [self.baselines[-1], self.controls[0], formal_free_record(self.baselines[-1]["atom_weights"], "clone")]
        )
        for mask in range(1, 32):
            mutation = next(
                row
                for row in rows
                if row["mask"] == mask and row["source"] == "mutated_cover_promote_6"
            )
            self.assertGreater(mutation["qualified_pairs"], 0)

    def test_every_mask_copied_by_clone(self) -> None:
        clone = formal_free_record(self.baselines[-1]["atom_weights"], "clone")
        rows = predicate_mask_rows([self.baselines[-1], clone])
        for mask in range(1, 32):
            base = next(
                row
                for row in rows
                if row["mask"] == mask and row["source"] == self.baselines[-1]["source"]
            )
            copied = next(
                row
                for row in rows
                if row["mask"] == mask and row["source"] == "clone"
            )
            self.assertEqual(
                (base["qualified_pairs"], base["qualified_triples"]),
                (copied["qualified_pairs"], copied["qualified_triples"]),
            )

    def test_combinatorial_counts(self) -> None:
        self.assertEqual(math.comb(10, 2), 45)
        self.assertEqual(math.comb(10, 3), 120)


if __name__ == "__main__":
    unittest.main()
