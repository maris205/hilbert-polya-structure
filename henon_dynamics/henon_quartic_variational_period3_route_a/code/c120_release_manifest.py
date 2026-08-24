#!/usr/bin/env python3
"""Write the closed C120 release manifest after all artifacts exist."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C120_PREFREEZE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        "C120_PREFREEZE_MANIFEST.json",
        "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fls",
        "paper/main.fdb_latexmk", "paper/main.synctex.gz",
    }
    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        relative = str(path.relative_to(ROOT))
        if path.is_file() and "__pycache__" not in path.parts and relative not in excluded:
            files[relative] = digest(path)
    evidence = ROOT / "results/c120_variational_period3_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    data = {
        "schema_id": "hcs-c120-quartic-variational-period3-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "An exact quartic variational primitive period-three and Morse certificate",
        "files": files,
        "excluded_from_manifest": sorted(excluded) + ["code/__pycache__/"],
        "results": {
            "fixed_count": 3,
            "period_three_count": 1,
            "mutation_rejections": 21,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf) if pdf.exists() else "",
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "gates": {
            "G0_model_freeze": "PASS",
            "G1_area_preserving_reversible_generating_identity": "PASS",
            "G2_exact_period_three_action_morse_certificate": "PASS",
            "G3_independent_symbolic_replay_mutation": "PASS",
            "G4_pdf_determinism_fonts_layout": "PASS",
            "G5_manifest_hash_closure": "PASS",
            "G6_complete_orbit_atlas": "NOT_ESTABLISHED",
            "G7_transfer_owner": "NOT_ESTABLISHED",
            "G7a_target_prime_correspondence": "NOT_ESTABLISHED",
            "G7b_target_divisor": "NOT_ESTABLISHED",
            "G8_arithmetic_route_b": "NOT_CLAIMED",
        },
        "nonclaims": [
            "complete primitive-orbit atlas or global variational classification",
            "target prime correspondence, log-prime clock, or target divisor",
            "transfer/Fredholm/nuclear operator owner",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator or Route-B authorization",
        ],
    }
    MANIFEST.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "manifest_sha256": digest(MANIFEST),
        "file_count": len(files),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf) if pdf.exists() else "",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
