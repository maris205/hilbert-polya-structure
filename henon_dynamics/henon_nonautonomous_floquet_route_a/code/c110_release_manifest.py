#!/usr/bin/env python3
"""Write the deterministic C110 pre-freeze release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C110_PREFREEZE_MANIFEST.json"


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
    }
    files: dict[str, str] = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = file_hash(path)
    evidence = PROJECT / "results/c110_nonautonomous_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    result = {
        "schema_id": "hcs-c110-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Period-two non-autonomous Hénon chronological Floquet and control-prefix pilot",
        "files": files,
        "excluded_from_manifest": [
            "C110_PREFREEZE_MANIFEST.json", "code/__pycache__/", "paper/main.aux",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.log", "paper/main.out",
        ],
        "gates": {
            "G0_candidate_definition_and_scope_audit": "PASS",
            "G1_admissible_primitive_necklace_enumeration_n_1_to_6": "PASS",
            "G2_chronological_reverse_and_same_control_trace_prefix": "PASS",
            "G3_determinant_newton_crosscheck": "PASS",
            "G4_checker_replay_and_hostile_mutations": "PASS",
            "G5_paper_double_isolated_compile_visual_font_check": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_geometric_henon_coding": "NOT_ESTABLISHED",
            "G8_source_native_fredholm_owner": "NOT_ESTABLISHED",
            "G9_release_closure": "PENDING",
        },
        "results": {
            "primitive_necklaces": 24,
            "primitive_count_by_length": {"1": 3, "2": 0, "3": 2, "4": 4, "5": 6, "6": 9},
            "chronology_sensitive_rows": 17,
            "transfer_dimension": 8,
            "max_block_period": 6,
            "mutation_rejections": 10,
            "evidence_sha256": file_hash(evidence),
            "pdf_pages": 2,
            "pdf_sha256": file_hash(pdf),
        },
        "route_a_assessment": {
            "A1": "A1_WEAK",
            "A2": "A2_CERTIFIED_PREFIX",
            "A1_qualification": "NONAUTONOMOUS_SYMBOLIC_PILOT_ONLY",
            "A2_qualification": "DISCRETE_FLOQUET_TRANSFER_PREFIX_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
        },
        "nonclaims": [
            "complete geometric Hénon coding and periodic-orbit completeness",
            "Fredholm determinant, nuclearity, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert–Pólya operator or Route-B authorization",
        ],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode())
    print(json.dumps({"status": result["status"], "manifest_sha256": file_hash(MANIFEST), "file_count": len(files)}, sort_keys=True))


if __name__ == "__main__":
    main()
