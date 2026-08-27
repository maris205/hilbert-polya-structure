#!/usr/bin/env python3
"""Independent standard-library tests for the P28 owner ledger builder."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("build_owner_ledger.py")
SPEC = importlib.util.spec_from_file_location("p28_owner_ledger", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_owner_ledger.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OwnerLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tensor_powers = [1, 2, 4, 8]
        self.rows = MODULE.build_rows(self.tensor_powers)

    def test_validation_passes(self) -> None:
        report = MODULE.validate_rows(self.rows, self.tensor_powers)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["row_count"], 12)

    def test_duplicate_grid_row_fails(self) -> None:
        report = MODULE.validate_rows(self.rows + [dict(self.rows[0])], self.tensor_powers)
        self.assertEqual(report["status"], "FAIL")

    def test_degree_grid(self) -> None:
        expected = {"0": 0, "+1/2": 1, "-1/2": -1}
        for row in self.rows:
            self.assertEqual(
                row["operator_bundle_degree"],
                expected[row["field_b"]] * row["tensor_power_N"],
            )

    def test_field_reversal_is_involutive(self) -> None:
        partner = {"0": "0", "+1/2": "-1/2", "-1/2": "+1/2"}
        for row in self.rows:
            field_b = row["field_b"]
            self.assertEqual(partner[partner[field_b]], field_b)
            self.assertEqual(row["antiunitary_partner_field"], partner[field_b])

    def test_no_trace_credit_is_minted(self) -> None:
        for row in self.rows:
            self.assertEqual(row["rescaled_operator_owner"], "UNASSIGNED")
            self.assertEqual(row["scaling_evidence_token"], "MODELING_CHOICE")
            self.assertEqual(row["trace_regime"], "UNASSIGNED")
            self.assertEqual(row["energy_window"], "OPEN")
            self.assertEqual(
                row["magnetic_orbit_trace_ownership"], "NOT_ESTABLISHED"
            )
            self.assertEqual(row["fixed_operator_credit_transfer_allowed"], "false")

    def test_only_n1_positive_row_names_fixed_operator_identity(self) -> None:
        marked = [row for row in self.rows if row["operator_identity_at_N1"] == "true"]
        self.assertEqual(len(marked), 1)
        self.assertEqual(marked[0]["field_b"], "+1/2")
        self.assertEqual(marked[0]["tensor_power_N"], 1)

    def test_target_data_are_absent(self) -> None:
        serialized = repr(self.rows).lower()
        for forbidden in ("riemann_zero", "zero_table", "prime_table", "von_mangoldt"):
            self.assertNotIn(forbidden, serialized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
