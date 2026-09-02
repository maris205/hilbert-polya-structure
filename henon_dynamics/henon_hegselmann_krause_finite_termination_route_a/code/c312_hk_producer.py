#!/usr/bin/env python3
"""Exhaustive exact rational ledger for one-dimensional HK dynamics."""
from __future__ import annotations
import argparse,hashlib,itertools,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUTPUT=ROOT/"results/c312_hk_evidence.json";SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76";EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788393600
GRID=[Fraction(k,2) for k in range(7)]
NAMED=[("threshold-pair","1",["0","1"]),("separated-pair","1",["0","3/2"]),("mean-counterexample","1",["0","1/2","7/5"]),("unit-chain-five","1",["0","1","2","3","4"]),("duplicate-chain","1",["0","0","1","2","2"]),("negative-cloud","1",["-3/2","-1","0","1/2"]),("scaled-chain","2",["0","2","4","6"]),("third-radius","1/3",["-1/3","0","1/3","2/3"]),("two-components","1",["0","1/2","3","7/2","4"]),("all-equal","5/7",["2","2","2","2"])]
FLAGS={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,"claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,"claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}
def q(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def update(state,eps):return tuple(sum((state[j] for j in range(len(state)) if abs(state[j]-state[i])<=eps),Fraction(0))/sum(abs(state[j]-state[i])<=eps for j in range(len(state))) for i in range(len(state)))
def comps(state,eps):
 out=[];start=0
 for i in range(len(state)-1):
  if state[i+1]-state[i]>eps:out.append([start,i]);start=i+1
 out.append([start,len(state)-1]);return out
def clusters(state):
 out=[];start=0
 for i in range(1,len(state)+1):
  if i==len(state) or state[i]!=state[start]:out.append({"position":q(state[start]),"multiplicity":i-start,"indices":list(range(start,i))});start=i
 return out
def thash(traj):return hashlib.sha256(json.dumps(traj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def build(cid,eps_text,initial_text):
 eps=Fraction(eps_text);state=tuple(Fraction(x) for x in initial_text)
 if tuple(sorted(state))!=state or eps<=0:raise ValueError("bad case")
 trajectory=[[q(x) for x in state]];graphs=[];contacts=0
 bound=4*len(state)**3+2*len(state)+2
 for _ in range(bound+1):
  graph=[[j for j in range(len(state)) if abs(state[j]-state[i])<=eps] for i in range(len(state))];graphs.append(graph);contacts+=sum(abs(state[j]-state[i])==eps for i in range(len(state)) for j in range(i+1,len(state)))
  nxt=update(state,eps)
  if nxt==state:break
  if tuple(sorted(nxt))!=nxt:raise AssertionError("order lost")
  state=nxt;trajectory.append([q(x) for x in state])
 else:raise AssertionError("termination bound exceeded")
 final_clusters=clusters(state);gaps=[Fraction(final_clusters[i+1]["position"])-Fraction(final_clusters[i]["position"]) for i in range(len(final_clusters)-1)]
 return {"case_id":cid,"n":len(state),"epsilon":eps_text,"initial":initial_text,"initial_components":comps(tuple(Fraction(x) for x in initial_text),eps),"termination_time":len(trajectory)-1,"theorem_bound":bound,"trajectory":trajectory,"trajectory_sha256":thash(trajectory),"neighbor_graph_changes":sum(graphs[i]!=graphs[i-1] for i in range(1,len(graphs))),"boundary_contact_count":contacts,"initial_mean":q(sum(Fraction(x) for x in initial_text)/len(state)),"final_mean":q(sum(state)/len(state)),"final_clusters":final_clusters,"minimum_final_gap":q(min(gaps)) if gaps else None}
def specs():
 out=list(NAMED)
 for n in range(1,6):
  for k,values in enumerate(itertools.combinations_with_replacement(GRID,n)):out.append((f"grid-n{n}-{k:04d}","1",[q(x) for x in values]))
 return out
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def main():
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=OUTPUT);a=p.parse_args();cases=[build(*s) for s in specs()]
 d={"schema":"hcs-c312-one-dimensional-hk-v1","candidate_id":"HCS-C312","obstruction_id":"HEN-O296","evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,"evaluator":{"version":"0.2.0","sha256":EVALUATOR},"model":{"state_space":"ordered n-tuples of real opinions","dynamics":"synchronous average over all agents at distance <=epsilon","parameters":"n>=1 and homogeneous confidence radius epsilon>0"},"theorem_contract":{"order":"order and coincident blocks are preserved","decomposition":"a gap greater than epsilon persists forever and splits independent subsystems","termination":"the system reaches an exact fixed configuration within 4n^3+2n+2 updates","fixed_points":"fixed configurations are exactly equal-position clusters separated by gaps greater than epsilon","cell_map":"on each strict neighbor-graph cell the update is a row-stochastic rational linear map","mean_warning":"the arithmetic mean is not generally conserved"},"cases":cases,"mean_counterexample":{"initial":["0","1/2","7/5"],"updated":["1/4","19/30","19/20"],"initial_mean":"19/30","updated_mean":"11/18"},"collision_boundary":{"C203":"C203 has a fixed signed graph and continuous semigroup; C312 has a state-dependent confidence graph and synchronous nonlinear map.","C259":"C259 is a continuous tree Kuramoto phase flow, not bounded-confidence averaging.","C301":"C301 is an absorbing random partition refinement; C312 is deterministic metric opinion clustering with possible edge loss."},"route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"scope_flags":FLAGS,"nonclaims":["No heterogeneous radii, noise, higher-dimensional sharp bound, or asynchronous update theorem is claimed.","Finite termination produces fixed clusters, not nontrivial primitive periodic orbits.","No target arithmetic datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted."],"references":[{"identifier":"arXiv:1211.1909","role":"one-dimensional order/decomposition and cubic convergence theorem lineage"}]}
 d["enumeration"]={"case_count":len(cases),"trajectory_state_count":sum(len(c["trajectory"]) for c in cases),"maximum_observed_termination":max(c["termination_time"] for c in cases),"changed_mean_cases":sum(c["initial_mean"]!=c["final_mean"] for c in cases)};d["enumeration"]["audited_leaf_count"]=leaves(d)+1;d["payload_sha256"]=ph(d);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C312_PRODUCER_PASS {d['payload_sha256']} {d['enumeration']['case_count']} {d['enumeration']['audited_leaf_count']}")
if __name__=="__main__":main()
