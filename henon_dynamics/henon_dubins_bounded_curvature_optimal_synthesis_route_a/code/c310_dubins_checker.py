#!/usr/bin/env python3
"""Independent complete-cell checker for HCS-C310."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1];DEFAULT=ROOT/"results/c310_dubins_evidence.json";YEVAL=ROOT/"evaluations/route_a/HCS-C310/2026-09-03.yaml"
SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";TAU=2*math.pi
SPECS=[("identity","0","0","0","1"),("straight-forward","3","0","0","1"),("straight-scaled","6","0","0","2"),("straight-backward","-3","0","0","1"),("quarter-left","1","1","1/2","1"),("quarter-right","1","-1","-1/2","1"),("half-turn-near","0","2","1","1"),("half-turn-axis","-4","0","1","1"),("ccc-boundary","4","0","0","1"),("ccc-outside","5","0","0","1"),("lsl-owner","-4","-2","0","1"),("rsr-owner","-4","-4","1/2","1"),("lsr-owner","-4","0","1","1"),("rsl-owner","-4","-4","0","1"),("rlr-owner","-2","0","1","1"),("lrl-owner","-2","-2","-1/2","1"),("generic-a","2","3","1/3","1"),("generic-b","-1","3","-2/3","1"),("generic-c","7/2","-5/3","5/6","1"),("generic-d","-7/3","4/3","-1/6","1"),("small-pose","1/10","-1/5","1/4","1"),("large-radius","3","4","1/2","5/2"),("small-radius","3","4","-1/2","1/2"),("scaled-reflection","6","-4","-1/3","2"),("coincident-half","0","0","1","1"),("coincident-quarter","0","0","1/2","1"),("vertical-up","0","5","0","1"),("vertical-down","0","-5","0","1"),("heading-wrap-plus","2","1","7/3","1"),("heading-wrap-minus","2","-1","-7/3","1")]
def duplicate(pairs):
 out={}
 for k,v in pairs:
  if k in out:raise ValueError("duplicate JSON key")
  out[k]=v
 return out
def strict(path):
 value=json.loads(path.read_text(),object_pairs_hook=duplicate,parse_constant=lambda x:(_ for _ in ()).throw(ValueError("nonfinite JSON")))
 if type(value)is not dict:raise TypeError("JSON root must be object")
 return value
class U(yaml.SafeLoader):pass
U.yaml_implicit_resolvers={k:[(t,p) for t,p in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def um(loader,node,deep=False):
 out={}
 for kn,vn in node.value:
  if kn.tag=="tag:yaml.org,2002:merge":raise ValueError("YAML merge forbidden")
  k=loader.construct_object(kn,deep=deep)
  if type(k)is not str or k in out:raise ValueError("bad YAML key")
  out[k]=loader.construct_object(vn,deep=deep)
 return out
U.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,um)
def sy(path):
 raw=path.read_text()
 for token in yaml.scan(raw):
  if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML anchors/aliases forbidden")
 value=yaml.load(raw,Loader=U)
 if type(value)is not dict:raise TypeError("YAML root must be mapping")
 return value
def ph(data):
 body=dict(data);body.pop("payload_sha256",None);return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def mod(x):
 out=x%TAU
 return 0.0 if abs(out)<1e-12 or abs(out-TAU)<1e-12 else out
def atan2c(y,x):return 0.0 if abs(y)<1e-12 and abs(x)<1e-12 else math.atan2(y,x)
def solve(word,d,a,b):
 sa,sb,ca,cb=math.sin(a),math.sin(b),math.cos(a),math.cos(b);cab=math.cos(a-b);tol=1e-12
 if word=="LSL":
  z=2+d*d-2*cab+2*d*(sa-sb)
  if abs(z)<tol:z=0.0
  if z < -tol:return z,None
  p=math.sqrt(max(0,z));w=atan2c(cb-ca,d+sa-sb);return z,(mod(-a+w),p,mod(b-w))
 if word=="RSR":
  z=2+d*d-2*cab+2*d*(sb-sa)
  if abs(z)<tol:z=0.0
  if z < -tol:return z,None
  p=math.sqrt(max(0,z));w=atan2c(ca-cb,d-sa+sb);return z,(mod(a-w),p,mod(-b+w))
 if word=="LSR":
  z=-2+d*d+2*cab+2*d*(sa+sb)
  if abs(z)<tol:z=0.0
  if z < -tol:return z,None
  p=math.sqrt(max(0,z));w=math.atan2(-ca-cb,d+sa+sb)-math.atan2(-2,p);return z,(mod(-a+w),p,mod(-b+w))
 if word=="RSL":
  z=-2+d*d+2*cab-2*d*(sa+sb)
  if abs(z)<tol:z=0.0
  if z < -tol:return z,None
  p=math.sqrt(max(0,z));w=math.atan2(ca+cb,d-sa-sb)-math.atan2(2,p);return z,(mod(a-w),p,mod(b-w))
 if word=="RLR":
  z=(6-d*d+2*cab+2*d*(sa-sb))/8
  if abs(z-1)<tol:z=1.0
  if abs(z+1)<tol:z=-1.0
  if abs(z)>1+tol:return z,None
  m=mod(TAU-math.acos(max(-1,min(1,z))));t=mod(a-atan2c(ca-cb,d-sa+sb)+m/2);return z,(t,m,mod(a-b-t+m))
 z=(6-d*d+2*cab+2*d*(-sa+sb))/8
 if abs(z-1)<tol:z=1.0
 if abs(z+1)<tol:z=-1.0
 if abs(z)>1+tol:return z,None
 m=mod(TAU-math.acos(max(-1,min(1,z))));t=mod(-a-atan2c(ca-cb,d+sa-sb)+m/2);return z,(t,m,mod(b-a-t+m))
def step(pose,mode,length):
 x,y,h=pose
 if mode=="L":return x+math.sin(h+length)-math.sin(h),y-math.cos(h+length)+math.cos(h),h+length
 if mode=="R":return x+math.sin(h)-math.sin(h-length),y+math.cos(h-length)-math.cos(h),h-length
 return x+length*math.cos(h),y+length*math.sin(h),h
def near(text,value,tol=4e-14):
 if type(text)is not str or not math.isfinite(float(text)) or abs(float(text)-value)>tol*max(1,abs(value)):raise AssertionError(f"numeric mismatch {text} {value}")
def main():
 if sys.flags.optimize:raise RuntimeError("C310 checker refuses optimized Python")
 p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=DEFAULT);p.add_argument("--evaluation",type=Path,default=YEVAL);a=p.parse_args();data=strict(a.evidence);ev=sy(a.evaluation);checks=0
 if ph(data)!=data.get("payload_sha256"):raise AssertionError("payload hash")
 if (data.get("candidate_id"),data.get("obstruction_id"),data.get("source_commit"),data.get("scope_literal")) != ("HCS-C310","HEN-O294",SOURCE,SCOPE):raise AssertionError("identity")
 if data["route_a"]!={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}:raise AssertionError("route")
 if any(type(v)is not bool or v for v in data["scope_flags"].values()):raise AssertionError("scope")
 checks+=15
 if len(data["cases"])!=len(SPECS):raise AssertionError("case count")
 coverage={w:0 for w in ("LSL","RSR","LSR","RSL","RLR","LRL")};feasible_count=0
 for case,spec in zip(data["cases"],SPECS):
  cid,xs,ys,phis,rs=spec
  if case["case_id"]!=cid or case["target"]!={"x":xs,"y":ys,"heading_pi":phis,"radius":rs}:raise AssertionError("case identity")
  x=float(Fraction(xs));y=float(Fraction(ys));R=float(Fraction(rs));phi=float(Fraction(phis))*math.pi;xn,yn=x/R,y/R;d=math.hypot(xn,yn);theta=math.atan2(yn,xn) if d else 0.;alpha=mod(-theta);beta=mod(phi-theta)
  for text,value in zip((case["normalized"]["d"],case["normalized"]["alpha"],case["normalized"]["beta"]),(d,alpha,beta)):near(text,value)
  lengths=[]
  if [row["word"] for row in case["candidates"]]!=["LSL","RSR","LSR","RSL","RLR","LRL"]:raise AssertionError("word order")
  for row in case["candidates"]:
   test,segs=solve(row["word"],d,alpha,beta);near(row["feasibility_value"],test)
   if row["feasible"] is not (segs is not None):raise AssertionError("feasibility")
   if segs is None:
    if any(row[k] is not None for k in ("segments","normalized_length","physical_length","endpoint_residual")):raise AssertionError("infeasible payload")
    continue
   feasible_count+=1
   if len(row["segments"])!=3:raise AssertionError("segment count")
   for text,value in zip(row["segments"],segs):near(text,value)
   length=sum(segs);near(row["normalized_length"],length);near(row["physical_length"],R*length)
   pose=(0.,0.,0.)
   for mode,length_i in zip(row["word"],segs):pose=step(pose,mode,length_i)
   residual=math.sqrt((R*pose[0]-x)**2+(R*pose[1]-y)**2+math.atan2(math.sin(pose[2]-phi),math.cos(pose[2]-phi))**2)
   near(row["endpoint_residual"],residual,1e-12);lengths.append((row["word"],R*length));checks+=12
  minimum=min(v for _,v in lengths);near(case["minimum_length"],minimum);near(case["euclidean_lower_bound"],math.hypot(x,y))
  winners=[w for w,v in lengths if abs(v-minimum)<1e-10]
  if case["minimizers"]!=winners:raise AssertionError(f"winner mismatch {cid}")
  if minimum+1e-12<math.hypot(x,y):raise AssertionError("Euclidean lower bound")
  for w in winners:coverage[w]+=1
  checks+=8
 if data["word_coverage"]!=coverage or not all(coverage.values()):raise AssertionError("winner coverage")
 if data["enumeration"]!={"case_count":len(SPECS),"candidate_word_cells":6*len(SPECS),"feasible_word_cells":feasible_count,"audited_leaf_count":data["enumeration"]["audited_leaf_count"]}:raise AssertionError("enumeration")
 if (ev.get("candidate_id"),ev.get("obstruction_id"),ev.get("source_commit"),ev.get("scope_literal"),ev.get("tuple"),ev.get("overall_verdict"),ev.get("route_b_invocation_allowed")) != ("HCS-C310","HEN-O294",SOURCE,SCOPE,data["route_a"]["tuple"],"ROUTE_A_REJECTED",False):raise AssertionError("evaluation")
 if ev.get("scope_flags")!=data["scope_flags"] or ev.get("theorem_status")!="PROVABLE_AS_STATED":raise AssertionError("evaluation scope")
 checks+=20
 print(f"C310 independent checker: PASS ({checks} checks)")
if __name__=="__main__":main()
