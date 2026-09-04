from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C373SmokeTests(unittest.TestCase):
    def test_evidence_hash_and_scale(self):
        value = json.loads((ROOT / "results/c373_higgs_oscillator_evidence.json").read_text())
        grid = value["finite_grid"]
        self.assertEqual(grid["classical_cell_count"], 2048)
        self.assertEqual(grid["quantum_state_label_count"], 8385)
        self.assertEqual(grid["total_revival_case_count"], 512)
        claimed = value.pop("payload_sha256")
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(claimed, hashlib.sha256(raw).hexdigest())

    def test_independent_checker(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c373_higgs_oscillator_checker.py")], text=True
        )
        self.assertIn("C373 checker PASS", output)

    def test_sympy_lane(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c373_higgs_oscillator_sympy_crosscheck.py")], text=True
        )
        self.assertIn("C373 SymPy PASS", output)


if __name__ == "__main__":
    unittest.main()
