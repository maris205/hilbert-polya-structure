import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]

class Smoke(unittest.TestCase):
    def test_independent_evidence(self):
        p=subprocess.run([sys.executable,'-B',str(ROOT/'code/c384_wild_checker.py')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr);self.assertIn('PASS',p.stdout)

    def test_pure_powers(self):
        x=json.loads((ROOT/'results/c384_wild_evidence.json').read_text())['payload']
        for row in x['period_rows']:
            if row['valuation_power']==row['n']:
                self.assertEqual(row['geometric'],1)
                self.assertEqual(row['primitive_cycles'],int(row['n']==1))

    def test_optimized_refusal(self):
        p=subprocess.run([sys.executable,'-O','-B',str(ROOT/'code/c384_wild_checker.py')],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertIn('refuses optimized Python',p.stderr)

if __name__=='__main__':unittest.main()
