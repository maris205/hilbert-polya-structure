#!/usr/bin/env python3
"""Tests for the P27 Round-5 cocompact residual-tower control."""

from __future__ import annotations

import csv
import importlib.util
import io
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round5_cocompact_owner_escape.py")
SPEC = importlib.util.spec_from_file_location("p27_round5_cocompact", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not import round5_cocompact_owner_escape.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CocompactOwnerEscapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = MODULE.build_rows()
        cls.validation = MODULE.validate(cls.rows)

    def test_frozen_scope_has_three_owners_and_eight_levels(self) -> None:
        self.assertEqual(len(MODULE.OWNERS), 3)
        self.assertEqual(MODULE.LEVELS, tuple(range(1, 9)))
        self.assertEqual(len(self.rows), 24)

    def test_factorial_moduli_are_exact_and_nested(self) -> None:
        self.assertEqual(MODULE.MODULI, (1, 2, 6, 24, 120, 720, 5040, 40320))
        self.assertTrue(self.validation["checks"]["factorial_schedule_nested"])

    def test_frozen_vectors_have_primitive_homology(self) -> None:
        for owner in MODULE.OWNERS:
            self.assertEqual(MODULE.homology_content(owner["homology_vector"]), 1)
        self.assertTrue(self.validation["checks"]["base_primitivity_certified"])

    def test_modular_homology_order_formula(self) -> None:
        self.assertEqual(MODULE.order_in_modular_homology((1, 0, 0, 0), 120), 120)
        self.assertEqual(MODULE.order_in_modular_homology((2, 0, 0, 0), 120), 60)
        self.assertEqual(MODULE.order_in_modular_homology((4, 6, 0, 0), 120), 60)
        self.assertEqual(MODULE.order_in_modular_homology((0, 0, 0, 0), 120), 1)

    def test_each_certified_bound_equals_n_factorial(self) -> None:
        self.assertTrue(self.validation["checks"]["homology_orders_equal_factorials"])
        for sequence in self.validation["lower_bounds_by_owner"].values():
            self.assertEqual(sequence, list(MODULE.MODULI))

    def test_lower_bounds_divide_forward(self) -> None:
        self.assertTrue(self.validation["checks"]["all_lower_bounds_divide_forward"])

    def test_no_full_residual_quotient_order_is_fabricated(self) -> None:
        self.assertFalse(self.validation["tower_definition"]["residual_core_enumerated"])
        self.assertTrue(
            self.validation["checks"]["full_quotient_orders_not_claimed_computed"]
        )

    def test_minimal_period_rows_keep_symbolic_length(self) -> None:
        payload = MODULE.build_outputs()["round5_cocompact_homology_escape_ledger.csv"]
        rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8"))))
        self.assertTrue(all("ell(" in row["minimal_lift_period_symbol"] for row in rows))
        self.assertTrue(
            all(row["certified_minimal_period_lower_bound"].startswith(">=") for row in rows)
        )

    def test_outputs_are_byte_deterministic(self) -> None:
        first = MODULE.build_outputs()
        second = MODULE.build_outputs()
        self.assertEqual(first, second)
        self.assertEqual(MODULE.combined_hash(first), MODULE.combined_hash(second))

    def test_route_owner_and_target_firewalls(self) -> None:
        self.assertTrue(
            self.validation["checks"]["route_and_target_firewalls_intact"]
        )
        self.assertEqual(self.validation["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.validation["a2_a4"], "NOT_EVALUATED")
        self.assertFalse(self.validation["route_b_invocation_allowed"])
        self.assertFalse(self.validation["prime_or_zero_tables_used"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
