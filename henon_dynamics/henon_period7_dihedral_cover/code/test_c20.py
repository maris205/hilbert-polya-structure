#!/usr/bin/env python3
"""Regression tests for the self-contained HCS-C20 certificate project."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import ast
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent
ROOT = CODE.parent
CERTIFICATE = ROOT / "results" / "c20_certificate.json"
REPORT = ROOT / "results" / "c20_independent_check.json"
CHECKER = CODE / "c20_independent_check.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("hcs_c20_checker", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load independent checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HCSC20Tests(unittest.TestCase):
    def test_full_independent_recomputation(self) -> None:
        report = load_checker().verify_certificate(CERTIFICATE)
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(report["checks_passed"], 133)

    def test_checked_report_binds_exact_certificate_bytes(self) -> None:
        report = json.loads(REPORT.read_text())
        actual = hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["certificate_sha256"], actual)
        self.assertIn("no import", report["independence"])
        self.assertIn("polynomial-quotient finite fields", report["independence"])

    def test_checker_is_nonimporting(self) -> None:
        source = CHECKER.read_text()
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module)
        self.assertNotIn("c20_producer", imported)
        self.assertNotIn("galois", imported)
        self.assertNotIn("numpy", imported)
        self.assertFalse(any(name.startswith("c19") for name in imported))
        self.assertNotIn("henon_period7_frobenius_curve", source)

    def test_fail_closed_on_identity_tamper(self) -> None:
        altered = json.loads(CERTIFICATE.read_text())
        altered["candidate_id"] = "HCS-C20-tampered"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tampered.json"
            path.write_text(json.dumps(altered))
            with self.assertRaisesRegex(AssertionError, "candidate identity"):
                load_checker().verify_certificate(path)

    def test_claim_boundary_and_local_factor_degrees(self) -> None:
        cert = json.loads(CERTIFICATE.read_text())
        boundary = cert["claim_boundary"]
        self.assertTrue(boundary["B_good_local_factors_at_5_11_13"])
        self.assertTrue(boundary["C_good_reduction_at_5_11_13"])
        self.assertTrue(boundary["E_good_reduction_at_5_11_13"])
        self.assertTrue(boundary["L_C_factors_certified_at_5_11_13"])
        self.assertTrue(boundary["L_E_equals_L_B_times_L_C_squared_certified_at_5_11_13"])
        self.assertFalse(boundary["blanket_good_reduction_claim_outside_5_11_13"])
        for row in cert["local_factors"]["selected_primes"]:
            self.assertEqual(len(row["L_B_coefficients_ascending"]), 5)
            self.assertEqual(len(row["L_C_coefficients_ascending"]), 7)
            self.assertEqual(len(row["L_E_coefficients_ascending"]), 17)
            self.assertTrue(row["B_good_reduction_proved"])
            self.assertTrue(row["C_good_reduction_proved"])
            self.assertTrue(row["E_good_reduction_proved"])
            self.assertIn("certified Hasse-Weil", row["L_C_status"])
            self.assertIn("certified Hasse-Weil", row["L_E_status"])

    def test_selected_prime_good_reduction_ledgers(self) -> None:
        cert = json.loads(CERTIFICATE.read_text())
        expected = {
            5: (0, "x**7 - x**4 + x**3 - 2*x**2 + 2*x - 2", "x + 1"),
            11: (0, "x**7 + 4*x**4 + x**3 - 2*x**2 + 2*x + 3", "x - 3"),
            13: (1, "x**7 - x**6 + 5*x**5 - x**4 - 3*x**3 - 5*x + 1", "x + 3"),
        }
        for row in cert["local_factors"]["selected_primes"]:
            p = row["p"]
            sigma0, polynomial, node_gcd = expected[p]
            ledger = row["selected_prime_good_reduction"]
            self.assertTrue(ledger["B_smooth_model"]["geometrically_integral_and_connected"])
            self.assertEqual(ledger["plane_integrality_witness"]["sigma0"], sigma0)
            self.assertEqual(ledger["plane_integrality_witness"]["P_sigma0_mod_p"], polynomial)
            self.assertEqual(ledger["residual_node_screen"]["gcd_P_Px"], node_gcd)
            self.assertTrue(ledger["vertical_inertia_screen"]["full_C7_vertical_inertia_excluded"])
            self.assertTrue(ledger["purity_and_tame_quotient"]["E_to_B_extends_finite_etale_degree_7"])
            self.assertTrue(ledger["plane_special_fiber_birational_comparison"]["same_function_field_as_E_mod_J"])
            self.assertIn("not inferred from p mod 7", ledger["geometric_connectedness"]["logic"])
            self.assertFalse(ledger["conclusion"]["blanket_all_prime_claim"])

    def test_plane_count_provenance(self) -> None:
        cert = json.loads(CERTIFICATE.read_text())
        expected = {
            5: ([3, 31, 141], [False, True, False], [9, 39, 147], [-3, -13, -21]),
            11: ([11, 159, 1163], [True, True, True], [19, 167, 1171], [-7, -45, 161]),
            13: ([10, 234, 2125], [False, True, False], [16, 242, 2131], [-2, -72, 67]),
        }
        for row in cert["local_factors"]["selected_primes"]:
            provenance = row["C_point_count_provenance"]
            affine, splits, counts, powers = expected[row["p"]]
            self.assertEqual(provenance["plane_affine_counts"], affine)
            self.assertEqual(provenance["node_splits"], splits)
            self.assertEqual(provenance["C_point_counts"], counts)
            self.assertEqual(provenance["C_frobenius_power_sums"], powers)
            self.assertEqual(
                provenance["L_C_from_Newton_coefficients_ascending"],
                row["L_C_coefficients_ascending"],
            )

    def test_square_class_scope_and_branch_witness(self) -> None:
        cert = json.loads(CERTIFICATE.read_text())
        neighbor = cert["chronological_neighbor"]
        branch = cert["branch_and_square_class"]
        self.assertEqual(neighbor["norm_polynomial"], branch["Q6"])
        self.assertFalse(neighbor["direct_square_root_identity_claimed"])
        self.assertEqual(branch["resultant_Q6_Px_at_u_remainder"], 2**42)
        self.assertTrue(branch["branch_root_is_simple"])

    def test_reflection_naming(self) -> None:
        cert = json.loads(CERTIFICATE.read_text())
        group = cert["group_and_genus"]
        self.assertIn("R(x,y)=(y,x)", group["reflection_naming"]["R"])
        self.assertIn("J=R*tau", group["reflection_naming"]["J"])
        self.assertIn("C=E/<J>", group["quotients"])
        self.assertNotIn("C=E/<R>", group["quotients"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
