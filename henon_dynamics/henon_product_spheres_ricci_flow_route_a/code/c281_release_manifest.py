#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C281 release."""
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
MANIFEST = ROOT / "C281_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c281_ricci_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C281/2026-09-01.yaml"
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
EVIDENCE_SHA = "c3670de8df2b2171eba51ee5616550601c347c0315ee6867b90be98686328ac5"
YAML_SHA = "8cca798a07b7990de881f709dd56a4f02845284c42a0d6010d10d31e92dff660"
YAML_SEMANTIC_SHA = "22b431fd2794b1d14ab67c8ba9ace8774ba6d2858512e49c4fac887047c7d14f"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "5659c753df3f3823ff40b8a6640a5010a9d8898d6256a09098ef40bf488ec139",
    "780fe2fdd67de3b12768212711c45d7ab073c4b1758809f557bb973739b0b4d3",
    "93b6aaf8229ec317c4933cf5bf264f82501c64ec1c7121625f2b27860e6a4d8a",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c281_ricci_checker.py", "code/c281_ricci_mutation.py",
    "code/c281_ricci_producer.py", "code/c281_ricci_replay.py",
    "code/c281_ricci_sympy_crosscheck.py", "code/c281_release_manifest.py",
    "evaluations/route_a/HCS-C281/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c281_ricci_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)

