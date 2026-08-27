#!/usr/bin/env python3
"""Independent standard-library tests for the P25 Round-4 audit."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round4_conditioning_audit.py")
SPEC = importlib.util.spec_from_file_location("p25_round4_audit", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round4_conditioning_audit.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ConditioningAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.project_root = MODULE_PATH.resolve().parents[1]
        cls.rows, cls.input_sha = MODULE.read_rows(cls.project_root)
        cls.source_audit = MODULE.refinement_source_audit(cls.project_root)
        cls.metrics = MODULE.build_metrics(cls.rows, cls.source_audit, cls.input_sha)

    def test_frozen_input_and_total_partition(self) -> None:
        self.assertEqual(len(self.rows), 2241)
        self.assertEqual(self.input_sha, MODULE.EXPECTED_INPUT_SHA256)
        self.assertEqual(self.metrics["direct_newton_rows"], 2202)
        self.assertEqual(self.metrics["stationarity_fallback_rows"], 39)

    def test_fallback_length_partition(self) -> None:
        self.assertEqual(
            self.metrics["fallback_by_topological_length"], {"11": 1, "12": 38}
        )

    def test_fallback_distance_partition(self) -> None:
        self.assertEqual(
            self.metrics["fallback_by_distance_ratio"],
            {"5.8": 4, "6": 10, "6.2": 25},
        )

    def test_fallback_condition_tiers(self) -> None:
        self.assertEqual(
            self.metrics["fallback_by_source_trace_condition_tier"],
            {"ABS_TRACE_1E9_TO_1E12": 1, "ABS_TRACE_GT_1E12": 38},
        )

    def test_refinement_selector_is_target_free_in_source(self) -> None:
        self.assertFalse(self.source_audit["fallback_selector_uses_paraxial_target"])
        self.assertEqual(self.source_audit["missing_functions"], [])
        self.assertEqual(self.source_audit["forbidden_target_name_findings"], {})
        self.assertTrue(
            self.source_audit[
                "fallback_call_precedes_paraxial_comparison_assignment"
            ]
        )

    def test_shared_acceptance_contract_passes(self) -> None:
        self.assertTrue(all(self.metrics["acceptance_checks"].values()))
        self.assertTrue(all(self.metrics["descriptive_claim_checks"].values()))

    def test_outputs_are_byte_deterministic(self) -> None:
        first = MODULE.build_outputs(self.project_root)
        second = MODULE.build_outputs(self.project_root)
        self.assertEqual(first, second)
        self.assertEqual(MODULE.combined_hash(first), MODULE.combined_hash(second))

    def test_route_and_target_firewalls(self) -> None:
        self.assertEqual(self.metrics["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["a2_evaluation"], "NOT_RUN")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["prime_or_zero_tables_used"])
        self.assertEqual(
            self.metrics["half_density_control_verdict"],
            "STOP_SCOPED / PROVES_TOO_MUCH",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
