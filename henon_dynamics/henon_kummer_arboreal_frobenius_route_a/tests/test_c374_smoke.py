from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
EVIDENCE = ROOT / "results/c374_kummer_arboreal_evidence.json"
YAML = ROOT / "evaluations/route_a/HCS-C374/2026-09-04.yaml"


def run(script: str, *args: str) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    proc = subprocess.run(
        [sys.executable, "-B", str(CODE / script), *args],
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if proc.returncode:
        raise AssertionError(proc.stdout)
    return proc.stdout


class C374Smoke(unittest.TestCase):
    def test_01_isolated_core_lanes(self):
        with tempfile.TemporaryDirectory(prefix="c374-smoke-") as directory:
            output = Path(directory) / "evidence.json"
            self.assertIn("C374_PRODUCER_PASS", run("c374_kummer_arboreal_producer.py", "--output", str(output)))
            self.assertIn("PASS (247 assertions)", run("c374_kummer_arboreal_checker.py", "--input", str(output)))
            self.assertIn("PASS (4145 exact checks)", run("c374_kummer_arboreal_sympy_crosscheck.py", "--input", str(output)))

    def test_02_replay_and_mutation(self):
        self.assertIn("byte replay: PASS", run("c374_kummer_arboreal_replay.py"))
        self.assertIn("PASS (42 attacks)", run("c374_kummer_arboreal_mutation.py"))

    def test_03_scope_and_paper_sentinels(self):
        evidence = json.loads(EVIDENCE.read_text())
        route = yaml.safe_load(YAML.read_text())
        self.assertEqual(set(evidence["scope_flags"].values()), {False})
        self.assertEqual(set(route["scope_flags"].values()), {False})
        self.assertFalse(route["route_b_invocation_allowed"])
        self.assertEqual(route["a4"]["verdict"], "A4_FORMAL_HINT")
        self.assertEqual(evidence["analytic_theorem"]["inverse_limit_index"], 2)
        self.assertEqual(evidence["arithmetic_controls"]["composite_label_decomposition"]
                         ["prime_power_count"], 5)
        self.assertEqual(evidence["arithmetic_controls"]["composite_label_decomposition"]
                         ["mixed_composite_count"], 20)
        source = (ROOT / "paper/main_body.tex").read_text()
        for token in (
            "Radical--cyclotomic intersection", "Exact image and restriction",
            "Fixed-root law", "Root-prime density", "Infinite arboreal image",
            "Route B is not invoked",
        ):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()