ROUTE_TOP_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "source_commit",
    "evaluation_date", "fixed_epoch", "scope_literal",
    "evaluator_authority_sha256", "source_lock", "a0", "a1", "a2", "a3",
    "a4", "adversarial_controls", "tuple", "overall_verdict",
    "claim_boundary", "blocking_conditions", "next_smallest_test",
    "round2_clues", "route_b_invocation_allowed",
}
SOURCE_LOCK_KEYS = {
    "object", "arithmetic_origin", "clock", "normalization",
    "determinant_convention", "cutoff", "precision", "allowed_data",
    "forbidden_data",
}
AXIS_KEYS = {
    "a0": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "arithmetic_controls", "artifacts"},
    "a1": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a2": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a3": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "weil_compression", "artifacts"},
    "a4": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
}
A2_METRIC_KEYS = {
    "zero_error_train", "zero_error_validation", "zero_error_test",
    "extra_zero_count", "missing_zero_count", "root_count_discrepancy",
    "cutoff_drift", "precision_drift", "control_margin",
}


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate and merge keys."""


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


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def semantic_hash(data: dict) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def validate_route_carrier(doc: object) -> dict:
    assert isinstance(doc, dict) and set(doc) == ROUTE_TOP_KEYS
    assert doc["schema"] == "route-a-evaluation-v0.2.0"
    assert doc["skill"] == "route-a-evaluator" and doc["skill_version"] == "0.2.0"
    assert doc["candidate_id"] == "HCS-C281" and doc["source_commit"] == SOURCE
    assert doc["evaluation_date"] == "2026-09-01" and doc["fixed_epoch"] == EPOCH
    assert doc["scope_literal"] == SCOPE and doc["evaluator_authority_sha256"] == EVAL
    assert isinstance(doc["source_lock"], dict) and set(doc["source_lock"]) == SOURCE_LOCK_KEYS
    assert doc["source_lock"]["arithmetic_origin"].startswith("none;")
    assert doc["source_lock"]["determinant_convention"] == "none"
    forbidden = doc["source_lock"]["forbidden_data"]
    assert all(token in forbidden for token in ("primes", "target zeros", "Euler factors", "root numbers", "Route-B"))

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

    assert set(doc["a1"]["metrics"]) == {
        "nonconstant_periodic_orbits", "primitive_orbit_owner",
        "analytic_and_boundary_rows", "independent_checker_assertions",
    }
    assert doc["a1"]["metrics"] == {
        "nonconstant_periodic_orbits": 0,
        "primitive_orbit_owner": "absent_by_strict_volume_monotonicity",
        "analytic_and_boundary_rows": 218,
        "independent_checker_assertions": 2063,
    }
    assert set(doc["a2"]["metrics"]) == A2_METRIC_KEYS
    assert all(isinstance(value, str) and value for value in doc["a2"]["metrics"].values())
    assert set(doc["a4"]["metrics"]) == {
        "time_reversal_or_antiunitary", "same_clock_unitary_lift",
        "natural_hilbert_space", "candidate_quantum_operator",
    }
    assert isinstance(doc["a0"]["arithmetic_controls"], list) and len(doc["a0"]["arithmetic_controls"]) == 5
    assert doc["a3"]["weil_compression"] == "absent and not inserted by hand"
    assert set(doc["adversarial_controls"]) == {"controls_used", "proves_too_much_risk", "verdict"}
    assert len(doc["adversarial_controls"]["controls_used"]) == 6
    assert doc["adversarial_controls"]["verdict"] == "STOP_SCOPED"
    assert doc["tuple"] == TUPLE == [doc[f"a{i}"]["verdict"] for i in range(5)]
    assert doc["overall_verdict"] == "ROUTE_A_REJECTED"
    assert isinstance(doc["blocking_conditions"], list) and len(doc["blocking_conditions"]) == 4
    assert doc["round2_clues"] == [] and doc["route_b_invocation_allowed"] is False
    return doc


def parse_route_carrier(text: str) -> dict:
    tokens = list(yaml.scan(text))
    assert not any(isinstance(token, (AnchorToken, AliasToken)) for token in tokens)
    return validate_route_carrier(yaml.load(text, Loader=UniqueSafeLoader))


def route_carrier_hostile_controls(text: str) -> int:
    attacks = [
        text + "\nroute_b_invocation_allowed: true\n",
        text.replace("  cutoff: complete all-parameter theorem;", "  cutoff: duplicate\n  cutoff: complete all-parameter theorem;", 1),
        text.replace("  verdict: A0_FAIL", "  verdict: A0_FAIL\n  verdict: A0_WEAK_ARITHMETIC_RELATION", 1),
        text.replace("tuple:\n  - A0_FAIL", "tuple:\n  - A0_WEAK_ARITHMETIC_RELATION", 1),
        "defaults: &defaults {}\n" + text,
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
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name: str) -> str:
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    out = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c281-ricci-r{round_number}-") as temp:
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
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c281-product-spheres-ricci-flow-v1"
    assert data["candidate_id"] == "HCS-C281" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-01" and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE and data["evaluator"]["sha256"] == EVAL
    assert data["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert data["classification_contract"]["partial_full_gate"] == "D<n iff normalized endpoint finite; D=n iff data are curved Einstein and normalized flow is stationary"
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(value is False for value in data["scope_flags"].values())
    counts = data["regression"]["counts"]
    assert counts == {"case_rows": 14, "flow_rows": 68, "normalized_rows": 66, "collapse_rows": 12,
                      "asymptotic_rows": 36, "covariance_rows": 14, "boundary_rows": 8}

    authority = ROOT.parents[1] / "flow_systems/skills/route-a-evaluator.md"
    assert digest(authority) == EVAL
    assert digest(YAML) == YAML_SHA
    yaml_text = YAML.read_text()
    route_doc = parse_route_carrier(yaml_text)
    assert semantic_hash(route_doc) == YAML_SEMANTIC_SHA
    route_carrier_rejections = route_carrier_hostile_controls(yaml_text)
    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free", "embedded and subset", "visually inspected"):
        assert token in compile_report, token
    tex_text = " ".join(TEX.read_text().split())
    for token in (r"\cite{Hamilton1982}", r"\cite{ChowKnopf2004}",
                  "Those sources are cited only for equation lineage and vocabulary",
                  "All product, endpoint, and normalization claims below are derived here"):
        assert token in tex_text, token
    audit_text = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("C185", "C270", "C277", "C283", "C133", "returned no prior owner",
                  "not a split of C283", "10.4310/jdg/1214436922", "10.1090/surv/110"):
        assert token in audit_text, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED-set(files)), sorted(set(files)-EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [2, 3, 4] and pdf_pages(PDF) == 4
    font_counts = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows))
    assert font_counts == [22, 22, 23]
    final_text = " ".join(subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower().split())
    for token in ("exact singularities of homogeneous ricci flow", "tied collapse", "constant-volume conjugacy",
                  "partial versus full collapse", "pointed", "flat torus", "2,063", "52/52",
                  "a0_fail", "a1_fail", "route_a_rejected", SCOPE.lower(),
                  "10.4310/jdg/1214436922", "10.1090/surv/110"):
        assert token in final_text, token

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        one, _ = fresh_build(round_number); two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    producer = run_python("c281_ricci_producer.py")
    checker = run_python("c281_ricci_checker.py")
    sympy = run_python("c281_ricci_sympy_crosscheck.py")
    replay = run_python("c281_ricci_replay.py")
    mutation = run_python("c281_ricci_mutation.py")
    assert "C281_PRODUCER_PASS" in producer and "C281 independent checker: PASS" in checker
    assert "C281_SYMPY_PASS" in sympy and "C281 byte replay: PASS" in replay
    cm = re.search(r"PASS \((\d+) assertions", checker)
    sm = re.search(r"PASS \((\d+) symbolic", sympy)
    mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and int(cm.group(1)) == 2063
    assert sm and int(sm.group(1)) == 20
    assert mm and mm.group(1) == mm.group(2) == "52"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c281-product-spheres-ricci-release-v1", "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C281", "evaluation_date": "2026-09-01", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE, "headline": data["headline"],
        "theorem_status": data["proof_contract"]["status"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
                           "fresh_builds_per_round": 2,
                           "round_artifacts": [str(p.relative_to(ROOT)) for p in ROUND_PATHS],
                           "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
                           "final_equals": "paper/main_round2.pdf"},
        "gates": {
            "G0_source_scope_evaluator": "PASS", "G1_exact_product_flow": "PASS",
            "G2_flat_factors_and_tied_clocks": "PASS", "G3_curvature_volume_diameter": "PASS",
            "G4_type_I_pointed_blowup": "PASS", "G5_normalized_time_partial_full_gate": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS", "G7_two_substantive_revisions": "PASS",
            "G8_deterministic_pdf_fonts_log_visual": "PASS", "G9_manifest_hash_closure": "PASS",
            "G10_claim_source_collision_traceability": "PASS", "G11_target_operator_route_b": "NOT_CLAIMED",
            "G12_unique_route_carrier_schema": "PASS",
        },
        "results": {**counts, "total_analytic_boundary_rows": sum(counts.values()),
                    "checker_assertions": int(cm.group(1)), "sympy_checks": int(sm.group(1)),
                    "hostile_rejections": int(mm.group(1)), "pdf_pages": 4,
                    "route_carrier_hostile_rejections": route_carrier_rejections,
                    "round_pdf_pages": page_counts, "embedded_subset_font_rows": font_counts,
                    "evidence_bytes": EVIDENCE.stat().st_size,
                    "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": EVIDENCE_SHA,
                    "pdf_sha256": digest(PDF)},
        "route_a_verdict": data["route_a"], "route_a_carrier": {
            "yaml_sha256": YAML_SHA, "semantic_sha256": YAML_SEMANTIC_SHA,
            "tuple": route_doc["tuple"], "overall": route_doc["overall_verdict"],
            "duplicate_merge_alias_policy": "REJECT",
        }, "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C281_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C281_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA,
                      "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
