"""Three small independent source/evidence smoke checks."""
import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("check388",ROOT/"code/c388_algebraic_checker.py")
check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)
class Smoke(unittest.TestCase):
    def test_index_three(self):
        A=check.expected_matrix(3,1,1)
        self.assertEqual(A,[[1,1,1]]*3)
        self.assertEqual(check.charpoly(A),[1,-3,0,0])
    def test_strict_evaluation(self):
        self.assertIs(check.evaluation()["route_b_invocation_allowed"],False)
    def test_full_certificates(self):
        self.assertEqual(check.verify(check.load(ROOT/"results/c388_algebraic_evidence.json"))["lattice_count"],142)
if __name__=="__main__":unittest.main()
