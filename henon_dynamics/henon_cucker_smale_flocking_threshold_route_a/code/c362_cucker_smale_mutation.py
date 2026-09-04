#!/usr/bin/env python3
"""Hostile repaired-hash and strict-parser mutations for C362."""
from __future__ import annotations
import copy, hashlib, importlib.util, json, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/'results/c362_cucker_smale_evidence.json'; Y=ROOT/'evaluations/route_a/HCS-C362/2026-09-04.yaml'; CHECK=ROOT/'code/c362_cucker_smale_checker.py'
spec=importlib.util.spec_from_file_location('c362_checker',CHECK); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def setpath(x,path,val):
    q=x
    for p in path[:-1]: q=q[p]
    q[path[-1]]=val
def repaired(x):
    z=copy.deepcopy(x); z.pop('payload_sha256',None); z['payload_sha256']=hashlib.sha256(canon(z)).hexdigest(); return z
def fails(x,yaml_path=Y):
    with tempfile.TemporaryDirectory(prefix='c362-mut-') as d:
        p=Path(d)/'e.json'; p.write_text(json.dumps(repaired(x),sort_keys=True,indent=2)+'\n')
        try: mod.check(p,yaml_path)
        except Exception: return True
    return False
def main():
    if sys.flags.optimize: raise RuntimeError('C362 mutation lane refuses optimized Python')
    base=json.loads(E.read_text()); attacks=[
      (['schema'],'wrong'),(['candidate_id'],'HCS-C361'),(['obstruction_id'],'HEN-O345'),(['evaluation_date'],'2026-09-03'),(['source_commit'],'0'*40),(['fixed_epoch'],1),(['scope_literal'],'BROKEN'),
      (['evaluator','authority'],'wrong'),(['evaluator','version'],'0.1.0'),(['evaluator','sha256'],'0'*64),(['route_a_yaml','relative_path'],'wrong'),(['route_a_yaml','raw_sha256'],'0'*64),(['route_a_yaml','semantic_sha256'],'0'*64),
      (['model','communication'],'psi=1'),(['theorem_contract','global_flow'],False),(['theorem_contract','ordered_variance_dissipation'],'wrong factor'),(['theorem_contract','diameter_comparison',1],'wrong sign'),(['theorem_contract','conditional_gate'],'non-strict gate'),(['theorem_contract','unconditional_chamber'],'beta<1/2'),(['theorem_contract','many_body_gate_is_necessary'],True),(['theorem_contract','two_body_sharpness'],'missing equality'),
      (['proof_receipts','barrier'],'increasing'),(['proof_receipts','equality_boundary'],'confined'),(['finite_evidence_role'],'proof by sampling'),(['collision_boundary','C203'],'same owner'),(['boundary_atlas','K=0'],'always flocks'),(['boundary_atlas','beta=1/2'],'excluded'),(['nonclaims',0],'necessity claimed'),(['references',0],'bad'),
      (['route_a','tuple',4],'A4_FORMAL_HINT'),(['route_a','overall'],'ROUTE_A_ADVANCES'),(['route_a','route_b_invocation_allowed'],True),(['scope_flags','claims_target_zero_match'],True),
      (['exact_system_rows',0,'energy_derivative'],'0'),(['exact_system_rows',1,'ordered_pair_rhs'],'0'),(['exact_system_rows',2,'diameter_squared_bound_upper'],'0'),(['exact_system_rows',3,'mean_acceleration',0],'1'),(['exact_system_rows',4,'label'],'renamed'),(['primitive_rows',1,'tail_diverges'],False),(['primitive_rows',3,'total_tail_from_zero'],'2'),(['two_body_rows',1,'confined'],True),(['two_body_rows',2,'limit_speed'],'0'),(['enumeration','exact_system_rows'],35),
      (['boundary_atlas','failed_many_body_gate'],'non-flocking')]
    passed=0
    for path,val in attacks:
        z=copy.deepcopy(base); setpath(z,path,val)
        if not fails(z): raise AssertionError(f'survived repaired mutation {path}')
        passed+=1
    for label,key in [('system','exact_system_rows'),('primitive','primitive_rows'),('two-body','two_body_rows')]:
        z=copy.deepcopy(base); z[key].pop()
        if not fails(z): raise AssertionError(f'survived {label} truncation')
        passed+=1
        z=copy.deepcopy(base); z[key][0],z[key][1]=z[key][1],z[key][0]
        if not fails(z): raise AssertionError(f'survived {label} reorder')
        passed+=1
    for path in [('evaluator','authority'),('theorem_contract','conditional_gate'),('exact_system_rows',0,'label'),('scope_flags','invokes_route_b')]:
        z=copy.deepcopy(base); q=z
        for p in path[:-1]: q=q[p]
        del q[path[-1]]
        if not fails(z): raise AssertionError(f'survived deletion {path}')
        passed+=1
    z=copy.deepcopy(base); z['unexpected']=1
    if not fails(z): raise AssertionError('survived extra key')
    passed+=1
    with tempfile.TemporaryDirectory(prefix='c362-stale-') as d:
        z=copy.deepcopy(base); z['candidate_id']='bad'; p=Path(d)/'e.json'; p.write_text(json.dumps(z))
        try: mod.check(p,Y)
        except Exception: passed+=1
        else: raise AssertionError('stale hash survived')
    for raw in ['{"a":1,"a":2}','{"x":NaN}','[]']:
        with tempfile.TemporaryDirectory(prefix='c362-json-') as d:
            p=Path(d)/'bad.json'; p.write_text(raw)
            try: mod.check(p,Y)
            except Exception: passed+=1
            else: raise AssertionError('malformed JSON survived')
    yraw=Y.read_text(); changes=[
      ('evaluator_authority: flow_systems/skills/route-a-evaluator.md','evaluator_authority: wrong'),('evidence_status: PROVED','evidence_status: STOP_SCOPED'),('route_b_invocation_allowed: false','route_b_invocation_allowed: true'),('claims_target_zero_match: false','claims_target_zero_match: true'),('candidate_id: HCS-C362','candidate_id: HCS-C361'),
      ('strongest_evidence: the tail barrier and sharp scalar threshold are exact source-dynamical quantities','strongest_evidence: altered'),
      ('strongest_failure: no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists','strongest_failure: altered'),
      ('normalization: complete ordered-pair sum with K/N and psi(r)=(1+r^2)^(-beta)','normalization: wrong factor')]
    for old,new in changes:
        with tempfile.TemporaryDirectory(prefix='c362-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw.replace(old,new,1))
            try: mod.check(E,p)
            except Exception: passed+=1
            else: raise AssertionError('YAML mutation survived')
    for extra in ['\ncandidate_id: DUPLICATE\n','\nx: &a 1\ny: *a\n','\n? [a,b]\n: c\n']:
        with tempfile.TemporaryDirectory(prefix='c362-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw+extra)
            try: mod.check(E,p)
            except Exception: passed+=1
            else: raise AssertionError('malformed YAML survived')
    print(f'C362 hostile mutation suite: PASS ({passed} attacks)')
if __name__=='__main__': main()
