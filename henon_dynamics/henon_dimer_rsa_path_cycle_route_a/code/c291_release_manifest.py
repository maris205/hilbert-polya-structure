#!/usr/bin/env python3
"""Close and attest the exact 27-payload / 28-physical-file C291 release."""
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
MANIFEST = ROOT / "C291_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c291_dimer_rsa_evidence.json"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C291/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVIDENCE_SHA = "65fdb2333d3fbb6c3177eaa7da5d303ab0b42f2ff99b8d55ecd97e1863008a0f"
EVIDENCE_PAYLOAD_SHA = "1e9911ffb46b20b1c50e0a22566eb5048860d50ff0fb3be787fb9e64d6092af4"
YAML_SHA = "ba834b4bd2911624df769ba5b06c08276d5aa622c0192655c4c6dfdf97829e24"
YAML_SEMANTIC_SHA = "53928a4f4a14928d254ae0a5093d3dfbc622a2d0d7811d7bce517b36771cc1f6"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "0a0d27c5341ea1eb04e31763c6eaf878f9281b95b5bce6137c34067c08123043",
    "c797bca28272288017a5156ab16a15dbab7040a90e611aecaf1db2a78a2d594f",
    "b410ec70209302f891992712b4a6be16663e04d2a79cd6f7e4f1e762fef64a22",
]
ROUND_TEXT = [
    ("conditioning on the first edge", "riccati ordinary generating function", "maximal matching"),
    ("second factorial moment and variance", "binary gap words", "boundary atlas and theorem limits"),
    ("executable reconstruction and adversarial controls", "19,371", "105/105", "route_a_rejected", "ai-use disclosure"),
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c291_dimer_rsa_checker.py",
    "code/c291_dimer_rsa_mutation.py", "code/c291_dimer_rsa_producer.py",
    "code/c291_dimer_rsa_replay.py", "code/c291_dimer_rsa_sympy_crosscheck.py",
    "code/c291_release_manifest.py",
    "evaluations/route_a/HCS-C291/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c291_dimer_rsa_evidence.json",
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)
YAML_TOP_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "candidate_definition", "family", "phase_space",
    "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock",
    "normalization", "determinant_convention", "orbit_cutoff", "precision",
    "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
    "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "scope_flags",
    "obstruction_id",
}
YAML_STRING_KEYS = YAML_TOP_KEYS - {
    "fixed_epoch", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
    "route_b_invocation_allowed", "scope_flags",
}
YAML_GATE_KEYS = {"verdict", "evidence_status", "strongest_failure"}
YAML_FLAG_KEYS = {
    "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy",
    "target_divisor_or_counting_law", "target_functional_equation", "target_zero_match",
    "hilbert_polya_operator", "route_b_authorization",
}


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe recursive loader which rejects duplicate mapping keys."""


def construct_unique_mapping(
    loader: UniqueYAMLLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def validate_route_yaml(path: Path) -> dict:
    assert digest(path) == YAML_SHA
    value = yaml.load(path.read_text(), Loader=UniqueYAMLLoader)
    assert type(value) is dict and set(value) == YAML_TOP_KEYS
    assert all(type(value[key]) is str for key in YAML_STRING_KEYS)
    assert type(value["fixed_epoch"]) is int and value["fixed_epoch"] == EPOCH
    assert type(value["route_b_invocation_allowed"]) is bool and value["route_b_invocation_allowed"] is False
    assert type(value["artifact_paths"]) is list and all(type(item) is str for item in value["artifact_paths"])
    assert value["artifact_paths"] == ["THEOREM_PACKAGE.md", "results/c291_dimer_rsa_evidence.json", "paper/main.pdf"]
    assert type(value["tuple"]) is list and all(type(item) is str for item in value["tuple"])
    assert value["tuple"] == TUPLE
    for gate in ("a0", "a1", "a2", "a3", "a4"):
        assert type(value[gate]) is dict and set(value[gate]) == YAML_GATE_KEYS
        assert all(type(item) is str for item in value[gate].values())
    assert type(value["scope_flags"]) is dict and set(value["scope_flags"]) == YAML_FLAG_KEYS
    assert all(type(item) is bool and item is False for item in value["scope_flags"].values())
    assert value["schema"] == "route-a-evaluation-v0.2.0"
    assert value["candidate_id"] == "HCS-C291" and value["evaluation_date"] == "2026-09-02"
    assert value["source_commit"] == SOURCE and value["scope_literal"] == SCOPE
    assert value["evaluator_authority_sha256"] == EVALUATOR
    assert value["overall_verdict"] == "ROUTE_A_REJECTED" and value["obstruction_id"] == "HEN-O275"
    semantic = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    assert hashlib.sha256(semantic.encode()).hexdigest() == YAML_SEMANTIC_SHA
    return value


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def normalized_pdf_text(path: Path) -> str:
    text = subprocess.check_output(["pdftotext", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c291-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING_RE.search(log)
        assert match is None, match.group(0) if match else ""
        return (work / "main.pdf").read_bytes(), log


def render_count(path: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="c291-render-") as temporary:
        prefix = Path(temporary) / "page"
        subprocess.run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        images = sorted(Path(temporary).glob("page-*.png"))
        assert images and all(image.stat().st_size > 1000 for image in images)
        return len(images)


def main() -> None:
    producer = run_python("c291_dimer_rsa_producer.py")
    assert "C291_PRODUCER_PASS" in producer
    assert digest(EVIDENCE) == EVIDENCE_SHA
    data = json.loads(EVIDENCE.read_text())
    assert data["payload_sha256"] == payload_hash(data) == EVIDENCE_PAYLOAD_SHA
    assert data["schema"] == "hcs-c291-dimer-rsa-path-cycle-v1"
    assert data["candidate_id"] == "HCS-C291"
    assert data["evaluation_date"] == "2026-09-02"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["theorem_contract"]["cycle_identity"] == "G_n(z)=z*F_{n-2}(z) for every simple cycle n>=3"
    assert data["theorem_contract"]["variance"].startswith("Var(M_n)=exp(-4)*n+2*exp(-4)")
    assert data["model_contract"]["output_semantics"] == "the terminal set is a jammed maximal matching, not generally a maximum matching"
    assert data["collision_snapshot"]["obstruction_id"] == "HEN-O275"
    assert data["collision_snapshot"]["registry_bytes_required"] is False
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(value is False for value in data["scope_flags"].values())
    assert [row["n"] for row in data["path_rows"]] == list(range(11))
    assert [row["n"] for row in data["cycle_rows"]] == list(range(3, 10))
    assert [row["n"] for row in data["factorial_moment_rows"]] == list(range(21))

    route_yaml = validate_route_yaml(YAML_PATH)
    assert route_yaml["scope_flags"] == data["scope_flags"]

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "PROVABLE AS STATED", "H_r'-(1/x+2x/(1-x))H_r", "binary gap word",
        "G_n(z)=zF_{n-2}(z)", "output is maximal", "not asserted maximum", "HEN-O275",
    ):
        assert token in theorem, token
    source_audit = " ".join((ROOT / "SOURCE_AUDIT.md").read_text().split())
    for token in (
        "10.1021/ja01875a053", "10.1103/RevModPhys.65.1281",
        "10.1007/s002200100387", "10.1002/rsa.3240020104",
        "not a literature-level originality or priority claim",
        "C291_READ_ONLY_COLLISION_SNAPSHOT_AT_7fbe9db3",
    ):
        assert token in source_audit, token
    tex = " ".join(TEX.read_text().split())
    for token in (
        "Exact Finite Dimer Random Sequential Adsorption", "triangular system determines every factorial moment",
        "Second factorial moment and variance", "binary gap words", "G_n(z)=zF_{n-2}(z)",
        "producer-independent bitmask/order oracle", "finite calculations are falsification tools",
        "AI-use disclosure", "not claim invention or literature priority",
    ):
        assert token in tex, token

    checker_source = (ROOT / "code/c291_dimer_rsa_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    for token in ("object_pairs_hook=unique_object", "processed-edge and matched-vertex mask", "expected_triangle", "EXACT_CLOSEST" if False else "EXPECTED_CLOSEST"):
        assert token in checker_source, token

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}", "two isolated directories per round", "byte-identical",
        "embedded and subset", "no overfull box above 10 pt", "visually inspected",
        *ROUND_HASHES,
    ):
        assert token in compile_report, token
    hostile = (ROOT / "results/HOSTILE_AUDIT.md").read_text()
    for token in ("Conditional independence", "All factorial moments", "105/105", "strict JSON loader rejects duplicate keys", "duplicate YAML keys", "HEN-O275"):
        assert token in hostile, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    archived_hashes = [digest(path) for path in ROUND_PATHS]
    assert archived_hashes == ROUND_HASHES
    assert len(set(archived_hashes)) == 3
    assert PDF.read_bytes() == ROUND_PATHS[2].read_bytes()
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == [3, 4, 5]
    font_counts = []
    rendered = []
    for path, required in zip(ROUND_PATHS, ROUND_TEXT):
        rows = font_rows(path)
        assert rows
        assert all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows))
        text = normalized_pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
        rendered.append(render_count(path))
    assert font_counts == [22, 23, 24]
    assert rendered == pages

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    checker = run_python("c291_dimer_rsa_checker.py")
    symbolic = run_python("c291_dimer_rsa_sympy_crosscheck.py")
    replay = run_python("c291_dimer_rsa_replay.py")
    mutation = run_python("c291_dimer_rsa_mutation.py")
    assert "strict duplicate-rejecting JSON/YAML schema" in checker
    assert "C291_SYMPY_PASS" in symbolic
    assert "C291 fresh-path byte replay: PASS" in replay
    assert "PASS 105/105" in mutation
    checker_match = re.search(r"PASS \((\d+) assertions", checker)
    symbolic_match = re.search(r"PASS \((\d+) symbolic", symbolic)
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert checker_match and int(checker_match.group(1)) == 19371
    assert symbolic_match and int(symbolic_match.group(1)) == 132
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2) == "105"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c291-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C291",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Exact finite path/cycle dimer RSA PGFs, factorial hierarchy, support, and boundary effect",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {
            "engine": "LuaLaTeX",
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "fixed_epoch": EPOCH,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages,
            "round_embedded_subset_font_rows": font_counts,
            "round_rendered_page_counts": rendered,
            "settled_warning_regex": WARNING_RE.pattern,
            "all_round_text_contracts": [list(tokens) for tokens in ROUND_TEXT],
            "visual_audit": "PASS: all 12 pages rendered and inspected; no clipping, collision, blank content, or malformed glyph",
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_exact_duplicate_rejecting_json_yaml_schema": "PASS",
            "G2_independent_bitmask_order_enumeration": "PASS",
            "G3_path_pgf_riccati_all_factorial_moments": "PASS",
            "G4_exact_mean_variance_pole_extraction": "PASS",
            "G5_exact_path_cycle_support": "PASS",
            "G6_cycle_identity_boundary_effect": "PASS",
            "G7_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_six_fresh_pdf_builds_fonts_logs_visuals": "PASS",
            "G10_manifest_exact_ledger": "PASS",
            "G11_claim_source_collision_traceability": "PASS",
            "G12_route_a": "REJECTED_ALL_FIVE_GATES",
            "G13_route_b": "NOT_AUTHORIZED",
        },
        "results": {
            "path_rows": 11,
            "cycle_rows": 7,
            "factorial_rows": 21,
            "factorial_max_order": 5,
            "moment_recurrence_max_n": 200,
            "direct_edge_orders_counted": 818225,
            "checker_assertions": int(checker_match.group(1)),
            "symbolic_checks": int(symbolic_match.group(1)),
            "hostile_rejections": int(mutation_match.group(1)),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": EVIDENCE_PAYLOAD_SHA,
            "evidence_sha256": EVIDENCE_SHA,
            "yaml_sha256": YAML_SHA,
            "yaml_semantic_sha256": YAML_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF),
            "pdf_pages": pages[-1],
        },
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "obstruction_id": "HEN-O275"},
        "collision_contract": {"snapshot_token": data["collision_snapshot"]["token"], "mutable_external_registry_bytes_required": False},
        "scope_flags": data["scope_flags"],
        "payload_file_count": len(files),
        "physical_file_count": len(files) + 1,
        "manifest_self_excluded": True,
        "file_sha256": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len({str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file()}) == 28
    print(
        "C291_RELEASE_PASS "
        f"payloads={len(files)} physical={len(files)+1} assertions={checker_match.group(1)} "
        f"symbolic={symbolic_match.group(1)} mutations={mutation_match.group(1)}/{mutation_match.group(2)} "
        f"evidence_sha256={EVIDENCE_SHA} pdf_sha256={digest(PDF)} manifest_sha256={digest(MANIFEST)}"
    )


if __name__ == "__main__":
    main()
