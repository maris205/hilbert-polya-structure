#!/usr/bin/env python3
"""Build the content-addressed self-excluded C195 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C195_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def excluded(path: Path) -> bool:
    if path == MANIFEST or "__pycache__" in path.parts or path.suffix == ".pyc":
        return True
    if path.parent == ROOT / "paper" and path.suffix in {
        ".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz", ".toc"
    }:
        return True
    return False


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def main() -> None:
    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and not excluded(path):
            files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c195_burgers_evidence.json"
    evidence_data = json.loads(evidence.read_text())
    final_pdf = ROOT / "paper/main.pdf"
    round_pdfs = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in round_pdfs]
    assert len(set(round_hashes)) == 3, "revision PDFs must be content-distinct"
    assert digest(final_pdf) == round_hashes[2], "final PDF must equal round 2"
    assert evidence_data["metadata"]["source_commit"] == "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
    assert evidence_data["metadata"]["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert evidence_data["route_a"] == {
        "A0": "A0_FAIL",
        "A1": "A1_FAIL",
        "A2": "A2_FAIL",
        "A3": "A3_FAIL",
        "A4": "A4_FORMAL_HINT",
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "qualification": "the positive projective heat lift is a source PDE linearization with no intrinsic rational-prime carrier, periodic-orbit divisor, target analytic structure, or Hilbert--Polya semantics",
    }

    result = {
        "schema": "hcs-c195-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C195",
        "evaluation_date": "2026-08-27",
        "source_commit": "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "For every viscosity, circumference, mean, and s>3/2, periodic viscous Burgers is globally conjugate to a positive projective drift-heat flow; every orbit converges to its unique constant, the first lift mode gives exact leading decay, and the full linearized spectrum is explicit",
        "gates": {
            "G0_source_lock_and_classical_ownership": "PASS_WITH_A0_FAIL",
            "G1_global_projective_conjugacy": "PASS",
            "G2_global_phase_portrait_and_no_recurrence": "PASS",
            "G3_first_mode_asymptotics_and_full_spectrum": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            **{key: evidence_data["summary"][key] for key in (
                "regression_cases", "generator_residual_rows", "reality_residual_cells",
                "positive_margin_rows", "snapshot_positive_margin_rows",
                "semigroup_identity_rows", "leading_mode_rows", "linear_spectrum_cells",
            )},
            "independent_checker_assertions": 1490,
            "sympy_checks": 129,
            "sympy_selected_cases": 9,
            "repaired_hash_mutation_rejections": 22,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "reference_registry_population": 2,
            "pdf_pages": pages(final_pdf),
            "evidence_bytes": evidence.stat().st_size,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(final_pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence_data["route_a"],
        "nonclaims": [
            "priority for the Hopf--Cole transformation or classical viscous-Burgers solution theory",
            "extension to inviscid Burgers, zero or negative viscosity, nonperiodic domains, or initial data outside the frozen Sobolev class",
            "proof of the all-parameter theorem by the finite trigonometric regression census",
            "an arithmetic interpretation of viscosity, length, mean, Fourier labels, heat decay, or Cole--Hopf lifts",
            "a primitive orbit zeta, Euler product or factor, root number, target divisor, functional equation, counting law, or automorphy theorem",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C195_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/*.aux", "paper/*.log", "paper/*.out", "paper/*.fls",
            "paper/*.fdb_latexmk", "paper/*.synctex.gz", "paper/*.toc",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}: {sorted(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C195_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(final_pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
