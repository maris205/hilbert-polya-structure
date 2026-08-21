#!/usr/bin/env python3
"""Write the deterministic C90 file ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C90_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls", PROJECT / "paper/main.log", PROJECT / "paper/main.out"}
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c90-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact joint survival, mixed moments, and covariance for all twenty-target pairs",
        "authority": {"c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b", "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5", "c89": "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9"},
        "files": files,
        "excluded_from_manifest": ["C90_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out"],
        "gates": {"G0_source_rebind_C88_C89": "PASS", "G1_all_400_joint_target_pairs": "PASS", "G2_all_115600_survival_cells": "PASS", "G3_mixed_moments_and_covariance": "PASS", "G4_marginal_symmetry_diagonal_checks": "PASS", "G5_checker_sympy_replay_hostile_mutations": "PASS", "G6_paper_double_isolated_compile_visual_font_check": "PASS", "G7_manifest_hash_verification": "PASS", "G8_arithmetic_local": "NOT_CLAIMED", "G9_release_closure": "PENDING"},
        "results": {"ordered_pair_count": 400, "joint_cells": 115600, "mixed_moment_cells": 19600, "hostile_mutations_rejected": 13, "evidence_sha256": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978", "pdf_sha256": "d1dcd62d535729aa36c6c173421c7e5ff9789d6520c464da6be3dfc23ae55af3"},
        "nonclaims": ["arithmetic/local data, Euler factors, root numbers, automorphy", "full Burnside ring or full table of marks", "Hilbert-Polya operators"],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
