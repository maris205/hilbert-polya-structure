#!/usr/bin/env python3
"""Run unit tests and emit a deterministic machine-readable report."""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import unittest

import test_counterterms


def flatten(suite: unittest.TestSuite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_counterterms)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    payload = {
        "schema_version": "SD-C31-unit-tests-v1",
        "candidate_id": "SD-C31",
        "tests_run": result.testsRun,
        "failure_count": len(result.failures),
        "error_count": len(result.errors),
        "skipped_count": len(result.skipped),
        "all_pass": result.wasSuccessful(),
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
        "failures": [test.id() for test, _ in result.failures],
        "errors": [test.id() for test, _ in result.errors],
        "test_ids": sorted(
            test.id()
            for test in flatten(unittest.defaultTestLoader.loadTestsFromModule(test_counterterms))
        ),
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "test_report.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not result.wasSuccessful():
        raise SystemExit(stream.getvalue())


if __name__ == "__main__":
    main()
