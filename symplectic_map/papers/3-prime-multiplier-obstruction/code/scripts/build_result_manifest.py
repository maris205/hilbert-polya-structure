#!/usr/bin/env python3
"""Build the deterministic post-validation artifact manifest."""

from __future__ import annotations

import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from prime_multiplier.protocol import sha256_file, write_json


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = PROJECT_ROOT / "results" / "final_result_manifest.json"


def included_files() -> list[Path]:
    paths: list[Path] = []
    for directory in ("code", "experiments", "notes", "results"):
        for path in (PROJECT_ROOT / directory).rglob("*"):
            if not path.is_file():
                continue
            relative_parts = path.relative_to(PROJECT_ROOT).parts
            if "__pycache__" in relative_parts or ".pytest_cache" in relative_parts:
                continue
            if path == OUTPUT or path.suffix == ".pyc":
                continue
            paths.append(path)
    paths.append(PROJECT_ROOT / "pyproject.toml")
    return sorted(set(paths), key=lambda item: str(item.relative_to(PROJECT_ROOT)))


def aggregate_hash(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        relative = str(path.relative_to(PROJECT_ROOT)).encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(bytes.fromhex(sha256_file(path)))
        digest.update(b"\n")
    return digest.hexdigest()


def main() -> int:
    paths = included_files()
    artifact_hashes = {
        str(path.relative_to(PROJECT_ROOT)): sha256_file(path) for path in paths
    }
    code_paths = [path for path in paths if path.relative_to(PROJECT_ROOT).parts[0] == "code"]
    test_suite = ET.parse(PROJECT_ROOT / "results" / "pytest.xml").getroot().find("testsuite")
    if test_suite is None:
        raise RuntimeError("pytest.xml contains no testsuite")
    payload = {
        "candidate_id": "pcf_quadratic_prime_multiplier_obstruction_v1",
        "created_utc_date": "2026-08-13",
        "verification_status": "VERIFIED",
        "source_lock_sha256": artifact_hashes["experiments/source_lock.json"],
        "code_tree_sha256": aggregate_hash(code_paths),
        "artifact_set_sha256": aggregate_hash(paths),
        "artifact_hashes": artifact_hashes,
        "test_suite": {
            "tests": int(test_suite.attrib["tests"]),
            "failures": int(test_suite.attrib["failures"]),
            "errors": int(test_suite.attrib["errors"]),
            "skipped": int(test_suite.attrib["skipped"]),
        },
        "scientific_classification": {
            "raw_rational_prime": "ABSENT_BY_THEOREM",
            "odd_rational_exponent_prime": "ABSENT_BY_THEOREM",
            "p2_exponent_prime_period_1": "ABSENT",
            "p2_exponent_prime_period_ge_2": "OPEN",
            "complex_modulus_only": "OUTSIDE_THEOREM",
            "symplectic_bridge": "BRANCHWISE_EXACT_ONLY",
        },
        "external_prime_or_zero_data_accessed": False,
        "conditional_real_orbit_ledger_executed": False,
        "manifest_role": "post-validation immutable convenience index; it is not a pre-execution unlock marker",
    }
    write_json(OUTPUT, payload)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

