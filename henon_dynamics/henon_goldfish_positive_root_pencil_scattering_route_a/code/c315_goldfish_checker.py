#!/usr/bin/env python3
"""Independent exact/Sturm/high-precision checker for HCS-C315."""
from __future__ import annotations
import argparse,hashlib,json,sys
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import sympy as sp
import yaml
ROOT=Path(__file__).resolve().parents[1];DEFAULT=ROOT/"results/c315_goldfish_evidence.json";DEFAULT_EVAL=ROOT/"evaluations/route_a/HCS-C315/2026-09-03.yaml";SOURCE="1938bae19e5a92f9ce2411aafdc68323bd641bd0";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EVALUATION_SEMANTIC_SHA256="6888df3b47857d102af6abdb00c3056a2711fb8705d030ac9aacdb30cc084698";EVALUATION_RAW_SHA256="dddc351e838b87f637b4fbebc2cba6cf48016667ef850c3a48478061a9cfdaa8";mp.mp.dps=100
SPECS=[("n2-basic",["0","1"],["1","2"]),("n2-skew",["-3/2","5/2"],["7/3","1/5"]),("n3-basic",["-2","0","3"],["1","2","4"]),("n3-fractions",["-5/3","-1/4","7/5"],["2/7","5/4","3/2"]),("n3-wide",["-7","1","9"],["5","1/3","2"]),("n4-basic",["-3","-1","2","5"],["1","3","2","4"]),("n4-fractions",["-11/4","-2/3","5/4","13/3"],["3/8","7/5","2/9","11/6"]),("n4-near",["0","1/5","2/5","1"],["1","2","3","4"]),("n5-basic",["-5","-2","0","3","8"],["2","1","4","3","5"]),("n5-fractions",["-7/2","-4/3","1/6","9/5","17/4"],["1/2","5/3","7/4","2/5","9/7"]),("n5-unit",["0","1","2","3","4"],["1","1","1","1","1"]),("n6-basic",["-6","-3","-1","2","5","9"],["1","2","3","4","5","6"]),("n6-zigzag",["-8","-5/2","-1/3","4/5","7/3","6"],["7/4","1/6","5/2","2/3","9/5","4"]),("n7-basic",["-9","-6","-3","-1","2","5","10"],["1","3","2","5","4","7","6"])]
TIMES=["-11","-3","-1/2","0","1/3","2","9"]
def pairs(items):
 o={}
 for k,v in items:
  if k in o:raise ValueError("duplicate JSON key")
  o[k]=v
 return o
def strict_json(p):
 v=json.loads(p.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in()).throw(ValueError("nonfinite JSON")))
 if type(v)is not dict:raise TypeError("JSON root")
 return v
