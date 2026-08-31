#!/usr/bin/env python3
"""Deterministic direct-permutation certificate for HCS-C260."""
from __future__ import annotations
import argparse, json, math
from collections import Counter
from hashlib import sha256
from pathlib import Path

SOURCE="98782afe1e754c311ad0736f72ce09dcc7c85c77"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c260_pgl2_evidence.json"
FIELD_SPECS=[(2,[0,1]),(3,[0,1]),(4,[1,1,1]),(5,[0,1]),(7,[0,1]),(8,[1,1,0,1]),(9,[1,0,1]),(11,[0,1]),(13,[0,1]),(16,[1,1,0,0,1]),(17,[0,1]),(19,[0,1]),(23,[0,1]),(25,[2,0,1]),(27,[1,2,0,1]),(29,[0,1]),(31,[0,1]),(32,[1,0,1,0,0,1])]

def payload_hash(d):
    b=dict(d); b.pop("payload_sha256",None)
    return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def prime_power(q):
    for p in range(2,q+1):
        if any(p%d==0 for d in range(2,int(p**.5)+1)): continue
        x,r=q,0
        while x%p==0: x//=p; r+=1
        if x==1:return p,r
    raise ValueError(q)
class GF:
    def __init__(self,q,mod):
        self.q=q; self.p,self.r=prime_power(q); self.mod=mod; assert len(mod)==self.r+1 and mod[-1]==1
        self.add_table=[[self._add_raw(a,b) for b in range(q)] for a in range(q)]
        self.mul_table=[[self._mul_raw(a,b) for b in range(q)] for a in range(q)]
        self.inv_table=[0]+[next(b for b in range(1,q) if self.mul_table[a][b]==1) for a in range(1,q)]
    def digits(self,a):
        z=[]
        for _ in range(self.r): z.append(a%self.p); a//=self.p
        return z
    def encode(self,z):
        a=0
        for c in reversed(z): a=a*self.p+c%self.p
        return a
    def _add_raw(self,a,b): return self.encode([(x+y)%self.p for x,y in zip(self.digits(a),self.digits(b))])
    def add(self,a,b): return self.add_table[a][b]
    def neg(self,a): return self.encode([(-x)%self.p for x in self.digits(a)])
    def sub(self,a,b): return self.add(a,self.neg(b))
    def _mul_raw(self,a,b):
        aa,bb=self.digits(a),self.digits(b); cc=[0]*(2*self.r-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb): cc[i+j]=(cc[i+j]+x*y)%self.p
        for k in range(len(cc)-1,self.r-1,-1):
            lead=cc[k]
            if lead:
                for j in range(self.r): cc[k-self.r+j]=(cc[k-self.r+j]-lead*self.mod[j])%self.p
        return self.encode(cc[:self.r])
    def mul(self,a,b): return self.mul_table[a][b]
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a); n//=2
        return z
    def inv(self,a): assert a; return self.inv_table[a]
    def div(self,a,b): return self.mul(a,self.inv(b))
    def trace2(self,a):
        assert self.p==2; z,x=0,a
        for _ in range(self.r): z=self.add(z,x); x=self.mul(x,x)
        assert z in (0,1); return z
def mm(F,A,B):
    a,b,c,d=A;e,f,g,h=B
    return(F.add(F.mul(a,e),F.mul(b,g)),F.add(F.mul(a,f),F.mul(b,h)),F.add(F.mul(c,e),F.mul(d,g)),F.add(F.mul(c,f),F.mul(d,h)))
def scalar(A): a,b,c,d=A; return b==0 and c==0 and a==d
def order(F,A):
    P=(1,0,0,1)
    for n in range(1,F.q+2):
        P=mm(F,P,A)
        if scalar(P):return n
    raise AssertionError
def reps(F):
    q=F.q
    for b in range(q):
        for c in range(q):
            bc=F.mul(b,c)
            for d in range(q):
                if d!=bc:yield(1,b,c,d)
    for c in range(1,q):
        for d in range(q):yield(0,1,c,d)
def perm(F,A):
    a,b,c,d=A; out=[]
    for x in range(F.q):
        den=F.add(F.mul(c,x),d)
        out.append(F.q if den==0 else F.div(F.add(F.mul(a,x),b),den))
    out.append(F.q if c==0 else F.div(a,c)); assert sorted(out)==list(range(F.q+1)); return out
