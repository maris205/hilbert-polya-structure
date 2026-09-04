#!/usr/bin/env python3
"""Independent exact checker for HCS-C362; never imports the producer."""
from __future__ import annotations
import hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]; EV=ROOT/'results/c362_cucker_smale_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C362/2026-09-04.yaml'
RAW='db434760c390e4bfe52298390a8a1ac342152d0b6b33db719e3c42d11f85ad09'; SEM='941bac50bb2f6c8998e8a0dd072a2caecfc8831d18b0e290b363b87cfe2a158a'
TOP={'schema','candidate_id','obstruction_id','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator','route_a_yaml','model','theorem_contract','proof_receipts','finite_evidence_role','collision_boundary','boundary_atlas','nonclaims','references','route_a','scope_flags','exact_system_rows','primitive_rows','two_body_rows','enumeration','payload_sha256'}
ROUTE=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL']
class Loader(yaml.SafeLoader): pass
Loader.yaml_implicit_resolvers={k:[(t,r) for t,r in v if t!='tag:yaml.org,2002:timestamp'] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def mapping(loader,node,deep=False):
    d={}
    for kn,vn in node.value:
        if kn.tag=='tag:yaml.org,2002:merge': raise ValueError('merge')
        k=loader.construct_object(kn,deep=deep)
        if type(k) is not str or k in d: raise ValueError('duplicate/non-string YAML key')
        d[k]=loader.construct_object(vn,deep=deep)
    return d
Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def strict_json(p):
    def uniq(pairs):
        d={}
        for k,v in pairs:
            if k in d: raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(p.read_text(),object_pairs_hook=uniq,parse_constant=lambda s:(_ for _ in()).throw(ValueError(s)))
def strict_yaml(p):
    raw=p.read_text()
    for t in yaml.scan(raw):
        if isinstance(t,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('alias')
    z=yaml.load(raw,Loader=Loader)
    if type(z) is not dict: raise TypeError('root')
    return z
def keys(x,s):
    if type(x) is not dict or set(x)!=set(s): raise AssertionError('schema drift')
def frac(s): return F(s)
def sub(x,y): return [a-b for a,b in zip(x,y)]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def norm2(x): return dot(x,x)
def recompute(row):
    p=[[frac(z) for z in q] for q in row['positions']]; v=[[frac(z) for z in q] for q in row['velocities']]
    N=row['N']; d=row['d']; K=frac(row['K']); beta=int(row['beta'])
    assert len(p)==len(v)==N and all(len(q)==d for q in p+v)
    w=[[(1+norm2(sub(p[i],p[j])))**(-beta) for j in range(N)] for i in range(N)]
    a=[ [K/F(N)*sum((w[i][j]*(v[j][k]-v[i][k]) for j in range(N)),F(0)) for k in range(d)] for i in range(N)]
    ma=[sum((a[i][k] for i in range(N)),F(0))/N for k in range(d)]
    mv=[sum((v[i][k] for i in range(N)),F(0))/N for k in range(d)]
    ed=F(2,N)*sum((dot(sub(v[i],mv),a[i]) for i in range(N)),F(0))
    rhs=-K/F(N*N)*sum((w[i][j]*norm2(sub(v[i],v[j])) for i in range(N) for j in range(N)),F(0))
    X2=max(norm2(sub(p[i],p[j])) for i in range(N) for j in range(i+1,N)); V2=max(norm2(sub(v[i],v[j])) for i in range(N) for j in range(i+1,N))
    active=[(i,j) for i in range(N) for j in range(i+1,N) if norm2(sub(v[i],v[j]))==V2]
    upper=max(2*dot(sub(v[i],v[j]),sub(a[i],a[j])) for i,j in active); bound=-2*K*(1+X2)**(-beta)*V2
    return ma,ed,rhs,X2,V2,active,upper,bound
def check(evidence=EV,yaml_path=YML):
    n=0; x=strict_json(evidence); keys(x,TOP); n+=1
    claimed=x.pop('payload_sha256'); assert claimed==hashlib.sha256(canonical(x)).hexdigest(); x['payload_sha256']=claimed; n+=1
    assert x['schema']=='hcs-c362-cucker-smale-evidence-v1' and x['candidate_id']=='HCS-C362' and x['obstruction_id']=='HEN-O346'; n+=3
    assert x['evaluation_date']=='2026-09-04' and x['source_commit']=='05ca5f96b2c69a6ad6ba153d1084df750d7722c0' and x['fixed_epoch']==1788480000 and x['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; n+=4
    keys(x['evaluator'],{'authority','version','sha256'}); assert x['evaluator']=={'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':'6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'}; n+=2
    keys(x['route_a_yaml'],{'relative_path','raw_sha256','semantic_sha256'}); assert x['route_a_yaml']=={'relative_path':'evaluations/route_a/HCS-C362/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM}; n+=2
    y=strict_yaml(yaml_path); assert hashlib.sha256(yaml_path.read_bytes()).hexdigest()==RAW and hashlib.sha256(canonical(y)).hexdigest()==SEM; n+=2
    ykeys={'schema','candidate_id','title','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator_authority','evaluator_version','evaluator_authority_sha256','obstruction_id','candidate_definition','family','phase_space','dynamics','parameters','parameter_provenance','arithmetic_origin','clock','normalization','determinant_convention','orbit_cutoff','precision','training_data','forbidden_data','artifact_paths','a0','a1','a2','a3','a4','tuple','overall_verdict','route_b_invocation_allowed','route_b_lock_reason','scope_flags','theorem_status','finite_evidence_role','source_owner_tokens'}
    keys(y,ykeys); assert y['candidate_id']=='HCS-C362' and y['obstruction_id']=='HEN-O346' and y['tuple']==ROUTE and y['overall_verdict']=='ROUTE_A_REJECTED' and y['route_b_invocation_allowed'] is False; n+=5
    gate_rows={
      'a0':('PROVED','the tail barrier and sharp scalar threshold are exact source-dynamical quantities','no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists'),
      'a1':('PROVED','the model has an intrinsic continuous-time flow and exact dissipation identities','flocking or escape trajectories do not form an isolated arithmetic primitive-periodic-orbit ledger'),
      'a2':('STOP_SCOPED','the communication primitive and two-body first integral are exact','neither is a dynamical zeta, Fredholm determinant, Euler product, or target divisor'),
      'a3':('STOP_SCOPED','all long-range, short-range, equality, and degenerate faces in the frozen theorem are analytic','there is no target continuation, functional equation, counting law, or Weil compression'),
      'a4':('STOP_SCOPED','frozen configurations carry symmetric graph Laplacians','the coevolving dissipative flow has no same-clock natural unitary, scattering, or Hamiltonian lift')}
    for a,(status,strong,fail) in gate_rows.items():
        keys(y[a],{'verdict','evidence_status','strongest_evidence','strongest_failure'}); assert y[a]=={'verdict':a.upper()+'_FAIL','evidence_status':status,'strongest_evidence':strong,'strongest_failure':fail}; n+=3
    assert y['evaluator_authority']=='flow_systems/skills/route-a-evaluator.md' and y['evaluator_version']=='0.2.0' and y['evaluator_authority_sha256']=='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'; n+=3
    assert y['normalization']=='complete ordered-pair sum with K/N and psi(r)=(1+r^2)^(-beta)' and y['theorem_status']=='PROVABLE_AS_STATED'; n+=2
    assert y['source_owner_tokens']==['DOI:10.1109/TAC.2007.895842','DOI:10.4310/CMS.2009.v7.n2.a2']; n+=1
    keys(x['scope_flags'],y['scope_flags']); assert x['scope_flags']==y['scope_flags'] and not any(x['scope_flags'].values()); n+=2
    keys(x['route_a'],{'tuple','overall','route_b_invocation_allowed'}); assert x['route_a']=={'tuple':ROUTE,'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}; n+=2
    model={'equations':'dot x_i=v_i; dot v_i=(K/N) sum_j psi(|x_j-x_i|)(v_j-v_i)','communication':'psi(r)=(1+r^2)^(-beta)','core_parameters':'N>=2,d>=1,K>0,beta>=0'}
    theorem={'global_flow':True,'mean_velocity_conserved':True,'ordered_variance_dissipation':'-K/N^2 sum_ij psi_ij |v_i-v_j|^2','diameter_comparison':['D+ X <= V','D+ V <= -K psi(X) V'],'conditional_gate':'V0 < K integral_X0^infinity psi','confinement':'K integral_X0^R psi=V0','alignment_rate':'K psi(R)','unconditional_chamber':'0<=beta<=1/2','many_body_gate_is_necessary':False,'two_body_sharpness':'outward scalar N=2 trichotomy below/equality/above for beta>1/2'}
    proof={'barrier':'V+K integral_X0^X psi is nonincreasing','primitive':'Phi_beta(r)=r*2F1(1/2,beta;3/2;-r^2)','tail_test':'integral at infinity diverges iff beta<=1/2','two_body_first_integral':'u(r)=u0-K integral_r0^r psi','equality_boundary':'u tends zero while r tends infinity','above_boundary':'u and r/t tend u0-A>0'}
    keys(x['model'],model); keys(x['theorem_contract'],theorem); keys(x['proof_receipts'],proof); assert x['model']==model and x['theorem_contract']==theorem and x['proof_receipts']==proof; n+=6
    assert x['finite_evidence_role']=='exact normalization and implementation receipt only; analytic proof owns arbitrary N and d'; n+=1
    assert x['collision_boundary']=={'C203':'fixed signed-Laplacian first-order consensus','C333':'randomized edge gossip second moments','C347':'noisy mean-field Kuramoto phases'}; n+=1
    assert x['boundary_atlas']=={'N=1':'diameters identically zero','K=0':'constant velocities; flocking iff V0=0','V0=0':'relative positions fixed','coincident_agents':'regular because psi(0)=1','beta=1/2':'unconditional endpoint','failed_many_body_gate':'no general non-flocking conclusion'}; n+=1
    assert x['references']==['10.1109/TAC.2007.895842','10.4310/CMS.2009.v7.n2.a2']; n+=1
    assert x['nonclaims']==['no necessity of the many-body sufficient gate','no singular kernel or collision-avoidance theorem','no delay, noise, or mean-field theorem','no priority claim','no target arithmetic, zero match, or Hilbert-Polya operator']; n+=1
    rowkeys={'label','N','d','K','beta','positions','velocities','mean_acceleration','energy_derivative','ordered_pair_rhs','position_diameter_squared','velocity_diameter_squared','active_velocity_pairs','diameter_squared_derivative_upper','diameter_squared_bound_upper'}
    expected_labels=[f'{q}-K{k}-b{b}' for q in ('two-line','three-line','four-line','three-plane') for k in ('1/2','1','2') for b in (0,1,2)]
    assert len(x['exact_system_rows'])==36 and [r['label'] for r in x['exact_system_rows']]==expected_labels; n+=2
    for r in x['exact_system_rows']:
        keys(r,rowkeys); ma,ed,rhs,X2,V2,active,upper,bound=recompute(r)
        assert list(map(frac,r['mean_acceleration']))==ma==[F(0)]*r['d']; assert frac(r['energy_derivative'])==ed==rhs==frac(r['ordered_pair_rhs']); n+=3
        assert frac(r['position_diameter_squared'])==X2 and frac(r['velocity_diameter_squared'])==V2 and r['active_velocity_pairs']==[[i,j] for i,j in active]; n+=3
        assert frac(r['diameter_squared_derivative_upper'])==upper and frac(r['diameter_squared_bound_upper'])==bound and upper<=bound; n+=3
    prim=[('0','r','infinity',True),('1/2','asinh(r)','infinity',True),('1','atan(r)','pi/2',False),('3/2','r/sqrt(1+r^2)','1',False),('2','atan(r)/2+r/(2*(1+r^2))','pi/4',False)]
    assert [(r['beta'],r['primitive'],r['total_tail_from_zero'],r['tail_diverges']) for r in x['primitive_rows']]==prim; n+=1
    two=[('3/2','1','0','1/2','below','1/sqrt(3)','0',True),('3/2','1','0','1','equality','infinity','0',False),('3/2','1','0','3/2','above','infinity','1/2',False)]
    assert [(r['beta'],r['K'],r['r0'],r['u0'],r['regime'],r['limit_distance'],r['limit_speed'],r['confined']) for r in x['two_body_rows']]==two; n+=1
    assert x['enumeration']=={'exact_system_rows':36,'primitive_rows':5,'two_body_rows':3,'exact_coordinate_cells':135}; n+=1
    return n
def main():
    if sys.flags.optimize: raise RuntimeError('C362 checker refuses optimized Python')
    print(f'C362 independent Cucker-Smale checker: PASS ({check()} assertions)')
if __name__=='__main__': main()
