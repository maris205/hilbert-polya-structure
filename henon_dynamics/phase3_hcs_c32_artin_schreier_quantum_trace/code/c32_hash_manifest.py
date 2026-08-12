#!/usr/bin/env python3
"""Fail-closed SHA-256 manifest for the HCS-C32 Phase-3 release."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results" / "ARTIFACT_HASHES.sha256"

REQUIRED_RELATIVE_PATHS = {
    "README.md",
    "EXACT_GATE_PROTOCOL.md",
    "THEOREM_PACKAGE.md",
    "DERIVATION_PACKAGE.md",
    "SOURCE_AUDIT.md",
    "SYNTHESIS_REPORT.md",
    "DEVILS_ADVOCATE_CHECKPOINT2.md",
    "PHASE3_CHECKPOINT.md",
    "code/README.md",
    "code/c32_morse_gate_producer.py",
    "code/c32_morse_gate_checker.py",
    "code/c32_hash_manifest.py",
    "code/test_c32_morse_gate.py",
    "code/run_c32_phase3.sh",
    "results/README.md",
    "results/RESULTS.md",
    "results/c32_morse_gate_certificate.json",
    "results/c32_morse_gate_independent_check.json",
}

EXCLUDED_PARTS = {
    "__pycache__",
    ".pytest_cache",
    ".ipynb_checkpoints",
    ".venv",
}

EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256",
    ".DS_Store",
    ".env",
}

EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".pyd", ".swp", ".tmp"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files(project: Path = PROJECT) -> list[Path]:
    missing = sorted(
        relative
        for relative in REQUIRED_RELATIVE_PATHS
        if not (project / relative).is_file()
    )
    if missing:
        raise RuntimeError("required release artifacts missing: " + ", ".join(missing))

    files: list[Path] = []
    for path in project.rglob("*"):
        if path.is_symlink():
            raise RuntimeError(f"symlink is forbidden in release tree: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(project)
        if path.name in EXCLUDED_NAMES:
            continue
        if path.suffix in EXCLUDED_SUFFIXES:
            continue
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        files.append(relative)
    return sorted(files, key=lambda item: item.as_posix())


def rendered_manifest(project: Path = PROJECT) -> str:
    return "".join(
        f"{digest(project / relative)}  {relative.as_posix()}\n"
        for relative in tracked_files(project)
    )


def verify(project: Path = PROJECT, manifest: Path = MANIFEST) -> None:
    if not manifest.is_file():
        raise RuntimeError("artifact manifest missing")
    observed: dict[str, str] = {}
    for line_number, line in enumerate(
        manifest.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if len(line) < 67 or line[64:66] != "  ":
            raise RuntimeError(f"malformed manifest line {line_number}")
        expected_digest = line[:64]
        relative = line[66:]
        if len(expected_digest) != 64 or any(
            character not in "0123456789abcdef" for character in expected_digest
        ):
            raise RuntimeError(f"invalid digest on manifest line {line_number}")
        if relative in observed:
            raise RuntimeError(f"duplicate manifest path: {relative}")
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise RuntimeError(f"unsafe manifest path: {relative}")
        observed[relative] = expected_digest

    expected_paths = [path.as_posix() for path in tracked_files(project)]
    if sorted(observed) != expected_paths:
        missing = sorted(set(expected_paths) - set(observed))
        extra = sorted(set(observed) - set(expected_paths))
        raise RuntimeError(f"manifest inventory mismatch; missing={missing}; extra={extra}")

    for relative in expected_paths:
        actual = digest(project / relative)
        if actual != observed[relative]:
            raise RuntimeError(f"artifact digest mismatch: {relative}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="explicitly refresh the manifest; default operation is read-only verify",
    )
    args = parser.parse_args()
    if args.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(rendered_manifest(), encoding="utf-8")
    verify()
    print(f"HCS-C32 manifest PASS ({len(tracked_files())} artifacts)")


if __name__ == "__main__":
    main()

