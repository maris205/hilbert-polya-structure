#!/usr/bin/env python3
"""Exact orbit-signature checks for C93."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
PROJECT=Path(__file__).resolve().parents[1]
def main():
 d=json.loads((PROJECT/'results/c93_first_passage_orbit_quotient_evidence.json').read_text()); rows=d['target_orbit_atlas']['rows']; assert len(rows)==16
 z=sp.Symbol('z')
 for row in rows:
  counts=row['law_signature']['first_passage_counts']; poly=sum(int(v)*z**i for i,v in enumerate(counts)); assert poly.subs(z,1)==20922789888000
  mean=sp.Rational(row['law_signature']['expected_first_passage_time']['numerator'],row['law_signature']['expected_first_passage_time']['denominator']); assert sp.diff(poly,z).subs(z,1)==mean*20922789888000
 assert sum(row['orbit_size'] for row in rows)==20
 print(json.dumps({'status':'C93_SYMPY_CROSSCHECK_PASS','target_orbit_count':16,'total_targets':20},sort_keys=True))
if __name__=='__main__': main()
