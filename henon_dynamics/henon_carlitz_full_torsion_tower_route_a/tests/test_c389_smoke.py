"""Small independent checker regression and schema smoke tests."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',ROOT/'code/c389_carlitz_checker.py')
C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
class Smoke(unittest.TestCase):
    def test_clean(self): self.assertEqual(C.check(ROOT/'results/c389_carlitz_evidence.json')['status'],'PASS')
    def test_bool_int(self):
        with self.assertRaises(ValueError): C.same({'x':True},{'x':1})
    def test_unknown(self):
        with self.assertRaises(ValueError): C.same({'x':1,'y':0},{'x':1})
if __name__=='__main__': unittest.main()
