#!/usr/bin/env python3
"""Tests for the P27 Round-4 period-escape audit."""

from __future__ import annotations

import csv
import importlib.util
import io
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round4_period_escape.py")
SPEC = importlib.util.spec_from_file_location("p27_round4_escape", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not import round4_period_escape.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PeriodEscapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.project_root = MODULE_PATH.resolve().parents[1]
        cls.rows, cls.input_sha = MODULE.read_input(cls.project_root)
        cls.validation = MODULE.validate(cls.rows, cls.input_sha)

    def test_frozen_input(self) -> None:
        self.assertEqual(len(self.rows), 24)
        self.assertEqual(self.input_sha, MODULE.EXPECTED_INPUT_SHA256)

    def test_nested_moduli(self) -> None:
        self.assertTrue(self.validation["checks"]["nested_moduli"])
        self.assertTrue(self.validation["checks"]["frozen_moduli_match"])

    def test_order_divisibility_and_sequences(self) -> None:
        self.assertTrue(self.validation["checks"]["orders_divide_along_tower"])
        self.assertEqual(
            self.validation["orders_by_element"],
            {key: list(value) for key, value in MODULE.EXPECTED_ORDERS.items()},
        )

    def test_every_frozen_element_has_prefix_escape(self) -> None:
        self.assertTrue(
            self.validation["checks"]["every_frozen_element_shows_prefix_growth"]
        )
        self.assertEqual(
            self.validation["last_to_first_order_growth_factor"],
            {"G3-A": 288, "G3-B": 2880, "G3-C": 576},
        )

    def test_period_ratio_is_exactly_the_finite_order(self) -> None:
        output = MODULE.build_outputs(self.project_root)["round4_period_escape_ledger.csv"]
        rows = list(csv.DictReader(io.StringIO(output.decode("utf-8"))))
        self.assertTrue(
            all(row["period_to_base_ratio"] == row["finite_quotient_order"] for row in rows)
        )

    def test_owner_firewall(self) -> None:
        output = MODULE.build_outputs(self.project_root)["round4_period_escape_ledger.csv"]
        rows = list(csv.DictReader(io.StringIO(output.decode("utf-8"))))
        self.assertTrue(
            all(row["inverse_limit_periodic_orbit_credit"] == "FORBIDDEN" for row in rows)
        )
        self.assertTrue(all(row["formal_route_a_tuple"] == "UNASSIGNED" for row in rows))

    def test_outputs_are_byte_deterministic(self) -> None:
        first = MODULE.build_outputs(self.project_root)
        second = MODULE.build_outputs(self.project_root)
        self.assertEqual(first, second)
        self.assertEqual(MODULE.combined_hash(first), MODULE.combined_hash(second))

    def test_route_and_target_boundaries(self) -> None:
        self.assertEqual(self.validation["a2_a4"], "NOT_EVALUATED")
        self.assertFalse(self.validation["route_b_invocation_allowed"])
        self.assertFalse(self.validation["prime_or_zero_tables_used"])
        self.assertEqual(self.validation["general_period_escape_theorem"], "PROVED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
