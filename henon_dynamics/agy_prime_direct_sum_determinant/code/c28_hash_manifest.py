#!/usr/bin/env python3
"""Write or verify the frozen HCS-C28 artifact hash manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results" / "ARTIFACT_HASHES.sha256"
EXCLUDED_SUFFIXES = {".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".run.xml", ".toc"}
EXCLUDED_DIRECTORIES = {"__pycache__", ".pytest_cache"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files() -> list[Path]:
    roots = [
        PROJECT / "README.md",
        PROJECT / "RESEARCH_QUESTION.md",
        PROJECT / "EXPERIMENT_PLAN.md",
        PROJECT / "DERIVATION_PACKAGE.md",
        PROJECT / "THEOREM_PACKAGE.md",
        PROJECT / "SOURCE_AUDIT.md",
        PROJECT / "NARRATIVE_REPORT.md",
        PROJECT / "PAPER_PLAN.md",
        PROJECT / "route_a_evaluation.yaml",
        PROJECT / "requirements.txt",
        PROJECT / "code",
        PROJECT / "results",
        PROJECT / "paper",
    ]
    files: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            candidates = [root]
        else:
            candidates = [path for path in root.rglob("*") if path.is_file()]
        for path in candidates:
            if (
                path == MANIFEST
                or path.suffix in EXCLUDED_SUFFIXES
                or any(part in EXCLUDED_DIRECTORIES for part in path.parts)
            ):
                continue
            files.append(path)
    return sorted(set(files), key=lambda path: str(path.relative_to(PROJECT)))


def render() -> str:
    return "".join(f"{sha256(path)}  {path.relative_to(PROJECT)}\n" for path in tracked_files())


def main() -> None:
    args = parse_args()
    expected = render()
    if args.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(PROJECT)} with {len(tracked_files())} entries")
        return
    if not MANIFEST.exists():
        raise SystemExit("manifest missing; use --write only for an intentional release update")
    observed = MANIFEST.read_text(encoding="utf-8")
    if observed != expected:
        raise SystemExit("artifact hash manifest mismatch")
    print(f"verified {len(tracked_files())} artifact hashes")


if __name__ == "__main__":
    main()
