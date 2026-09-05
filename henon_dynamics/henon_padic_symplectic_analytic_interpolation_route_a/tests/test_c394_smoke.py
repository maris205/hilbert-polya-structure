"""Three bounded positive-path smoke tests, not mathematical proofs."""
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"code"))
from c394_interpolation_checker import check, evaluation, EVAL

class Smoke(unittest.TestCase):
    def test_payload(self):
        result = check(ROOT/"results/c394_interpolation_evidence.json")
        self.assertEqual(result["residue_points"], 109876)

    def test_scope(self):
        data = evaluation(EVAL)
        self.assertTrue(all(v is False for v in data["scope_flags"].values()))
        self.assertIs(data["route_b_invocation_allowed"], False)

    def test_finite_not_genuine(self):
        import json
        data = json.loads((ROOT/"results/c394_interpolation_evidence.json").read_text())
        self.assertEqual(data["controls"]["genuine_periodic_points"], [[0, 0]])
        self.assertTrue(any(any(L > 1 for L, _ in row["cycle_histogram"]) for row in data["finite_levels"]))

if __name__ == "__main__":
    unittest.main()
