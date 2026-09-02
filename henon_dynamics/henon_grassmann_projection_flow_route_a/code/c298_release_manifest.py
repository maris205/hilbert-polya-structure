#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C298 release."""
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

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C298_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c298_grassmann_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C298/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "0519b0fd34b0ae5c41e2e92be6970d677229c1571c05552faba8fdf0667d3134"
PAYLOAD_SHA = "0d1a24a89ab2eb2d4cbfdea313c5d49d76dbec33e585ac01f603cf3f7a181545"
EVALUATION_FILE_SHA = "20788a969a882e33aac741f0a14ca907776b897f62c59a718d7607cd0cb00d6a"
EVALUATION_SEMANTIC_SHA = "bb0c3bad6379a1f38ffda0f2e8349725367d43c81349447a972e62725c5b06f1"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "0d8d6e35da94f740b9246155b3adaf44b2769700dd352c89f8bc8f6b32b388db",
    "b33a6ebe333284632d72bd20ccaec7f065f32d4c7a40dfa164d632147449dde7",
    "37c2512b70f1042b18b3fc89282fa58f82d65897e9e4c6aab6f8199957477295",
]
ROUND_PAGES = [3, 4, 4]
ROUND_FONTS = [21, 22, 23]
ROUND_TEXT = [
    ("global exact projector", "simple spectrum: every schubert cell and its rate", "strict lyapunov law"),
    ("matroid guard", "associated-graded limit", "complete critical atlas"),
    ("exact evidence and boundary audit", "collision with c185", "route_a_rejected", "no_bad_euler_or_root_number", "ai-use statement"),
]
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
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Plucker weights are finite-dimensional source exponents, not prime norms or target spectral zeros.",
    "The symmetric generator A is not asserted to be a Hilbert--Polya operator.",
    "No literary priority is claimed for Oja, Brockett, Grassmann power-flow, Schubert, or Morse--Bott mechanisms.",
]
COLLISION_BOUNDARY = {
    "C185": "C185 evolves a full symmetric matrix on a fixed isospectral orbit toward a separate diagonal target; C298 fixes A and evolves a rank-k projection/subspace under the induced linear action.",
    "subset_sum_warning": "simple eigenvalues need not have distinct k-fold subset sums; uniqueness uses the representable-matroid greedy basis on actual support.",
}
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c298_grassmann_checker.py",
    "code/c298_grassmann_mutation.py", "code/c298_grassmann_producer.py",
    "code/c298_grassmann_replay.py", "code/c298_grassmann_sympy_crosscheck.py",
    "code/c298_release_manifest.py",
    "evaluations/route_a/HCS-C298/2026-09-02.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c298_grassmann_evidence.json",
}
EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C298",
    "title": "Exact Grassmann projection flow and Schubert--Morse--Bott atlas",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O282",
    "candidate_definition": "Rank-k real orthogonal projections evolving by dot(P)=[P,[P,A]] for a fixed real symmetric matrix A.",
    "family": "Grassmann gradient and continuous subspace power flow",
    "phase_space": "real Grassmannian Gr(k,n) represented by rank-k orthogonal projections",
    "dynamics": "positive gradient flow of P maps to Tr(AP)",
    "parameters": "n>=2; 1<=k<=n-1; A=A^T real",
    "parameter_provenance": "all finite dimensions and both simple and repeated spectra are covered",
    "arithmetic_origin": "none; eigenvalue and Plucker weights are source-linear-algebra data",
    "clock": "continuous real time t",
    "normalization": "orthogonal projection represents an unoriented subspace",
    "determinant_convention": "Plucker coordinates are projective and defined up to one common nonzero scale",
    "orbit_cutoff": "global exact theorem; finite cases are regression evidence only",
    "precision": "exact integers and rationals in evidence; symbolic identities in SymPy",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": [
        "results/c298_grassmann_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf",
    ],
    "a0": {
        "verdict": "A0_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "the flow has finite-dimensional eigenvalue and Plucker weights",
        "strongest_failure": "no arithmetic local datum or target Euler factor is constructed",
        "artifacts": ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    },
    "a1": {
        "verdict": "A1_FAIL",
        "evidence_status": "strict Lyapunov obstruction",
        "strongest_evidence": "every orbit has an exact invariant-subspace limit",
        "strongest_failure": "nonconstant recurrence and primitive periodic-orbit repetition are absent",
        "artifacts": ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    },
    "a2": {
        "verdict": "A2_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "continuous time gives explicit exponential weights",
        "strongest_failure": "time is not an arithmetic clock or logarithmic prime norm",
        "artifacts": ["THEOREM_PACKAGE.md"],
    },
    "a3": {
        "verdict": "A3_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "exterior-power coordinates give finite exponential sums",
        "strongest_failure": "no target completed function or target functional equation is present",
        "artifacts": ["THEOREM_PACKAGE.md", "results/c298_grassmann_evidence.json"],
    },
    "a4": {
        "verdict": "A4_FORMAL_HINT",
        "evidence_status": "analogy only",
        "strongest_evidence": "a fixed symmetric generator orders subspaces by its eigenspaces",
        "strongest_failure": "the flow is dissipative gradient dynamics and A is not a certified Hilbert--Polya operator",
        "artifacts": ["SOURCE_AUDIT.md", "paper/main.pdf"],
    },
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; global solution, limits, and Morse--Bott structure are analytic",
    "source_owner_tokens": [
        "10.1007/BF00275687", "10.1016/0024-3795(91)90021-N", "hdl:2078.5/90452",
    ],
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicate_keys(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    value = json.loads(
        path.read_text(), object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_nonfinite,
    )
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    return value


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe loader retaining dates as strings and rejecting ambiguous maps."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML mapping keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping
)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return value


