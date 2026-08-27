#!/usr/bin/env python3
"""Independent standard-library tests for P26 Round 4."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round4_hecke_correspondence.py")
SPEC = importlib.util.spec_from_file_location("p26_round4", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round4_hecke_correspondence.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HeckeCorrespondenceTests(unittest.TestCase):
    def test_double_coset_right_action_is_unique_and_exact(self) -> None:
        rows = MODULE.branch_owner_rows()
        self.assertEqual(len(rows), 385)
        self.assertTrue(
            all(row["right_action_identity_exact"] == "true" for row in rows)
        )
        self.assertTrue(all(int(row["gluing_determinant"]) == 1 for row in rows))
        self.assertTrue(all(int(row["gluing_c_mod_11"]) == 0 for row in rows))

    def test_permutation_cycles_partition_each_branch_set(self) -> None:
        for word in MODULE.ROUND2.gamma0_11_positive_necklaces(9):
            matrix = MODULE.ROUND2.matrix_from_word(word)
            for prime in MODULE.HECKE_PRIMES:
                ids = [item[0] for item in MODULE.hecke_representatives(prime)]
                permutation = MODULE.right_action_permutation(matrix, prime)
                cycles = MODULE.permutation_cycles(permutation, ids)
                flattened = [branch_id for cycle in cycles for branch_id in cycle]
                self.assertEqual(sorted(flattened), sorted(ids))
                self.assertEqual(sum(map(len, cycles)), prime + 1)

    def test_cycle_owner_is_integral_gamma0_11_with_power_trace(self) -> None:
        word = "LRRLRRR"
        matrix = MODULE.ROUND2.matrix_from_word(word)
        prime = 5
        representatives = dict(MODULE.hecke_representatives(prime))
        ids = list(representatives)
        cycles = MODULE.permutation_cycles(
            MODULE.right_action_permutation(matrix, prime), ids
        )
        for cycle in cycles:
            branch = representatives[cycle[0]]
            owner = MODULE.integral_matrix(
                MODULE.multiply(
                    MODULE.multiply(
                        branch, MODULE.ROUND2.matrix_power(matrix, len(cycle))
                    ),
                    MODULE.rational_inverse(branch),
                )
            )
            self.assertEqual(MODULE.determinant(owner), 1)
            self.assertEqual(owner[2] % 11, 0)
            self.assertEqual(
                MODULE.ROUND2.trace(owner),
                MODULE.ROUND2.trace(
                    MODULE.ROUND2.matrix_power(matrix, len(cycle))
                ),
            )

    def test_primitivity_certificate_detects_a_known_power(self) -> None:
        primitive = (15, 4, 11, 3)
        square = MODULE.ROUND2.matrix_power(primitive, 2)
        repeated = MODULE.primitivity_certificate(square)
        self.assertFalse(repeated["primitive"])
        self.assertEqual(repeated["primitive_root_exponent"], 2)
        self.assertEqual(repeated["primitive_root_matrix"], primitive)
        base = MODULE.primitivity_certificate(primitive)
        self.assertTrue(base["primitive"])
        self.assertEqual(base["primitive_root_exponent"], 1)

        # PSL central-sign regression: if B=-primitive has negative trace, then
        # B^3=-primitive^3 represents the same PSL class as primitive^3.  The
        # positive-trace representative must still expose the exact root.
        negative_trace_root = tuple(-entry for entry in primitive)
        negative_cube = MODULE.ROUND2.matrix_power(negative_trace_root, 3)
        positive_psl_representative = tuple(-entry for entry in negative_cube)
        signed_repeated = MODULE.primitivity_certificate(positive_psl_representative)
        self.assertFalse(signed_repeated["primitive"])
        self.assertEqual(signed_repeated["primitive_root_exponent"], 3)
        self.assertEqual(signed_repeated["primitive_root_matrix"], primitive)

    def test_eta_product_hecke_coefficients_are_exact(self) -> None:
        rows = MODULE.coefficient_ledger()
        self.assertEqual(len(rows), 320)
        self.assertTrue(all(row["eigen_relation_exact"] == "true" for row in rows))
        self.assertEqual({int(row["a_p"]) for row in rows}, {-2, -1, 1, 4})

    def test_nonmodular_control_fails_but_has_no_owner(self) -> None:
        rows = MODULE.coefficient_ledger()
        failures = [
            row for row in rows if row["generic_control_relation_exact"] == "false"
        ]
        self.assertGreater(len(failures), 250)
        self.assertTrue(
            all(
                row["generic_control_owner_status"]
                == "NO_GAMMA0_11_QUOTIENT_OWNER"
                for row in rows
            )
        )

    def test_direct_period_identity_small_configuration(self) -> None:
        word = "LRRLRRR"
        matrix = MODULE.ROUND2.matrix_from_word(word)
        coefficients = MODULE.ROUND2.level11_eta_product_coefficients(384)
        generic = [
            coefficient + MODULE.control_perturbation(index)
            for index, coefficient in enumerate(coefficients)
        ]
        base = MODULE.transformed_path_period(
            matrix, (1, 0, 0, 1), coefficients, 64
        )
        generic_base = MODULE.transformed_path_period(
            matrix, (1, 0, 0, 1), generic, 64
        )
        prime = 2
        eigenvalue = coefficients[prime]
        hecke_sum = sum(
            (
                MODULE.transformed_path_period(matrix, branch, coefficients, 64)
                for _, branch in MODULE.hecke_representatives(prime)
            ),
            0.0j,
        )
        generic_sum = sum(
            (
                MODULE.transformed_path_period(matrix, branch, generic, 64)
                for _, branch in MODULE.hecke_representatives(prime)
            ),
            0.0j,
        )
        self.assertLess(abs(hecke_sum - eigenvalue * base), 1.0e-10)
        self.assertGreater(abs(generic_sum - eigenvalue * generic_base), 1.0)

    def test_scope_does_not_promote_route_or_euler_claim(self) -> None:
        serialized = repr(MODULE.coefficient_ledger()).lower()
        self.assertNotIn("riemann_zero", serialized)
        self.assertNotIn("route_b_ready", serialized)
        self.assertEqual(MODULE.CLOSED_CONTROL_RE_WEIGHT, 3)
        self.assertEqual(MODULE.CLOSED_CONTROL_IM_WEIGHT, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
