#!/usr/bin/env python3
"""Producer-independent checker using only direct permutation geometry."""
from __future__ import annotations
import argparse,json,math
from collections import Counter
from functools import reduce
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c260_pgl2_evidence.json"
SOURCE="98782afe1e754c311ad0736f72ce09dcc7c85c77";EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c";SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788048000
EXPECTED=["A0_WEAK_ARITHMETIC_RELATION","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"]
FROZEN_SHA="e15f9d2bdc9c09acf9c214777b1ea935b839815b48e8e2978887598608812e2a"
THEOREM_SHA="15aba9e1f51faff74d45b346c423c1c80b92fe0fa53a2a80bd27882f57ba5360"
ROWS_SHA="01ab0258971388e1dea560c436471fed0a1a8524b8bc033783b6ede918e7b777"
SPECS=[(2,[0,1]),(3,[0,1]),(4,[1,1,1]),(5,[0,1]),(7,[0,1]),(8,[1,1,0,1]),(9,[1,0,1]),(11,[0,1]),(13,[0,1]),(16,[1,1,0,0,1]),(17,[0,1]),(19,[0,1]),(23,[0,1]),(25,[2,0,1]),(27,[1,2,0,1]),(29,[0,1]),(31,[0,1]),(32,[1,0,1,0,0,1])]
def phash(d):
 b=dict(d);b.pop("payload_sha256",None);return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def jhash(x):return sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def pp(q):
 for p in range(2,q+1):
  if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
  x,r=q,0
  while x%p==0:x//=p;r+=1
  if x==1:return p,r
 raise ValueError
class Field:
 def __init__(self,q,m):
  self.q=q;self.p,self.r=pp(q);self.m=m
  self.at=[[self._ar(a,b) for b in range(q)] for a in range(q)];self.mt=[[self._mr(a,b) for b in range(q)] for a in range(q)]
  self.it=[0]+[next(b for b in range(1,q) if self.mt[a][b]==1) for a in range(1,q)]
 def ds(self,a):
  z=[]
  for _ in range(self.r):z.append(a%self.p);a//=self.p
  return z
 def en(self,z):
  a=0
  for c in reversed(z):a=a*self.p+c%self.p
  return a
 def _ar(self,a,b):return self.en([(x+y)%self.p for x,y in zip(self.ds(a),self.ds(b))])
 def _mr(self,a,b):
  aa,bb=self.ds(a),self.ds(b);cc=[0]*(2*self.r-1)
  for i,x in enumerate(aa):
   for j,y in enumerate(bb):cc[i+j]=(cc[i+j]+x*y)%self.p
  for k in range(len(cc)-1,self.r-1,-1):
   for j in range(self.r):cc[k-self.r+j]=(cc[k-self.r+j]-cc[k]*self.m[j])%self.p
  return self.en(cc[:self.r])
 def a(self,x,y):return self.at[x][y]
 def n(self,x):return self.en([(-u)%self.p for u in self.ds(x)])
 def s(self,x,y):return self.a(x,self.n(y))
 def mlt(self,x,y):return self.mt[x][y]
 def d(self,x,y):return self.mlt(x,self.it[y])
def reps(F):
 for b in range(F.q):
  for c in range(F.q):
   bc=F.mlt(b,c)
   for d in range(F.q):
    if d!=bc:yield(1,b,c,d)
 for c in range(1,F.q):
  for d in range(F.q):yield(0,1,c,d)
def permutation(F,A):
 a,b,c,d=A;P=[]
 for x in range(F.q):
  den=F.a(F.mlt(c,x),d);P.append(F.q if den==0 else F.d(F.a(F.mlt(a,x),b),den))
 P.append(F.q if c==0 else F.d(a,c));assert sorted(P)==list(range(F.q+1));return P
def cyc(P):
 seen=set();z=[]
 for x in range(len(P)):
  if x not in seen:
   y,L=x,0
   while y not in seen:seen.add(y);L+=1;y=P[y]
   z.append(L)
 return sorted(z)
