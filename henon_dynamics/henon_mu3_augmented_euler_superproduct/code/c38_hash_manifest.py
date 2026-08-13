#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "ARTIFACT_HASHES.sha256"
EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256", "compile.log", "main.aux", "main.bbl",
    "main.blg", "main.fdb_latexmk", "main.fls", "main.log", "main.out",
}
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
REQUIRED = {
    "README.md", "DERIVATION_PACKAGE.md", "EXPERIMENT_PLAN.md",
    "EXPERIMENT_TRACKER.md", "IMPLEMENTATION_CHECKLIST.md", "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md", "SOURCE_AUDIT.md", "results/RESULTS.md",
    "results/c38_certificate.json", "results/independent_check.json",
    "results/TEST_REPORT.md", "paper/main.tex", "paper/main.pdf",
    "paper/references.bib", "paper/math_commands.tex",
    "code/c38_producer.py", "code/c38_checker.py", "code/test_c38.py",
    "code/run_c38.sh", "code/c38_hash_manifest.py",
    "route_a_evaluation.yaml", "paper/COMPILATION_REPORT.md",
    "evaluations/route_a/HCS-C38/20260813T210000Z.yaml",
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tracked() -> list[Path]:
    paths = []
    for path in PROJECT.rglob("*"):
        if not path.is_file() or path.name in EXCLUDED_NAMES:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        paths.append(path)
    rel = {str(p.relative_to(PROJECT)) for p in paths}
    missing = sorted(REQUIRED - rel)
    if missing:
        raise SystemExit("required release artifacts missing: " + ", ".join(missing))
    return sorted(paths, key=lambda p: str(p.relative_to(PROJECT)))


def write() -> None:
    lines = [f"{digest(path)}  {path.relative_to(PROJECT)}" for path in tracked()]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} manifest entries")


def verify() -> None:
    if not MANIFEST.is_file():
        raise SystemExit("manifest missing")
    expected = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, rel = line.split("  ", 1)
        expected[rel] = sha
    actual_paths = tracked()
    actual_rel = {str(p.relative_to(PROJECT)) for p in actual_paths}
    if set(expected) != actual_rel:
        raise SystemExit("manifest inventory mismatch")
    for path in actual_paths:
        rel = str(path.relative_to(PROJECT))
        if digest(path) != expected[rel]:
            raise SystemExit(f"artifact digest mismatch: {rel}")
    print(f"verified {len(expected)} manifest entries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    write() if args.write else verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
