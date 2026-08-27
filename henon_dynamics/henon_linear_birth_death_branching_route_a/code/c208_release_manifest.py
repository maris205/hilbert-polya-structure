#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C208 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C208_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c208_branching_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "2be1666222c3cb7dbc407d571f0bc9c3d695b19b54067b105f15a9c02c5b3cf5"
EVIDENCE_SHA256 = "d94b84c4d64799ea2dc9728fc96b8d8eb0f4976fd7d006af7441dd4b00565818"
PDF_SHA256 = "b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325"
PDF_BYTES = 203066
ROUND_HASHES = [
    "a7f06d2a137d4b6081675f674e6121192acfc6b1748ad8d93f8a5f5e8e96008c",
    "150e6f0ccded222b2430a534bd7ad56dc2bf7ba6d52998d88a260a798c6ccbb4",
    "b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325",
]
CHECKER_ASSERTIONS = 2194
SYMPY_CHECKS = 1009
HOSTILE_REJECTIONS = 23

EXPECTED_PAYLOADS = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c208_branching_checker.py", "code/c208_branching_mutation.py",
    "code/c208_branching_producer.py", "code/c208_branching_replay.py",
    "code/c208_branching_sympy_crosscheck.py", "code/c208_release_manifest.py",
    "evaluations/route_a/HCS-C208/2026-08-27.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c208_branching_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
            or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert digest(PDF) == PDF_SHA256 and PDF.stat().st_size == PDF_BYTES
    assert evidence["summary"]["exact_scalar_identity_count"] == 1232
    assert evidence["summary"]["transition_probability_count"] == 845
    assert evidence["summary"]["survivor_weight_count"] == 195
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["theorem"]["mixture_warning"].startswith("the all-parameter family is a binomial-survivor mixture")
    assert evidence["theorem"]["subcritical_qsd_invariance"] == (
        "for rho=lambda/mu and g(s)=(1-rho)s/(1-rho*s), "
        "[g(F_t(s))-g(F_t(0))]/[1-g(F_t(0))]=g(s)"
    )
    assert evidence["asymptotics"]["supercritical_atom_at_zero"] == "(mu/lambda)^z"
    assert evidence["citations"][0]["report_number"] == "KAR ONR 3"

    physical_before = [path for path in ROOT.rglob("*") if path.is_file()]
    sidecars = [str(path.relative_to(ROOT)) for path in physical_before if is_sidecar(path)]
    assert not sidecars, f"unexpected sidecars: {sidecars}"
    files = {}
    for path in sorted(physical_before):
        if path == MANIFEST:
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    assert set(files) == EXPECTED_PAYLOADS, (
        f"payload path mismatch; missing={sorted(EXPECTED_PAYLOADS - set(files))}; "
        f"extra={sorted(set(files) - EXPECTED_PAYLOADS)}"
    )

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
              ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert pages == 4
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert len(font_lines) == 24
    for line in font_lines:
        fields = line.split()
        assert fields[-5:-3] == ["yes", "yes"], f"font not embedded/subset: {line}"
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ["survivor mixture", "genuinely quasi-stationary", "critical Yaglom scaling",
                   "Gamma", "ROUTE_A_REJECTED", "NO_BAD_EULER_OR_ROOT_NUMBER", "KAR ONR 3"]:
        assert phrase in extracted, f"missing extracted phrase: {phrase}"

    result = {
        "schema": "hcs-c208-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C208",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_lock_clock_scope": "PASS",
            "G1_all_rate_mobius_semigroup": "PASS",
            "G2_survivor_mixture_transitions_moments_boundaries": "PASS",
            "G3_three_regime_limits_atom_initial_population": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_improvements_reproducible_pdf_visual": "PASS",
            "G6_manifest_exact_path_hash_closure": "PASS",
            "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_cases": evidence["summary"]["parameter_case_count"],
            "semigroup_cases": evidence["summary"]["semigroup_case_count"],
            "exact_scalar_identities": evidence["summary"]["exact_scalar_identity_count"],
            "checker_assertions": CHECKER_ASSERTIONS,
            "sympy_checks": SYMPY_CHECKS,
            "hostile_rejections": HOSTILE_REJECTIONS,
            "pdf_pages": pages,
            "embedded_subset_fonts": len(font_lines),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C208_RELEASE_MANIFEST.json"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [path for path in ROOT.rglob("*") if path.is_file()]
    assert len(physical_after) == 28, f"expected 28 physical files, found {len(physical_after)}"
    print(json.dumps({
        "status": "C208_MANIFEST_PASS",
        "payload_file_count": len(files),
        "physical_file_count": len(physical_after),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
