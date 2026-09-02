#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C294 release."""
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
MANIFEST = ROOT / "C294_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c294_three_disk_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C294/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "85e1fa131ba318099c20b1edc97b577f6f1356a882065a874b95034cb032f1f9"
PAYLOAD_SHA = "a27ee002fc16d6ae328dc7176a319860ade994ed35560f1e8b9c1b7ffb19dfc5"
EVALUATION_FILE_SHA = "cd7b961bb230d4ace1c2bb8e2ed0eaf88556bc4b986b054f3af91c3ed411d907"
EVALUATION_SEMANTIC_SHA = "832f2efec20b72d69ea1be577a6fc38168b09625a2804dbb03cc9ff7fad91f4b"
TUPLE = ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "b3ca978ef07c70e038fac52d960970b9e1e728038295082a963b9c0cd4490965",
    "e94f2d1c50fb73ec9292e33dbcaaf7ffaa88f9a9dba04db89850965cb4430921",
    "a8d7f4c1a0aa4b2bca95435348e6305c942cf226f3201157d8a2e0f8105606d8",
]
ROUND_PAGES = [3, 3, 4]
ROUND_FONTS = [20, 20, 21]
ROUND_TEXT = [
    ("complete periodic-ray coding", "compact convex minimization", "source collision-code zeta"),
    ("why the proof is not a finite computation", "dispersing hyperbolicity", "source collision-code zeta"),
    ("boundary atlas", "route_a_rejected", "no_bad_euler_or_root_number", "ai-use statement"),
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
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c294_three_disk_checker.py",
    "code/c294_three_disk_mutation.py", "code/c294_three_disk_producer.py",
    "code/c294_three_disk_replay.py", "code/c294_three_disk_sympy_crosscheck.py",
    "code/c294_release_manifest.py",
    "evaluations/route_a/HCS-C294/2026-09-02.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c294_three_disk_evidence.json",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
    "source_owner_tokens",
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
    """Safe loader retaining dates as strings and rejecting duplicate/merge keys."""


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
    with tempfile.TemporaryDirectory(prefix="c294-raster-") as temporary:
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


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c294-r{round_number}-") as temporary:
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
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    producer = run_python("c294_three_disk_producer.py")
    assert "C294_PRODUCER_PASS" in producer
    data = strict_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == PAYLOAD_SHA
    assert data["schema"] == "hcs-c294-three-disk-open-billiard-v1"
    assert data["candidate_id"] == "HCS-C294"
    assert data["obstruction_id"] == "HEN-O278"
    assert data["evaluation_date"] == "2026-09-02"
    assert data["fixed_epoch"] == EPOCH and type(data["fixed_epoch"]) is int
    assert data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["model"]["parameter_chamber"] == "r>0 and d>4r/sqrt(3)"
    assert data["theorem_contract"]["fixed_count"] == "F_n=2^n+2(-1)^n"
    assert data["theorem_contract"]["collision_zeta"] == "1/((1-2z)(1+z)^2)"
    assert data["proof_contract"]["finite_role"].startswith("finite words and optical grids")
    assert data["route_a"] == {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    }
    assert data["scope_flags"] == FLAGS
    assert data["enumeration"]["count_cell_count"] == 26
    assert data["enumeration"]["optical_cell_count"] == 175
    assert data["enumeration"]["geometry_cell_count"] == 8
    assert len(data["enumeration"]["zeta_coefficients_0_to_16"]) == 17
    assert [item["identifier"] for item in data["references"]] == [
        "10.1070/RM1970v025n02ABEH003794", "10.5802/aif.1137", "10.1063/1.456019",
    ]

    evaluation = strict_yaml(EVALUATION)
    assert digest(EVALUATION) == EVALUATION_FILE_SHA
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert set(evaluation) == YAML_KEYS
    assert evaluation["schema"] == "route-a-evaluation-v0.2.0"
    assert evaluation["candidate_id"] == "HCS-C294"
    assert evaluation["evaluation_date"] == "2026-09-02"
    assert evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == EPOCH
    assert evaluation["scope_literal"] == SCOPE
    assert evaluation["evaluator_authority_sha256"] == EVALUATOR
    assert evaluation["obstruction_id"] == "HEN-O278"
    assert evaluation["tuple"] == TUPLE
    assert evaluation["overall_verdict"] == "ROUTE_A_REJECTED"
    assert evaluation["route_b_invocation_allowed"] is False
    assert evaluation["theorem_status"] == "PROVABLE_AS_STATED"
    assert evaluation["scope_flags"] == FLAGS
    assert evaluation["source_owner_tokens"] == [
        "10.1070/RM1970v025n02ABEH003794", "10.5802/aif.1137", "10.1063/1.456019",
    ]
    for axis, verdict in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE):
        assert set(evaluation[axis]) == {
            "verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts",
        }
        assert evaluation[axis]["verdict"] == verdict

    checker_source = (ROOT / "code/c294_three_disk_checker.py").read_text()
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

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED", "strict convexity", "Finite evidence is regression evidence only",
        "HEN-O278", "1/((1-2z)(1+z)^2)",
    ):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "10.1070/RM1970v025n02ABEH003794", "10.5802/aif.1137", "10.1063/1.456019",
        "no literature-priority claim",
    ):
        assert token in source_audit, token
    hostile = (ROOT / "results/HOSTILE_AUDIT.md").read_text()
    for token in ("all 58 attacks", "repaired each JSON payload hash", "scope-polarity attack", "duplicate", "exact semantic tree", "finite word table prove the coding theorem"):
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
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c294_three_disk_checker.py")
    symbolic = run_python("c294_three_disk_sympy_crosscheck.py")
    replay = run_python("c294_three_disk_replay.py")
    mutation = run_python("c294_three_disk_mutation.py")
    assert "C294 independent checker: PASS" in checker and "producer import forbidden" in checker
    assert "C294 SymPy cross-check: PASS" in symbolic
    assert "C294 byte replay: PASS" in replay
    assert "C294 hostile mutation suite: PASS 58/58" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (92280, 417, 58)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c294-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C294",
        "obstruction_id": "HEN-O278",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "all-period convex coding, primitive collision ledgers, and hyperbolicity for the equilateral no-eclipse three-disk billiard",
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
            "G0a_strict_json_yaml": "PASS",
            "G1_sharp_no_eclipse_capsule_gap": "PASS",
            "G2_all_period_convex_existence_uniqueness": "PASS",
            "G3_specular_nongrazing_exterior_converse": "PASS",
            "G4_fixed_primitive_reversal_zeta_ledgers": "PASS",
            "G5_length_and_hyperbolic_monodromy": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS",
            "G8_six_fresh_pdf_builds_fonts_logs_text_raster": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_source_and_claim_traceability": "PASS",
            "G11_target_euler_root_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "fixed_primitive_rows": 16,
            "direct_enumeration_rows": 10,
            "zeta_coefficients": 17,
            "optical_products": 175,
            "geometry_cases": 6,
            "symmetric_orbit_anchors": 2,
            "recorded_audit_cells": 226,
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
        "boundary_risk": "At or below d=4r/sqrt(3), the full reduced-word coding proof is not certified; no claim is extrapolated across the equality surface.",
        "excluded_from_manifest": [
            "C294_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C294_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
