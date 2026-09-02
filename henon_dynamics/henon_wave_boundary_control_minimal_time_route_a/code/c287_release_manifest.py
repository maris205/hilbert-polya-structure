#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C287 release."""
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
MANIFEST = ROOT / "C287_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c287_wave_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C287/2026-09-02.yaml"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "0a2e32e70ffdc8a3a5b0a21fa489fc677591c66d70470cd029bcacaba9578303"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
EXPECTED_THEOREM = {
    "revival": "the least positive full-energy wave-group identity time is 2L/c",
    "critical_identity": "at T=2L/c, integral |u_x(L,t)|^2 dt=4E(0)/c^3",
    "observability": "one-end observability holds for every T>=2L/c, equality included",
    "short_time_failure": "every T<2L/c misses a nonzero smooth periodic traveling profile",
    "hum": "duality gives exact L2 Dirichlet boundary control on the transposition state space at exactly the same threshold",
    "boundary": "no zero mode; endpoint reversal, T=0, half revival, and all positive L,c scalings are explicit",
}
EXPECTED_PROOF = {
    "periodic_coordinate": "u(x,t)=F(x+ct)-F(-x+ct) with 2L-periodic F",
    "energy_coordinate": "E=c^2 integral_0^(2L)|F'|^2",
    "trace_coordinate": "u_x(L,t)=2F'(L+ct)",
    "missed_arc": "if cT<2L, support a nonzero smooth mean-zero F' in the complementary arc",
    "revival_phases": "all nonzero modes have frequencies n*pi*c/L and common gcd one",
    "finite_role": "exact cells audit constants and conventions but do not prove infinite-dimensional observability",
}
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "91bfa4f1d7a1f821160acce33df8dc17f3c92692c4d87956b1d94a1226c9ef1b",
    "787750ff8f7b3bd93772661f31c13c45cea2b9cd56b3613f580071bff874ead0",
    "e0fb034b86b6016aca38207387bcd3152eba62ce76e85b08c2239305f2e23fe7",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md",
    "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md",
    "README.md",
    "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
    "code/README.md",
    "code/c287_release_manifest.py",
    "code/c287_wave_checker.py",
    "code/c287_wave_mutation.py",
    "code/c287_wave_producer.py",
    "code/c287_wave_replay.py",
    "code/c287_wave_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C287/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md",
    "paper/README.md",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/main_round0_original.pdf",
    "paper/main_round1.pdf",
    "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c287_wave_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|undefined citations|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix
        in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True
    )


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(
        next(
            line.split(":", 1)[1]
            for line in info.splitlines()
            if line.startswith("Pages:")
        )
    )


def pdf_text(path: Path) -> str:
    return " ".join(
        subprocess.check_output(["pdftotext", str(path), "-"], text=True)
        .lower()
        .split()
    )


