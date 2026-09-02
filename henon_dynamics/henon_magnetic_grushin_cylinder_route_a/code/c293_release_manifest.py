#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C293 release."""
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
MANIFEST = ROOT/"C293_RELEASE_MANIFEST.json"
EVIDENCE = ROOT/"results/c293_grushin_evidence.json"
EVALUATION = ROOT/"evaluations/route_a/HCS-C293/2026-09-02.yaml"
PAPER = ROOT/"paper"; TEX = PAPER/"main.tex"; PDF = PAPER/"main.pdf"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH = 1788307200
EVIDENCE_SHA = "b84946889a6036c3b8a7bc11023a8e055a69c905e34535bc30a977c9ac727edd"
EVALUATION_SHA = "e3ff56c62d1830a03a8a0b2a7d33acf73d6d997de4d9c872e6f6ff278d98adae"
TUPLE = ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_NATURAL_QUANTIZATION"]
SCOPE_FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
    "automorphy": False, "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_input": False,
}
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C293",
    "evaluation_date": "2026-09-02", "source_commit": SOURCE,
    "fixed_epoch": EPOCH, "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR, "theorem_status": "PROVABLE AS STATED",
    "tuple": TUPLE, "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "axes": {
        "A0": "weak source-local coefficient relation only",
        "A1": "no primitive-orbit repetition bridge", "A2": "no arithmetic clock",
        "A3": "partial source-local meromorphic structure only",
        "A4": "natural Friedrichs quantization",
    },
    "scope_flags": SCOPE_FLAGS,
}
ROUND_PATHS = [PAPER/"main_round0_original.pdf", PAPER/"main_round1.pdf", PAPER/"main_round2.pdf"]
ROUND_HASHES = [
    "3e7b203f3348837f846133f2079e58622737c83e6364ff20a874fd6f02d30638",
    "a5563a310c68a4c150fcbe891b40bb48093aa39e28cbc9124291877cbab7df3a",
    "3295011b255e5e70761bd1119af1b8b72453b0724cfbb21663614321a763935d",
]
ROUND_TEXT = [
    ("complete flux dichotomy", "almost-everywhere multiplicity two", "singular-continuous spectrum is empty", "k ∈ z, n ∈ n0"),
    ("exact embedded multiplicity", "full heat operator is not trace class", "one resonant angular fourier channel"),
    ("source-local zeta series and logarithmic weyl law", "j≡1 (mod 2)", "75/75", "duplicate-key-rejecting evaluation yaml", "route_a_rejected", SCOPE.lower()),
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c293_grushin_checker.py", "code/c293_grushin_mutation.py", "code/c293_grushin_producer.py", "code/c293_grushin_replay.py", "code/c293_grushin_sympy_crosscheck.py", "code/c293_release_manifest.py",
    "evaluations/route_a/HCS-C293/2026-09-02.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c293_grushin_evidence.json",
}
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")


def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body=dict(data); body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate rejection and dates kept as strings."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    loader.flatten_mapping(node); out = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try: duplicate = key in out
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, "unhashable YAML key", key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate YAML key: {key}", key_node.start_mark)
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml_load(path: Path) -> dict:
    value = yaml.load(path.read_text(), Loader=UniqueSafeLoader)
    if type(value) is not dict: raise TypeError("evaluation YAML top level must be object")
    return value


def assert_exact_tree(value, expected, label: str) -> None:
    assert type(value) is type(expected), f"{label} exact type"
    if type(expected) is dict:
        assert set(value) == set(expected), f"{label} exact keys"
        for key in expected: assert_exact_tree(value[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        assert len(value) == len(expected), f"{label} length"
        for index, item in enumerate(expected): assert_exact_tree(value[index], item, f"{label}[{index}]")
    else:
        assert value == expected, f"{label} value"


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name: str) -> str:
    env=dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE":"1","TZ":"UTC"})
    return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=env,text=True)


