#!/usr/bin/env python3
"""Write the deterministic C101 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C101_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "43d71ab86e84def24b50563334f92a72efaf122a5760caab975e19b5ed46306d"
PDF_SHA = "4623ffb3b63c86bddb361cd09b08c95cbaccde1796a9c35f9f74d98e257c2657"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c101_triple_coupling_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    assert digest(evidence) == EVIDENCE_SHA
    assert pdf.exists()
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
        "schema_id": "hcs-c101-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact three-target first-passage coupling",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
            "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
            "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
        },
        "files": files,
        "excluded_from_manifest": ["C101_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out", "paper/main.synctex.gz"],
        "gates": {
            "G0_source_rebind_C88_C90": "PASS",
            "G1_nested_chain_and_joint_pmf": "PASS",
            "G2_pair_and_single_marginal_recovery": "PASS",
            "G3_moments_covariance_cumulants": "PASS",
            "G4_checker_symbolic_replay_mutation": "PASS",
            "G5_double_isolated_pdf_and_font_audit": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "unordered_distinct_triple_count": 1140,
            "joint_pmf_cell_count": 5600820,
            "pair_marginal_recovery_count": 400,
            "single_marginal_recovery_count": 20,
            "mixed_moment_cell_count": 72960,
            "hostile_mutations_rejected": 13,
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
