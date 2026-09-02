#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C288 release."""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C288_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c288_delta_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "5a2964874978f390fe5e861c99bcbe902e994e7acc8179bf00ba0054d795833d"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "16c7dd82828c3130602a1ab1d25b91a38c7452c68a4325764a12691d15641eae",
    "5de873c3dbef1500762cf7cdbab0c57cc6667af7bd93eb4335107fc4b1435759",
    "f6d2973ac3523a6b29609820e348f45cddec81135ee36f02d6f6019ad05dae35",
]
ROUND_TEXT = [
    ("the frozen singular hamiltonian", "rank-one resolvent"),
    (
        "spectrum and two-channel scattering",
        "purely absolutely continuous",
        "no embedded point or singular-continuous spectrum",
    ),
    (
        "heat dynamics and the relative trace",
        "strict duplicate-rejecting checker",
        "1,726",
        "30/30",
        SCOPE.lower(),
        "route_a_rejected",
    ),
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c288_delta_checker.py",
    "code/c288_delta_mutation.py", "code/c288_delta_producer.py",
    "code/c288_delta_replay.py", "code/c288_delta_sympy_crosscheck.py",
    "code/c288_release_manifest.py",
    "evaluations/route_a/HCS-C288/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c288_delta_evidence.json",
}
# This deliberately matches warnings, not package-identification lines such
# as "Package: rerunfilecheck".  It is applied to the settled second-pass log.
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TZ"] = "UTC"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=env,
        text=True,
    )


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(
        next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:"))
    )


