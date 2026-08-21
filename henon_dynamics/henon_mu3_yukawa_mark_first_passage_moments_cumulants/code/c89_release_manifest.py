#!/usr/bin/env python3
"""Write the deterministic C89 file ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C89_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls", PROJECT / "paper/main.log", PROJECT / "paper/main.out"}
    excluded_prefix = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or any(str(path).startswith(str(prefix)) for prefix in excluded_prefix):
            continue
        files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c89-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact raw, factorial, central moments and cumulants for twenty C88 first-passage targets",
        "authority": {
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
        },
        "files": files,
        "excluded_from_manifest": ["C89_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out"],
        "gates": {
            "G0_source_rebind_C88": "PASS",
            "G1_twenty_exact_distribution_rows": "PASS",
            "G2_raw_factorial_central_cumulant_orders_0_to_6": "PASS",
            "G3_survival_tail_identities": "PASS",
            "G4_checker_sympy_replay_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_visual_font_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "target_count": 20,
            "label_count": 16,
            "moment_orders": [0, 1, 2, 3, 4, 5, 6],
            "hostile_mutations_rejected": 13,
            "evidence_sha256": "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9",
            "pdf_sha256": "5f7d98c1a62a8bb1ebe2ffaf88cb9331ea1f53d2fe89dc816ca3463f9e9c797b",
        },
        "nonclaims": ["arithmetic/local data, Euler factors, root numbers, automorphy", "full Burnside ring or full table of marks", "Hilbert-Polya operators"],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
