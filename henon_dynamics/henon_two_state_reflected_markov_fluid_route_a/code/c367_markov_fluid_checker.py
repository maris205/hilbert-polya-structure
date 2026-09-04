#!/usr/bin/env python3
"""Independent exact checker for HCS-C367; never imports the producer."""
from __future__ import annotations
import hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EV=ROOT/'results/c367_markov_fluid_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C367/2026-09-04.yaml'
RAW='f2672e7cee3be37d6181bce68387adb23d82578c223914a574e05904a3648df6'; SEM='e6a6ad6f49505299d702a3d53ff5ffc2f4346ef6447e82dcda583d57f6da5552'
EVAL='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
ROUTE=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL']
TOP={'schema','candidate_id','obstruction_id','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator','route_a_yaml','model','theorem_contract','proof_receipts','finite_evidence_role','collision_boundary','boundary_principle','nonclaims','references','route_a','scope_flags','core_rows','zero_rate_atlas','enumeration','payload_sha256'}

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
    if type(x) is not dict or set(x)!=set(expected): raise AssertionError(f'schema drift: {set(x) if type(x) is dict else type(x)}')
def typed_equal(left,right):
    if type(left) is not type(right): return False
    if type(left) is dict:
        return set(left)==set(right) and all(typed_equal(left[k],right[k]) for k in left)
    if type(left) in (list,tuple):
        return len(left)==len(right) and all(typed_equal(a,b) for a,b in zip(left,right))
    return left==right
def fs(q):
    q=F(q); return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

ATLAS=[
  ('a>0,b>0','c>0,d>0',['{0,1}'],'core sign trichotomy','unique only when ac<bd'),
  ('a>0,b>0','c=0,d>0',['{0,1}'],'absorbing workload at zero','unique delta_0 tensor pi'),
  ('a>0,b>0','c>0,d=0',['{0,1}'],'linear escape at speed ac/(a+b)','none'),
  ('a>0,b>0','c=0,d=0',['{0,1}'],'frozen workload','all nu tensor pi'),
  ('a=0,b>0','d>0; c arbitrary',['{0}'],'absorb in off then drain','unique delta_(0,0)'),
  ('a=0,b>0','d=0; c arbitrary',['{0}'],'absorb in off then freeze','all nu tensor delta_0'),
  ('a>0,b=0','c>0; d arbitrary',['{1}'],'absorb in on then escape at speed c','none'),
  ('a>0,b=0','c=0; d arbitrary',['{1}'],'absorb in on then freeze','all nu tensor delta_1'),
  ('a=0,b=0','d>0,c>0',['{0}','{1}'],'off drains; on escapes','delta_(0,0) only'),
  ('a=0,b=0','d>0,c=0',['{0}','{1}'],'off drains; on frozen','convex mixtures of delta_(0,0) and nu tensor delta_1'),
  ('a=0,b=0','d=0,c>0',['{0}','{1}'],'off frozen; on escapes','all nu tensor delta_0'),
  ('a=0,b=0','d=0,c=0',['{0}','{1}'],'both classes frozen','all laws on workload times frozen environment')]

def expected_row(a,b,c,d):
    a,b,c,d=map(F,(a,b,c,d)); wall=a*c-b*d; regime='stable' if wall<0 else 'null' if wall==0 else 'transient'
    stable=None
    if wall<0:
        k=(b*d-a*c)/(c*d); atom=(b*d-a*c)/((a+b)*d); q0=a*c*k/((a+b)*d); q1=a*k/(a+b); plus=a*(c+d)/((a+b)*d)
        moments=[]
        for n in range(1,9):
            m0=q0*math.factorial(n)/k**(n+1); m1=q1*math.factorial(n)/k**(n+1)
            moments.append({'order':n,'state0':fs(m0),'state1':fs(m1),'total':fs(m0+m1)})
        stable={'kappa':fs(k),'boundary_atom':fs(atom),'density0_coefficient':fs(q0),'density1_coefficient':fs(q1),'positive_workload_mass':fs(plus),'zero_flux':'0','boundary_flux_residual':'0','environment_marginals':[fs(b/(a+b)),fs(a/(a+b))],'total_mass':'1','regulator_rate':fs((b*d-a*c)/(a+b)),'moments':moments}
    return {'a':fs(a),'b':fs(b),'c':fs(c),'d':fs(d),'wall_ac_minus_bd':fs(wall),'mean_drift':fs(wall/(a+b)),'cycle_increment_mean':fs(c/b-d/a),'regime':regime,'stable_receipt':stable}

