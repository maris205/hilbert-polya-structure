from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C370SmokeTests(unittest.TestCase):
    def test_evidence_self_hash_and_scale(self):
        path = ROOT / "results/c370_brieskorn_reeb_evidence.json"
        value = json.loads(path.read_text())
        grid = value["finite_grid"]
        self.assertEqual(grid["pair_count"], 1003)
        self.assertEqual(grid["fixed_time_cell_count"], 5_469_178)
        self.assertEqual(grid["orbit_type_row_count"], 4_012)
        self.assertEqual(grid["rotation_row_count"], 3_009)
        self.assertEqual(grid["nondegenerate_cz_cell_count"], 103_749)
        claimed = value.pop("payload_sha256")
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(claimed, hashlib.sha256(raw).hexdigest())

    def test_independent_checker(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c370_brieskorn_reeb_checker.py")], text=True
        )
        self.assertIn("C370 checker PASS", output)

    def test_sympy_lane(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c370_brieskorn_reeb_sympy_crosscheck.py")], text=True
        )
        self.assertIn("C370 SymPy PASS", output)


if __name__ == "__main__":
    unittest.main()
