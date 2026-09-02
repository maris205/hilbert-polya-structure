#!/usr/bin/env python3
"""Exact orbit-family and Laplace receipts for round spheres."""
from __future__ import annotations
import argparse,hashlib,json,math
from fractions import Fraction
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];OUTPUT=ROOT/"results/c313_sphere_evidence.json";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788393600;mp.mp.dps=90
FLAGS={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,"claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,"claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}
def q(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def mpf(x):return mp.mpf(x.numerator)/x.denominator
def dec(x):return "0.0" if abs(x)<mp.mpf("1e-78") else mp.nstr(x,72,strip_zeros=False)
def mult(d,l):return (2*l+d-1)*math.factorial(l+d-2)//(math.factorial(l)*math.factorial(d-1))
def radius(d):return (Fraction(1),Fraction(3,2),Fraction(2))[d%3]
def spectral_dimension(d):
 R=radius(d);rows=[];cum=0
 for l in range(41):
  m=mult(d,l);cum+=m;lam=Fraction(l*(l+d-1),1)/(R*R);shift=Fraction(2*l+d-1,2)/R
  rows.append({"ell":l,"laplace_eigenvalue":q(lam),"multiplicity":m,"cumulative_multiplicity":cum,"shifted_frequency":q(shift)})
 heat=[]
 for tt in (Fraction(1,10),Fraction(1),Fraction(10)):
  total=sum(mp.mpf(row["multiplicity"])*mp.exp(-mpf(Fraction(row["laplace_eigenvalue"]))*mpf(tt)) for row in rows)
  heat.append({"time":q(tt),"ell_cutoff":40,"partial_trace":dec(total)})
 return {"dimension":d,"radius":q(R),"phase_dimension":2*d-1,"oriented_grassmann_dimension":2*d-2,"primitive_period_over_pi":q(2*R),"period_phase":1 if (d-1)%2==0 else -1,"spectral_rows":rows,"heat_partial_sums":heat}
def geodesic_probe(d,R,time_pi,tilted):
 n=d+1;r=mpf(R);tau=mpf(time_pi)*mp.pi;t=tau*r
 x=[mp.mpf("0")]*n;v=[mp.mpf("0")]*n
 if tilted:x[0]=r*mp.mpf(3)/5;x[1]=r*mp.mpf(4)/5;v[0]=-mp.mpf(4)/5;v[1]=mp.mpf(3)/5
 else:x[0]=r;v[1]=1
 c,s=mp.cos(t/r),mp.sin(t/r);xt=[c*x[i]+r*s*v[i] for i in range(n)];vt=[-s*x[i]/r+c*v[i] for i in range(n)]
 dot=lambda a,b:sum(a[i]*b[i] for i in range(n))
 return {"dimension":d,"radius":q(R),"time_over_pi_R":q(time_pi),"frame":"tilted-3-4-5" if tilted else "coordinate","x":[dec(z) for z in xt],"v":[dec(z) for z in vt],"sphere_residual":dec(dot(xt,xt)-r*r),"speed_residual":dec(dot(vt,vt)-1),"tangency_residual":dec(dot(xt,vt))}
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def main():
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=OUTPUT);a=p.parse_args();dims=[spectral_dimension(d) for d in range(2,13)];probes=[]
 for d in (2,3,4,7,12):
  R=radius(d)
  for t in (Fraction(0),Fraction(1,6),Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2)):probes.append(geodesic_probe(d,R,t,(d+int(6*t))%2==0))
 data={"schema":"hcs-c313-round-sphere-geodesic-laplace-v1","candidate_id":"HCS-C313","obstruction_id":"HEN-O297","evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,"evaluator":{"version":"0.2.0","sha256":EVALUATOR},"model":{"manifold":"round sphere S_R^d with d>=2 and R>0","phase_space":"unit tangent bundle T^1 S_R^d","dynamics":"unit-speed geodesic flow","quantization":"nonnegative Laplace--Beltrami operator and its completed-square half-wave"},"theorem_contract":{"flow":"Phi_t(x,v)=(cos(t/R)x+R sin(t/R)v,-sin(t/R)x/R+cos(t/R)v)","orbits":"every orbit has least period 2pi R and is a fiber over an oriented two-plane","clean_return":"Fix(Phi_t) is the whole phase space for t in 2pi R Z and empty otherwise; the return differential is identity","spectrum":"lambda_l=l(l+d-1)/R^2 with the full spherical-harmonic multiplicity","revival":"Q=sqrt(-Delta+(d-1)^2/(4R^2)) satisfies exp(-i2pi R Q)=(-1)^(d-1)I and exp(-i4pi R Q)=I","heat":"the positive-time heat operator is trace class with the exact spectral series"},"dimension_rows":dims,"geodesic_probes":probes,"collision_boundary":{"C242":"C242 studies an irrational ellipsoid Reeb flow with two isolated coordinate orbits; C313 has a maximally clean continuum of great circles.","C275":"C275 is an elliptic billiard with boundary reflection and caustics, not a boundaryless round geodesic flow.","C281":"C281 evolves product-sphere metrics by Ricci flow; C313 fixes one round metric and studies its geodesic/Laplace dynamics."},"route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"scope_flags":FLAGS,"nonclaims":["The continuum of great circles is not an isolated primitive-orbit ledger.","The Laplacian and shifted half-wave are natural source quantizations, not Hilbert--Polya operators or target-zero matches.","No target arithmetic datum, Euler factor, root number, automorphy, divisor law, or functional equation is asserted."],"references":[{"identifier":"10.5802/aif.2339","role":"periodic-geodesic and Laplace-spectrum lineage"}]}
 data["enumeration"]={"dimension_rows":len(dims),"spectral_cells":sum(len(x["spectral_rows"]) for x in dims),"geodesic_probes":len(probes),"heat_partial_rows":sum(len(x["heat_partial_sums"]) for x in dims)};data["enumeration"]["audited_leaf_count"]=leaves(data)+1;data["payload_sha256"]=ph(data);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C313_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")
if __name__=="__main__":main()
