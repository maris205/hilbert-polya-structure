#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C303 release."""
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
MANIFEST = ROOT / "C303_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c303_thermal_qubit_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C303/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVIDENCE_SHA = "f3ceeec5f667b97f09ea2963b204dd35e64d5fc2f263a3a71c084fae9764f483"
PAYLOAD_SHA = "58c53b268e74d907b935db4cef5aca7452c8a4623ff295de69ba088881cc569e"
EVALUATION_FILE_SHA = "b4c2585c0040533d85f8691a7d2b0768fa48a2e2a9a5916c25cd14db47484a74"
EVALUATION_SEMANTIC_SHA = "567a963311029b3db03111066d426fd263bc3a77994a47146d4d0c3fccc5cca4"
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "a76618c30507dbae459d920e98d60e796278de712cea42dc6113e3dee209948a",
    "e2a467c3f76a6b77e0eacaa243a664ff0b74b2378e21df7bf8f9f1b1a422576b",
    "16c82784cff2f4cbe661938e425c5065dd77ee4de220f9caaa3ff1d7c6a9c544",
]
ROUND_PAGES = [2, 3, 3]
ROUND_FONTS = [23, 23, 24]
ROUND_TEXT = [
    ("all-rate solution", "exact entanglement-breaking threshold", "source owners"),
    ("sharp trace contraction", "complete boundary atlas", "zero generator"),
    ("exact evidence, collisions", "route_a_rejected", "no_bad_euler_or_root_number", "ai-use statement"),
]
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c303_thermal_qubit_checker.py",
    "code/c303_thermal_qubit_mutation.py", "code/c303_thermal_qubit_producer.py",
    "code/c303_thermal_qubit_replay.py", "code/c303_thermal_qubit_sympy_crosscheck.py",
    "code/c303_release_manifest.py",
    "evaluations/route_a/HCS-C303/2026-09-02.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c303_thermal_qubit_evidence.json",
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_nonfinite(value):
    raise ValueError(f"nonfinite JSON value: {value}")


def strict_json(path: Path) -> dict:
    value = json.loads(
        path.read_text(), object_pairs_hook=reject_duplicates,
        parse_constant=reject_nonfinite,
    )
    if type(value) is not dict:
        raise TypeError("top-level JSON object required")
    return value


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
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True
    )


def pdf_pages(path: Path) -> int:
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(
        line.split(":", 1)[1] for line in text.splitlines()
        if line.startswith("Pages:")
    ))


def font_rows(path: Path) -> list[str]:
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [
        line for line in text.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]


