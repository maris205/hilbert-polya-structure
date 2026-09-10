#!/usr/bin/env python3
"""Write the deterministic C103 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C103_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "b425d9decf5161c0419dadc28e0b60cffbe92fe4fa91e6474a991c3b6e53bfe4"
PDF_SHA = "145251a0f73217698b957819e20b700cd0b7da5ccb8eba884010105c50606737"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c103_minmax_aggregation_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    assert digest(evidence) == EVIDENCE_SHA
    assert digest(pdf) == PDF_SHA
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
        PROJECT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = digest(path)
    result = {
        "schema_id": "hcs-c103-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact minimum and maximum aggregation of first-passage times",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
            "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
            "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
        },
        "files": files,
        "excluded_from_manifest": ["C103_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out", "paper/main.synctex.gz"],
        "gates": {
            "G0_source_rebind_C88_C90": "PASS",
            "G1_joint_pmf_and_aggregation": "PASS",
            "G2_minimum_tail_and_maximum_cdf": "PASS",
            "G3_sum_transpose_and_diagonal": "PASS",
            "G4_checker_symbolic_replay_mutation": "PASS",
            "G5_double_isolated_pdf_and_font_audit": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "ordered_pair_count": 400,
            "joint_pmf_cell_count": 115600,
            "minimum_maximum_cell_count": 13600,
            "minimum_tail_identity_count": 6800,
            "maximum_cdf_identity_count": 6800,
            "sum_identity_count": 400,
            "diagonal_identity_count": 20,
            "hostile_mutations_rejected": 10,
            "pdf_pages": 1,
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": PDF_SHA,
        },
        "nonclaims": ["arithmetic/local data, Euler factors, root numbers, automorphy", "full Burnside ring or full table of marks", "Hilbert-Polya operators"],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