def lcm(xs):return reduce(math.lcm,xs,1)
def direct_type(C,q,p):
 f=C.count(1);d=lcm(C)
 if f==q+1:return"identity",d
 if f==1:assert d==p;return"unipotent",d
 if f==2:assert d>1 and (q-1)%d==0;return"split",d
 assert f==0 and d>1 and (q+1)%d==0;return"nonsplit",d
def tot(n):return sum(math.gcd(k,n)==1 for k in range(1,n+1))
def expected_hist(q,p):return{"identity":{"1":1},"unipotent":{str(p):q*q-1},"split":{str(d):q*(q+1)*tot(d)//2 for d in range(2,q+2) if (q-1)%d==0},"nonsplit":{str(d):q*(q-1)*tot(d)//2 for d in range(2,q+2) if (q+1)%d==0}}
def preflight(d):
 assert d["schema"]=="hcs-c260-pgl2-projective-mobius-cycle-atlas-v1" and d["candidate_id"]=="HCS-C260"
 assert d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE
 assert d["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","sha256":EVAL,"version":"0.2.0"} and d["payload_sha256"]==phash(d)
 assert d["route_a"]["tuple"]==EXPECTED and d["route_a"]["overall"]=="ROUTE_A_EXPLORATORY" and d["route_a"]["route_b_invocation_allowed"] is False
 assert all(v is False for v in d["scope_flags"].values()) and [x["doi"] for x in d["citations"]]==["10.3934/amc.2012.6.347","10.1090/proc/13126","10.1017/S0004972700006675"]
 assert jhash(d["frozen_object"])==FROZEN_SHA and jhash(d["theorem"])==THEOREM_SHA
 R=d["regression"];assert R["field_count"]==len(SPECS) and R["field_values"]==[q for q,_ in SPECS]
 assert R["enumerated_pgl_elements"]==155346 and R["direct_state_images"]==4367094 and R["direct_assertion_units"]==6314520 and jhash(R["field_rows"])==ROWS_SHA
 assert [x["identity_id"] for x in d["exact_identities"]]==["cayley_hamilton","reversor","unipotent_fix","split_fix","nonsplit_fix","mobius","zeta","koopman","group_size"]
 assert d["nonclaims"]==[
  "literature priority for the classical conjugacy classification",
  "that the finite test set proves the arbitrary-prime-power theorem",
  "a rational-prime primitive-orbit dictionary or logarithmic prime clock",
  "target arithmetic local data, Euler factors, root numbers, automorphy, divisor, or functional equation",
  "a target Fredholm determinant, Hilbert--Polya operator, or Route-B authorization"]
def validate(d):
 preflight(d);rows={r["q"]:r for r in d["regression"]["field_rows"]};assertions=0;elements=images=units=0
 for q,mod in SPECS:
  F=Field(q,mod);hist={k:Counter() for k in("identity","unipotent","split","nonsplit")};H=sha256();count=0
  for A in reps(F):
   C=cyc(permutation(F,A));t,o=direct_type(C,q,F.p);hist[t][str(o)]+=1
   rec={"matrix":list(A),"type":t,"order":o,"cycles":C};H.update((json.dumps(rec,sort_keys=True,separators=(",",":"))+"\n").encode());count+=1;assertions+=3+2*o
  obs={k:dict(sorted(hist[k].items(),key=lambda z:int(z[0]))) for k in hist};row=rows[q]
  assert count==q*(q*q-1)==row["pgl_element_count"];assert obs==expected_hist(q,F.p)==row["order_histograms"]==row["theoretical_order_histograms"];assert H.hexdigest()==row["element_record_sha256"]
  assertions+=8;elements+=count;images+=count*(q+1);units+=row["direct_assertion_units"]
 assert elements==d["regression"]["enumerated_pgl_elements"];assert images==d["regression"]["direct_state_images"];assert units==d["regression"]["direct_assertion_units"];return assertions
def main():
 p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=EVIDENCE);p.add_argument("--quick",action="store_true");a=p.parse_args();d=json.loads(a.evidence.read_text())
 if a.quick:preflight(d);print("C260 quick hostile preflight: PASS")
 else: print(f"C260 independent checker: PASS ({validate(d)} assertions; 18 prime-power fields, all projective permutations, cycle types, order censuses, and characteristic-two faces)")
if __name__=="__main__":main()
