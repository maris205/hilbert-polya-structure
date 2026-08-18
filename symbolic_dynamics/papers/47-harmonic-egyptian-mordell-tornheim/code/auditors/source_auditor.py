#!/usr/bin/env python3
"""Frozen source/object auditor, physically separate from proof and literature."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Any
M="59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);a=p.parse_args();r=Path(a.root).resolve(strict=True)
 try:
  mp=r/"preauthority/SHA256SUMS.txt"
  if hashlib.sha256(mp.read_bytes()).hexdigest()!=M:raise ValueError("seal")
  names=[]
  for line in mp.read_text(encoding="ascii").splitlines():
   d,n=line.split("  ",1);q=r/"preauthority"/n
   if q.is_symlink() or hashlib.sha256(q.read_bytes()).hexdigest()!=d:raise ValueError("row")
   names.append(n)
  if names!=sorted(names) or len(names)!=15:raise ValueError("set")
  lock=(r/"preauthority/SOURCE_LOCK.md").read_text(encoding="utf-8")
  for x in ["m+n\\mid mn","Loops are retained","unit of time","not temporal primitives","P46","target zeros"]:
   if x not in lock:raise ValueError("source marker")
  out={"candidate_id":"SD-C49","payload":{"entry_count":15,"manifest_sha256":M,
       "paper46_generated_inputs":0,"source_relation":"EXACT_INTEGER_DIVISIBILITY_WITH_LOOPS",
       "source_lock_sha256":hashlib.sha256((r/"preauthority/SOURCE_LOCK.md").read_bytes()).hexdigest()},
       "schema":"paper47-source-audit-v1","status":"PASS"};sys.stdout.buffer.write(c(out))
 except Exception as e:sys.stderr.write(f"S_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
