#!/usr/bin/env python3
"""Write or verify the repository-anchored HCS-C16 release manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


CANDIDATE_ID = "HCS-C16"
RELEASE_TAG = "hcs-c16-v1"
PROJECT = Path("henon_dynamics/s_arithmetic_height_clock_obstruction")
RELEASE_FILES = (
    Path("henon_dynamics/README.md"),
    Path("henon_dynamics/docs/candidate_registry.md"),
    Path("henon_dynamics/docs/obstruction_registry.md"),
    Path("henon_dynamics/docs/related_programs/README.md"),
    PROJECT / "AUTO_REVIEW.md",
    PROJECT / "COMPILE_REPORT.md",
    PROJECT / "DERIVATION_PACKAGE.md",
    PROJECT / "EXPERIMENT_PLAN.md",
    PROJECT / "IDEA_REPORT.md",
    PROJECT / "NARRATIVE_REPORT.md",
    PROJECT / "PAPER_PLAN.md",
    PROJECT / "README.md",
    PROJECT / "REPOSITORY_UPDATE.md",
    PROJECT / "SOURCE_AUDIT.md",
    PROJECT / "requirements.txt",
    PROJECT / "code/independent_check.py",
    PROJECT / "code/release_manifest.py",
    PROJECT / "code/s_arithmetic_clock.py",
    PROJECT / "code/test_s_arithmetic_clock.py",
    PROJECT / "evaluations/route_a/hcs_c16/20260807T041943Z.yaml",
    PROJECT / "paper/main.pdf",
    PROJECT / "paper/main.tex",
    PROJECT / "paper/math_commands.tex",
    PROJECT / "paper/references.bib",
    PROJECT / "paper/sections/0_abstract.tex",
    PROJECT / "paper/sections/1_introduction.tex",
    PROJECT / "paper/sections/2_arithmetic_host.tex",
    PROJECT / "paper/sections/3_joint_clock.tex",
    PROJECT / "paper/sections/4_flat_and_wall.tex",
    PROJECT / "paper/sections/5_height.tex",
    PROJECT / "paper/sections/6_spectral.tex",
    PROJECT / "paper/sections/7_assessment.tex",
    PROJECT / "paper/sections/A_reproducibility.tex",
    PROJECT / "results/artifact_hashes.json",
    PROJECT / "results/exact_certificates.json",
    PROJECT / "results/independent_check.json",
    PROJECT / "results/near_wall.csv",
    PROJECT / "results/primitive_box_counts.csv",
    PROJECT / "results/primitive_height_counts.csv",
)
DEFAULT_OUTPUT = PROJECT / "results/release_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def expected_hashes(root: Path) -> dict[str, str]:
    missing = [str(path) for path in RELEASE_FILES if not (root / path).is_file()]
    if missing:
        raise FileNotFoundError(f"missing release files: {missing!r}")
    return {path.as_posix(): sha256(root / path) for path in RELEASE_FILES}


def write_manifest(root: Path, output: Path) -> None:
    payload = {
        "candidate_id": CANDIDATE_ID,
        "files": expected_hashes(root),
        "provenance_note": (
            "SHA-256 binds the listed release files for consistency. "
            "Authenticity is supplied by the Git remote and release tag, not by this self-issued file."
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
    if set(payload) != {
        "candidate_id", "files", "provenance_note", "release_tag", "schema_version"
    }:
        raise ValueError("release manifest top-level schema mismatch")
    if payload["candidate_id"] != CANDIDATE_ID:
        raise ValueError("candidate ID mismatch")
    if payload["release_tag"] != RELEASE_TAG or payload["schema_version"] != 1:
        raise ValueError("release tag or schema version mismatch")
    expected = expected_hashes(root)
    if payload["files"] != expected:
        actual = payload.get("files")
        actual_keys = set(actual) if isinstance(actual, dict) else set()
        expected_keys = set(expected)
        changed = sorted(
            key for key in actual_keys & expected_keys if actual.get(key) != expected[key]
        ) if isinstance(actual, dict) else []
        raise ValueError(
            "release hash mismatch: "
            f"missing={sorted(expected_keys - actual_keys)!r}, "
            f"extra={sorted(actual_keys - expected_keys)!r}, changed={changed!r}"
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
    repo = repository_root()
    if arguments.write:
        write_manifest(repo, arguments.output)
    else:
        verify_manifest(repo, arguments.output)
