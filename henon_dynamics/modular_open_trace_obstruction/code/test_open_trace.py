#!/usr/bin/env python3
"""Regression and tamper tests for the HCS-C18 computation package."""

from __future__ import annotations

import ast
import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import mpmath as mp

import independent_check as checker


PROJECT = Path(__file__).resolve().parent.parent
RESULTS = PROJECT / "results"


class IndependentMathematicsTests(unittest.TestCase):
    def test_factorization_totient_and_root_formula(self) -> None:
        brute_phi = lambda q: sum(__import__("math").gcd(x, q) == 1 for x in range(1, q + 1))
        brute_roots = lambda q: sum((x * x + 1) % q == 0 for x in range(q))
        for q in range(1, 101):
            self.assertEqual(checker.independent_phi(q), brute_phi(q))
            self.assertEqual(checker.independent_sqrt_minus_one_count(q), brute_roots(q))

    def test_endpoint_primitive_and_affine_sections(self) -> None:
        matrix = checker.ZMat(1, 2, 2, 5)
        numerator, denominator, sign, ratio = checker.endpoint_image(matrix, -3, 5)
        self.assertEqual((numerator, denominator), (7, 19))
        self.assertEqual(abs(sign), 1)
        self.assertEqual(ratio, __import__("fractions").Fraction(19, 5))

    def test_local_block_functional_equation(self) -> None:
        old_precision = mp.mp.dps
        try:
            mp.mp.dps = 80
            s = mp.mpc(mp.mpf("0.5"), mp.mpf("1.3"))
            for prime in (2, 3, 5, 7):
                product = checker.p_block(prime, s) * checker.p_block(prime, 1 - s)
                self.assertLess(checker.maxnorm(product - mp.eye(2)), mp.mpf("1e-70"))
                plus = checker.p_channel(prime, False, s)
                minus = checker.p_channel(prime, True, s)
                walsh = mp.matrix([[1, 1], [1, -1]]) / mp.sqrt(2)
                self.assertLess(
                    checker.maxnorm(walsh.T * checker.p_block(prime, s) * walsh - checker.diag([plus, minus])),
                    mp.mpf("1e-70"),
                )
        finally:
            mp.mp.dps = old_precision


class ArtifactVerificationTests(unittest.TestCase):
    def test_checker_does_not_import_producer(self) -> None:
        source_path = Path(__file__).resolve().parent / "independent_check.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        imports: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        self.assertNotIn("open_trace", imports)

    def test_committed_results_pass(self) -> None:
        report = checker.verify_results(RESULTS)
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(report["independent_of_producer_import"])
        self.assertTrue(report["projector_paths_outside_bare_product_no_go"])
        self.assertEqual(
            report["verified_counts"],
            {
                "arithmetic_rows": 2000,
                "open_series_rows": 12,
                "endpoint_rows": 30,
                "double_coset_witnesses": 3,
                "squarefree_levels": 4,
            },
        )

    def test_extra_summary_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "results"
            shutil.copytree(RESULTS, copied)
            path = copied / "summary.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["unregistered_field"] = True
            path.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(checker.CheckFailure, "schema mismatch"):
                checker.verify_results(copied)

    def test_tampered_arithmetic_row_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "results"
            shutil.copytree(RESULTS, copied)
            path = copied / "arithmetic_counts.csv"
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
                fields = list(rows[0])
            rows[4]["sqrt_minus_one_count"] = "0"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(checker.CheckFailure, "root count mismatch"):
                checker.verify_results(copied)

    def test_tampered_projector_amplitude_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "results"
            shutil.copytree(RESULTS, copied)
            path = copied / "scattering_checks.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["projector_resolved_paths"]["baseline"]["amplitude"]["real"] = "0.0"
            path.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(checker.CheckFailure, "baseline amplitude"):
                checker.verify_results(copied)


if __name__ == "__main__":
    unittest.main()
