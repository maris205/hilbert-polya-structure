#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C284 release."""
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
MANIFEST = ROOT / "C284_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c284_point_vortex_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C284/2026-09-02.yaml"
SOURCE_AUDIT = ROOT / "SOURCE_AUDIT.md"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "4fed9820df14c399e53fb3e616d3451297ebd055f78f8123fcdfb39db9462a53"
YAML_SHA = "0bab3830179a0e5ce89a9986027a83fa0c23ee952edad96b7b2015dfdbcbec49"
YAML_SEMANTIC_SHA = "93c65d5ccbda2a2f12df328f329be5220f04961c2240965d9da1f943c9a7b268"
REGISTRY_SNAPSHOT_SHA = "c8fb9282ba71c6ec4d4cf596a571bcd98ee73488d1e21acb63eb6793e29fff32"
OBSTRUCTION_SNAPSHOT_SHA = "bc790201679af48bdda3e924f3f1bd66b3cc1ffd5302868f5836d9ae96cbf9c6"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "84ffd06198298313ea07c65d9a857261f3546be11fbfa7f0add3f28945e683e5",
    "7f838e6c0863795737bcd76fa0d36f4c089731b8c1e1bd5687e4e2dd589ad53d",
    "6b1501af2dba761ad34e87cc89502c8f4ba8e9c8bb04ed7771ef49f6bf009f6f",
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
    "code/c284_point_vortex_checker.py",
    "code/c284_point_vortex_mutation.py",
    "code/c284_point_vortex_producer.py",
    "code/c284_point_vortex_replay.py",
    "code/c284_point_vortex_sympy_crosscheck.py",
    "code/c284_release_manifest.py",
    "evaluations/route_a/HCS-C284/2026-09-02.yaml",
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
    "results/c284_point_vortex_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)

