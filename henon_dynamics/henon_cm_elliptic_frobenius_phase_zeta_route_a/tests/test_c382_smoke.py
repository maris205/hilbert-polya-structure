import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('independent_c382',ROOT/'code/c382_cm_checker.py')
checker=importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class Smoke(unittest.TestCase):
    def test_full_independent_ledger(self):
        self.assertGreater(checker.validate(ROOT/'results/c382_cm_evidence.json'),17000)
    def test_good_prime_and_phase_fixtures(self):
        d=checker.strict(ROOT/'results/c382_cm_evidence.json')
        self.assertEqual(d['prime_ledger'][0]['fixed_counts'][:4],[4,16,28,64])
        self.assertEqual(d['prime_ledger'][1]['primary_upper_pair'],[-1,2])
        self.assertEqual(d['prime_ledger'][1]['fixed_counts'][:3],[8,32,104])
    def test_optimized_execution_refused(self):
        for flag in ('-O','-OO'):
            r=subprocess.run([sys.executable,flag,'-B',str(ROOT/'code/c382_cm_checker.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('refuses optimized Python',r.stderr)

if __name__=='__main__':
    unittest.main()
