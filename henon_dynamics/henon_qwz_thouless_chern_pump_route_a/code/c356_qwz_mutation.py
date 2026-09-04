#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutation suite for C356."""
from __future__ import annotations
import copy, hashlib, importlib.util, json, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/'results/c356_qwz_evidence.json'; Y=ROOT/'evaluations/route_a/HCS-C356/2026-09-03.yaml'; CHECK=ROOT/'code/c356_qwz_checker.py'
spec=importlib.util.spec_from_file_location('c356_independent_checker',CHECK); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def setpath(x,path,val):
    q=x
    for p in path[:-1]: q=q[p]
    q[path[-1]]=val
def repaired(x):
    z=copy.deepcopy(x); z.pop('payload_sha256',None); z['payload_sha256']=hashlib.sha256(canon(z)).hexdigest(); return z
def fails_json(x,yaml_path=Y):
    with tempfile.TemporaryDirectory(prefix='c356-mut-') as d:
        p=Path(d)/'e.json'; p.write_text(json.dumps(repaired(x),sort_keys=True,indent=2)+'\n')
        try: mod.check(p,yaml_path)
        except Exception: return True
    return False
def main():
    if sys.flags.optimize: raise RuntimeError('C356 mutation lane refuses optimized Python')
    base=json.loads(E.read_text()); attacks=[
      (['schema'],'hcs-c356-qwz-evidence-v0'),(['evaluation_date'],'2026-09-04'),
      (['candidate_id'],'HCS-C355'),(['obstruction_id'],'HEN-O339'),(['source_commit'],'0'*40),(['fixed_epoch'],1),(['scope_literal'],'BROKEN'),
      (['evaluator','authority'],'elsewhere'),(['evaluator','version'],'0.1.0'),(['evaluator','sha256'],'0'*64),
      (['route_a_yaml','relative_path'],'evaluations/route_a/HCS-C355/2026-09-03.yaml'),
      (['route_a_yaml','raw_sha256'],'0'*64),(['route_a_yaml','semantic_sha256'],'0'*64),
      (['theorem_contract','finite_speed_exact_quantization'],True),(['mass_rows',0,'chern'],1),(['mass_rows',1,'gapped'],True),
      (['mass_rows',2,'direct_gap'],'99'),(['mass_rows',3,'corner_norm_squared',0],'99'),
      (['dirac_rows',0,'chirality'],-1),(['dirac_rows',1,'chern_jump'],-1),(['lattice_gauge_rows',4,'rounded'],0),
      (['lattice_gauge_rows',5,'chern_float'],'0.25'),(['finite_grid','lattice_rows'],11),
      (['route_a','tuple',4],'A4_FAIL'),(['route_a','overall'],'ROUTE_A_ADVANCES'),(['route_a','route_b_invocation_allowed'],True),
      (['scope_flags','claims_target_zero_match'],True),(['references',0],'bad-doi'),(['enumeration','exact_assertions'],0)]
    attacks += [(['model','orientation'],'reversed'),(['theorem_contract','chern_mass_sum'],'wrong sign'),
      (['proof_receipts','north_pole_degree'],'numerical guess'),(['nonclaims',0],'finite speed exact'),
      (['collision_boundary','C318'],'same owner')]
    passed=0
    for path,val in attacks:
        z=copy.deepcopy(base); setpath(z,path,val)
        if not fails_json(z): raise AssertionError(f'survived repaired mutation {path}')
        passed+=1
    ledger_attacks=[]
    z=copy.deepcopy(base); z['mass_rows'][1]=copy.deepcopy(z['mass_rows'][0]); ledger_attacks.append(('mass duplicate/omit',z))
    z=copy.deepcopy(base); z['lattice_gauge_rows'][1]=copy.deepcopy(z['lattice_gauge_rows'][0]); ledger_attacks.append(('lattice duplicate/omit',z))
    z=copy.deepcopy(base); z['mass_rows'].pop(); ledger_attacks.append(('mass truncation',z))
    z=copy.deepcopy(base); z['lattice_gauge_rows'].pop(); ledger_attacks.append(('lattice truncation',z))
    z=copy.deepcopy(base); z['mass_rows'][0],z['mass_rows'][1]=z['mass_rows'][1],z['mass_rows'][0]; ledger_attacks.append(('mass reorder',z))
    z=copy.deepcopy(base); z['lattice_gauge_rows'][0],z['lattice_gauge_rows'][1]=z['lattice_gauge_rows'][1],z['lattice_gauge_rows'][0]; ledger_attacks.append(('lattice reorder',z))
    for label,z in ledger_attacks:
        if not fails_json(z): raise AssertionError(f'survived repaired ledger mutation: {label}')
        passed+=1
    for path in [('evaluator','authority'),('mass_rows',0,'mass'),('dirac_rows',0,'point'),('scope_flags','invokes_route_b')]:
        z=copy.deepcopy(base); q=z
        for p in path[:-1]: q=q[p]
        del q[path[-1]]
        if not fails_json(z): raise AssertionError(f'survived deletion {path}')
        passed+=1
    z=copy.deepcopy(base); z['unexpected']=1
    if not fails_json(z): raise AssertionError('survived extra key')
    passed+=1
    # Stale outer hash control.
    with tempfile.TemporaryDirectory(prefix='c356-stale-') as d:
        z=copy.deepcopy(base); z['candidate_id']='bad'; p=Path(d)/'e.json'; p.write_text(json.dumps(z))
        try: mod.check(p,Y)
        except Exception: passed+=1
        else: raise AssertionError('stale hash survived')
    # Malformed JSON controls.
    for raw in ['{"a":1,"a":2}','{"x":NaN}','[]']:
        with tempfile.TemporaryDirectory(prefix='c356-json-') as d:
            p=Path(d)/'bad.json'; p.write_text(raw)
            try: mod.check(p,Y)
            except Exception: passed+=1
            else: raise AssertionError('malformed JSON survived')
    # YAML raw/semantic and structural attacks.
    yraw=Y.read_text()
    changes=[('evaluator_authority: flow_systems/skills/route-a-evaluator.md','evaluator_authority: wrong'),
      ('evidence_status: PROVED','evidence_status: STOP_SCOPED'),('route_b_invocation_allowed: false','route_b_invocation_allowed: true'),
      ('claims_target_zero_match: false','claims_target_zero_match: true'),('candidate_id: HCS-C356','candidate_id: HCS-C355')]
    for old,new in changes:
        with tempfile.TemporaryDirectory(prefix='c356-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw.replace(old,new,1))
            try: mod.check(E,p)
            except Exception: passed+=1
            else: raise AssertionError('YAML mutation survived')
    for extra in ['\ncandidate_id: DUPLICATE\n','\nx: &a 1\ny: *a\n','\n? [a,b]\n: c\n']:
        with tempfile.TemporaryDirectory(prefix='c356-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw+extra)
            try: mod.check(E,p)
            except Exception: passed+=1
            else: raise AssertionError('malformed YAML survived')
    print(f'C356 hostile mutation suite: PASS ({passed} attacks)')
if __name__=='__main__': main()
