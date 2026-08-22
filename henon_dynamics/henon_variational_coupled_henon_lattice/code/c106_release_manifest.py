#!/usr/bin/env python3
"""Create the deterministic C106 file ledger after all artifacts are frozen."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C106_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "3c3c512f021a8bb4ba094ed8dc14a9635346f566ef404fd6f799dbf7340d1f9b"
PDF_SHA = "73eccfff0ada7eafe1a96caac809faad1a70845bb719f2d558a76634ce9a0d2f"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c106_variational_lattice_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    assert digest(evidence) == EVIDENCE_SHA
    assert digest(pdf) == PDF_SHA
    excluded_names = {
        "C106_PREFREEZE_MANIFEST.json",
        "paper/main.aux",
        "paper/main.fdb_latexmk",
        "paper/main.fls",
        "paper/main.log",
        "paper/main.out",
        "paper/main.synctex.gz",
    }
    files: dict[str, str] = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = str(path.relative_to(PROJECT))
        if relative in excluded_names:
            continue
        files[relative] = digest(path)
    result = {
        "schema_id": "hcs-c106-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact low-period coupling witness for a variational two-site Hénon lattice",
        "authority": {},
        "files": files,
        "excluded_from_manifest": sorted(excluded_names) + ["code/__pycache__/"] ,
        "gates": {
            "G0_model_and_parameter_freeze": "PASS",
            "G1_exact_variational_symplectic_reversor_checks": "PASS",
            "G2_low_period_orbit_and_monodromy": "PASS",
            "G3_independent_checker_symbolic_replay_mutation": "PASS",
            "G4_double_isolated_pdf_and_font_audit": "PASS",
            "G5_manifest_hash_verification": "PASS",
            "G6_A1_complete_primitive_orbit_atlas": "NOT_CLAIMED",
            "G7_A2_fredholm_operator_owner": "NOT_ESTABLISHED",
            "G8_arithmetic_local": "NOT_CLAIMED",
            "G9_release_closure": "PENDING",
        },
        "results": {
            "fixed_point_witness_count": 2,
            "period_two_witness_count": 1,
            "hostile_mutations_rejected": 11,
            "pdf_pages": 2,
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": PDF_SHA,
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "PARTIAL_CERTIFIED_LOW_PERIOD_ONLY",
            "A2": "A2_FAIL",
            "A2_qualification": "OPERATOR_OWNER_OPEN",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "complete primitive-orbit atlas or global Markov partition",
            "Fredholm determinant, trace formula, analytic continuation, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert–Pólya operator or Riemann-zero correspondence",
        ],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode())
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
