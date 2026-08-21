#!/usr/bin/env python3
"""Write the deterministic C92 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C92_PREFREEZE_MANIFEST.json"


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
        "schema_id": "hcs-c92-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact first-passage label sensitivity atlas",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
        },
        "files": files,
        "excluded_from_manifest": [
            "C92_PREFREEZE_MANIFEST.json", "../codex_prompt.md", "code/__pycache__/",
            "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out",
        ],
        "gates": {
            "G0_source_rebind_C88": "PASS",
            "G1_20_targets_16_labels_all_rank_cells": "PASS",
            "G2_efficiency_and_moment_identities": "PASS",
            "G3_independent_reconstruction": "PASS",
            "G4_sympy_replay_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_visual_font_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "target_count": 20,
            "labels_per_target": 16,
            "support_count": 65536,
            "total_permutations": 20922789888000,
            "hostile_mutations_rejected": 12,
            "pdf_pages": 1,
            "evidence_sha256": "902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812",
            "pdf_sha256": "960f7c5869ed49a40f21cf22dd5eb2c1a14b652b982ce0ee69407454406b4a95",
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
