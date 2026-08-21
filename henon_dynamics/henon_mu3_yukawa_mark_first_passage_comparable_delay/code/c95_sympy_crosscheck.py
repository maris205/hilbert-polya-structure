#!/usr/bin/env python3
"""SymPy normalization, moment, conditional, and marginal checks for C95."""
from __future__ import annotations
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sympy as sp

PROJECT=Path(__file__).resolve().parents[1]
EVIDENCE=PROJECT/'results/c95_comparable_delay_evidence.json'
EXPECTED_C88='4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b'
EXPECTED_C90='c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978'

def q(v): return sp.Rational(v['numerator'],v['denominator'])

def main():
 d=json.loads(EVIDENCE.read_text()); assert d['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; assert d['authority']['c88']==EXPECTED_C88 and d['authority']['c90']==EXPECTED_C90
 rows=d['delay_atlas']['pair_rows']; assert len(rows)==102; total=factorial(16); x,y,z=sp.symbols('x y z'); conditional=0
 for row in rows:
  pmf=row['joint_pmf_permutation_counts']; poly=sp.expand(sum(pmf[str(a)][str(b)]*x**a*y**b for a in range(17) for b in range(17))/total)
  assert sp.simplify(poly.subs({x:1,y:1})-1)==0
  assert all(pmf[str(a)][str(b)]==0 for a in range(17) for b in range(17) if a>b)
  dpoly=sp.expand(sum(row['delay_permutation_count_by_delta'][str(delta)]*z**delta for delta in range(17))/total)
  assert sp.simplify(dpoly.subs(z,1)-1)==0
  assert sp.simplify(sp.diff(dpoly,z).subs(z,1)-q(row['delay_mean']))==0
  second=sp.diff(dpoly,z,2).subs(z,1)+sp.diff(dpoly,z).subs(z,1)
  assert sp.simplify(second-q(row['delay_second_moment']))==0
  assert sp.simplify(second-q(row['delay_mean'])**2-q(row['delay_variance']))==0
  assert all(row['marginal_identity'].values())
  for c in row['conditional_delay_rows_given_lower_time']:
   den=c['conditioning_permutation_count']; cp=sum(q(c['conditional_delay_probability_by_delta'][str(delta)])*z**delta for delta in range(17))
   if den:
    assert sp.simplify(cp.subs(z,1)-1)==0
    assert sp.simplify(sp.diff(cp,z).subs(z,1)-q(c['conditional_mean_delay']))==0
    csecond=sp.diff(cp,z,2).subs(z,1)+sp.diff(cp,z).subs(z,1)
    assert sp.simplify(csecond-q(c['conditional_second_moment_delay']))==0
    assert sp.simplify(csecond-q(c['conditional_mean_delay'])**2-q(c['conditional_variance_delay']))==0
    conditional+=1
   else: assert sp.simplify(cp)==0
 print(json.dumps({'status':'C95_SYMPY_CROSSCHECK_PASS','pair_count':len(rows),'conditional_rows_with_positive_mass':conditional,'evidence_sha256':sha256(EVIDENCE.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__': main()
