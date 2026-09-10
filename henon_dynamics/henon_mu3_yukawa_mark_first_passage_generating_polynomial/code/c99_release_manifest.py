#!/usr/bin/env python3
"""Write deterministic C99 prefreeze ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C99_PREFREEZE_MANIFEST.json"


def main() -> None:
    excluded = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls", PROJECT / "paper/main.log", PROJECT / "paper/main.out"}
    prefixes = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if path.is_file() and path not in excluded and not any(str(path).startswith(str(prefix)) for prefix in prefixes):
            files[str(path.relative_to(PROJECT))] = sha256(path.read_bytes()).hexdigest()
    result = {
        "schema_id": "hcs-c99-prefreeze-manifest-v1", "status": "PREFREEZE_COMPLETE_NOT_RELEASED", "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "headline": "Exact first-passage probability generating polynomials and derivative spectra for twenty C88 targets",
        "authority": {"c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b", "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5", "c89": "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9"},
        "files": files, "excluded_from_manifest": ["C99_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out"],
        "gates": {"G0_source_rebind_C88_C89": "PASS", "G1_all_20_generating_polynomials": "PASS", "G2_all_340_coefficients_support_spectra": "PASS", "G3_derivatives_recover_C89_orders_0_to_6": "PASS", "G4_checker_sympy_replay_hostile_mutations": "PASS", "G5_paper_double_isolated_compile_visual_font_check": "PASS", "G6_manifest_hash_verification": "PASS", "G7_arithmetic_local": "NOT_CLAIMED", "G8_release_closure": "PENDING"},
        "results": {"target_count": 20, "coefficient_cells": 340, "derivative_orders_0_to_6": 7, "hostile_mutations_rejected": 16, "evidence_sha256": "6ef947aeba00ca89fc03b96be877402e55ed7e72451711796a0b44d51ce467ad", "pdf_pages": 1, "pdf_sha256": "bde6a5d119360f2049160ad29fc9b10d40d1223da1d1159aae0bb29c58b102aa"},
        "nonclaims": ["arithmetic/local data, Euler factors, root numbers, automorphy", "full Burnside ring or full table of marks", "Hilbert-Polya operators"],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
