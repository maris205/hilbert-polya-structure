#!/usr/bin/env python3
"""Run the frozen SD-C30 exact tests and write a deterministic summary."""

from __future__ import annotations

import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "test_summary.json"


class ReportCounter:
    def __init__(self) -> None:
        self.collected = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0

    def pytest_collection_finish(self, session: pytest.Session) -> None:
        self.collected = session.testscollected

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when != "call":
            if report.failed:
                self.failed += 1
            return
        if report.passed:
            self.passed += 1
        elif report.failed:
            self.failed += 1
        elif report.skipped:
            self.skipped += 1


def main() -> int:
    counter = ReportCounter()
    exit_code = pytest.main(
        [
            "-q",
            "-p",
            "no:cacheprovider",
            str(ROOT / "code" / "test_sdc30_exact.py"),
        ],
        plugins=[counter],
    )
    executed = counter.passed + counter.failed + counter.skipped
    collected = max(counter.collected, executed)
    payload = {
        "candidate_id": "SD-C30",
        "collected": collected,
        "passed": counter.passed,
        "failed": counter.failed,
        "skipped": counter.skipped,
        "status": (
            "PASS"
            if exit_code == 0 and counter.passed == collected
            else "FAIL"
        ),
        "test_mode": "exact_integer_rational_symbolic_cpu",
        "cache_provider": "disabled",
        "target_zero_data_used": False,
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return int(exit_code)


if __name__ == "__main__":
    raise SystemExit(main())
