#!/usr/bin/env python3
"""Build a result-free source packet from the immutable P47 input."""
from __future__ import annotations
import argparse,hashlib,json,os,sys
from pathlib import Path
from typing import Any
M="59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885"
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);a=p.parse_args()
 try:
  if not os.path.isabs(a.root):raise ValueError("absolute")
  r=Path(a.root).resolve(strict=True);mp=r/"preauthority/SHA256SUMS.txt"
  if hashlib.sha256(mp.read_bytes()).hexdigest()!=M:raise ValueError("seal")
  rows=[]
  for line in mp.read_text(encoding="ascii").splitlines():
   d,n=line.split("  ",1);q=r/"preauthority"/n
   if q.is_symlink() or hashlib.sha256(q.read_bytes()).hexdigest()!=d:raise ValueError("row")
   rows.append({"path":"preauthority/"+n,"sha256":d})
  if [x["path"] for x in rows]!=sorted(x["path"] for x in rows) or len(rows)!=15:raise ValueError("set")
  out={"candidate_id":"SD-C49","payload":{"allowed_research_inputs":rows,"canonical_results_existed_at_selection":False,"paper46_generated_inputs":0,"phase2_parent_manifest_sha256":"d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181","preauthority_manifest_sha256":M,"result_status":"UNSEEN_AT_SOURCE_LOCK","target_zero_data_used":False},"schema":"paper47-source-packet-v1","status":"PASS"};sys.stdout.buffer.write(c(out))
 except Exception as e:sys.stderr.write(f"PACKET_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
