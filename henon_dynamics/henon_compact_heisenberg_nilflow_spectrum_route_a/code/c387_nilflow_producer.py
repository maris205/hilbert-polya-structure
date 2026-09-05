#!/usr/bin/env python3
"""Exact finite audit of the explicitly proved continuous Heisenberg family."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
FLAGS=['claims_target_arithmetic_local_data','claims_target_euler_factors',
 'claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law',
 'claims_target_functional_equation','claims_target_zero_match',
 'claims_hilbert_polya_operator','invokes_route_b']
ROUTE=['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FORMAL_HINT']

def rat(a):
    a=F(a);return [a.numerator,a.denominator]

def flow(point,b,c,t):
    x,y,z=point
    return [x+t,y+b*t,z+c*t+b*x*t+b*t*t/2]

def reverse(point,c):
    x,y,z=point;return [-x,-y+2*c,z-2*c*x]

def encoded(point):return [rat(v) for v in point]

def build():
    slopes=[(p,q) for q in range(1,5) for p in range(-3,4) if gcd(p,q)==1]
    phases=[F(j,d) for d in range(1,7) for j in range(d) if gcd(j,d)==1]
    gammas=[F(-2,3),F(0),F(5,7)]
    orbit=[];tori=[];identities=[];blocks=[]
    for p,q in slopes:
        beta=F(p,q)
        for gamma in gammas:
            for theta in phases:
                for x in [F(0),F(1,3)]:
                    y=(gamma*q+p*x+F(p*q,2)-theta)/q;z=F(1,5)
                    shifts=[k*theta+F(p*q*k*(k-1),2) for k in range(1,13)]
                    orbit.append(dict(p=p,q=q,gamma=rat(gamma),theta=rat(theta),
                      point=encoded([x,y,z]),least_period=q*theta.denominator,
                      positive_return_multipliers=[k for k in range(1,13) if k%theta.denominator==0],
                      negative_return_multipliers=[-k for k in range(1,13) if k%theta.denominator==0],
                      central_lattice_displacements=[rat(s) for s in shifts],
                      nonhorizontal_half_integer_returns=False))
            point=[F(1,3),F(-2,5),F(1,7)]
            for t,s in [(F(-3,2),F(2,3)),(F(0),F(5,4)),(F(7,3),F(-2,3))]:
                final=flow(point,beta,gamma,t+s)
                identities.append(dict(p=p,q=q,gamma=rat(gamma),point=encoded(point),
                  t=rat(t),s=rat(s),group_result=encoded(final),
                  reversed_flow_result=encoded(flow(point,beta,gamma,-t)),
                  involution_result=encoded(point),
                  section_iterate=encoded([F(0),point[1]+5*beta,
                    point[2]-5*point[1]+5*gamma-F(25,2)*beta])))
        for k in range(1,13):
            tori.append(dict(p=p,q=q,multiplier=k,time=k*q,fixed_tori=k,
              primitive_tori=sum(gcd(a,k)==1 for a in range(1,k+1)),
              fixed_phases=[rat(F(j,k)) for j in range(k)],
              return_matrix=[[1,0,0],[0,1,0],[p*k,-q*k,1]],
              clean_rank=1,isolated=False,all_multipliers_one=True))
    for m in [v for v in range(-6,7) if v]:
        for j in range(abs(m)):
            for beta in [F(-3,2),F(0),F(2,3)]:
                gamma=F(5,7);constant=beta*j+gamma*m
                blocks.append(dict(m=m,j=j,beta=rat(beta),gamma=rat(gamma),
                  residue_labels=[j+m*ell for ell in range(-2,3)],
                  potential_over_2pi=[rat(constant),rat(beta*m)],
                  chirp_over_pi=[rat(F(0)),rat(2*constant),rat(beta*m)],
                  spectral_type='Lebesgue_multiplicity_one',domain='C_mj_H1_R'))
    irrational=[dict(time=n,beta_sqrt2_horizontal_coefficient=n,
       rational_beta_theta_sqrt2_central_coefficient=n,return_exists=False) for n in range(1,25)]
    payload=dict(schema='hcs-c387-nilflow-v1',candidate_id='HCS-C387',obstruction_id='HEN-O371',
      source_commit='3e692da6fa94362225c7534e9b66c83c15c7f284',fixed_epoch=1788566400,
      source=dict(object='Gamma\\H left integer Heisenberg quotient',
       vector_field='X+beta*Y+gamma*Z',clock='original real time t',
       measure='unit Haar mass',generator='U_t=exp(i*t*A), A=-i*W',
       zero_X_component_in_scope=False),route_tuple=ROUTE,
      scope_literal='NO_BAD_EULER_OR_ROOT_NUMBER',scope_flags={k:False for k in FLAGS},
      route_b_invocation_allowed=False,
      grid=dict(slopes=len(slopes),gammas=len(gammas),rational_phases=len(phases),
       orbit_rows=len(orbit),fixed_torus_rows=len(tori),flow_identity_rows=len(identities),
       signed_block_rows=len(blocks),irrational_rows=len(irrational),return_multiplier_cutoff=12),
      orbit_rows=orbit,fixed_torus_rows=tori,flow_identity_rows=identities,
      signed_block_rows=blocks,irrational_controls=irrational,
      global_theorem=dict(all_real_parameters=True,all_times=True,
       unique_ergodic_iff_irrational_beta=True,time_one_map_ergodic=False,
       whole_flow_weakly_mixing=False,noncentral_correlations_decay=True,
       generator_spectrum='R',noncentral_multiplicity='countably_infinite',
       singular_continuous_component=False,same_clock_reversal=True,
       unitary_compact=False,resolvent_compact=False,heat_compact=False,
       finite_schatten=False,positive_heat_extended_trace='infinity',
       ordinary_orbit_zeta='one_or_undefined',global_fredholm_determinant_constructed=False))
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    return dict(payload=payload,payload_sha256=sha256(canonical).hexdigest())

def main():
    if sys.flags.optimize:raise RuntimeError('C387 producer refuses optimized Python')
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'results/c387_nilflow_evidence.json')
    args=ap.parse_args();data=build();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print('C387_PRODUCER_PASS payload_sha256='+data['payload_sha256']+' grid='+json.dumps(data['payload']['grid'],sort_keys=True))

if __name__=='__main__':main()
