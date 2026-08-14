#!/usr/bin/env python3
"""Write or verify the full-project HCS-C51 release manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "results/ARTIFACT_HASHES.sha256"
CERT_RELATIVE = "results/c51_certificate.json"
CHECK_RELATIVE = "results/independent_check.json"
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
    "route_a_evaluation.yaml",
    "evaluations/route_a/HCS-C51/20260814T050000Z.yaml",
    "paper/main.tex",
    "paper/main.pdf",
    "paper/math_commands.tex",
    "paper/references.bib",
    "paper/COMPILATION_REPORT.md",
    "paper/sections/0_abstract.tex",
    "paper/sections/1_introduction.tex",
    "paper/sections/2_source_and_main.tex",
    "paper/sections/3_two_weight_rank.tex",
    "paper/sections/4_log_l_extraction.tex",
    "paper/sections/5_center_tower.tex",
    "paper/sections/6_compatible_odd.tex",
    "paper/sections/7_hodge_projector.tex",
    "paper/sections/8_route_a.tex",
    "paper/sections/9_declarations.tex",
    "paper/sections/A_exact_replays.tex",
    "code/README.md",
    "code/c51_producer.py",
    "code/c51_checker.py",
    "code/test_c51.py",
    "code/run_c51.sh",
    "code/c51_hash_manifest.py",
    "code/c51_atomic_promote.py",
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
        relative = str(path.relative_to(PROJECT))
        artifacts[relative] = path
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
        write_manifest(
            arguments.manifest, arguments.certificate, arguments.check
        )
    else:
        verify_manifest(
            arguments.manifest, arguments.certificate, arguments.check
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
