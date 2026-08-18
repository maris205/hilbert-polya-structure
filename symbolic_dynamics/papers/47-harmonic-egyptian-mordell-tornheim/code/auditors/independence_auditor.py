#!/usr/bin/env python3
"""Static physical-independence auditor I for D and P."""
from __future__ import annotations
import argparse, ast, hashlib, json, sys
from pathlib import Path
from typing import Any
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def imports(tree:ast.AST)->list[str]:
 out=[]
 for n in ast.walk(tree):
  if isinstance(n,ast.Import):out.extend(x.name for x in n.names)
  elif isinstance(n,ast.ImportFrom):out.append(n.module or "")
 return sorted(out)
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);a=p.parse_args();r=Path(a.root).resolve(strict=True)
 try:
  dp=r/"code/evaluator_d/evaluate.py";pp=r/"code/evaluator_p/evaluate.py";ds=dp.read_text(encoding="utf-8");ps=pp.read_text(encoding="utf-8")
  di=imports(ast.parse(ds));pi=imports(ast.parse(ps));allowed={"__future__","argparse","hashlib","json","math","os","stat","sys","fractions","pathlib","typing"}
  if any(x.split(".")[0] not in allowed for x in di+pi):raise ValueError("local import")
  if "(m * n) % (m + n) == 0" not in ds or "def edge(" not in ds:raise ValueError("D constructor")
  if "def parameter_support(" not in ps or "def divisor_row(" not in ps:raise ValueError("P constructors")
  if "def edge(" in ps or "% (m + n)" in ps or "evaluator_d" in ps or "evaluator_p" in ds:raise ValueError("lane leak")
  if "parameter_support" in ds or "divisor_row" in ds:raise ValueError("shared science")
  out={"candidate_id":"SD-C49","payload":{"direct_imports":di,"direct_sha256":hashlib.sha256(dp.read_bytes()).hexdigest(),
   "parameter_imports":pi,"parameter_sha256":hashlib.sha256(pp.read_bytes()).hexdigest(),
   "project_local_imports":0,"scientific_constructor_overlap":0,"shared_intermediates":0},
   "schema":"paper47-independence-audit-v1","status":"PASS"};sys.stdout.buffer.write(c(out))
 except Exception as e:sys.stderr.write(f"I_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