class UL(yaml.SafeLoader):pass
UL.yaml_implicit_resolvers={k:[(t,p) for t,p in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def ym(loader,node,deep=False):
 o={}
 for kn,vn in node.value:
  if kn.tag=="tag:yaml.org,2002:merge":raise ValueError("merge")
  k=loader.construct_object(kn,deep=deep)
  if type(k)is not str or k in o:raise ValueError("YAML key")
  o[k]=loader.construct_object(vn,deep=deep)
 return o
UL.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,ym)
def strict_yaml(p):
 raw=p.read_text()
 for tok in yaml.scan(raw):
  if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML alias")
 v=yaml.load(raw,Loader=UL)
 if type(v)is not dict:raise TypeError("YAML root")
 return v
def digest(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def mul(a,b):
 o=[Fraction(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o
def add(a,b):
 n=max(len(a),len(b));a=[Fraction(0)]*(n-len(a))+a;b=[Fraction(0)]*(n-len(b))+b;return [x+y for x,y in zip(a,b)]
def polynomials(xs,vs):
 P=[Fraction(1)]
 for x in xs:P=mul(P,[Fraction(1),-x])
 Q=[Fraction(0)]*len(xs)
 for i,v in enumerate(vs):
  q=[Fraction(1)]
  for j,x in enumerate(xs):
   if i!=j:q=mul(q,[Fraction(1),-x])
  Q=add(Q,[v*c for c in q])
 return P,Q
def qs(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def mf(x):return mp.mpf(x.numerator)/x.denominator
def deriv(c):return [c[i]*Fraction(len(c)-1-i) for i in range(len(c)-1)]
def peval(c,z):
 a=mp.mpf(0)
 for q in c:a=a*z+mf(q)
 return a
def poly(c):
 z=sp.symbols("z");return sp.Poly(sum(sp.Rational(q.numerator,q.denominator)*z**(len(c)-1-i) for i,q in enumerate(c)),z)
def roots(c):return sorted(mp.mpf(str(sp.N(v,90))) for v in sp.nroots(poly(c),n=90,maxsteps=300))
def intervals(c):
 rows=poly(c).intervals(eps=sp.Rational(1,10**70))
 if any(m!=1 for _,m in rows) or len(rows)!=len(c)-1:raise AssertionError("non-simple/non-real")
 return [(mp.mpf(str(sp.N(a,90))),mp.mpf(str(sp.N(b,90)))) for (a,b),_ in rows]
def close(text,want,tol=mp.mpf("3e-69")):
 if type(text)is not str:raise AssertionError("decimal type")
 got=mp.mpf(text)
 if not mp.isfinite(got) or abs(got-want)>tol*max(1,abs(want)):raise AssertionError(f"decimal {got} != {want}")
def main():
 if sys.flags.optimize:raise RuntimeError("C315 checker refuses optimized Python")
 ap=argparse.ArgumentParser();ap.add_argument("--evidence",type=Path,default=DEFAULT);ap.add_argument("--evaluation",type=Path,default=DEFAULT_EVAL);a=ap.parse_args();d=strict_json(a.evidence);ev=strict_yaml(a.evaluation);checks=0
 if hashlib.sha256(json.dumps(ev,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()!=EVALUATION_SEMANTIC_SHA256:raise AssertionError("evaluation semantic digest mismatch")
 checks+=1
 if hashlib.sha256(a.evaluation.read_bytes()).hexdigest()!=EVALUATION_RAW_SHA256:raise AssertionError("evaluation raw-byte digest mismatch")
 checks+=1
 if digest(d)!=d.get("payload_sha256"):raise AssertionError("payload hash")
 expected_top={"schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal","evaluator","model","theorem_contract","cases","boundary_atlas","collision_boundary","route_a","scope_flags","nonclaims","references","enumeration","payload_sha256"}
 if set(d)!=expected_top:raise AssertionError("top keys")
 if (d["schema"],d["candidate_id"],d["obstruction_id"],d["source_commit"],d["fixed_epoch"],d["scope_literal"])!=("hcs-c315-positive-goldfish-v1","HCS-C315","HEN-O299",SOURCE,1788393600,SCOPE):raise AssertionError("identity")
 if d["evaluation_date"]!="2026-09-03" or d["evaluator"]!={"version":"0.2.0","sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}:raise AssertionError("date/evaluator")
 checks+=8
 model={"dynamics":"zddot_i=2 sum_{j!=i} zdot_i zdot_j/(z_i-z_j)","domain":"N>=2, x_1<...<x_N real, and every initial velocity v_i>0","linearization":"roots of p(z,t)=P(z)-tQ(z)","invariant":"Q(z)=sum_i zdot_i(t) product_{j!=i}(z-z_j(t)) is time independent"}
 theorem={"global":"the polynomial pencil is real rooted and simple for every real time, so the solution is complete and collision free","interlacing":"the moving roots have a strict signed-time interlacing with initial positions and invariant Q-roots","monotonicity":"every particle velocity stays strictly positive and their sum is constant","scattering":"one ballistic carrier transfers from the leftmost incoming rank to the rightmost outgoing rank while N-1 roots approach fixed interlacing anchors","asymptotics":"all finite roots and the ballistic root have explicit first inverse-time coefficients"}
 if d["model"]!=model or d["theorem_contract"]!=theorem:raise AssertionError("model/theorem")
 if d["route_a"]!={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}:raise AssertionError("route")
 if len(d["scope_flags"])!=9 or any(type(v)is not bool or v for v in d["scope_flags"].values()):raise AssertionError("scope")
 boundary=[{"face":"N=1","status":"free particle, listed only as a trivial boundary"},{"face":"one zero velocity","status":"global simplicity can fail; (x,v)=((0,1),(1,0)) collides at t=1"},{"face":"mixed velocity signs","status":"reality can fail; (x,v)=((0,1),(1,-1)) has a double root at t=1/4 and complex roots later"},{"face":"coincident initial positions","status":"excluded because the Newtonian vector field is singular"},{"face":"all negative velocities","status":"obtainable by time reversal but not merged into the positive-cone theorem"}]
 collision={"C196":"repulsive inverse-square Calogero--Moser uses a Hermitian eigenvalue pencil and N asymptotic free velocities; C315 uses a hyperbolic polynomial pencil and one-carrier scattering","C292":"sticky particles resolve physical mergers; C315 proves strict no-collision on a positive velocity cone","C296":"hard rods use event-driven elastic relabeling, not a smooth velocity-coupled root flow"}
 nonclaims=["Calogero retains ownership of the goldfish model and polynomial-root solution.","The positive-real interlacing closure is not presented as a literature-priority claim.","No canonical quantization, target determinant, target arithmetic data, Euler factors, root numbers, automorphy, target zero match, or Hilbert--Polya operator is asserted."]
 references=[{"doi":"10.1016/S0167-2789(01)00160-9","role":"standard goldfish model ownership"},{"handle":"11573/11324","role":"Calogero polynomial-zero dynamics lineage"},{"doi":"10.1088/0305-4470/37/47/008","role":"free-particle linearization context"}]
 if d["boundary_atlas"]!=boundary or d["collision_boundary"]!=collision or d["nonclaims"]!=nonclaims or d["references"]!=references:raise AssertionError("static boundary/source contract")
 checks+=18
 required={"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"}
 if set(ev)!=required:raise AssertionError("evaluation keys")
 if (ev["schema"],ev["candidate_id"],ev["obstruction_id"],ev["source_commit"],ev["fixed_epoch"],ev["scope_literal"])!=("route-a-evaluation-v0.2.0","HCS-C315","HEN-O299",SOURCE,1788393600,SCOPE):raise AssertionError("evaluation identity")
 if ev["tuple"]!=d["route_a"]["tuple"] or ev["overall_verdict"]!="ROUTE_A_REJECTED" or ev["route_b_invocation_allowed"] is not False or ev["scope_flags"]!=d["scope_flags"] or ev["theorem_status"]!="PROVABLE_AS_STATED":raise AssertionError("evaluation contract")
 for key,v in zip(("a0","a1","a2","a3","a4"),d["route_a"]["tuple"]):
  if ev[key].get("verdict")!=v:raise AssertionError("evaluation branch")
 checks+=22
 if [x["case_id"] for x in d["cases"]]!=[x[0] for x in SPECS]:raise AssertionError("case order")
 for row,(cid,xraw,vraw) in zip(d["cases"],SPECS):
  keys={"case_id","dimension","initial_positions","initial_velocities","P_coefficients","Q_coefficients","total_velocity","velocity_weighted_position","ballistic_intercept","anchor_roots","beta_coefficients","time_rows","asymptotic_rows"}
  if set(row)!=keys:raise AssertionError("case keys")
  xs=list(map(Fraction,xraw));vs=list(map(Fraction,vraw));n=len(xs);P,Q=polynomials(xs,vs);V=sum(vs,Fraction());M=sum((x*v for x,v in zip(xs,vs)),Fraction());c=M/V
  if row["dimension"]!=n or row["initial_positions"]!=xraw or row["initial_velocities"]!=vraw or row["P_coefficients"]!=list(map(qs,P)) or row["Q_coefficients"]!=list(map(qs,Q)) or (row["total_velocity"],row["velocity_weighted_position"],row["ballistic_intercept"])!=(qs(V),qs(M),qs(c)):raise AssertionError("exact coefficients")
  qint=intervals(Q);yr=roots(Q);qd=deriv(Q);betas=[-peval(P,y)/peval(qd,y) for y in yr]
  for i,(lo,hi) in enumerate(qint):
   if not (mf(xs[i])<lo<=hi<mf(xs[i+1])):raise AssertionError("anchor interlace")
   close(row["anchor_roots"][i],yr[i]);close(row["beta_coefficients"][i],betas[i])
   if betas[i]<=0:raise AssertionError("beta sign")
   checks+=4
  if [r["time"] for r in row["time_rows"]]!=TIMES:raise AssertionError("time order")
  for rec,traw in zip(row["time_rows"],TIMES):
   if set(rec)!={"time","roots","velocities","sum_roots","sum_velocities","max_ode_residual"}:raise AssertionError("time row keys")
   t=Fraction(traw);co=[p-t*q for p,q in zip(P,[Fraction()]+Q)];zr=roots(co);pint=intervals(co);dp=deriv(co);ddp=deriv(dp);vel=[peval(Q,z)/peval(dp,z) for z in zr]
   for got,want in zip(rec["roots"],zr):close(got,want)
   for got,want in zip(rec["velocities"],vel):close(got,want)
   if not all(v>0 for v in vel):raise AssertionError("positive velocities")
   close(rec["sum_roots"],sum(map(mf,xs))+mf(t)*mf(V));close(rec["sum_velocities"],mf(V));close(rec["max_ode_residual"],0,mp.mpf("2e-66"))
   if t>0:
    for i in range(n-1):
     if not (mf(xs[i])<pint[i][0]<=pint[i][1]<qint[i][0]):raise AssertionError("positive interlace")
    if not (pint[-1][0]>mf(xs[-1])):raise AssertionError("positive ballistic")
   elif t<0:
    if not (pint[0][1]<mf(xs[0])):raise AssertionError("negative ballistic")
    for i in range(n-1):
     if not (qint[i][1]<pint[i+1][0]<=pint[i+1][1]<mf(xs[i+1])):raise AssertionError("negative interlace")
   checks+=2*n+8
  for rec,sign in zip(row["asymptotic_rows"],(-1,1)):
   if set(rec)!={"time","finite_root_errors","ballistic_root_error","ballistic_velocity_limit","ballistic_intercept"}:raise AssertionError("asymptotic keys")
   t=Fraction(sign*1000000);co=[p-t*q for p,q in zip(P,[Fraction()]+Q)];zr=roots(co);tv=mf(t);finite=zr[1:] if sign<0 else zr[:-1];pred=[y-b/tv for y,b in zip(yr,betas)];ball=zr[0] if sign<0 else zr[-1];bpred=mf(V)*tv+mf(c)+sum(betas)/tv
   if rec["time"]!=qs(t) or rec["ballistic_velocity_limit"]!=qs(V) or rec["ballistic_intercept"]!=qs(c):raise AssertionError("asym exact")
   for got,want in zip(rec["finite_root_errors"],[z-p for z,p in zip(finite,pred)]):close(got,want)
   close(rec["ballistic_root_error"],ball-bpred);checks+=n+3
 enum=d["enumeration"]
 wants=(len(SPECS),len(SPECS)*len(TIMES),sum(len(x[1])*len(TIMES) for x in SPECS),sum(len(x[1])-1 for x in SPECS),2*len(SPECS))
 if (enum["case_count"],enum["time_rows"],enum["root_time_cells"],enum["anchor_cells"],enum["asymptotic_rows"])!=wants:raise AssertionError("enumeration")
 if set(enum)!={"case_count","time_rows","root_time_cells","anchor_cells","asymptotic_rows","audited_leaf_count"}:raise AssertionError("enumeration keys")
 body=dict(d);body.pop("payload_sha256")
 if enum["audited_leaf_count"]!=leaves(body):raise AssertionError("audited leaf count")
 checks+=5
 print(f"C315 independent checker: PASS ({checks} checks)")
if __name__=="__main__":main()
