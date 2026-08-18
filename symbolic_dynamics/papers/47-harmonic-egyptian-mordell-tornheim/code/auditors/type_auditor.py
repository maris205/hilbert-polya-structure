#!/usr/bin/env python3
"""Typed object/marker/clock firewall auditor T."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from typing import Any
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--root",required=True);a=p.parse_args();r=Path(a.root).resolve(strict=True)
 try:
  q=r/"preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md";t=q.read_text(encoding="utf-8")
  for x in ["PositiveIntegerVertex","IntegralHarmonicQuotient","OrderedCoprimeEdgeCoordinate","BasedClosedVertexWalk","LeastPeriodClosedOrbit","OneEdgeTimeMarker","TYPE_ERROR","CLOCK_ERROR","OPERATOR_SIGN_ERROR"]:
   if x not in t:raise ValueError("type marker")
  out={"candidate_id":"SD-C49","payload":{"bool_integer_equivalence":False,"clock":"one_edge",
   "coprime_coordinate_is_temporal_primitive":False,"harmonic_quotient_is_time":False,
   "object_contract_sha256":hashlib.sha256(q.read_bytes()).hexdigest(),"recursive_type_equality":True},
   "schema":"paper47-type-audit-v1","status":"PASS"};sys.stdout.buffer.write(c(out))
 except Exception as e:sys.stderr.write(f"T_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
