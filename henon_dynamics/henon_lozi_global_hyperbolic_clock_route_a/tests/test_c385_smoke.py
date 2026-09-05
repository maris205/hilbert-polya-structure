"""Three focused checks, separate from the full cyclic-system checker."""
if not __debug__:
    raise RuntimeError("c385 smoke refuses optimized Python")
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Smoke(unittest.TestCase):
    def test_period_one(self):
        d=json.loads((ROOT/"results/c385_lozi_evidence.json").read_text())
        for row in d["rows"]:
            if row["n"]==1:
                a=F(*row["a"]);x=F(*row["x_cycle"][0]);s=2*int(row["word"])-1
                self.assertEqual(x,1/(2+a*s))
    def test_signed_stability(self):
        d=json.loads((ROOT/"results/c385_lozi_evidence.json").read_text())
        self.assertEqual({r["unstable_sign"] for r in d["rows"]},{-1,1})
        self.assertEqual(len(d["primitive_rows"]),123)
    def test_checker_independence(self):
        code=(ROOT/"code/c385_lozi_checker.py").read_text()
        self.assertNotIn("import c385_lozi_producer",code)
        self.assertNotIn("from c385_lozi_producer",code)
        self.assertIn("linear_solve",code)
if __name__=="__main__":unittest.main()
