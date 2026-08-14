#!/usr/bin/env python3
"""Run all 14 exact SD-C20 tests and write a deterministic certificate."""

from __future__ import annotations

import io
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import test_sdc20_incidence_transition_holonomy_experiment as test_module  # noqa: E402


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_module)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    payload = {
        "candidate_id": "SD-C20",
        "errors": len(result.errors),
        "failures": len(result.failures),
        "skipped": len(result.skipped),
        "successful": result.wasSuccessful(),
        "target_zero_data_used": False,
        "tests_run": result.testsRun,
    }
    (ROOT / "results" / "test_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(stream.getvalue(), end="")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
