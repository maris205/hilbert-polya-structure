#!/usr/bin/env python3
"""Write the deterministic C93 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C93_PREFREEZE_MANIFEST.json"


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
        "schema_id": "hcs-c93-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Effective-orbit quotient of first-passage laws",
        "authority": {
            "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
            "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
            "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
            "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
            "c92": "902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812",
        },
        "files": files,
        "excluded_from_manifest": [
            "C93_PREFREEZE_MANIFEST.json", "../codex_prompt.md", "code/__pycache__/",
            "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out",
        ],
        "gates": {
            "G0_source_rebind_C75_C76_C88_C92": "PASS",
            "G1_effective_1920_group_rebuild": "PASS",
            "G2_target_orbit_and_generator_equivariance": "PASS",
            "G3_independent_checker": "PASS",
            "G4_sympy_replay_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_visual_font_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "target_count": 20,
            "effective_group_order": 1920,
            "ambient_lifted_group_order": 11520,
            "target_orbit_count": 16,
            "orbit_size_spectrum": {"1": 12, "2": 4},
            "hostile_mutations_rejected": 10,
            "pdf_pages": 1,
            "evidence_sha256": "4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe",
            "pdf_sha256": "956588842f57ec297299fd12c4de52bd37d2d3d9b6a4eaeec9e10f81790bcc20",
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
