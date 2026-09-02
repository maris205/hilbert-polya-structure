#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C299 release."""
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
MANIFEST = ROOT / "C299_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c299_lamb_oseen_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C299/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "518343c593f63402eabbcb602761d54c56003d27c3e9f3774ee405b5115c74c2"
PAYLOAD_SHA = "a1e673d61021eea58b54d2fdbf3d813ee87d7b84d91fbfcefb528f4e741766b4"
EVALUATION_FILE_SHA = "620b0fa1429d57052a57a01ffcb33ded1b12664cc63965ca3a8cc12953d2296c"
EVALUATION_SEMANTIC_SHA = "614bdcc273694f3a585b391584ab7a8efb2b3a60b9b4cf3924c248cb50f38b27"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "1c127bc83686c042835e589ccbfbbe84609b5ac90e336f973557f03c4a4fedc9",
    "8e2ba5c010ae21cf61edffcfa77f69df2f49c0293c3e2a94bc2ae915ffd19de7",
    "5b1a4d4dd9480e55ff970b5ae01dac8435c5c9ac4a62ee3c1f740288cd342b61",
]
ROUND_PAGES = [3, 3, 4]
ROUND_FONTS = [20, 23, 24]
ROUND_TEXT = [
    ("radial forward-similar uniqueness", "every particle orbit", "all moments, norms, and exact dissipation"),
    ("boundary atlas and recurrence obstruction", "whole-plane kinetic energy diverges logarithmically", "weak trace"),
    ("exact evidence and hostile audit", "collision boundaries", "route_a_rejected", "no_bad_euler_or_root_number", "ai-use statement"),
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
    "The circulation Gamma and Gaussian moments are fluid-mechanical source data, not rational-prime labels or prime-power weights.",
    "The Navier-Stokes generator is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lamb-Oseen formula or its standard radial reduction.",
]
COLLISION_BOUNDARY = {
    "C206": "C206 studies Couette advection-diffusion Fourier shearing on T times R; C299 classifies radial nonlinear-vorticity self-similarity on R^2, whose advection cancels geometrically.",
    "C207": "C207 classifies Barenblatt profiles for scalar nonlinear diffusion; C299 reconstructs velocity by Biot-Savart and audits circulation, particle angles, enstrophy, and the point-vortex boundary.",
    "energy_warning": "nonzero circulation gives logarithmically divergent whole-plane kinetic energy; only enstrophy and palinstrophy are claimed finite.",
}
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c299_lamb_oseen_checker.py",
    "code/c299_lamb_oseen_mutation.py", "code/c299_lamb_oseen_producer.py",
    "code/c299_lamb_oseen_replay.py", "code/c299_lamb_oseen_sympy_crosscheck.py",
    "code/c299_release_manifest.py",
    "evaluations/route_a/HCS-C299/2026-09-02.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c299_lamb_oseen_evidence.json",
}


def route_branch(verdict, status, evidence, failure, artifacts):
    return {
        "verdict": verdict,
        "evidence_status": status,
        "strongest_evidence": evidence,
        "strongest_failure": failure,
        "artifacts": artifacts,
    }


EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C299",
    "title": "Radial Lamb--Oseen forward self-similarity: uniqueness, exact trajectories, and dissipation boundaries",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O283",
    "candidate_definition": "Two-dimensional viscous vorticity on the plane in the bounded-at-origin, finite-circulation, radial forward-self-similar class.",
    "family": "Lamb--Oseen vortex and radial Navier--Stokes similarity dynamics",
    "phase_space": "signed radial vorticities on R^2 with finite circulation, restricted to the declared similarity class",
    "dynamics": "partial_t omega plus u dot grad omega equals nu Delta omega, with velocity reconstructed by planar Biot--Savart",
    "parameters": "Gamma real; nu>0; tau_0>=0; tau=t+tau_0>0",
    "parameter_provenance": "the theorem covers the full stated parameter set and every profile in the declared regular finite-circulation class",
    "arithmetic_origin": "none; circulation, viscosity, Gaussian moments, and exponential-integral angles are fluid-mechanical data",
    "clock": "physical viscous time t, equivalently positive age tau=t+tau_0",
    "normalization": "the integral of omega over R^2 equals the signed circulation Gamma",
    "determinant_convention": "not applicable; no determinant or zeta normalization is used",
    "orbit_cutoff": "global analytic classification and exact trajectories; finite rows are regression evidence only",
    "precision": "exact rational parameter receipts and 72-digit transcendental values; independent symbolic identities",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c299_lamb_oseen_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": route_branch(
        "A0_FAIL", "exact negative classification",
        "circulation and Gaussian moments are explicitly computable source-side fluid quantities",
        "no arithmetic local datum, rational-prime label, or target Euler factor is constructed",
        ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    ),
    "a1": route_branch(
        "A1_FAIL", "strict dissipation obstruction",
        "all positive radii admit exact nonautonomous angular trajectories",
        "for Gamma nonzero every finite Lp norm with p>1 decreases strictly, so recurrent vorticity states and primitive periodic-orbit repetition are absent",
        ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    ),
    "a2": route_branch(
        "A2_FAIL", "exact negative classification",
        "the long-time particle angle has a logarithmic term",
        "the clock is physical viscous time and the logarithm is not a rational-prime norm or arithmetic length",
        ["THEOREM_PACKAGE.md"],
    ),
    "a3": route_branch(
        "A3_FAIL", "exact negative classification",
        "Gaussian moments and an exponential-integral trajectory primitive are closed form",
        "no target completed function, target zero set, or functional equation is present",
        ["results/c299_lamb_oseen_evidence.json", "paper/main.pdf"],
    ),
    "a4": route_branch(
        "A4_FAIL", "dissipative-generator mismatch",
        "the heat operator supplies a classical similarity mechanism",
        "the dissipative Navier--Stokes evolution is not a certified self-adjoint Hilbert--Polya operator",
        ["SOURCE_AUDIT.md", "paper/main.pdf"],
    ),
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; classification, trajectories, moments, dissipation, and boundary limits are proved analytically",
    "source_owner_tokens": ["Oseen-1912-Arkiv-7-no14", "10.1007/s00220-004-1254-9"],
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    result = json.loads(
        path.read_text(), object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_nonfinite,
    )
    if type(result) is not dict:
        raise TypeError("JSON top level must be an object")
    return result


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader, node, deep=False):
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
    result = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(result) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return result


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
    with tempfile.TemporaryDirectory(prefix="c299-raster-") as temporary:
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
    with tempfile.TemporaryDirectory(prefix=f"c299-r{round_number}-") as temporary:
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
    producer = run_python("c299_lamb_oseen_producer.py")
    assert "C299_PRODUCER_PASS" in producer
    data = strict_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == PAYLOAD_SHA
    assert data["schema"] == "hcs-c299-lamb-oseen-self-similar-vortex-v1"
    assert data["candidate_id"] == "HCS-C299" and data["obstruction_id"] == "HEN-O283"
    assert data["evaluation_date"] == "2026-09-02"
    assert type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH
    assert data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE
    assert exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR})
    assert "bounded-at-origin" in data["theorem_contract"]["classification"]
    assert "continuous real-lift angle" in data["theorem_contract"]["lagrangian"]
    assert "C=0" in data["proof_contract"]["uniqueness_ode"]
    assert "finite rows regress" in data["proof_contract"]["finite_role"]
    assert exact_tree_equal(data["route_a"], {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    })
    assert exact_tree_equal(data["scope_flags"], FLAGS)
    assert exact_tree_equal(data["nonclaims"], NONCLAIMS)
    assert exact_tree_equal(data["collision_boundary"], COLLISION_BOUNDARY)
    enumeration = data["enumeration"]
    assert type(enumeration["field_case_count"]) is int and enumeration["field_case_count"] == 8
    assert type(enumeration["point_receipt_cells"]) is int and enumeration["point_receipt_cells"] == 72
    assert type(enumeration["moment_receipt_cells"]) is int and enumeration["moment_receipt_cells"] == 72
    assert type(enumeration["lp_receipt_cells"]) is int and enumeration["lp_receipt_cells"] == 48
    assert type(enumeration["lagrangian_receipt_cells"]) is int and enumeration["lagrangian_receipt_cells"] == 12
    assert type(enumeration["boundary_receipt_cells"]) is int and enumeration["boundary_receipt_cells"] == 9
    assert type(enumeration["audited_cell_count"]) is int and enumeration["audited_cell_count"] == 213
    assert [item["identifier"] for item in data["references"]] == [
        "Oseen-1912-Arkiv-7-no14", "10.1007/s00220-004-1254-9",
    ]

    evaluation = strict_yaml(EVALUATION)
    assert digest(EVALUATION) == EVALUATION_FILE_SHA
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert exact_tree_equal(evaluation, EXPECTED_EVALUATION)

    checker_source = (ROOT / "code/c299_lamb_oseen_checker.py").read_text()
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
    assert "YAML anchors and aliases are forbidden" in checker_source
    assert "noncanonical rational receipt" in checker_source
    assert "exact boundary ledger" in checker_source

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED", "declared radial forward-self-similar class", "C=0",
        "kinetic energy is infinite", "HEN-O283", "arbitrary vortex filaments",
    ):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "Oseen-1912-Arkiv-7-no14", "10.1007/s00220-004-1254-9",
        "C206 is not being relabeled", "C207 is not being relabeled",
    ):
        assert token in source_audit, token
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in (
        "All 84 attacks", "72 repaired-hash semantic mutations", "scope escalation",
        "collision-boundary text", "Wrong exponential-integral sign", "Energy coefficient error",
    ):
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

    checker = run_python("c299_lamb_oseen_checker.py")
    symbolic = run_python("c299_lamb_oseen_sympy_crosscheck.py")
    replay = run_python("c299_lamb_oseen_replay.py")
    mutation = run_python("c299_lamb_oseen_mutation.py")
    assert "C299 independent Lamb-Oseen checker: PASS" in checker and "producer import forbidden" in checker
    assert "C299 SymPy cross-check: PASS" in symbolic
    assert "C299 byte replay: PASS" in replay
    assert "C299 hostile mutation suite: PASS 84/84" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (1195, 31, 84)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c299-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C299",
        "obstruction_id": "HEN-O283",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "complete radial forward-self-similar Lamb-Oseen classification with exact particle angles, moments, dissipation, and singular boundaries",
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
            "visual_inspection": "PASS all 10 archived pages",
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
            "G1_declared_class_radial_uniqueness": "PASS",
            "G2_biot_savart_velocity_and_origin": "PASS",
            "G3_exact_lagrangian_primitive_and_asymptotics": "PASS",
            "G4_all_moments_lp_norms_and_dissipation": "PASS",
            "G5_zero_age_inviscid_recurrence_energy_boundaries": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS",
            "G8_six_fresh_pdf_builds_fonts_logs_text_raster": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_source_collision_and_claim_traceability": "PASS",
            "G11_target_euler_root_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "field_cases": 8,
            "point_receipt_cells": 72,
            "moment_receipt_cells": 72,
            "lp_receipt_cells": 48,
            "lagrangian_receipt_cells": 12,
            "boundary_receipt_cells": 9,
            "audited_cells": 213,
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
        "boundary_risk": "Uniqueness is confined to the regular finite-circulation radial similarity class; zero age and zero viscosity are weak boundaries, r=0 is separate, and whole-plane kinetic energy diverges for nonzero circulation.",
        "collision_boundary": data["collision_boundary"],
        "excluded_from_manifest": [
            "C299_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C299_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
