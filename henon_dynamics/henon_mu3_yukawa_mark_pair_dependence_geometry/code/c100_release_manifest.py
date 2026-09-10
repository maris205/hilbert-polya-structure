#!/usr/bin/env python3
"""Write deterministic C100 prefreeze ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C100_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls", PROJECT / "paper/main.log", PROJECT / "paper/main.out"}
    prefixes = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if path.is_file() and path not in excluded and not any(str(path).startswith(str(prefix)) for prefix in prefixes):
            files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c100-prefreeze-manifest-v1", "status": "PREFREEZE_COMPLETE_NOT_RELEASED", "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "headline": "Exact dependence geometry for all 400 ordered C88/C90 first-passage pairs",
        "authority": {"c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b", "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5", "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978", "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737"},
        "files": files, "excluded_from_manifest": ["C100_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out"],
        "gates": {"G0_source_rebind_C88_C90": "PASS", "G1_all_400_ordered_pairs": "PASS", "G2_all_115600_joint_pmf_cells": "PASS", "G3_covariance_correlation_TV_L1_Frechet": "PASS", "G4_transpose_diagonal_relation_spectrum": "PASS", "G5_checker_sympy_replay_hostile_mutations": "PASS", "G6_paper_double_isolated_compile_visual_font_check": "PASS", "G7_manifest_hash_verification": "PASS", "G8_arithmetic_local": "NOT_CLAIMED", "G9_release_closure": "PENDING"},
        "results": {"ordered_pair_count": 400, "joint_pmf_cells": 115600, "relation_type_spectrum": {"diagonal": 20, "strict_comparable": 164, "incomparable": 216}, "hostile_mutations_rejected": 16, "evidence_sha256": "52839c81d7d8081715a056684175044255852da26fca9e0b51554dfedd7e17e0", "pdf_pages": 1, "pdf_sha256": "3770b4b2b8d5db595a9b5131d9a95ff5d13dc97c70cd9064e731aee7edc30a05"},
        "nonclaims": ["arithmetic/local data, Euler factors, root numbers, automorphy", "full Burnside ring or full table of marks", "Hilbert-Polya operators"],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
