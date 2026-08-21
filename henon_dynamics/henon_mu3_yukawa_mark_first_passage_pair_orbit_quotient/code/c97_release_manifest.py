#!/usr/bin/env python3
"""Write the deterministic C97 prefreeze file ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C97_PREFREEZE_MANIFEST.json"
EVIDENCE_SHA = "099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696"
PDF_SHA = "7c52b3081c1941b8c18aec7cfce89e2a95f4f85581e6135505061af0260422b1"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    evidence = PROJECT / "results/c97_pair_orbit_quotient_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    assert digest(evidence) == EVIDENCE_SHA
    assert digest(pdf) == PDF_SHA
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
        PROJECT / "paper/main.synctex.gz",
    }
    excluded_prefix = (PROJECT / "code/__pycache__",)
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or any(str(path).startswith(str(prefix)) for prefix in excluded_prefix):
            continue
        files[str(path.relative_to(PROJECT))] = digest(path)
    result = {
        "schema_id": "hcs-c97-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Ordered-pair orbit quotient of exact finite first-passage laws",
        "authority": {
            "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
            "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
            "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
            "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
            "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
            "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
            "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
            "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
            "c93": "4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe",
            "c93_manifest": "a60e0855482e205b0174281c4a20b8f86d2eb9531a3f980cb76d92fcfb77c608",
        },
        "files": files,
        "excluded_from_manifest": [
            "C97_PREFREEZE_MANIFEST.json", "../codex_prompt.md", "code/__pycache__/",
            "paper/main.aux", "paper/main.fdb_latexmk", "paper/main.fls",
            "paper/main.log", "paper/main.out", "paper/main.synctex.gz",
        ],
        "gates": {
            "G0_source_rebind_C75_C76_C88_C90_C93": "PASS",
            "G1_effective_1920_group_and_target_action": "PASS",
            "G2_all_400_pairs_and_C90_transport": "PASS",
            "G3_independent_inclusion_column_checker": "PASS",
            "G4_sympy_replay_14_hostile_mutations": "PASS",
            "G5_double_isolated_pdf_and_font_audit": "PASS",
            "G6_manifest_hash_verification": "PASS",
            "G7_arithmetic_local": "NOT_CLAIMED",
            "G8_release_closure": "PENDING",
        },
        "results": {
            "effective_label_group_order": 1920,
            "ambient_lifted_group_order": 11520,
            "ordered_pair_count": 400,
            "pair_orbit_count": 272,
            "orbit_size_spectrum": {"1": 144, "2": 128},
            "self_transpose_orbit_count": 20,
            "burnside_fixed_ordered_pair_sum": 522240,
            "hostile_mutations_rejected": 14,
            "pdf_pages": 2,
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": PDF_SHA,
        },
        "nonclaims": [
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "full Burnside ring or full table of marks",
            "Hilbert-Polya operators",
        ],
    }
    MANIFEST.write_bytes((json.dumps(result, sort_keys=True, indent=2) + "\n").encode())
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
