#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C285 release."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from yaml.constructor import ConstructorError
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C285_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c285_gordon_newell_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C285/2026-09-02.yaml"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR_SNAPSHOT = {
    "skill": "route-a-evaluator",
    "version": "0.2.0",
    "semantic_token": EVAL,
    "scope_literal": SCOPE,
}
EPOCH = 1788307200
EVIDENCE_SHA = "981db83511e8bcccd0f8296ca98ae7a7035a475cba0661b3361836488c062106"
YAML_SHA = "bd1cf3e65ad4c957b2ebdaf01bbf8c5db7cf6b8afa179c8052b0d8135c86644e"
YAML_SEMANTIC_SHA = "d982f7573a7e79930eb4b0c4d8ee1a44a28bcf26bb2f4877127f74faaaea9cfa"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "281d88d391a2ca9fdf79ba30ac840959150bf9081954571e7c9543c0ea798fe5",
    "ab2bf74aa9be4ab4a1a33b1b584755ab505e807134514b40e9bdb781ea13052d",
    "088d2ca85d86d1e1fc797071bef5aa8c4a4364178f0ab61f454d77df14e6000e",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c285_gordon_newell_checker.py", "code/c285_gordon_newell_mutation.py",
    "code/c285_gordon_newell_producer.py", "code/c285_gordon_newell_replay.py",
    "code/c285_gordon_newell_sympy_crosscheck.py", "code/c285_release_manifest.py",
    "evaluations/route_a/HCS-C285/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c285_gordon_newell_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)

ROUTE_TOP_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority_sha256", "source_lock", "a0", "a1",
    "a2", "a3", "a4", "adversarial_controls", "overall_verdict", "tuple", "claim_boundary",
    "blocking_conditions", "next_smallest_test", "round2_clues", "route_b_invocation_allowed",
}
SOURCE_LOCK_KEYS = {"object", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                    "cutoff", "precision", "allowed_data", "forbidden_data"}
AXIS_KEYS = {
    "a0": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "arithmetic_controls", "artifacts"},
    "a1": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a2": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a3": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "weil_compression", "artifacts"},
    "a4": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
}
A2_METRIC_KEYS = {"zero_error_train", "zero_error_validation", "zero_error_test", "extra_zero_count",
                  "missing_zero_count", "root_count_discrepancy", "cutoff_drift", "precision_drift",
                  "control_margin"}


