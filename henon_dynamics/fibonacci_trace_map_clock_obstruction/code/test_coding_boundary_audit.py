import importlib.util
import sys
import unittest
from pathlib import Path

import sympy as sp


MODULE_PATH = Path(__file__).with_name("coding_boundary_audit.py")
SPEC = importlib.util.spec_from_file_location("coding_boundary_audit", MODULE_PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class CodingBoundaryAuditTests(unittest.TestCase):
    def test_marked_counts(self):
        certificate = AUDIT.build_certificate(15)
        self.assertEqual(certificate["marked_counts"]["values"][:8], [1, 2, 3, 5, 8, 13, 21, 34])

    def test_closed_and_boundary_divisors_differ(self):
        A, u, v = AUDIT.source_ten_state_data()
        z = sp.symbols("z")
        determinant = sp.factor((sp.eye(A.rows) - z * A).det())
        boundary = sp.factor((u * (sp.eye(A.rows) - z * A).inv() * v)[0])
        self.assertEqual(determinant.subs(z, -1), 0)
        self.assertEqual(sp.diff(determinant, z).subs(z, -1), 0)
        self.assertNotEqual(sp.diff(determinant, z, 2).subs(z, -1), 0)
        numerator, denominator = sp.fraction(sp.cancel(boundary))
        self.assertEqual(numerator.subs(z, -1), 0)
        self.assertNotEqual(sp.diff(numerator, z).subs(z, -1), 0)
        self.assertNotEqual(sp.expand(determinant), sp.expand(denominator))

    def test_six_state_quotient_intertwines_with_decorated_boundary(self):
        A10, u10, v10 = AUDIT.source_ten_state_data()
        A6, u6, v6, Q = AUDIT.quotient_six_state_data()
        self.assertEqual(A10 * Q, Q * A6)
        self.assertEqual(u10 * Q, u6)
        self.assertEqual(Q * v6, v10)


if __name__ == "__main__":
    unittest.main()
