#!/usr/bin/env python3
"""Build the self-excluded, content-addressed C209 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C209_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c209_kreweras_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def run_json(script: Path) -> dict:
    output = subprocess.check_output([sys.executable, "-B", str(script)], text=True)
    return json.loads(output.strip().splitlines()[-1])


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False

    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    assert all(path.exists() for path in rounds + [PDF])
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[-1]

    producer = run_json(ROOT / "code/c209_kreweras_producer.py")
    checker = run_json(ROOT / "code/c209_kreweras_checker.py")
    sympy = run_json(ROOT / "code/c209_sympy_crosscheck.py")
    replay = run_json(ROOT / "code/c209_replay.py")
    mutation = run_json(ROOT / "code/c209_mutation.py")
    assert producer["status"] == "C209_PRODUCER_PASS"
    assert checker["status"] == "C209_CHECK_PASS"
    assert sympy["status"] == "C209_SYMPY_PASS"
    assert replay["status"] == "C209_REPLAY_PASS"
    assert mutation["status"] == "C209_MUTATION_PASS"

    replay = evidence["finite_replay"]
    result = {
        "schema": "hcs-c209-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C209",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": 1787875200,
            "passes_per_round": 2,
            "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
            "final_equals": "paper/main_round2.pdf",
        },
        "headline": "The ordinary Kreweras complement on NC(n) has an attributed all-iterate fixed ledger; finite Mobius inversion closes exact periods, cycles, zeta, Koopman spectrum, rank duality, and reflection reversal with explicit n=1,2 boundaries.",
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_kreweras_structural_identities": "PASS",
            "G2_all_iterate_csp_fixed_ledger": "PASS_WITH_SOURCE_ATTRIBUTION",
            "G3_period_cycle_zeta_spectrum_reversor": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "n_rows": replay["n_row_count"],
            "fixed_rows": replay["fixed_row_count"],
            "period_rows": replay["period_row_count"],
            "spectral_rows": replay["spectral_row_count"],
            "rank_rows": replay["rank_row_count"],
            "q_catalan_rows": replay["q_catalan_row_count"],
            "structural_rows": replay["structural_row_count"],
            "direct_enumeration_n_max": replay["direct_enumeration_n_max"],
            "direct_enumerated_partitions": sum(row["catalan"] for row in replay["n_rows"] if row["direct_enumeration_selected"]),
            "independent_checker_assertions": checker["assertions"],
            "sympy_checks": sympy["checks"],
            "repaired_hash_mutation_rejections": mutation["repaired_hash_rejections"],
            "stale_hash_mutation_rejections": mutation["stale_hash_rejections"],
            "citation_registry_population": len(evidence["source_registry"]),
            "pdf_pages": pdf_pages(PDF),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C209_RELEASE_MANIFEST.json",
            "code/__pycache__/", "*.pyc", "paper/*.aux", "paper/*.log", "paper/*.out",
            "paper/*.fdb_latexmk", "paper/*.fls", "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C209_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