class UniqueSafeLoader(yaml.SafeLoader):
    """YAML loader that fails closed on duplicate and merge keys."""


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or key_node.value == "<<":
            raise ConstructorError("mapping", node.start_mark, "merge keys are forbidden", key_node.start_mark)
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ConstructorError("mapping", node.start_mark, "non-string mapping key", key_node.start_mark)
        if key in mapping:
            raise ConstructorError("mapping", node.start_mark, f"duplicate key {key!r}", key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique_object(pairs):
    """Reject duplicate JSON keys before any release assertion is evaluated."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def semantic_hash(data: dict) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def validate_route_carrier(doc: object) -> dict:
    assert isinstance(doc, dict) and set(doc) == ROUTE_TOP_KEYS
    assert doc["schema"] == "route-a-evaluation-v0.2.0"
    assert doc["skill"] == "route-a-evaluator" and doc["skill_version"] == "0.2.0"
    assert doc["candidate_id"] == "HCS-C285" and doc["source_commit"] == SOURCE
    assert doc["evaluation_date"] == "2026-09-02" and doc["fixed_epoch"] == EPOCH
    assert doc["scope_literal"] == SCOPE and doc["evaluator_authority_sha256"] == EVAL
    assert isinstance(doc["source_lock"], dict) and set(doc["source_lock"]) == SOURCE_LOCK_KEYS
    assert doc["source_lock"]["arithmetic_origin"].startswith("none;")
    assert doc["source_lock"]["determinant_convention"] == "none"
    assert all(token in doc["source_lock"]["forbidden_data"]
               for token in ("primes", "target zeros", "Euler factors", "root numbers", "Route-B"))
    for index, axis in enumerate(("a0", "a1", "a2", "a3", "a4")):
        record = doc[axis]
        assert isinstance(record, dict) and set(record) == AXIS_KEYS[axis]
        assert record["verdict"] == TUPLE[index] and record["evidence_status"] == "PROVED"
        assert isinstance(record["strongest_evidence"], str) and record["strongest_evidence"]
        assert isinstance(record["strongest_failure"], str) and record["strongest_failure"]
        artifacts = record["artifacts"]
        assert isinstance(artifacts, list) and artifacts and len(artifacts) == len(set(artifacts))
        for artifact in artifacts:
            assert isinstance(artifact, str) and not Path(artifact).is_absolute() and ".." not in Path(artifact).parts
            target = (ROOT / artifact).resolve()
            assert target.is_relative_to(ROOT.resolve()) and target.is_file()
    assert doc["a0"]["arithmetic_controls"] == ["station relabeling", "common traffic-gauge scaling",
                                                  "zero-edge irreducible routing", "dense nonreversible routing",
                                                  "all-equal weights"]
    assert doc["a1"]["metrics"] == {"positive_population_network_cases": 8, "exact_state_rows": 177,
                                      "independent_checker_assertions": 11628,
                                      "primitive_orbit_owner": "absent_for_stochastic_queueing_paths"}
    assert set(doc["a2"]["metrics"]) == A2_METRIC_KEYS
    assert all(isinstance(value, str) and value for value in doc["a2"]["metrics"].values())
    assert doc["a3"]["weil_compression"] == "absent and not inserted by hand"
    assert doc["a4"]["metrics"] == {
        "time_reversal_or_antiunitary": "stochastic_time_reversal_only_not_antiunitary_quantization",
        "same_clock_unitary_lift": "absent",
        "natural_hilbert_space": "finite weighted state space for Markov analysis only",
        "candidate_quantum_operator": "none",
    }
    assert set(doc["adversarial_controls"]) == {"controls_used", "proves_too_much_risk", "verdict"}
    assert len(doc["adversarial_controls"]["controls_used"]) == 6
    assert doc["adversarial_controls"]["verdict"] == "STOP_SCOPED"
    assert doc["tuple"] == TUPLE == [doc[f"a{i}"]["verdict"] for i in range(5)]
    assert doc["overall_verdict"] == "ROUTE_A_REJECTED"
    assert len(doc["blocking_conditions"]) == 4 and doc["round2_clues"] == []
    assert doc["route_b_invocation_allowed"] is False
    return doc


def parse_route_carrier(text: str) -> dict:
    tokens = list(yaml.scan(text))
    assert not any(isinstance(token, (AnchorToken, AliasToken)) for token in tokens)
    return validate_route_carrier(yaml.load(text, Loader=UniqueSafeLoader))


def route_carrier_hostile_controls(text: str) -> int:
    attacks = [
        text + "\nroute_b_invocation_allowed: true\n",
        text.replace("  cutoff: complete all-parameter", "  cutoff: duplicate\n  cutoff: complete all-parameter", 1),
        text.replace("  verdict: A0_FAIL", "  verdict: A0_FAIL\n  verdict: A0_WEAK_ARITHMETIC_RELATION", 1),
        text.replace("tuple:\n  - A0_FAIL", "tuple:\n  - A0_WEAK_ARITHMETIC_RELATION", 1),
        text.replace("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_ACCEPTED", 1),
        text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1),
        text + "\nunexpected_top_level: fail\n",
        "defaults: &defaults {}\n" + text,
        "defaults: &defaults {}\n" + text.replace("source_lock:\n", "source_lock:\n  <<: *defaults\n", 1),
    ]
    rejected = 0
    for attack in attacks:
        try:
            parse_route_carrier(attack)
        except (AssertionError, ConstructorError, yaml.YAMLError):
            rejected += 1
    assert rejected == len(attacks)
    return rejected


def is_sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
            or "__pycache__" in path.parts or path.name.endswith(".synctex.gz"))


def run_python(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def render_count(path: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="c285-render-") as temp:
        prefix = Path(temp) / "page"
        subprocess.run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        images = sorted(Path(temp).glob("page-*.png"))
        assert images and all(image.stat().st_size > 20000 for image in images)
        return len(images)


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c285-gordon-newell-r{round_number}-") as temp:
        work = Path(temp)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        assert not WARNING_RE.search(log)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    data = json.loads(EVIDENCE.read_text(), object_pairs_hook=unique_object)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c285-gordon-newell-bottleneck-v1"
    assert data["candidate_id"] == "HCS-C285" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-02" and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE and data["evaluator"] == {"version": "0.2.0", "sha256": EVAL}
    assert data["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert "classical Gordon--Newell ownership is explicit" in data["proof_contract"]["novelty_boundary"]
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED",
                                "route_b_invocation_allowed": False}
    assert all(value is False for value in data["scope_flags"].values())
    counts = data["regression"]["counts"]
    assert counts == {"case_rows": 9, "state_rows": 177, "z_rows": 9, "moment_rows": 9,
                      "factorial_cells": 165, "flow_rows": 9, "reversal_rows": 9,
                      "condensation_rows": 28, "boundary_rows": 12}
    assert data["boundary_contract"] == data["regression"]["boundary_rows"]

    assert digest(YAML) == YAML_SHA
    yaml_text = YAML.read_text()
    route_doc = parse_route_carrier(yaml_text)
    assert semantic_hash(route_doc) == YAML_SEMANTIC_SHA
    route_carrier_rejections = route_carrier_hostile_controls(yaml_text)

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free",
                  "embedded and subset", "visually inspected", "22/22", "23/23", "24/24"):
        assert token in compile_report, token
    tex_text = " ".join(TEX.read_text().split())
    for token in (r"\cite{GordonNewell1967}", r"\cite{Kelly1979}", r"\cite{KellyYudovina2014}",
                  "Those sources are cited for classical ownership and standard context",
                  "no literature originality is claimed", "Finite cells are regression oracles"):
        assert token in tex_text, token
    for token in (r"\mathcal S_N", r"\ifnum\CRevisionRound>1\relax\space Zero population"):
        assert token in tex_text, token
    assert "{cal S}_N" not in tex_text and "case.Zero population" not in tex_text
    checker_source = (ROOT / "code/c285_gordon_newell_checker.py").read_text()
    for token in ("validate_exact_json_schema(data)", "type(value) is expected",
                  'value == f"{parsed.numerator}/{parsed.denominator}"',
                  'integer_list(row["state"])'):
        assert token in checker_source, token
    mutation_source = (ROOT / "code/c285_gordon_newell_mutation.py").read_text()
    for token in ("route_boolean_as_integer", "scope_boolean_as_integer",
                  "rational_string_as_integer", "state_integer_as_boolean",
                  "noncanonical_fraction_text", "nested-duplicate-key.json"):
        assert token in mutation_source, token
    audit_text = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("C225", "C263", "C220", "C246", "C282", "C181", "No Gordon–Newell",
                  "not a split", "10.1287/opre.15.2.254", "10.1017/CBO9781139565363"):
        assert token in audit_text, token

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix not in {".pdf", ".json"} and "code" not in path.parts:
            text = path.read_text(errors="replace")
            assert "TODO" not in text and "FIXME" not in text and "[VERIFY]" not in text

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    assert PDF.read_bytes() == ROUND_PATHS[2].read_bytes()
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [2, 3, 4] and pdf_pages(PDF) == 4
    font_counts = []
    render_counts = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes"
                            for row in rows)
        font_counts.append(len(rows))
        render_counts.append(render_count(path))
    assert font_counts == [22, 23, 24] and render_counts == page_counts
    round_texts = [" ".join(subprocess.check_output(
        ["pdftotext", str(path), "-"], text=True).lower().split()) for path in ROUND_PATHS]
    common_tokens = ("canonical flow and bottleneck condensation", "gordon and newell",
                     "no literature originality", "or quantization is claimed")
    for round_number, round_text in enumerate(round_texts):
        assert f"revision round {round_number}" in round_text
        assert all(token in round_text for token in common_tokens)
        assert "cals" not in round_text and "case.zero" not in round_text
    assert "complete thermodynamic limit" in round_texts[1]
    assert "dirichlet(1, . . . , 1)" in round_texts[1]
    final_text = round_texts[2]
    for token in ("canonical flow and bottleneck condensation", "complete bottleneck limit",
                  "dirichlet(1, . . . , 1)", "boundary atlas", "gordon and newell", "11,628", "64/64",
                  "no literature originality", "or formal quantization is claimed", "a0_fail", "a4_fail",
                  "route_a_rejected", SCOPE.lower(), "10.1287/opre.15.2.254",
                  "10.1017/cbo9781139565363"):
        assert token in final_text, token
    assert "case. zero population" in final_text

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        one, _ = fresh_build(round_number)
        two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    producer = run_python("c285_gordon_newell_producer.py")
    checker = run_python("c285_gordon_newell_checker.py")
    sympy = run_python("c285_gordon_newell_sympy_crosscheck.py")
    replay = run_python("c285_gordon_newell_replay.py")
    mutation = run_python("c285_gordon_newell_mutation.py")
    assert "C285_PRODUCER_PASS" in producer and "C285 independent checker: PASS" in checker
    assert "C285_SYMPY_PASS" in sympy and "C285 double fresh-path byte replay: PASS" in replay
    cm = re.search(r"PASS \((\d+) assertions", checker)
    sm = re.search(r"PASS \((\d+) symbolic", sympy)
    mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and int(cm.group(1)) == 11628
    assert sm and int(sm.group(1)) == 28
    assert mm and mm.group(1) == mm.group(2) == "64"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c285-gordon-newell-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C285",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "theorem_status": data["proof_contract"]["status"],
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_canonical_product_form_and_fraction_left_nullspace": "PASS",
            "G2_three_way_partition_and_all_occupancy_derivatives": "PASS",
            "G3_station_edge_flows_and_time_reversal": "PASS",
            "G4_unique_tied_all_equal_condensation": "PASS",
            "G5_zero_equal_smallN_and_singular_boundaries": "PASS",
            "G6_strict_exact_json_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_paper_revisions": "PASS",
            "G8_deterministic_pdf_fonts_log_visual": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_classical_ownership_collision_traceability": "PASS",
            "G11_target_operator_route_b": "NOT_CLAIMED",
            "G12_unique_route_carrier_schema": "PASS",
            "G13_pdf_text_state_space_and_spacing_sentinels": "PASS",
        },
        "results": {
            **counts,
            "total_primary_rows": sum(value for key, value in counts.items() if key != "factorial_cells"),
            "checker_assertions": int(cm.group(1)), "sympy_checks": int(sm.group(1)),
            "hostile_rejections": int(mm.group(1)), "route_carrier_hostile_rejections": route_carrier_rejections,
            "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA, "pdf_pages": 4, "pdf_sha256": digest(PDF),
            "round_pdf_pages": page_counts, "rendered_page_counts": render_counts,
            "embedded_subset_font_rows": font_counts,
        },
        "route_a_verdict": data["route_a"],
        "route_a_carrier": {
            "yaml_sha256": YAML_SHA, "semantic_sha256": YAML_SEMANTIC_SHA,
            "tuple": route_doc["tuple"], "overall": route_doc["overall_verdict"],
            "duplicate_merge_alias_policy": "REJECT",
            "evaluator_snapshot": EVALUATOR_SNAPSHOT,
            "external_registry_byte_dependency": "none",
        },
        "classical_owner": data["citation_contract"]["classical_owner"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C285_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C285_MANIFEST_PASS", "payload_file_count": 27,
                      "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
