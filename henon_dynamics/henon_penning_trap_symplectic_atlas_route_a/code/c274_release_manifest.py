#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C274 release."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C274_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c274_penning_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C274/2026-09-01.yaml"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
EVIDENCE_SHA = "d926343f30716cf64888052c2034055ad352e50e59616dddb9a599d3e5c1ddca"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "ff97af92b8e5eb9c75ac232176f733bddeaf2e3c45c9b5861d970fda67c440c2",
    "4624322756d44a9db0a26ef23b2a7c55f797dd62c1dce2deb4a1d979b226fada",
    "960afb3c5ec99cbd320a033c72affbc3cde357b0fe4b4cee6c741de773df9d42",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c274_penning_checker.py", "code/c274_penning_mutation.py",
    "code/c274_penning_producer.py", "code/c274_penning_replay.py",
    "code/c274_penning_sympy_crosscheck.py", "code/c274_release_manifest.py",
    "evaluations/route_a/HCS-C274/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c274_penning_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def is_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True
    )


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [
        line for line in output.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c274-r{round_number}-") as temp:
        work = Path(temp)
        env = dict(os.environ)
        env.update({
            "SOURCE_DATE_EPOCH": str(EPOCH),
            "FORCE_SOURCE_DATE": "1",
            "TZ": "UTC",
        })
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(
                command, cwd=work, env=env, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
        log = (work / "main.log").read_text(errors="replace")
        assert not WARNING_RE.search(log)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["schema"] == "hcs-c274-penning-symplectic-atlas-v1"
    assert data["candidate_id"] == "HCS-C274" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-01" and data["fixed_epoch"] == EPOCH
    assert data["evaluator"]["sha256"] == EVAL and data["scope_literal"] == SCOPE
    assert data["payload_sha256"] == payload_hash(data)
    assert data["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert data["proof_contract"]["scope"] == (
        "ideal axially symmetric trap only; no imperfections, damping, many-body effects, or experimental accuracy claim"
    )
    assert data["flow_contract"]["dimension"] == 6
    assert data["model_contract"]["delta"] == "Delta=c^2-2*zeta^2"
    assert data["mode_contract"]["krein_signs"] == [
        "positive modified-cyclotron", "negative magnetron", "positive axial"
    ]
    assert data["orbit_contract"]["closed_orbit_gate"] == (
        "a nonstationary stable-chamber orbit is closed iff its active labeled modes in "
        "(omega_+,omega_-,zeta) are rationally commensurate"
    )
    assert data["orbit_contract"]["stable_strobe_fixed_dimension"] == (
        "with labeled (f1,f2,f3)=(omega_+,omega_-,zeta), including coincident values, "
        "dim Fix M(t)=2*#{j: f_j*t in 2*pi*Z}"
    )
    assert data["route_a"] == {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False
    }
    assert all(value is False for value in data["scope_flags"].values())
    counts = data["regression"]["counts"]
    assert counts == {
        "flow_rows": 48, "flow_matrix_cells": 1728, "mode_rows": 24,
        "strobe_rows": 13, "period_rows": 7, "boundary_rows": 9, "numeric_cells": 2743,
    }

    yaml_text = YAML.read_text()
    for token in (
        "candidate_id: HCS-C274", f"source_commit: {SOURCE}", f"fixed_epoch: {EPOCH}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVAL}",
        "A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
    ):
        assert token in yaml_text, token
    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free", "embedded and subset"):
        assert token in compile_report, token
    tex_text = " ".join(TEX.read_text().split())
    for token in (
        r"\cite{BrownGabrielse1982}", r"\cite{BrownGabrielse1986}",
        "ideal-trap Hamiltonian and frequency normalization as model lineage",
        "no displayed formula or proof step is outsourced",
        "modified-cyclotron and magnetron labels follow",
        "the amplitudes, signed normal form, and Krein conclusion below are derived locally",
    ):
        assert token in tex_text, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [3, 3, 4] and pdf_pages(PDF) == 4
    all_font_rows = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(
            len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes"
            for row in rows
        )
        all_font_rows.append(len(rows))

    final_text = " ".join(
        subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower().split()
    )
    for token in (
        "exact six-dimensional symplectic flow", "magnetic-confinement threshold",
        "negative magnetron", "critical jordan", "active-mode resonance", "strobe fixed",
        "provable as stated", "a1_weak", "a4_natural_quantization", "route_a_rejected",
        SCOPE.lower(), "brown and gabrielse [1]", "brown and gabrielse [2]",
        "no displayed formula or proof step is outsourced",
        "modified-cyclotron and magnetron labels follow",
        "10.1103/physreva.25.2423", "10.1103/revmodphys.58.233",
    ):
        assert token in final_text, token

    fresh_hashes: list[list[str]] = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        build_one, _ = fresh_build(round_number)
        build_two, _ = fresh_build(round_number)
        assert build_one == build_two == archive.read_bytes()
        fresh_hashes.append([
            hashlib.sha256(build_one).hexdigest(), hashlib.sha256(build_two).hexdigest()
        ])
        assert fresh_hashes[-1] == [expected_hash, expected_hash]

    producer = run_python("c274_penning_producer.py")
    checker = run_python("c274_penning_checker.py")
    sympy = run_python("c274_penning_sympy_crosscheck.py")
    replay = run_python("c274_penning_replay.py")
    mutation = run_python("c274_penning_mutation.py")
    assert "C274_PRODUCER_PASS" in producer
    assert "C274 independent checker: PASS" in checker
    assert "C274_SYMPY_PASS" in sympy and "C274 byte replay: PASS" in replay
    checker_match = re.search(r"PASS \((\d+) assertions", checker)
    sympy_match = re.search(r"PASS \((\d+) symbolic", sympy)
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert checker_match and int(checker_match.group(1)) == 3664
    assert sympy_match and int(sympy_match.group(1)) == 96
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2) == "26"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c274-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C274",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "theorem_status": data["proof_contract"]["status"],
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_exact_six_dimensional_flow": "PASS",
            "G2_symplectic_energy_semigroup": "PASS",
            "G3_full_stability_jordan_instability_atlas": "PASS",
            "G4_signed_actions_krein": "PASS",
            "G5_boundaries_and_sign_reversal": "PASS",
            "G6_active_resonance_period_strobe": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_deterministic_pdf_fonts_log": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_claim_local_source_traceability": "PASS",
            "G12_imperfect_trap_extension": "NOT_CLAIMED",
            "G13_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **counts,
            "checker_assertions": int(checker_match.group(1)),
            "sympy_checks": int(sympy_match.group(1)),
            "hostile_rejections": int(mutation_match.group(1)),
            "pdf_pages": 4,
            "round_pdf_pages": page_counts,
            "embedded_subset_font_rows": all_font_rows,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": digest(PDF),
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C274_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C274_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
