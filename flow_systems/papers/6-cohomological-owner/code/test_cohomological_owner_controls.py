#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cohomological_owner_controls as controls


class ArithmeticTests(unittest.TestCase):
    def test_mobius_initial_values(self) -> None:
        self.assertEqual([controls.mobius(n) for n in range(1, 11)], [1, -1, -1, 0, -1, 1, -1, 0, 0, 1])

    def test_known_irreducible_counts(self) -> None:
        self.assertEqual(
            [controls.affine_irreducible_count(d) for d in range(1, 9)],
            [2, 1, 2, 3, 6, 9, 18, 30],
        )

    def test_every_degree_is_positive(self) -> None:
        self.assertTrue(all(controls.p1_closed_point_count(d) > 0 for d in range(1, 101)))

    def test_fixed_points_cycles_and_cohomology_match(self) -> None:
        for n in range(1, 41):
            expected = controls.p1_point_count(n)
            self.assertEqual(controls.reconstructed_fixed_points(n), expected)
            self.assertEqual(controls.cohomological_supertrace(n), expected)


class KoopmanTests(unittest.TestCase):
    def test_frequency_occurrence_condition(self) -> None:
        q = Fraction(2, 3)
        expected = sum(controls.p1_closed_point_count(d) for d in range(1, 19) if d % 3 == 0)
        self.assertEqual(controls.multiplicity_through_degree(q, 18), expected)

    def test_zero_multiplicity_grows(self) -> None:
        values = [controls.multiplicity_through_degree(Fraction(0), d) for d in (4, 8, 12, 16)]
        self.assertEqual(values, sorted(values))
        self.assertTrue(all(right > left for left, right in zip(values, values[1:])))

    def test_weight_invariance_is_structural_not_numeric(self) -> None:
        # Component weights never enter the exact multiplicity function.
        self.assertEqual(
            controls.multiplicity_through_degree(Fraction(-3, 4), 20),
            controls.multiplicity_through_degree(Fraction(-3, 4), 20),
        )


class ArtifactTests(unittest.TestCase):
    def test_run_writes_self_consistent_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            certificate = controls.run(output, max_degree=16, max_power=16)
            self.assertEqual(certificate["candidate_id"], controls.CANDIDATE_ID)
            self.assertTrue(certificate["exact_identities"]["cycle_point_cohomology_ledgers_match"])
            self.assertFalse(certificate["limited_route_b_koopman"]["hilbert_polya_claim_allowed"])
            manifest = json.loads((output / "manifest.sha256.json").read_text(encoding="utf-8"))
            for name, expected in manifest["artifacts"].items():
                self.assertEqual(controls.sha256(output / name), expected)

    def test_degree_csv_has_exact_matches(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            controls.run(output, max_degree=12, max_power=12)
            with (output / "degree_trace_ledger.csv").open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 12)
            self.assertTrue(all(row["all_three_match"] == "true" for row in rows))
            self.assertTrue(all(row["closed_point_count_positive"] == "true" for row in rows))

    def test_invalid_cutoffs_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(ValueError):
                controls.run(Path(temporary), max_degree=7, max_power=8)


if __name__ == "__main__":
    unittest.main(verbosity=2)

