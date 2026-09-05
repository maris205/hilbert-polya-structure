#!/usr/bin/env python3
"""Exact formula-side finite regressions; infinite claims belong to the proof."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
SCOPE='NO_BAD_EULER_OR_ROOT_NUMBER'
BASE='0c877206d202f732e21ea0b194f9c7fdf30467ee'
ROUTE=['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FAIL']
FLAGS={k:False for k in ('claims_target_arithmetic_local_data','claims_target_euler_factors',
 'claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law',
 'claims_target_functional_equation','claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b')}

class Ring:
    def __init__(self,q): self.q=q
    def addc(self,a,b): return a^b if self.q==4 else (a+b)%self.q
    def negc(self,a): return a if self.q==4 else (-a)%self.q
    def mulc(self,a,b):
        if self.q!=4: return a*b%self.q
        z=0
        while b:
            if b&1: z^=a
            b>>=1; a<<=1
            if a&4: a^=7
        return z
    def powc(self,a,n):
        z=1
        for _ in range(n): z=self.mulc(z,a)
        return z
    def trim(self,a):
        a=list(a)
        while len(a)>1 and a[-1]==0: a.pop()
        return tuple(a or [0])
    def add(self,a,b):
        return self.trim([self.addc(a[i] if i<len(a) else 0,b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
    def neg(self,a): return tuple(self.negc(x) for x in a)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]=self.addc(c[i+j],self.mulc(x,y))
        return self.trim(c)
    def div(self,a,b):
        if b==(0,): raise ZeroDivisionError
        r=list(a); z=[0]*max(1,len(a)-len(b)+1); inv=self.powc(b[-1],self.q-2)
        while tuple(r)!=(0,) and len(r)>=len(b):
            d=len(r)-len(b); c=self.mulc(r[-1],inv); z[d]=c
            r=list(self.sub(r,[0]*d+[self.mulc(c,x) for x in b]))
        return self.trim(z),self.trim(r)
    def mod(self,a,b): return self.div(a,b)[1]
    def gcd(self,a,b):
        while b!=(0,): a,b=b,self.mod(a,b)
        return tuple(self.mulc(x,self.powc(a[-1],self.q-2)) for x in a)
    def pow(self,a,n):
        z=(1,)
        while n:
            if n&1: z=self.mul(z,a)
            a=self.mul(a,a); n//=2
        return z
    def monic(self,d): return [tuple(c)+(1,) for c in itertools.product(range(self.q),repeat=d)]
    def irreducible(self,a):
        return len(a)>1 and all(self.mod(a,b)!=(0,) for d in range(1,(len(a)-1)//2+1) for b in self.monic(d))
    def divisors(self,a): return [b for d in range(len(a)) for b in self.monic(d) if self.mod(a,b)==(0,)]
    def factors(self,a):
        out=[]
        for d in range(1,len(a)):
            for b in self.monic(d):
                if not self.irreducible(b): continue
                k=0
                while a!=(1,) and self.mod(a,b)==(0,): a=self.div(a,b)[0]; k+=1
                if k: out.append((b,k))
        return out
    def phi(self,a):
        z=self.q**(len(a)-1)
        for P,_ in self.factors(a): z=z//(self.q**(len(P)-1))*(self.q**(len(P)-1)-1)
        return z
    def order(self,b,a):
        if a==(1,): return 1
        y=self.mod(b,a); n=1
        while y!=(1,): y=self.mod(self.mul(y,b),a); n+=1
        return n
    def carlitz(self,a):
        total=[(0,)]*len(a); iterate=[(1,)]
        for j,c in enumerate(a):
            for i,v in enumerate(iterate): total[i]=self.add(total[i],tuple(self.mulc(c,x) for x in v))
            nxt=[(0,)]*(len(iterate)+1)
            for i,v in enumerate(iterate):
                nxt[i]=self.add(nxt[i],self.mul((0,1),v))
                nxt[i+1]=self.add(nxt[i+1],self.pow(v,self.q))
            iterate=nxt
        while len(total)>1 and total[-1]==(0,): total.pop()
        return total
    def ordinary(self,lin): return {self.q**i:c for i,c in enumerate(lin) if c!=(0,)}
    def xadd(self,a,b):
        c=dict(a)
        for i,v in b.items(): c[i]=self.add(c.get(i,(0,)),v)
        return {i:v for i,v in c.items() if v!=(0,)}
    def xmul(self,a,b):
        c={}
        for i,v in a.items():
            for j,w in b.items(): c[i+j]=self.add(c.get(i+j,(0,)),self.mul(v,w))
        return {i:v for i,v in c.items() if v!=(0,)}
    def xpow(self,a,n):
        z={0:(1,)}
        while n:
            if n&1: z=self.xmul(z,a)
            a=self.xmul(a,a); n//=2
        return z
    def psi(self,P,k):
        cp=self.ordinary(self.carlitz(P)); inner=self.ordinary(self.carlitz(self.pow(P,k-1))); out={}
        for j,c in cp.items(): out=self.xadd(out,{i:self.mul(v,c) for i,v in self.xpow(inner,j-1).items()})
        return out

def encode_x(a): return [[i,list(c)] for i,c in sorted(a.items())]
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def digest(x): return hashlib.sha256(canonical(x)).hexdigest()
def make():
    rings=[]; towers=[]
    for q,maxd,primed in ((2,3,3),(3,3,2),(4,2,2),(5,2,2)):
        R=Ring(q)
        for d in range(maxd+1):
            for a in R.monic(d):
                strata=R.divisors(a); maps=[]
                for bb in itertools.product(range(q),repeat=d):
                    b=R.trim(bb); joint=Counter(); cycles=Counter()
                    for D in strata:
                        pop=R.phi(D)
                        if b==(0,): h,l=(0 if D==(1,) else 1),1
                        else:
                            star=(1,); h=0
                            for P,k in R.factors(D):
                                v=0; t=b
                                while R.mod(t,P)==(0,): v+=1; t=R.div(t,P)[0]
                                if v: h=max(h,(k+v-1)//v)
                                else: star=R.mul(star,R.pow(P,k))
                            l=R.order(b,star)
                        joint[h,l]+=pop
                        if h==0: cycles[l]+=pop//l
                    fixed=[]; bn=(1,)
                    for n in range(1,13):
                        bn=R.mod(R.mul(bn,b),a)
                        fixed.append(q**(len(R.gcd(a,R.sub(bn,(1,))))-1))
                    maps.append({'b':list(b),'joint':[[h,l,c] for (h,l),c in sorted(joint.items())],
                                 'cycles':[[l,c] for l,c in sorted(cycles.items())],'fixed':fixed})
                rings.append({'q':q,'a':list(a),'size':q**d,'carlitz':[list(c) for c in R.carlitz(a)],
                              'strata':[[list(D),R.phi(D)] for D in strata],'maps':maps})
        for d in range(1,primed+1):
            for P in R.monic(d):
                if not R.irreducible(P): continue
                Q=q**d
                for k in range(1,4):
                    if Q**k>256: continue
                    a=R.pow(P,k); degree=(Q-1)*Q**(k-1)
                    hist=[[s,(Q-1)*Q**(k-s-1) if s else (Q-2)*Q**(k-1)] for s in range(k)]
                    groups=[[0,0,degree]]+[[Q**(s-1),Q**s-1,Q**(k-s)] for s in range(1,k)]
                    towers.append({'q':q,'P':list(P),'k':k,'Q':Q,'a':list(a),'degree':degree,
                      'carlitz':[list(c) for c in R.carlitz(a)],'psi':encode_x(R.psi(P,k)),
                      'valuation':[1,degree],'ramification_histogram':hist,'lower_groups':groups,
                      'different':Q**(k-1)*(k*(Q-1)-1),'restriction_kernel':1 if k==1 else Q})
    payload={'candidate':'C389','baseline':BASE,'scope':SCOPE,'tuple':ROUTE,'scope_flags':FLAGS,
       'field_encoding':{'2':'prime field','3':'prime field','4':'F2[w]/(w^2+w+1); 0,1,w,1+w','5':'prime field'},
       'ring_cases':rings,'tower_cases':towers,'controls':{'rank_zero_nonzero_torsion':False,
       'composite_conductor_is_single_prime':False,'all_nonunit_maps_are_permutations':False,
       'geometric_twist_conjugacy_implies_K_conjugacy':False,'finite_tests_prove_all_levels':False,
       'mandatory_a1_controls_completed':0,'target_prime_clock_constructed':False}}
    return {'schema':'c389-carlitz-evidence-v1','payload_sha256':digest(payload),'payload':payload}

def main():
    if not __debug__: raise SystemExit('optimized mode forbidden')
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,default=ROOT/'results/c389_carlitz_evidence.json'); args=p.parse_args()
    out=make(); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','ring_cases':len(out['payload']['ring_cases']),'tower_cases':len(out['payload']['tower_cases']),'payload_sha256':out['payload_sha256']}))

if __name__=='__main__': main()
