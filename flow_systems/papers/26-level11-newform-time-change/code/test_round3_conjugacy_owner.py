#!/usr/bin/env python3
"""Independent standard-library tests for P26 Round 3."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round3_conjugacy_owner.py")
SPEC = importlib.util.spec_from_file_location("p26_round3", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round3_conjugacy_owner.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ConjugacyOwnerTests(unittest.TestCase):
    def test_matrix_inverse_and_conjugation(self) -> None:
        matrix = (15, 4, 11, 3)
        inverse = MODULE.matrix_inverse(matrix)
        self.assertEqual(
            MODULE.ROUND2.matrix_multiply(matrix, inverse), MODULE.IDENTITY
        )
        for _, owner_change in MODULE.CONJUGATORS:
            conjugated = MODULE.conjugate(matrix, owner_change)
            self.assertEqual(MODULE.ROUND2.determinant(conjugated), 1)
            self.assertEqual(MODULE.ROUND2.trace(conjugated), 18)

    def test_all_exact_owner_rows_validate(self) -> None:
        rows = MODULE.exact_owner_rows()
        self.assertEqual(len(rows), 99)
        self.assertEqual(MODULE.validate_exact_rows(rows), [])

    def test_repeat_and_inverse_identities_are_exact(self) -> None:
        for row in MODULE.exact_owner_rows():
            self.assertEqual(row["square_conjugacy_identity_exact"], "true")
            self.assertEqual(row["cube_conjugacy_identity_exact"], "true")
            self.assertEqual(row["inverse_orientation_identity_exact"], "true")

    def test_translation_covariance_small_configuration(self) -> None:
        rows = MODULE.translation_covariance_rows(q_cutoff=96, quadrature_panels=128)
        self.assertEqual(len(rows), 44)
        self.assertLess(max(float(row["absolute_residual"]) for row in rows), 1e-11)

    def test_no_target_data_or_route_promotion(self) -> None:
        rows = MODULE.exact_owner_rows()
        serialized = repr(rows).lower()
        for forbidden in ("prime_table", "riemann_zero", "formal_a0_a4_tuple"):
            self.assertNotIn(forbidden, serialized)
        self.assertTrue(all(row["analytic_evidence_token"] == "PROVED" for row in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
