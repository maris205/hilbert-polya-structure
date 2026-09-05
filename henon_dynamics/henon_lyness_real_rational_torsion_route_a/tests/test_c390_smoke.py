import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("independent_checker",ROOT/"code/c390_lyness_checker.py")
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class Smoke(unittest.TestCase):
    def test_full_certificate(self):self.assertEqual(checker.verify(checker.load(ROOT/"results/c390_lyness_evidence.json"))["sufficient_period_witnesses"],690)
    def test_strict_evaluation(self):self.assertEqual(checker.evaluation()["overall_verdict"],"ROUTE_A_REJECTED")
    def test_false_is_not_zero(self):
        with self.assertRaises(AssertionError):checker.rat([False,1])
if __name__=="__main__":unittest.main()