def pdf_text(path: Path) -> str:
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def raster_audit(path: Path, count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c303-raster-") as temporary:
        for page in range(1, count + 1):
            prefix = Path(temporary) / f"page-{page}"
            subprocess.run(
                [
                    "pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                    "-png", str(path), str(prefix),
                ],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            outputs = list(Path(temporary).glob(f"page-{page}-*.png"))
            assert len(outputs) == 1 and outputs[0].stat().st_size > 1000
            sizes.append(outputs[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c303-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update({
            "SOURCE_DATE_EPOCH": str(EPOCH),
            "FORCE_SOURCE_DATE": "1",
            "TZ": "UTC",
        })
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error",
            "-jobname=main", source,
        ]
        for _ in range(2):
            subprocess.run(
                command, cwd=work, env=env, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING_RE.search(log)
        assert match is None, match.group(0) if match else ""
        return (work / "main.pdf").read_bytes()


def main() -> None:
    producer = run_python("c303_thermal_qubit_producer.py")
    assert "C303_PRODUCER_PASS" in producer
    data = strict_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == PAYLOAD_SHA
    assert data["schema"] == "hcs-c303-thermal-qubit-lindblad-v1"
    assert data["candidate_id"] == "HCS-C303"
    assert data["obstruction_id"] == "HEN-O287"
    assert data["source_commit"] == SOURCE
    assert type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["evaluation_file_sha256"] == EVALUATION_FILE_SHA
    assert data["route_a"] == {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    assert data["scope_flags"] == FLAGS
    assert data["model"]["dephasing_convention"] == "the isolated coherence decay rate is gamma_phi"
    assert data["theorem_contract"]["choi_ppt"] == "p(1-p)(1-eta)^2>=eta^q"
    assert data["summary"] == {
        "choi_exact_cells": 75, "liouvillian_cases": 12, "trace_cases": 10,
        "semigroup_cases": 12, "threshold_cases": 8, "boundary_faces": 7,
        "audited_rows": 124,
    }

    checker_source = (ROOT / "code/c303_thermal_qubit_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not any("producer" in name for name in imports)
    assert "object_pairs_hook=reject_duplicates" in checker_source
    assert "parse_constant=reject_nonfinite" in checker_source
    assert "exact_tree_equal(route_yaml, EXPECTED_EVALUATION)" in checker_source

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED", "not negotiable", "3-2sqrt(2)",
        "kernel dimension", "HEN-O287", "Stinespring dilation",
    ):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "10.1063/1.522979", "10.1007/BF01608499",
        "10.1016/0024-3795(75)90075-0", "C303 instead evolves density matrices",
    ):
        assert token in source_audit, token
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in (
        "All 35 attacks", "repairs every affected JSON payload hash",
        "Finite determinant is not arithmetic", "Stinespring dilation",
        "NO_BAD_EULER_OR_ROOT_NUMBER",
    ):
        assert token in hostile, token
    compile_report = " ".join((PAPER / "COMPILE_REPORT.md").read_text().split())
    for token in (
        "SOURCE_DATE_EPOCH=1788307200", "two isolated fresh directories",
        "byte-identical", *ROUND_HASHES,
    ):
        assert token in compile_report, token

    physical = {
        str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
        if path.is_file()
    }
    unexpected_sidecars = [name for name, path in physical.items() if sidecar(path)]
    assert not unexpected_sidecars, unexpected_sidecars
    files = {
        name: digest(path) for name, path in sorted(physical.items())
        if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED)
    )
    assert len(files) == 27

    assert digest(EVALUATION) == EVALUATION_FILE_SHA
    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == ROUND_PAGES
    font_counts, raster_sizes = [], []
    for path, required, count in zip(ROUND_PATHS, ROUND_TEXT, ROUND_PAGES):
        rows = font_rows(path)
        assert rows and all(
            len(row.split()) >= 7
            and row.split()[-5] == "yes"
            and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
        raster_sizes.append(raster_audit(path, count))
    assert font_counts == ROUND_FONTS

    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(
        zip(ROUND_PATHS, ROUND_HASHES)
    ):
        first = fresh_build(round_number)
        second = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c303_thermal_qubit_checker.py")
    symbolic = run_python("c303_thermal_qubit_sympy_crosscheck.py")
    replay = run_python("c303_thermal_qubit_replay.py")
    mutation = run_python("c303_thermal_qubit_mutation.py")
    assert "producer import forbidden" in checker
    assert "strict JSON/YAML exact tree" in checker
    assert "C303 SymPy cross-check: PASS" in symbolic
    assert "C303 byte replay: PASS" in replay
    assert "C303 hostile mutation suite: PASS 35/35" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    hostile_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, hostile_n) == (709, 129, 35)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c303-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C303",
        "obstruction_id": "HEN-O287",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "exact all-rate thermal qubit semigroup, sharp trace contraction, and faithful-bath entanglement-breaking threshold",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "fresh_build_directory_count": 6,
            "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [
                str(path.relative_to(ROOT)) for path in ROUND_PATHS
            ],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages,
            "round_pdf_bytes": [path.stat().st_size for path in ROUND_PATHS],
            "round_embedded_subset_font_rows": font_counts,
            "round_text_contracts": [list(items) for items in ROUND_TEXT],
            "raster_page_bytes": raster_sizes,
            "visual_inspection": "PASS all 8 archived pages",
            "final_equals": "paper/main_round2.pdf",
        },
        "evaluation_contract": {
            "path": str(EVALUATION.relative_to(ROOT)),
            "file_sha256": EVALUATION_FILE_SHA,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "duplicate_merge_anchor_alias_rejection": True,
            "exact_recursive_semantic_tree_and_types": True,
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G0a_strict_json_yaml_exact_types": "PASS",
            "G1_exact_channel_and_semigroup": "PASS",
            "G2_liouvillian_spectrum_and_all_degeneracies": "PASS",
            "G3_normalized_choi_cp_and_ppt": "PASS",
            "G4_unique_faithful_thermal_eb_threshold": "PASS",
            "G5_sharp_trace_contraction_and_recurrence": "PASS",
            "G6_boundary_atlas_including_zero_generator": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_six_fresh_pdf_builds_fonts_logs_text_raster": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_source_collision_and_claim_traceability": "PASS",
            "G12_target_euler_root_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **data["summary"],
            "checker_assertions": checker_n,
            "symbolic_checks": symbolic_n,
            "hostile_rejections": hostile_n,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": PAYLOAD_SHA,
            "evidence_sha256": EVIDENCE_SHA,
            "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF),
            "pdf_pages": pages[-1],
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "boundary_risk": "One-sided amplitude damping and pure dephasing are EB only in their infinite-time limits; the zero generator has a four-dimensional, not two-dimensional, kernel.",
        "collision_boundary": data["collision_boundary"],
        "excluded_from_manifest": [
            "C303_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C303_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
