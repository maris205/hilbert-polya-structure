#!/usr/bin/env python3
"""Run the 18 frozen SD-C33 tests and write the legacy-compatible report."""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import unittest

import test_wilson


def flatten(suite: unittest.TestSuite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    test_wilson.RESULTS = args.results
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_wilson)
    all_tests = list(flatten(unittest.defaultTestLoader.loadTestsFromModule(test_wilson)))
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    failed_ids = {test.id() for test, _ in result.failures + result.errors}
    tests = {
        test._testMethodName.removeprefix("test_"): test.id() not in failed_ids
        for test in all_tests
    }
    report = {
        "candidate_id": "SD-C33",
        "passed": sum(bool(value) for value in tests.values()),
        "total": len(tests),
        "failures": sorted(key for key, value in tests.items() if not value),
        "tests": tests,
    }
    (args.results / "test_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not result.wasSuccessful():
        raise SystemExit(stream.getvalue())
    print(json.dumps({"passed": report["passed"], "total": report["total"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
