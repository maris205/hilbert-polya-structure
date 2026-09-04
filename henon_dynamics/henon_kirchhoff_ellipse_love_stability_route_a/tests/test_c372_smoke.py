from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C372SmokeTests(unittest.TestCase):
    def test_evidence_payload_hash(self):
        value = json.loads((ROOT / "results/c372_kirchhoff_love_evidence.json").read_text())
        claimed = value.pop("payload_sha256")
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(claimed, hashlib.sha256(raw).hexdigest())

    def test_independent_checker(self):
        output = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c372_kirchhoff_love_checker.py")], text=True)
        self.assertIn("C372 independent checker: PASS", output)

    def test_sympy_crosscheck(self):
        output = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c372_kirchhoff_love_sympy_crosscheck.py")], text=True)
        self.assertIn("C372 SymPy cross-check: PASS", output)


if __name__ == "__main__":
    unittest.main()
