#!/usr/bin/env python3
"""Independent contract checker for HCS-C356; shares no implementation code."""
from __future__ import annotations
import cmath, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]; EV=ROOT/'results/c356_qwz_evidence.json'; YML=ROOT/'evaluations/route_a/HCS-C356/2026-09-03.yaml'
RAW='65ca3b4edca93782ccf74b735a103dc1728c3f9ed33b74259c666a9becf1775c'; SEM='38b482ef987c719deda54769345e813b350a8103ba24e03277729292977a2b17'
TOP={'schema','candidate_id','obstruction_id','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator','route_a_yaml','model','theorem_contract','proof_receipts','finite_grid','collision_boundary','nonclaims','references','route_a','scope_flags','mass_rows','dirac_rows','lattice_gauge_rows','enumeration','payload_sha256'}
ROUTE=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_NATURAL_QUANTIZATION']
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
def strict_json(path):
    def uniq(pairs):
        d={}
        for k,v in pairs:
            if k in d: raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(path.read_text(),object_pairs_hook=uniq,parse_constant=lambda s:(_ for _ in()).throw(ValueError(s)))
def strict_yaml(path):
    raw=path.read_text()
    for t in yaml.scan(raw):
        if isinstance(t,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError('alias')
    z=yaml.load(raw,Loader=Loader)
    if type(z) is not dict: raise TypeError('root')
    return z
def keys(x,s):
    if type(x) is not dict or set(x)!=set(s): raise AssertionError(f'schema drift: {set(x) if type(x) is dict else type(x)}')
def frac(s): return Fraction(s)
def spinor(m,k,t):
    a,b,c=math.sin(k),math.sin(t),m+math.cos(k)+math.cos(t); q=math.sqrt(a*a+b*b+c*c)
    if q+c>1e-13:
        z=math.sqrt(2*q*(q+c)); return (-(a-1j*b)/z,(q+c)/z)
    z=math.sqrt(2*q*(q-c)); return ((q-c)/z,-(a+1j*b)/z)
def ip(x,y): return x[0].conjugate()*y[0]+x[1].conjugate()*y[1]
def lattice(m,n):
    v=[[spinor(m,2*math.pi*i/n,2*math.pi*j/n) for j in range(n)] for i in range(n)]; total=0.; low=1.
    for i in range(n):
      for j in range(n):
        q=[ip(v[i][j],v[(i+1)%n][j]),ip(v[(i+1)%n][j],v[(i+1)%n][(j+1)%n]),ip(v[(i+1)%n][(j+1)%n],v[i][(j+1)%n]),ip(v[i][(j+1)%n],v[i][j])]
        low=min(low,*(abs(a) for a in q)); total+=cmath.phase(math.prod(a/abs(a) for a in q))
    return total/(2*math.pi),low
def check(evidence=EV,yaml_path=YML):
    n=0; x=strict_json(evidence); keys(x,TOP); n+=1
    claimed=x.pop('payload_sha256'); assert claimed==hashlib.sha256(canonical(x)).hexdigest(); x['payload_sha256']=claimed; n+=1
    assert x['schema']=='hcs-c356-qwz-evidence-v1' and x['evaluation_date']=='2026-09-03'; n+=2
    assert x['candidate_id']=='HCS-C356' and x['obstruction_id']=='HEN-O340' and x['source_commit']=='140c8714b74de666d56f441ddfb712026955901a'; n+=3
    assert x['fixed_epoch']==1788393600 and x['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'; n+=2
    keys(x['evaluator'],{'authority','version','sha256'}); assert x['evaluator']=={'authority':'flow_systems/skills/route-a-evaluator.md','version':'0.2.0','sha256':'6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'}; n+=2
    keys(x['route_a_yaml'],{'relative_path','raw_sha256','semantic_sha256'}); n+=1
    assert x['route_a_yaml']['relative_path']=='evaluations/route_a/HCS-C356/2026-09-03.yaml'; n+=1
    y=strict_yaml(yaml_path); assert hashlib.sha256(yaml_path.read_bytes()).hexdigest()==RAW and hashlib.sha256(canonical(y)).hexdigest()==SEM; n+=2
    assert x['route_a_yaml']['raw_sha256']==RAW and x['route_a_yaml']['semantic_sha256']==SEM; n+=2
    expected_top={'schema','candidate_id','title','evaluation_date','source_commit','fixed_epoch','scope_literal','evaluator_authority','evaluator_version','evaluator_authority_sha256','obstruction_id','candidate_definition','family','phase_space','dynamics','parameters','parameter_provenance','arithmetic_origin','clock','normalization','determinant_convention','orbit_cutoff','precision','training_data','forbidden_data','artifact_paths','a0','a1','a2','a3','a4','tuple','overall_verdict','route_b_invocation_allowed','route_b_lock_reason','scope_flags','theorem_status','finite_evidence_role','source_owner_tokens'}
    keys(y,expected_top); assert y['candidate_id']=='HCS-C356' and y['tuple']==ROUTE and y['overall_verdict']=='ROUTE_A_REJECTED' and y['route_b_invocation_allowed'] is False; n+=4
    for a,status in [('a0','PROVED'),('a1','PROVED'),('a2','STOP_SCOPED'),('a3','STOP_SCOPED'),('a4','PROVED')]:
        keys(y[a],{'verdict','evidence_status','strongest_evidence','strongest_failure'}); assert y[a]['evidence_status']==status; n+=2
    keys(y['scope_flags'],x['scope_flags'].keys()); assert not any(y['scope_flags'].values()) and y['scope_flags']==x['scope_flags']; n+=2
    model={'hamiltonian':'sin(k)sigma_x+sin(tau)sigma_y+(m+cos(k)+cos(tau))sigma_z','orientation':'dk wedge dtau','lower_projector':'(I-dhat dot sigma)/2'}
    theorem={'spectrum':'plus/minus |d|','gapped_iff':'m not in {-2,0,2}','direct_gap':'2 min(|m+2|,|m|,|m-2|)','chern_convention':'(2*pi*i)^-1 integral Tr(P[dP,dP]) dk dtau','chern_mass_sum':'-1/2[sgn(m+2)-2sgn(m)+sgn(m-2)]','adiabatic_charge':'filled lower band and gapped adiabatic limit only','finite_speed_exact_quantization':False}
    proof={'norm_square':'m^2+2+2m(x+y)+2xy','curvature_numerator':'cos(k)+cos(tau)+m cos(k) cos(tau)','projector_trace':'-i/2 nhat dot (partial_k nhat cross partial_tau nhat)','north_pole_degree':'sum over four Dirac points of chirality times indicator(mass>0)','dirac_jump_rule':'increasing mass changes lower c1 by -chirality'}
    keys(x['model'],model); keys(x['theorem_contract'],theorem); keys(x['proof_receipts'],proof)
    assert x['model']==model and x['theorem_contract']==theorem and x['proof_receipts']==proof; n+=6
    keys(x['finite_grid'],{'role','mass_rows','dirac_rows','lattice_rows'}); keys(x['collision_boundary'],{'C318','C331','C337'}); keys(x['route_a'],{'tuple','overall','route_b_invocation_allowed'}); n+=3
    assert x['route_a']=={'tuple':ROUTE,'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}; n+=1
    assert x['collision_boundary']=={'C318':'finite SSH chain and edges, not a Bloch-torus Chern pump','C331':'Dirac-monopole sphere and magnetic spectrum, not this QWZ line bundle','C337':'kicked-rotor resonance, not adiabatic band transport'}; n+=1
    assert x['nonclaims']==['no exact finite-speed quantization','no edge theorem','no disorder or interaction theorem','no priority claim','no target arithmetic or zero match']; n+=1
    assert x['references']==['10.1103/PhysRevB.27.6083','10.1103/PhysRevB.74.085308']; n+=1
    mass_ledger=['-3','-2','-3/2','-1/2','0','1/2','3/2','2','3']
    assert [r['mass'] for r in x['mass_rows']]==mass_ledger; n+=1
    for r in x['mass_rows']:
        keys(r,{'mass','gapped','direct_gap','chern','corner_norm_squared'}); m=frac(r['mass']); corners=[(m+2)**2,m*m,m*m,(m-2)**2]
        assert list(map(frac,r['corner_norm_squared']))==corners; gap=2*min(map(abs,(m+2,m,m-2))); assert frac(r['direct_gap'])==gap and r['gapped']==(gap>0)
        want=None if m in (-2,0,2) else (0 if abs(m)>2 else (-1 if m<0 else 1)); assert r['chern']==want; n+=5
    expected=[(-2,['0','0'],1,-1),(0,['pi','0'],-1,1),(0,['0','pi'],-1,1),(2,['pi','pi'],1,-1)]
    assert len(x['dirac_rows'])==4
    for r,e in zip(x['dirac_rows'],expected): keys(r,{'mass','point','chirality','chern_jump'}); assert (r['mass'],r['point'],r['chirality'],r['chern_jump'])==e and r['chern_jump']==-r['chirality']; n+=3
    lattice_ledger=[(m,g) for m in (-3,-1,1,3) for g in (9,15,21)]
    assert [(r['m'],r['grid']) for r in x['lattice_gauge_rows']]==lattice_ledger; n+=1
    for r in x['lattice_gauge_rows']:
        keys(r,{'m','grid','chern_float','rounded','absolute_residual','minimum_link_modulus'}); val,low=lattice(r['m'],r['grid']); want=0 if abs(r['m'])>2 else (-1 if r['m']<0 else 1)
        assert r['rounded']==want and abs(float(r['chern_float'])-val)<5e-12 and float(r['absolute_residual'])<1e-10 and abs(float(r['minimum_link_modulus'])-low)<5e-12; n+=5
    assert x['finite_grid']=={'role':'regression only; analytic degree proof owns topology','mass_rows':9,'dirac_rows':4,'lattice_rows':12}; n+=1
    assert x['enumeration']=={'exact_assertions':70,'lattice_regressions':12}; n+=1
    return n
def main():
    if sys.flags.optimize: raise RuntimeError('C356 checker refuses optimized Python')
    print(f'C356 independent QWZ checker: PASS ({check()} assertions)')
if __name__=='__main__': main()
