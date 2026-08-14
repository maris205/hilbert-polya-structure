from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DynatomicGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads((ROOT / "results" / "c60_certificate.json").read_text())
        cls.independent = json.loads((ROOT / "results" / "c60_independent_check.json").read_text())

    def test_candidate(self) -> None:
        self.assertTrue(self.certificate["check"])
        self.assertEqual(self.certificate["candidate_id"], "HCS-P60")

    def test_degrees(self) -> None:
        self.assertEqual(
            [row["quotient_degree"] for row in self.certificate["finite_exact_rows"]],
            [2, 2, 6, 14, 28, 62, 126, 246],
        )

    def test_finite_exactness(self) -> None:
        for row in self.certificate["finite_exact_rows"]:
            self.assertTrue(row["closure_squarefree"])
            self.assertTrue(row["quotient_irreducible_over_Q"])

    def test_p58_crosslock(self) -> None:
        self.assertEqual(
            self.certificate["p58_period9_quotient_match"],
            "b0e55d474c54eba2a0bd8b8e742a11ebfae94380bf4c6c4d5253c7d89cbef9dd",
        )

    def test_entropy_boundary(self) -> None:
        entropy = self.certificate["entropy_comparison"]
        self.assertEqual(entropy["strict_gap"], "(1/2)log(2/phi)>0")
        self.assertEqual(
            self.certificate["claim_status"]["all_period_effective_dynatomic_root_count"],
            "OPEN",
        )

    def test_independent(self) -> None:
        self.assertTrue(self.independent["check"])
        self.assertEqual(self.independent["degree_sequence"], [2, 2, 6, 14, 28, 62, 126, 246])

    def test_mutations(self) -> None:
        audit = self.certificate["mutation_audit"]
        self.assertEqual(audit["attempted"], 20)
        self.assertEqual(audit["rejected"], 20)

    def test_route_scope(self) -> None:
        self.assertFalse(self.certificate["route_a_status"]["full_arithmetic_candidate_pass"])
        self.assertFalse(self.certificate["route_b_authorized"])


if __name__ == "__main__":
    unittest.main()
