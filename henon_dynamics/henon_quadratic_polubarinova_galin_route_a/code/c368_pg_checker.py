#!/usr/bin/env python3
"""Independent exact checker for HCS-C368; never imports the producer."""
from __future__ import annotations
import hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EV=ROOT/'results/c368_pg_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C368/2026-09-04.yaml'
RAW='c64fe4edd602d025c3213f97695986a0242f9fe01fbd94d5a1f51fc446bb104f'; SEM='06b3bda0befdab3c589ae7c15f29a2fbbfd7029b6f3128945e369828d4ac9c77'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
ROUTE=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL']
TOP={'schema','candidate_id','obstruction_id','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator','route_a_yaml','model','theorem_contract','proof_receipts','finite_evidence_role','collision_boundary','boundary_principle','nonclaims','references','route_a','scope_flags','coefficient_panels','rational_cusp_endpoints','boundary_atlas','enumeration','payload_sha256'}

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
def strict_json(path):
    def unique(pairs):
        out={}
        for k,v in pairs:
            if k in out: raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in()).throw(ValueError(s)))
def strict_yaml(path):
    raw=path.read_text()
    for tok in yaml.scan(raw):
        if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('YAML aliases forbidden')
    z=yaml.load(raw,Loader=Loader)
    if type(z) is not dict: raise TypeError('YAML root')
    return z
def keys(x,expected):
    if type(x) is not dict or set(x)!=set(expected): raise AssertionError('schema drift')
def typed_equal(left,right):
    if type(left) is not type(right): return False
    if type(left) is dict:
        return set(left)==set(right) and all(typed_equal(left[k],right[k]) for k in left)
    if type(left) in (list,tuple):
        return len(left)==len(right) and all(typed_equal(a,b) for a,b in zip(left,right))
    return left==right
def fs(q):
    q=F(q); return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def expected_panel(a,br,bi,q):
    a,br,bi,q=map(F,(a,br,bi,q)); u=a*a; norm=br*br+bi*bi; gap=u-4*norm
    geometry='smooth_univalent' if gap>0 else 'boundary_cusp' if gap==0 and norm else 'invalid_interior_critical'
    if norm==0: geometry='circle'
    receipt=None
    if gap>0:
        ad=a*q/gap; bdr=-2*q*br/gap; bdi=-2*q*bi/gap
        branch='circle' if norm==0 else 'injection' if q>0 else 'stationary' if q==0 else 'suction'
        receipt={'branch':branch,'a_dot':fs(ad),'b_dot_re':fs(bdr),'b_dot_im':fs(bdi),'kappa_re':fs(u*br),'kappa_im':fs(u*bi),
          'm0':fs(u+2*norm),'kappa_dot_re':fs(2*a*ad*br+u*bdr),'kappa_dot_im':fs(2*a*ad*bi+u*bdi),
          'm0_dot':fs(2*a*ad+4*(br*bdr+bi*bdi)),'m0_dot_minus_2q':fs(2*a*ad+4*(br*bdr+bi*bdi)-2*q),
          'ratio_squared':fs(4*norm/u)}
    return {'a':fs(a),'b_re':fs(br),'b_im':fs(bi),'q':fs(q),'u':fs(u),'b_abs_squared':fs(norm),'smooth_gap':fs(gap),'geometry':geometry,'flow_receipt':receipt}

def expected_endpoint(s,pr,pi,a0,q):
    s,pr,pi,a0,q=map(F,(s,pr,pi,a0,q)); uc=s*s; kr=s**3*pr/2; ki=s**3*pi/2; u0=a0*a0
    br=kr/u0; bi=ki/u0; m0=u0+2*(br*br+bi*bi); mc=3*uc/2; time=(m0-mc)/(-2*q); bcr=kr/uc; bci=ki/uc
    return {'s':fs(s),'phase_re':fs(pr),'phase_im':fs(pi),'a0':fs(a0),'b0_re':fs(br),'b0_im':fs(bi),'q':fs(q),
      'kappa_re':fs(kr),'kappa_im':fs(ki),'u0':fs(u0),'m0_initial':fs(m0),'u_c':fs(uc),'m0_c':fs(mc),
      'first_cusp_time':fs(time),'a_c':fs(s),'b_c_re':fs(bcr),'b_c_im':fs(bci),'zeta_c_re':fs(-pr),
      'zeta_c_im':fs(pi),'z_c_re':fs(-bcr),'z_c_im':fs(bci),'cusp_B':fs(s/2),'cusp_ratio_limit':fs(2/s),
      'time_balance_residual':'0','critical_residual':'0'}

