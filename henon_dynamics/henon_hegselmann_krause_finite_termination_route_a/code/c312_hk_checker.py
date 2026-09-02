#!/usr/bin/env python3
"""Producer-independent exhaustive rational checker for HCS-C312."""
from __future__ import annotations
import argparse,hashlib,itertools,json,sys
from fractions import Fraction
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1];E=R/"results/c312_hk_evidence.json";Y=R/"evaluations/route_a/HCS-C312/2026-09-03.yaml";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";GRID=[Fraction(k,2) for k in range(7)];NAMED=[("threshold-pair","1",["0","1"]),("separated-pair","1",["0","3/2"]),("mean-counterexample","1",["0","1/2","7/5"]),("unit-chain-five","1",["0","1","2","3","4"]),("duplicate-chain","1",["0","0","1","2","2"]),("negative-cloud","1",["-3/2","-1","0","1/2"]),("scaled-chain","2",["0","2","4","6"]),("third-radius","1/3",["-1/3","0","1/3","2/3"]),("two-components","1",["0","1/2","3","7/2","4"]),("all-equal","5/7",["2","2","2","2"])]
def q(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def specs():
 out=list(NAMED)
 for n in range(1,6):
  for k,v in enumerate(itertools.combinations_with_replacement(GRID,n)):out.append((f"grid-n{n}-{k:04d}","1",[q(x) for x in v]))
 return out
def dup(xs):
 d={}
 for k,v in xs:
  if k in d:raise ValueError("duplicate JSON key")
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
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def upd(s,e):return tuple(sum((s[j] for j in range(len(s)) if abs(s[j]-s[i])<=e),Fraction(0))/sum(abs(s[j]-s[i])<=e for j in range(len(s))) for i in range(len(s)))
def comps(s,e):
 o=[];z=0
 for i in range(len(s)-1):
  if s[i+1]-s[i]>e:o.append([z,i]);z=i+1
 o.append([z,len(s)-1]);return o
def cl(s):
 o=[];z=0
 for i in range(1,len(s)+1):
  if i==len(s) or s[i]!=s[z]:o.append({"position":q(s[z]),"multiplicity":i-z,"indices":list(range(z,i))});z=i
 return o
def build(cid,et,init):
 e=Fraction(et);s=tuple(Fraction(x) for x in init);traj=[[q(x) for x in s]];graphs=[];contacts=0;bound=4*len(s)**3+2*len(s)+2
 for _ in range(bound+1):
  g=[[j for j in range(len(s)) if abs(s[j]-s[i])<=e] for i in range(len(s))];graphs.append(g);contacts+=sum(abs(s[j]-s[i])==e for i in range(len(s)) for j in range(i+1,len(s)));n=upd(s,e)
  if n==s:break
  if tuple(sorted(n))!=n:raise AssertionError("order")
  s=n;traj.append([q(x) for x in s])
 else:raise AssertionError("bound")
 cs=cl(s);gaps=[Fraction(cs[i+1]["position"])-Fraction(cs[i]["position"]) for i in range(len(cs)-1)]
 return {"case_id":cid,"n":len(s),"epsilon":et,"initial":init,"initial_components":comps(tuple(Fraction(x) for x in init),e),"termination_time":len(traj)-1,"theorem_bound":bound,"trajectory":traj,"trajectory_sha256":hashlib.sha256(json.dumps(traj,sort_keys=True,separators=(",",":")).encode()).hexdigest(),"neighbor_graph_changes":sum(graphs[i]!=graphs[i-1] for i in range(1,len(graphs))),"boundary_contact_count":contacts,"initial_mean":q(sum(Fraction(x) for x in init)/len(s)),"final_mean":q(sum(s)/len(s)),"final_clusters":cs,"minimum_final_gap":q(min(gaps)) if gaps else None}
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def main():
 if sys.flags.optimize:raise RuntimeError("C312 checker refuses optimized Python")
 p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=E);p.add_argument("--evaluation",type=Path,default=Y);a=p.parse_args();d=sj(a.evidence);ev=sy(a.evaluation);checks=0
 if ph(d)!=d.get("payload_sha256") or (d.get("candidate_id"),d.get("obstruction_id"),d.get("source_commit"),d.get("scope_literal")) != ("HCS-C312","HEN-O296",SOURCE,SCOPE):raise AssertionError("identity")
 if d["route_a"]!={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False} or any(type(v)is not bool or v for v in d["scope_flags"].values()):raise AssertionError("route/scope")
 if d["mean_counterexample"]!={"initial":["0","1/2","7/5"],"updated":["1/4","19/30","19/20"],"initial_mean":"19/30","updated_mean":"11/18"}:raise AssertionError("mean counterexample")
 ss=specs()
 if len(d["cases"])!=len(ss):raise AssertionError("count")
 states=changed=maxterm=0
 for got,spec in zip(d["cases"],ss):
  want=build(*spec)
  if got!=want:raise AssertionError(f"case mismatch {spec[0]}")
  final=tuple(Fraction(x["position"]) for x in got["final_clusters"]);eps=Fraction(got["epsilon"])
  if any(final[i+1]-final[i]<=eps for i in range(len(final)-1)):raise AssertionError("cluster gap")
  if got["termination_time"]>got["theorem_bound"]:raise AssertionError("bound")
  states+=len(got["trajectory"]);changed+=got["initial_mean"]!=got["final_mean"];maxterm=max(maxterm,got["termination_time"]);checks+=leaves(got)
 expected={"case_count":len(ss),"trajectory_state_count":states,"maximum_observed_termination":maxterm,"changed_mean_cases":changed,"audited_leaf_count":d["enumeration"]["audited_leaf_count"]}
 if d["enumeration"]!=expected:raise AssertionError("enumeration")
 if (ev.get("candidate_id"),ev.get("obstruction_id"),ev.get("source_commit"),ev.get("scope_literal"),ev.get("tuple"),ev.get("overall_verdict"),ev.get("route_b_invocation_allowed")) != ("HCS-C312","HEN-O296",SOURCE,SCOPE,d["route_a"]["tuple"],"ROUTE_A_REJECTED",False):raise AssertionError("evaluation")
 if ev.get("scope_flags")!=d["scope_flags"] or ev.get("theorem_status")!="PROVABLE_AS_STATED":raise AssertionError("evaluation scope")
 print(f"C312 independent checker: PASS ({checks+30} checks)")
if __name__=="__main__":main()
