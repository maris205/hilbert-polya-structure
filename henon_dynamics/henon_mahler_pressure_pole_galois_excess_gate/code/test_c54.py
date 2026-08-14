#!/usr/bin/env python3
"""Unit tests for the HCS-P54 finite certificate."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
sys.path.insert(0, str(CODE))

import c54_pressure_pole as producer  # noqa: E402
import independent_check as checker  # noqa: E402


class PressurePoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = producer.build_certificate()

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.payload["dependency_locks"]), 8)

    def test_exact_galois_excess_pattern(self) -> None:
        rows = self.payload["exact_orbits"]
        self.assertTrue(rows["period_1"]["excess_positive"])
        self.assertTrue(rows["period_3"]["excess_positive"])
        self.assertTrue(rows["period_4"]["excess_zero"])

    def test_exact_excess_formulas(self) -> None:
        rows = self.payload["exact_orbits"]
        self.assertEqual(rows["period_1"]["galois_excess_formula"], "acosh(sqrt(7)-1)")
        self.assertEqual(rows["period_3"]["galois_excess_formula"], "acosh(21*sqrt(5)-19)")
        self.assertEqual(rows["period_4"]["galois_excess_formula"], "0")

    def test_pressure_residue_interval(self) -> None:
        interval = self.payload["physical_pressure_pole"]["residue_certificate"]
        left, right = interval["residue_open_interval"].strip("()").split(",")
        self.assertLess(float(left), float(interval["midpoint_value"]))
        self.assertLess(float(interval["midpoint_value"]), float(right))

    def test_scalar_roof_cohomology_obstruction(self) -> None:
        obstruction = self.payload["scalar_roof_cohomology_obstruction"]
        self.assertEqual(obstruction["period_four_forces_c"], "1.0")
        self.assertGreater(float(obstruction["period_one_residual"]), 1.0)

    def test_finite_log_derivative_identity(self) -> None:
        rows = self.payload["finite_log_derivative_fixture"]["fixtures"]
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(float(row["identity_abs_error"]) < 1e-55 for row in rows))

    def test_conditional_theorem_not_promoted(self) -> None:
        self.assertEqual(
            self.payload["conditional_holder_completion"]["status"],
            "CONDITIONAL_THEOREM",
        )
        self.assertFalse(self.payload["route_b_authorized"])

    def test_independent_validator(self) -> None:
        checker.validate(self.payload)

    def test_mutation_suite(self) -> None:
        self.assertEqual(checker.mutation_suite(self.payload), 12)

    def test_standalone_entrypoints(self) -> None:
        for command in (
            [sys.executable, "-B", str(CODE / "c54_pressure_pole.py"), "--check"],
            [sys.executable, "-B", str(CODE / "independent_check.py")],
        ):
            completed = subprocess.run(command, cwd=PROJECT, check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(completed.stdout)["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
