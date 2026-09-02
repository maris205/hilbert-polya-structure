#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C311."""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from fractions import Fraction
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1];E=ROOT/"results/c311_brusselator_evidence.json";Y=ROOT/"evaluations/route_a/HCS-C311/2026-09-03.yaml";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";AS=["1/4","1/3","1/2","2/3","1","3/2","2","3","4","5","7","10"]
def dup(xs):
 d={}
 for k,v in xs:
  if k in d:raise ValueError("duplicate JSON key")
  d[k]=v
 return d
def sj(p):
 v=json.loads(p.read_text(),object_pairs_hook=dup,parse_constant=lambda x:(_ for _ in()).throw(ValueError("nonfinite JSON")))
 if type(v)is not dict:raise TypeError("JSON root")
 return v
class U(yaml.SafeLoader):pass
U.yaml_implicit_resolvers={k:[(t,p) for t,p in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def um(l,n,deep=False):
 d={}
 for kn,vn in n.value:
  if kn.tag=="tag:yaml.org,2002:merge":raise ValueError("merge")
  k=l.construct_object(kn,deep=deep)
  if type(k)is not str or k in d:raise ValueError("YAML key")
  d[k]=l.construct_object(vn,deep=deep)
 return d
U.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,um)
def sy(p):
 raw=p.read_text()
 for t in yaml.scan(raw):
  if isinstance(t,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML aliases")
 v=yaml.load(raw,Loader=U)
 if type(v)is not dict:raise TypeError("YAML root")
 return v
def q(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def near(s,x):
 if type(s)is not str or not math.isfinite(float(s)) or abs(float(s)-x)>4e-14*max(1,abs(x)):raise AssertionError("decimal")
def main():
 if sys.flags.optimize:raise RuntimeError("C311 checker refuses optimized Python")
 p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=E);p.add_argument("--evaluation",type=Path,default=Y);o=p.parse_args();d=sj(o.evidence);ev=sy(o.evaluation);checks=0
 if ph(d)!=d.get("payload_sha256") or (d.get("candidate_id"),d.get("obstruction_id"),d.get("source_commit"),d.get("scope_literal")) != ("HCS-C311","HEN-O295",SOURCE,SCOPE):raise AssertionError("identity/hash")
 if d["route_a"]!={"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}:raise AssertionError("route")
 if any(type(v)is not bool or v for v in d["scope_flags"].values()):raise AssertionError("scope")
 if d["model"]!={"parameters":"A>0 and B>=0","dynamics":"xdot=A-(B+1)x+x^2 y, ydot=Bx-x^2 y","state_space":"closed nonnegative quadrant"}:raise AssertionError("model")
 checks+=18
 if len(d["parameter_rows"])!=len(AS):raise AssertionError("rows")
 probe_count=0
 for row,text in zip(d["parameter_rows"],AS):
  a=Fraction(text);a2=a*a;bc=1+a2;bs=(a-1)**2;bu=(a+1)**2;poly=4*a**4-7*a2+4
  if row["A"]!=text or row["hopf_B"]!=q(bc) or row["equilibrium"]!={"x":text,"y":q(bc/a)}:raise AssertionError("equilibrium")
  if row["jacobian"]!=[[q(a2),q(a2)],[q(-a2-1),q(-a2)]] or row["linear_boundaries"]!={"stable_defective_B":q(bs),"hopf_B":q(bc),"unstable_defective_B":q(bu)}:raise AssertionError("linear data")
  h=row["hopf_data"]
  expected={"omega":text,"transversality":"1/2","q":[{"real":"1","imag":"0"},{"real":"-1","imag":q(1/a)}],"p":[{"real":"1/2","imag":q(a/2)},{"real":"0","imag":q(a/2)}],"G21_real":q(-(a2+2)/a2),"G21_imag":q(-poly/(3*a**3)),"kuznetsov_l1":q(-(a2+2)/(2*a**3)),"physical_radial_cubic":q(-(a2+2)/(2*a2)),"radius_squared_per_mu":q(a2/(a2+2)),"x_first_harmonic_per_sqrt_mu":h["x_first_harmonic_per_sqrt_mu"],"frequency_shift_per_mu":q(-poly/(6*a*(a2+2)))}
  if h!=expected:raise AssertionError("Hopf exact data")
  near(h["x_first_harmonic_per_sqrt_mu"],2*float(a)/math.sqrt(float(a2+2)))
  for probe in row["linear_probes"]:
   B=Fraction(probe["B"]);trace=B-bc;disc=trace*trace-4*a2
   if probe["trace"]!=q(trace) or probe["discriminant"]!=q(disc):raise AssertionError("probe invariants")
   roots=[]
   if disc<0:roots=[(float(trace)/2,math.sqrt(float(-disc))/2),(float(trace)/2,-math.sqrt(float(-disc))/2)]
   else:roots=[(float(trace)/2+math.sqrt(float(disc))/2,0),(float(trace)/2-math.sqrt(float(disc))/2,0)]
   for got,(re,im) in zip(probe["eigenvalues"],roots):near(got["real"],re);near(got["imag"],im);checks+=4
   probe_count+=1
  checks+=22
 if d["enumeration"]["A_rows"]!=len(AS) or d["enumeration"]["linear_probe_rows"]!=probe_count:raise AssertionError("enumeration")
 if (ev.get("candidate_id"),ev.get("obstruction_id"),ev.get("source_commit"),ev.get("scope_literal"),ev.get("tuple"),ev.get("overall_verdict"),ev.get("route_b_invocation_allowed")) != ("HCS-C311","HEN-O295",SOURCE,SCOPE,d["route_a"]["tuple"],"ROUTE_A_REJECTED",False):raise AssertionError("evaluation")
 if ev.get("scope_flags")!=d["scope_flags"] or ev.get("theorem_status")!="PROVABLE_AS_STATED":raise AssertionError("evaluation scope")
 print(f"C311 independent checker: PASS ({checks+20} checks)")
if __name__=="__main__":main()