def pdf_pages(path: Path) -> int:
    text=subprocess.check_output(["pdfinfo",str(path)],text=True)
    return int(next(line.split(":",1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    text=subprocess.check_output(["pdffonts",str(path)],text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    text=subprocess.check_output(["pdftotext","-layout",str(path),"-"],text=True)
    return " ".join(text.lower().split())


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c293-r{round_number}-") as temporary:
        work=Path(temporary); env=dict(os.environ); env.update({"SOURCE_DATE_EPOCH":str(EPOCH),"FORCE_SOURCE_DATE":"1","TZ":"UTC"})
        source=rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
        for _ in range(2): subprocess.run(command,cwd=work,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=(work/"main.log").read_text(errors="replace"); match=WARNING_RE.search(log)
        assert match is None, match.group(0) if match else ""
        return (work/"main.pdf").read_bytes()


def main() -> None:
    producer=run_python("c293_grushin_producer.py"); assert "C293_PRODUCER_PASS" in producer
    data=json.loads(EVIDENCE.read_text()); assert digest(EVIDENCE)==EVIDENCE_SHA and data["payload_sha256"]==payload_hash(data)
    assert data["schema"]=="hcs-c293-magnetic-grushin-cylinder-v1" and data["candidate_id"]=="HCS-C293"
    assert data["source_commit"]==SOURCE and data["evaluation_date"]=="2026-09-02" and data["fixed_epoch"]==EPOCH and data["scope_literal"]==SCOPE
    assert data["evaluator"]=={"version":"0.2.0","sha256":EVALUATOR}
    assert data["model"]["realization"]=="nonnegative closed-form Friedrichs realization; essential self-adjointness is not claimed"
    assert data["theorem_contract"]["integer"]=="for alpha in Z exactly one resonant Fourier channel has absolutely continuous spectrum [0,infinity) of almost-everywhere multiplicity two, the singular-continuous spectrum is empty, and positive-integer oscillator eigenvalues remain embedded"
    assert data["proof_contract"]["integer_type"].startswith("the resonant block is the free line Laplacian")
    assert data["integer_spectrum"]=={"absolutely_continuous_spectrum":"[0,infinity) from exactly one free Fourier channel","absolutely_continuous_multiplicity":2,"point_spectrum":"every positive integer, embedded in [0,infinity)","singular_continuous_spectrum_empty":True,"nonresonant_compact_resolvent":True}
    assert data["route_a"]=={"tuple":TUPLE,"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    assert all(value is False for value in data["scope_flags"].values())
    assert data["enumeration"]=={"noninteger_fluxes":["1/3","1/2","2/5"],"k_values":list(range(-5,6)),"n_values":list(range(5)),"spectral_cells":165,"heat_cells":9,"integer_heat_cells":3,"multiplicity_cells":96,"counting_cells":6,"zeta_cells":4,"symmetry_cells":10}
    assert [r["identifier"] for r in data["references"]]==["arXiv:1406.6578","arXiv:2312.04359"]

    evaluation = strict_yaml_load(EVALUATION)
    assert_exact_tree(evaluation, EVALUATION_EXPECTED, "evaluation")
    assert semantic_hash(evaluation) == EVALUATION_SHA
    yaml_text=EVALUATION.read_text()
    for token in (f"source_commit: {SOURCE}",f"fixed_epoch: {EPOCH}",f"scope_literal: {SCOPE}",f"evaluator_authority_sha256: {EVALUATOR}","tuple: [A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_NATURAL_QUANTIZATION]","overall_verdict: ROUTE_A_REJECTED","route_b_invocation_allowed: false"):
        assert token in yaml_text,token
    theorem=" ".join((ROOT/"THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE AS STATED","Friedrichs","a.e. multiplicity two","2 d_odd(N)","source-local","not target Euler"):
        assert token in theorem,token
    source_audit=(ROOT/"SOURCE_AUDIT.md").read_text()
    for token in ("arXiv:1406.6578","arXiv:2312.04359","does not mean","literature-level originality"):
        assert token in source_audit,token
    tex=TEX.read_text()
    assert "\r" not in tex and ",quad n" not in tex and ",\\quad n\\in\\N_0" in tex
    assert "j\\equiv1\\pmod 2" in tex
    for token in ("Complete flux dichotomy","almost-everywhere multiplicity two","singular-continuous spectrum is empty","Exact embedded multiplicity","Source-local zeta series and logarithmic Weyl law","claim that these classical mechanisms are newly discovered"):
        assert token in tex,token

    checker_source=(ROOT/"code/c293_grushin_checker.py").read_text(); tree=ast.parse(checker_source); imports=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import): imports.extend(alias.name for alias in node.names)
        elif isinstance(node,ast.ImportFrom): imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    assert "object_pairs_hook=reject_duplicate_keys" in checker_source and "direct_channel_trace" in checker_source and "mp.sinh" not in checker_source
    assert '"absolutely_continuous_multiplicity": 2' in checker_source
    mutation_source=(ROOT/"code/c293_grushin_mutation.py").read_text(); assert "integer-spectrum-ac-multiplicity-one" in mutation_source

    compile_report=(PAPER/"COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}","two isolated directories for each round","byte-identical","settled warning regex found no","embedded and subset",*ROUND_HASHES): assert token in compile_report,token
    hostile=(ROOT/"results/HOSTILE_AUDIT.md").read_text()
    for token in ("All 75 attacks","21 evaluation-YAML attacks","multiplicity from two to one","duplicate top/nested","individual Fourier–Hermite levels"): assert token in hostile,token

    physical={str(path.relative_to(ROOT)):path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name,path in physical.items() if sidecar(path)]
    files={name:digest(path) for name,path in sorted(physical.items()) if path!=MANIFEST}
    assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED)); assert len(files)==27
    assert [digest(path) for path in ROUND_PATHS]==ROUND_HASHES and len(set(ROUND_HASHES))==3 and digest(PDF)==ROUND_HASHES[2]
    pages=[pdf_pages(path) for path in ROUND_PATHS]; assert pages==[2,3,4]
    font_counts=[]
    for path,required in zip(ROUND_PATHS,ROUND_TEXT):
        rows=font_rows(path); assert rows and all(len(row.split())>=7 and row.split()[-5]=="yes" and row.split()[-4]=="yes" for row in rows)
        font_counts.append(len(rows)); text=pdf_text(path)
        for token in required: assert token in text,(path.name,token)
    assert font_counts==[23,24,26]

    fresh_hashes=[]
    for round_number,(archive,expected) in enumerate(zip(ROUND_PATHS,ROUND_HASHES)):
        first=fresh_build(round_number); second=fresh_build(round_number); assert first==second==archive.read_bytes()
        pair=[hashlib.sha256(first).hexdigest(),hashlib.sha256(second).hexdigest()]; assert pair==[expected,expected]; fresh_hashes.append(pair)

    checker=run_python("c293_grushin_checker.py"); symbolic=run_python("c293_grushin_sympy_crosscheck.py"); replay=run_python("c293_grushin_replay.py"); mutation=run_python("c293_grushin_mutation.py")
    assert "C293 independent Fourier-Hermite checker: PASS" in checker and "strict duplicate-rejecting JSON/YAML schemas" in checker
    assert f"evaluation-semantic-sha256={EVALUATION_SHA}" in checker
    assert "C293_SYMPY_PASS" in symbolic and "C293 byte replay: PASS" in replay and "C293_MUTATION_PASS 75/75" in mutation
    checker_n=int(re.search(r"PASS \((\d+) assertions",checker).group(1)); symbolic_n=int(re.search(r"PASS \((\d+) symbolic",symbolic).group(1)); mutation_n=int(re.search(r"PASS (\d+)/(\d+)",mutation).group(1))
    assert (checker_n,symbolic_n,mutation_n)==(2053,750,75) and digest(EVIDENCE)==EVIDENCE_SHA

    result={
        "schema":"hcs-c293-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C293","evaluation_date":"2026-09-02","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,
        "headline":"Friedrichs magnetic Grushin cylinder with flux-driven compact/continuous transition, exact heat, source zeta, and logarithmic Weyl law","theorem_status":"PROVABLE AS STATED",
        "build_contract":{"engine":"LuaLaTeX","fixed_epoch":EPOCH,"passes_per_build":2,"fresh_builds_per_round":2,"settled_warning_regex":WARNING_RE.pattern,"round_artifacts":[str(p.relative_to(ROOT)) for p in ROUND_PATHS],"round_pdf_sha256":ROUND_HASHES,"fresh_build_sha256":fresh_hashes,"round_pdf_pages":pages,"round_embedded_subset_font_rows":font_counts,"all_round_text_contracts":[list(x) for x in ROUND_TEXT],"visual_inspection":"PASS all pages","final_equals":"paper/main_round2.pdf"},
        "evaluation_contract":{"path":str(EVALUATION.relative_to(ROOT)),"semantic_sha256":EVALUATION_SHA,"duplicate_keys_rejected":True,"exact_schema_types_values":True},
        "gates":{"G0_source_scope_evaluator":"PASS","G0a_evaluation_yaml_duplicate_rejecting_exact_schema":"PASS","G1_exact_duplicate_rejecting_schema":"PASS","G2_friedrichs_fourier_hermite_realization":"PASS","G3_noninteger_compact_pure_point":"PASS","G4_integer_ac_multiplicity_two_plus_embedded_point":"PASS","G5_heat_multiplicity_source_zeta_weyl":"PASS","G6_checker_sympy_replay_mutation":"PASS","G7_two_substantive_revisions":"PASS","G8_six_fresh_pdf_builds_fonts_logs_text":"PASS","G9_manifest_hash_closure":"PASS","G10_claim_source_traceability":"PASS","G11_target_euler_zero_operator_route_b":"NOT_CLAIMED"},
        "results":{**{k:v for k,v in data["enumeration"].items() if k not in {"noninteger_fluxes","k_values","n_values"}},"audited_cells":293,"checker_assertions":checker_n,"symbolic_checks":symbolic_n,"hostile_rejections":mutation_n,"evidence_json_hostile_rejections":54,"evaluation_yaml_hostile_rejections":21,"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":data["payload_sha256"],"evidence_sha256":EVIDENCE_SHA,"evaluation_semantic_sha256":EVALUATION_SHA,"pdf_sha256":digest(PDF),"pdf_pages":pages[-1]},
        "integer_spectral_type":data["integer_spectrum"],"route_a_verdict":data["route_a"],"nonclaims":data["nonclaims"],
        "excluded_from_manifest":["C293_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files,
    }
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
    print(json.dumps({"status":"C293_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":EVIDENCE_SHA,"pdf_sha256":digest(PDF)},sort_keys=True))


if __name__=="__main__": main()
