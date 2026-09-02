#!/usr/bin/env python3
"""Producer-independent orbit and spectral checker for HCS-C313."""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from fractions import Fraction
from pathlib import Path
import mpmath as mp,yaml
R0=Path(__file__).resolve().parents[1];E=R0/"results/c313_sphere_evidence.json";Y=R0/"evaluations/route_a/HCS-C313/2026-09-03.yaml";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";mp.mp.dps=80
def dup(xs):
 d={}
 for k,v in xs:
  if k in d:raise ValueError("duplicate JSON")
  d[k]=v
 return d
def sj(p):
 v=json.loads(p.read_text(),object_pairs_hook=dup,parse_constant=lambda x:(_ for _ in()).throw(ValueError("nonfinite")))
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
  if isinstance(t,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("aliases")
 v=yaml.load(raw,Loader=U)
 if type(v)is not dict:raise TypeError("YAML root")
 return v
def q(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def radius(d):return (Fraction(1),Fraction(3,2),Fraction(2))[d%3]
def mult(d,l):return (2*l+d-1)*math.factorial(l+d-2)//(math.factorial(l)*math.factorial(d-1))
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def near(s,x,tol=3e-68):
 if type(s)is not str or abs(mp.mpf(s)-x)>tol*max(mp.mpf(1),abs(x)):raise AssertionError(f"decimal {s} {x}")
def main():
 if sys.flags.optimize:raise RuntimeError("C313 checker refuses optimized Python")
 p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=E);p.add_argument("--evaluation",type=Path,default=Y);a=p.parse_args();d=sj(a.evidence);ev=sy(a.evaluation);checks=0
 if ph(d)!=d.get("payload_sha256") or (d.get("candidate_id"),d.get("obstruction_id"),d.get("source_commit"),d.get("scope_literal")) != ("HCS-C313","HEN-O297",SOURCE,SCOPE):raise AssertionError("identity")
 if d["route_a"]!={"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False} or any(type(v)is not bool or v for v in d["scope_flags"].values()):raise AssertionError("route/scope")
 checks+=18;cells=heats=0
 if [x["dimension"] for x in d["dimension_rows"]]!=list(range(2,13)):raise AssertionError("dimensions")
 for row in d["dimension_rows"]:
  dim=row["dimension"];R=radius(dim)
  if (row["radius"],row["phase_dimension"],row["oriented_grassmann_dimension"],row["primitive_period_over_pi"],row["period_phase"]) != (q(R),2*dim-1,2*dim-2,q(2*R),1 if (dim-1)%2==0 else -1):raise AssertionError("geometry row")
  cum=0
  for l,spec in enumerate(row["spectral_rows"]):
   m=mult(dim,l);cum+=m;lam=Fraction(l*(l+dim-1),1)/(R*R);freq=Fraction(2*l+dim-1,2)/R
   if spec!={"ell":l,"laplace_eigenvalue":q(lam),"multiplicity":m,"cumulative_multiplicity":cum,"shifted_frequency":q(freq)}:raise AssertionError("spectral cell")
   if cum!=math.comb(l+dim,dim)+(math.comb(l+dim-1,dim) if l+dim-1>=dim else 0):raise AssertionError("cumulative identity")
   cells+=1;checks+=6
  for h in row["heat_partial_sums"]:
   t=Fraction(h["time"]);total=sum(mp.mpf(x["multiplicity"])*mp.exp(-mp.mpf(Fraction(x["laplace_eigenvalue"]).numerator)/Fraction(x["laplace_eigenvalue"]).denominator*mp.mpf(t.numerator)/t.denominator) for x in row["spectral_rows"])
   if h["ell_cutoff"]!=40:raise AssertionError("cutoff")
   near(h["partial_trace"],total);heats+=1;checks+=2
 for probe in d["geodesic_probes"]:
  dim=probe["dimension"];R=Fraction(probe["radius"]);r=mp.mpf(R.numerator)/R.denominator;t=mp.mpf(Fraction(probe["time_over_pi_R"]).numerator)/Fraction(probe["time_over_pi_R"]).denominator*mp.pi;c,s=mp.cos(t),mp.sin(t);x=[mp.mpf(0)]*(dim+1);v=[mp.mpf(0)]*(dim+1)
  if probe["frame"]=="coordinate":x[0]=r;v[1]=1
  else:x[0]=3*r/5;x[1]=4*r/5;v[0]=-mp.mpf(4)/5;v[1]=mp.mpf(3)/5
  xx=[c*x[i]+r*s*v[i] for i in range(dim+1)];vv=[-s*x[i]/r+c*v[i] for i in range(dim+1)]
  for got,want in zip(probe["x"],xx):near(got,want)
  for got,want in zip(probe["v"],vv):near(got,want)
  near(probe["sphere_residual"],sum(z*z for z in xx)-r*r);near(probe["speed_residual"],sum(z*z for z in vv)-1);near(probe["tangency_residual"],sum(xx[i]*vv[i] for i in range(dim+1)));checks+=2*dim+5
 en=d["enumeration"]
 if en["dimension_rows"]!=11 or en["spectral_cells"]!=cells or en["geodesic_probes"]!=len(d["geodesic_probes"]) or en["heat_partial_rows"]!=heats:raise AssertionError("enumeration")
 if (ev.get("candidate_id"),ev.get("obstruction_id"),ev.get("source_commit"),ev.get("scope_literal"),ev.get("tuple"),ev.get("overall_verdict"),ev.get("route_b_invocation_allowed")) != ("HCS-C313","HEN-O297",SOURCE,SCOPE,d["route_a"]["tuple"],"ROUTE_A_REJECTED",False):raise AssertionError("evaluation")
 if ev.get("scope_flags")!=d["scope_flags"] or ev.get("theorem_status")!="PROVABLE_AS_STATED":raise AssertionError("evaluation scope")
 print(f"C313 independent checker: PASS ({checks+20} checks)")
if __name__=="__main__":main()
