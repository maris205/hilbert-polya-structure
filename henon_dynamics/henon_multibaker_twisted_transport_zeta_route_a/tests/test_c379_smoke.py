"""Small independent release smoke checks."""
if not __debug__:
    raise RuntimeError("c379 smoke refuses optimized Python")
import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class Smoke(unittest.TestCase):
    def test_boundary(self):
        x=json.loads((ROOT/"results/c379_multibaker_evidence.json").read_text())
        self.assertEqual(x["fixed_rows"][0]["geometric"],[])
        self.assertEqual(x["fixed_rows"][0]["symbolic"],[[-1,1],[1,1]])

    def test_parity(self):
        x=json.loads((ROOT/"results/c379_multibaker_evidence.json").read_text())
        self.assertFalse(x["diffusion"]["even_ring_uniform_mixing"])
        self.assertEqual(x["control_rows"][1]["untilted_period"],2)

    def test_independence(self):
        checker=(ROOT/"code/c379_multibaker_checker.py").read_text()
        self.assertNotIn("import c379_multibaker_producer",checker)
        self.assertNotIn("from c379_multibaker_producer",checker)

if __name__=="__main__":unittest.main()
