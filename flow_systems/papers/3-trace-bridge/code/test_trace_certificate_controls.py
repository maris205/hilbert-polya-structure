#!/usr/bin/env python3
"""Unit tests for the deterministic Stage-3 trace-certificate controls."""

from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import trace_certificate_controls as controls  # noqa: E402


class QuadraticNormTests(unittest.TestCase):
    def test_integral_hyperbolic_discriminants_are_nonsquare(self) -> None:
        for trace_abs in range(3, 101):
            self.assertFalse(controls.is_square(trace_abs * trace_abs - 4))

    def test_base_norm_and_galois_inverse_are_exact(self) -> None:
        for trace_abs in range(3, 31):
            norm = controls.hyperbolic_norm(trace_abs)
            self.assertEqual(norm.norm(), Fraction(1))
            self.assertEqual(norm.conjugate(), norm.inverse())
            self.assertFalse(norm.is_rational())

    def test_positive_repetitions_remain_irrational_norm_one(self) -> None:
        for trace_abs in range(3, 21):
            norm = controls.hyperbolic_norm(trace_abs)
            for repetition in range(1, 9):
                powered = norm**repetition
                self.assertEqual(powered.norm(), Fraction(1))
                self.assertEqual(powered.conjugate(), powered.inverse())
                self.assertNotEqual(powered.b, 0)

    def test_finite_enumeration_summary(self) -> None:
        rows, summary = controls.enumerate_hyperbolic_norms(3, 8, 4)
        self.assertEqual(len(rows), 24)
        self.assertTrue(summary["all_discriminants_nonsquare"])
        self.assertTrue(summary["all_exact_field_norms_one"])
        self.assertTrue(summary["all_galois_conjugates_equal_inverse"])
        self.assertTrue(summary["all_tested_positive_powers_irrational"])

    def test_nonhyperbolic_trace_is_rejected(self) -> None:
        for trace_abs in (0, 1, 2):
            with self.assertRaises(ValueError):
                controls.hyperbolic_norm(trace_abs)


class SmoothGermTests(unittest.TestCase):
    def test_compact_bump_support(self) -> None:
        self.assertEqual(controls.compact_bump(0.0, 2.0, 0.5), 0.0)
        self.assertEqual(controls.compact_bump(1.5, 2.0, 0.5), 0.0)
        self.assertEqual(controls.compact_bump(2.5, 2.0, 0.5), 0.0)
        self.assertAlmostEqual(controls.compact_bump(2.0, 2.0, 0.5), 1.0)

    def test_sampled_germ_is_identical_locally_and_different_globally(self) -> None:
        rows, summary = controls.sampled_germ_control()
        self.assertEqual(len(rows), summary["sample_count"])
        self.assertTrue(summary["support_disjoint"])
        self.assertEqual(summary["maximum_local_absolute_difference"], 0.0)
        self.assertGreater(summary["maximum_global_absolute_difference"], 0.0)
        audited = [row for row in rows if row["inside_audited_neighborhood"]]
        self.assertTrue(audited)
        self.assertTrue(
            all(float(row["absolute_difference"]) == 0.0 for row in audited)
        )


class CertificateIdentityTests(unittest.TestCase):
    def test_same_source_records_pass_t0_without_implying_completeness(self) -> None:
        den, mod = controls.candidate_certificates()
        den_audit = den.validate_t0()
        mod_audit = mod.validate_t0()
        self.assertTrue(den_audit["t0_passes"])
        self.assertFalse(den_audit["all_required_fields_populated"])
        self.assertTrue(mod_audit["t0_passes"])
        self.assertTrue(mod_audit["all_required_fields_populated"])

    def test_coordinatewise_splice_and_clock_relock_fail_t0(self) -> None:
        audit = controls.certificate_t0_control()
        hybrid = audit["coordinatewise_den_mod_splice"]
        relocked = audit["same_candidate_different_clock_lock"]
        self.assertFalse(hybrid["t0_passes"])
        self.assertGreaterEqual(len(hybrid["observed_provenances"]), 2)
        self.assertFalse(relocked["t0_passes"])
        self.assertIn("clock", relocked["mismatched_fields"])
        self.assertFalse(audit["bridge_morphism_supplied"])
        self.assertFalse(audit["route_b_invocation_allowed"])


class ArtifactTests(unittest.TestCase):
    def test_run_outputs_are_deterministic_and_manifest_verifies(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output_dir = Path(temporary) / "results"
            first = controls.run_all(output_dir)
            self.assertTrue(first["manifest_verification"]["verified"])

            artifact_names = (
                "hyperbolic_norm_audit.csv",
                "smooth_germ_control.csv",
                "certificate_t0_audit.json",
                "run_summary.json",
                "manifest.sha256",
            )
            first_bytes = {
                name: (output_dir / name).read_bytes() for name in artifact_names
            }
            second = controls.run_all(output_dir)
            self.assertTrue(second["manifest_verification"]["verified"])
            second_bytes = {
                name: (output_dir / name).read_bytes() for name in artifact_names
            }
            self.assertEqual(first_bytes, second_bytes)

            summary = json.loads((output_dir / "run_summary.json").read_text())
            self.assertEqual(summary["data_policy"]["riemann_zero_inputs"], 0)
            self.assertEqual(summary["data_policy"]["fitted_parameters"], 0)
            self.assertEqual(summary["data_policy"]["network_inputs"], 0)
            self.assertFalse(summary["route_b_invocation_allowed"])

            with (output_dir / "hyperbolic_norm_audit.csv").open(
                newline="", encoding="utf-8"
            ) as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(
                len(rows), summary["hyperbolic_norm_control"]["rows"]
            )

    def test_manifest_detects_changed_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output_dir = Path(temporary) / "results"
            controls.run_all(output_dir)
            summary_path = output_dir / "run_summary.json"
            summary_path.write_text("changed\n", encoding="utf-8")
            verification = controls.verify_manifest(output_dir / "manifest.sha256")
            self.assertFalse(verification["verified"])
            self.assertTrue(
                any("run_summary.json" in failure for failure in verification["failures"])
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
