"""Boundary and proof/evidence separation smoke tests."""
if not __debug__:
    raise RuntimeError("c381 smoke refuses optimized Python")
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Smoke(unittest.TestCase):
    def test_neutral(self):
        x=json.loads((ROOT/"results/c381_lsv_evidence.json").read_text())
        self.assertTrue(x["periodic_rows"][0]["neutral"])
        self.assertEqual(x["periodic_rows"][0]["multiplier_bounds"],[2**80,2**80])
    def test_clocks(self):
        x=json.loads((ROOT/"results/c381_lsv_evidence.json").read_text())
        self.assertEqual(x["induced_rows"][1]["return_period"],1)
        self.assertEqual(x["induced_rows"][1]["original_time"],2)
        self.assertFalse(x["trace_head_rows"][0]["infinite_trace_claim"])
    def test_independence(self):
        text=(ROOT/"code/c381_lsv_checker.py").read_text()
        self.assertNotIn("import c381_lsv_producer",text)
        self.assertNotIn("from c381_lsv_producer",text)
if __name__=="__main__":unittest.main()
