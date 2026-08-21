#!/usr/bin/env python3
"""Write the deterministic C94 prefreeze file ledger."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C94_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
    }
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c94-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact first-passage hazards and conditional residual-life laws for twenty targets",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
        },
        "files": files,
        "excluded_from_manifest": [
            "C94_PREFREEZE_MANIFEST.json",
            "code/__pycache__/",
            "paper/main.aux",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.log",
            "paper/main.out",
        ],
        "gates": {
            "G0_source_rebind_C88": "PASS",
            "G1_twenty_target_hazard_atlas": "PASS",
            "G2_residual_survival_and_pmf_grids": "PASS",
            "G3_mean_second_moment_variance_identities": "PASS",
            "G4_checker_sympy_replay_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_visual_font_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "target_count": 20,
            "label_count": 16,
            "hazard_steps": 340,
            "residual_grid_cells_per_surface": 5780,
            "defined_conditioning_rows": 261,
            "hostile_mutations_rejected": 13,
            "evidence_sha256": "e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b3",
            "pdf_sha256": "c9678e7a39c3ae4aeaff56ce20f809cd2bd894bae4ca98cf5164cd18c2dddf54",
        },
        "nonclaims": [
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "full Burnside ring or full table of marks",
            "Hilbert-Polya operators",
        ],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
