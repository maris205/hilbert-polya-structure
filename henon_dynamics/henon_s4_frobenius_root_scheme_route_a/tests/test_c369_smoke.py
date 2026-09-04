from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C369SmokeTests(unittest.TestCase):
    def test_evidence_self_hash(self):
        path = ROOT / "results/c369_s4_frobenius_evidence.json"
        value = json.loads(path.read_text())
        claimed = value.pop("payload_sha256")
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(claimed, hashlib.sha256(raw).hexdigest())

    def test_independent_checker(self):
        output = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c369_s4_frobenius_checker.py")], text=True)
        self.assertIn("C369 independent checker: PASS", output)

    def test_sympy_lane(self):
        output = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c369_s4_frobenius_sympy_crosscheck.py")], text=True)
        self.assertIn("C369 SymPy cross-check: PASS", output)


if __name__ == "__main__":
    unittest.main()
