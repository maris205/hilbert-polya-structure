"""Small externally invoked lanes; no producer imports."""
import pathlib
import subprocess
import sys
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Smoke(unittest.TestCase):
    def test_exact_checker(self):
        r=subprocess.run([sys.executable,"-B",str(ROOT/"code/c395_bcz_checker.py")],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
    def test_evaluation(self):
        r=subprocess.run([sys.executable,"-B",str(ROOT/"code/c395_bcz_checker.py"),"--evaluation-only"],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
    def test_optimized_refusal(self):
        for p in sorted((ROOT/"code").glob("c395_*.py")):
            for flag in ("-O","-OO"):
                r=subprocess.run([sys.executable,flag,str(p),"--help"],capture_output=True,text=True)
                self.assertNotEqual(r.returncode,0)
                self.assertIn("refuses optimized Python",r.stdout+r.stderr)
if __name__=="__main__":unittest.main()
