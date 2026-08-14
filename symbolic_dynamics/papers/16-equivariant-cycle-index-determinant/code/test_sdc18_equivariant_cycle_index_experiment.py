from __future__ import annotations

import csv
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import sdc18_equivariant_cycle_index_experiment as audit  # noqa: E402


class CombinatorialLedgerTests(unittest.TestCase):
    def test_squarefree_counts(self):
        expected = {2: 2, 3: 6, 4: 26, 5: 150, 6: 1082, 7: 9366}
        actual = {n: len(audit.squarefree_cyclic_words(n)) for n in expected}
        self.assertEqual(actual, expected)

    def test_squarefree_words_are_primitive(self):
        for n in range(2, 8):
            for word in audit.squarefree_cyclic_words(n):
                self.assertEqual(audit.minimal_period(word), len(word))

    def test_squarefree_scalar_virtual_dimension_zero(self):
        for n in range(2, 8):
            words = audit.squarefree_cyclic_words(n)
            virtual_dimension = sum(audit.word_sign(n, word) for word in words)
            self.assertEqual(virtual_dimension, 0)

    def test_s3_residual_character(self):
        certificate = audit.s3_certificate()
        self.assertTrue(certificate["pass"])
        self.assertEqual(certificate["virtual_character"], [0, 0, 3])
        self.assertEqual(
            certificate["decomposition"],
            {"trivial": 1, "sign": 1, "standard": -1},
        )

    def test_s3_burnside_marks(self):
        marks = audit.s3_certificate()["subgroup_marks"]
        self.assertEqual(marks["trivial"]["virtual_mark"], 0)
        self.assertEqual(marks["C2"]["virtual_mark"], 0)
        self.assertEqual(marks["C3"]["virtual_mark"], 3)
        self.assertEqual(marks["S3"]["virtual_mark"], 1)


class PowerFirewallTests(unittest.TestCase):
    def test_rank_one_and_adams_witnesses(self):
        for n in range(2, 9):
            for power in range(2, 9):
                target = (power - 1, 1) + (0,) * (n - 2)
                self.assertEqual(audit.coefficient_of_b_power(n, power, target), power)
                self.assertEqual(audit.coefficient_of_adams_b(n, power, target), 0)

    def test_squarefree_degree_has_no_higher_adams_preimage(self):
        certificate = audit.projective_and_c2_certificate()
        self.assertTrue(certificate["all_adams_squarefree_pass"])

    def test_projective_zero_specialization(self):
        certificate = audit.projective_and_c2_certificate()
        self.assertTrue(certificate["all_zero_specialization_pass"])

    def test_c2_sign_power_consistency_and_naive_failure(self):
        certificate = audit.projective_and_c2_certificate()
        self.assertTrue(certificate["all_c2_sign_power_pass"])
        self.assertGreater(certificate["naive_integer_adams_mismatch_count"], 0)


class OperatorNoGoTests(unittest.TestCase):
    def test_distinct_and_equal_stabilizers(self):
        rows = audit.stabilizer_rows()
        self.assertTrue(all(row["pass"] for row in rows))
        for row in rows:
            if row["specialization"].startswith("distinct"):
                self.assertEqual(row["stabilizer_order"], 1)
            else:
                self.assertEqual(row["stabilizer_order"], row["expected_order"])

    def test_rank_one_nontrivial_determinants(self):
        rows = audit.rank_one_rows()
        self.assertTrue(all(row["pass"] for row in rows))
        self.assertTrue(all(row["nontrivial_isotypic_eigenvalue"] == "0" for row in rows))
        self.assertTrue(all(row["nontrivial_sector_determinant"] == "1" for row in rows))

    def test_diagonal_n2_certificate(self):
        x = Fraction(1, 4)
        y = Fraction(1, 9)
        target = (1 - x) * (1 - y)
        diagonal = audit.diagonal_superdet((x, y))
        self.assertEqual(target, Fraction(2, 3))
        self.assertEqual(diagonal, Fraction(24, 35))
        self.assertNotEqual(target, diagonal)

    def test_all_diagonal_prime_controls_mismatch(self):
        rows = audit.diagonal_rows()
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(row["pass"] for row in rows))
        self.assertTrue(all(row["diagonal_coefficient_x1x2"] == 2 for row in rows))

    def test_schatten_theorem_labels(self):
        rows = audit.schatten_rows()
        self.assertEqual(len(rows), 2 * 5 * 4 * 4)
        for row in rows:
            exponent = float(row["q_sigma"])
            self.assertEqual(row["theorem_Sq_membership"], exponent > 1.0)

    def test_all_inventory_controls(self):
        rows = audit.control_rows()
        self.assertEqual(len(rows), 7 + 16 * 7 * 4)
        self.assertTrue(
            all(
                row["scalar_identity_pass"]
                and row["distinct_stabilizer_pass"]
                and row["mixed_factor_pass"]
                for row in rows
            )
        )


class FrozenArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        summary_path = ROOT / "results" / "summary.json"
        if not summary_path.exists():
            subprocess.run([sys.executable, str(ROOT / "code" / "sdc18_equivariant_cycle_index_experiment.py")], check=True)

    def test_summary_has_no_zero_data_and_all_checks_pass(self):
        summary = json.loads((ROOT / "results" / "summary.json").read_text(encoding="utf-8"))
        self.assertFalse(summary["zero_data_used"])
        self.assertTrue(summary["all_exact_checks_pass"])
        self.assertEqual(summary["exact_check_count"], 12)

    def test_result_tables_are_nonempty(self):
        expected = (
            "sn_character_table.csv",
            "burnside_cyclic_marks.csv",
            "orbit_decomposition.csv",
            "ghost_power_audit.csv",
            "rank_one_audit.csv",
            "stabilizer_audit.csv",
            "diagonal_superdet_audit.csv",
            "schatten_cutoffs.csv",
            "control_audit.csv",
        )
        for name in expected:
            path = ROOT / "results" / name
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertGreater(len(rows), 0, name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