ROUTE_TOP_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "evaluation_date",
    "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority",
    "evaluator_authority_sha256", "source_lock", "a0", "a1", "a2", "a3",
    "a4", "adversarial_controls", "overall_verdict", "tuple",
    "claim_boundary", "blocking_conditions", "next_smallest_test",
    "round2_clues", "route_b_invocation_allowed", "nonclaims",
}
SOURCE_LOCK_KEYS = {
    "object", "arithmetic_origin", "clock", "normalization",
    "angular_velocity", "determinant_convention", "cutoff", "precision",
    "allowed_data", "forbidden_data",
}
AXIS_KEYS = {
    "a0": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "arithmetic_controls", "artifacts"},
    "a1": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a2": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    "a3": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "weil_compression", "artifacts"},
    "a4": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
}
ROUTE_NONCLAIM_KEYS = {
    "nonlinear_heptagon_stability", "arithmetic_local_data", "euler_factors",
    "root_numbers", "automorphy", "target_divisor_or_counting_law",
    "target_functional_equation", "target_zero_match",
    "hilbert_polya_operator", "route_b_authorization",
}


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate and merge keys."""


def construct_unique_mapping(
    loader: UniqueSafeLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or key_node.value == "<<":
            raise ConstructorError(
                "mapping", node.start_mark, "merge keys are forbidden",
                key_node.start_mark,
            )
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise ConstructorError(
                "mapping", node.start_mark, "non-string mapping key",
                key_node.start_mark,
            )
        if key in mapping:
            raise ConstructorError(
                "mapping", node.start_mark, f"duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique_json_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string JSON key: {key!r}")
        result[key] = value
    return result


def reject_json_constant(token: str) -> None:
    raise ValueError(f"nonstandard JSON constant: {token}")


def load_json_strict(path: Path) -> dict:
    value = json.loads(
        path.read_text(), object_pairs_hook=unique_json_object,
        parse_constant=reject_json_constant,
    )
    assert type(value) is dict
    return value


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(
        clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(data: dict) -> str:
    raw = json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def validate_artifacts(value: object) -> None:
    assert type(value) is list and value and len(value) == len(set(value))
    for artifact in value:
        assert type(artifact) is str
        path = Path(artifact)
        assert not path.is_absolute() and ".." not in path.parts
        target = (ROOT / path).resolve()
        assert target.is_relative_to(ROOT.resolve()) and target.is_file()


def validate_route_carrier(doc: object) -> dict:
    assert type(doc) is dict and set(doc) == ROUTE_TOP_KEYS
    assert doc["schema"] == "route-a-evaluation-v0.2.0"
    assert doc["skill"] == "route-a-evaluator"
    assert doc["skill_version"] == "0.2.0"
    assert doc["candidate_id"] == "HCS-C284"
    assert doc["evaluation_date"] == "2026-09-02"
    assert doc["source_commit"] == SOURCE
    assert type(doc["fixed_epoch"]) is int and doc["fixed_epoch"] == EPOCH
    assert doc["scope_literal"] == SCOPE
    assert doc["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md"
    assert doc["evaluator_authority_sha256"] == EVAL

    lock = doc["source_lock"]
    assert type(lock) is dict and set(lock) == SOURCE_LOCK_KEYS
    assert all(type(value) is str and value for value in lock.values())
    assert lock["clock"] == "physical point-vortex time"
    assert lock["angular_velocity"] == "Omega=Gamma*(N-1)/(4*pi*R^2)"
    assert lock["determinant_convention"].startswith("none;")
    assert lock["cutoff"].startswith("complete all-N analytic theorem;")
    for token in ("primes", "target zeros", "Euler factors", "root numbers", "Route-B"):
        assert token in lock["forbidden_data"]

    for index, axis in enumerate(("a0", "a1", "a2", "a3", "a4")):
        record = doc[axis]
        assert type(record) is dict and set(record) == AXIS_KEYS[axis]
        assert record["verdict"] == TUPLE[index]
        assert record["evidence_status"] == "PROVED"
        assert type(record["strongest_evidence"]) is str and record["strongest_evidence"]
        assert type(record["strongest_failure"]) is str and record["strongest_failure"]
        validate_artifacts(record["artifacts"])

    assert doc["a0"]["arithmetic_controls"] == [
        "neighboring_N", "Gamma_scaling", "radius_scaling",
        "negative_common_circulation", "N_below_domain",
    ]
    assert doc["a1"]["metrics"] == {
        "analytic_mode_rows": 2077,
        "polygon_rows": 62,
        "symmetry_slice_rows": 7,
        "independent_checker_assertions": 65655,
        "hostile_mutations_rejected": 76,
        "primitive_orbit_owner": "absent",
        "relative_rotation_clock": (
            "Omega=Gamma*(N-1)/(4*pi*R^2); labeled and unlabeled return "
            "conventions are not conflated"
        ),
    }
    assert doc["a2"]["metrics"] == {
        "target_determinant": "absent",
        "target_zero_comparison": "not_applicable",
        "extra_zero_count": "not_applicable",
        "missing_zero_count": "not_applicable",
    }
    assert doc["a3"]["analytic_structure"] == (
        "finite-dimensional source-local linear spectrum only"
    )
    assert doc["a3"]["weil_compression"] == "absent"
    assert doc["a4"]["metrics"] == {
        "natural_hilbert_space": "absent for the claimed theorem",
        "same_clock_unitary_lift": "absent",
        "candidate_quantum_operator": "none",
    }

    controls = doc["adversarial_controls"]
    assert type(controls) is dict and set(controls) == {
        "controls_used", "proves_too_much_risk", "strongest_control", "verdict"
    }
    assert controls["controls_used"] == [
        "Gamma_half", "Gamma_five", "R_half", "R_four",
        "Gamma_zero_boundary", "Gamma_negative_boundary", "N_equals_7",
        "N_equals_8", "N_equals_64",
    ]
    assert type(controls["proves_too_much_risk"]) is str
    assert type(controls["strongest_control"]) is str
    assert controls["verdict"] == "STOP_SCOPED"
    assert doc["tuple"] == TUPLE == [doc[f"a{i}"]["verdict"] for i in range(5)]
    assert doc["overall_verdict"] == "ROUTE_A_REJECTED"
    assert doc["claim_boundary"] == (
        "exact reduced linear-stability theorem for one equal-circulation "
        "planar regular polygon only"
    )
    assert type(doc["blocking_conditions"]) is list
    assert len(doc["blocking_conditions"]) == 4
    assert all(type(value) is str and value for value in doc["blocking_conditions"])
    assert len(doc["blocking_conditions"]) == len(set(doc["blocking_conditions"]))
    assert doc["next_smallest_test"] == (
        "none; retain as a closed classical source theorem"
    )
    assert doc["round2_clues"] == []
    assert doc["route_b_invocation_allowed"] is False
    assert type(doc["nonclaims"]) is dict and set(doc["nonclaims"]) == ROUTE_NONCLAIM_KEYS
    assert all(value is False for value in doc["nonclaims"].values())
    return doc


def parse_route_carrier(text: str) -> dict:
    tokens = list(yaml.scan(text))
    assert not any(isinstance(token, (AnchorToken, AliasToken)) for token in tokens)
    return validate_route_carrier(yaml.load(text, Loader=UniqueSafeLoader))


def route_carrier_hostile_controls(text: str) -> int:
    attacks = [
        text + "\nroute_b_invocation_allowed: true\n",
        text.replace(
            "  cutoff: complete all-N analytic theorem;",
            "  cutoff: duplicate\n  cutoff: complete all-N analytic theorem;",
            1,
        ),
        text.replace(
            "  verdict: A0_FAIL",
            "  verdict: A0_FAIL\n  verdict: A0_WEAK_ARITHMETIC_RELATION",
            1,
        ),
        text.replace(
            "tuple: [A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]",
            "tuple: [A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL]",
            1,
        ),
        text.replace("source_lock:\n", "source_lock:\n  <<: {object: injected}\n", 1),
        "probe: &probe value\nalias_probe: *probe\n" + text,
        text + "\nunexpected_top: true\n",
        text.replace(
            "overall_verdict: ROUTE_A_REJECTED",
            "overall_verdict: ROUTE_A_ACCEPTED",
            1,
        ),
        text.replace(
            "  nonlinear_heptagon_stability: false",
            "  nonlinear_heptagon_stability: true",
            1,
        ),
        text.replace(
            "    independent_checker_assertions: 65655",
            "    independent_checker_assertions: true",
            1,
        ),
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
    return (
        path.suffix
        in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
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
    return int(
        next(
            line.split(":", 1)[1]
            for line in info.splitlines()
            if line.startswith("Pages:")
        )
    )


def font_rows(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [
        line
        for line in output.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c284-r{round_number}-") as temp:
        work = Path(temp)
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
    data = load_json_strict(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c284-thomson-polygon-point-vortex-stability-v1"
    assert data["candidate_id"] == "HCS-C284"
    assert data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-02"
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVAL}
    assert data["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert data["proof_contract"]["heptagon_boundary"] == (
        "N=7 is asserted only to be linearly degenerate in m=3,4; "
        "nonlinear stability is not claimed"
    )
    assert data["proof_contract"]["novelty_boundary"] == (
        "classical owner results are reconstructed and executable; "
        "no literature-priority claim is made"
    )
    assert data["model_contract"]["angular_velocity"] == (
        "Omega=Gamma*(N-1)/(4*pi*R^2)"
    )
    assert data["block_contract"]["hessian_block"] == (
        "Gamma^(-1)*D^2G_hat_m=c*diag(2*(N-1)-q_m,q_m), q_m=m*(N-m)"
    )
    assert data["block_contract"]["square"] == (
        "L_m^2=-c^2*q_m*(2*(N-1)-q_m)*I"
    )
    assert data["reduction_contract"]["rotation_scale"].startswith(
        "fix angular impulse and quotient rotations"
    )
    assert data["route_a"] == {
        "tuple": TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    assert all(value is False for value in data["scope_flags"].values())
    assert data["source_owner_contract"] == {
        "classical_owner": (
            "J. J. Thomson, A Treatise on the Motion of Vortex Rings (1883)"
        ),
        "linear_stability_owner_doi": "10.1080/14786443109461714",
        "later_stability_context_doi": "10.1137/S0036141098302124",
        "polygonal_relative_equilibrium_doi": "10.1063/1.3646115",
        "use_boundary": (
            "sources establish lineage and classical ownership; every displayed "
            "proof and executable count is reconstructed in-package"
        ),
    }
    counts = data["regression"]["counts"]
    assert counts == {
        "block_rows": 2077,
        "polygon_rows": 62,
        "scale_rows": 64,
        "slice_rows": 7,
        "boundary_rows": 8,
    }

    assert digest(YAML) == YAML_SHA
    yaml_text = YAML.read_text()
    route_doc = parse_route_carrier(yaml_text)
    assert semantic_hash(route_doc) == YAML_SEMANTIC_SHA
    route_carrier_rejections = route_carrier_hostile_controls(yaml_text)

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}",
        "byte-identical",
        "warning-free",
        "embedded and subset",
        "visually inspected",
        "All twelve rendered pages",
    ):
        assert token in compile_report, token

    tex_text = " ".join(TEX.read_text().split())
    for token in (
        r"\cite{Thomson1883}",
        r"\cite{Havelock1931}",
        r"\cite{CabralSchmidt2000}",
        r"\cite{Celli2011}",
        "classical owners of the polygon",
        "No calculation or proof below is outsourced",
        "no literature-priority claim is made",
        "algebraic multiplicity four and geometric multiplicity two",
        "does not assert nonlinear",
    ):
        assert token in tex_text, token

    source_text = " ".join(SOURCE_AUDIT.read_text().split())
    for token in (
        "direct linear ring-stability owner",
        "no literature priority claim",
        "10.1080/14786443109461714",
        "10.1137/S0036141098302124",
        "10.1063/1.3646115",
        "frozen read-only collision snapshot",
        REGISTRY_SNAPSHOT_SHA,
        OBSTRUCTION_SNAPSHOT_SHA,
        "not live file dependencies",
        SCOPE,
    ):
        assert token in source_text, token

    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    assert not [name for name, path in physical.items() if is_sidecar(path)]
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
    assert len(set(ROUND_HASHES)) == 3
    assert digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [3, 4, 5]
    assert pdf_pages(PDF) == 5
    font_counts = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows
        assert all(
            len(row.split()) >= 7
            and row.split()[-5] == "yes"
            and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
    assert font_counts == [18, 19, 20]

    final_text = " ".join(
        subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
        .lower()
        .split()
    )
    for token in (
        "complete dft block",
        "algebraic multiplicity four",
        "geometric multiplicity two",
        "65,655",
        "4,585",
        "76/76",
        "duplicate keys",
        "seven symmetry",
        "a0_fail",
        "a1_weak",
        "route_a_rejected",
        SCOPE.lower(),
        "10.1080/14786443109461714",
        "10.1137/s0036141098302124",
        "10.1063/1.3646115",
    ):
        assert token in final_text, token

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(
        zip(ROUND_PATHS, ROUND_HASHES)
    ):
        one, _ = fresh_build(round_number)
        two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    producer = run_python("c284_point_vortex_producer.py")
    checker = run_python("c284_point_vortex_checker.py")
    sympy = run_python("c284_point_vortex_sympy_crosscheck.py")
    replay = run_python("c284_point_vortex_replay.py")
    mutation = run_python("c284_point_vortex_mutation.py")
    assert "C284_PRODUCER_PASS" in producer
    assert "C284 independent raw-Hessian checker: PASS" in checker
    assert "C284_SYMPY_PASS" in sympy
    assert "C284 double fresh-path byte replay: PASS" in replay
    assert "repaired-hash schema/semantic attacks plus stale-hash" in mutation
    checker_match = re.search(r"PASS \((\d+) assertions", checker)
    sympy_match = re.search(r"PASS \((\d+) exact identities", sympy)
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert checker_match and int(checker_match.group(1)) == 65655
    assert sympy_match and int(sympy_match.group(1)) == 4585
    assert mutation_match
    assert mutation_match.group(1) == mutation_match.group(2) == "76"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c284-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C284",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "theorem_status": data["proof_contract"]["status"],
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES,
            "fresh_build_sha256": fresh_hashes,
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_relative_equilibrium_and_clock": "PASS",
            "G2_raw_cartesian_hessian": "PASS",
            "G3_complete_dft_blocks": "PASS",
            "G4_symmetry_reduction": "PASS",
            "G5_sharp_6_7_8_threshold": "PASS",
            "G6_heptagon_linear_only_boundary": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_deterministic_pdf_fonts_log_visual": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_claim_source_traceability": "PASS",
            "G12_target_operator_route_b": "NOT_CLAIMED",
            "G13_exact_json_schema_and_duplicate_policy": "PASS",
            "G14_unique_route_carrier_schema": "PASS",
        },
        "results": {
            **counts,
            "checker_assertions": int(checker_match.group(1)),
            "sympy_checks": int(sympy_match.group(1)),
            "hostile_rejections": int(mutation_match.group(1)),
            "route_carrier_hostile_rejections": route_carrier_rejections,
            "pdf_pages": 5,
            "round_pdf_pages": page_counts,
            "embedded_subset_font_rows": font_counts,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA,
            "pdf_sha256": digest(PDF),
        },
        "route_a_verdict": data["route_a"],
        "route_a_carrier": {
            "yaml_sha256": YAML_SHA,
            "semantic_sha256": YAML_SEMANTIC_SHA,
            "tuple": route_doc["tuple"],
            "overall": route_doc["overall_verdict"],
            "duplicate_merge_alias_policy": "REJECT",
        },
        "source_owner_contract": data["source_owner_contract"],
        "collision_snapshot": {
            "candidate_registry_sha256": REGISTRY_SNAPSHOT_SHA,
            "obstruction_registry_sha256": OBSTRUCTION_SNAPSHOT_SHA,
            "range": "HCS-C1 through HCS-C283",
            "policy": (
                "frozen read-only audit snapshot; no live external-registry "
                "dependency"
            ),
        },
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C284_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
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
                "status": "C284_MANIFEST_PASS",
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
