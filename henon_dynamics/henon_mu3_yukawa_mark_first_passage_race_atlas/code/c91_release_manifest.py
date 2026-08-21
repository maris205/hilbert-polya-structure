#!/usr/bin/env python3
"""Write the deterministic C91 prefreeze file ledger."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C91_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
    }
    excluded_prefix = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or any(str(path).startswith(str(prefix)) for prefix in excluded_prefix):
            continue
        files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c91-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact left-first, tie, and right-first laws for all 108 incomparable C88 target pairs",
        "authority": {
            "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
            "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
            "c83": "033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28",
            "c83_manifest": "981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85",
            "c85": "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152",
            "c85_manifest": "d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261",
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
        },
        "files": files,
        "excluded_from_manifest": [
            "C91_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out",
        ],
        "gates": {
            "G0_source_rebind_C75_C83_C85_C88": "PASS",
            "G1_all_108_unordered_incomparable_pairs": "PASS",
            "G2_exact_left_tie_right_boundary_counts": "PASS",
            "G3_every_pair_partitions_16_factorial": "PASS",
            "G4_checker_sympy_replay_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_font_reference_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "target_count": 20,
            "incomparable_pair_count": 108,
            "pairs_with_nonzero_ties": 99,
            "hostile_mutations_rejected": 16,
            "evidence_sha256": "36b0fffda585ea483ba5603101c83c361b85ca4ba9a49c878f1e366d3c13ff0f",
            "pdf_sha256": "468d2f66b2296bd96a05760cc6d70e25e850d94b89c9bafa17fc0040a162b26b",
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
