#!/usr/bin/env python3
"""Write the deterministic SHA-256 release manifest for HCS-C26."""

from __future__ import annotations

import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
ARTIFACTS = (
    "requirements.txt",
    "code/README.md",
    "code/c26_producer.py",
    "code/c26_independent_check.py",
    "code/c26_hash_manifest.py",
    "code/test_c26.py",
    "code/run_c26.sh",
    "results/c26_certificate.json",
    "results/c26_independent_check.json",
    "results/README.md",
    "results/RESULTS.md",
    "results/VALIDATION_REPORT.md",
    "results/TEST_REPORT.md",
    "results/MATERIAL_PASSPORTS.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    missing = [relative for relative in ARTIFACTS if not (PROJECT / relative).is_file()]
    if missing:
        raise SystemExit(f"refusing incomplete manifest; missing: {missing}")
    lines = [f"{digest(PROJECT / relative)}  {relative}" for relative in ARTIFACTS]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT} with {len(lines)} artifacts")


if __name__ == "__main__":
    main()
