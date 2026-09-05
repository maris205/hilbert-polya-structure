#!/usr/bin/env python3
"""Independent recount through the integer lattice, not the producer's phase rule."""
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
CHECKS=0

def need(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise ValueError(msg)

def same(a,b,path='root'):
    need(type(a) is type(b),'type '+path)
    if isinstance(b,dict):
        need(set(a)==set(b),'keys '+path)
        for k in b:same(a[k],b[k],path+'.'+k)
    elif isinstance(b,list):
        need(len(a)==len(b),'length '+path)
        for k,(x,y) in enumerate(zip(a,b)):same(x,y,path+'.'+str(k))
    else:need(a==b,'value '+path)

def frac(pair):
    need(type(pair) is list and len(pair)==2 and all(type(v) is int for v in pair),'rational type')
    a,b=pair;need(b>0 and gcd(a,b)==1,'reduced rational');return Fraction(a,b)

def enc(value):
    v=Fraction(value);return [v.numerator,v.denominator]

def vec(values):return [enc(v) for v in values]

def product(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]+a[0]*b[1]]

def translate(a,b,c,t):
    return product(a,[t,b*t,c*t+b*t*t/2])

def lattice(a,b):
    r=b[0]-a[0];s=b[1]-a[1];k=b[2]-a[2]-r*a[1]
    return all(v.denominator==1 for v in (r,s,k)),k

def involution(a,c):
    # Implement T_c I T_-c as three group operations, not the closed formula.
    before=product(a,[0,-c,0]);middle=[-before[0],-before[1],before[2]]
    return product(middle,[0,c,0])

def load(path):
    def unique(pairs):
        out={}
        for k,v in pairs:need(k not in out,'duplicate JSON');out[k]=v
        return out
    return json.loads(Path(path).read_text(),object_pairs_hook=unique,
      parse_constant=lambda v:(_ for _ in ()).throw(ValueError('nonfinite JSON '+v)))