ATLAS=[
 ('a>2|b|, b nonzero, q>0','global smooth injection','u increases without bound; 2|b|/a decreases to zero'),
 ('a>2|b|, b nonzero, q=0','stationary map','all coefficients remain fixed'),
 ('a>2|b|, b nonzero, q<0','finite-time smooth suction','first boundary-critical time is (M0-3u_c/2)/(-2q)'),
 ('b=0, q>0','expanding circles','a squared equals a0 squared plus 2qt globally'),
 ('b=0, q=0','stationary circle','a remains fixed'),
 ('b=0, q<0','shrinking circles','collapse at a0 squared divided by -2q with no pre-collapse cusp'),
 ('a=2|b| with b nonzero','already boundary-critical','ordinary semicubical cusp at time zero; excluded from smooth initial data'),
 ('0<a<2|b|','invalid conformal initial datum','f prime vanishes inside the disk; no Laplacian-growth domain is asserted')]

def check(evidence=EV,yaml_path=YML):
    n=0; x=strict_json(evidence); keys(x,TOP); n+=1
    claimed=x.pop('payload_sha256'); assert claimed==hashlib.sha256(canonical(x)).hexdigest(); x['payload_sha256']=claimed; n+=1
    assert x['schema']=='hcs-c368-quadratic-pg-evidence-v1' and x['candidate_id']=='HCS-C368' and x['obstruction_id']=='HEN-O352'; n+=3
    assert x['evaluation_date']=='2026-09-04' and x['source_commit']=='323ea43f6970544467f8a89f0ed9be0c7c39f896' and typed_equal(x['fixed_epoch'],1788480000) and x['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; n+=4
    assert typed_equal(x['evaluator'],{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL}); n+=1
    assert typed_equal(x['route_a_yaml'],{'relative_path':'evaluations/route_a/HCS-C368/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM}); n+=1
    y=strict_yaml(yaml_path); assert hashlib.sha256(yaml_path.read_bytes()).hexdigest()==RAW and hashlib.sha256(canonical(y)).hexdigest()==SEM; n+=2
    ykeys={'schema','candidate_id','title','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator_authority','evaluator_version','evaluator_authority_sha256','obstruction_id','candidate_definition','family','phase_space','dynamics','parameters','parameter_provenance','arithmetic_origin','clock','normalization','determinant_convention','orbit_cutoff','precision','training_data','forbidden_data','artifact_paths','a0','a1','a2','a3','a4','tuple','overall_verdict','route_b_invocation_allowed','route_b_lock_reason','scope_flags','theorem_status','finite_evidence_role','source_owner_tokens'}
    keys(y,ykeys); n+=1
    assert y['schema']=='route-a-evaluation-v0.2.0' and y['candidate_id']=='HCS-C368' and y['obstruction_id']=='HEN-O352'; n+=3
    assert y['evaluation_date']=='2026-09-04' and y['source_commit']==x['source_commit'] and y['fixed_epoch']==1788480000 and y['scope_literal']==x['scope_literal']; n+=4
    assert y['evaluator_authority']=='flow_systems/skills/route-a-evaluator.md' and y['evaluator_version']=='0.2.0' and y['evaluator_authority_sha256']==EVAL; n+=3
    assert y['tuple']==ROUTE and y['overall_verdict']=='ROUTE_A_REJECTED' and y['route_b_invocation_allowed'] is False; n+=3
    gates={
      'a0':('A0_FAIL','PROVED','the conserved quadratic coefficient and linear area clock are exact source-dynamical invariants','no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists'),
      'a1':('A1_FAIL','PROVED','the smooth univalent coefficient branch has an intrinsic maximal physical-time flow','moving planar boundaries do not furnish an isolated primitive-periodic-orbit ledger with source-derived weights'),
      'a2':('A2_FAIL','STOP_SCOPED','the quadratic conformal map and its coefficient invariant are globally branch-controlled until the first singularity','neither the map nor the area law is a dynamical zeta, Fredholm determinant, Euler product, or target divisor'),
      'a3':('A3_FAIL','STOP_SCOPED','injection, stationarity, suction, cusp, circular, and invalid-initial faces are closed analytically','there is no target continuation, functional equation, counting law, or Weil compression'),
      'a4':('A4_FAIL','STOP_SCOPED','the Polubarinova-Galin equation is a natural source-side free-boundary evolution','irreversible source or sink dynamics supplies no same-clock natural unitary, scattering, or Hamiltonian lift')}
    for name,(v,s,e,f) in gates.items():
        keys(y[name],{'verdict','evidence_status','strongest_evidence','strongest_failure'}); assert typed_equal(y[name],{'verdict':v,'evidence_status':s,'strongest_evidence':e,'strongest_failure':f}); n+=2
    assert y['theorem_status']=='PROVABLE_AS_STATED' and y['finite_evidence_role']=='exact coefficient and branch regression, not proof by finite sampling'; n+=2
    assert y['source_owner_tokens']==['DOI:10.1007/s13324-018-0239-3','DOI:10.1017/S0022112072002551','DOI:10.5186/aasfm.2013.3802']; n+=1
    model={'map':'f(zeta,t)=a(t) zeta+b(t) zeta^2','normalization':'a(t)>0 real, b(t) complex, f(0,t)=0','boundary_equation':'Re[f_t conjugate(zeta f_zeta)]=q on |zeta|=1','smooth_branch':'a>2|b|'}
    theorem={'coefficient_odes':'a_dot=a q/(a^2-4|b|^2), b_dot=-2q b/(a^2-4|b|^2)','invariant':'kappa=a^2 b is constant','area_clock':'M0=a^2+2|b|^2=Area/pi and M0_dot=2q','reduction':'u=a^2 and M0=F(u)=u+2|kappa|^2/u^2','branch_wall':'u_c=(4|kappa|^2)^(1/3), with smooth univalence iff u>u_c','injection':'q>0 is global and asymptotically circular','stationary':'q=0 fixes the map','suction':'q<0 and kappa nonzero reaches its first cusp at T=(M0(0)-3u_c/2)/(-2q)','circle':'kappa=0 remains circular and under suction collapses without a pre-collapse cusp'}
    proof={'fourier_constant':'a a_dot+2 Re(b_dot conjugate(b))=q','fourier_mode':'a b_dot+2 a_dot b=0','monotonicity':'F prime(u)=1-4|kappa|^2/u^3 is positive for u>u_c','critical_point':'zeta_c=-a/(2b) reaches the unit circle exactly at a=2|b|','cusp_expansion':'after rotation, z-z_c=-B s^2-i B s^3+O(s^4), so Y^2/X^3 tends 1/B'}
    assert typed_equal(x['model'],model) and typed_equal(x['theorem_contract'],theorem) and typed_equal(x['proof_receipts'],proof); n+=3
    assert x['finite_evidence_role']=='500 exact rational coefficient panels and 180 rationalized cusp endpoints are regression receipts; the analytic proof owns the continuum theorem'; n+=1
    collision={
      'workspace_scan':'G0 scan over HCS-C1--HCS-C363; the closest retained neighbors are C207 and C360',
      'workspace_nearest_neighbors':{
        'C207':'Barenblatt scalar nonlinear-diffusion similarity atlas with pressure/support free-boundary geometry; not a Polubarinova-Galin conformal-map boundary evolution',
        'C360':'Berger SU(2) homogeneous Ricci metric flow; not a Polubarinova-Galin conformal-map boundary evolution'},
      'same_batch_separation':{
        'C364':'finite Gauss reduction permutation',
        'C366':'finite Krawtchouk XX spin chain',
        'C367':'reflected Markov fluid queue'}}
    assert typed_equal(x['collision_boundary'],collision); n+=1
    assert x['boundary_principle']=='separate smooth noncircular, circular collapse, already-cusped, and interior-critical invalid initial data'; n+=1
    assert typed_equal(x['references'],['10.1007/s13324-018-0239-3','10.1017/S0022112072002551','10.5186/aasfm.2013.3802']); n+=1
    assert typed_equal(x['nonclaims'],['no surface-tension regularization or weak post-cusp continuation','no multiply connected or higher-degree classification','no identification of kappa with a target arithmetic invariant','no priority claim','no target arithmetic, target zero match, or Hilbert-Polya operator']); n+=1
    assert typed_equal(x['route_a'],{'tuple':ROUTE,'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}); n+=1
    keys(x['scope_flags'],y['scope_flags']); assert typed_equal(x['scope_flags'],y['scope_flags']) and all(type(v) is bool and v is False for v in x['scope_flags'].values()); n+=2
    vals=(F(-1),F(-1,2),F(0),F(1,2),F(1)); expected=[expected_panel(a,br,bi,q) for a in (1,2,3,4) for br in vals for bi in vals for q in (-2,-1,0,1,2)]
    assert typed_equal(x['coefficient_panels'],expected); n+=len(expected)
    for row in x['coefficient_panels']:
        if row['flow_receipt'] is None: continue
        r=row['flow_receipt']; assert F(r['kappa_dot_re'])==0 and F(r['kappa_dot_im'])==0 and F(r['m0_dot_minus_2q'])==0; n+=3
        assert F(r['ratio_squared'])<1; n+=1
    phases=((1,0),(-1,0),(0,1),(0,-1),(F(3,5),F(4,5)),(F(-3,5),F(4,5)))
    endpoints=[expected_endpoint(s,pr,pi,a0,q) for s in (1,2,3,4,5) for pr,pi in phases for a0 in (s+1,s+2) for q in (F(-1,2),-1,-2)]
    assert typed_equal(x['rational_cusp_endpoints'],endpoints); n+=len(endpoints)
    for row in x['rational_cusp_endpoints']:
        assert F(row['time_balance_residual'])==0 and F(row['critical_residual'])==0 and F(row['first_cusp_time'])>0; n+=3
        assert F(row['cusp_ratio_limit'])*F(row['cusp_B'])==1; n+=1
        ac=F(row['a_c']); bcr=F(row['b_c_re']); bci=F(row['b_c_im']); zr=F(row['zeta_c_re']); zi=F(row['zeta_c_im'])
        z2r=zr*zr-zi*zi; z2i=2*zr*zi
        assert ac*zr+bcr*z2r-bci*z2i==F(row['z_c_re']); n+=1
        assert ac*zi+bcr*z2i+bci*z2r==F(row['z_c_im']); n+=1
    for row in x['boundary_atlas']:
        keys(row,{'face','classification','endpoint'}); n+=1
    got=[(r['face'],r['classification'],r['endpoint']) for r in x['boundary_atlas']]; assert typed_equal(got,ATLAS); n+=8
    geom={name:sum(r['geometry']==name for r in expected) for name in ('smooth_univalent','boundary_cusp','invalid_interior_critical','circle')}
    branches={name:sum(r['flow_receipt'] is not None and r['flow_receipt']['branch']==name for r in expected) for name in ('injection','stationary','suction','circle')}
    enum={'coefficient_panels':500,'smooth_noncircular_panels':geom['smooth_univalent'],'boundary_cusp_panels':geom['boundary_cusp'],'invalid_panels':geom['invalid_interior_critical'],'circle_panels':geom['circle'],'injection_receipts':branches['injection'],'stationary_receipts':branches['stationary'],'suction_receipts':branches['suction'],'circle_flow_receipts':branches['circle'],'rational_cusp_endpoints':180,'boundary_rows':8}
    assert typed_equal(x['enumeration'],enum); n+=1
    return n

def main():
    if sys.flags.optimize: raise RuntimeError('C368 checker refuses optimized Python')
    print(f'C368 independent PG checker: PASS ({check()} assertions)')
if __name__=='__main__': main()
