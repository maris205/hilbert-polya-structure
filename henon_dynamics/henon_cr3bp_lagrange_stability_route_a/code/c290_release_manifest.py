#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C290 release."""
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

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C290_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c290_cr3bp_evidence.json"
PAPER=ROOT/"paper"; TEX=PAPER/"main.tex"
YAML_PATH=ROOT/"evaluations/route_a/HCS-C290/2026-09-02.yaml"
SOURCE="7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH=1788307200; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
EVIDENCE_SHA="e282dd2df3ea8aa0cbec179dff3c9ee39f83cd181f23f026b28598cc9a4a3fe2"
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
ROUND_PATHS=[PAPER/"main_round0_original.pdf",PAPER/"main_round1.pdf",PAPER/"main_round2.pdf"]
ROUND_HASHES=["7c3d1df6a841187f8a0e65ad73f5d4d850d1d3a0b4921beb21590960ea2ba4d6","42927de3b7740dd44e340c0b43c5796bf952efc0477dc052987378b2aefeef88","88ce6ad9ad23e0cebea986cf9305bc6b258c5816170120e656c334b0b38aed9e"]
ROUND_TEXT=[
    ("equilibrium and linear-type atlas","defective with linear growth","not stable","exactly five points"),
    ("boundary ledger and interpretation","two sign checks","continuum of equilibria","nonlinear stability, control resonance bifurcations, or invoke kam"),
    ("executable evidence and adversarial closure","65/65","strict yaml","a1_fail",SCOPE.lower(),"ai-use statement"),
]
EXPECTED={
    "README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_PLAN.md","PAPER_IMPROVEMENT_LOG.md",
    "code/README.md","code/c290_cr3bp_producer.py","code/c290_cr3bp_checker.py","code/c290_cr3bp_sympy_crosscheck.py","code/c290_cr3bp_replay.py","code/c290_cr3bp_mutation.py","code/c290_release_manifest.py",
    "evaluations/route_a/HCS-C290/2026-09-02.yaml",
    "results/c290_cr3bp_evidence.json","results/RESULTS.md","results/TEST_REPORT.md","results/HOSTILE_AUDIT.md",
    "paper/README.md","paper/COMPILE_REPORT.md","paper/main.tex","paper/main.pdf","paper/main_round0_original.pdf","paper/main_round1.pdf","paper/main_round2.pdf",
}
WARNING_RE=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined references|Rerun to get|Missing character")
FLAGS={"arithmetic_local_data":False,"euler_factors":False,"root_numbers":False,"automorphy":False,"target_divisor_or_counting_law":False,"target_functional_equation":False,"target_zero_match":False,"hilbert_polya_operator":False,"route_b_input":False}
YAML_EXPECTED={
    "schema":"hcs-route-a-evaluation-v0.2.0","candidate_id":"HCS-C290","evaluation_date":"2026-09-02",
    "source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"evaluator_version":"0.2.0",
    "evaluator_authority_sha256":EVALUATOR,"title":"Lagrange equilibria and linear stability in the planar CR3BP",
    "obstruction_id":"HEN-O274","tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED",
    "route_b_invocation_allowed":False,
    "route_b_lock_reason":"No intrinsic primitive-period family, arithmetic bridge, or target spectral bridge is proved.",
    "scope_flags":FLAGS,"theorem_status":"PROVABLE_AS_STATED",
    "finite_evidence_role":"regression_only_not_all_parameter_proof",
    "source_owner_tokens":["Lagrange-1772-Oeuvres-VI-229-331","BnF-Gallica-ark-12148-bpt6k5789653w","10.1112/plms/s1-6.1.86","10.1007/978-0-387-09724-4"],
}
YAML_SEMANTIC_SHA="8bae85795b5f694a177e856d2f2f2fab85c03af5738c67d1ae2ec0a4d158a366"


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe loader that rejects duplicate, merge, and non-string mapping keys."""


def construct_unique_yaml_mapping(loader:UniqueYAMLLoader,node:yaml.nodes.MappingNode,deep:bool=False)->dict:
    result={}
    for key_node,value_node in node.value:
        if key_node.tag=="tag:yaml.org,2002:merge" or key_node.value=="<<":
            raise ConstructorError("mapping",node.start_mark,"YAML merge keys are forbidden",key_node.start_mark)
        key=loader.construct_object(key_node,deep=deep)
        if type(key) is not str:
            raise ConstructorError("mapping",node.start_mark,"non-string YAML mapping key",key_node.start_mark)
        if key in result:
            raise ConstructorError("mapping",node.start_mark,f"duplicate YAML key: {key}",key_node.start_mark)
        result[key]=loader.construct_object(value_node,deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,construct_unique_yaml_mapping)


def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def payload_hash(data:dict)->str:
    body=dict(data);body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def semantic_hash(data:dict)->str:return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def strict_yaml_load(path:Path)->dict:
    text=path.read_text();tokens=list(yaml.scan(text))
    assert not any(isinstance(token,(AnchorToken,AliasToken)) for token in tokens)
    result=yaml.load(text,Loader=UniqueYAMLLoader);assert type(result) is dict
    return result
def validate_route_yaml(path:Path)->dict:
    route=strict_yaml_load(path);assert set(route)==set(YAML_EXPECTED)
    for key,expected in YAML_EXPECTED.items():assert type(route[key]) is type(expected),(key,type(route[key]),type(expected))
    assert type(route["scope_flags"]) is dict and set(route["scope_flags"])==set(FLAGS)
    assert all(type(value) is bool for value in route["scope_flags"].values())
    assert type(route["tuple"]) is list and all(type(value) is str for value in route["tuple"])
    assert type(route["source_owner_tokens"]) is list and all(type(value) is str for value in route["source_owner_tokens"])
    assert len(route["source_owner_tokens"])==len(set(route["source_owner_tokens"]))
    assert route==YAML_EXPECTED
    assert semantic_hash(route)==YAML_SEMANTIC_SHA
    return route
def sidecar(path:Path)->bool:return path.suffix in {".aux",".log",".out",".toc",".fls",".fdb_latexmk",".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")
def run_python(name:str)->str:
    return subprocess.check_output([sys.executable,"-B",str(ROOT/"code"/name)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"),text=True)
def pages(path:Path)->int:
    out=subprocess.check_output(["pdfinfo",str(path)],text=True);return int(next(line.split(":",1)[1] for line in out.splitlines() if line.startswith("Pages:")))
def font_rows(path:Path)->list[str]:
    out=subprocess.check_output(["pdffonts",str(path)],text=True);return [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
def pdf_text(path:Path)->str:return " ".join(subprocess.check_output(["pdftotext",str(path),"-"],text=True).lower().split())
def fresh_build(round_number:int)->tuple[bytes,str]:
    with tempfile.TemporaryDirectory(prefix=f"c290-r{round_number}-") as tmp:
        env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE="1",TZ="UTC")
        source=rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",source]
        for _ in range(2):subprocess.run(command,cwd=tmp,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=(Path(tmp)/"main.log").read_text(errors="replace");hit=WARNING_RE.search(log);assert hit is None,hit.group(0) if hit else ""
        return (Path(tmp)/"main.pdf").read_bytes(),log


def main()->None:
    assert "C290_PRODUCER_PASS" in run_python("c290_cr3bp_producer.py")
    data=json.loads(EVIDENCE.read_text());assert digest(EVIDENCE)==EVIDENCE_SHA;assert data["payload_sha256"]==payload_hash(data)
    assert data["schema"]=="hcs-c290-cr3bp-lagrange-stability-v1" and data["candidate_id"]=="HCS-C290"
    assert data["source_commit"]==SOURCE and data["evaluation_date"]=="2026-09-02" and data["fixed_epoch"]==EPOCH
    assert data["scope_literal"]==SCOPE and data["evaluator"]=={"version":"0.2.0","sha256":EVALUATOR}
    assert data["theorem_contract"]["critical"].endswith("not linearly stable")
    assert data["proof_contract"]["critical_defect"].endswith("nontrivial Jordan block")
    assert data["route_a"]=={"tuple":TUPLE,"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    assert type(data["route_a"]["route_b_invocation_allowed"]) is bool
    assert all(type(v) is bool and v is False for v in data["scope_flags"].values())
    assert data["enumeration"]=={"mu_values":["1/1000","1/100","1/50","1/30","1/25","1/10","1/4","1/2"],"triangular_cells":8,"collinear_cells":24,"critical_cells":1,"boundary_cells":5}
    assert all(type(data["enumeration"][k]) is int for k in ("triangular_cells","collinear_cells","critical_cells","boundary_cells"))
    assert data["critical_cell"]["defective"] is True and data["critical_cell"]["linear_growth"] is True and data["critical_cell"]["linearly_stable"] is False
    assert [r["identifier"] for r in data["references"]]==["Lagrange-1772-Oeuvres-VI-229-331","BnF-Gallica-ark-12148-bpt6k5789653w","10.1112/plms/s1-6.1.86","10.1007/978-0-387-09724-4"]
    route_yaml=validate_route_yaml(YAML_PATH)
    route_yaml_sha=semantic_hash(route_yaml)
    theorem=" ".join((ROOT/"THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE AS STATED","exactly five equilibria","geometric multiplicity one","not linearly stable","Finite evidence is regression only"):
        assert token in theorem,token
    source_audit=(ROOT/"SOURCE_AUDIT.md").read_text()
    for token in ("Lagrange","bpt6k5789653w","Gascheau","1874","10.1112/plms/s1-6.1.86","10.1007/978-0-387-09724-4","not literature-level originality"):
        assert token in source_audit,token
    tex=" ".join(TEX.read_text().split())
    for token in ("The Five Lagrange Equilibria","Gascheau's 1843 thesis","Routh's 1874 paper","including at mass ratios where the two linear frequencies are resonant","geometric multiplicity one","linearly growing solutions","all four exact","both $L_4$ and $L_5$","strict YAML lane","finite checks validate","AI-use statement"):
        assert token in tex,token

    checker_source=(ROOT/"code/c290_cr3bp_checker.py").read_text();tree=ast.parse(checker_source);imports=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):imports.extend(alias.name for alias in node.names)
        elif isinstance(node,ast.ImportFrom):imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    for token in ("object_pairs_hook=reject_duplicates","UniqueYAMLLoader","YAML_EXPECTED","root_bisect","for sign in (-1, 1)","for point,sign in ((\"L4\",1),(\"L5\",-1))","critical boolean types","route primitive types"):
        assert token in checker_source,token
    report=(PAPER/"COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}","two isolated fresh directories","byte-identical","warning-free",*ROUND_HASHES):assert token in report,token
    hostile=(ROOT/"results/HOSTILE_AUDIT.md").read_text()
    for token in ("wrong Coriolis sign","four critical rank cells","resonant masses","booleans to integer","duplicate JSON keys","dedicated YAML lane"):
        assert token in hostile,token

    physical={str(p.relative_to(ROOT)):p for p in ROOT.rglob("*") if p.is_file()};assert not [n for n,p in physical.items() if sidecar(p)]
    files={n:digest(p) for n,p in sorted(physical.items()) if p!=MANIFEST};assert set(files)==EXPECTED,(sorted(EXPECTED-set(files)),sorted(set(files)-EXPECTED));assert len(files)==27
    archived=[digest(p) for p in ROUND_PATHS];assert archived==ROUND_HASHES and len(set(archived))==3;assert digest(PAPER/"main.pdf")==ROUND_HASHES[2]
    page_counts=[pages(p) for p in ROUND_PATHS];assert page_counts==[3,3,4]
    font_counts=[]
    for path,terms in zip(ROUND_PATHS,ROUND_TEXT):
        rows=font_rows(path);assert rows;assert all(len(row.split())>=7 and row.split()[-5]=="yes" and row.split()[-4]=="yes" for row in rows)
        font_counts.append(len(rows));text=pdf_text(path)
        for term in terms:assert term in text,(path.name,term)
    assert font_counts==[23,23,25]
    fresh_hashes=[]
    for number,(path,expected) in enumerate(zip(ROUND_PATHS,ROUND_HASHES)):
        first,_=fresh_build(number);second,_=fresh_build(number);assert first==second==path.read_bytes()
        pair=[hashlib.sha256(first).hexdigest(),hashlib.sha256(second).hexdigest()];assert pair==[expected,expected];fresh_hashes.append(pair)

    checker=run_python("c290_cr3bp_checker.py");symbolic=run_python("c290_cr3bp_sympy_crosscheck.py");replay=run_python("c290_cr3bp_replay.py");mutation=run_python("c290_cr3bp_mutation.py")
    cm=re.search(r"PASS \((\d+) assertions",checker);sm=re.search(r"PASS \((\d+) symbolic",symbolic);mm=re.search(r"PASS (\d+)/(\d+)",mutation)
    assert cm and int(cm.group(1))==781;assert sm and int(sm.group(1))==46;assert "C290 byte replay: PASS" in replay;assert mm and mm.group(1)==mm.group(2)=="65";assert digest(EVIDENCE)==EVIDENCE_SHA
    result={
        "schema":"hcs-c290-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C290","evaluation_date":"2026-09-02","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,
        "headline":"Exactly five CR3BP Lagrange equilibria with complete collinear/triangular linear types and a defective critical boundary","theorem_status":"PROVABLE AS STATED",
        "build_contract":{"engine":"LuaLaTeX","passes_per_build":2,"fresh_builds_per_round":2,"settled_warning_regex":WARNING_RE.pattern,"round_artifacts":[str(p.relative_to(ROOT)) for p in ROUND_PATHS],"round_pdf_sha256":ROUND_HASHES,"fresh_build_sha256":fresh_hashes,"round_pdf_pages":page_counts,"round_embedded_subset_font_rows":font_counts,"all_round_text_contracts":[list(t) for t in ROUND_TEXT],"final_equals":"paper/main_round2.pdf"},
        "gates":{"G0_source_scope_evaluator":"PASS","G1_strict_schema_and_exact_types":"PASS","G2_exactly_five_equilibria":"PASS","G3_collinear_saddle_center":"PASS","G4_both_triangular_signs":"PASS","G5_routh_split_and_critical_defect":"PASS","G6_boundary_and_linear_only_firewall":"PASS","G7_checker_sympy_replay_mutation":"PASS","G8_two_substantive_revisions":"PASS","G9_six_fresh_pdf_builds_fonts_logs_text":"PASS","G10_manifest_hash_closure":"PASS","G11_source_owner_originality_boundary":"PASS","G12_route_b":"NOT_INVOKED"},
        "results":{"triangular_cells":8,"collinear_cells":24,"critical_cells":1,"critical_rank_cells":4,"boundary_cells":5,"checker_assertions":int(cm.group(1)),"symbolic_checks":int(sm.group(1)),"hostile_rejections":int(mm.group(1)),"evidence_bytes":EVIDENCE.stat().st_size,"evidence_payload_sha256":data["payload_sha256"],"evidence_sha256":EVIDENCE_SHA,"route_yaml_semantic_sha256":route_yaml_sha,"pdf_sha256":digest(PAPER/"main.pdf"),"pdf_pages":4},
        "route_a_verdict":data["route_a"],"nonclaims":data["nonclaims"],"excluded_from_manifest":["C290_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper build sidecars"],"files":files,
    }
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n");assert len([p for p in ROOT.rglob("*") if p.is_file()])==28
    print(json.dumps({"status":"C290_MANIFEST_PASS","payload_file_count":27,"physical_file_count":28,"manifest_sha256":digest(MANIFEST),"evidence_sha256":EVIDENCE_SHA,"pdf_sha256":digest(PAPER/"main.pdf")},sort_keys=True))


if __name__=="__main__":main()
