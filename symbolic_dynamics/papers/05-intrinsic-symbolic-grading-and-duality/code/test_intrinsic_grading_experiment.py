#!/usr/bin/env python3
"""Regression tests for the Paper05 exact grading and duality audit."""

from __future__ import annotations

import unittest

from intrinsic_grading_experiment import (
    DUAL_GRID,
    complex_invariants,
    divisor_mobius_prefix,
    dual_ratio_diagnostics,
    finite_dual_ratio,
    proper_open_divisors,
    run_experiment,
    schatten_diagnostics,
)


class IntrinsicGradingTest(unittest.TestCase):
    def test_hand_complexes(self) -> None:
        expected = {
            2: (-1, {"-1": 1}),
            4: (0, {}),
            6: (1, {"0": 1}),
            12: (0, {}),
            30: (-1, {"1": 1}),
        }
        for n, (euler, betti) in expected.items():
            with self.subTest(n=n):
                inv = complex_invariants(n)
                self.assertTrue(inv["boundary_squared_zero_over_Z"])
                self.assertEqual(inv["reduced_euler"], euler)
                self.assertEqual(inv["homology_supertrace"], euler)
                self.assertEqual(inv["betti_gf2"], betti)

    def test_poset_mobius_prefix(self) -> None:
        mu = divisor_mobius_prefix(64)
        for n in range(2, 65):
            inv = complex_invariants(n)
            self.assertEqual(inv["reduced_euler"], mu[n])
            self.assertEqual(inv["homology_supertrace"], mu[n])

    def test_finite_dual_identities(self) -> None:
        atoms = [n for n in range(2, 128) if not proper_open_divisors(n)]
        rows, summary = dual_ratio_diagnostics(atoms)
        self.assertLess(summary["max_reflection_product_residual"], 1e-12)
        self.assertLess(summary["max_critical_modulus_residual"], 1e-12)
        for _, s in DUAL_GRID:
            ratio = finite_dual_ratio(atoms, s)
            reflected = finite_dual_ratio(atoms, 1.0 - s)
            self.assertAlmostEqual(abs(ratio * reflected - 1.0), 0.0, places=12)
        self.assertGreater(len(rows), 0)

    def test_schatten_domain_diagnostics(self) -> None:
        atoms = [n for n in range(2, 128) if not proper_open_divisors(n)]
        rows, summary = schatten_diagnostics(atoms)
        self.assertFalse(summary["ordinary_trace_class_overlap"])
        self.assertFalse(summary["S_2_overlap"])
        self.assertEqual(summary["S_4_overlap"], "1/4<Re(s)<3/4")
        self.assertFalse(summary["relative_ratio_minus_identity_open_S_q_domain"])
        self.assertTrue(summary["relative_ratio_center_isolated_zero"])
        central = [
            row
            for row in rows
            if row["point"] == "critical_real"
            and row["sector"] == "relative_ratio_minus_identity"
        ]
        self.assertTrue(all(row["partial_norm"] == 0.0 for row in central))

    def test_full_frozen_run(self) -> None:
        summary, artifacts = run_experiment(512)
        exact = summary["exact_main"]
        self.assertEqual(exact["objects_checked"], 511)
        self.assertEqual(exact["boundary_squared_zero_fraction"], 1.0)
        self.assertEqual(exact["euler_equals_poset_mobius_fraction"], 1.0)
        self.assertEqual(exact["homology_supertrace_equals_mobius_fraction"], 1.0)
        self.assertEqual(exact["betti_pattern_exact_fraction"], 1.0)
        self.assertEqual(exact["max_simplex_object"], 480)
        self.assertEqual(exact["max_simplex_count"], 976)
        self.assertEqual(exact["total_simplices_including_empty"], 15629)
        self.assertEqual(
            summary["graded_determinant_pair"]["berezinian_zeta_coefficient_accuracy"],
            1.0,
        )
        self.assertEqual(
            summary["graded_determinant_pair"]
            ["fock_supertrace_mobius_coefficient_accuracy"],
            1.0,
        )
        self.assertEqual(summary["factor_count_with_multiplicity"]
                         ["nonsquarefree_false_nonzero_count"], 198)
        self.assertEqual(summary["free_mixing"]["pairs"], 28)
        self.assertEqual(summary["decision"]["overall"], "SCOPED_THEOREM_STOP")
        self.assertFalse(summary["source_lock"]["zero_data_read"])
        self.assertEqual(len(artifacts["factorization_complexes"]), 511)


if __name__ == "__main__":
    unittest.main(verbosity=2)
