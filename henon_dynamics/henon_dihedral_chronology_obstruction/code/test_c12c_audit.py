import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("c12c_audit.py")
SPEC = importlib.util.spec_from_file_location("c12c_audit", MODULE_PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class C12CAuditTests(unittest.TestCase):
    def test_low_period_counts(self):
        expected = {
            1: (2, 0, 2),
            2: (1, 0, 1),
            3: (2, 0, 2),
            4: (3, 0, 3),
            5: (6, 0, 6),
            6: (9, 1, 8),
            7: (18, 2, 16),
            8: (30, 6, 24),
        }
        for n, (cyclic, doublets, dihedral) in expected.items():
            row = AUDIT.orbit_count(n)
            self.assertEqual(row.cyclic_orbits, cyclic)
            self.assertEqual(row.chiral_doublets, doublets)
            self.assertEqual(row.dihedral_orbits, dihedral)

    def test_partition_and_burnside_integrality_to_100(self):
        for n in range(1, 101):
            row = AUDIT.orbit_count(n)
            self.assertEqual(
                row.cyclic_orbits,
                row.diagonal_orbits
                + row.nondiagonal_orbits
                + row.chiral_cyclic_orbits,
            )
            self.assertEqual(
                row.dihedral_orbits,
                row.diagonal_orbits
                + row.nondiagonal_orbits
                + row.chiral_doublets,
            )

    def test_period_six_normalizations_are_rational(self):
        cert = AUDIT.period_six_certificate()
        self.assertEqual(cert["component_genera"], {"C6": 0, "D6": 0, "N6_normalization": 0})
        self.assertIn("(sigma - 6)*(sigma + 2)", cert["squarefree_double_cover"])

    def test_period_fourteen_typo(self):
        row = AUDIT.orbit_count(14)
        self.assertEqual(row.cyclic_orbits, 1161)
        self.assertEqual(row.diagonal_orbits, 56)
        self.assertEqual(row.nondiagonal_orbits, 119)
        self.assertEqual(row.chiral_doublets, 493)
        self.assertEqual(2 * 493 + 56 + 119, 1161)


if __name__ == "__main__":
    unittest.main()
