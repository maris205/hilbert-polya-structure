#!/usr/bin/env python3
"""Canonical exact implementation evidence for HCS-C362."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/c362_cucker_smale_evidence.json'
YML=ROOT/'evaluations/route_a/HCS-C362/2026-09-04.yaml'
SOURCE='05ca5f96b2c69a6ad6ba153d1084df750d7722c0'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
RAW='db434760c390e4bfe52298390a8a1ac342152d0b6b33db719e3c42d11f85ad09'
SEM='941bac50bb2f6c8998e8a0dd072a2caecfc8831d18b0e290b363b87cfe2a158a'
SCOPE='NO_BAD_EULER_OR_ROOT_NUMBER'

class Loader(yaml.SafeLoader): pass
Loader.yaml_implicit_resolvers={k:[(t,r) for t,r in v if t!='tag:yaml.org,2002:timestamp'] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        if kn.tag=='tag:yaml.org,2002:merge': raise ValueError('merge key')
        k=loader.construct_object(kn,deep=deep)
        if type(k) is not str or k in out: raise ValueError('duplicate/non-string YAML key')
        out[k]=loader.construct_object(vn,deep=deep)
    return out
Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def digest(x): return hashlib.sha256(canonical(x)).hexdigest()
def strict_yaml(p):
    raw=p.read_text()
    for tok in yaml.scan(raw):
        if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('YAML aliases forbidden')
    z=yaml.load(raw,Loader=Loader)
    if type(z) is not dict: raise TypeError('YAML root')
    return z
def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def vsub(x,y): return [a-b for a,b in zip(x,y)]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def norm2(x): return dot(x,x)
def make_row(label,positions,velocities,K,beta):
    p=[[F(z) for z in q] for q in positions]; v=[[F(z) for z in q] for q in velocities]
    N=len(p); d=len(p[0]); weights=[]
    for i in range(N):
        weights.append([])
        for j in range(N):
            q=1+norm2(vsub(p[i],p[j])); weights[-1].append(q**(-beta))
    acc=[]
    for i in range(N):
        acc.append([K/F(N)*sum((weights[i][j]*(v[j][k]-v[i][k]) for j in range(N)),F(0)) for k in range(d)])
    mean_acc=[sum((acc[i][k] for i in range(N)),F(0))/N for k in range(d)]
    mean_v=[sum((v[i][k] for i in range(N)),F(0))/N for k in range(d)]
    ed=F(2,N)*sum((dot(vsub(v[i],mean_v),acc[i]) for i in range(N)),F(0))
    rhs=-K/F(N*N)*sum((weights[i][j]*norm2(vsub(v[i],v[j])) for i in range(N) for j in range(N)),F(0))
    X2=max(norm2(vsub(p[i],p[j])) for i in range(N) for j in range(i+1,N))
    V2=max(norm2(vsub(v[i],v[j])) for i in range(N) for j in range(i+1,N))
    active=[(i,j) for i in range(N) for j in range(i+1,N) if norm2(vsub(v[i],v[j]))==V2]
    upper=max(F(2)*dot(vsub(v[i],v[j]),vsub(acc[i],acc[j])) for i,j in active)
    bound=-F(2)*K*(1+X2)**(-beta)*V2
    if any(mean_acc) or ed!=rhs or upper>bound: raise AssertionError('exact row identity')
    return {'label':f'{label}-K{fs(K)}-b{beta}','N':N,'d':d,'K':fs(K),'beta':str(beta),
      'positions':[[fs(z) for z in q] for q in p],'velocities':[[fs(z) for z in q] for q in v],
      'mean_acceleration':[fs(z) for z in mean_acc],'energy_derivative':fs(ed),'ordered_pair_rhs':fs(rhs),
      'position_diameter_squared':fs(X2),'velocity_diameter_squared':fs(V2),
      'active_velocity_pairs':[[i,j] for i,j in active],
      'diameter_squared_derivative_upper':fs(upper),'diameter_squared_bound_upper':fs(bound)}
def build(eval_path):
    y=strict_yaml(eval_path)
    if hashlib.sha256(eval_path.read_bytes()).hexdigest()!=RAW or digest(y)!=SEM: raise AssertionError('evaluation digest')
    configs=[
      ('two-line',[[0],[1]],[[2],[-1]]),
      ('three-line',[[-1],[0],[2]],[[3],[0],[-2]]),
      ('four-line',[[0],[2],[5],[9]],[[4],[1],[0],[-3]]),
      ('three-plane',[[0,0],[2,0],[0,3]],[[2,1],[-1,0],[0,-2]])]
    systems=[make_row(label,p,v,K,b) for label,p,v in configs for K in (F(1,2),F(1),F(2)) for b in (0,1,2)]
    primitive=[
      {'beta':'0','primitive':'r','total_tail_from_zero':'infinity','tail_diverges':True},
      {'beta':'1/2','primitive':'asinh(r)','total_tail_from_zero':'infinity','tail_diverges':True},
      {'beta':'1','primitive':'atan(r)','total_tail_from_zero':'pi/2','tail_diverges':False},
      {'beta':'3/2','primitive':'r/sqrt(1+r^2)','total_tail_from_zero':'1','tail_diverges':False},
      {'beta':'2','primitive':'atan(r)/2+r/(2*(1+r^2))','total_tail_from_zero':'pi/4','tail_diverges':False}]
    two=[
      {'beta':'3/2','K':'1','r0':'0','u0':'1/2','regime':'below','limit_distance':'1/sqrt(3)','limit_speed':'0','confined':True},
      {'beta':'3/2','K':'1','r0':'0','u0':'1','regime':'equality','limit_distance':'infinity','limit_speed':'0','confined':False},
      {'beta':'3/2','K':'1','r0':'0','u0':'3/2','regime':'above','limit_distance':'infinity','limit_speed':'1/2','confined':False}]
    flags={'claims_target_arithmetic_local_data':False,'claims_target_euler_factors':False,'claims_root_number':False,'claims_automorphy':False,'claims_target_divisor_or_counting_law':False,'claims_target_functional_equation':False,'claims_target_zero_match':False,'claims_hilbert_polya_operator':False,'invokes_route_b':False}
    body={'schema':'hcs-c362-cucker-smale-evidence-v1','candidate_id':'HCS-C362','obstruction_id':'HEN-O346','evaluation_date':'2026-09-04','source_commit':SOURCE,'fixed_epoch':1788480000,'scope_literal':SCOPE,
      'evaluator':{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL},
      'route_a_yaml':{'relative_path':'evaluations/route_a/HCS-C362/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM},
      'model':{'equations':'dot x_i=v_i; dot v_i=(K/N) sum_j psi(|x_j-x_i|)(v_j-v_i)','communication':'psi(r)=(1+r^2)^(-beta)','core_parameters':'N>=2,d>=1,K>0,beta>=0'},
      'theorem_contract':{'global_flow':True,'mean_velocity_conserved':True,'ordered_variance_dissipation':'-K/N^2 sum_ij psi_ij |v_i-v_j|^2','diameter_comparison':['D+ X <= V','D+ V <= -K psi(X) V'],'conditional_gate':'V0 < K integral_X0^infinity psi','confinement':'K integral_X0^R psi=V0','alignment_rate':'K psi(R)','unconditional_chamber':'0<=beta<=1/2','many_body_gate_is_necessary':False,'two_body_sharpness':'outward scalar N=2 trichotomy below/equality/above for beta>1/2'},
      'proof_receipts':{'barrier':'V+K integral_X0^X psi is nonincreasing','primitive':'Phi_beta(r)=r*2F1(1/2,beta;3/2;-r^2)','tail_test':'integral at infinity diverges iff beta<=1/2','two_body_first_integral':'u(r)=u0-K integral_r0^r psi','equality_boundary':'u tends zero while r tends infinity','above_boundary':'u and r/t tend u0-A>0'},
      'finite_evidence_role':'exact normalization and implementation receipt only; analytic proof owns arbitrary N and d',
      'collision_boundary':{'C203':'fixed signed-Laplacian first-order consensus','C333':'randomized edge gossip second moments','C347':'noisy mean-field Kuramoto phases'},
      'boundary_atlas':{'N=1':'diameters identically zero','K=0':'constant velocities; flocking iff V0=0','V0=0':'relative positions fixed','coincident_agents':'regular because psi(0)=1','beta=1/2':'unconditional endpoint','failed_many_body_gate':'no general non-flocking conclusion'},
      'nonclaims':['no necessity of the many-body sufficient gate','no singular kernel or collision-avoidance theorem','no delay, noise, or mean-field theorem','no priority claim','no target arithmetic, zero match, or Hilbert-Polya operator'],
      'references':['10.1109/TAC.2007.895842','10.4310/CMS.2009.v7.n2.a2'],
      'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'scope_flags':flags,
      'exact_system_rows':systems,'primitive_rows':primitive,'two_body_rows':two,
      'enumeration':{'exact_system_rows':len(systems),'primitive_rows':len(primitive),'two_body_rows':len(two),'exact_coordinate_cells':sum(r['N']*r['d'] for r in systems)}}
    body['payload_sha256']=digest(body); return body
def main():
    if sys.flags.optimize: raise RuntimeError('C362 producer refuses optimized Python')
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=OUT); ap.add_argument('--evaluation',type=Path,default=YML); a=ap.parse_args()
    x=build(a.evaluation); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print(f'C362_PRODUCER_PASS {x["payload_sha256"]} {len(x["exact_system_rows"])} {len(x["two_body_rows"])}')
if __name__=='__main__': main()
