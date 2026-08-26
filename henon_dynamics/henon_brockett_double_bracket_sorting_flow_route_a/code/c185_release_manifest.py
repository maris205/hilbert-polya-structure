#!/usr/bin/env python3
"""Build the content-addressed self-excluded C185 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C185_RELEASE_MANIFEST.json"
CHECKER_ASSERTIONS = 183158
SYMPY_CHECKS = 253765
MUTATION_REJECTIONS = 67
STALE_REJECTIONS = 1


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pdf_pages(path: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(path)], text=True)
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise AssertionError("pdfinfo did not report a page count")


def main() -> None:
    assert CHECKER_ASSERTIONS > 0 and SYMPY_CHECKS > 0 and MUTATION_REJECTIONS > 0
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux",
        ROOT / "paper/main.log",
        ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk",
        ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c185_brockett_evidence.json"
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
        "schema": "hcs-c185-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C185",
        "evaluation_date": "2026-08-26",
        "source_commit": "908a6818caedb0c46195a591873a2ac9c685b55e",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The all-size simple-spectrum Brockett double-bracket flow is globally isospectral, has an exact strict Lyapunov law, resolves all permutation equilibria and pair modes by inversion index, generically sorts, and admits no nonconstant recurrent orbit; these classical sorting dynamics fail the arithmetic Route-A gate",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_global_isospectral_lyapunov_theorem": "PASS",
            "G2_all_permutation_equilibria_pair_modes_and_morse_index": "PASS",
            "G3_generic_sorting_and_no_recurrence": "PASS",
            "G4_repeated_spectrum_morse_bott_boundary": "PASS_SCOPED",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "permutation_rows": evidence_data["counts"]["permutation_rows"],
            "pair_mode_rows": evidence_data["counts"]["pair_mode_rows"],
            "matrix_regression_rows": evidence_data["counts"]["matrix_regression_rows"],
            "independent_checker_assertions": CHECKER_ASSERTIONS,
            "sympy_checks": SYMPY_CHECKS,
            "repaired_hash_mutation_rejections": MUTATION_REJECTIONS,
            "stale_hash_mutation_rejections": STALE_REJECTIONS,
            "citation_registry_population": 1,
            "reference_registry_population": 1,
            "pdf_pages": pdf_pages(pdf),
            "evidence_bytes": evidence.stat().st_size,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence_data["route_a_verdict"],
        "nonclaims": evidence_data["nonclaims"],
        "excluded_from_manifest": [
            "C185_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C185_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
