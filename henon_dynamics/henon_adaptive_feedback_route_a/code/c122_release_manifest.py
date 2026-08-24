#!/usr/bin/env python3
"""Create the content-addressed C122 prefreeze manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C122_PREFREEZE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        "C122_PREFREEZE_MANIFEST.json",
        "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fls",
        "paper/main.fdb_latexmk", "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        rel = str(path.relative_to(ROOT))
        if path.is_file() and "__pycache__" not in path.parts and rel not in excluded:
            files[rel] = digest(path)
    evidence = ROOT / "results" / "c122_adaptive_evidence.json"
    pdf = ROOT / "paper" / "main.pdf"
    payload = {
        "schema_id": "hcs-c122-adaptive-feedback-henon-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact adaptive-parameter feedback and low-period monodromy in a three-dimensional Hénon automorphism",
        "files": files,
        "excluded_from_manifest": sorted(excluded) + ["code/__pycache__/"],
        "results": {"fixed_count": 2, "period_two_count": 1, "mutation_rejections": 16, "pdf_pages": 2, "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)},
        "route_a_verdict": {"A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL", "A4": "A4_FAIL", "overall": "ROUTE_A_EXPLORATORY"},
        "gates": {"G0_model_freeze": "PASS", "G1_inverse_and_constant_jacobian": "PASS", "G2_exact_fixed_and_period_two": "PASS", "G3_independent_symbolic_replay_mutation": "PASS", "G4_pdf_determinism_fonts_layout": "PASS", "G5_manifest_hash_closure": "PASS", "G6_complete_orbit_atlas": "NOT_ESTABLISHED", "G7_transfer_owner": "NOT_ESTABLISHED", "G8_arithmetic_route_b": "NOT_CLAIMED"},
        "nonclaims": ["prime-like target correspondence", "complete primitive-orbit atlas", "target-divisor match or analytic bridge", "transfer/Fredholm/nuclear operator owner", "arithmetic/local data, Euler factors, root numbers, or automorphy", "Hilbert--Polya operator or Route-B authorization"],
    }
    MANIFEST.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
