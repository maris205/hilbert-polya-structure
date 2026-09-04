"""Minimal executable contract for HCS-C378."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C378Smoke(unittest.TestCase):
    def test_producer_is_byte_stable(self):
        with tempfile.TemporaryDirectory(prefix="c378-test-") as directory:
            output = Path(directory) / "evidence.json"
            subprocess.run(
                [sys.executable, "-B", str(ROOT / "code/c378_dyson_ou_producer.py"), "--output", str(output)],
                check=True, capture_output=True, text=True,
            )
            self.assertEqual(output.read_bytes(), (ROOT / "results/c378_dyson_ou_evidence.json").read_bytes())

    def test_independent_checker(self):
        subprocess.run(
            [sys.executable, "-B", str(ROOT / "code/c378_dyson_ou_checker.py")],
            check=True, capture_output=True, text=True,
        )

    def test_optimized_mode_refusal(self):
        for name in ("c378_dyson_ou_producer.py", "c378_dyson_ou_checker.py"):
            process = subprocess.run(
                [sys.executable, "-O", str(ROOT / "code" / name), "--help"],
                capture_output=True, text=True,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertIn("refuses optimized Python", process.stdout + process.stderr)


if __name__ == "__main__":
    unittest.main()
