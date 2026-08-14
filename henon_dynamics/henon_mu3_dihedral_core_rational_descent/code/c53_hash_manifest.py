#!/usr/bin/env python3
"""Write or verify the full-project HCS-C53 release manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results/ARTIFACT_HASHES.sha256"
CERT_RELATIVE = "results/c53_certificate.json"
CHECK_RELATIVE = "results/independent_check.json"
ROUTE_RELATIVE = "route_a_evaluation.yaml"
ROUTE_ARCHIVE_RELATIVE = "evaluations/route_a/HCS-C53/20260814T150000Z.yaml"
REQUIRED = {
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
    "paper/sections/2_source_main.tex",
    "paper/sections/3_explicit_descent.tex",
    "paper/sections/4_rational_packets.tex",
    "paper/sections/5_dihedral_core.tex",
    "paper/sections/6_compatible_polynomials.tex",
    "paper/sections/7_artin_scope.tex",
    "paper/sections/8_exact_replay.tex",
    "paper/sections/9_declarations.tex",
    "paper/sections/A_proof_details.tex",
    "code/README.md",
    "code/c53_producer.py",
    "code/c53_checker.py",
    "code/test_c53.py",
    "code/run_c53.sh",
    "code/c53_hash_manifest.py",
    "code/c53_atomic_promote.py",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    CERT_RELATIVE,
    CHECK_RELATIVE,
}
EXCLUDED_NAMES = {
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


def inventory(
    certificate_override: Path | None = None,
    check_override: Path | None = None,
) -> dict[str, Path]:
    artifacts: dict[str, Path] = {}
    for path in PROJECT.rglob("*"):
        if not path.is_file() or path.name in EXCLUDED_NAMES:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        artifacts[str(path.relative_to(PROJECT))] = path
    if certificate_override is not None:
        artifacts[CERT_RELATIVE] = certificate_override
    if check_override is not None:
        artifacts[CHECK_RELATIVE] = check_override
    missing = REQUIRED - set(artifacts)
    extras = set(artifacts) - REQUIRED
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
        f"{digest(artifacts[relative])}  {relative}\n"
        for relative in sorted(artifacts)
    )


def write_manifest(
    output: Path,
    certificate_override: Path | None,
    check_override: Path | None,
) -> None:
    text = manifest_text(inventory(certificate_override, check_override))
    temporary = output.with_name(output.name + ".new")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(output)
    print(f"wrote {len(text.splitlines())} full-project manifest entries")


def verify_manifest(
    manifest: Path,
    certificate_override: Path | None,
    check_override: Path | None,
) -> None:
    if not manifest.is_file():
        raise SystemExit(f"manifest missing: {manifest}")
    expected = manifest_text(inventory(certificate_override, check_override))
    if manifest.read_text(encoding="utf-8") != expected:
        raise SystemExit("manifest inventory or digest mismatch")
    print(f"verified {len(expected.splitlines())} full-project manifest entries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    if (arguments.certificate is None) != (arguments.check is None):
        parser.error("--certificate and --check must be supplied together")
    if arguments.write:
        write_manifest(arguments.manifest, arguments.certificate, arguments.check)
        verify_manifest(arguments.manifest, arguments.certificate, arguments.check)
    else:
        verify_manifest(arguments.manifest, arguments.certificate, arguments.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
