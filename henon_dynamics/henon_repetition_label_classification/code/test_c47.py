from __future__ import annotations

import json
import unittest
from pathlib import Path

import c47_label_classifier as C47


class LabelClassifierTests(unittest.TestCase):
    def test_monomials_and_constants(self) -> None:
        for exponent in range(-8, 9):
            self.assertTrue(C47.satisfies_square_law({exponent: 1}))
        self.assertTrue(C47.satisfies_square_law({}))
        self.assertFalse(C47.satisfies_square_law({0: -1}))

    def test_trace_and_fixed_determinant_fail(self) -> None:
        self.assertFalse(C47.satisfies_square_law({-1: 1, 1: 1}))
        self.assertFalse(C47.satisfies_square_law({-1: -1, 0: 2, 1: -1}))

    def test_finite_adversarial_scan(self) -> None:
        scan = C47.laurent_scan(3)
        self.assertEqual(scan["tested"], 3**7)
        self.assertEqual(scan["solution_count"], 8)

    def test_committed_certificate(self) -> None:
        path = Path(__file__).resolve().parents[1] / "results" / "c47_certificate.json"
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), C47.build_certificate())


if __name__ == "__main__":
    unittest.main()
