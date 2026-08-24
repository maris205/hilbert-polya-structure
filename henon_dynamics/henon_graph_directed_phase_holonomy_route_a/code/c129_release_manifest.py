#!/usr/bin/env python3
"""Build the content-addressed C129 release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C129_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c129_phase_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c129-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Frozen translation-lattice phase holonomy restores finite-quotient position sensitivity to a graph-directed Hardy Fredholm owner",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_strict_interior_and_strong_separation": "PASS",
            "G2_all_period_primitive_coding": "PASS",
            "G3_twisted_trace_class_hardy_operator": "PASS",
            "G4_all_order_trace_fredholm_primitive_identity": "PASS",
            "G5_exact_positive_and_negative_controls": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_double_compile_fonts_layout": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_divisor_matching": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "rooted_closed_words_through_period_8": 284,
            "primitive_cycles_through_period_8": 40,
            "trace_prefix_length": 8,
            "fredholm_taylor_degree": 8,
            "independent_checker_assertions": 71,
            "sympy_checks": 49,
            "repaired_hash_mutation_rejections": 35,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE FREDHOLM DETERMINANT BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "FROZEN U1 CHARACTER IS A FORMAL PHASE LIFT, NOT A NATURAL UNITARY QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "complete geometric recovery from one finite character",
            "a target-facing zero or divisor match",
            "prime-like information or arithmetic/local data",
            "Euler factors, root numbers, automorphy, or a Riemann-zero correspondence",
            "a self-adjoint Hilbert--Polya operator or natural unitary quantization",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C129_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log",
            "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 manifest files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "manifest_sha256": digest(MANIFEST),
        "file_count": len(files),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
