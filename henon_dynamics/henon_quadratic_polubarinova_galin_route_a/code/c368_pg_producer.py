#!/usr/bin/env python3
"""Canonical exact evidence for HCS-C368."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/c368_pg_evidence.json'
YML=ROOT/'evaluations/route_a/HCS-C368/2026-09-04.yaml'
SOURCE='323ea43f6970544467f8a89f0ed9be0c7c39f896'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
RAW='c64fe4edd602d025c3213f97695986a0242f9fe01fbd94d5a1f51fc446bb104f'
SEM='06b3bda0befdab3c589ae7c15f29a2fbbfd7029b6f3128945e369828d4ac9c77'
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

def panel(a,br,bi,q):
    a,br,bi,q=map(F,(a,br,bi,q)); u=a*a; norm=br*br+bi*bi; gap=u-4*norm
    geometry='smooth_univalent' if gap>0 else 'boundary_cusp' if gap==0 and norm else 'invalid_interior_critical'
    if norm==0: geometry='circle'
    row={'a':fs(a),'b_re':fs(br),'b_im':fs(bi),'q':fs(q),'u':fs(u),'b_abs_squared':fs(norm),
         'smooth_gap':fs(gap),'geometry':geometry,'flow_receipt':None}
    if gap>0:
        ad=a*q/gap; bdr=-2*q*br/gap; bdi=-2*q*bi/gap
        kre=u*br; kim=u*bi; m0=u+2*norm
        invr=2*a*ad*br+u*bdr; invi=2*a*ad*bi+u*bdi
        mdot=2*a*ad+4*(br*bdr+bi*bdi)
        branch='circle' if norm==0 else 'injection' if q>0 else 'stationary' if q==0 else 'suction'
        row['flow_receipt']={'branch':branch,'a_dot':fs(ad),'b_dot_re':fs(bdr),'b_dot_im':fs(bdi),
          'kappa_re':fs(kre),'kappa_im':fs(kim),'m0':fs(m0),'kappa_dot_re':fs(invr),
          'kappa_dot_im':fs(invi),'m0_dot':fs(mdot),'m0_dot_minus_2q':fs(mdot-2*q),
          'ratio_squared':fs(4*norm/u)}
    return row

def cusp_endpoint(s,pr,pi,a0,q):
    s,pr,pi,a0,q=map(F,(s,pr,pi,a0,q)); assert pr*pr+pi*pi==1 and a0>s and q<0
    uc=s*s; kr=s*s*s*pr/2; ki=s*s*s*pi/2; u0=a0*a0
    br=kr/u0; bi=ki/u0; norm=br*br+bi*bi; m0=u0+2*norm; mc=3*uc/2; time=(m0-mc)/(-2*q)
    bcr=kr/uc; bci=ki/uc; zr=-pr; zi=pi; z2r=zr*zr-zi*zi; z2i=2*zr*zi
    assert u0**3>4*(kr*kr+ki*ki) and bcr*bcr+bci*bci==uc/4 and time>0
    assert s*zr+bcr*z2r-bci*z2i==-bcr and s*zi+bcr*z2i+bci*z2r==bci
    return {'s':fs(s),'phase_re':fs(pr),'phase_im':fs(pi),'a0':fs(a0),'b0_re':fs(br),'b0_im':fs(bi),
      'q':fs(q),'kappa_re':fs(kr),'kappa_im':fs(ki),'u0':fs(u0),'m0_initial':fs(m0),
      'u_c':fs(uc),'m0_c':fs(mc),'first_cusp_time':fs(time),'a_c':fs(s),
      'b_c_re':fs(bcr),'b_c_im':fs(bci),'zeta_c_re':fs(-pr),'zeta_c_im':fs(pi),
      'z_c_re':fs(-bcr),'z_c_im':fs(bci),'cusp_B':fs(s/2),'cusp_ratio_limit':fs(2/s),
      'time_balance_residual':fs(m0+2*q*time-mc),'critical_residual':fs(uc**3-4*(kr*kr+ki*ki))}

def boundary_atlas():
    return [
      {'face':'a>2|b|, b nonzero, q>0','classification':'global smooth injection','endpoint':'u increases without bound; 2|b|/a decreases to zero'},
      {'face':'a>2|b|, b nonzero, q=0','classification':'stationary map','endpoint':'all coefficients remain fixed'},
      {'face':'a>2|b|, b nonzero, q<0','classification':'finite-time smooth suction','endpoint':'first boundary-critical time is (M0-3u_c/2)/(-2q)'},
      {'face':'b=0, q>0','classification':'expanding circles','endpoint':'a squared equals a0 squared plus 2qt globally'},
      {'face':'b=0, q=0','classification':'stationary circle','endpoint':'a remains fixed'},
      {'face':'b=0, q<0','classification':'shrinking circles','endpoint':'collapse at a0 squared divided by -2q with no pre-collapse cusp'},
      {'face':'a=2|b| with b nonzero','classification':'already boundary-critical','endpoint':'ordinary semicubical cusp at time zero; excluded from smooth initial data'},
      {'face':'0<a<2|b|','classification':'invalid conformal initial datum','endpoint':'f prime vanishes inside the disk; no Laplacian-growth domain is asserted'}]

def build(eval_path):
    y=strict_yaml(eval_path)
    if hashlib.sha256(eval_path.read_bytes()).hexdigest()!=RAW or digest(y)!=SEM: raise AssertionError('evaluation digest drift')
    vals=(F(-1),F(-1,2),F(0),F(1,2),F(1))
    rows=[panel(a,br,bi,q) for a in (1,2,3,4) for br in vals for bi in vals for q in (-2,-1,0,1,2)]
    phases=((1,0),(-1,0),(0,1),(0,-1),(F(3,5),F(4,5)),(F(-3,5),F(4,5)))
    endpoints=[cusp_endpoint(s,pr,pi,a0,q) for s in (1,2,3,4,5) for pr,pi in phases for a0 in (s+1,s+2) for q in (F(-1,2),-1,-2)]
    geom={name:sum(r['geometry']==name for r in rows) for name in ('smooth_univalent','boundary_cusp','invalid_interior_critical','circle')}
    branches={name:sum(r['flow_receipt'] is not None and r['flow_receipt']['branch']==name for r in rows) for name in ('injection','stationary','suction','circle')}
    flags={'claims_target_arithmetic_local_data':False,'claims_target_euler_factors':False,'claims_root_number':False,'claims_automorphy':False,'claims_target_divisor_or_counting_law':False,'claims_target_functional_equation':False,'claims_target_zero_match':False,'claims_hilbert_polya_operator':False,'invokes_route_b':False}
    body={'schema':'hcs-c368-quadratic-pg-evidence-v1','candidate_id':'HCS-C368','obstruction_id':'HEN-O352','evaluation_date':'2026-09-04','source_commit':SOURCE,'fixed_epoch':1788480000,'scope_literal':SCOPE,
      'evaluator':{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL},
      'route_a_yaml':{'relative_path':'evaluations/route_a/HCS-C368/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM},
      'model':{'map':'f(zeta,t)=a(t) zeta+b(t) zeta^2','normalization':'a(t)>0 real, b(t) complex, f(0,t)=0','boundary_equation':'Re[f_t conjugate(zeta f_zeta)]=q on |zeta|=1','smooth_branch':'a>2|b|'},
      'theorem_contract':{'coefficient_odes':'a_dot=a q/(a^2-4|b|^2), b_dot=-2q b/(a^2-4|b|^2)','invariant':'kappa=a^2 b is constant','area_clock':'M0=a^2+2|b|^2=Area/pi and M0_dot=2q','reduction':'u=a^2 and M0=F(u)=u+2|kappa|^2/u^2','branch_wall':'u_c=(4|kappa|^2)^(1/3), with smooth univalence iff u>u_c','injection':'q>0 is global and asymptotically circular','stationary':'q=0 fixes the map','suction':'q<0 and kappa nonzero reaches its first cusp at T=(M0(0)-3u_c/2)/(-2q)','circle':'kappa=0 remains circular and under suction collapses without a pre-collapse cusp'},
      'proof_receipts':{'fourier_constant':'a a_dot+2 Re(b_dot conjugate(b))=q','fourier_mode':'a b_dot+2 a_dot b=0','monotonicity':'F prime(u)=1-4|kappa|^2/u^3 is positive for u>u_c','critical_point':'zeta_c=-a/(2b) reaches the unit circle exactly at a=2|b|','cusp_expansion':'after rotation, z-z_c=-B s^2-i B s^3+O(s^4), so Y^2/X^3 tends 1/B'},
      'finite_evidence_role':'500 exact rational coefficient panels and 180 rationalized cusp endpoints are regression receipts; the analytic proof owns the continuum theorem',
      'collision_boundary':{
        'workspace_scan':'G0 scan over HCS-C1--HCS-C363; the closest retained neighbors are C207 and C360',
        'workspace_nearest_neighbors':{
          'C207':'Barenblatt scalar nonlinear-diffusion similarity atlas with pressure/support free-boundary geometry; not a Polubarinova-Galin conformal-map boundary evolution',
          'C360':'Berger SU(2) homogeneous Ricci metric flow; not a Polubarinova-Galin conformal-map boundary evolution'},
        'same_batch_separation':{
          'C364':'finite Gauss reduction permutation',
          'C366':'finite Krawtchouk XX spin chain',
          'C367':'reflected Markov fluid queue'}},
      'boundary_principle':'separate smooth noncircular, circular collapse, already-cusped, and interior-critical invalid initial data',
      'nonclaims':['no surface-tension regularization or weak post-cusp continuation','no multiply connected or higher-degree classification','no identification of kappa with a target arithmetic invariant','no priority claim','no target arithmetic, target zero match, or Hilbert-Polya operator'],
      'references':['10.1007/s13324-018-0239-3','10.1017/S0022112072002551','10.5186/aasfm.2013.3802'],
      'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'scope_flags':flags,
      'coefficient_panels':rows,'rational_cusp_endpoints':endpoints,'boundary_atlas':boundary_atlas(),
      'enumeration':{'coefficient_panels':len(rows),'smooth_noncircular_panels':geom['smooth_univalent'],'boundary_cusp_panels':geom['boundary_cusp'],'invalid_panels':geom['invalid_interior_critical'],'circle_panels':geom['circle'],'injection_receipts':branches['injection'],'stationary_receipts':branches['stationary'],'suction_receipts':branches['suction'],'circle_flow_receipts':branches['circle'],'rational_cusp_endpoints':len(endpoints),'boundary_rows':8}}
    body['payload_sha256']=digest(body); return body

def main():
    if sys.flags.optimize: raise RuntimeError('C368 producer refuses optimized Python')
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=OUT); ap.add_argument('--evaluation',type=Path,default=YML); args=ap.parse_args()
    x=build(args.evaluation); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print(f'C368_PRODUCER_PASS {x["payload_sha256"]} {len(x["coefficient_panels"])} {len(x["rational_cusp_endpoints"])}')
if __name__=='__main__': main()
