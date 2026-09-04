#!/usr/bin/env python3
"""Repaired-hash hostile mutations and parser attacks for HCS-C367."""
from __future__ import annotations
import copy, hashlib, importlib.util, json, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EV=ROOT/'results/c367_markov_fluid_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C367/2026-09-04.yaml'; CHECK=ROOT/'code/c367_markov_fluid_checker.py'
spec=importlib.util.spec_from_file_location('c367_independent_checker',CHECK); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def setpath(x,path,value):
    q=x
    for item in path[:-1]: q=q[item]
    q[path[-1]]=value
def repaired(x):
    z=copy.deepcopy(x); z.pop('payload_sha256',None); z['payload_sha256']=hashlib.sha256(canonical(z)).hexdigest(); return z
def rejected(x,yaml_path=YML):
    with tempfile.TemporaryDirectory(prefix='c367-mut-') as d:
        p=Path(d)/'evidence.json'; p.write_text(json.dumps(repaired(x),sort_keys=True,indent=2)+'\n')
        try: mod.check(p,yaml_path)
        except Exception: return True
    return False
def main():
    if sys.flags.optimize: raise RuntimeError('C367 mutation lane refuses optimized Python')
    base=json.loads(EV.read_text()); attacks=[
      (['schema'],'wrong'),(['candidate_id'],'HCS-C366'),(['obstruction_id'],'HEN-O350'),(['evaluation_date'],'2026-09-03'),(['source_commit'],'0'*40),(['fixed_epoch'],1),(['fixed_epoch'],1788480000.0),(['scope_literal'],'BROKEN'),
      (['evaluator','authority'],'wrong'),(['evaluator','version'],'0.1.0'),(['evaluator','sha256'],'0'*64),(['route_a_yaml','relative_path'],'wrong'),(['route_a_yaml','raw_sha256'],'0'*64),(['route_a_yaml','semantic_sha256'],'0'*64),
      (['model','environment'],'q10=a'),(['model','fluid_slopes'],'r0=d'),(['model','reflection'],'unreflected'),(['model','core_domain'],'nonnegative'),
      (['theorem_contract','mean_drift'],'(ac+bd)/(a+b)'),(['theorem_contract','stable'],'ac<=bd'),(['theorem_contract','critical'],'positive recurrent'),(['theorem_contract','overload'],'oscillatory'),(['theorem_contract','embedded_chain'],'wrong order'),(['theorem_contract','stable_rate'],'reciprocal'),(['theorem_contract','only_atom'],'state 1 atom'),(['theorem_contract','all_moments'],'wrong factorial'),(['theorem_contract','regulator_rate'],'wrong sign'),
      (['proof_receipts','environment_stationary'],'pi=(a,b)/(a+b)'),(['proof_receipts','cycle_mean'],'c/a-d/b'),(['proof_receipts','cycle_time_mean'],'a+b'),(['proof_receipts','interior_zero_flux'],'c f0=d f1'),(['proof_receipts','boundary_balance'],'b p_*=c f1(0)'),(['proof_receipts','critical_engine'],'positive recurrent'),
      (['finite_evidence_role'],'finite panels prove recurrence'),(['collision_boundary','C351'],'same owner'),(['collision_boundary','C346'],'stochastic Markov-additive fluid'),(['collision_boundary','C343'],'Erlang-2 distributed-delay Hopf crossing'),(['boundary_principle'],'assert global uniqueness'),(['nonclaims',0],'Brownian component claimed'),(['references',0],'bad'),
      (['route_a','tuple',4],'A4_NATURAL_QUANTIZATION'),(['route_a','overall'],'ROUTE_A_ADVANCES'),(['route_a','route_b_invocation_allowed'],True),(['route_a','route_b_invocation_allowed'],0),(['scope_flags','claims_target_zero_match'],True),(['scope_flags','claims_target_zero_match'],0),(['scope_flags','invokes_route_b'],True),
      (['core_rows',0,'regime'],'stable'),(['core_rows',0,'mean_drift'],'1'),(['core_rows',1,'stable_receipt','kappa'],'1'),(['core_rows',1,'stable_receipt','boundary_atom'],'0'),(['core_rows',1,'stable_receipt','density0_coefficient'],'0'),(['core_rows',1,'stable_receipt','density1_coefficient'],'0'),(['core_rows',1,'stable_receipt','positive_workload_mass'],'1'),(['core_rows',1,'stable_receipt','environment_marginals',0],'0'),(['core_rows',1,'stable_receipt','regulator_rate'],'0'),(['core_rows',1,'stable_receipt','moments',0,'total'],'0'),(['core_rows',1,'stable_receipt','moments',0,'order'],True),
      (['zero_rate_atlas',1,'invariant_family'],'none'),(['zero_rate_atlas',4,'classification'],'globally irreducible'),(['zero_rate_atlas',5,'invariant_family'],'unique'),(['zero_rate_atlas',8,'invariant_family'],'none'),(['zero_rate_atlas',11,'classification'],'unique'),(['enumeration','core_rows'],80),(['enumeration','moment_cells'],0)]
    passed=0
    for path,value in attacks:
        z=copy.deepcopy(base); setpath(z,path,value)
        if not rejected(z): raise AssertionError(f'survived repaired mutation {path}')
        passed+=1
    for key in ('core_rows','zero_rate_atlas'):
        z=copy.deepcopy(base); z[key].pop()
        if not rejected(z): raise AssertionError(f'survived truncation {key}')
        passed+=1
        z=copy.deepcopy(base); z[key][0],z[key][1]=z[key][1],z[key][0]
        if not rejected(z): raise AssertionError(f'survived reorder {key}')
        passed+=1
    for path in [('evaluator','authority'),('theorem_contract','critical'),('core_rows',1,'stable_receipt','moments'),('zero_rate_atlas',0,'closed_classes'),('scope_flags','invokes_route_b')]:
        z=copy.deepcopy(base); q=z
        for item in path[:-1]: q=q[item]
        del q[path[-1]]
        if not rejected(z): raise AssertionError(f'survived deletion {path}')
        passed+=1
    z=copy.deepcopy(base); z['unexpected']=1
    if not rejected(z): raise AssertionError('survived extra evidence key')
    passed+=1
    z=copy.deepcopy(base); z['zero_rate_atlas'][0]['unexpected']=False
    if not rejected(z): raise AssertionError('survived extra zero-rate-row key')
    passed+=1
    z=copy.deepcopy(base); z['collision_boundary']={'C351':'open Jackson network with discrete queue lengths','C332':'deterministic Moreau play hysteresis','C343':'Erlang-2 distributed-delay Hopf crossing'}
    if not rejected(z): raise AssertionError('survived obsolete collision ledger')
    passed+=1
    with tempfile.TemporaryDirectory(prefix='c367-stale-') as d:
        z=copy.deepcopy(base); z['candidate_id']='bad'; p=Path(d)/'stale.json'; p.write_text(json.dumps(z))
        try: mod.check(p,YML)
        except Exception: passed+=1
        else: raise AssertionError('stale outer hash survived')
    for raw in ('{"a":1,"a":2}','{"x":NaN}','[]'):
        with tempfile.TemporaryDirectory(prefix='c367-json-') as d:
            p=Path(d)/'bad.json'; p.write_text(raw)
            try: mod.check(p,YML)
            except Exception: passed+=1
            else: raise AssertionError('malformed JSON survived')
    yraw=YML.read_text(); yaml_changes=[
      ('evaluator_authority: flow_systems/skills/route-a-evaluator.md','evaluator_authority: wrong'),
      ('evaluator_version: 0.2.0','evaluator_version: 0.1.0'),
      ('evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c','evaluator_authority_sha256: '+64*'0'),
      ('evidence_status: PROVED','evidence_status: STOP_SCOPED'),
      ('evidence_status: STOP_SCOPED','evidence_status: PROVED'),
      ('route_b_invocation_allowed: false','route_b_invocation_allowed: true'),
      ('claims_target_zero_match: false','claims_target_zero_match: true'),
      ('candidate_id: HCS-C367','candidate_id: HCS-C366'),
      ('strongest_evidence: the mean-drift wall and stationary exponential rate are exact source-dynamical quantities','strongest_evidence: altered'),
      ('strongest_failure: no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists','strongest_failure: altered'),
      ('normalization: q01=a, q10=b, r0=-d, r1=c, and right-continuous minimal regulator at zero','normalization: wrong')]
    for old,new in yaml_changes:
        with tempfile.TemporaryDirectory(prefix='c367-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw.replace(old,new,1))
            try: mod.check(EV,p)
            except Exception: passed+=1
            else: raise AssertionError(f'YAML mutation survived: {old}')
    for extra in ('\ncandidate_id: DUPLICATE\n','\nx: &a 1\ny: *a\n','\n? [a,b]\n: c\n'):
        with tempfile.TemporaryDirectory(prefix='c367-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw+extra)
            try: mod.check(EV,p)
            except Exception: passed+=1
            else: raise AssertionError('malformed YAML survived')
    print(f'C367 hostile mutation suite: PASS ({passed} attacks)')
if __name__=='__main__': main()
