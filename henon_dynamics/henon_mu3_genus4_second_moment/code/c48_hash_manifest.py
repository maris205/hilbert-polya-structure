#!/usr/bin/env python3
"""Write or verify a deterministic HCS-C48 artifact manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256", "compile.log", "main.aux", "main.bbl",
    "main.blg", "main.fdb_latexmk", "main.fls", "main.log", "main.out",
}
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
REQUIRED = {
    "README.md", "THEOREM_PACKAGE.md", "DERIVATION_PACKAGE.md",
    "EXPERIMENT_PLAN.md", "EXPERIMENT_TRACKER.md", "IMPLEMENTATION_CHECKLIST.md",
    "PAPER_PLAN.md", "NARRATIVE_REPORT.md", "SOURCE_AUDIT.md",
    "results/RESULTS.md", "results/c48_certificate.json",
    "results/independent_check.json", "results/TEST_REPORT.md",
    "paper/main.tex", "paper/main.pdf", "paper/references.bib",
    "paper/math_commands.tex", "code/README.md", "code/c48_producer.py",
    "code/c48_checker.py", "code/test_c48.py", "code/run_c48.sh",
    "code/c48_hash_manifest.py", "route_a_evaluation.yaml",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def artifacts() -> list[Path]:
    paths: list[Path] = []
    for path in PROJECT.rglob("*"):
        if not path.is_file() or path.name in EXCLUDED_NAMES:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        paths.append(path)
    relative = {str(path.relative_to(PROJECT)) for path in paths}
    missing = sorted(REQUIRED - relative)
    if missing:
        raise SystemExit("required release artifacts missing: " + ", ".join(missing))
    return sorted(paths, key=lambda path: str(path.relative_to(PROJECT)))


def write() -> None:
    lines = [f"{digest(path)}  {path.relative_to(PROJECT)}" for path in artifacts()]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} manifest entries to {MANIFEST.relative_to(PROJECT)}")


def verify() -> None:
    if not MANIFEST.is_file():
        raise SystemExit("manifest missing")
    expected: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha256, relative = line.split("  ", 1)
        expected[relative] = sha256
    paths = artifacts()
    actual = {str(path.relative_to(PROJECT)) for path in paths}
    if set(expected) != actual:
        raise SystemExit("manifest inventory mismatch")
    for path in paths:
        relative = str(path.relative_to(PROJECT))
        if digest(path) != expected[relative]:
            raise SystemExit(f"artifact digest mismatch: {relative}")
    print(f"verified {len(expected)} manifest entries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    write() if args.write else verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
