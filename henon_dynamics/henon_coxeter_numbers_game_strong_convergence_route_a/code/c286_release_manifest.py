#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C286 release."""
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
from yaml.constructor import ConstructorError
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C286_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c286_numbers_game_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C286/2026-09-02.yaml"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "e770246fe3d448e684b2adc50465dc715ff0e4008db3c9616a28719a84588081"
YAML_SHA = "05e2a09af46bec75f723b1c697b1f90b89f18e480e6792f602deb99a5ec58e54"
YAML_SEMANTIC_SHA = "80801ba80891956653d9cbf6dd4becd3a9d3692a5e23c2dfe69ab2823f8a280b"
REGISTRY_SHA = "c8fb9282ba71c6ec4d4cf596a571bcd98ee73488d1e21acb63eb6793e29fff32"
OBSTRUCTION_SHA = "bc790201679af48bdda3e924f3f1bd66b3cc1ffd5302868f5836d9ae96cbf9c6"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
EXPECTED_MODEL = {
    "root_system": "finite reduced crystallographic root system Phi with chosen simple roots and coroots",
    "position": "dominant weight lambda with coordinates x_i=<lambda,alpha_i^vee> >= 0",
    "legal_move": "fire i only when x_i>0 and replace lambda by s_i lambda",
    "coordinate_update": "x'_j=x_j-A_{j i}x_i for A_{i j}=<alpha_j,alpha_i^vee>",
    "word_convention": "sequence i_1,...,i_m accumulates as s_{i_m}...s_{i_1}",
    "scope": "finite crystallographic systems only; affine and indefinite systems are stopping boundaries",
}
EXPECTED_THEOREM = {
    "zero_set": "J={i:<lambda,alpha_i^vee>=0}; W_J fixes lambda",
    "terminal": "every legal play ends at w_0 lambda in the closed anti-dominant chamber",
    "length": "every play has |Phi+|-|Phi_J+| moves",
    "cumulative_element": "every complete play multiplies to the unique longest/minimal right-coset representative w_0 w_J in W^J",
    "strict_face": "J empty gives w_0 and |Phi+| moves",
    "zero_face": "lambda=0 gives w_0w_J=e and zero moves",
    "product_face": "disconnected components contribute additively and their legal plays interleave",
}
EXPECTED_PROOF = {
    "finite_evidence_role": "complete small-type branch enumeration is regression evidence, not the all-system proof",
    "mechanism": "legal firing is a left weak-order ascent inside W^J; the finite quotient has unique maximum w_0w_J",
    "scope": "all dominant positions in all finite reduced crystallographic root systems, including reducible systems",
    "status": "PROVABLE AS STATED",
}
EXPECTED_ANALYTIC_OBLIGATIONS = [
    "derive the coordinate reflection rule from the weight-coroot pairing",
    "identify the wall stabilizer W_J and minimal right-coset representatives W^J",
    "prove every legal firing is a strict left weak-order ascent remaining in W^J",
    "prove a play stops only at the unique anti-dominant orbit representative",
    "derive l(w_0w_J)=|Phi+|-|Phi_J+|",
    "close strict, wall, zero, disconnected, and rank-one faces",
    "stop explicitly at the finite crystallographic boundary",
]
EXPECTED_COLLISION = {
    "registry_range": "HCS-C1 through HCS-C283 plus current frozen assignments",
    "closest_distinctions": [
        "C192 is a stochastic face-semigroup chamber walk, not legal Coxeter reflection reduction",
        "C185 is a continuous isospectral matrix-sorting flow, not a finite firing game",
        "C187 and C209 are finite cyclic-sieving permutations, not weak-order confluence",
        "C204 classifies finite-field linear endomorphisms, not real root-system chamber dynamics",
    ],
}
EXPECTED_NONCLAIMS = [
    "The theorem and its strong-convergence mechanism are classical; no literature-priority claim is made.",
    "No affine, indefinite, Kac--Moody, noncrystallographic, or arbitrary generalized-Cartan extension is claimed.",
    "Reduced firing words are not relabelled as rational primes, periodic orbits, Euler factors, or target zeros.",
    "The natural reflection representation is not promoted to a same-clock Hilbert--Polya operator.",
    "Finite branch enumeration tests conventions but does not prove the all-system theorem.",
]
EXPECTED_SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_authorization": False,
}
ROUND_PATHS = [
    PAPER / "main_round0_original.pdf",
    PAPER / "main_round1.pdf",
    PAPER / "main_round2.pdf",
]
ROUND_HASHES = [
    "baa01816e5a604b684a9ae067ff2c1fbf4b3a8bbac2b18c736ab5f1b7d479300",
    "5a248cb37dfb8eb26b3b698fd9ae0d2f23375dd0018c93bec9cf4d90ba4b7bab",
    "3a3684fe15c61d0e6fa76b46a0719a80e3e63d1a6a2a6091028f11d95a92e518",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c286_numbers_game_checker.py",
    "code/c286_numbers_game_mutation.py", "code/c286_numbers_game_producer.py",
    "code/c286_numbers_game_replay.py", "code/c286_numbers_game_sympy_crosscheck.py",
    "code/c286_release_manifest.py",
    "evaluations/route_a/HCS-C286/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c286_numbers_game_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|undefined citations|Rerun to get|Missing character",
    re.IGNORECASE,
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


def construct_unique_mapping(
    loader: UniqueSafeLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict:
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


def reject_duplicate_json_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    """Reject duplicate JSON keys at every object nesting level."""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_unique_json(path: Path) -> dict:
    data = json.loads(
        path.read_text(), object_pairs_hook=reject_duplicate_json_object
    )
    assert type(data) is dict
    return data


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(data: dict) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def validate_route_carrier(doc: object) -> dict:
    assert isinstance(doc, dict) and set(doc) == ROUTE_TOP_KEYS
    assert doc["schema"] == "route-a-evaluation-v0.2.0"
    assert doc["skill"] == "route-a-evaluator" and doc["skill_version"] == "0.2.0"
    assert doc["candidate_id"] == "HCS-C286" and doc["source_commit"] == SOURCE
    assert doc["evaluation_date"] == "2026-09-02" and doc["fixed_epoch"] == EPOCH
    assert doc["scope_literal"] == SCOPE and doc["evaluator_authority_sha256"] == EVAL
    assert isinstance(doc["source_lock"], dict) and set(doc["source_lock"]) == SOURCE_LOCK_KEYS
    lock = doc["source_lock"]
    assert lock["arithmetic_origin"].startswith("none;")
    assert lock["determinant_convention"] == "none"
    assert "complete all-rank finite-type theorem" in lock["cutoff"]
    assert "exact integer" in lock["precision"]
    forbidden = lock["forbidden_data"]
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

    assert doc["a1"]["metrics"] == {
        "nonconstant_periodic_orbits": 0,
        "primitive_orbit_owner": "absent_reduced_words_are_terminating_paths_not_periodic_orbits",
        "analytic_and_boundary_rows": 3506,
        "independent_checker_assertions": 19056,
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
        text.replace(
            "  cutoff: complete all-rank finite-type theorem;",
            "  cutoff: duplicate\n  cutoff: complete all-rank finite-type theorem;",
            1,
        ),
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
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def pdf_text(path: Path) -> str:
    return " ".join(
        subprocess.check_output(["pdftotext", str(path), "-"], text=True)
        .lower()
        .split()
    )


def font_rows(path: Path) -> list[str]:
    out = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c286-numbers-r{round_number}-") as temp:
        work = Path(temp)
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
        assert not WARNING_RE.search(log)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    data = load_unique_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert set(data) == {
        "analytic_proof_obligations", "candidate_id", "collision_contract",
        "evaluation_date", "evaluator", "fixed_epoch", "headline",
        "model_contract", "nonclaims", "payload_sha256", "proof_contract",
        "regression", "route_a", "schema", "scope_flags", "scope_literal",
        "source_commit", "theorem_contract",
    }
    assert data["schema"] == "hcs-c286-coxeter-numbers-game-v1"
    assert data["candidate_id"] == "HCS-C286" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-02"
    assert type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE and data["evaluator"] == {"version": "0.2.0", "sha256": EVAL}
    assert type(data["evaluator"]) is dict and set(data["evaluator"]) == {"version", "sha256"}
    assert data["model_contract"] == EXPECTED_MODEL
    assert data["theorem_contract"] == EXPECTED_THEOREM
    assert data["proof_contract"] == EXPECTED_PROOF
    assert data["analytic_proof_obligations"] == EXPECTED_ANALYTIC_OBLIGATIONS
    assert data["collision_contract"] == EXPECTED_COLLISION
    assert data["nonclaims"] == EXPECTED_NONCLAIMS
    assert data["scope_flags"] == EXPECTED_SCOPE_FLAGS
    assert all(type(value) is bool for value in data["scope_flags"].values())
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert type(data["route_a"]["route_b_invocation_allowed"]) is bool
    counts = data["regression"]["counts"]
    assert counts == {"case_rows": 23, "branch_rows": 3332, "level_rows": 143, "boundary_rows": 8}
    assert all(type(value) is int for value in counts.values())
    assert set(data["regression"]) == {"case_rows", "branch_rows", "level_rows", "boundary_rows", "counts"}

    authority = ROOT.parents[1] / "flow_systems/skills/route-a-evaluator.md"
    assert digest(authority) == EVAL
    assert digest(YAML) == YAML_SHA
    yaml_text = YAML.read_text()
    route_doc = parse_route_carrier(yaml_text)
    assert semantic_hash(route_doc) == YAML_SEMANTIC_SHA
    route_carrier_rejections = route_carrier_hostile_controls(yaml_text)

    compile_report = " ".join((PAPER / "COMPILE_REPORT.md").read_text().split())
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free",
        "embedded and subset", "visually inspected", "All nine pages",
        "final-pass log", "644/1404/1881",
    ):
        assert token in compile_report, token
    tex_text = " ".join(TEX.read_text().split())
    for token in (
        r"\cite{Mozes1990}", r"\cite{Eriksson1995,Eriksson1996}",
        "We claim no priority", "finite reduced crystallographic root system",
        r"\ellW(w_0w_J)=|\Phi^+|-|\Phi_J^+|",
        "rejects duplicate JSON keys at every depth", "19,056", "84/84",
        r"\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)}",
    ):
        assert token in tex_text, token
    audit_text = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "Mozes", "Eriksson", "Humphreys", "Bourbaki", "no literature priority",
        "C185", "C192", "C176", "C181", "C187", "C204", "C209", "C279--C283",
        "10.1016/0097-3165(90)90024-Q", "10.1006/eujc.1996.0031",
        "10.1017/CBO9780511623646", REGISTRY_SHA, OBSTRUCTION_SHA,
    ):
        assert token in audit_text, token

    checker_tree = ast.parse((ROOT / "code/c286_numbers_game_checker.py").read_text())
    checker_imports: list[str] = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            checker_imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            checker_imports.append(node.module or "")
    assert not [name for name in checker_imports if "producer" in name]

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [2, 3, 4] and pdf_pages(PDF) == 4
    font_counts: list[int] = []
    round_texts: list[str] = []
    word_counts: list[int] = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(
            len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes"
            for row in rows
        )
        font_counts.append(len(rows))
        text = pdf_text(path)
        round_texts.append(text)
        word_counts.append(len(text.split()))
    assert font_counts == [20, 23, 24]
    assert word_counts == [644, 1404, 1881]
    for token in (
        "strong convergence in the finite coxeter numbers game",
        "theorem 1 (strict chamber)",
        "10.1006/eujc.1996.0031",
    ):
        assert token in round_texts[0], token
    for token in (
        "walls as a parabolic quotient",
        "every degenerate face",
        "arbitrary wall",
    ):
        assert token in round_texts[1], token
    final_text = round_texts[2]
    for token in (
        "strong convergence in the finite coxeter numbers game", "walls as a parabolic quotient",
        "every degenerate face", "zero vector", "disconnected", "rank-one",
        "producer-independent executable reconstruction", "19,056", "84/84",
        "rejects duplicate json keys at every depth", "complete unique grid",
        "a0_fail", "a1_fail", "a2_fail", "a3_fail", "a4_fail",
        "route_a_rejected", "route b is false", SCOPE.lower(),
        "10.1016/0097-3165(90)90024-q", "10.1006/eujc.1996.0031",
        "10.1017/cbo9780511623646",
    ):
        assert token in final_text, token

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        one, _ = fresh_build(round_number)
        two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    producer = run_python("c286_numbers_game_producer.py")
    checker = run_python("c286_numbers_game_checker.py")
    sympy = run_python("c286_numbers_game_sympy_crosscheck.py")
    replay = run_python("c286_numbers_game_replay.py")
    mutation = run_python("c286_numbers_game_mutation.py")
    assert "C286_PRODUCER_PASS" in producer and "C286 independent checker: PASS" in checker
    assert "C286_SYMPY_PASS" in sympy and "C286 byte replay: PASS" in replay
    cm = re.search(r"PASS \((\d+) assertions", checker)
    sm = re.search(r"PASS \((\d+) symbolic", sympy)
    mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and int(cm.group(1)) == 19056
    assert sm and int(sm.group(1)) == 577
    assert mm and mm.group(1) == mm.group(2) == "84"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c286-coxeter-numbers-game-release-v2",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C286",
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
            "G1_coordinate_reflection_and_word_convention": "PASS",
            "G2_positive_roots_and_weak_order": "PASS",
            "G3_parabolic_coset_terminal_and_length": "PASS",
            "G4_strict_wall_zero_disconnected_rank_one": "PASS",
            "G5_finite_only_scope_stop": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS",
            "G8_deterministic_pdf_fonts_log_visual": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_claim_source_collision_traceability": "PASS",
            "G11_target_operator_route_b": "NOT_CLAIMED",
            "G12_unique_route_carrier_schema": "PASS",
            "G13_unique_json_contract_schema_type_grids": "PASS",
        },
        "results": {
            **counts, "total_regression_rows": sum(counts.values()),
            "checker_assertions": int(cm.group(1)), "sympy_checks": int(sm.group(1)),
            "hostile_rejections": int(mm.group(1)), "route_carrier_hostile_rejections": route_carrier_rejections,
            "pdf_pages": 4, "round_pdf_pages": page_counts,
            "embedded_subset_font_rows": font_counts,
            "round_word_counts": word_counts,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF),
        },
        "route_a_verdict": data["route_a"],
        "route_a_carrier": {
            "yaml_sha256": YAML_SHA, "semantic_sha256": YAML_SEMANTIC_SHA,
            "tuple": route_doc["tuple"], "overall": route_doc["overall_verdict"],
            "duplicate_merge_alias_policy": "REJECT",
        },
        "collision_snapshot": {
            "candidate_registry_sha256": REGISTRY_SHA,
            "obstruction_registry_sha256": OBSTRUCTION_SHA,
            "policy": "frozen read-only audit snapshot; no live external-registry dependency",
        },
        "evidence_json_policy": {
            "duplicate_keys_at_any_depth": "REJECT",
            "unknown_or_missing_contract_fields": "REJECT",
            "strict_scalar_types": "ENFORCED",
            "complete_unique_row_grids": "ENFORCED",
        },
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C286_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C286_MANIFEST_PASS", "payload_file_count": 27,
        "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
