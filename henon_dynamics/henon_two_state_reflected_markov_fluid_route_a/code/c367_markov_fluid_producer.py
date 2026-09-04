#!/usr/bin/env python3
"""Canonical exact evidence for HCS-C367."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/c367_markov_fluid_evidence.json'
YML=ROOT/'evaluations/route_a/HCS-C367/2026-09-04.yaml'
SOURCE='323ea43f6970544467f8a89f0ed9be0c7c39f896'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
RAW='f2672e7cee3be37d6181bce68387adb23d82578c223914a574e05904a3648df6'
SEM='e6a6ad6f49505299d702a3d53ff5ffc2f4346ef6447e82dcda583d57f6da5552'
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
def strict_yaml(path):
    raw=path.read_text()
    for tok in yaml.scan(raw):
        if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('YAML aliases forbidden')
    z=yaml.load(raw,Loader=Loader)
    if type(z) is not dict: raise TypeError('YAML root')
    return z
def fs(q):
    q=F(q); return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def core_row(a,b,c,d):
    a,b,c,d=map(F,(a,b,c,d)); wall=a*c-b*d
    regime='stable' if wall<0 else 'null' if wall==0 else 'transient'
    row={'a':fs(a),'b':fs(b),'c':fs(c),'d':fs(d),'wall_ac_minus_bd':fs(wall),
         'mean_drift':fs(wall/(a+b)),'cycle_increment_mean':fs(c/b-d/a),'regime':regime,
         'stable_receipt':None}
    if wall<0:
        kap=(b*d-a*c)/(c*d); atom=(b*d-a*c)/((a+b)*d)
        coef0=a*c*kap/((a+b)*d); coef1=a*kap/(a+b)
        pplus=a*(c+d)/((a+b)*d); reg=(b*d-a*c)/(a+b)
        moments=[]
        for n in range(1,9):
            m0=coef0*math.factorial(n)/(kap**(n+1))
            m1=coef1*math.factorial(n)/(kap**(n+1))
            moments.append({'order':n,'state0':fs(m0),'state1':fs(m1),'total':fs(m0+m1)})
        assert c*coef1==d*coef0 and a*atom==d*coef0
        assert atom+coef0/kap==b/(a+b) and coef1/kap==a/(a+b)
        assert atom+(coef0+coef1)/kap==1 and d*atom==reg
        row['stable_receipt']={'kappa':fs(kap),'boundary_atom':fs(atom),'density0_coefficient':fs(coef0),
          'density1_coefficient':fs(coef1),'positive_workload_mass':fs(pplus),
          'zero_flux':fs(c*coef1-d*coef0),'boundary_flux_residual':fs(a*atom-d*coef0),
          'environment_marginals':[fs(atom+coef0/kap),fs(coef1/kap)],
          'total_mass':fs(atom+(coef0+coef1)/kap),'regulator_rate':fs(reg),'moments':moments}
    return row

def zero_atlas():
    return [
      {'communication':'a>0,b>0','drifts':'c>0,d>0','closed_classes':['{0,1}'],'classification':'core sign trichotomy','invariant_family':'unique only when ac<bd'},
      {'communication':'a>0,b>0','drifts':'c=0,d>0','closed_classes':['{0,1}'],'classification':'absorbing workload at zero','invariant_family':'unique delta_0 tensor pi'},
      {'communication':'a>0,b>0','drifts':'c>0,d=0','closed_classes':['{0,1}'],'classification':'linear escape at speed ac/(a+b)','invariant_family':'none'},
      {'communication':'a>0,b>0','drifts':'c=0,d=0','closed_classes':['{0,1}'],'classification':'frozen workload','invariant_family':'all nu tensor pi'},
      {'communication':'a=0,b>0','drifts':'d>0; c arbitrary','closed_classes':['{0}'],'classification':'absorb in off then drain','invariant_family':'unique delta_(0,0)'},
      {'communication':'a=0,b>0','drifts':'d=0; c arbitrary','closed_classes':['{0}'],'classification':'absorb in off then freeze','invariant_family':'all nu tensor delta_0'},
      {'communication':'a>0,b=0','drifts':'c>0; d arbitrary','closed_classes':['{1}'],'classification':'absorb in on then escape at speed c','invariant_family':'none'},
      {'communication':'a>0,b=0','drifts':'c=0; d arbitrary','closed_classes':['{1}'],'classification':'absorb in on then freeze','invariant_family':'all nu tensor delta_1'},
      {'communication':'a=0,b=0','drifts':'d>0,c>0','closed_classes':['{0}','{1}'],'classification':'off drains; on escapes','invariant_family':'delta_(0,0) only'},
      {'communication':'a=0,b=0','drifts':'d>0,c=0','closed_classes':['{0}','{1}'],'classification':'off drains; on frozen','invariant_family':'convex mixtures of delta_(0,0) and nu tensor delta_1'},
      {'communication':'a=0,b=0','drifts':'d=0,c>0','closed_classes':['{0}','{1}'],'classification':'off frozen; on escapes','invariant_family':'all nu tensor delta_0'},
      {'communication':'a=0,b=0','drifts':'d=0,c=0','closed_classes':['{0}','{1}'],'classification':'both classes frozen','invariant_family':'all laws on workload times frozen environment'}]

def build(eval_path):
    y=strict_yaml(eval_path)
    if hashlib.sha256(eval_path.read_bytes()).hexdigest()!=RAW or digest(y)!=SEM: raise AssertionError('evaluation digest drift')
    rows=[core_row(a,b,c,d) for a in (1,2,3) for b in (1,2,3) for c in (1,2,3) for d in (1,2,3)]
    regimes={q:sum(r['regime']==q for r in rows) for q in ('stable','null','transient')}
    flags={'claims_target_arithmetic_local_data':False,'claims_target_euler_factors':False,'claims_root_number':False,'claims_automorphy':False,'claims_target_divisor_or_counting_law':False,'claims_target_functional_equation':False,'claims_target_zero_match':False,'claims_hilbert_polya_operator':False,'invokes_route_b':False}
    body={'schema':'hcs-c367-reflected-markov-fluid-evidence-v1','candidate_id':'HCS-C367','obstruction_id':'HEN-O351','evaluation_date':'2026-09-04','source_commit':SOURCE,'fixed_epoch':1788480000,'scope_literal':SCOPE,
      'evaluator':{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL},
      'route_a_yaml':{'relative_path':'evaluations/route_a/HCS-C367/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM},
      'model':{'environment':'q01=a, q10=b','fluid_slopes':'r0=-d, r1=c','reflection':'X=Y+sup_{s<=t}(-Y_s)^+','core_domain':'a,b,c,d>0'},
      'theorem_contract':{'mean_drift':'(ac-bd)/(a+b)','stable':'ac<bd: positive recurrent with unique invariant probability','critical':'ac=bd: null recurrent with no invariant probability','overload':'ac>bd: transient and X_t/t tends mean drift','embedded_chain':'W_(n+1)=max(0,W_n+c I_n-d O_n)','stable_rate':'kappa=(bd-ac)/(cd)','only_atom':'mass (bd-ac)/((a+b)d) at (0,0)','all_moments':'P(X>0)*n!/kappa^n','regulator_rate':'(bd-ac)/(a+b)=d times boundary atom'},
      'proof_receipts':{'environment_stationary':'pi=(b,a)/(a+b)','cycle_mean':'c/b-d/a','cycle_time_mean':'1/b+1/a','interior_zero_flux':'c f1=d f0','boundary_balance':'a p_*=d f0(0)','critical_engine':'zero-mean nondegenerate finite-variance Lindley chain is null recurrent'},
      'finite_evidence_role':'81 exact rational core panels and 12 boundary rows are regression receipts; analytic proof owns the continuum theorem',
      'collision_boundary':{'C351':'open Jackson network with discrete queue lengths','C346':'deterministic two-dimensional oblique Skorokhod map, not a Markov-additive reflected fluid','C332':'deterministic Moreau play hysteresis'},
      'boundary_principle':'classify each closed environmental class; do not assert global uniqueness on reducible faces',
      'nonclaims':['no Brownian component or diffusion approximation','no many-state matrix-analytic extension','no finite-buffer or queueing-network product form','no priority claim','no target arithmetic, target zero match, or Hilbert-Polya operator'],
      'references':['10.1002/j.1538-7305.1982.tb03089.x','10.1080/15326349508807330'],
      'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'scope_flags':flags,
      'core_rows':rows,'zero_rate_atlas':zero_atlas(),
      'enumeration':{'core_rows':len(rows),'stable_rows':regimes['stable'],'null_rows':regimes['null'],'transient_rows':regimes['transient'],'zero_rate_rows':12,'moment_cells':8*regimes['stable']}}
    body['payload_sha256']=digest(body); return body

def main():
    if sys.flags.optimize: raise RuntimeError('C367 producer refuses optimized Python')
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=OUT); ap.add_argument('--evaluation',type=Path,default=YML); args=ap.parse_args()
    x=build(args.evaluation); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print(f'C367_PRODUCER_PASS {x["payload_sha256"]} {len(x["core_rows"])} {len(x["zero_rate_atlas"])}')
if __name__=='__main__': main()
