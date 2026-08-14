#!/usr/bin/env python3
"""Write or verify the scoped and full-project HCS-C54 manifests."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
FULL_MANIFEST = PROJECT / "results/ARTIFACT_HASHES.sha256"
SCOPED_MANIFEST = PROJECT / "results/CODE_RESULTS_HASHES.sha256"
CERT_RELATIVE = "results/c54_certificate.json"
CHECK_RELATIVE = "results/independent_check.json"
SCOPED_MANIFEST_RELATIVE = "results/CODE_RESULTS_HASHES.sha256"
ROUTE_RELATIVE = "route_a_evaluation.yaml"
ROUTE_ARCHIVE_RELATIVE = "evaluations/route_a/HCS-C54/20260814T134920Z.yaml"
SCOPED_REQUIRED = {
    "code/README.md",
    "code/c54_producer.py",
    "code/c54_checker.py",
    "code/test_c54.py",
    "code/c54_atomic_promote.py",
    "code/c54_hash_manifest.py",
    "code/run_c54.sh",
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
    ROUTE_ARCHIVE_RELATIVE,
    "paper/main.tex",
    "paper/main.pdf",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/COMPILATION_REPORT.md",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_source_category.tex",
    "paper/sections/3_universal_group.tex",
    "paper/sections/4_rational_group_form.tex",
    "paper/sections/5_denominator_rigidity.tex",
    "paper/sections/6_n3_character.tex",
    "paper/sections/7_counterpacket_scope.tex",
    "paper/sections/8_exact_replay.tex",
    "paper/sections/9_declarations.tex",
    "paper/sections/A_proof_details.tex",
    "paper/sections/B_fermat_refinement.tex",
    "code/README.md",
    "code/c54_producer.py",
    "code/c54_checker.py",
    "code/test_c54.py",
    "code/c54_atomic_promote.py",
    "code/c54_hash_manifest.py",
    "code/run_c54.sh",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    CERT_RELATIVE,
    CHECK_RELATIVE,
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
    extras = set(artifacts) - FULL_REQUIRED
    if missing or extras:
        raise SystemExit(
            "manifest inventory mismatch; missing="
            + ",".join(sorted(missing))
            + "; extras="
            + ",".join(sorted(extras))
        )
    if artifacts[ROUTE_RELATIVE].read_bytes() != artifacts[
        ROUTE_ARCHIVE_RELATIVE
    ].read_bytes():
        raise SystemExit("Route-A root/archive byte mismatch")
    return artifacts


def manifest_text(artifacts: dict[str, Path]) -> str:
    return "".join(
        f"{digest(artifacts[relative])}  {relative}\n" for relative in sorted(artifacts)
    )


def atomic_write(output: Path, text: str) -> None:
    temporary = output.with_name(output.name + ".new")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(output)


def write_manifests(
    full_output: Path,
    scoped_output: Path,
    certificate_override: Path | None,
    check_override: Path | None,
) -> None:
    scoped_text = manifest_text(
        scoped_inventory(certificate_override, check_override)
    )
    atomic_write(scoped_output, scoped_text)
    full_text = manifest_text(
        full_inventory(certificate_override, check_override, scoped_output)
    )
    atomic_write(full_output, full_text)
    print(f"wrote {len(scoped_text.splitlines())} scoped manifest entries")
    print(f"wrote {len(full_text.splitlines())} full-project manifest entries")


def verify_manifests(
    full_manifest: Path,
    scoped_manifest: Path,
    certificate_override: Path | None,
    check_override: Path | None,
) -> None:
    if not scoped_manifest.is_file():
        raise SystemExit(f"scoped manifest missing: {scoped_manifest}")
    expected_scoped = manifest_text(
        scoped_inventory(certificate_override, check_override)
    )
    if scoped_manifest.read_text(encoding="utf-8") != expected_scoped:
        raise SystemExit("scoped manifest inventory or digest mismatch")
    if not full_manifest.is_file():
        raise SystemExit(f"full-project manifest missing: {full_manifest}")
    expected_full = manifest_text(
        full_inventory(certificate_override, check_override, scoped_manifest)
    )
    if full_manifest.read_text(encoding="utf-8") != expected_full:
        raise SystemExit("full-project manifest inventory or digest mismatch")
    print(f"verified {len(expected_scoped.splitlines())} scoped manifest entries")
    print(f"verified {len(expected_full.splitlines())} full-project manifest entries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=FULL_MANIFEST)
    parser.add_argument("--scoped-manifest", type=Path, default=SCOPED_MANIFEST)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    if (arguments.certificate is None) != (arguments.check is None):
        parser.error("--certificate and --check must be supplied together")
    if arguments.write:
        write_manifests(
            arguments.manifest,
            arguments.scoped_manifest,
            arguments.certificate,
            arguments.check,
        )
    verify_manifests(
        arguments.manifest,
        arguments.scoped_manifest,
        arguments.certificate,
        arguments.check,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
