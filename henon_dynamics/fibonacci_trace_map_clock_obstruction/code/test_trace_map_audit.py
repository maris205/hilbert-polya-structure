import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

import sympy as sp


MODULE_PATH = Path(__file__).with_name("trace_map_audit.py")
SPEC = importlib.util.spec_from_file_location("trace_map_audit", MODULE_PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class TraceMapAuditTests(unittest.TestCase):
    def test_chronological_products_match_trace_recurrence(self):
        result = AUDIT.verify_chronological_products(5)
        self.assertTrue(all(row["verified"] for row in result["checks"]))

    def test_first_band_edge_escapes(self):
        sequence = AUDIT.half_trace_sequence(0, 1, 9)
        self.assertEqual(sequence[1], Fraction(-1))
        self.assertEqual(sequence[5], Fraction(5))
        end, triple = AUDIT.first_escape_triple(sequence)
        self.assertEqual(end, 5)
        self.assertEqual(triple, (Fraction(3, 2), Fraction(2), Fraction(5)))

    def test_first_discriminant_zero_escapes(self):
        sequence = AUDIT.half_trace_sequence(-1, 1, 9)
        self.assertEqual(sequence[1], Fraction(0))
        end, triple = AUDIT.first_escape_triple(sequence)
        self.assertEqual(end, 7)
        self.assertEqual(triple, (Fraction(3, 2), Fraction(2), Fraction(5)))

    def test_all_registered_gcd_gates(self):
        rows = AUDIT.modular_gcd_audit(max_k=8, prime=AUDIT.PRIME)
        self.assertEqual(len(rows), 8 * 3 * 2)
        self.assertTrue(all(row["simultaneous_gcd_degree_mod_p"] == 0 for row in rows))

    def test_degrees_are_physical_word_lengths(self):
        E, d = AUDIT.trace_polynomials(8, 1)
        lengths = AUDIT.word_lengths(8)
        for k in range(-1, 9):
            self.assertEqual(sp.degree(d[k], E), lengths[k])


if __name__ == "__main__":
    unittest.main()

