#!/usr/bin/env python3
"""Full release closure for HCS-C278."""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C278_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c278_camassa_holm_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C278/2026-09-01.yaml"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c278_release_manifest.py",
    "code/c278_camassa_holm_checker.py", "code/c278_camassa_holm_mutation.py",
    "code/c278_camassa_holm_producer.py", "code/c278_camassa_holm_replay.py",
    "code/c278_camassa_holm_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C278/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c278_camassa_holm_evidence.json",
}
MODEL = {
    "equation": "m_t+u m_x+2 u_x m=0, m=u-u_xx",
    "ansatz": "u=sum_{j=1}^2 p_j exp(-|x-q_j|), q_1<q_2",
    "distribution_identity": "(1-partial_x^2)exp(-|x-q|)=2 delta_q",
    "clock": "physical Camassa-Holm time before collision; declared alpha-extension after collision",
    "invariants": "P=p_1+p_2 and E=p_1^2+p_2^2+2p_1p_2 exp(-(q_2-q_1))",
}
PROOF_CONTRACT = {
    "classification": "PROVABLE AS STATED for p_1p_2!=0 inside the two strict ordered chambers, with p_1p_2=0 recorded separately as a degenerate boundary",
    "weak_reduction": "match delta and delta-prime coefficients in the momentum equation",
    "integrability": "two invariants reduce the flow to one separable quadratic equation in y",
    "profile_limit": "with c=(q_1+q_2)/2 and h=(q_2-q_1)/2, finite-time convergence of c and the kernel Lipschitz bound give ||u-P exp(-|.-c|)||_infinity <= (|P|+|p|)h -> 0",
    "global_scope": "no assertion of uniqueness for arbitrary H1 initial data or arbitrary weak continuations",
    "finite_evidence_role": "regression and normalization control only; analytic identities carry the theorem",
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REGRESSION_KEYS = {
    "same_sign_rows", "opposite_sign_rows", "alpha_rows", "boundaries", "counts",
}
SAME_SIGN_ROW_KEYS = {
    "P", "D", "t", "y", "gap", "p", "p1", "p2", "energy", "centre",
    "q1", "q2", "gap_ode_residual", "p_ode_residual",
    "D2_reconstruction_residual",
}
OPPOSITE_SIGN_ROW_KEYS = {
    "P", "D", "time_to_collision", "y", "gap", "p", "p1", "p2",
    "energy", "gap_ode_residual", "p_ode_residual",
    "D2_reconstruction_residual", "gap_quadratic_coefficient", "scaled_gap",
    "scaled_amplitude_difference",
}
ALPHA_ROW_KEYS = {
    "P", "D_minus", "alpha", "energy_minus", "energy_plus", "D_plus_squared",
    "energy_loss", "postcollision_state",
}
COUNTS = {
    "same_sign_rows": 15, "opposite_sign_rows": 12,
    "alpha_rows": 15, "boundary_rows": 4,
}
BOUNDARIES = [
    {"name": "single_peak", "law": "u=p exp(-|x-q_0-pt|), E=P^2=p^2"},
    {"name": "zero_total_momentum", "law": "P=0 remains in the signed collision chamber when E>0"},
    {"name": "zero_field", "law": "P=E=0 gives u=0"},
    {"name": "coincident_pair", "law": "q=0 is an extended collision state, not an ordered pre-collision chart point"},
]
REFERENCES = [
    {
        "id": "CamassaHolm1993",
        "title": "An integrable shallow water equation with peaked solitons",
        "authors": "Roberto Camassa and Darryl D. Holm",
        "venue": "Physical Review Letters 71(11) (1993), 1661-1664",
        "doi": "10.1103/PhysRevLett.71.1661",
        "url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.71.1661",
    },
    {
        "id": "GrunertHolden2016",
        "title": "The general peakon-antipeakon solution for the Camassa-Holm equation",
        "authors": "Katrin Grunert and Helge Holden",
        "venue": "Journal of Hyperbolic Differential Equations 13 (2016), 353-380",
        "doi": "10.1142/S0219891616500119",
        "url": "https://arxiv.org/abs/1502.07686",
    },
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run(name: str) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=environment, text=True)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C278"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVALUATOR
    assert data["payload_sha256"] == payload_hash(data)
    assert data["model"] == MODEL
    assert data["proof_contract"] == PROOF_CONTRACT
    assert data["route_a"]["tuple"] == TUPLE
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert data["scope_flags"] == SCOPE_FLAGS
    regression = data["regression"]
    assert set(regression) == REGRESSION_KEYS
    assert regression["counts"] == COUNTS
    assert regression["boundaries"] == BOUNDARIES
    assert all(set(row) == SAME_SIGN_ROW_KEYS for row in regression["same_sign_rows"])
    assert all(set(row) == OPPOSITE_SIGN_ROW_KEYS for row in regression["opposite_sign_rows"])
    assert all(set(row) == ALPHA_ROW_KEYS for row in regression["alpha_rows"])
    assert data["references"] == REFERENCES

    yaml = YAML.read_text()
    for literal in (
        "candidate_id: HCS-C278", f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR}",
        "A4_FORMAL_HINT", "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert literal in yaml, literal
    proof = (ROOT / "THEOREM_PACKAGE.md").read_text()
    assert "PROVABLE AS STATED" in proof
    assert "ydot^2=D^2(y-1)(y-P^2/D^2)" in proof
    assert "arbitrary weak-data uniqueness" in proof
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report
    assert "byte-identical" in report and "Final-pass warnings: none" in report

    checker_tree = ast.parse((ROOT / "code/c278_camassa_holm_checker.py").read_text())
    imported = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not [name for name in imported if "producer" in name]

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = [line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    assert fonts
    assert all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes" for line in fonts)
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for literal in (
        "complete signed two-peakon", "invariant scalar reduction",
        "scattering, collision", "declared α extension", "executable receipt",
        "a4_formal_hint", "route_a_rejected", SCOPE.lower(),
    ):
        assert literal in text, literal

    producer = run("c278_camassa_holm_producer.py")
    checker = run("c278_camassa_holm_checker.py")
    sympy = run("c278_camassa_holm_sympy_crosscheck.py")
    replay = run("c278_camassa_holm_replay.py")
    mutation = run("c278_camassa_holm_mutation.py")
    assert "C278_PRODUCER_PASS" in producer
    assert "C278 independent checker: PASS" in checker
    assert "C278_SYMPY_PASS" in sympy
    assert "C278 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2)
    checker_assertions = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    sympy_checks = int(re.search(r"PASS \((\d+) symbolic", sympy).group(1))
    counts = data["regression"]["counts"]

    result = {
        "schema": "hcs-c278-release-v1", "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C278", "evaluation_date": "2026-09-01",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "Complete signed Camassa-Holm two-peakon scattering, collision, and alpha-extension atlas",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS", "G1_distributional_peakon_reduction": "PASS",
            "G2_same_sign_scattering": "PASS", "G3_signed_collision_asymptotics": "PASS",
            "G4_alpha_and_boundary_atlas": "PASS", "G5_checker_sympy_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS", "G7_deterministic_pdf_fonts_log": "PASS",
            "G8_manifest_hash_closure": "PASS", "G9_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **counts, "checker_assertions": checker_assertions, "sympy_checks": sympy_checks,
            "hostile_rejections": int(match.group(1)), "pdf_pages": pages,
            "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C278_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C278_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
