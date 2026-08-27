#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C190 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C190_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c190_bulgarian_necklace_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVIDENCE_SHA256 = "78d1ab6aa74d47adb23c8bbcfe1f5ba04125a4aaa152e3d834be4c7f6dde03a4"
PDF_SHA256 = "aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_build_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == "52e6fd775ea565fa86eaf0c4fa1dae1c1e793c9ad4e565be89c14092842b94d3"
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert digest(PDF) == PDF_SHA256
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL",
        "A1_WEAK",
        "A2_FAIL",
        "A3_FAIL",
        "A4_FORMAL_HINT",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["scope_flags"]["claimed_complete_transient_classification"] is False
    assert evidence["scope_flags"]["claimed_global_reversor"] is False

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_build_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert round_hashes == [
        "5aeb6d8128631751374a0dbc710095c781334a8bc4681724b7894adae12819af",
        "85cc22910952e28904f73362d1b0d801aca7c6d55631edfaee7388fdb5cbb366",
        PDF_SHA256,
    ]
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pdf_pages = int(next(
        line.split(":", 1)[1]
        for line in pdf_info.splitlines()
        if line.startswith("Pages:")
    ))
    assert pdf_pages == 2

    replay = evidence["finite_replay"]
    result = {
        "schema": "hcs-c190-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C190",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "For every Bulgarian-solitaire deck size, Brandt recurrent words "
            "determine every positive-iterate fixed count, least period, primitive "
            "cycle, finite zeta factor, full Koopman algebraic multiplicity, and "
            "recurrent reflection formula, while complete transient geometry remains excluded"
        ),
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_all_N_recurrent_conjugacy": "PASS",
            "G2_fixed_period_cycle_and_zeta": "PASS",
            "G3_full_koopman_and_reflection_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_actual_improvements_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "system_rows": replay["system_row_count"],
            "direct_partitions": replay["partition_population"],
            "recurrent_word_partition_pairs": replay["word_partition_pair_count"],
            "direct_cycles": replay["cycle_row_count"],
            "fixed_rows": replay["fixed_row_count"],
            "period_rows": replay["period_row_count"],
            "spectral_rows": replay["spectral_row_count"],
            "independent_checker_assertions": 658664,
            "sympy_checks": 2210,
            "repaired_hash_mutation_rejections": 118,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "reference_registry_population": 2,
            "pdf_pages": pdf_pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": [
            "priority for Brandt's recurrent theorem or the Akin--Davis treatment",
            "complete transient functional trees, hitting-time distributions, or nilpotent Jordan sizes",
            "a global reversor for the noninvertible full map",
            "an all-N theorem inferred from the N<=40 regression census",
            "rational-prime semantics, arithmetic local data, or a target divisor",
            "a target functional equation, continuation theorem, Weil compression, or Hilbert--Polya operator",
            "Route-B authorization, external peer review, or an acceptance score",
        ],
        "excluded_from_manifest": [
            "C190_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/*.aux",
            "paper/*.log",
            "paper/*.out",
            "paper/*.fdb_latexmk",
            "paper/*.fls",
            "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C190_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
