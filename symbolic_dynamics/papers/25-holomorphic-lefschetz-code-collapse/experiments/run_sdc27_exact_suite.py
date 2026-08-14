#!/usr/bin/env python3
"""Run two deterministic SD-C27 pipelines, audit, and freeze hashes."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PIPELINE = (
    ("code/generate_sdc27_artifacts.py",),
    ("code/run_sdc27_tests.py",),
    ("code/analyze_sdc27_results.py",),
)
FINALIZE = (
    ("code/audit_sdc27_artifact_integrity.py",),
    ("code/freeze_sdc27_artifacts.py",),
    ("code/freeze_sdc27_artifacts.py", "--check"),
)
EXCLUDED_FROM_DOUBLE_RUN = {
    "results/SHA256SUMS.txt",
    "results/double_run_certificate.json",
    "results/integrity_audit.json",
}


def environment() -> dict[str, str]:
    value = dict(os.environ)
    value["PYTHONDONTWRITEBYTECODE"] = "1"
    value["PYTHONHASHSEED"] = "0"
    value["PYTHONPATH"] = str(ROOT / "code")
    return value


def run_commands(commands: tuple[tuple[str, ...], ...]) -> None:
    for arguments in commands:
        subprocess.run(
            [sys.executable, "-B", *arguments],
            cwd=ROOT,
            env=environment(),
            check=True,
        )


def deterministic_snapshot() -> dict[str, str]:
    paths = sorted(
        [path for path in (ROOT / "code").glob("*.py") if path.is_file()]
        + [path for path in RESULTS.iterdir() if path.is_file()],
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )
    return {
        path.relative_to(ROOT).as_posix(): sha256(path.read_bytes()).hexdigest()
        for path in paths
        if path.relative_to(ROOT).as_posix() not in EXCLUDED_FROM_DOUBLE_RUN
    }


def combined_digest(snapshot: dict[str, str]) -> str:
    payload = "\n".join(
        f"{digest}  {path}" for path, digest in snapshot.items()
    ) + "\n"
    return sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    run_commands(PIPELINE)
    first = deterministic_snapshot()
    run_commands(PIPELINE)
    second = deterministic_snapshot()
    mismatched = sorted(
        path for path in set(first) | set(second) if first.get(path) != second.get(path)
    )
    first_digest = combined_digest(first)
    second_digest = combined_digest(second)
    certificate = {
        "candidate_id": "SD-C27",
        "artifact_count": len(first),
        "first_run_combined_sha256": first_digest,
        "second_run_combined_sha256": second_digest,
        "mismatched_paths": mismatched,
        "byte_identical": not mismatched and first_digest == second_digest,
        "status": "PASS" if not mismatched and first_digest == second_digest else "FAIL",
        "protocol": "two complete generator+pytest+analysis runs; code/result bytes compared",
        "excluded_self_referential_artifacts": sorted(EXCLUDED_FROM_DOUBLE_RUN),
    }
    (RESULTS / "double_run_certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(certificate, indent=2, sort_keys=True))
    if certificate["status"] != "PASS":
        return 1
    run_commands(FINALIZE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
