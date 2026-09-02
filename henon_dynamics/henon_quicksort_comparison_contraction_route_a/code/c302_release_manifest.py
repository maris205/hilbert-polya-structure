#!/usr/bin/env python3
"""End-to-end deterministic closure for the 27-payload HCS-C302 package."""
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

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C302_RELEASE_MANIFEST.json"
EVIDENCE=ROOT/"results/c302_quicksort_evidence.json"
EVALUATION=ROOT/"evaluations/route_a/HCS-C302/2026-09-02.yaml"
TEX=ROOT/"paper/main.tex"
SOURCE="83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH=1788307200
EVIDENCE_SHA="0ceba774a464fa86ffa9cb20c44b4b7c57aafb3c6d5aec5a63f1417f92e788fc"
PAYLOAD_SHA="8f1092fa6172e1199583e8ef942cc7d5713102eef96fe9991a2af4f34f057a6b"
EVALUATION_SHA="a6b8dc1da0d76a95e818938fcea7e37f147d267a42936e161fb183aab5ef6f7c"
EVALUATION_SEMANTIC_SHA="8ad9af9fb9b8d57ef99b7df1508a3a3e29a71f9b72ecaf19f93d53a1c56a726c"
TEX_SHA="1464250b660fcb020e50832d0a6a71c07d18dea2184b106e89fc2d5a93424e4e"
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"]
FLAGS={
 "claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,
 "claims_root_number":False,"claims_automorphy":False,
 "claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,
 "claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False,
}
ROUND_PATHS=[ROOT/"paper/main_round0_original.pdf",ROOT/"paper/main_round1.pdf",ROOT/"paper/main_round2.pdf"]
ROUND_HASHES=[
 "a623329732dd0ca43dd54c1f1798b58b3ee4820d019f981759dff25c1f96f397",
 "a8f95799b46c71ea7c67f3bd66e5f011a95a13ac577b810186d6b457003c7a46",
 "e28a494e10ffa2f67f724b7458264bab62d30db6868a2c0ee38e50b46d5921bc",
]
ROUND_PAGES=[2,2,3]
ROUND_FONTS=[17,17,23]
PRESENT=[
 ["the finite recursive law","every finite law and its first two moments"],
 ["the contraction limit","same tree","recursive coupling realizes"],
 ["exact moments and non-gaussianity","third-moment license","conditional rosenthal inequality","no_bad_euler_or_root_number"],
]
ABSENT=[
 ["the contraction limit","third-moment license"],
 ["exact moments and non-gaussianity","third-moment license"],
 [],
]
EXPECTED={
 "EXPERIMENT_PLAN.md","NARRATIVE_REPORT.md","PAPER_IMPROVEMENT_LOG.md","PAPER_PLAN.md",
 "README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md","code/README.md",
 "code/c302_quicksort_checker.py","code/c302_quicksort_mutation.py","code/c302_quicksort_producer.py",
 "code/c302_quicksort_replay.py","code/c302_quicksort_sympy_crosscheck.py","code/c302_release_manifest.py",
 "evaluations/route_a/HCS-C302/2026-09-02.yaml","paper/COMPILE_REPORT.md","paper/README.md",
 "paper/main.pdf","paper/main.tex","paper/main_round0_original.pdf","paper/main_round1.pdf",
 "paper/main_round2.pdf","results/HOSTILE_AUDIT.md","results/RESULTS.md","results/TEST_REPORT.md",
 "results/c302_quicksort_evidence.json",
}
WARNING_RE=re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character",re.I)


def digest(path:Path)->str:
 return hashlib.sha256(path.read_bytes()).hexdigest()


def duplicate_guard(pairs):
 out={}
 for key,value in pairs:
  if key in out: raise ValueError(f"duplicate JSON key: {key}")
  out[key]=value
 return out


def reject_nonfinite(value):
 raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path:Path)->dict:
 text=path.read_bytes().decode("utf-8",errors="strict")
 value=json.loads(text,object_pairs_hook=duplicate_guard,parse_constant=reject_nonfinite)
 if type(value) is not dict: raise TypeError("JSON top level")
 if text!=json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False)+"\n": raise ValueError("noncanonical JSON")
 return value


