from __future__ import annotations

import json
import unittest
from pathlib import Path

import c46_integral_monodromy as C46


class IntegralMonodromyTests(unittest.TestCase):
    def test_exceptional_low_period_relations(self) -> None:
        self.assertEqual(str(C46.cyclic_relations(C46.sp.symbols("x0:1"))[0]), "x0**2 + 2*x0 - 6")
        self.assertEqual(len(C46.cyclic_relations(C46.sp.symbols("x0:2"))), 2)

    def test_first_trace_polynomials(self) -> None:
        self.assertEqual(C46.period_record(1)["trace_reduced"], "-2*x0")
        self.assertEqual(C46.period_record(2)["trace_reduced"], "4*x0*x1 - 2")
        self.assertEqual(C46.period_record(3)["trace_reduced"], "-8*x0*x1*x2 + 2*x0 + 2*x1 + 2*x2")

    def test_fixed_multiplier_polynomial(self) -> None:
        self.assertEqual(C46.fixed_multiplier_polynomial().all_coeffs(), [1, -4, -22, -4, 1])

    def test_committed_certificate(self) -> None:
        path = Path(__file__).resolve().parents[1] / "results" / "c46_certificate.json"
        committed = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(committed, C46.build_certificate(len(committed["finite_rows"])))


if __name__ == "__main__":
    unittest.main()
