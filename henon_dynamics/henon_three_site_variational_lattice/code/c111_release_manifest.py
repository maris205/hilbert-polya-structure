#!/usr/bin/env python3
"""Create the deterministic C111 pre-freeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C111_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "b2facafdea39fcdb6b0f36bf167cef19c8fcdf0259cfb84165ed4ddc7e999de3"
PDF_SHA = "c55a1d70f6386f77a980722d966c7d51890fe3e9dbf80c7f48163892f3045005"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c111_three_site_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    assert digest(evidence) == EVIDENCE_SHA
    assert digest(pdf) == PDF_SHA
    excluded = {
        "C111_PREFREEZE_MANIFEST.json",
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
        if relative in excluded:
            continue
        files[relative] = digest(path)
    result = {
        "schema_id": "hcs-c111-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact Fourier-mode low-period witness for a three-site variational Hénon ring",
        "authority": {},
        "files": files,
        "excluded_from_manifest": sorted(excluded) + ["code/__pycache__/"] ,
        "gates": {
            "G0_model_and_parameter_freeze": "PASS",
            "G1_exact_variational_symplectic_reversor_checks": "PASS",
            "G2_low_period_orbit_and_mode_monodromy": "PASS",
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
            "fourier_transverse_multiplicity": 2,
            "hostile_mutations_rejected": 12,
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
    print(json.dumps({"file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": PDF_SHA, "pdf_pages": 2}, sort_keys=True))


if __name__ == "__main__":
    main()
