#!/usr/bin/env python3
"""Write or verify the full-project HCS-C50 release-candidate manifest."""
from __future__ import annotations
import argparse,hashlib
from pathlib import Path

PROJECT=Path(__file__).resolve().parents[1]
MANIFEST=PROJECT/"results/ARTIFACT_HASHES.sha256"
EXCLUDED={"ARTIFACT_HASHES.sha256","compile.log","main.aux","main.bbl","main.blg","main.fdb_latexmk","main.fls","main.log","main.out"}
EXCLUDED_PARTS={"__pycache__",".pytest_cache",".ipynb_checkpoints"}
REQUIRED={
 "README.md","RESEARCH_QUESTION.md","THEOREM_PACKAGE.md","PROOF_PACKAGE.md",
 "DERIVATION_PACKAGE.md","EXPERIMENT_PLAN.md","EXPERIMENT_TRACKER.md",
 "IMPLEMENTATION_CHECKLIST.md","METHODOLOGY_BLUEPRINT.md","PAPER_PLAN.md",
 "NARRATIVE_REPORT.md","SOURCE_AUDIT.md","INTEGRITY_REPORT.md",
 "route_a_evaluation.yaml","evaluations/route_a/HCS-C50/20260814T040000Z.yaml",
 "paper/main.tex","paper/main.pdf","paper/math_commands.tex","paper/references.bib",
 "paper/COMPILATION_REPORT.md","paper/sections/0_abstract.tex",
 "paper/sections/1_introduction.tex","paper/sections/2_source_and_main.tex",
 "paper/sections/3_elliptic_decomposition.tex","paper/sections/4_second_resummation.tex",
 "paper/sections/5_fourth_moment.tex","paper/sections/6_continuation_operator.tex",
 "paper/sections/7_route_a.tex","paper/sections/8_declarations.tex",
 "paper/sections/A_exact_certificates.tex",
 "code/README.md","code/c50_producer.py","code/c50_checker.py","code/test_c50.py",
 "code/run_c50.sh","code/c50_hash_manifest.py","results/RESULTS.md","results/TEST_REPORT.md",
 "results/c50_certificate.json","results/independent_check.json",
}

def digest(path:Path)->str:
 h=hashlib.sha256();
 with path.open("rb") as stream:
  for block in iter(lambda:stream.read(1<<20),b""): h.update(block)
 return h.hexdigest()

def artifacts()->list[Path]:
 paths=[]
 for path in PROJECT.rglob("*"):
  if path.is_file() and path.name not in EXCLUDED and not any(part in EXCLUDED_PARTS for part in path.parts): paths.append(path)
 relative={str(path.relative_to(PROJECT)) for path in paths}; missing=REQUIRED-relative
 if missing: raise SystemExit("required artifacts missing: "+", ".join(sorted(missing)))
 return sorted(paths,key=lambda path:str(path.relative_to(PROJECT)))

def write()->None:
 lines=[f"{digest(path)}  {path.relative_to(PROJECT)}" for path in artifacts()]
 temporary=MANIFEST.with_suffix(".sha256.new")
 temporary.write_text("\n".join(lines)+"\n",encoding="utf-8"); temporary.replace(MANIFEST)
 print(f"wrote {len(lines)} manifest entries")

def verify()->None:
 if not MANIFEST.is_file(): raise SystemExit("manifest missing")
 expected={}
 for line in MANIFEST.read_text().splitlines():
  sha,relative=line.split("  ",1); expected[relative]=sha
 actual={str(path.relative_to(PROJECT)):digest(path) for path in artifacts()}
 if expected!=actual: raise SystemExit("manifest inventory or digest mismatch")
 print(f"verified {len(expected)} manifest entries")

def main()->int:
 parser=argparse.ArgumentParser(); parser.add_argument("--write",action="store_true"); args=parser.parse_args()
 write() if args.write else verify(); return 0
if __name__=="__main__": raise SystemExit(main())
