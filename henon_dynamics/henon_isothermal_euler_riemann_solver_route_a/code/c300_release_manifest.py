#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C300 release."""
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
MANIFEST = ROOT / "C300_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c300_euler_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C300/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "e4a054b3485659ac58021f94b6f36c11a331b92efee04dd1930f910b5a2d994e"
PAYLOAD_SHA = "6b6a3f8392e153c9e989afec5aacded80dbd434abc67133c61d73dc90406f7b0"
EVALUATION_FILE_SHA = "3e92895517cdf46946320f43a47407ffed42bd6fc4ff11422e88f404f7a3aa0f"
EVALUATION_SEMANTIC_SHA = "6941298ff0ba08c6fc29f2a3af3386e08a82913aeadf39f8d3ab53ea89d7b11e"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "d494467b8163758a36e942a588982ab358a18d263be3236eeef0aa86755a9a69",
    "32020b4388648121ae19fd60ece4ca076476c023190d8265566335017d79936a",
    "051da17fe465f1314e40a00329bf06d677b598080f8609cd05f6b9af4790e90a",
]
ROUND_PAGES = [2, 3, 3]
ROUND_FONTS = [17, 17, 18]
ROUND_TEXT = [
    ("one scalar equation for the full solver", "the four patterns in one table", "rankine"),
    ("lax ordering and mechanical entropy", "compressed-to-outer density ratio", "uniqueness of the assembled two-wave entropy solution"),
    ("boundaries, executable evidence, and route a", "pressureless-limit solution theorem", "route_a_rejected", "no_bad_euler_or_root_number"),
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
    "Densities, characteristic speeds, and wave families are source PDE data, not rational-prime labels or prime-power weights.",
    "The entropy solution semigroup is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lax Riemann construction or isothermal wave curves.",
]
COLLISION = {
    "C195": "C195 is scalar periodic viscous Burgers dynamics; C300 is a two-field inviscid Riemann solver with two genuinely nonlinear families and four wave patterns.",
    "pressureless_warning": "vacuum and delta-shock behavior at a=0 are excluded singular limits, not imported conclusions.",
}
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "code/README.md",
    "code/c300_euler_checker.py", "code/c300_euler_mutation.py", "code/c300_euler_producer.py",
    "code/c300_euler_replay.py", "code/c300_euler_sympy_crosscheck.py", "code/c300_release_manifest.py",
    "evaluations/route_a/HCS-C300/2026-09-02.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c300_euler_evidence.json",
}


def branch(verdict, status, evidence, failure, artifacts):
    return {
        "verdict": verdict, "evidence_status": status, "strongest_evidence": evidence,
        "strongest_failure": failure, "artifacts": artifacts,
    }


EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C300",
    "title": "Complete positive-density Riemann atlas for one-dimensional isothermal Euler flow",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O284",
    "candidate_definition": "The self-similar Lax entropy Riemann solver for one-dimensional isothermal Euler flow with positive left and right densities and sound speed a>0.",
    "family": "strictly hyperbolic two-field conservation law and four-pattern Riemann dynamics",
    "phase_space": "positive-density conservative states U=(rho,rho u) separated by one initial discontinuity",
    "dynamics": "rho_t+(rho u)_x=0 and (rho u)_t+(rho u^2+a^2 rho)_x=0",
    "parameters": "a>0; rho_L>0; rho_R>0; u_L,u_R finite real",
    "parameter_provenance": "the theorem covers every datum in the full positive-density finite-velocity chamber",
    "arithmetic_origin": "none; density, velocity, sound speed, shock speed, and entropy production are source PDE data",
    "clock": "physical time t and similarity coordinate xi=x/t",
    "normalization": "physical density and velocity; common positive density scaling is recorded as a symmetry",
    "determinant_convention": "not applicable; the scalar monotone root equation is not a determinant",
    "orbit_cutoff": "one global Riemann theorem; finite patterns are regression evidence only",
    "precision": "exact rational parameters plus 72-digit logarithmic, radical, residual, and entropy receipts",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c300_euler_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": branch(
        "A0_FAIL", "exact negative classification",
        "all wave curves and intermediate states are explicit source-side PDE data",
        "no rational-prime local datum or target Euler factor is constructed",
        ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    ),
    "a1": branch(
        "A1_FAIL", "exact structural mismatch",
        "the entropy solution contains two ordered elementary waves and one intermediate sector",
        "a finite self-similar fan is not a recurrent primitive-periodic-orbit system",
        ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    ),
    "a2": branch(
        "A2_FAIL", "exact negative classification",
        "wave speeds order events in the physical similarity coordinate",
        "xi=x/t is not an arithmetic clock or logarithmic rational-prime norm",
        ["THEOREM_PACKAGE.md"],
    ),
    "a3": branch(
        "A3_FAIL", "exact negative classification",
        "one monotone scalar equation determines the intermediate density",
        "the scalar root equation is not a target determinant, completed function, or functional equation",
        ["results/c300_euler_evidence.json", "paper/main.pdf"],
    ),
    "a4": branch(
        "A4_FAIL", "entropy-semigroup mismatch",
        "a strictly convex mechanical entropy selects compressive shocks",
        "the nonlinear entropy solution semigroup is not a certified self-adjoint Hilbert--Polya operator",
        ["SOURCE_AUDIT.md", "paper/main.pdf"],
    ),
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; monotonicity, wave construction, Lax ordering, entropy production, and no-vacuum are analytic",
    "source_owner_tokens": ["10.1002/cpa.3160100406", "10.1090/mmono/055", "10.1007/978-3-642-04048-1"],
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path):
    result = json.loads(Path(path).read_text(), object_pairs_hook=reject_duplicate_keys, parse_constant=reject_nonfinite)
    if type(result) is not dict:
        raise TypeError("JSON top level must be an object")
    return result


