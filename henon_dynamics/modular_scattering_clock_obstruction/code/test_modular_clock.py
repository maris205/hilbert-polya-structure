#!/usr/bin/env python3
"""Unit tests for the independent HCS-C17 result checker."""

from __future__ import annotations

import ast
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import mpmath as mp

import independent_check as checker


PROJECT = Path(__file__).resolve().parent.parent
RESULTS = PROJECT / "results"


class IndependentArithmeticTests(unittest.TestCase):
    def test_matrix_inverse_power_and_conjugacy(self) -> None:
        matrix = checker.Matrix2(2, 1, 3, 2)
        self.assertEqual(matrix.determinant(), 1)
        self.assertEqual(matrix.multiply(matrix.inverse()), checker.IDENTITY)
        self.assertEqual(matrix.power(2), checker.Matrix2(7, 4, 12, 7))
        conjugate = checker.INVERSION.inverse().multiply(matrix).multiply(checker.INVERSION)
        self.assertEqual(conjugate.trace(), matrix.trace())
        self.assertNotEqual(abs(conjugate.x10), abs(matrix.x10))

    def test_totient_uses_independent_arithmetic(self) -> None:
        expected = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4]
        self.assertEqual([checker.totient(n) for n in range(1, 13)], expected)
        self.assertEqual(checker.totient_table(12)[1:], expected)

    def test_gauss_cyclic_witness(self) -> None:
        base = checker.gauss_product((1, 1, 1, 2))
        shifted = checker.gauss_product((1, 2, 1, 1))
        prefix = checker.gauss_product((1, 1))
        self.assertEqual(prefix.inverse().multiply(base).multiply(prefix), shifted)
        self.assertEqual(base.trace(), shifted.trace())
        self.assertNotEqual(abs(base.x10), abs(shifted.x10))

    def test_scattering_functional_equation(self) -> None:
        old_precision = mp.mp.dps
        try:
            mp.mp.dps = 70
            s = mp.mpc(mp.mpf("0.5"), mp.mpf("2"))
            coefficient = checker.scattering(s)
            self.assertLess(abs(abs(coefficient) - 1), mp.mpf("1e-60"))
            self.assertLess(abs(coefficient * checker.scattering(1 - s) - 1), mp.mpf("1e-60"))
        finally:
            mp.mp.dps = old_precision


class ResultVerificationTests(unittest.TestCase):
    def test_checker_has_no_producer_import(self) -> None:
        source = (Path(__file__).resolve().parent / "independent_check.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module)
        self.assertNotIn("modular_clock", imported)

    def test_committed_results_pass_full_independent_check(self) -> None:
        report = checker.verify_results(RESULTS)
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(report["independent_of_producer_import"])
        self.assertEqual(
            report["verified_rows"],
            {
                "rigidity_family": 400,
                "chebyshev": 48,
                "double_coset": 80,
                "gauss_word": 274,
                "homogenization": 96,
                "dirichlet": 12,
            },
        )

    def test_tampered_result_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "results"
            shutil.copytree(RESULTS, copied)
            certificate_path = copied / "exact_certificates.json"
            certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
            certificate["conjugacy_witness"]["absolute_c_pair"][0] += 1
            certificate_path.write_text(json.dumps(certificate), encoding="utf-8")
            with self.assertRaisesRegex(checker.VerificationError, "conjugacy c pair mismatch"):
                checker.verify_results(copied)


if __name__ == "__main__":
    unittest.main()