def font_rows(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [
        line
        for line in output.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c287-r{round_number}-") as temp:
        work = Path(temp)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = [
            "lualatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-jobname=main",
            source,
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
        assert not WARNING_RE.search(log)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c287-wave-boundary-control-v1"
    assert data["candidate_id"] == "HCS-C287"
    assert data["evaluation_date"] == "2026-09-02"
    assert data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["theorem_contract"] == EXPECTED_THEOREM
    assert data["proof_contract"] == EXPECTED_PROOF
    assert data["route_a"] == {
        "tuple": TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    assert set(data["scope_flags"]) == {
        "arithmetic_local_data",
        "euler_factors",
        "root_numbers",
        "automorphy",
        "target_divisor_or_counting_law",
        "target_functional_equation",
        "target_zero_match",
        "hilbert_polya_operator",
        "route_b_input",
    }
    assert not any(data["scope_flags"].values())
    assert data["enumeration"] == {
        "parameter_rows": 16,
        "modal_cells": 256,
        "revival_cells": 16,
        "subcritical_cells": 16,
        "mode_min": 1,
        "mode_max": 16,
    }
    assert {row["identifier"] for row in data["references"]} == {
        "10.1137/1030001",
        "10.1137/0330055",
    }

    yaml_text = YAML.read_text()
    for token in (
        "schema: route-a-evaluation-v0.2.0",
        "candidate_id: HCS-C287",
        f"source_commit: {SOURCE}",
        f"fixed_epoch: {EPOCH}",
        f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR}",
        "tuple: [A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION]",
        "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert token in yaml_text, token

    theorem_text = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED",
        "2L/c",
        "4E(0)/c^3",
        "O_T^* O_T",
        "does not assert that `O_T` is onto all of `L^2(0,T)`",
        "A4_NATURAL_QUANTIZATION",
    ):
        assert token in theorem_text, token

    tex_text = " ".join(TEX.read_text().split())
    for token in (
        "Least full-space revival",
        "Exact critical observability",
        "Sharp failure below the round trip",
        "control-adjoint observation",
        r"\mathcal O_T^*\mathcal O_T",
        "not a claimed surjection onto all of",
        "2,804 assertions",
        "23/23",
        "not priority for HUM",
    ):
        assert token in tex_text, token

    source_text = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "10.1137/1030001",
        "10.1137/0330055",
        "not a literature-level originality claim",
    ):
        assert token in source_text, token

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}",
        "byte-identical",
        "warning-free",
        "embedded and subset",
        "visually inspected",
        "All six rendered pages",
    ):
        assert token in compile_report, token

    checker_tree = ast.parse((ROOT / "code/c287_wave_checker.py").read_text())
    imports: list[str] = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]

    producer = run_python("c287_wave_producer.py")
    checker = run_python("c287_wave_checker.py")
    symbolic = run_python("c287_wave_sympy_crosscheck.py")
    replay = run_python("c287_wave_replay.py")
    mutation = run_python("c287_wave_mutation.py")
    assert "C287_PRODUCER_PASS" in producer
    assert "C287 independent checker: PASS" in checker
    assert "C287_SYMPY_PASS" in symbolic
    assert "C287 byte replay: PASS" in replay
    assert "C287 mutation suite: PASS 23/23" in mutation
    checker_match = re.search(r"PASS \((\d+) assertions", checker)
    symbolic_match = re.search(r"PASS \((\d+) symbolic", symbolic)
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert checker_match and int(checker_match.group(1)) == 2804
    assert symbolic_match and int(symbolic_match.group(1)) == 86
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2) == "23"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items())
        if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        sorted(EXPECTED - set(files)),
        sorted(set(files) - EXPECTED),
    )
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [1, 2, 3] and pdf_pages(PDF) == 3
    font_counts: list[int] = []
    word_counts: list[int] = []
    round_texts: list[str] = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(
            len(row.split()) >= 7
            and row.split()[-5] == "yes"
            and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
        text = pdf_text(path)
        round_texts.append(text)
        word_counts.append(len(text.split()))
    assert font_counts == [19, 21, 23]
    # Counts use Python's Unicode-whitespace tokenization on normalized
    # ``pdftotext`` output; this is intentionally the same extraction path
    # whose semantic tokens are gated immediately below.
    assert word_counts == [260, 489, 1003]
    for token in ("least full-space revival", "not l/c"):
        assert token in round_texts[0], token
    for token in ("exact critical observability", "including equality"):
        assert token in round_texts[1], token
    for token in (
        "hum duality and function spaces",
        "scaled isometry onto its closed range",
        "not a claimed surjection onto all of",
        "hum gramian",
        "2,804",
        "23/23",
        SCOPE.lower(),
        "route_a_rejected",
        "10.1137/1030001",
        "10.1137/0330055",
    ):
        assert token in round_texts[2], token

    fresh_hashes: list[list[str]] = []
    for round_number, (archive, expected_hash) in enumerate(
        zip(ROUND_PATHS, ROUND_HASHES)
    ):
        one, _ = fresh_build(round_number)
        two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    release = {
        "schema": "hcs-c287-release-v2",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C287",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": (
            "Exact critical one-end wave observability and controllability "
            "at the round-trip time"
        ),
        "evidence_sha256": EVIDENCE_SHA,
        "evidence_payload_sha256": data["payload_sha256"],
        "build_contract": {
            "engine": "LuaLaTeX",
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "fixed_epoch": EPOCH,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_exact_critical_identity": "PASS",
            "G2_short_time_obstruction": "PASS",
            "G3_hum_spaces_and_gramian": "PASS",
            "G4_exact_contracts_unique_key_sets": "PASS",
            "G5_checker_symbolic_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS",
            "G7_deterministic_pdf_logs_fonts_text_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_source_traceability": "PASS",
            "G10_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **data["enumeration"],
            "checker_assertions": int(checker_match.group(1)),
            "symbolic_checks": int(symbolic_match.group(1)),
            "hostile_rejections": int(mutation_match.group(1)),
            "pdf_pages": 3,
            "round_pdf_pages": page_counts,
            "round_pdf_sha256": ROUND_HASHES,
            "pdf_sha256": digest(PDF),
            "embedded_subset_font_rows": font_counts,
            "round_word_counts": word_counts,
            "evidence_bytes": EVIDENCE.stat().st_size,
        },
        "route_a_tuple": TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "nonclaims": data["nonclaims"],
        "file_count_excluding_manifest": len(files),
        "excluded_from_manifest": [
            "C287_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(
        json.dumps(release, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(
        json.dumps(
            {
                "status": "C287_RELEASE_PASS",
                "payload_file_count": 27,
                "physical_file_count": 28,
                "checker_assertions": int(checker_match.group(1)),
                "symbolic_checks": int(symbolic_match.group(1)),
                "hostile_rejections": int(mutation_match.group(1)),
                "evidence_sha256": EVIDENCE_SHA,
                "pdf_sha256": digest(PDF),
                "manifest_sha256": digest(MANIFEST),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