def payload_hash(data):
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


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml(path):
    raw = Path(path).read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    result = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(result) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return result


def exact_tree_equal(actual, expected):
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree_equal(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree_equal(a, e) for a, e in zip(actual, expected))
    return actual == expected


def semantic_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path):
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")
    )


def run_python(name):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path):
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path):
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path):
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def raster_audit(path, page_count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c300-raster-") as temporary:
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


def fresh_build(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c300-r{round_number}-") as temporary:
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
        return (work / "main.pdf").read_bytes()


def main() -> None:
    producer = run_python("c300_euler_producer.py")
    assert "C300_PRODUCER_PASS" in producer
    data = strict_json(EVIDENCE)
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == PAYLOAD_SHA
    assert data["schema"] == "hcs-c300-isothermal-euler-riemann-v1"
    assert data["candidate_id"] == "HCS-C300" and data["obstruction_id"] == "HEN-O284"
    assert data["evaluation_date"] == "2026-09-02"
    assert type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH
    assert data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE
    assert exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR})
    assert "strictly negative" in data["proof_contract"]["entropy_formula"]
    assert "full-data theorem is analytic" in data["proof_contract"]["finite_role"]
    assert exact_tree_equal(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    assert exact_tree_equal(data["scope_flags"], FLAGS)
    assert exact_tree_equal(data["nonclaims"], NONCLAIMS)
    assert exact_tree_equal(data["collision_boundary"], COLLISION)
    enum = data["enumeration"]
    expected_counts = {
        "case_count": 20, "wave_count": 40, "root_receipt_cells": 120,
        "wave_receipt_cells": 273, "scaling_receipt_cells": 20,
        "pressureless_receipt_cells": 16, "boundary_receipt_cells": 8,
        "audited_cell_count": 437,
    }
    for key, value in expected_counts.items():
        assert type(enum[key]) is int and enum[key] == value
    assert exact_tree_equal(enum["wave_kind_counts"], {"rarefaction": 17, "shock": 17, "zero": 6})
    assert exact_tree_equal(enum["pattern_counts"], {
        "R-R": 4, "R-S": 4, "R-Z": 1, "S-R": 3, "S-S": 4,
        "S-Z": 1, "Z-R": 1, "Z-S": 1, "Z-Z": 1,
    })
    assert [item["identifier"] for item in data["references"]] == [
        "10.1002/cpa.3160100406", "10.1090/mmono/055", "10.1007/978-3-642-04048-1",
    ]

    evaluation = strict_yaml(EVALUATION)
    assert digest(EVALUATION) == EVALUATION_FILE_SHA
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert exact_tree_equal(evaluation, EXPECTED_EVALUATION)

    checker_source = (ROOT / "code/c300_euler_checker.py").read_text()
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
    assert "noncanonical decimal receipt" in checker_source
    assert "exact YAML semantic tree and types" in checker_source
    assert "sys.flags.optimize" in checker_source
    assert not any(isinstance(node, ast.Assert) for node in ast.walk(tree))

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE AS STATED", "unique `rho_*>0`", "h'(r)=(r-1)^2/(2r^2)", "rho_*=exp[-1/(2a)]", "HEN-O284"):
        assert token in theorem, token
    source = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("10.1002/cpa.3160100406", "10.1090/mmono/055", "10.1007/978-3-642-04048-1", "C195"):
        assert token in source, token
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in ("All 110 attacks", "93 repaired-hash semantic mutations", "Wave-sign swap", "Entropy asserted from Lax by slogan", "scope escalation", "Optimized execution erases assertions"):
        assert token in hostile, token
    compile_report = " ".join((PAPER / "COMPILE_REPORT.md").read_text().split())
    for token in ("SOURCE_DATE_EPOCH=1788307200", "two fresh directories", "byte-identical", *ROUND_HASHES):
        assert token in compile_report, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    sidecars = [name for name, path in physical.items() if sidecar(path)]
    assert not sidecars, sidecars
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == ROUND_PAGES
    fonts, rasters = [], []
    for path, required, page_count in zip(ROUND_PATHS, ROUND_TEXT, ROUND_PAGES):
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        fonts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
        rasters.append(raster_audit(path, page_count))
    assert fonts == ROUND_FONTS

    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, second = fresh_build(round_number), fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c300_euler_checker.py")
    symbolic = run_python("c300_euler_sympy_crosscheck.py")
    replay = run_python("c300_euler_replay.py")
    mutation = run_python("c300_euler_mutation.py")
    assert "C300 independent isothermal-Euler checker: PASS" in checker and "producer import forbidden" in checker
    assert "C300 SymPy cross-check: PASS" in symbolic
    assert "C300 byte replay: PASS" in replay
    assert "C300 hostile mutation suite: PASS 110/110" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (1219, 30, 110)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c300-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C300", "obstruction_id": "HEN-O284",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "complete positive-density isothermal Euler Riemann solver with all wave patterns, strict entropy production, no-vacuum, and singular pressureless boundaries",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2, "fresh_build_directory_count": 6,
            "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages, "round_pdf_bytes": [path.stat().st_size for path in ROUND_PATHS],
            "round_embedded_subset_font_rows": fonts,
            "round_text_contracts": [list(items) for items in ROUND_TEXT],
            "raster_page_bytes": rasters, "visual_inspection": "PASS all 8 archived pages",
            "final_equals": "paper/main_round2.pdf",
        },
        "evaluation_contract": {
            "path": str(EVALUATION.relative_to(ROOT)), "file_sha256": EVALUATION_FILE_SHA,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "duplicate_merge_anchor_alias_rejection": True,
            "exact_recursive_semantic_tree_and_types": True,
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS", "G0a_strict_json_yaml_exact_types": "PASS",
            "G1_monotone_root_full_positive_chamber": "PASS", "G2_all_four_patterns_and_zero_faces": "PASS",
            "G3_fan_profiles_shock_speeds_and_wave_order": "PASS", "G4_lax_and_strict_entropy_production": "PASS",
            "G5_no_vacuum_scaling_and_pressureless_boundary": "PASS", "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS", "G8_six_fresh_pdf_builds_fonts_logs_text_raster": "PASS",
            "G9_manifest_hash_closure": "PASS", "G10_source_collision_and_claim_traceability": "PASS",
            "G11_target_euler_root_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "cases": 20, "waves": 40, "rarefactions": 17, "shocks": 17, "zero_waves": 6,
            "pattern_labels": 9, "scaling_pairs": 4, "pressureless_probe_pairs": 4,
            "boundary_rows": 8, "audited_cells": 437, "checker_assertions": checker_n,
            "symbolic_checks": symbolic_n, "hostile_rejections": mutation_n,
            "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": PAYLOAD_SHA,
            "evidence_sha256": EVIDENCE_SHA, "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF), "pdf_pages": pages[-1],
        },
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "boundary_risk": "No-vacuum is restricted to a>0, positive input densities, and finite velocities; vacuum inputs and the nonuniform pressureless concentration/vacuum limits are excluded.",
        "collision_boundary": data["collision_boundary"],
        "excluded_from_manifest": ["C300_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C300_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