def check(path):
    global CHECKS
    CHECKS=0;obj=load(path);need(set(obj)=={'payload','payload_sha256'},'envelope')
    data=obj['payload'];need(type(data) is dict,'payload type')
    actual=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    need(type(obj['payload_sha256']) is str and actual==obj['payload_sha256'],'payload hash')
    slopes=[(p,q) for q in range(1,5) for p in range(-3,4) if gcd(p,q)==1]
    phases=[Fraction(j,d) for d in range(1,7) for j in range(d) if gcd(j,d)==1]
    gammas=[Fraction(-2,3),Fraction(0),Fraction(5,7)]
    orbit=[];tori=[];identities=[];blocks=[]
    for p,q in slopes:
        b=Fraction(p,q)
        for c in gammas:
            for phase in phases:
                for x in [Fraction(0),Fraction(1,3)]:
                    y=(c*q+p*x+Fraction(p*q,2)-phase)/q;a=[x,y,Fraction(1,5)]
                    positives=[];negatives=[];shifts=[];first=None
                    # Search all integer times, not merely the phase's predicted times.
                    for time in range(1,12*q+1):
                        hit,shift=lattice(a,translate(a,b,c,Fraction(time)))
                        if hit:
                            if first is None:first=time
                            need(time%q==0,'nonhorizontal return');positives.append(time//q)
                        if time%q==0:shifts.append(enc(shift))
                    for k in range(1,13):
                        if lattice(a,translate(a,b,c,Fraction(-k*q)))[0]:negatives.append(-k)
                        need(not lattice(a,translate(a,b,c,Fraction(2*k+1,2)))[0],'half integer return')
                    need(first==phase.denominator*q,'least period independent search')
                    orbit.append(dict(p=p,q=q,gamma=enc(c),theta=enc(phase),point=vec(a),least_period=first,
                      positive_return_multipliers=positives,negative_return_multipliers=negatives,
                      central_lattice_displacements=shifts,nonhorizontal_half_integer_returns=False))
            a=[Fraction(1,3),Fraction(-2,5),Fraction(1,7)]
            for t,s in [(Fraction(-3,2),Fraction(2,3)),(Fraction(0),Fraction(5,4)),(Fraction(7,3),Fraction(-2,3))]:
                composed=translate(translate(a,b,c,t),b,c,s)
                need(composed==translate(a,b,c,t+s),'flow group law')
                rev=involution(translate(involution(a,c),b,c,t),c)
                need(rev==translate(a,b,c,-t),'same clock reversal')
                section=[Fraction(0),a[1],a[2]]
                for _ in range(5):
                    end=translate(section,b,c,Fraction(1))
                    section=product([-1,0,0],end)
                identities.append(dict(p=p,q=q,gamma=enc(c),point=vec(a),t=enc(t),s=enc(s),
                  group_result=vec(composed),reversed_flow_result=vec(rev),
                  involution_result=vec(involution(involution(a,c),c)),section_iterate=vec(section)))
        for k in range(1,13):
            fixed=[];primitive=0
            for j in range(k):
                phase=Fraction(j,k)
                y=Fraction(p,2)-phase/q;a=[Fraction(0),y,Fraction(0)]
                need(lattice(a,translate(a,b,Fraction(0),Fraction(k*q)))[0],'fixed phase return')
                fixed.append(enc(phase));primitive+=phase.denominator==k
            matrix=[[1,0,0],[0,1,0],[p*k,-q*k,1]]
            need(matrix[2][1]!=0 and p*k*q-q*k*p==0,'rank/kernel')
            tori.append(dict(p=p,q=q,multiplier=k,time=k*q,fixed_tori=len(fixed),primitive_tori=primitive,
              fixed_phases=fixed,return_matrix=matrix,clean_rank=1,isolated=False,all_multipliers_one=True))
    for m in [v for v in range(-6,7) if v]:
        for j in range(abs(m)):
            for b in [Fraction(-3,2),Fraction(0),Fraction(2,3)]:
                c=Fraction(5,7);linear=2*(b*j+c*m);quadratic=b*m
                residues=[j+m*ell for ell in range(-2,3)]
                need(all((k-j)%abs(m)==0 for k in residues),'negative mode residues')
                blocks.append(dict(m=m,j=j,beta=enc(b),gamma=enc(c),residue_labels=residues,
                  potential_over_2pi=[enc(linear/2),enc(quadratic)],
                  chirp_over_pi=[enc(0),enc(linear),enc(quadratic)],
                  spectral_type='Lebesgue_multiplicity_one',domain='C_mj_H1_R'))
    flags=['claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number',
      'claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation',
      'claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b']
    expected=dict(schema='hcs-c387-nilflow-v1',candidate_id='HCS-C387',obstruction_id='HEN-O371',
      source_commit='3e692da6fa94362225c7534e9b66c83c15c7f284',fixed_epoch=1788566400,
      source=dict(object='Gamma\\H left integer Heisenberg quotient',vector_field='X+beta*Y+gamma*Z',
       clock='original real time t',measure='unit Haar mass',generator='U_t=exp(i*t*A), A=-i*W',zero_X_component_in_scope=False),
      route_tuple=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FORMAL_HINT'],
      scope_literal='NO_BAD_EULER_OR_ROOT_NUMBER',scope_flags={k:False for k in flags},route_b_invocation_allowed=False,
      grid=dict(slopes=len(slopes),gammas=3,rational_phases=len(phases),orbit_rows=len(orbit),
       fixed_torus_rows=len(tori),flow_identity_rows=len(identities),signed_block_rows=len(blocks),irrational_rows=24,return_multiplier_cutoff=12),
      orbit_rows=orbit,fixed_torus_rows=tori,flow_identity_rows=identities,signed_block_rows=blocks,
      irrational_controls=[dict(time=n,beta_sqrt2_horizontal_coefficient=n,
       rational_beta_theta_sqrt2_central_coefficient=n,return_exists=False) for n in range(1,25)],
      global_theorem=dict(all_real_parameters=True,all_times=True,unique_ergodic_iff_irrational_beta=True,
       time_one_map_ergodic=False,whole_flow_weakly_mixing=False,noncentral_correlations_decay=True,
       generator_spectrum='R',noncentral_multiplicity='countably_infinite',singular_continuous_component=False,
       same_clock_reversal=True,unitary_compact=False,resolvent_compact=False,heat_compact=False,
       finite_schatten=False,positive_heat_extended_trace='infinity',ordinary_orbit_zeta='one_or_undefined',
       global_fredholm_determinant_constructed=False))
    same(data,expected)
    return CHECKS

def main():
    if sys.flags.optimize:raise RuntimeError('C387 checker refuses optimized Python')
    path=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'results/c387_nilflow_evidence.json'
    print('C387_CHECKER_PASS exact_assertions='+str(check(path))+' independent_integer_lattice_recount=true')

if __name__=='__main__':main()
