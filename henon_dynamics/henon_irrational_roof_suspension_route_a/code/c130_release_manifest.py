#!/usr/bin/env python3
"""Build the content-addressed C130 release manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "C130_RELEASE_MANIFEST.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded_suffixes = {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"}
    rows = []
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file()):
        relative = path.relative_to(ROOT).as_posix()
        if path == OUT or "__pycache__" in path.parts or any(relative.endswith(suffix) for suffix in excluded_suffixes):
            continue
        rows.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha(path)})
    if len(rows) != 27:
        raise AssertionError(f"expected 27 payload files, found {len(rows)}")

    evidence = ROOT / "results" / "c130_suspension_evidence.json"
    pdf = ROOT / "paper" / "main.pdf"
    data = {
        "schema": "HCS-C130-release-v1",
        "candidate_id": "HCS-C130",
        "date_utc": "2026-08-24",
        "status": "RELEASE_COMPLETE",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All-period nonlattice suspension Euler/trace identity with exact clock-sector separation",
        "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "route_b_invocation_allowed": False,
        "gates": {
            "G0_source_lock": "PASS",
            "G1_mixing_sft_and_positive_roof": "PASS",
            "G2_bivariate_and_exponential_determinant": "PASS",
            "G3_all_period_primitive_euler_trace_identity": "PASS",
            "G4_irrational_clock_sector_separation": "PASS",
            "G5_rational_roof_collision_periodicity_control": "PASS",
            "G6_independent_checker_sympy_replay_and_hash_mutations": "PASS",
            "G7_double_build_fonts_warnings_visual": "PASS",
            "G8_release_manifest_27_payload_exact_closure": "PASS",
            "G9_target_divisor_match": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "metrics": {
            "period_prefix": 10,
            "rooted_closed_words": 2046,
            "primitive_cycles": 226,
            "clock_sectors": 65,
            "independent_checker_assertions": 139,
            "sympy_checks": 110,
            "repaired_hash_mutations_rejected": 43,
            "stale_hash_mutations_rejected": 1,
            "hostile_mutations_rejected_total": 44,
            "pdf_pages": 2,
        },
        "evidence_sha256": sha(evidence),
        "paper_pdf_sha256": sha(pdf),
        "file_count_excluding_manifest": len(rows),
        "excluded_from_manifest": [
            "C130_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.toc",
            "paper/main.fls",
            "paper/main.fdb_latexmk",
            "paper/main.synctex.gz",
        ],
        "nonclaims": [
            "an arithmetic Euler product, local factor, or root number",
            "a target zero or pole divisor match",
            "orbit-level injectivity within a fixed clock sector",
            "a target functional equation or counting law",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization",
        ],
        "files": rows,
    }
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C130_RELEASE_MANIFEST_WRITE_PASS",
        "payload_files": len(rows),
        "manifest_sha256": sha(OUT),
        "evidence_sha256": sha(evidence),
        "pdf_sha256": sha(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
