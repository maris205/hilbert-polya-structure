#!/usr/bin/env python3
"""Deterministic certificate for a two-threshold relay phase oscillator.

State (theta,y,sigma) follows theta_dot=sigma, y_dot=-gamma*y.  The relay
switches + to - at theta=+h and - to + at theta=-h.  Guard priority and the
no-sliding convention are frozen in the evidence; this is not a claim about
all Filippov selections.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT="3ff451e904f8f063e88c40ef87f4697a6586b1a5"; EVAL_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
ROOT=Path(__file__).resolve().parents[1]; DEFAULT_OUTPUT=ROOT/"results/c252_relay_evidence.json"; WORKING_DIGITS=90; SERIALIZED_DIGITS=64; mp.mp.dps=WORKING_DIGITS
def ft(q):
    q=q if isinstance(q,F) else F(q); return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
def mq(q): q=q if isinstance(q,F) else F(q); return mp.mpf(q.numerator)/q.denominator
def dec(x): return mp.nstr(mp.mpf(x),SERIALIZED_DIGITS,strip_zeros=False,min_fixed=-70,max_fixed=70)
def ph(d):
    b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def leg(h,g,y0,sigma,leg_index):
    # leg 0 starts at -h with sigma=+1; leg 1 starts at +h with sigma=-1
    assert sigma in (-1,1)
    duration=2*h; y1=mq(y0)*mp.e**(-mq(g)*mq(duration)); target=h if sigma==1 else -h
    return {"leg":leg_index,"start_theta":ft(-h if sigma==1 else h),"end_theta":ft(target),"sigma":sigma,"duration":ft(duration),"y_start":ft(y0),"y_end":dec(y1),"decay_factor":dec(mp.e**(-mq(g)*mq(duration))),"guard":"theta=+h -> sigma=-1" if sigma==1 else "theta=-h -> sigma=+1"}

def cycle(h,g,y0):
    q=mp.e**(-mq(g)*mq(4*h)); y1=mq(y0)*q
    return {"h":ft(h),"gamma":ft(g),"y0":ft(y0),"full_period":ft(4*h),"return_theta":ft(-h),"return_sigma":1,"y_return":dec(y1),"poincare_multiplier":dec(q),"fixed_periodic_y":ft(0) if y0==0 else None,"nonzero_contraction":bool(g>0)}

CASES=[("contracting_a",F(1,2),F(1),F(3,2)),("contracting_b",F(2),F(3,4),F(-2)),("neutral",F(3,2),F(0),F(5,3)),("small_h",F(1,5),F(7,3),F(1,7)),("large_h",F(5,2),F(1,5),F(-3,2)),("zero_y",F(1),F(2),F(0)),("rational_decay",F(3,4),F(2),F(4,3)),("boundary_grazing",F(1),F(1),F(1))]

def row(cid,h,g,y):
    c=cycle(h,g,y); l0=leg(h,g,y,1,0); l1=leg(h,g,F(0),-1,1) # y=0 placeholder for geometry
    l1["y_start"]=l0["y_end"]; l1["y_end"]=dec(mq(l0["y_end"])*mp.e**(-mq(g)*mq(2*h)))
    return {"case_id":cid,"h":ft(h),"gamma":ft(g),"y0":ft(y),"left_section":ft(-h),"right_section":ft(h),"leg_time":ft(2*h),"full_period":ft(4*h),"leg_rows":[l0,l1],"cycle":c,"half_multiplier":dec(mp.e**(-mq(g)*mq(2*h))),"full_multiplier":dec(mp.e**(-mq(g)*mq(4*h))),"guard_policy":"instantaneous switch at equality; mode is held strictly inside (-h,h)","grazing":y==0}

def build():
    data={"schema":"hcs-c252-hysteretic-relay-v1","candidate_id":"HCS-C252","evaluation_date":"2026-08-30","source_commit":SOURCE_COMMIT,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL_SHA},"headline":"A two-threshold hysteretic relay phase oscillator has an exact switching map, a periodic orbit, transverse decay, grazing policy, and a no-Zeno theorem.","frozen_object":{"state":"(theta,y,sigma) with theta in [-h,h], y in R, sigma in {+1,-1}","flow":"theta_dot=sigma, y_dot=-gamma*y, gamma>=0","guards":"theta=+h switches +1 to -1; theta=-h switches -1 to +1","clock":"continuous hybrid time","normalization":"h>0; return section Sigma_-=(theta=-h,sigma=+1)","determinant_convention":"none; no primitive-orbit/Fredholm determinant","arithmetic_origin":"none; source-defined relay parameters","forbidden_data":"target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators"},"theorem":{"wellposedness":"The guard-priority hybrid convention gives a unique forward execution from every consistent interior/boundary state.","event_map":"Each leg has time 2h and maps y to exp(-2 gamma h)y; the full return map on Sigma_- is y -> exp(-4 gamma h)y.","periodic_set":"For gamma>0 the unique periodic orbit is y=0 with period 4h; for gamma=0 every constant y is periodic with the same phase period.","entry":"Every interior trajectory reaches a switching section in at most 2h, then follows the exact two-leg cycle.","no_zeno":"All successive event times equal 2h>0, so finite-time Zeno accumulation is impossible.","grazing":"y=0 is a transverse-neutral geometric grazing label only; no sliding segment is introduced.","route_boundary":"The relay flow has no arithmetic labels, target determinant, or Hilbert--Polya operator."},"regression":{"rows":[row(*s) for s in CASES],"row_count":len(CASES),"boundary_rows":[{"face_id":"gamma_zero","policy":"neutral continuum of y-level cycles"},{"face_id":"y_zero","policy":"unique attracting periodic phase orbit when gamma>0"},{"face_id":"h_zero","policy":"excluded because inter-event time would vanish"},{"face_id":"inconsistent_boundary_mode","policy":"instantaneous guard correction before flow"}],"boundary_row_count":4,"working_digits":WORKING_DIGITS,"serialized_digits":SERIALIZED_DIGITS},"exact_identities":[{"identity_id":"leg_time","formula":"tau_+=tau_-=2h"},{"identity_id":"half_map","formula":"y_{n+1}=exp(-2 gamma h)y_n"},{"identity_id":"full_map","formula":"P(y)=exp(-4 gamma h)y"},{"identity_id":"period","formula":"T=4h"},{"identity_id":"fixed_set","formula":"P(y)=y iff gamma=0 or y=0"},{"identity_id":"no_zeno","formula":"inf_n tau_n=2h>0"},{"identity_id":"flow_solution","formula":"y(t)=y_0 exp(-gamma t)"},{"identity_id":"guard_left","formula":"theta=-h,sigma=-1 => sigma:=+1"},{"identity_id":"guard_right","formula":"theta=+h,sigma=+1 => sigma:=-1"},{"identity_id":"entry_bound","formula":"interior entry time <=2h"}],"route_a":{"tuple":["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,"strongest_positive":"Exact hybrid event/return theorem and no-Zeno bound.","strongest_failure":"No arithmetic origin, primitive target orbit, determinant, or natural Hilbert--Polya lift."},"scope_flags":{k:False for k in ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]},"citations":[{"key":"Liberzon2003","claim":"switching/hysteresis terminology","source":"D. Liberzon, Switching in Systems and Control, Birkhauser (2003)"},{"key":"Filippov1988","claim":"discontinuous-system boundary vocabulary","source":"A. F. Filippov, Differential Equations with Discontinuous Righthand Sides (1988)"},{"key":"diBernardo2008","claim":"hybrid relay context","source":"M. di Bernardo et al., Piecewise-smooth Dynamical Systems, Springer (2008)"}],"nonclaims":["literature priority or general Filippov selection theory","a sliding continuation at h=0 or an unspecified relay convention","target arithmetic, Euler factors, root numbers, automorphy, target divisor or functional equation","a primitive-orbit zeta, Fredholm determinant, or Hilbert--Polya operator","external peer review or numerical evidence promoted to a theorem"]}
    data["payload_sha256"]=ph(data); return data
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT); a=ap.parse_args(); a.output.parent.mkdir(parents=True,exist_ok=True); d=build(); a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"status":"C252_PRODUCER_PASS","rows":d["regression"]["row_count"],"payload_sha256":d["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
