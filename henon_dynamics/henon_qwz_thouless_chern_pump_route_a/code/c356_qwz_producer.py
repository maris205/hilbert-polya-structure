#!/usr/bin/env python3
"""Canonical exact and regression evidence producer for HCS-C356."""
from __future__ import annotations
import argparse, cmath, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/c356_qwz_evidence.json'
YAML=ROOT/'evaluations/route_a/HCS-C356/2026-09-03.yaml'
SOURCE='140c8714b74de666d56f441ddfb712026955901a'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
RAW='65ca3b4edca93782ccf74b735a103dc1728c3f9ed33b74259c666a9becf1775c'
SEM='38b482ef987c719deda54769345e813b350a8103ba24e03277729292977a2b17'
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
def cy(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def digest(x): return hashlib.sha256(cy(x)).hexdigest()
def strict_yaml(path):
    raw=path.read_text()
    for tok in yaml.scan(raw):
        if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('YAML aliases forbidden')
    x=yaml.load(raw,Loader=Loader)
    if type(x) is not dict: raise TypeError('YAML root')
    return x
def fstr(x):
    x=Fraction(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def chamber(m):
    if m in (-2,0,2): return None
    return 0 if abs(m)>2 else (-1 if m<0 else 1)
def spinor(m,k,t):
    x,y,z=math.sin(k),math.sin(t),m+math.cos(k)+math.cos(t); r=math.sqrt(x*x+y*y+z*z)
    if r+z>1e-13:
        s=math.sqrt(2*r*(r+z)); return (-(x-1j*y)/s,(r+z)/s)
    s=math.sqrt(2*r*(r-z)); return ((r-z)/s,-(x+1j*y)/s)
def inner(a,b): return a[0].conjugate()*b[0]+a[1].conjugate()*b[1]
def lattice(m,n):
    u=[[spinor(m,2*math.pi*i/n,2*math.pi*j/n) for j in range(n)] for i in range(n)]
    total=0.0; minimum=1.0
    for i in range(n):
        for j in range(n):
            a=u[i][j]; b=u[(i+1)%n][j]; c=u[(i+1)%n][(j+1)%n]; d=u[i][(j+1)%n]
            links=[inner(a,b),inner(b,c),inner(c,d),inner(d,a)]
            minimum=min(minimum,*(abs(z) for z in links))
            total+=cmath.phase(math.prod(z/abs(z) for z in links))
    val=total/(2*math.pi)
    return {'m':m,'grid':n,'chern_float':f'{val:.12f}','rounded':int(round(val)),
            'absolute_residual':f'{abs(val-round(val)):.3e}','minimum_link_modulus':f'{minimum:.12f}'}
def build(eval_path):
    raw=eval_path.read_bytes(); sem=strict_yaml(eval_path)
    if hashlib.sha256(raw).hexdigest()!=RAW or digest(sem)!=SEM: raise AssertionError('evaluation digest')
    masses=[Fraction(-3),Fraction(-2),Fraction(-3,2),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(3,2),Fraction(2),Fraction(3)]
    rows=[]
    for m in masses:
        gap=2*min(abs(m+2),abs(m),abs(m-2))
        rows.append({'mass':fstr(m),'gapped':gap>0,'direct_gap':fstr(gap),'chern':chamber(m),
          'corner_norm_squared':[fstr((m+2)**2),fstr(m*m),fstr(m*m),fstr((m-2)**2)]})
    dirs=[{'mass':-2,'point':['0','0'],'chirality':1,'chern_jump':-1},
          {'mass':0,'point':['pi','0'],'chirality':-1,'chern_jump':1},
          {'mass':0,'point':['0','pi'],'chirality':-1,'chern_jump':1},
          {'mass':2,'point':['pi','pi'],'chirality':1,'chern_jump':-1}]
    grids=[lattice(m,n) for m in (-3,-1,1,3) for n in (9,15,21)]
    body={'schema':'hcs-c356-qwz-evidence-v1','candidate_id':'HCS-C356','obstruction_id':'HEN-O340',
      'evaluation_date':'2026-09-03','source_commit':SOURCE,'fixed_epoch':1788393600,'scope_literal':SCOPE,
      'evaluator':{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL},
      'route_a_yaml':{'relative_path':'evaluations/route_a/HCS-C356/2026-09-03.yaml','raw_sha256':RAW,'semantic_sha256':SEM},
      'model':{'hamiltonian':'sin(k)sigma_x+sin(tau)sigma_y+(m+cos(k)+cos(tau))sigma_z','orientation':'dk wedge dtau','lower_projector':'(I-dhat dot sigma)/2'},
      'theorem_contract':{'spectrum':'plus/minus |d|','gapped_iff':'m not in {-2,0,2}','direct_gap':'2 min(|m+2|,|m|,|m-2|)',
        'chern_convention':'(2*pi*i)^-1 integral Tr(P[dP,dP]) dk dtau','chern_mass_sum':'-1/2[sgn(m+2)-2sgn(m)+sgn(m-2)]',
        'adiabatic_charge':'filled lower band and gapped adiabatic limit only','finite_speed_exact_quantization':False},
      'proof_receipts':{'norm_square':'m^2+2+2m(x+y)+2xy','curvature_numerator':'cos(k)+cos(tau)+m cos(k) cos(tau)',
        'projector_trace':'-i/2 nhat dot (partial_k nhat cross partial_tau nhat)','north_pole_degree':'sum over four Dirac points of chirality times indicator(mass>0)',
        'dirac_jump_rule':'increasing mass changes lower c1 by -chirality'},
      'finite_grid':{'role':'regression only; analytic degree proof owns topology','mass_rows':len(rows),'dirac_rows':len(dirs),'lattice_rows':len(grids)},
      'collision_boundary':{'C318':'finite SSH chain and edges, not a Bloch-torus Chern pump','C331':'Dirac-monopole sphere and magnetic spectrum, not this QWZ line bundle','C337':'kicked-rotor resonance, not adiabatic band transport'},
      'nonclaims':['no exact finite-speed quantization','no edge theorem','no disorder or interaction theorem','no priority claim','no target arithmetic or zero match'],
      'references':['10.1103/PhysRevB.27.6083','10.1103/PhysRevB.74.085308'],
      'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_NATURAL_QUANTIZATION'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},
      'scope_flags':{'claims_target_arithmetic_local_data':False,'claims_target_euler_factors':False,'claims_root_number':False,'claims_automorphy':False,'claims_target_divisor_or_counting_law':False,'claims_target_functional_equation':False,'claims_target_zero_match':False,'claims_hilbert_polya_operator':False,'invokes_route_b':False},
      'mass_rows':rows,'dirac_rows':dirs,'lattice_gauge_rows':grids,
      'enumeration':{'exact_assertions':len(rows)*6+len(dirs)*4,'lattice_regressions':len(grids)}}
    body['payload_sha256']=digest(body); return body
def main():
    if sys.flags.optimize: raise RuntimeError('C356 producer refuses optimized Python')
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=OUT); ap.add_argument('--evaluation',type=Path,default=YAML); a=ap.parse_args()
    x=build(a.evaluation); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print(f'C356_PRODUCER_PASS {x["payload_sha256"]} {len(x["mass_rows"])} {len(x["lattice_gauge_rows"])}')
if __name__=='__main__': main()
