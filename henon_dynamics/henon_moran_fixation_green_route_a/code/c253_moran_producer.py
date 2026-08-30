#!/usr/bin/env python3
"""Deterministic exact certificate for the finite Moran birth--death process.

For population size N, type count i, selection ratio rho and event scale beta,
lambda_i=beta*rho*i*(N-i)/N and mu_i=beta*i*(N-i)/N.  Boundaries 0,N
absorb.  All receipts are source-local rational calculations.
"""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import mpmath as mp

SOURCE="3ff451e904f8f063e88c40ef87f4697a6586b1a5"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c253_moran_evidence.json"; mp.mp.dps=90

def ft(q):
    q=q if isinstance(q,F) else F(q); return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
def mq(q): q=q if isinstance(q,F) else F(q); return mp.mpf(q.numerator)/q.denominator
def dec(x): return mp.nstr(mp.mpf(x),64,strip_zeros=False,min_fixed=-70,max_fixed=70)
def ph(d):
    b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def rates(N,rho,beta):
    lam=[F(0)]+[beta*rho*F(i*(N-i),N) for i in range(1,N)]
    mu=[F(0)]+[beta*F(i*(N-i),N) for i in range(1,N)]
    return lam,mu

def solve(A,b):
    n=len(b); M=[list(map(F,A[i]))+[F(b[i])] for i in range(n)]
    for col in range(n):
        piv=next(j for j in range(col,n) if M[j][col])
        M[col],M[piv]=M[piv],M[col]; z=M[col][col]; M[col]=[x/z for x in M[col]]
        for j in range(n):
            if j==col: continue
            z=M[j][col]
            if z: M[j]=[M[j][k]-z*M[col][k] for k in range(n+1)]
    return [M[i][-1] for i in range(n)]

