#!/usr/bin/env python3
"""Write the deterministic C98 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C98_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb"
PDF_SHA = "774fa65062106e611c3d597b56aa4865a341f880263b1431bc4a6661f5820cfb"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c98_conditional_kernel_evidence.json"
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
    excluded_prefix = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or any(str(path).startswith(str(prefix)) for prefix in excluded_prefix):
            continue
        files[str(path.relative_to(PROJECT))] = digest(path)
    result = {
        "schema_id": "hcs-c98-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact conditional first-passage kernels and variance decompositions",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
            "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
            "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
        },
        "files": files,
        "excluded_from_manifest": [
            "C98_PREFREEZE_MANIFEST.json", "../codex_prompt.md", "code/__pycache__/",
            "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls",
            "paper/main.log", "paper/main.out", "paper/main.synctex.gz",
        ],
        "gates": {
            "G0_source_rebind_C88_C90": "PASS",
            "G1_all_400_joint_pmfs_and_marginals": "PASS",
            "G2_all_conditional_bayes_and_tower_identities": "PASS",
            "G3_independent_checker_and_6800_C88_cells": "PASS",
            "G4_sympy_replay_16_hostile_mutations": "PASS",
            "G5_double_isolated_pdf_and_font_audit": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "ordered_pair_count": 400,
            "joint_and_bayes_cell_count": 115600,
            "candidate_conditioning_row_count": 6800,
            "attainable_conditioning_row_count": 4980,
            "empty_conditioning_row_count": 1820,
            "total_expectation_identity_count": 400,
            "total_variance_identity_count": 400,
            "synchronous_c88_cell_crosscheck_count": 6800,
            "hostile_mutations_rejected": 16,
            "pdf_pages": 2,
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": PDF_SHA,
        },
        "nonclaims": [
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "full Burnside ring or full table of marks",
            "Hilbert-Polya operators",
        ],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
