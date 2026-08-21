#!/usr/bin/env python3
"""SymPy generating-function checks for C96."""
from __future__ import annotations
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sympy as sp
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c96_coverage_order_statistics_evidence.json'; EXPECTED_C88='4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b'
def q(v): return sp.Rational(v['numerator'],v['denominator'])
def main():
 d=json.loads(EVIDENCE.read_text()); assert d['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER' and d['authority']['c88']==EXPECTED_C88; rows=d['coverage_atlas']['rank_rows']; assert len(rows)==20; total=factorial(16); z=sp.symbols('z'); normalized=0
 for row in rows:
  poly=sp.expand(sum(row['permutation_count_by_first_reach_time'][str(k)]*z**k for k in range(17))/total)
  assert sp.simplify(poly.subs(z,1)-1)==0
  assert sp.simplify(sp.diff(poly,z).subs(z,1)-q(row['mean']))==0
  second=sp.diff(poly,z,2).subs(z,1)+sp.diff(poly,z).subs(z,1); assert sp.simplify(second-q(row['raw_moments_orders_1_to_4']['2']))==0
  assert sp.simplify(second-q(row['mean'])**2-q(row['variance']))==0
  for k in range(17):
   cert=row['first_reach_support_edge_factorial_certificate'][str(k)]
   assert cert['support_or_edge_count']*cert['completion_factorial_weight']==cert['permutation_count']==row['permutation_count_by_first_reach_time'][str(k)]
  normalized+=1
 for i in range(19):
  for k in range(17): assert q(rows[i]['cdf_by_prefix_size'][str(k)])>=q(rows[i+1]['cdf_by_prefix_size'][str(k)])
 assert rows[0]['minimum_time']==0 and rows[0]['maximum_time']==0
 print(json.dumps({'status':'C96_SYMPY_CROSSCHECK_PASS','rank_count':len(rows),'normalized_pgf_count':normalized,'factorial_certificate_count':17*len(rows),'evidence_sha256':sha256(EVIDENCE.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__': main()
