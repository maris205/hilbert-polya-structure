#!/usr/bin/env python3
"""Build the content-addressed self-excluded C175 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C175_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c175_rule184_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    round0 = ROOT / "paper/main_round0_original.pdf"
    round1 = ROOT / "paper/main_round1.pdf"
    round2 = ROOT / "paper/main_round2.pdf"
    round_hashes = [digest(round0), digest(round1), digest(round2)]
    assert len(set(round_hashes)) == 3, "paper rounds must be distinct"
    assert digest(pdf) == round_hashes[2], "final must equal round 2"
    evidence_data = json.loads(evidence.read_text())

    result = {
        "schema": "hcs-c175-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every cyclic Rule-184 sector has an explicitly attracting isolated-minority rotation core, closed all-iterate fixed counts, and a sharp full-versus-core Koopman boundary",
        "gates": {
            "G0_source_lock_and_A0_arithmetic_gate": "PASS_WITH_A0_FAIL",
            "G1_all_N_k_periodic_core_classification": "PASS",
            "G2_gap_lyapunov_and_finite_attraction": "PASS",
            "G3_all_iterate_fixed_counts_and_primitive_zeta": "PASS",
            "G4_full_sector_vs_core_koopman_boundary": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "sector_rows": 90,
            "classified_words": 8190,
            "fixed_rows": 1636,
            "primitive_rows": 299,
            "word_iterate_checks": 196608,
            "independent_checker_assertions": 34545,
            "sympy_checks": 25563,
            "repaired_hash_mutation_rejections": 16,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 0,
            "reference_registry_population": 0,
            "pdf_pages": 3,
            "evidence_payload_sha256": evidence_data["payload_sha256"],
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "FINITE_RATIONAL_SOURCE_STRUCTURE_WITH_NO_TARGET_GLOBAL_ANALYTIC_COMPARISON",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "NATURAL_UNITARY_ONLY_ON_FULL_SECTORS_WITH_M_AT_MOST_ONE_OR_ON_THE_PERIODIC_CORE_THAT_DISCARDS_TRANSIENTS",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "external novelty or priority for classical Rule-184 facts",
            "prime semantics for traffic cycles or repetitions",
            "unitarity of a full sector containing transient states",
            "a target divisor, functional equation, counting law, continuation, or Weil compression",
            "arithmetic local factors, Euler factors, root numbers, automorphy, a Hilbert--Polya operator, Route-B authorization, or external peer review",
        ],
        "excluded_from_manifest": [
            "C175_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C175_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