def check(evidence=EV,yaml_path=YML):
    n=0; x=strict_json(evidence); keys(x,TOP); n+=1
    claimed=x.pop('payload_sha256'); assert claimed==hashlib.sha256(canonical(x)).hexdigest(); x['payload_sha256']=claimed; n+=1
    assert x['schema']=='hcs-c367-reflected-markov-fluid-evidence-v1' and x['candidate_id']=='HCS-C367' and x['obstruction_id']=='HEN-O351'; n+=3
    assert x['evaluation_date']=='2026-09-04' and x['source_commit']=='323ea43f6970544467f8a89f0ed9be0c7c39f896' and typed_equal(x['fixed_epoch'],1788480000) and x['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; n+=4
    assert typed_equal(x['evaluator'],{'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':EVAL}); n+=1
    assert typed_equal(x['route_a_yaml'],{'relative_path':'evaluations/route_a/HCS-C367/2026-09-04.yaml','raw_sha256':RAW,'semantic_sha256':SEM}); n+=1
    y=strict_yaml(yaml_path); assert hashlib.sha256(yaml_path.read_bytes()).hexdigest()==RAW and hashlib.sha256(canonical(y)).hexdigest()==SEM; n+=2
    ykeys={'schema','candidate_id','title','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator_authority','evaluator_version','evaluator_authority_sha256','obstruction_id','candidate_definition','family','phase_space','dynamics','parameters','parameter_provenance','arithmetic_origin','clock','normalization','determinant_convention','orbit_cutoff','precision','training_data','forbidden_data','artifact_paths','a0','a1','a2','a3','a4','tuple','overall_verdict','route_b_invocation_allowed','route_b_lock_reason','scope_flags','theorem_status','finite_evidence_role','source_owner_tokens'}
    keys(y,ykeys); n+=1
    assert y['schema']=='route-a-evaluation-v0.2.0' and y['candidate_id']=='HCS-C367' and y['obstruction_id']=='HEN-O351'; n+=3
    assert y['evaluation_date']=='2026-09-04' and y['source_commit']=='323ea43f6970544467f8a89f0ed9be0c7c39f896' and y['fixed_epoch']==1788480000 and y['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; n+=4
    assert y['evaluator_authority']=='flow_systems/skills/route-a-evaluator.md' and y['evaluator_version']=='0.2.0' and y['evaluator_authority_sha256']==EVAL; n+=3
    assert y['tuple']==ROUTE and y['overall_verdict']=='ROUTE_A_REJECTED' and y['route_b_invocation_allowed'] is False; n+=3
    gates={
      'a0':('A0_FAIL','PROVED','the mean-drift wall and stationary exponential rate are exact source-dynamical quantities','no rational-prime carrier, prime-power repetition, arithmetic weight, or logarithmic-prime clock exists'),
      'a1':('A1_FAIL','PROVED','the reflected PDMP and its embedded Lindley chain have an intrinsic continuous-time law','excursions do not form an isolated arithmetic primitive-periodic-orbit ledger'),
      'a2':('A2_FAIL','STOP_SCOPED','the two-state stationary transform is elementary and branch-safe','it is not a dynamical zeta, Fredholm determinant, Euler product, or target divisor'),
      'a3':('A3_FAIL','STOP_SCOPED','stable, null, transient, and zero-rate faces are closed analytically','there is no target continuation, functional equation, counting law, or Weil compression'),
      'a4':('A4_FAIL','STOP_SCOPED','the Markov additive generator is a natural dissipative operator for the source process','reflection and stochastic switching supply no same-clock natural unitary, scattering, or Hamiltonian lift')}
    for name,(v,s,e,f) in gates.items():
        keys(y[name],{'verdict','evidence_status','strongest_evidence','strongest_failure'}); assert typed_equal(y[name],{'verdict':v,'evidence_status':s,'strongest_evidence':e,'strongest_failure':f}); n+=2
    assert y['normalization']=='q01=a, q10=b, r0=-d, r1=c, and right-continuous minimal regulator at zero'; n+=1
    assert y['theorem_status']=='PROVABLE_AS_STATED' and y['finite_evidence_role']=='exact algebra and normalization regression, not proof by finite sampling'; n+=2
    assert y['source_owner_tokens']==['DOI:10.1002/j.1538-7305.1982.tb03089.x','DOI:10.1080/15326349508807330']; n+=1
    assert typed_equal(x['model'],{'environment':'q01=a, q10=b','fluid_slopes':'r0=-d, r1=c','reflection':'X=Y+sup_{s<=t}(-Y_s)^+','core_domain':'a,b,c,d>0'}); n+=1
    theorem={'mean_drift':'(ac-bd)/(a+b)','stable':'ac<bd: positive recurrent with unique invariant probability','critical':'ac=bd: null recurrent with no invariant probability','overload':'ac>bd: transient and X_t/t tends mean drift','embedded_chain':'W_(n+1)=max(0,W_n+c I_n-d O_n)','stable_rate':'kappa=(bd-ac)/(cd)','only_atom':'mass (bd-ac)/((a+b)d) at (0,0)','all_moments':'P(X>0)*n!/kappa^n','regulator_rate':'(bd-ac)/(a+b)=d times boundary atom'}
    proof={'environment_stationary':'pi=(b,a)/(a+b)','cycle_mean':'c/b-d/a','cycle_time_mean':'1/b+1/a','interior_zero_flux':'c f1=d f0','boundary_balance':'a p_*=d f0(0)','critical_engine':'zero-mean nondegenerate finite-variance Lindley chain is null recurrent'}
    assert typed_equal(x['theorem_contract'],theorem) and typed_equal(x['proof_receipts'],proof); n+=2
    assert x['finite_evidence_role']=='81 exact rational core panels and 12 boundary rows are regression receipts; analytic proof owns the continuum theorem'; n+=1
    assert typed_equal(x['collision_boundary'],{'C351':'open Jackson network with discrete queue lengths','C346':'deterministic two-dimensional oblique Skorokhod map, not a Markov-additive reflected fluid','C332':'deterministic Moreau play hysteresis'}); n+=1
    assert x['boundary_principle']=='classify each closed environmental class; do not assert global uniqueness on reducible faces'; n+=1
    assert typed_equal(x['references'],['10.1002/j.1538-7305.1982.tb03089.x','10.1080/15326349508807330']); n+=1
    assert typed_equal(x['nonclaims'],['no Brownian component or diffusion approximation','no many-state matrix-analytic extension','no finite-buffer or queueing-network product form','no priority claim','no target arithmetic, target zero match, or Hilbert-Polya operator']); n+=1
    assert typed_equal(x['route_a'],{'tuple':ROUTE,'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}); n+=1
    keys(x['scope_flags'],y['scope_flags']); assert typed_equal(x['scope_flags'],y['scope_flags']) and all(type(v) is bool and v is False for v in x['scope_flags'].values()); n+=2
    expected=[expected_row(a,b,c,d) for a in (1,2,3) for b in (1,2,3) for c in (1,2,3) for d in (1,2,3)]
    assert len(x['core_rows'])==81 and typed_equal(x['core_rows'],expected); n+=82
    stable=sum(r['regime']=='stable' for r in expected); null=sum(r['regime']=='null' for r in expected); transient=81-stable-null
    for row in x['core_rows']:
        if row['stable_receipt'] is None: continue
        a,b,c,d=map(F,(row[k] for k in ('a','b','c','d'))); q=row['stable_receipt']; k=F(q['kappa']); atom=F(q['boundary_atom']); q0=F(q['density0_coefficient']); q1=F(q['density1_coefficient'])
        assert c*q1==d*q0 and a*atom==d*q0 and atom+(q0+q1)/k==1; n+=3
        assert [F(z) for z in q['environment_marginals']]==[b/(a+b),a/(a+b)] and d*atom==F(q['regulator_rate']); n+=2
        for m in q['moments']:
            order=m['order']; assert 1<=order<=8 and F(m['total'])==F(q['positive_workload_mass'])*math.factorial(order)/k**order; n+=2
    for row in x['zero_rate_atlas']:
        keys(row,{'communication','drifts','closed_classes','classification','invariant_family'}); n+=1
    got=[(r['communication'],r['drifts'],r['closed_classes'],r['classification'],r['invariant_family']) for r in x['zero_rate_atlas']]
    assert typed_equal(got,ATLAS); n+=12
    assert typed_equal(x['enumeration'],{'core_rows':81,'stable_rows':stable,'null_rows':null,'transient_rows':transient,'zero_rate_rows':12,'moment_cells':8*stable}); n+=1
    return n

def main():
    if sys.flags.optimize: raise RuntimeError('C367 checker refuses optimized Python')
    print(f'C367 independent Markov-fluid checker: PASS ({check()} assertions)')
if __name__=='__main__': main()
