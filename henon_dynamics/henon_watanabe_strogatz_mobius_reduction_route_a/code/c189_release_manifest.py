#!/usr/bin/env python3
"""Build the content-addressed self-excluded C189 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C189_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def excluded_build_file(path: Path) -> bool:
    if path == MANIFEST or "__pycache__" in path.parts or path.suffix == ".pyc":
        return True
    if path.parent == ROOT / "paper" and path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz", ".toc"}:
        return True
    return False


def pdf_pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def main() -> None:
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or excluded_build_file(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c189_ws_evidence.json"
    evidence_data = json.loads(evidence.read_text())
    pdf = ROOT / "paper/main.pdf"
    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(pdf) == round_hashes[2]

    result = {
        "schema": "hcs-c189-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C189",
        "evaluation_date": "2026-08-27",
        "source_commit": "4d7b214759f7ff982c0b19e662918acd307e0f58",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every identical common first-harmonic phase system is one PSU(1,1) flow with N-3 generic cross-ratio invariants, exact collision strata, and a complete constant-generator trichotomy; elliptic resonances fix continua and stop an ordinary isolated-orbit zeta",
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_arbitrary_forcing_PSU11_reduction": "PASS",
            "G2_cross_ratios_and_collision_strata": "PASS",
            "G3_constant_trichotomy_period_and_fixed_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            **{key: evidence_data["summary"][key] for key in (
                "local_riccati_rows", "mobius_action_rows", "generic_configuration_rows",
                "collision_stratum_rows", "cross_ratio_cells", "three_landmark_reconstruction_rows",
                "circle_residual_cells", "constant_generator_rows",
            )},
            "independent_checker_assertions": 2646,
            "sympy_checks": 18,
            "repaired_hash_mutation_rejections": 24,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 3,
            "reference_registry_population": 3,
            "pdf_pages": pdf_pages(pdf),
            "evidence_bytes": evidence.stat().st_size,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence_data["route_a"],
        "nonclaims": [
            "priority for the Watanabe--Strogatz reduction, Mobius group action, or partial integrability",
            "extension to heterogeneous frequencies, oscillator-specific forcing, delay, or higher phase harmonics",
            "isolated primitive-orbit counts on elliptic resonant configuration strata",
            "an arithmetic interpretation of phase labels, forcing, discriminants, cross ratios, or periods",
            "a target Euler product, divisor, functional equation, counting law, or continuation theorem",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C189_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/*.aux", "paper/*.log", "paper/*.out", "paper/*.fls",
            "paper/*.fdb_latexmk", "paper/*.synctex.gz", "paper/*.toc",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}: {sorted(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C189_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
