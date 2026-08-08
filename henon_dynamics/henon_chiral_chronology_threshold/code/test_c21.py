#!/usr/bin/env python3
"""Regression and fail-closed tests for HCS-C21."""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
CERTIFICATE = PROJECT / "results" / "c21_certificate.json"
REPORT = PROJECT / "results" / "c21_independent_check.json"
CHECKER = CODE / "c21_independent_check.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("hcs_c21_checker", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load independent checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mutated_path(mutator):
    data = json.loads(CERTIFICATE.read_text())
    mutator(data)
    directory = tempfile.TemporaryDirectory()
    path = Path(directory.name) / "mutated.json"
    path.write_text(json.dumps(data))
    return directory, path


class HCSC21Tests(unittest.TestCase):
    def test_full_independent_recomputation(self) -> None:
        report = load_checker().verify_certificate(CERTIFICATE)
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(report["checks_passed"], 100)

    def test_checked_report_binds_exact_certificate_bytes(self) -> None:
        report = json.loads(REPORT.read_text())
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["certificate_sha256"], hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest())
        self.assertGreaterEqual(report["checks_passed"], 115)
        self.assertIn("no import", report["independence"])

    def test_checker_is_nonimporting(self) -> None:
        source = CHECKER.read_text()
        tree = ast.parse(source)
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module)
        self.assertNotIn("c21_producer", imports)
        self.assertNotIn("c20_producer", imports)
        self.assertNotIn("c20_independent_check", imports)
        self.assertNotIn("henon_period7_dihedral_cover", imports)
        self.assertNotIn("henon_dihedral_chronology_obstruction", imports)

    def assert_tamper_fails(self, mutator, pattern: str) -> None:
        directory, path = mutated_path(mutator)
        try:
            with self.assertRaisesRegex(AssertionError, pattern):
                load_checker().verify_certificate(path)
        finally:
            directory.cleanup()

    def test_fail_closed_on_candidate_tamper(self) -> None:
        self.assert_tamper_fails(lambda d: d.__setitem__("candidate_id", "HCS-C21-tampered"), "candidate identity")

    def test_fail_closed_on_source_polynomial_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["period_six_source_polynomials"].__setitem__("f_r", d["period_six_source_polynomials"]["f_r"] + "+1"),
            "f_r exact string",
        )

    def test_fail_closed_on_ordered_cover_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["ordered_cover_geometry"]["matching_map"].__setitem__("m_r(x)", "x^2-A"),
            "matching formula",
        )

    def test_fail_closed_on_sheet_resultant_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["ordered_cover_geometry"]["valid_ordered_edge_model"].__setitem__(
                "sheet_separation_resultant", "0"
            ),
            "sheet separation certificate",
        )

    def test_fail_closed_on_branch_genus_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["ordered_cover_geometry"]["branch_and_genus"].__setitem__("genus_E6", 2),
            "ordered cover genus",
        )

    def test_fail_closed_on_tau_character_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["weight_one_cohomology"].__setitem__("tau_minimal_polynomial_on_H1", "T^2+T+1"),
            "tau minimal polynomial",
        )

    def test_fail_closed_on_fixed_field_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["weight_one_cohomology"]["fixed_field_ledger"].__setitem__(
                "conclusion", "Q(E6)^<tau>=Q(A,w)"
            ),
            "rotation fixed-field equality",
        )

    def test_fail_closed_on_shadow_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["cross_period_shadow"]["fiber_product"].__setitem__("factorization", "irreducible"),
            "fiber-product certificate",
        )

    def test_fail_closed_on_threshold_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["chronology_threshold"].__setitem__(
                "first_witnessed_nontrivial_weight_one_chronology_period_within_declared_component_scope",
                6,
            ),
            "scoped chronology threshold period",
        )

    def test_fail_closed_on_clock_averaging_tamper(self) -> None:
        self.assert_tamper_fails(
            lambda d: d["source_lock"]["clock_separation"].__setitem__("identified_or_averaged", True),
            "three clocks are not averaged",
        )

    def test_claim_boundaries(self) -> None:
        certificate = json.loads(CERTIFICATE.read_text())
        boundary = certificate["claim_boundary"]
        self.assertTrue(boundary["period6_ordered_cover_D6_genus1_proved"])
        self.assertTrue(boundary["period6_tau_H1_trivial_proved"])
        self.assertTrue(boundary["scoped_first_witnessed_threshold_through_n7_proved"])
        self.assertFalse(boundary["published_period6_scalar_formulas_claimed_new"])
        self.assertFalse(boundary["all_exact_period_components_classified"])
        self.assertFalse(boundary["period7_full_saturated_scheme_claimed"])
        self.assertFalse(boundary["primitive_cross_period_Hecke_bridge_claimed"])
        self.assertFalse(boundary["cross_period_Fredholm_determinant_claimed"])
        self.assertFalse(boundary["Riemann_divisor_claimed"])
        self.assertFalse(boundary["Hilbert_Polya_operator_claimed"])
        convention = certificate["ordered_cover_geometry"]["valid_ordered_edge_model"]
        self.assertIn("H_A^-1", convention["edge_coordinate_convention"])
        self.assertIn("conjugate by reversal rho", convention["comparison_to_c20_convention"])
        notation = certificate["source_lock"]["notation_separation"]
        self.assertNotEqual(notation["radical_in_prose"], notation["frobenius_degree_in_prose"])
        obstruction = certificate["cross_period_shadow"]["chronology_equivariant_morphism_obstruction"]
        self.assertIn("dominant nonconstant", obstruction["hypothesis"])
        self.assertIn("multivalued correspondences", obstruction["not_excluded"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