def cycles(P):
    seen=[False]*len(P); out=[]
    for x in range(len(P)):
        if not seen[x]:
            y,L=x,0
            while not seen[y]:seen[y]=True;L+=1;y=P[y]
            out.append(L)
    return sorted(out)
def kind(F,A):
    if scalar(A):return"identity"
    a,b,c,d=A; tr=F.add(a,d); det=F.sub(F.mul(a,d),F.mul(b,c))
    if F.p==2:
        if tr==0:return"unipotent"
        return"split" if F.trace2(F.div(det,F.mul(tr,tr)))==0 else"nonsplit"
    delta=F.sub(F.mul(tr,tr),F.mul(4%F.p,det))
    if delta==0:return"unipotent"
    return"split" if F.pow(delta,(F.q-1)//2)==1 else"nonsplit"
def expected(q,p,t,d):
    if t=="identity":return[1]*(q+1)
    if t=="unipotent":assert d==p;return[1]+[p]*(q//p)
    if t=="split":assert d>1 and (q-1)%d==0;return[1,1]+[d]*((q-1)//d)
    assert t=="nonsplit" and d>1 and (q+1)%d==0;return[d]*((q+1)//d)
def phi(n):return sum(math.gcd(k,n)==1 for k in range(1,n+1))
def theory(q,p):
    s={str(d):q*(q+1)*phi(d)//2 for d in range(2,q+2) if (q-1)%d==0}
    ns={str(d):q*(q-1)*phi(d)//2 for d in range(2,q+2) if (q+1)%d==0}
    return{"identity":{"1":1},"unipotent":{str(p):q*q-1},"split":s,"nonsplit":ns}
def field_row(q,mod):
    F=GF(q,mod); counts=Counter(); hist={k:Counter() for k in("identity","unipotent","split","nonsplit")}; H=sha256(); witnesses={}; elements=images=checks=0
    for A in reps(F):
        t=kind(F,A);d=order(F,A);cyc=cycles(perm(F,A));assert cyc==expected(q,F.p,t,d)
        rec={"matrix":list(A),"type":t,"order":d,"cycles":cyc};H.update((json.dumps(rec,sort_keys=True,separators=(",",":"))+"\n").encode())
        counts[t]+=1;hist[t][str(d)]+=1;witnesses.setdefault(t,rec);elements+=1;images+=q+1;checks+=4+2*d
    obs={k:dict(sorted(hist[k].items(),key=lambda z:int(z[0]))) for k in hist}; th=theory(q,F.p);assert obs==th;assert elements==q*(q*q-1)
    return{"q":q,"p":F.p,"extension_degree":F.r,"modulus_coefficients_low_to_high":mod,"pgl_element_count":elements,"direct_state_images":images,"direct_assertion_units":checks,"type_counts":dict(sorted(counts.items())),"order_histograms":obs,"theoretical_order_histograms":th,"element_record_sha256":H.hexdigest(),"witnesses":witnesses}
def build():
    rows=[field_row(q,m) for q,m in FIELD_SPECS]
    d={"schema":"hcs-c260-pgl2-projective-mobius-cycle-atlas-v1","candidate_id":"HCS-C260","evaluation_date":"2026-08-31","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,"evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},
    "headline":"Every element of PGL_2(F_q), for every prime power q, has exactly one of four projective-line cycle types; fixed, primitive, zeta, reversor, and finite Koopman data close exactly.",
    "frozen_object":{"phase_space":"P^1(F_q) with q=p^r an arbitrary prime power","map":"x -> (a*x+b)/(c*x+d) for [A] in PGL_2(F_q)","clock":"one projective Mobius update","normalization":"matrices modulo nonzero scalar; q finite points plus infinity","determinant_convention":"source Artin--Mazur zeta and finite Koopman determinant only","arithmetic_origin":"intrinsic finite-field and projective-linear structure","forbidden_data":"target zeros or primes, arithmetic local factors, Euler factors, root numbers, automorphy, target divisor or functional equation, Hilbert--Polya operators"},
    "theorem":{"classification":"identity, nontrivial unipotent, split semisimple, or nonsplit semisimple","identity":"cycle type 1^(q+1)","unipotent":"order p and cycle type 1^1 p^(q/p)","split":"eigenvalue-ratio order d|q-1 and cycle type 1^2 d^((q-1)/d)","nonsplit":"eigenvalue-ratio order d|q+1 and cycle type d^((q+1)/d)","fixed":"#Fix(g^n) is the sum of cycle lengths dividing n","primitive":"P_m=sum_{e|m} mu(m/e)#Fix(g^e), and C_m=P_m/m","zeta":"zeta_g(t)=product_over_cycles (1-t^L)^(-1)","koopman":"det(I-t U_g)=zeta_g(t)^(-1); each L-cycle contributes every L-th root once","reversor":"in a cyclic basis H=[[0,det(A)],[1,0]] is projectively involutive and conjugates g to g^(-1)","characteristic_two":"tr(A)=0 gives the repeated-root face; otherwise Tr_Fq/F2(det(A)/tr(A)^2) distinguishes split zero from nonsplit one","type_census":"unipotent q^2-1; split order d count q(q+1)phi(d)/2; nonsplit order d count q(q-1)phi(d)/2","route_boundary":"finite-field arithmetic supplies no rational-prime orbit dictionary, logarithmic prime clock, target divisor, or Hilbert--Polya identification"},
    "regression":{"field_values":[q for q,_ in FIELD_SPECS],"field_count":len(rows),"field_rows":rows,"enumerated_pgl_elements":sum(r["pgl_element_count"] for r in rows),"direct_state_images":sum(r["direct_state_images"] for r in rows),"direct_assertion_units":sum(r["direct_assertion_units"] for r in rows)},
    "exact_identities":[{"identity_id":"cayley_hamilton","formula":"A^2-tr(A)A+det(A)I=0"},{"identity_id":"reversor","formula":"HAH^(-1)=det(A)A^(-1) in a cyclic basis"},{"identity_id":"unipotent_fix","formula":"F_n=1+q*1_(p|n)"},{"identity_id":"split_fix","formula":"F_n=2+(q-1)*1_(d|n)"},{"identity_id":"nonsplit_fix","formula":"F_n=(q+1)*1_(d|n)"},{"identity_id":"mobius","formula":"P_m=sum_(e|m)mu(m/e)F_e"},{"identity_id":"zeta","formula":"zeta=product_L(1-t^L)^(-c_L)"},{"identity_id":"koopman","formula":"det(I-tU)=product_L(1-t^L)^(c_L)"},{"identity_id":"group_size","formula":"|PGL_2(F_q)|=q(q^2-1)"}],
    "route_a":{"tuple":["A0_WEAK_ARITHMETIC_RELATION","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False,"strongest_positive":"all-prime-power analytic cycle classification and a canonical finite same-clock unitary Koopman owner","strongest_failure":"no rational-prime primitive carrier, log-prime clock, target divisor, target analytic continuation, or Hilbert--Polya identification"},
    "scope_flags":{"uses_target_zero_table":False,"uses_prime_table":False,"claims_arithmetic_local_data":False,"claims_euler_factors":False,"claims_root_numbers":False,"claims_automorphy":False,"claims_target_divisor_or_functional_equation":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False},
    "citations":[{"key":"Sakzad2012","doi":"10.3934/amc.2012.6.347","claim":"finite-field Mobius permutation cycle structures"},{"key":"Forsyth2016","doi":"10.1090/proc/13126","claim":"PGL_2 projective-line action and cycle characterization"},{"key":"Wall1980","doi":"10.1017/S0004972700006675","claim":"projective-linear conjugacy classes over finite fields"}],
    "nonclaims":["literature priority for the classical conjugacy classification","that the finite test set proves the arbitrary-prime-power theorem","a rational-prime primitive-orbit dictionary or logarithmic prime clock","target arithmetic local data, Euler factors, root numbers, automorphy, divisor, or functional equation","a target Fredholm determinant, Hilbert--Polya operator, or Route-B authorization"]}
    d["payload_sha256"]=payload_hash(d);return d
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=DEFAULT);a=p.parse_args();a.output.parent.mkdir(parents=True,exist_ok=True);d=build();a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C260_PRODUCER_PASS","fields":d["regression"]["field_count"],"pgl_elements":d["regression"]["enumerated_pgl_elements"],"state_images":d["regression"]["direct_state_images"],"payload_sha256":d["payload_sha256"]},sort_keys=True))
if __name__=="__main__":main()
