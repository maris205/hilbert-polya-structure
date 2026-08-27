#!/usr/bin/env python3
"""Independent standard-library tests for the P28 Round-3 trace contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("build_round3_trace_contract.py")
SPEC = importlib.util.spec_from_file_location("p28_round3_contract", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round3_trace_contract.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TraceContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tensor_powers = [2, 4, 8, 16]
        self.rows = MODULE.build_rows(self.tensor_powers)

    def test_validation_passes(self) -> None:
        report = MODULE.validate_rows(self.rows, self.tensor_powers)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["row_count"], 12)
        self.assertEqual(report["source_bound_signed_field_rows"], 8)

    def test_even_subsequence_mapping(self) -> None:
        for row in self.rows:
            self.assertEqual(row["source_tensor_m"], row["tensor_power_N"] // 2)
            self.assertEqual(row["even_subsequence"], "true")

    def test_unit_speed_shell_algebra_is_frozen(self) -> None:
        for n_value in self.tensor_powers:
            invariants = MODULE.algebraic_invariants(n_value)
            self.assertTrue(all(invariants.values()))
        for row in self.rows:
            self.assertEqual(row["classical_hamiltonian"], "sqrt(|p|^2+1/4)")
            self.assertEqual(row["spectral_center_lambda"], "(sqrt(5)/2)*N")
            self.assertEqual(row["classical_shell"], "|p|^2=1")
            self.assertEqual(row["laplacian_center_nu"], "N^2")
            self.assertEqual(row["physical_unit_speed"], "1_for_H0=|p|^2/2")
            self.assertEqual(
                row["clock_conversion"], "T_trace=(sqrt(5)/2)*T_physical"
            )

    def test_signed_fields_are_source_bound_but_control_is_open(self) -> None:
        for row in self.rows:
            self.assertIn("real_even", row["test_function_class"])
            if row["field_b"] == "0":
                self.assertEqual(row["trace_binding_evidence_token"], "OPEN")
            else:
                self.assertEqual(row["trace_binding_evidence_token"], "PROVED")
                self.assertIn("sqrt(5/3)", row["primitive_period_trace_clock"])
                self.assertIn("2/sqrt(3)", row["primitive_period_physical_clock"])

    def test_time_reversed_owner_keeps_k_and_reverses_action(self) -> None:
        for n_value in self.tensor_powers:
            positive = next(
                row
                for row in self.rows
                if row["field_b"] == "+1/2"
                and row["tensor_power_N"] == n_value
            )
            negative = next(
                row
                for row in self.rows
                if row["field_b"] == "-1/2"
                and row["tensor_power_N"] == n_value
            )
            self.assertEqual(
                positive["action_frequency_per_N"],
                "-sqrt(3)/2*k*log_Norm(h)",
            )
            self.assertEqual(
                negative["action_frequency_per_N"],
                "+sqrt(3)/2*k*log_Norm(h)",
            )

        report = MODULE.validate_rows(self.rows, self.tensor_powers)
        self.assertEqual(report["signed_action_pairings_checked"], 4)

    def test_owner_and_route_firewalls(self) -> None:
        for row in self.rows:
            self.assertEqual(row["fixed_operator_credit_transfer_allowed"], "false")
            self.assertEqual(row["formal_route_a_tuple"], "UNASSIGNED")
            self.assertEqual(row["route_b_invocation_allowed"], "false")

    def test_invalid_tensor_powers_fail(self) -> None:
        for raw in ("", "1,2", "2,2", "3"):
            with self.assertRaises(ValueError):
                MODULE.parse_even_tensor_powers(raw)

    def test_target_data_are_absent(self) -> None:
        serialized = repr(self.rows).lower()
        for forbidden in ("riemann_zero", "zero_table", "prime_table", "von_mangoldt"):
            self.assertNotIn(forbidden, serialized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
