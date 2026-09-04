from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C375SmokeTests(unittest.TestCase):
    def test_evidence_self_hash_and_scope(self):
        path = ROOT / "results/c375_lps_nonbacktracking_evidence.json"
        value = json.loads(path.read_text())
        claimed = value.pop("payload_sha256")
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        self.assertEqual(claimed, hashlib.sha256(raw).hexdigest())
        self.assertFalse(any(value["scope_flags"].values()))
        self.assertEqual(value["total_vertices"], 104316)

    def test_independent_checker(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c375_lps_nonbacktracking_checker.py")], text=True
        )
        self.assertIn("C375 independent checker: PASS", output)

    def test_sympy_lane(self):
        output = subprocess.check_output(
            [sys.executable, "-B", str(ROOT / "code/c375_lps_nonbacktracking_sympy_crosscheck.py")], text=True
        )
        self.assertIn("C375 SymPy cross-check: PASS", output)


if __name__ == "__main__":
    unittest.main()