def green(N,rho,beta):
    lam,mu=rates(N,rho,beta); n=N-1
    Q=[[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(1,N):
        j=i-1; Q[j][j]=-(lam[i]+mu[i])
        if i+1<N: Q[j][j+1]=lam[i]
        if i-1>0: Q[j][j-1]=mu[i]
    # inverse of -Q by solving each column
    A=[[-Q[i][j] for j in range(n)] for i in range(n)]
    cols=[]
    for c in range(n):
        e=[F(int(i==c)) for i in range(n)]; cols.append(solve(A,e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def fixation(N,rho,i):
    if rho==1: return F(i,N)
    # avoid negative powers using integer powers
    a=F(1)-F(1,rho**i); b=F(1)-F(1,rho**N)
    return a/b

def weights(N,rho):
    # speed measure on transient states, w_1=1
    out=[F(0)]*(N-1); out[0]=F(1)
    for i in range(1,N-1):
        out[i]=out[i-1]*rho*F(i*(N-i),(i+1)*(N-i-1))
    return out

def row(cid,N,rho,beta,start):
    lam,mu=rates(N,rho,beta); G=green(N,rho,beta)
    f=fixation(N,rho,start); t=sum(G[start-1])
    w=weights(N,rho); total=sum(w)
    wn=[x/total for x in w]
    return {"case_id":cid,"N":N,"rho":ft(rho),"beta":ft(beta),"start_i":start,
            "lambda_rates":[ft(x) for x in lam],"mu_rates":[ft(x) for x in mu],
            "fixation_probability":ft(f),"fixation_probability_decimal":dec(mq(f)),
            "expected_absorption_time":ft(t),"expected_absorption_time_decimal":dec(mq(t)),
            "green_matrix":[[ft(x) for x in rr] for rr in G],
            "reversible_weights":[ft(x) for x in w],"reversible_weights_normalized":[dec(mq(x)) for x in wn],
            "transient_state_count":N-1,"boundary_policy":"X=0 and X=N absorbing"}

CASES=[("neutral_N3",3,F(1),F(1),1),("selected_up_N4",4,F(2),F(1),2),("selected_down_N5",5,F(1,2),F(3,2),3),("mixed_N6",6,F(3,2),F(2),1),("mixed_N7",7,F(4,3),F(5,2),4),("neutral_N8",8,F(1),F(3,4),5),("weak_sel_N9",9,F(9,10),F(4,3),2),("strong_sel_N10",10,F(5,2),F(2,3),7)]

def build():
    d={"schema":"hcs-c253-moran-fixation-green-v1","candidate_id":"HCS-C253","evaluation_date":"2026-08-30","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"headline":"The finite Moran birth--death process is closed by an exact fixation formula, rational Green matrix and absorption-time ledger, reversible killed-chain weights, and explicit neutral/zero-rate/singleton faces.","frozen_object":{"state":"X in {0,...,N}, type count in a fixed population","rates":"lambda_i=beta*rho*i*(N-i)/N; mu_i=beta*i*(N-i)/N","parameters":"integer N>=2, rho>0, beta>0; boundaries absorbing","clock":"continuous event time","normalization":"transient generator Q; Green=(-Q)^(-1)","determinant_convention":"none; no target or Fredholm determinant","arithmetic_origin":"none; source-defined finite population parameters","forbidden_data":"target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert--Polya operators"},"theorem":{"absorption":"For beta>0 the finite chain hits 0 or N almost surely.","fixation":"u_i=(1-rho^{-i})/(1-rho^{-N}) for rho!=1 and u_i=i/N for rho=1.","green":"The transient occupation matrix is G=(-Q)^(-1), so t_i=sum_j G_ij is the exact expected absorption time.","reversibility":"The killed chain is diagonally symmetrizable with w_{i+1}/w_i=rho*i*(N-i)/((i+1)*(N-i-1)).","boundaries":"rho=1 is neutral; beta=0 freezes every state and makes absorption time infinite; N=1 has no transient state.","route_boundary":"The finite stochastic process has no arithmetic labels, primitive target orbit, determinant, or Hilbert--Polya operator."},"regression":{"rows":[row(*s) for s in CASES],"row_count":len(CASES),"boundary_rows":[{"face_id":"neutral","condition":"rho=1","policy":"u_i=i/N"},{"face_id":"zero_rate","condition":"beta=0","policy":"frozen chain; no finite absorption claim"},{"face_id":"singleton","condition":"N=1","policy":"already absorbed; transient Green matrix empty"},{"face_id":"selection_limit","condition":"rho tends to 0 or infinity","policy":"outside positive finite-rate receipt"}],"boundary_row_count":4,"working_digits":90,"serialized_digits":64},"exact_identities":[{"identity_id":"rates","formula":"lambda_i=beta*rho*i*(N-i)/N; mu_i=beta*i*(N-i)/N"},{"identity_id":"generator","formula":"Q_ii=-(lambda_i+mu_i), Q_i,i+1=lambda_i, Q_i,i-1=mu_i"},{"identity_id":"fixation_selected","formula":"u_i=(1-rho^{-i})/(1-rho^{-N})"},{"identity_id":"fixation_neutral","formula":"u_i=i/N"},{"identity_id":"backward_equation","formula":"lambda_i(u_{i+1}-u_i)+mu_i(u_{i-1}-u_i)=0"},{"identity_id":"time_equation","formula":"lambda_i(t_{i+1}-t_i)+mu_i(t_{i-1}-t_i)=-1"},{"identity_id":"green_inverse","formula":"G=(-Q)^(-1)"},{"identity_id":"detailed_balance","formula":"w_i lambda_i=w_{i+1} mu_{i+1}"},{"identity_id":"absorption","formula":"finite transient Q is nonsingular for beta>0"},{"identity_id":"neutral_face","formula":"rho=1 gives u_i=i/N"}],"route_a":{"tuple":["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,"strongest_positive":"Exact finite-state fixation, Green, time, and reversible-weight theorem.","strongest_failure":"No arithmetic origin, primitive target orbit, determinant, or Hilbert--Polya lift."},"scope_flags":{k:False for k in ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]},"citations":[{"key":"Moran1958","claim":"finite population birth-death model","source":"P. A. P. Moran, Random processes in genetics, Mathematical Proceedings Cambridge 54 (1958)"},{"key":"Ewens2004","claim":"fixation and diffusion context","source":"W. J. Ewens, Mathematical Population Genetics, Springer (2004)"},{"key":"Norris1997","claim":"finite Markov-chain Green/resolvent vocabulary","source":"J. R. Norris, Markov Chains, Cambridge University Press (1997)"}],"nonclaims":["literature priority or a diffusion limit beyond the frozen finite chain","a beta=0 finite absorption time (the chain is frozen)","target arithmetic, Euler factors, root numbers, automorphy, target divisor or functional equation","a primitive-orbit zeta, Fredholm determinant, or Hilbert--Polya operator","external peer review or numerical evidence promoted to a theorem"]}
    d["payload_sha256"]=ph(d); return d
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=DEFAULT); a=ap.parse_args(); a.output.parent.mkdir(parents=True,exist_ok=True); d=build(); a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"status":"C253_PRODUCER_PASS","rows":d["regression"]["row_count"],"payload_sha256":d["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
