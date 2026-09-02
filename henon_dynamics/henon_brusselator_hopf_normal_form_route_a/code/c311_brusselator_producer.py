#!/usr/bin/env python3
"""Exact Hopf and linear-chamber receipts for HCS-C311."""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];OUTPUT=ROOT/"results/c311_brusselator_evidence.json";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788393600;mp.mp.dps=90
AS=["1/4","1/3","1/2","2/3","1","3/2","2","3","4","5","7","10"]
FLAGS={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,"claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,"claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}
def qs(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def dec(x):return mp.nstr(x,72,strip_zeros=False) if x else "0.0"
def mpf(x):return mp.mpf(x.numerator)/x.denominator
def row(text):
 a=Fraction(text);a2=a*a;bc=1+a2;bs=(a-1)*(a-1);bu=(a+1)*(a+1);poly=4*a**4-7*a2+4
 re_g=-(a2+2)/a2;im_g=-poly/(3*a**3);l1=-(a2+2)/(2*a**3);radial=-(a2+2)/(2*a2);r2=a2/(a2+2);freq=-poly/(6*a*(a2+2))
 probes=[]
 for label,trace in (("stable-node",-3*a),("stable-focus",-a),("hopf",Fraction(0)),("unstable-focus",a),("unstable-node",3*a)):
  B=bc+trace;disc=trace*trace-4*a2
  if B<0:continue
  root=mp.sqrt(mpf(abs(disc)))/2
  if disc<0:eigs=[{"real":dec(mpf(trace)/2),"imag":dec(root)},{"real":dec(mpf(trace)/2),"imag":dec(-root)}]
  else:eigs=[{"real":dec(mpf(trace)/2+root),"imag":"0.0"},{"real":dec(mpf(trace)/2-root),"imag":"0.0"}]
  probes.append({"label":label,"B":qs(B),"trace":qs(trace),"discriminant":qs(disc),"eigenvalues":eigs})
 return {"A":text,"hopf_B":qs(bc),"equilibrium":{"x":text,"y":qs(bc/a)},"jacobian":[[qs(a2),qs(a2)],[qs(-a2-1),qs(-a2)]],"linear_boundaries":{"stable_defective_B":qs(bs),"hopf_B":qs(bc),"unstable_defective_B":qs(bu)},"hopf_data":{"omega":text,"transversality":"1/2","q":[{"real":"1","imag":"0"},{"real":"-1","imag":qs(1/a)}],"p":[{"real":"1/2","imag":qs(a/2)},{"real":"0","imag":qs(a/2)}],"G21_real":qs(re_g),"G21_imag":qs(im_g),"kuznetsov_l1":qs(l1),"physical_radial_cubic":qs(radial),"radius_squared_per_mu":qs(r2),"x_first_harmonic_per_sqrt_mu":dec(2*mpf(a)/mp.sqrt(mpf(a2+2))),"frequency_shift_per_mu":qs(freq)},"linear_probes":probes}
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def main():
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=OUTPUT);a=p.parse_args();rows=[row(x) for x in AS]
 d={"schema":"hcs-c311-brusselator-hopf-v1","candidate_id":"HCS-C311","obstruction_id":"HEN-O295","evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,"evaluator":{"version":"0.2.0","sha256":EVALUATOR},"model":{"parameters":"A>0 and B>=0","dynamics":"xdot=A-(B+1)x+x^2 y, ydot=Bx-x^2 y","state_space":"closed nonnegative quadrant"},"theorem_contract":{"global_existence":"the quadrant is invariant and x+y<=x0+y0+At","equilibrium":"the unique nonnegative equilibrium is (A,B/A)","linear_atlas":"stable node, defective node, stable focus, Hopf, unstable focus, defective node, and unstable node boundaries are exact","hopf":"B=1+A^2, omega=A, real-part transversality 1/2","normal_form":"with the declared q,p normalization, G21 and the first Lyapunov coefficient are exact for all A>0","cycle":"the Hopf is supercritical and creates a stable local cycle for mu=B-(1+A^2)>0 with explicit leading radius and frequency"},"parameter_rows":rows,"singular_faces":[{"face":"B=0","statement":"the equilibrium lies on y=0 and is linearly stable; at A=1 it is the stable defective-node boundary"},{"face":"A=0","statement":"excluded from the Hopf theorem; the equilibrium formula B/A is singular and x=0 becomes an equilibrium line"}],"collision_boundary":{"C249":"C249 proves the Van der Pol Lienard cycle globally; C311 derives the Brusselator chemical Hopf coefficient and complete local chamber atlas.","C235":"C235 treats replicator dynamics on a simplex with uniform mutation, not autocatalytic planar kinetics.","C254":"C254 treats a chemostat washout/transcritical system, not the Brusselator Hopf normal form."},"route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"scope_flags":FLAGS,"nonclaims":["Only the local Hopf cycle is classified; no global uniqueness of periodic orbits is claimed.","The isolated local limit cycle is source chemical dynamics, not an arithmetic primitive owner.","No target arithmetic datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted."],"references":[{"identifier":"10.1063/1.1668896","role":"Prigogine--Lefever Brusselator lineage"},{"identifier":"10.1007/978-1-4757-3978-7","role":"Hopf normal-form convention and formula lineage"}]}
 d["enumeration"]={"A_rows":len(rows),"linear_probe_rows":sum(len(r["linear_probes"]) for r in rows)};d["enumeration"]["audited_leaf_count"]=leaves(d)+1;d["payload_sha256"]=ph(d);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C311_PRODUCER_PASS {d['payload_sha256']} {d['enumeration']['audited_leaf_count']}")
if __name__=="__main__":main()
