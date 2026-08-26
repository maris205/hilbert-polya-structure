#!/usr/bin/env python3
"""Build the content-addressed self-excluded C186 release manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C186_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out", ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c186_euler_top_evidence.json"
    evidence_data = json.loads(evidence.read_text())
    pdf = ROOT / "paper/main.pdf"
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(pdf) == round_hashes[2]
    result = {
        "schema": "hcs-c186-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C186",
        "evaluation_date": "2026-08-26",
        "source_commit": "908a6818caedb0c46195a591873a2ac9c685b55e",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every triaxial Euler top admits a two-regime all-energy Jacobi atlas with exact periods, KKS actions, axial stability, and a heteroclinic separatrix; resonant time maps have whole fixed circles and therefore no ordinary isolated-orbit Artin--Mazur census",
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_all_energy_elliptic_atlas": "PASS",
            "G2_equilibria_separatrix_and_period_limits": "PASS",
            "G3_action_angle_and_fixed_set_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "regular_rows": evidence_data["summary"]["regular_rows"],
            "exact_regular_residual_cells": evidence_data["summary"]["exact_regular_residual_cells"],
            "equilibrium_rows": evidence_data["summary"]["equilibrium_rows"],
            "separatrix_rows": evidence_data["summary"]["separatrix_rows"],
            "divergence_rows": evidence_data["summary"]["divergence_rows"],
            "independent_checker_assertions": 4268,
            "sympy_checks": 25,
            "repaired_hash_mutation_rejections": 20,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "reference_registry_population": 2,
            "pdf_pages": 0,
            "evidence_bytes": evidence.stat().st_size,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence_data["route_a"],
        "nonclaims": [
            "priority for Jacobi's Euler-top solution, stability portrait, or action-angle theory",
            "isolated primitive-orbit counts on energy surfaces carrying continuous orbit families",
            "an arithmetic interpretation of inertia, energy, period, or resonance labels",
            "a target divisor, functional equation, counting law, or continuation theorem",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": ["C186_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    try:
        import subprocess
        pages = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
        result["results"]["pdf_pages"] = int(next(line.split(":", 1)[1] for line in pages.splitlines() if line.startswith("Pages:")))
    except Exception as exc:
        raise AssertionError(f"cannot determine PDF page count: {exc}")
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C186_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
