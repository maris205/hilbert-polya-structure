from __future__ import annotations

import json
import unittest
from pathlib import Path

import sympy as sp

import c48_pressure_labels as P48


class PressureLabelTests(unittest.TestCase):
    def test_exact_orbits_and_traces(self) -> None:
        orbits = P48.orbit_certificate()
        self.assertEqual(orbits["period_1"]["trace"], "2 + 2*sqrt(7)")
        self.assertEqual(orbits["period_3"]["trace"], "-42*sqrt(5) - 38")
        self.assertEqual(orbits["period_4"]["trace"], "578")
        for orbit in orbits.values():
            self.assertEqual(orbit["determinant"], "1")
            self.assertTrue(orbit["inside_abs_q_interval_1_3_to_5_8"])
            self.assertTrue(all(value == "0" for value in orbit["recurrence_residuals"]))

    def test_period_three_mutation_is_rejected(self) -> None:
        a = -sp.sqrt(5) / 6
        b = (1 + sp.sqrt(5)) / 6
        true_trace = sp.trace(P48.chronological_monodromy((a, b, a)))
        self.assertNotEqual(sp.simplify(true_trace), 38 + 42 * sp.sqrt(5))
        mutated = (a, b, -a)
        self.assertTrue(any(value != 0 for value in P48.recurrence_residuals(mutated)))

    def test_compositum_degree_and_duplicate_control(self) -> None:
        fields = P48.field_certificate()
        primitive = fields["primitive_element"]
        self.assertEqual(primitive["minimal_polynomial_degree"], 32)
        self.assertEqual(
            primitive["coefficient_sha256"],
            "d190eee1cc3f950d4d41efdadc0acedd9c628456d5a1dc6eba8708063c4188a0",
        )
        self.assertEqual(fields["pair_and_duplicate_controls"]["duplicate_L3_control"], 16)

    def test_ramification_sentinels(self) -> None:
        fields = P48.field_certificate()
        discriminants = fields["polynomial_discriminants"]
        self.assertNotIn("5", discriminants["f1"]["factorization"])
        self.assertNotIn("11", discriminants["f1"]["factorization"])
        self.assertNotIn("29", discriminants["f1"]["factorization"])
        self.assertNotIn("29", discriminants["f3"]["factorization"])
        self.assertEqual(fields["period_3_relative_discriminant"]["norm_factorization"]["11"], 1)

    def test_dependencies_and_committed_certificate(self) -> None:
        self.assertEqual(len(P48.dependency_locks()), 8)
        path = Path(__file__).resolve().parents[1] / "results" / "c48_certificate.json"
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), P48.build_certificate())


if __name__ == "__main__":
    unittest.main()
