#!/usr/bin/env python3
"""Repaired-hash hostile mutations and parser attacks for HCS-C368."""
from __future__ import annotations
import copy, hashlib, importlib.util, json, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EV=ROOT/'results/c368_pg_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C368/2026-09-04.yaml'; CHECK=ROOT/'code/c368_pg_checker.py'
spec=importlib.util.spec_from_file_location('c368_independent_checker',CHECK); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def setpath(x,path,value):
    q=x
    for item in path[:-1]: q=q[item]
    q[path[-1]]=value
def repaired(x):
    z=copy.deepcopy(x); z.pop('payload_sha256',None); z['payload_sha256']=hashlib.sha256(canonical(z)).hexdigest(); return z
def rejected(x,yaml_path=YML):
    with tempfile.TemporaryDirectory(prefix='c368-mut-') as d:
        p=Path(d)/'evidence.json'; p.write_text(json.dumps(repaired(x),sort_keys=True,indent=2)+'\n')
        try: mod.check(p,yaml_path)
        except Exception: return True
    return False
def main():
    if sys.flags.optimize: raise RuntimeError('C368 mutation lane refuses optimized Python')
    base=json.loads(EV.read_text())
    smooth=next(i for i,r in enumerate(base['coefficient_panels']) if r['geometry']=='smooth_univalent' and r['q']=='1')
    cusp=next(i for i,r in enumerate(base['coefficient_panels']) if r['geometry']=='boundary_cusp')
    invalid=next(i for i,r in enumerate(base['coefficient_panels']) if r['geometry']=='invalid_interior_critical')
    circle=next(i for i,r in enumerate(base['coefficient_panels']) if r['geometry']=='circle')
    attacks=[
      (['schema'],'wrong'),(['candidate_id'],'HCS-C367'),(['obstruction_id'],'HEN-O351'),(['evaluation_date'],'2026-09-03'),(['source_commit'],'0'*40),(['fixed_epoch'],1),(['fixed_epoch'],1788480000.0),(['scope_literal'],'BROKEN'),
      (['evaluator','authority'],'wrong'),(['evaluator','version'],'0.1.0'),(['evaluator','sha256'],'0'*64),(['route_a_yaml','relative_path'],'wrong'),(['route_a_yaml','raw_sha256'],'0'*64),(['route_a_yaml','semantic_sha256'],'0'*64),
      (['model','map'],'linear only'),(['model','normalization'],'a complex'),(['model','boundary_equation'],'wrong sign'),(['model','smooth_branch'],'a>=|b|'),
      (['theorem_contract','coefficient_odes'],'wrong denominator'),(['theorem_contract','invariant'],'a b constant'),(['theorem_contract','area_clock'],'M0 dot=q'),(['theorem_contract','reduction'],'wrong F'),(['theorem_contract','branch_wall'],'wrong wall'),(['theorem_contract','injection'],'finite cusp'),(['theorem_contract','stationary'],'rotates'),(['theorem_contract','suction'],'wrong time'),(['theorem_contract','circle'],'pre-collapse cusp'),
      (['proof_receipts','fourier_constant'],'wrong'),(['proof_receipts','fourier_mode'],'wrong'),(['proof_receipts','monotonicity'],'negative'),(['proof_receipts','critical_point'],'inside always'),(['proof_receipts','cusp_expansion'],'linear cusp'),
      (['finite_evidence_role'],'finite panels prove continuum'),
      (['collision_boundary','workspace_scan'],'same-batch scan only'),
      (['collision_boundary','workspace_nearest_neighbors','C207'],'same conformal-map evolution'),
      (['collision_boundary','workspace_nearest_neighbors','C360'],'same conformal-map evolution'),
      (['collision_boundary','same_batch_separation','C364'],'same owner'),
      (['boundary_principle'],'merge invalid face'),(['nonclaims',0],'post-cusp continuation proved'),(['references',0],'bad'),
      (['route_a','tuple',0],'A0_STRONG_ARITHMETIC_RELATION'),(['route_a','overall'],'ROUTE_A_ADVANCES'),(['route_a','route_b_invocation_allowed'],True),(['route_a','route_b_invocation_allowed'],0),(['scope_flags','claims_target_zero_match'],True),(['scope_flags','claims_target_zero_match'],0),(['scope_flags','invokes_route_b'],True),
      (['coefficient_panels',smooth,'geometry'],'invalid_interior_critical'),(['coefficient_panels',smooth,'smooth_gap'],'0'),(['coefficient_panels',smooth,'flow_receipt','a_dot'],'0'),(['coefficient_panels',smooth,'flow_receipt','b_dot_re'],'0'),(['coefficient_panels',smooth,'flow_receipt','kappa_re'],'0'),(['coefficient_panels',smooth,'flow_receipt','kappa_dot_re'],'1'),(['coefficient_panels',smooth,'flow_receipt','m0_dot'],'0'),(['coefficient_panels',smooth,'flow_receipt','m0_dot_minus_2q'],'1'),(['coefficient_panels',smooth,'flow_receipt','ratio_squared'],'2'),
      (['coefficient_panels',cusp,'geometry'],'smooth_univalent'),(['coefficient_panels',invalid,'geometry'],'boundary_cusp'),(['coefficient_panels',circle,'geometry'],'smooth_univalent'),
      (['rational_cusp_endpoints',0,'u_c'],'0'),(['rational_cusp_endpoints',0,'m0_c'],'0'),(['rational_cusp_endpoints',0,'first_cusp_time'],'0'),(['rational_cusp_endpoints',0,'a_c'],'0'),(['rational_cusp_endpoints',0,'b_c_re'],'0'),(['rational_cusp_endpoints',0,'zeta_c_re'],'0'),(['rational_cusp_endpoints',0,'z_c_re'],'0'),(['rational_cusp_endpoints',12,'z_c_im'],'0'),(['rational_cusp_endpoints',0,'cusp_B'],'0'),(['rational_cusp_endpoints',0,'cusp_ratio_limit'],'0'),(['rational_cusp_endpoints',0,'time_balance_residual'],'1'),(['rational_cusp_endpoints',0,'critical_residual'],'1'),
      (['boundary_atlas',2,'endpoint'],'no cusp'),(['boundary_atlas',5,'endpoint'],'pre-collapse cusp'),(['boundary_atlas',6,'classification'],'smooth'),(['boundary_atlas',7,'classification'],'valid'),
      (['enumeration','coefficient_panels'],499),(['enumeration','smooth_noncircular_panels'],0),(['enumeration','rational_cusp_endpoints'],179),(['enumeration','boundary_rows'],7)]
    passed=0
    for path,value in attacks:
        z=copy.deepcopy(base); setpath(z,path,value)
        if not rejected(z): raise AssertionError(f'survived repaired mutation {path}')
        passed+=1
    for key in ('coefficient_panels','rational_cusp_endpoints','boundary_atlas'):
        z=copy.deepcopy(base); z[key].pop()
        if not rejected(z): raise AssertionError(f'survived truncation {key}')
        passed+=1
        z=copy.deepcopy(base); z[key][0],z[key][1]=z[key][1],z[key][0]
        if not rejected(z): raise AssertionError(f'survived reorder {key}')
        passed+=1
    for path in [('evaluator','authority'),('theorem_contract','suction'),('proof_receipts','cusp_expansion'),
                 ('collision_boundary','workspace_nearest_neighbors','C207'),
                 ('collision_boundary','workspace_nearest_neighbors','C360'),
                 ('rational_cusp_endpoints',0,'first_cusp_time'),('scope_flags','invokes_route_b')]:
        z=copy.deepcopy(base); q=z
        for item in path[:-1]: q=q[item]
        del q[path[-1]]
        if not rejected(z): raise AssertionError(f'survived deletion {path}')
        passed+=1
    z=copy.deepcopy(base); z['unexpected']=1
    if not rejected(z): raise AssertionError('survived extra evidence key')
    passed+=1
    z=copy.deepcopy(base); z['boundary_atlas'][0]['unexpected']=False
    if not rejected(z): raise AssertionError('survived extra boundary-row key')
    passed+=1
    with tempfile.TemporaryDirectory(prefix='c368-stale-') as d:
        z=copy.deepcopy(base); z['candidate_id']='bad'; p=Path(d)/'stale.json'; p.write_text(json.dumps(z))
        try: mod.check(p,YML)
        except Exception: passed+=1
        else: raise AssertionError('stale outer hash survived')
    for raw in ('{"a":1,"a":2}','{"x":NaN}','[]'):
        with tempfile.TemporaryDirectory(prefix='c368-json-') as d:
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
      ('candidate_id: HCS-C368','candidate_id: HCS-C367'),
      ('strongest_evidence: the conserved quadratic coefficient and linear area clock are exact source-dynamical invariants','strongest_evidence: altered'),
      ('strongest_failure: no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists','strongest_failure: altered'),
      ('normalization: f of zeta and t equals a of t times zeta plus b of t times zeta squared, with a positive and f of zero equal to zero','normalization: wrong')]
    for old,new in yaml_changes:
        with tempfile.TemporaryDirectory(prefix='c368-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw.replace(old,new,1))
            try: mod.check(EV,p)
            except Exception: passed+=1
            else: raise AssertionError(f'YAML mutation survived: {old}')
    for extra in ('\ncandidate_id: DUPLICATE\n','\nx: &a 1\ny: *a\n','\n? [a,b]\n: c\n'):
        with tempfile.TemporaryDirectory(prefix='c368-yaml-') as d:
            p=Path(d)/'bad.yaml'; p.write_text(yraw+extra)
            try: mod.check(EV,p)
            except Exception: passed+=1
            else: raise AssertionError('malformed YAML survived')
    print(f'C368 hostile mutation suite: PASS ({passed} attacks)')
if __name__=='__main__': main()
