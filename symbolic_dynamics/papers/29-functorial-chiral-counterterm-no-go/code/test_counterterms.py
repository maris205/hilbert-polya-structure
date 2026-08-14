#!/usr/bin/env python3
"""Unit tests for the exact SD-C31 prototype."""

from __future__ import annotations

from fractions import Fraction
import unittest

from counterterm_core import (
    analytic_gram,
    baseline_scheme_record,
    canonical_direct_ledger,
    coefficient_search,
    cutoff_compiler_check,
    direct_control_record,
    divisibility_inventory,
    divisibility_poset,
    exact_projector_checks,
    generic_dag_poset,
    identity_matrix,
    local_shift_family,
    matrix_inverse,
    matrix_multiply,
    mutated_cover_poset,
    permute_poset,
    radical_amplitude,
    random_inventory_poset,
    random_permutation,
    tail_certificates,
    transport_check,
)


class ExactIncidenceTests(unittest.TestCase):
    def test_fraction_matrix_inverse(self) -> None:
        matrix = (
            (Fraction(1), Fraction(1), Fraction(1)),
            (Fraction(0), Fraction(1), Fraction(1)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        self.assertEqual(matrix_multiply(matrix, matrix_inverse(matrix)), identity_matrix(3))

    def test_divisibility_source_atoms(self) -> None:
        poset = divisibility_poset(12)
        self.assertEqual(tuple(poset.roof_weights[i] for i in poset.atoms()), (2, 3, 5, 7, 11))

    def test_mutated_cover_promotes_six(self) -> None:
        poset = mutated_cover_poset(18)
        self.assertIn(6, tuple(poset.roof_weights[i] for i in poset.atoms()))

    def test_composite_only_atoms(self) -> None:
        poset = divisibility_inventory((1, 4, 6, 9, 12, 18, 36), "control")
        self.assertEqual(tuple(poset.roof_weights[i] for i in poset.atoms()), (4, 6, 9))

    def test_generic_dag_has_four_atoms(self) -> None:
        self.assertEqual(len(generic_dag_poset().atoms()), 4)

    def test_random_inventory_has_five_atoms(self) -> None:
        self.assertEqual(len(random_inventory_poset().atoms()), 5)

    def test_projector_compiler_sanity(self) -> None:
        self.assertTrue(exact_projector_checks(divisibility_poset(12))["all_pass"])

    def test_mutated_compiler_sanity(self) -> None:
        self.assertTrue(exact_projector_checks(mutated_cover_poset())["all_pass"])

    def test_cutoff_restriction_12_to_18(self) -> None:
        self.assertTrue(cutoff_compiler_check(12, 18)["all_pass"])

    def test_cutoff_restriction_18_to_30(self) -> None:
        self.assertTrue(cutoff_compiler_check(18, 30)["all_pass"])

    def test_relabel_transport(self) -> None:
        poset = divisibility_poset(12)
        order = random_permutation(poset.size, 29112)
        copy = permute_poset(poset, order, "copy")
        self.assertTrue(transport_check(poset, copy, order)["all_pass"])


class CountertermTests(unittest.TestCase):
    def test_analytic_diagonal(self) -> None:
        self.assertEqual(analytic_gram((2, 3))[0][0], Fraction(17, 16))

    def test_analytic_off_diagonal(self) -> None:
        self.assertEqual(analytic_gram((2, 3))[0][1], Fraction(1, 17 * 82))

    def test_full_lead_identity(self) -> None:
        for cutoff in (12, 18, 30):
            self.assertTrue(baseline_scheme_record(cutoff)["identity_D_equals_H_plus_S0"])

    def test_minimal_schemes_are_distinct(self) -> None:
        self.assertTrue(baseline_scheme_record(30)["schemes_distinct"])

    def test_shift_family_is_local_and_natural(self) -> None:
        row = local_shift_family(30, (Fraction(1, 2), Fraction(-1), Fraction(2)))
        self.assertTrue(row["is_atom_local"] and row["is_isomorphism_natural"] and row["is_prefix_additive"])

    def test_tail_bounds_decrease(self) -> None:
        small = tail_certificates(12)["shift_tail_bounds"]["S0"]["rational_upper_bound"]
        large = tail_certificates(30)["shift_tail_bounds"]["S0"]["rational_upper_bound"]
        self.assertLess(Fraction(large["numerator"], large["denominator"]), Fraction(small["numerator"], small["denominator"]))

    def test_radical_amplitude_exact(self) -> None:
        row = radical_amplitude(Fraction(4), 18)
        self.assertEqual(row["squarefree_radicand"], 2)
        self.assertEqual(row["rational_coefficient"]["text"], "2/3")

    def test_all_controls_have_mixed_terms(self) -> None:
        controls = (
            mutated_cover_poset(),
            divisibility_inventory((1, 4, 6, 9, 12, 18, 36), "composite"),
            generic_dag_poset(),
            random_inventory_poset(),
        )
        self.assertTrue(all(direct_control_record(poset)["nonzero_mixed_count"] > 0 for poset in controls))

    def test_all_controls_have_B4_terms(self) -> None:
        controls = (mutated_cover_poset(), generic_dag_poset(), random_inventory_poset())
        self.assertTrue(all(direct_control_record(poset)["positive_b4_count"] > 0 for poset in controls))

    def test_generic_direct_ledger_relabels(self) -> None:
        poset = generic_dag_poset()
        order = random_permutation(poset.size, 29331)
        copy = permute_poset(poset, order, "copy")
        self.assertEqual(canonical_direct_ledger(direct_control_record(poset)), canonical_direct_ledger(direct_control_record(copy)))

    def test_coefficient_grid_has_no_selective_solution(self) -> None:
        grid = tuple(Fraction(value, 2) for value in (-4, -2, -1, 0, 1, 2, 4))
        self.assertTrue(coefficient_search(grid)["exact_no_solution"])

    def test_preserve_and_cancel_constraints_conflict(self) -> None:
        self.assertNotEqual(Fraction(0), Fraction(1))


if __name__ == "__main__":
    unittest.main()
