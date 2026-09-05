#!/usr/bin/env python3
"""Exact affine-return evidence for the complete Lozi chamber theorem."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('c385 producer refuses optimized Python')
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FLAGS=('claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation','claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b')
TUPLE=['A0_FAIL','A1_WEAK','A2_FAIL','A3_FAIL','A4_FORMAL_HINT']
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def frac(x):
    x=F(x);return [x.numerator,x.denominator]
def necklace(w): return min(w[i:]+w[:i] for i in range(len(w)))
def period(w): return next(d for d in range(1,len(w)+1) if len(w)%d==0 and w==w[:d]*(len(w)//d))
def row(a,w):
    A,B,C,D=F(1),F(0),F(0),F(1);h,k=F(0),F(0)
    for bit in w:
        t=-a*(2*int(bit)-1)
        A,B,C,D=t*A-C,t*B-D,A,B
        h,k=1+t*h-k,h
    det=(1-A)*(1-D)-B*C
    x=((1-D)*h+B*k)/det;y=(C*h+(1-A)*k)/det
    orbit=[];xx,yy=x,y
    for bit in w:
        orbit.append(frac(xx));assert (xx>0)==(bit=='1')
        xx,yy=1-a*abs(xx)-yy,xx
    assert (xx,yy)==(x,y)
    return {'a':frac(a),'word':w,'n':len(w),'least_period':period(w),
            'necklace':necklace(w[:period(w)]),'reversed_necklace':necklace(w[:period(w)][::-1]),
            'x_cycle':orbit,'matrix':[frac(v) for v in (A,B,C,D)],
            'trace':frac(A+D),'flat_denominator':frac(abs(det)),
            'unstable_sign':(-1)**w.count('1')}

def make():
    records=[];summaries=[];primitive=[]
    for a in (F(9,2),F(5),F(6)):
        for n in range(1,8):
            rows=[row(a,f'{i:0{n}b}') for i in range(2**n)]
            records.extend(rows)
            prim=[r for r in rows if r['least_period']==n and r['word']==r['necklace']]
            primitive.extend({'a':frac(a),'n':n,'word':r['word'],'trace':r['trace']} for r in prim)
            summaries.append({'a':frac(a),'n':n,'fixed':2**n,'primitive':len(prim),
                              'flat_trace':frac(sum((1/F(*r['flat_denominator']) for r in rows),F(0))),
                              'minimum_abs_coordinate':frac(min(abs(F(*v)) for r in rows for v in r['x_cycle']))})
    return {'schema':'c385-lozi-evidence-v1','candidate_id':'HCS-C385','obstruction_id':'HEN-O369',
      'source_commit':'3e692da6fa94362225c7534e9b66c83c15c7f284','evaluation_date':'2026-09-05','fixed_epoch':1788566400,
      'evaluator_authority':'flow_systems/skills/route-a-evaluator.md','evaluator_version':'0.2.0',
      'evaluator_authority_sha256':'6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c',
      'scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','scope_flags':{k:False for k in FLAGS},
      'route_a':{'tuple':TUPLE,'overall_verdict':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},
      'definition':'F_a(x,y)=(1-a*abs(x)-y,x); a>4; all bounded two-sided orbits',
      'clock':'unit map iteration; derived instability suspension is a separate clock',
      'cutoffs':{'parameters':[[9,2],[5,1],[6,1]],'period_max':7},
      'rows':records,'summaries':summaries,'primitive_rows':primitive,
      'controls':{'same_symbolic_counts_different_multipliers':'all three parameters',
        'prime_and_composite_exclusion':'all integers m>1; integer a>=5; rational positive clock scaling',
        'a4_boundary':'zero proven sign margin; no theorem asserted',
        'flat_germ_not_topological_zeta':'weights are abs(2-trace(M))^(-1)',
        'reversal_not_quotiented':'oriented primitive counts'},
      'nonclaims':['no sharp horseshoe boundary','no theorem for C116 pruned parameter',
        'no trace-class owner for flat germ','no irrational rescaling obstruction','no literature priority']}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'results/c385_lozi_evidence.json');a=p.parse_args()
    x=make();x['payload_sha256']=hashlib.sha256(canonical(x)).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
    print(f"C385 producer PASS: {len(x['rows'])} affine returns, {len(x['primitive_rows'])} primitive rows")
if __name__=='__main__':main()
