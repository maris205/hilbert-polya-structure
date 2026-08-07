#!/usr/bin/env python3
"""Write or verify the repository-anchored HCS-C17 release manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


CANDIDATE_ID = "HCS-C17"
RELEASE_TAG = "hcs-c17-v1"
PROJECT = Path("henon_dynamics/modular_scattering_clock_obstruction")
GLOBAL_FILES = (
    Path("henon_dynamics/README.md"),
    Path("henon_dynamics/docs/candidate_registry.md"),
    Path("henon_dynamics/docs/obstruction_registry.md"),
    Path("henon_dynamics/docs/related_programs/README.md"),
)
BUILD_SUFFIXES = {".aux", ".bbl", ".blg", ".log", ".out", ".pyc"}
IGNORED_PARTS = {"__pycache__", ".pytest_cache"}
DEFAULT_OUTPUT = PROJECT / "results/release_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def release_files(root: Path) -> tuple[Path, ...]:
    project_root = root / PROJECT
    paths = list(GLOBAL_FILES)
    for absolute in sorted(project_root.rglob("*")):
        if not absolute.is_file():
            continue
        relative = absolute.relative_to(root)
        if relative == DEFAULT_OUTPUT:
            continue
        if absolute.suffix in BUILD_SUFFIXES:
            continue
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        paths.append(relative)
    if len(paths) != len(set(paths)):
        raise ValueError("release file enumeration contains duplicates")
    return tuple(paths)


def expected_hashes(root: Path) -> dict[str, str]:
    paths = release_files(root)
    missing = [str(path) for path in paths if not (root / path).is_file()]
    if missing:
        raise FileNotFoundError(f"missing release files: {missing!r}")
    return {path.as_posix(): sha256(root / path) for path in paths}


def write_manifest(root: Path, output: Path) -> None:
    payload = {
        "candidate_id": CANDIDATE_ID,
        "files": expected_hashes(root),
        "provenance_note": (
            "SHA-256 binds the listed release files for consistency. "
            "Authenticity is supplied by the SSH Git remote and release tag, "
            "not by this self-issued file."
        ),
        "release_tag": RELEASE_TAG,
        "schema_version": 1,
    }
    destination = root / output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {destination} with {len(payload['files'])} files")


def load_strict(path: Path) -> object:
    def no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


def verify_manifest(root: Path, output: Path) -> None:
    destination = root / output
    payload = load_strict(destination)
    if not isinstance(payload, dict):
        raise ValueError("release manifest must be a JSON object")
    expected_keys = {
        "candidate_id", "files", "provenance_note", "release_tag", "schema_version"
    }
    if set(payload) != expected_keys:
        raise ValueError("release manifest top-level schema mismatch")
    if payload["candidate_id"] != CANDIDATE_ID:
        raise ValueError("candidate ID mismatch")
    if payload["release_tag"] != RELEASE_TAG or payload["schema_version"] != 1:
        raise ValueError("release tag or schema version mismatch")
    expected = expected_hashes(root)
    if payload["files"] != expected:
        actual = payload.get("files")
        actual_keys = set(actual) if isinstance(actual, dict) else set()
        expected_file_keys = set(expected)
        changed = (
            sorted(
                key
                for key in actual_keys & expected_file_keys
                if actual.get(key) != expected[key]
            )
            if isinstance(actual, dict)
            else []
        )
        raise ValueError(
            "release hash mismatch: "
            f"missing={sorted(expected_file_keys - actual_keys)!r}, "
            f"extra={sorted(actual_keys - expected_file_keys)!r}, "
            f"changed={changed!r}"
        )
    print(f"verified {destination} with {len(expected)} files")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--verify", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    repository = repository_root()
    if arguments.write:
        write_manifest(repository, arguments.output)
    else:
        verify_manifest(repository, arguments.output)
