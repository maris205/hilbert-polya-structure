"""Three small smoke tests; not a replacement for complete release lanes."""
import importlib.util
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module():
    spec=importlib.util.spec_from_file_location("c391_check",ROOT/"code/c391_checker.py")
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
class Smoke(unittest.TestCase):
    def test_yaml(self):self.assertEqual(module().check_yaml()["candidate_id"],"HCS-C391")
    def test_evidence(self):self.assertEqual(len(module().check(ROOT/"results/c391_evidence.json")),64)
    def test_boolean_is_not_rational(self):
        with self.assertRaises(AssertionError):module().rational([True,1])
if __name__=="__main__":unittest.main()