def font_rows(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [
        line for line in output.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]


def normalized_pdf_text(path: Path) -> str:
    output = subprocess.check_output(["pdftotext", str(path), "-"], text=True)
    return " ".join(output.lower().split())


def fresh_build(round_number: int) -> tuple[bytes, str]:
    """Compile one round with two LuaLaTeX passes in a fresh directory."""
    with tempfile.TemporaryDirectory(prefix=f"c288-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update(
            {
                "SOURCE_DATE_EPOCH": str(EPOCH),
                "FORCE_SOURCE_DATE": "1",
                "TZ": "UTC",
            }
        )
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error",
            "-jobname=main", source,
        ]
        for _ in range(2):
            subprocess.run(
                command,
                cwd=work,
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        log = (work / "main.log").read_text(errors="replace")
        assert WARNING_RE.search(log) is None, WARNING_RE.search(log).group(0)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    producer = run_python("c288_delta_producer.py")
    assert "C288_PRODUCER_PASS" in producer
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c288-delta-point-interaction-v1"
    assert data["candidate_id"] == "HCS-C288"
    assert data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-02"
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["theorem_contract"]["spectrum"] == (
        "[0,infinity) is purely absolutely continuous with no singular-continuous "
        "part; exactly one eigenvalue -alpha^2/4 occurs iff alpha<0"
    )
    assert data["proof_contract"]["heat_inversion"] == (
        "the explicit Laplace identity for the resolvent correction gives the erfc heat term"
    )
    assert data["route_a"] == {
        "tuple": TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    assert all(value is False for value in data["scope_flags"].values())
    assert data["enumeration"] == {
        "alpha_values": ["-4", "-2", "-1", "0", "1", "2", "4"],
        "regular_resolvent_cells": 32,
        "pole_cells": 3,
        "scattering_cells": 28,
        "bound_state_cells": 3,
        "heat_cells": 8,
    }
    assert data["references"][0]["identifier"] == "10.1007/978-3-642-88201-2"

    yaml_text = (ROOT / "evaluations/route_a/HCS-C288/2026-09-02.yaml").read_text()
    for token in (
        f"source_commit: {SOURCE}", f"fixed_epoch: {EPOCH}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR}",
        "tuple: [A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION]",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
    ):
        assert token in yaml_text, token

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED", "rank-one resolvent", "relative trace",
        "singular-continuous spectrum", "L_t->s", "A4_NATURAL_QUANTIZATION",
    ):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    assert "10.1007/978-3-642-88201-2" in source_audit
    assert "not literature-level originality" in source_audit
    tex = " ".join(TEX.read_text().split())
    for token in (
        "Rank-one resolvent", "Complete sign atlas", "singular-continuous spectrum",
        r"\mathcal L_{t\to s}", "Heat kernel and trace defect",
        "strict duplicate-rejecting checker", "not a priority claim",
    ):
        assert token in tex, token

    checker_source = (ROOT / "code/c288_delta_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    assert "object_pairs_hook=reject_duplicate_keys" in checker_source
    assert "mp.invertlaplace" in checker_source
    assert "mp.erfc" not in checker_source
    assert "int_R exp(-2*kappa*|x|) dx=1/kappa" in checker_source

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}", "two isolated directories for each",
        "byte-identical", "warning-free", "embedded and subset",
        ROUND_HASHES[0], ROUND_HASHES[1], ROUND_HASHES[2],
    ):
        assert token in compile_report, token
    hostile = (ROOT / "results/HOSTILE_AUDIT.md").read_text()
    for token in (
        "duplicate JSON keys", "inverse Laplace", "integrated diagonal resolvent",
        "30/30", "singular-continuous",
    ):
        assert token in hostile, token

    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*") if path.is_file()
    }
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items()) if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED)
    )
    assert len(files) == 27

    archived_hashes = [digest(path) for path in ROUND_PATHS]
    assert archived_hashes == ROUND_HASHES
    assert len(set(archived_hashes)) == 3
    assert digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == [1, 2, 3]
    font_counts: list[int] = []
    for path, required_text in zip(ROUND_PATHS, ROUND_TEXT):
        rows = font_rows(path)
        assert rows
        assert all(
            len(row.split()) >= 7
            and row.split()[-5] == "yes"
            and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
        pdf_text = normalized_pdf_text(path)
        for token in required_text:
            assert token in pdf_text, (path.name, token)
    assert font_counts == [19, 19, 22]

    fresh_hashes: list[list[str]] = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    checker = run_python("c288_delta_checker.py")
    symbolic = run_python("c288_delta_sympy_crosscheck.py")
    replay = run_python("c288_delta_replay.py")
    mutation = run_python("c288_delta_mutation.py")
    assert "C288 independent Laplace/interface checker: PASS" in checker
    assert "strict duplicate-rejecting schema" in checker
    assert "C288_SYMPY_PASS" in symbolic
    assert "C288 byte replay: PASS" in replay
    assert "PASS 30/30" in mutation
    checker_match = re.search(r"PASS \((\d+) assertions", checker)
    symbolic_match = re.search(r"PASS \((\d+) symbolic", symbolic)
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert checker_match and int(checker_match.group(1)) == 1726
    assert symbolic_match and int(symbolic_match.group(1)) == 46
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2) == "30"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c288-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C288",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Complete resolvent, bound/scattering, heat-kernel, and relative-trace atlas for one delta interaction",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages,
            "round_embedded_subset_font_rows": font_counts,
            "all_round_text_contracts": [list(tokens) for tokens in ROUND_TEXT],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_exact_duplicate_rejecting_schema": "PASS",
            "G2_form_domain_and_rank_one_resolvent": "PASS",
            "G3_pure_ac_plus_unique_attractive_bound_state": "PASS",
            "G4_two_channel_scattering": "PASS",
            "G5_independent_inverse_laplace_heat_kernel": "PASS",
            "G6_integrated_diagonal_relative_trace": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_six_fresh_pdf_builds_fonts_logs_text": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_claim_source_traceability": "PASS",
            "G12_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "regular_resolvent_cells": 32,
            "pole_cells": 3,
            "scattering_cells": 28,
            "bound_state_cells": 3,
            "heat_cells": 8,
            "checker_assertions": int(checker_match.group(1)),
            "symbolic_checks": int(symbolic_match.group(1)),
            "hostile_rejections": int(mutation_match.group(1)),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": digest(PDF),
            "pdf_pages": 3,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C288_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(
        json.dumps(
            {
                "status": "C288_MANIFEST_PASS",
                "payload_file_count": 27,
                "physical_file_count": 28,
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": EVIDENCE_SHA,
                "pdf_sha256": digest(PDF),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
