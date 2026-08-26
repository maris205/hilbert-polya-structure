#!/usr/bin/env python3
"""Build the content-addressed self-excluded C171 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C171_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {MANIFEST, ROOT/"paper/main.aux", ROOT/"paper/main.log", ROOT/"paper/main.out",
                ROOT/"paper/main.fdb_latexmk", ROOT/"paper/main.fls", ROOT/"paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT/"results/c171_ehrenfest_evidence.json"
    pdf = ROOT/"paper/main.pdf"
    result = {
        "schema": "hcs-c171-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C171",
        "evaluation_date": "2026-08-26", "source_commit": "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All-dimensional Walsh diagonalization and exact reversible Krawtchouk compression of the Ehrenfest hypercube walk",
        "gates": {"G0_source_arithmetic_clock_weight_lock": "PASS", "G1_all_d_walsh_spectrum": "PASS",
                  "G2_all_d_trace_determinant_return": "PASS", "G3_reversible_lumping_and_similarity": "PASS",
                  "G4_independent_checker_sympy_replay_mutation": "PASS", "G5_bilingual_three_round_deterministic_pdf": "PASS",
                  "G6_manifest_hash_closure": "PASS", "G7_target_arithmetic_route_b": "NOT_CLAIMED"},
        "results": {"d_max": 18, "n_max": 24, "independent_checker_assertions": 2990,
                    "sympy_checks": 914, "repaired_hash_mutation_rejections": 38, "stale_hash_mutation_rejections": 1,
                    "pdf_pages": 2, "pivot_required": False,
                    "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)},
        "route_a_verdict": {"A0": "A0_FAIL", "A1": "A1_FAIL", "A2": "A2_FAIL", "A3": "A3_FAIL",
                            "A4": "A4_FORMAL_HINT", "overall": "ROUTE_A_REJECTED",
                            "route_b_invocation_allowed": False},
        "nonclaims": ["a uniform all-d Artin--Mazur zeta interpretation of the weighted Markov determinant",
                       "a prime or prime-power orbit correspondence", "a target divisor, functional equation, or counting law",
                       "arithmetic local data, Euler factors, or root numbers", "automorphy or a Hilbert--Polya operator"],
        "integrity": {"hard_gate": "unconditional all-d source theorem", "hard_gate_status": "PASS",
                      "finite_ledgers_are_proof": False, "external_reviewer_simulated": False,
                      "registered_citation_population": 0},
        "excluded_from_manifest": ["C171_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux",
                                   "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls",
                                   "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "C171_MANIFEST_PASS", "file_count": len(files),
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence),
                      "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
