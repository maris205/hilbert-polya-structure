#!/usr/bin/env python3
"""Write or verify the scoped and full-project HCS-C55 manifests.

The scoped manifest is the persistent code/results identity.  A later paper
freeze may refresh only the full manifest; it must never silently replace the
historical scoped identity.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
FULL_MANIFEST = PROJECT / "results/ARTIFACT_HASHES.sha256"
SCOPED_MANIFEST = PROJECT / "results/CODE_RESULTS_HASHES.sha256"
CERT_RELATIVE = "results/c55_certificate.json"
CHECK_RELATIVE = "results/independent_check.json"
SCOPED_MANIFEST_RELATIVE = "results/CODE_RESULTS_HASHES.sha256"
ROUTE_RELATIVE = "route_a_evaluation.yaml"

SCOPED_REQUIRED = {
    "code/README.md",
    "code/c55_producer.py",
    "code/c55_checker.py",
    "code/test_c55.py",
    "code/c55_atomic_promote.py",
    "code/c55_hash_manifest.py",
    "code/run_c55.sh",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    CERT_RELATIVE,
    CHECK_RELATIVE,
}

FULL_REQUIRED = {
    "README.md",
    "RESEARCH_QUESTION.md",
    "THEOREM_PACKAGE.md",
    "PROOF_PACKAGE.md",
    "DERIVATION_PACKAGE.md",
    "EXPERIMENT_PLAN.md",
    "EXPERIMENT_TRACKER.md",
    "IMPLEMENTATION_CHECKLIST.md",
    "METHODOLOGY_BLUEPRINT.md",
    "PAPER_PLAN.md",
    "NARRATIVE_REPORT.md",
    "SOURCE_AUDIT.md",
    "INTEGRITY_REPORT.md",
    ROUTE_RELATIVE,
    *SCOPED_REQUIRED,
    SCOPED_MANIFEST_RELATIVE,
}

FULL_EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256",
    "compile.log",
    "main.aux",
    "main.bbl",
    "main.blg",
    "main.fdb_latexmk",
    "main.fls",
    "main.log",
    "main.out",
    "main.txt",
}
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def scoped_inventory(
    certificate_override: Path | None = None,
    check_override: Path | None = None,
) -> dict[str, Path]:
    artifacts: dict[str, Path] = {}
    for directory in (PROJECT / "code", PROJECT / "results"):
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if not path.is_file() or path.name in {
                "ARTIFACT_HASHES.sha256",
                "CODE_RESULTS_HASHES.sha256",
            }:
                continue
            if any(part in EXCLUDED_PARTS for part in path.parts):
                continue
            artifacts[str(path.relative_to(PROJECT))] = path
    if certificate_override is not None:
        artifacts[CERT_RELATIVE] = certificate_override
    if check_override is not None:
        artifacts[CHECK_RELATIVE] = check_override
    missing = SCOPED_REQUIRED - set(artifacts)
    extras = set(artifacts) - SCOPED_REQUIRED
    if missing or extras:
        raise SystemExit(
            "scoped manifest inventory mismatch; missing="
            + ",".join(sorted(missing))
            + "; extras="
            + ",".join(sorted(extras))
        )
    return artifacts


def full_inventory(
    certificate_override: Path | None = None,
    check_override: Path | None = None,
    scoped_manifest_override: Path | None = None,
) -> dict[str, Path]:
    artifacts: dict[str, Path] = {}
    for path in PROJECT.rglob("*"):
        if not path.is_file() or path.name in FULL_EXCLUDED_NAMES:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        artifacts[str(path.relative_to(PROJECT))] = path
    if certificate_override is not None:
        artifacts[CERT_RELATIVE] = certificate_override
    if check_override is not None:
        artifacts[CHECK_RELATIVE] = check_override
    if scoped_manifest_override is not None:
        artifacts[SCOPED_MANIFEST_RELATIVE] = scoped_manifest_override
    missing = FULL_REQUIRED - set(artifacts)
    if missing:
        raise SystemExit("full manifest required inventory missing=" + ",".join(sorted(missing)))
    archives = sorted((PROJECT / "evaluations/route_a/HCS-C55").glob("*.yaml"))
    if len(archives) > 1:
        raise SystemExit("multiple HCS-C55 Route-A archives")
    if archives and artifacts[ROUTE_RELATIVE].read_bytes() != archives[0].read_bytes():
        raise SystemExit("Route-A root/archive byte mismatch")
    return artifacts


def manifest_text(artifacts: dict[str, Path]) -> str:
    return "".join(
        f"{digest(artifacts[relative])}  {relative}\n"
        for relative in sorted(artifacts)
    )


def atomic_write(output: Path, text: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".new")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(output)


def expected_scoped(certificate: Path | None, check: Path | None) -> str:
    return manifest_text(scoped_inventory(certificate, check))


def expected_full(
    certificate: Path | None,
    check: Path | None,
    scoped_manifest: Path,
) -> str:
    return manifest_text(full_inventory(certificate, check, scoped_manifest))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--scoped-only", action="store_true")
    mode.add_argument("--full-only", action="store_true")
    parser.add_argument("--manifest", type=Path, default=FULL_MANIFEST)
    parser.add_argument("--scoped-manifest", type=Path, default=SCOPED_MANIFEST)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    if (arguments.certificate is None) != (arguments.check is None):
        parser.error("--certificate and --check must be supplied together")
    do_scoped = not arguments.full_only
    do_full = not arguments.scoped_only

    if arguments.write and do_scoped:
        text = expected_scoped(arguments.certificate, arguments.check)
        atomic_write(arguments.scoped_manifest, text)
        print(f"wrote {len(text.splitlines())} scoped manifest entries")
    if do_scoped:
        expected = expected_scoped(arguments.certificate, arguments.check)
        if not arguments.scoped_manifest.is_file():
            raise SystemExit(f"scoped manifest missing: {arguments.scoped_manifest}")
        if arguments.scoped_manifest.read_text(encoding="utf-8") != expected:
            raise SystemExit("scoped manifest inventory or digest mismatch")
        print(f"verified {len(expected.splitlines())} scoped manifest entries")

    if arguments.write and do_full:
        if not arguments.scoped_manifest.is_file():
            raise SystemExit("full manifest requires an existing scoped manifest")
        text = expected_full(
            arguments.certificate, arguments.check, arguments.scoped_manifest
        )
        atomic_write(arguments.manifest, text)
        print(f"wrote {len(text.splitlines())} full-project manifest entries")
    if do_full:
        if not arguments.manifest.is_file():
            raise SystemExit(f"full manifest missing: {arguments.manifest}")
        expected = expected_full(
            arguments.certificate, arguments.check, arguments.scoped_manifest
        )
        if arguments.manifest.read_text(encoding="utf-8") != expected:
            raise SystemExit("full manifest inventory or digest mismatch")
        print(f"verified {len(expected.splitlines())} full-project manifest entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
