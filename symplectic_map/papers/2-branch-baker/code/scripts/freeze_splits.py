#!/usr/bin/env python3
"""Create hash-bound validation or sealed-test unlock declarations."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from branch_baker.protocol import (
    PROJECT_ROOT,
    REQUIRED_DEVELOPMENT_ARTIFACTS,
    REQUIRED_VALIDATION_ARTIFACTS,
    TEST_UNLOCK_PATH,
    VALIDATION_UNLOCK_PATH,
    VERIFICATION_MANIFEST_PATH,
    build_test_unlock,
    build_validation_unlock,
    build_verification_manifest,
    write_json_new,
)


DEFAULT_DEVELOPMENT = list(REQUIRED_DEVELOPMENT_ARTIFACTS)
DEFAULT_VALIDATION = list(REQUIRED_VALIDATION_ARTIFACTS)


def _paths(values: list[str]) -> list[Path]:
    paths = []
    for value in values:
        path = Path(value)
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        paths.append(path)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("validation", "test"))
    args = parser.parse_args()
    created = datetime.now(timezone.utc).isoformat()

    if args.stage == "validation":
        development = _paths(DEFAULT_DEVELOPMENT)
        payload = build_validation_unlock(development, created)
        write_json_new(VALIDATION_UNLOCK_PATH, payload)
        print(VALIDATION_UNLOCK_PATH)
        return

    validation = _paths(DEFAULT_VALIDATION)
    manifest = build_verification_manifest(validation, created)
    write_json_new(VERIFICATION_MANIFEST_PATH, manifest)
    unlock = build_test_unlock(created)
    write_json_new(TEST_UNLOCK_PATH, unlock)
    print(VERIFICATION_MANIFEST_PATH)
    print(TEST_UNLOCK_PATH)


if __name__ == "__main__":
    main()
