#!/usr/bin/env python3
"""Create the content-addressed C123 manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C123_PREFREEZE_MANIFEST.json"


def h(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {"C123_PREFREEZE_MANIFEST.json", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fls", "paper/main.fdb_latexmk", "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        rel = str(path.relative_to(ROOT))
        if path.is_file() and "__pycache__" not in path.parts and rel not in excluded:
            files[rel] = h(path)
    evidence = ROOT / "results" / "c123_noise_evidence.json"
    pdf = ROOT / "paper" / "main.pdf"
    payload = {
        "schema_id": "hcs-c123-additive-noise-henon-moment-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact periodic-noise words and a degree-four Markov moment operator for an additive-noise Hénon contraction",
        "files": files,
        "excluded_from_manifest": sorted(excluded) + ["code/__pycache__/"],
        "results": {"max_period": 6, "primitive_necklaces": 23, "markov_dimension": 15, "mutation_rejections": 19, "pdf_pages": 2, "evidence_sha256": h(evidence), "pdf_sha256": h(pdf)},
        "route_a_verdict": {"A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL", "A4": "A4_FAIL", "overall": "ROUTE_A_EXPLORATORY"},
        "gates": {"G0_model_freeze": "PASS", "G1_periodic_word_prefix": "PASS", "G2_degree_four_markov_moments": "PASS", "G3_independent_symbolic_replay_mutation": "PASS", "G4_pdf_determinism_fonts_layout": "PASS", "G5_manifest_hash_closure": "PASS", "G6_complete_random_orbit_atlas": "NOT_ESTABLISHED", "G7_global_nuclear_owner": "NOT_ESTABLISHED", "G8_arithmetic_route_b": "NOT_CLAIMED"},
        "nonclaims": ["prime-like target correspondence", "complete random primitive-orbit atlas", "target-divisor match or analytic bridge", "global nuclear/Fredholm transfer owner", "arithmetic/local data, Euler factors, root numbers, or automorphy", "Hilbert--Polya operator or Route-B authorization"],
    }
    MANIFEST.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"manifest_sha256": h(MANIFEST), "file_count": len(files), "evidence_sha256": h(evidence), "pdf_sha256": h(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