class UniqueSafeLoader(yaml.SafeLoader): pass
UniqueSafeLoader.yaml_implicit_resolvers={
 key:[(tag,pattern) for tag,pattern in resolvers if tag!="tag:yaml.org,2002:timestamp"]
 for key,resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader,node,deep=False):
 out={}
 for key_node,value_node in node.value:
  if key_node.tag=="tag:yaml.org,2002:merge": raise ValueError("YAML merge")
  key=loader.construct_object(key_node,deep=deep)
  if type(key) is not str or key in out: raise ValueError("non-string or duplicate YAML key")
  out[key]=loader.construct_object(value_node,deep=deep)
 return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)


def strict_yaml(path:Path)->dict:
 raw=path.read_text(encoding="utf-8")
 for token in yaml.scan(raw):
  if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("YAML alias")
 value=yaml.load(raw,Loader=UniqueSafeLoader)
 if type(value) is not dict: raise TypeError("YAML top level")
 return value


def semantic_hash(value:dict)->str:
 return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def payload_hash(value:dict)->str:
 body=dict(value); body.pop("payload_sha256",None)
 return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def run(command:list[str],cwd:Path|None=None,env:dict[str,str]|None=None)->str:
 result=subprocess.run(command,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 if result.returncode: raise RuntimeError("command failed: "+" ".join(command)+"\n"+result.stdout)
 return result.stdout.strip()


def fresh_pdf(round_number:int)->tuple[bytes,str]:
 with tempfile.TemporaryDirectory(prefix=f"c302-r{round_number}-") as folder:
  work=Path(folder); env=dict(os.environ)
  env.update({"SOURCE_DATE_EPOCH":str(EPOCH),"FORCE_SOURCE_DATE":"1","TZ":"UTC"})
  argument=rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
  command=["lualatex","-interaction=nonstopmode","-halt-on-error","-jobname=main",argument]
  run(command,cwd=work,env=env); run(command,cwd=work,env=env)
  return (work/"main.pdf").read_bytes(),(work/"main.log").read_text(errors="replace")


def pdf_pages(path:Path)->int:
 match=re.search(r"^Pages:\s+(\d+)\s*$",run(["pdfinfo",str(path)]),re.M)
 if not match: raise AssertionError("missing page count")
 return int(match.group(1))


def font_count(path:Path)->int:
 lines=run(["pdffonts",str(path)]).splitlines()[2:]
 if not lines: raise AssertionError("no fonts")
 for line in lines:
  if re.search(r"\byes\s+yes\s+(?:yes|no)\s+\d+\s+\d+\s*$",line) is None:
   raise AssertionError("font not embedded/subset: "+line)
 return len(lines)


def render_count(path:Path,pages:int)->int:
 with tempfile.TemporaryDirectory(prefix="c302-render-") as folder:
  prefix=Path(folder)/"page"
  run(["pdftoppm","-png","-r","72",str(path),str(prefix)])
  images=list(Path(folder).glob("page-*.png"))
  if len(images)!=pages or any(image.stat().st_size==0 for image in images): raise AssertionError("render failure")
  return len(images)


def validate(evidence:dict,evaluation:dict)->None:
 assert digest(EVIDENCE)==EVIDENCE_SHA
 assert evidence["payload_sha256"]==PAYLOAD_SHA==payload_hash(evidence)
 assert digest(EVALUATION)==EVALUATION_SHA and semantic_hash(evaluation)==EVALUATION_SEMANTIC_SHA
 assert digest(TEX)==TEX_SHA
 assert evidence["candidate_id"]==evaluation["candidate_id"]=="HCS-C302"
 assert evidence["obstruction_id"]==evaluation["obstruction_id"]=="HEN-O286"
 assert evidence["source_commit"]==evaluation["source_commit"]==SOURCE
 assert evidence["fixed_epoch"]==evaluation["fixed_epoch"]==EPOCH
 assert evidence["scope_literal"]==evaluation["scope_literal"]==SCOPE
 assert evidence["evaluator_authority_sha256"]==evaluation["evaluator_authority_sha256"]==EVALUATOR
 assert evidence["route_a"]["tuple"]==evaluation["tuple"]==TUPLE
 assert evidence["route_a"]["overall_verdict"]==evaluation["overall_verdict"]=="ROUTE_A_REJECTED"
 assert evidence["route_a"]["route_b_invocation_allowed"] is False and evaluation["route_b_invocation_allowed"] is False
 assert evidence["scope_flags"]==evaluation["scope_flags"]==FLAGS and all(value is False for value in FLAGS.values())


def main()->None:
 outputs={
  "producer":run([sys.executable,str(ROOT/"code/c302_quicksort_producer.py")]),
  "independent_checker":run([sys.executable,str(ROOT/"code/c302_quicksort_checker.py")]),
  "sympy_crosscheck":run([sys.executable,str(ROOT/"code/c302_quicksort_sympy_crosscheck.py")]),
  "deterministic_replay":run([sys.executable,str(ROOT/"code/c302_quicksort_replay.py")]),
  "mutation_suite":run([sys.executable,str(ROOT/"code/c302_quicksort_mutation.py")]),
 }
 evidence=strict_json(EVIDENCE); evaluation=strict_yaml(EVALUATION); validate(evidence,evaluation)
 round_rows=[]
 for number,(archive,want_sha,want_pages,want_fonts) in enumerate(zip(ROUND_PATHS,ROUND_HASHES,ROUND_PAGES,ROUND_FONTS)):
  first,log1=fresh_pdf(number); second,log2=fresh_pdf(number); archived=archive.read_bytes()
  assert first==second==archived and hashlib.sha256(archived).hexdigest()==want_sha
  assert WARNING_RE.search(log1) is None and WARNING_RE.search(log2) is None
  pages=pdf_pages(archive); fonts=font_count(archive)
  assert pages==want_pages and fonts==want_fonts and render_count(archive,pages)==pages
  text=run(["pdftotext",str(archive),"-"]).lower()
  assert all(marker in text for marker in PRESENT[number])
  assert all(marker not in text for marker in ABSENT[number])
  round_rows.append({"round":number,"path":archive.relative_to(ROOT).as_posix(),"sha256":want_sha,
   "pages":pages,"embedded_subset_font_rows":fonts,"two_fresh_builds_identical":True,
   "archived_bytes_match":True,"warning_free_second_passes":True,"rendered_pages":pages})
 assert len(set(ROUND_HASHES))==3
 final=ROOT/"paper/main.pdf"
 assert final.read_bytes()==ROUND_PATHS[2].read_bytes() and digest(final)==ROUND_HASHES[2]
 actual={path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_file()}
 assert actual==EXPECTED|{MANIFEST.name},("tree mismatch",sorted(actual-(EXPECTED|{MANIFEST.name})),sorted((EXPECTED|{MANIFEST.name})-actual))
 files=[{"path":name,"sha256":digest(ROOT/name),"bytes":(ROOT/name).stat().st_size} for name in sorted(EXPECTED)]
 manifest={
  "schema":"hcs-c302-release-manifest-v1","candidate_id":"HCS-C302","obstruction_id":"HEN-O286",
  "title":"Exact Quicksort comparison costs and contraction limit","evaluation_date":"2026-09-02",
  "source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"evaluator_authority_sha256":EVALUATOR,
  "payload_file_count":len(EXPECTED),"physical_file_count":len(EXPECTED)+1,
  "evidence":{"path":EVIDENCE.relative_to(ROOT).as_posix(),"file_sha256":EVIDENCE_SHA,
   "payload_sha256":PAYLOAD_SHA,"finite_pgf_rows":evidence["regression_summary"]["finite_pgf_rows"],
   "pgf_coefficient_cells":evidence["regression_summary"]["pgf_coefficient_cells"],
   "centered_pivot_rows":evidence["regression_summary"]["centered_pivot_rows"],
   "variance_diagnostic_rows":evidence["regression_summary"]["variance_diagnostic_rows"]},
  "evaluation":{"path":EVALUATION.relative_to(ROOT).as_posix(),"file_sha256":EVALUATION_SHA,
   "semantic_sha256":EVALUATION_SEMANTIC_SHA,"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED",
   "route_b_invocation_allowed":False,"scope_flags":FLAGS},
  "paper":{"tex_sha256":TEX_SHA,"rounds":round_rows,"all_round_hashes_distinct":True,
   "final_path":"paper/main.pdf","final_sha256":ROUND_HASHES[2],"final_equals_round2":True},
  "verification":{key:value.splitlines() for key,value in outputs.items()}|{"closed_world":True},
  "files":files,
 }
 MANIFEST.write_text(json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
 assert strict_json(MANIFEST)==manifest and len(files)==27 and len(actual)==28
 print("C302 release PASS")
 print(f"payload_files={len(files)} physical_files={len(actual)}")
 print(f"evidence_sha256={EVIDENCE_SHA}")
 print(f"payload_sha256={PAYLOAD_SHA}")
 print(f"final_pdf_sha256={ROUND_HASHES[2]}")
 print(f"manifest_sha256={digest(MANIFEST)}")


if __name__=="__main__": main()