def exact_tree_equal(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(
            exact_tree_equal(actual[key], expected[key]) for key in expected
        )
    if type(expected) is list:
        return len(actual) == len(expected) and all(
            exact_tree_equal(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
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
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def raster_audit(path: Path, page_count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c298-raster-") as temporary:
        for page in range(1, page_count + 1):
            prefix = Path(temporary) / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            outputs = list(Path(temporary).glob(f"page-{page}-*.png"))
            assert len(outputs) == 1 and outputs[0].stat().st_size > 1000
            sizes.append(outputs[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c298-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
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
    producer = run_python("c298_grassmann_producer.py")
    assert "C298_PRODUCER_PASS" in producer
    data = strict_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == PAYLOAD_SHA
    assert data["schema"] == "hcs-c298-grassmann-projection-flow-v1"
    assert data["candidate_id"] == "HCS-C298"
    assert data["obstruction_id"] == "HEN-O282"
    assert data["evaluation_date"] == "2026-09-02"
    assert type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH
    assert data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE
    assert exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR})
    assert data["model"]["flow"] == "dot(P)=[P,[P,A]]"
    assert data["theorem_contract"]["global_solution"].startswith("P(t)=Y(t)")
    assert "representable matroid" in data["proof_contract"]["matroid_guard"]
    assert "never assumed distinct" in data["proof_contract"]["tie_guard"]
    assert exact_tree_equal(data["route_a"], {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    })
    assert exact_tree_equal(data["scope_flags"], FLAGS)
    assert exact_tree_equal(data["nonclaims"], NONCLAIMS)
    assert exact_tree_equal(data["collision_boundary"], COLLISION_BOUNDARY)
    enumeration = data["enumeration"]
    assert type(enumeration["simple_case_count"]) is int and enumeration["simple_case_count"] == 8
    assert type(enumeration["repeated_case_count"]) is int and enumeration["repeated_case_count"] == 6
    assert type(enumeration["simple_plucker_support_cells"]) is int and enumeration["simple_plucker_support_cells"] == 80
    assert type(enumeration["repeated_plucker_support_cells"]) is int and enumeration["repeated_plucker_support_cells"] == 37
    assert type(enumeration["linear_mode_cells"]) is int and enumeration["linear_mode_cells"] == 50
    assert type(enumeration["morse_bott_component_rows"]) is int and enumeration["morse_bott_component_rows"] == 22
    assert type(enumeration["audited_cell_count"]) is int and enumeration["audited_cell_count"] == 189
    assert [item["identifier"] for item in data["references"]] == [
        "10.1007/BF00275687", "10.1016/0024-3795(91)90021-N", "hdl:2078.5/90452",
    ]

    evaluation = strict_yaml(EVALUATION)
    assert digest(EVALUATION) == EVALUATION_FILE_SHA
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert exact_tree_equal(evaluation, EXPECTED_EVALUATION)

    checker_source = (ROOT / "code/c298_grassmann_checker.py").read_text()
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
        "PROVABLE AS STATED", "strong basis exchange", "associated-graded subspace",
        "actual second nonzero Plücker weight", "HEN-O282",
    ):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "10.1007/BF00275687", "10.1016/0024-3795(91)90021-N",
        "hdl:2078.5/90452", "C185 is not being relabeled",
    ):
        assert token in source_audit, token
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in ("All 116 attacks", "repaired every affected JSON payload hash", "scope-escalation", "collision-boundary text", "all 36 structural path", "integer zero", "tied subset sums"):
        assert token in hostile, token
    compile_report = " ".join((PAPER / "COMPILE_REPORT.md").read_text().split())
    for token in ("SOURCE_DATE_EPOCH=1788307200", "two isolated directories", "byte-identical", *ROUND_HASHES):
        assert token in compile_report, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    unexpected_sidecars = [name for name, path in physical.items() if sidecar(path)]
    assert not unexpected_sidecars, unexpected_sidecars
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == ROUND_PAGES
    font_counts = []
    raster_sizes = []
    for path, required, page_count in zip(ROUND_PATHS, ROUND_TEXT, ROUND_PAGES):
        rows = font_rows(path)
        assert rows and all(
            len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
        raster_sizes.append(raster_audit(path, page_count))
    assert font_counts == ROUND_FONTS

    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first = fresh_build(round_number)
        second = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c298_grassmann_checker.py")
    symbolic = run_python("c298_grassmann_sympy_crosscheck.py")
    replay = run_python("c298_grassmann_replay.py")
    mutation = run_python("c298_grassmann_mutation.py")
    assert "C298 independent Grassmann checker: PASS" in checker and "producer import forbidden" in checker
    assert "C298 SymPy cross-check: PASS" in symbolic
    assert "C298 byte replay: PASS" in replay
    assert "C298 hostile mutation suite: PASS 116/116" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (2717, 534, 116)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c298-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C298",
        "obstruction_id": "HEN-O282",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "global Grassmann projection flow with exact Schubert limits, actual-support rates, and a complete repeated-spectrum Morse--Bott atlas",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "fresh_build_directory_count": 6,
            "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages,
            "round_pdf_bytes": [path.stat().st_size for path in ROUND_PATHS],
            "round_embedded_subset_font_rows": font_counts,
            "round_text_contracts": [list(items) for items in ROUND_TEXT],
            "raster_page_bytes": raster_sizes,
            "visual_inspection": "PASS all 11 archived pages",
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
            "G1_global_projector_solution": "PASS",
            "G2_plucker_scaling_and_matroid_tie_guard": "PASS",
            "G3_simple_schubert_limits_and_actual_support_rates": "PASS",
            "G4_equilibria_linear_modes_and_dimensions": "PASS",
            "G5_repeated_spectrum_associated_grade_morse_bott": "PASS",
            "G6_strict_lyapunov_no_recurrence": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_six_fresh_pdf_builds_fonts_logs_text_raster": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_source_collision_and_claim_traceability": "PASS",
            "G12_target_euler_root_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "simple_spectrum_cases": 8,
            "repeated_spectrum_cases": 6,
            "simple_plucker_support_cells": 80,
            "repeated_plucker_support_cells": 37,
            "linear_mode_cells": 50,
            "morse_bott_component_rows": 22,
            "audited_cells": 189,
            "checker_assertions": checker_n,
            "symbolic_checks": symbolic_n,
            "hostile_rejections": mutation_n,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": PAYLOAD_SHA,
            "evidence_sha256": EVIDENCE_SHA,
            "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF),
            "pdf_pages": pages[-1],
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "boundary_risk": "Subset-sum ties are handled only through actual representable-matroid support; repeated eigenvalues require the full associated-graded leading component, never an invented unique coordinate.",
        "collision_boundary": data["collision_boundary"],
        "excluded_from_manifest": [
            "C298_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C298_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
