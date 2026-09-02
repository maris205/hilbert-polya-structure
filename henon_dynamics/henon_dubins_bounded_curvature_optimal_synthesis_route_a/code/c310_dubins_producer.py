#!/usr/bin/env python3
"""Deterministic six-word Dubins synthesis receipts for HCS-C310."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]; OUTPUT=ROOT/"results/c310_dubins_evidence.json"
SOURCE="b3e2f3f7207b85d7be942ff72b1f49e754615c76"; EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788393600; mp.mp.dps=90; TAU=2*mp.pi
FLAGS={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,"claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,"claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}
SPECS=[
 ("identity","0","0","0","1"),("straight-forward","3","0","0","1"),("straight-scaled","6","0","0","2"),
 ("straight-backward","-3","0","0","1"),("quarter-left","1","1","1/2","1"),("quarter-right","1","-1","-1/2","1"),
 ("half-turn-near","0","2","1","1"),("half-turn-axis","-4","0","1","1"),("ccc-boundary","4","0","0","1"),
 ("ccc-outside","5","0","0","1"),("lsl-owner","-4","-2","0","1"),("rsr-owner","-4","-4","1/2","1"),
 ("lsr-owner","-4","0","1","1"),("rsl-owner","-4","-4","0","1"),("rlr-owner","-2","0","1","1"),
 ("lrl-owner","-2","-2","-1/2","1"),("generic-a","2","3","1/3","1"),("generic-b","-1","3","-2/3","1"),
 ("generic-c","7/2","-5/3","5/6","1"),("generic-d","-7/3","4/3","-1/6","1"),("small-pose","1/10","-1/5","1/4","1"),
 ("large-radius","3","4","1/2","5/2"),("small-radius","3","4","-1/2","1/2"),("scaled-reflection","6","-4","-1/3","2"),
 ("coincident-half","0","0","1","1"),("coincident-quarter","0","0","1/2","1"),("vertical-up","0","5","0","1"),
 ("vertical-down","0","-5","0","1"),("heading-wrap-plus","2","1","7/3","1"),("heading-wrap-minus","2","-1","-7/3","1"),
]

def rat(text): return Fraction(text)
def mpq(text):
    value=Fraction(text); return mp.mpf(value.numerator)/value.denominator
def clean(value): return mp.mpf("0") if abs(value)<mp.mpf("1e-78") else value
def dec(value):
    value=clean(value)
    return "0.0" if value==0 else mp.nstr(value,72,strip_zeros=False)
def mod(value):
    out=mp.fmod(value,TAU)
    if out<0: out+=TAU
    if abs(out)<mp.mpf("1e-70") or abs(out-TAU)<mp.mpf("1e-70"): return mp.mpf("0")
    return clean(out)
def atan2c(y,x):
    return mp.mpf("0") if abs(y)<mp.mpf("1e-70") and abs(x)<mp.mpf("1e-70") else mp.atan2(y,x)
def angle_error(value): return clean(mp.atan2(mp.sin(value),mp.cos(value)))

def primitive(pose,mode,length):
    x,y,theta=pose
    if mode=="L": return (x+mp.sin(theta+length)-mp.sin(theta),y-mp.cos(theta+length)+mp.cos(theta),theta+length)
    if mode=="R": return (x+mp.sin(theta)-mp.sin(theta-length),y+mp.cos(theta-length)-mp.cos(theta),theta-length)
    return (x+length*mp.cos(theta),y+length*mp.sin(theta),theta)

def solve_word(word,d,a,b):
    sa,sb,ca,cb=mp.sin(a),mp.sin(b),mp.cos(a),mp.cos(b); cab=mp.cos(a-b); tol=mp.mpf("1e-70")
    if word=="LSL":
        test=2+d*d-2*cab+2*d*(sa-sb)
        if abs(test)<tol:test=mp.mpf("0")
        if test < -tol:return test,None
        p=mp.sqrt(max(mp.mpf("0"),test));tmp=atan2c(cb-ca,d+sa-sb); seg=(mod(-a+tmp),p,mod(b-tmp))
    elif word=="RSR":
        test=2+d*d-2*cab+2*d*(sb-sa)
        if abs(test)<tol:test=mp.mpf("0")
        if test < -tol:return test,None
        p=mp.sqrt(max(mp.mpf("0"),test));tmp=atan2c(ca-cb,d-sa+sb);seg=(mod(a-tmp),p,mod(-b+tmp))
    elif word=="LSR":
        test=-2+d*d+2*cab+2*d*(sa+sb)
        if abs(test)<tol:test=mp.mpf("0")
        if test < -tol:return test,None
        p=mp.sqrt(max(mp.mpf("0"),test));tmp=mp.atan2(-ca-cb,d+sa+sb)-mp.atan2(-2,p);seg=(mod(-a+tmp),p,mod(-b+tmp))
    elif word=="RSL":
        test=-2+d*d+2*cab-2*d*(sa+sb)
        if abs(test)<tol:test=mp.mpf("0")
        if test < -tol:return test,None
        p=mp.sqrt(max(mp.mpf("0"),test));tmp=mp.atan2(ca+cb,d-sa-sb)-mp.atan2(2,p);seg=(mod(a-tmp),p,mod(b-tmp))
    elif word=="RLR":
        test=(6-d*d+2*cab+2*d*(sa-sb))/8
        if abs(test-1)<tol:test=mp.mpf("1")
        if abs(test+1)<tol:test=-mp.mpf("1")
        if abs(test)>1+tol:return test,None
        middle=mod(TAU-mp.acos(max(-mp.mpf(1),min(mp.mpf(1),test))));first=mod(a-atan2c(ca-cb,d-sa+sb)+middle/2);seg=(first,middle,mod(a-b-first+middle))
    else:
        test=(6-d*d+2*cab+2*d*(-sa+sb))/8
        if abs(test-1)<tol:test=mp.mpf("1")
        if abs(test+1)<tol:test=-mp.mpf("1")
        if abs(test)>1+tol:return test,None
        middle=mod(TAU-mp.acos(max(-mp.mpf(1),min(mp.mpf(1),test))));first=mod(-a-atan2c(ca-cb,d+sa-sb)+middle/2);seg=(first,middle,mod(b-a-first+middle))
    return clean(test),tuple(clean(value) for value in seg)

def build_case(spec):
    case_id,xs,ys,phis,rs=spec; x,y,R=mpq(xs),mpq(ys),mpq(rs); phi=mpq(phis)*mp.pi
    xn,yn=x/R,y/R; d=mp.sqrt(xn*xn+yn*yn); theta=mp.atan2(yn,xn) if d else mp.mpf("0"); a=mod(-theta);b=mod(phi-theta)
    candidates=[]
    for word in ("LSL","RSR","LSR","RSL","RLR","LRL"):
        test,segments=solve_word(word,d,a,b)
        if segments is None:
            candidates.append({"word":word,"feasible":False,"feasibility_value":dec(test),"segments":None,"normalized_length":None,"physical_length":None,"endpoint_residual":None})
            continue
        pose=(mp.mpf("0"),mp.mpf("0"),mp.mpf("0"))
        for mode,length in zip(word,segments):pose=primitive(pose,mode,length)
        residual=mp.sqrt((R*pose[0]-x)**2+(R*pose[1]-y)**2+angle_error(pose[2]-phi)**2)
        length=sum(segments)
        candidates.append({"word":word,"feasible":True,"feasibility_value":dec(test),"segments":[dec(value) for value in segments],"normalized_length":dec(length),"physical_length":dec(R*length),"endpoint_residual":dec(residual)})
    finite=[mp.mpf(row["physical_length"]) for row in candidates if row["feasible"]]; minimum=min(finite)
    minimizers=[row["word"] for row in candidates if row["feasible"] and abs(mp.mpf(row["physical_length"])-minimum)<mp.mpf("1e-60")]
    return {"case_id":case_id,"target":{"x":xs,"y":ys,"heading_pi":phis,"radius":rs},"normalized":{"d":dec(d),"alpha":dec(a),"beta":dec(b)},"candidates":candidates,"minimum_length":dec(minimum),"minimizers":minimizers,"euclidean_lower_bound":dec(mp.sqrt(x*x+y*y))}

def ph(data):
    body=dict(data);body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(value):
    if type(value) is dict:return sum(leaves(v) for v in value.values())
    if type(value) is list:return sum(leaves(v) for v in value)
    return 1
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=OUTPUT);args=parser.parse_args();cases=[build_case(spec) for spec in SPECS]
    data={"schema":"hcs-c310-dubins-six-word-v1","candidate_id":"HCS-C310","obstruction_id":"HEN-O294","evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,"evaluator":{"version":"0.2.0","sha256":EVALUATOR},"model":{"configuration":"SE(2)","dynamics":"xdot=cos(theta), ydot=sin(theta), abs(thetadot)<=1/R, forward motion only","boundary_data":"two oriented poses; Euclidean invariance fixes the initial pose at (0,0,0)"},"theorem_contract":{"synthesis":"a global minimizer exists among LSL, RSR, LSR, RSL, RLR, and LRL","formulas":"all six normalized segment triples, feasibility discriminants, degeneracies, and ties are retained","replay":"integrating every feasible word returns the prescribed pose","scaling":"multiplying positions and R by s multiplies every length by s","symmetry":"reflection interchanges L and R and negates y and heading"},"cases":cases,"word_coverage":{word:sum(word in case["minimizers"] for case in cases) for word in ("LSL","RSR","LSR","RSL","RLR","LRL")},"collision_boundary":{"C222":"C222 is a second-order double-integrator switching problem without curvature-bounded SE(2) geometry.","C270":"C270 is Heisenberg sub-Riemannian control with reversible horizontal velocity rather than a forward-only car.","C305":"C305 has convex first-order velocity balls and constant wind; C310 has nonholonomic heading and bang-straight-bang synthesis."},"route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"scope_flags":FLAGS,"nonclaims":["Endpoint-optimal controlled arcs are not asserted to be intrinsic primitive periodic orbits.","Pontryagin's Hamiltonian is a source control device, not a Hilbert--Polya operator.","No target arithmetic datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted."],"references":[{"identifier":"10.2307/2372560","role":"original Dubins bounded-curvature theorem and historical ownership"}]}
    data["enumeration"]={"case_count":len(cases),"candidate_word_cells":6*len(cases),"feasible_word_cells":sum(row["feasible"] for case in cases for row in case["candidates"])};data["enumeration"]["audited_leaf_count"]=leaves(data)+1;data["payload_sha256"]=ph(data)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C310_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")
if __name__=="__main__":main()
