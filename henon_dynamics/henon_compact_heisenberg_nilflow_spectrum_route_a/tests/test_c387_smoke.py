import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('independent_nilflow_checker',ROOT/'code/c387_nilflow_checker.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)

class Smoke(unittest.TestCase):
    def test_evidence(self):
        self.assertGreater(checker.check(ROOT/'results/c387_nilflow_evidence.json'),10000)
    def test_no_producer_import(self):
        self.assertNotIn('import c387_nilflow_producer',(ROOT/'code/c387_nilflow_checker.py').read_text())
    def test_frozen_boundary(self):
        d=checker.load(ROOT/'results/c387_nilflow_evidence.json')['payload']
        self.assertEqual(d['route_tuple'],['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FORMAL_HINT'])
        self.assertTrue(all(v is False for v in d['scope_flags'].values()))
        self.assertIs(d['global_theorem']['time_one_map_ergodic'],False)

if __name__=='__main__':unittest.main()
