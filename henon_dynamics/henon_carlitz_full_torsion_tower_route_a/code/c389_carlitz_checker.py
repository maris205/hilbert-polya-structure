#!/usr/bin/env python3
"""Independent right-composition and explicit functional-graph reconstruction."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def need(ok,msg):
    global COUNT
    COUNT+=1
    if not ok: raise ValueError(msg)
def same(got,want,path='$'):
    need(type(got) is type(want),'type '+path)
    if type(want) is dict:
        need(set(got)==set(want),'keys '+path)
        for k,v in want.items(): same(got[k],v,path+'.'+k)
    elif type(want) is list:
        need(len(got)==len(want),'length '+path)
        for i,v in enumerate(want): same(got[i],v,path+'['+str(i)+']')
    else: need(got==want,'value '+path)
def load(path):
    def pairs(items):
        d={}
        for k,v in items:
            need(k not in d,'duplicate JSON key'); d[k]=v
        return d
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON')))

class Algebra:
    def __init__(self,q): self.q=q
    def plus(self,x,y): return x^y if self.q==4 else (x+y)%self.q
    def times(self,x,y):
        return ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))[x][y] if self.q==4 else x*y%self.q
    def minus(self,x): return x if self.q==4 else -x%self.q
    def norm(self,x):
        x=list(x)
        while x and x[-1]==0: x.pop()
        return tuple(x or [0])
    def sum(self,x,y):
        z=list(x)+[0]*max(0,len(y)-len(x))
        for i,b in enumerate(y): z[i]=self.plus(z[i],b)
        return self.norm(z)
    def neg(self,x): return tuple(self.minus(a) for a in x)
    def product(self,x,y):
        out=(0,)
        for i,c in enumerate(x): out=self.sum(out,(0,)*i+tuple(self.times(c,b) for b in y))
        return out
    def quotient(self,x,y):
        z=[0]*max(1,len(x)-len(y)+1); rem=x
        inv=next(c for c in range(1,self.q) if self.times(c,y[-1])==1)
        while rem!=(0,) and len(rem)>=len(y):
            shift=len(rem)-len(y); coeff=self.times(rem[-1],inv); z[shift]=coeff
            rem=self.sum(rem,(0,)*shift+tuple(self.minus(self.times(coeff,c)) for c in y))
        return self.norm(z),rem
    def remainder(self,x,y): return self.quotient(x,y)[1]
    def gcd(self,x,y):
        while y!=(0,): x,y=y,self.remainder(x,y)
        inv=next(c for c in range(1,self.q) if self.times(c,x[-1])==1)
        return tuple(self.times(c,inv) for c in x)
    def power(self,x,n):
        y=(1,)
        for _ in range(n): y=self.product(y,x)
        return y
    def polynomials(self,d,monic=True):
        return [self.norm(t+(1,)) if monic else self.norm(t) for t in itertools.product(range(self.q),repeat=d)]
    def prime(self,P):
        return all(self.remainder(P,D)!=(0,) for j in range(1,(len(P)-1)//2+1) for D in self.polynomials(j))
    def linearized(self,a):
        current=[(1,)]; ans=[(0,)]*len(a)
        for coeff in a:
            for j,c in enumerate(current): ans[j]=self.sum(ans[j],tuple(self.times(coeff,t) for t in c))
            nxt=[(0,)]*(len(current)+1)
            for j,c in enumerate(current):
                nxt[j]=self.sum(nxt[j],(0,)*(self.q**j)+c)
                nxt[j+1]=self.sum(nxt[j+1],c)
            current=nxt
        while len(ans)>1 and ans[-1]==(0,): ans.pop()
        return ans
    def xquotient(self,top,bottom):
        rem=dict(top); result={}; degree=max(bottom)
        need(bottom[degree]==(1,),'monic denominator')
        while rem and max(rem)>=degree:
            j=max(rem)-degree; coeff=rem[max(rem)]; result[j]=coeff
            for k,c in bottom.items():
                value=self.sum(rem.get(j+k,(0,)),self.neg(self.product(coeff,c)))
                if value==(0,): rem.pop(j+k,None)
                else: rem[j+k]=value
        need(not rem,'primitive quotient remainder')
        return result
    def xpoly(self,a): return {self.q**i:c for i,c in enumerate(self.linearized(a)) if c!=(0,)}

@lru_cache(maxsize=1)
def reconstruct():
    rings=[]; towers=[]
    for q,md,pd in ((2,3,3),(3,3,2),(4,2,2),(5,2,2)):
        B=Algebra(q)
        for d in range(md+1):
            for a in B.polynomials(d):
                points=B.polynomials(d,False); strata=Counter(); maps=[]
                for x in points:
                    D=B.quotient(a,B.gcd(a,x))[0]; strata[D]+=1
                ordered=sorted(strata,key=lambda v:(len(v),v))
                for b in points:
                    image={x:B.remainder(B.product(b,x),a) for x in points}; joint=Counter(); cp=Counter()
                    for x in points:
                        orbit={}; y=x
                        while y not in orbit: orbit[y]=len(orbit); y=image[y]
                        h,l=orbit[y],len(orbit)-orbit[y]; joint[h,l]+=1
                        if h==0: cp[l]+=1
                    fixed=[]; iterate=dict(zip(points,points))
                    for _ in range(12):
                        iterate={x:image[iterate[x]] for x in points}
                        fixed.append(sum(iterate[x]==x for x in points))
                    maps.append({'b':list(b),'joint':[[h,l,c] for (h,l),c in sorted(joint.items())],
                                 'cycles':[[l,c//l] for l,c in sorted(cp.items())],'fixed':fixed})
                rings.append({'q':q,'a':list(a),'size':len(points),'carlitz':[list(c) for c in B.linearized(a)],
                              'strata':[[list(D),strata[D]] for D in ordered],'maps':maps})
        for d in range(1,pd+1):
            for P in B.polynomials(d):
                if not B.prime(P): continue
                Q=q**d
                reduced={i:B.remainder(c,P) for i,c in B.xpoly(P).items()}
                need(all(c==(0,) for i,c in reduced.items() if i!=Q) and reduced[Q]==(1,),'critical reduction')
                for k in range(1,4):
                    if Q**k>256: continue
                    a=B.power(P,k); degree=Q**k-Q**(k-1)
                    psi=B.xquotient(B.xpoly(a),B.xpoly(B.power(P,k-1)))
                    need(psi.get(0)==P and psi[max(psi)]==(1,) and max(psi)==degree,'primitive degree/constant')
                    need(all(B.remainder(c,P)==(0,) for i,c in psi.items() if i<degree),'Eisenstein coefficients')
                    hist=Counter(); unit_count=0
                    for x in B.polynomials(d*k,False):
                        if B.gcd(x,P)!=(1,): continue
                        unit_count+=1; y=B.sum(x,B.neg((1,)))
                        if y==(0,): continue
                        s=0
                        while B.remainder(y,P)==(0,): s+=1; y=B.quotient(y,P)[0]
                        hist[s]+=1
                    need(unit_count==degree,'full unit group size')
                    groups=[[0,0,unit_count]]
                    for s in range(1,k):
                        size=1+sum(v for j,v in hist.items() if j>=s)
                        groups.append([Q**(s-1),Q**s-1,size])
                    different=sum((hi-lo+1)*(size-1) for lo,hi,size in groups)
                    towers.append({'q':q,'P':list(P),'k':k,'Q':Q,'a':list(a),'degree':degree,
                        'carlitz':[list(c) for c in B.linearized(a)],'psi':[[i,list(c)] for i,c in sorted(psi.items())],
                        'valuation':[1,degree],'ramification_histogram':[[s,hist[s]] for s in range(k)],
                        'lower_groups':groups,'different':different,'restriction_kernel':1 if k==1 else Q})
    return {'candidate':'C389','baseline':'0c877206d202f732e21ea0b194f9c7fdf30467ee',
       'scope':'NO_BAD_EULER_OR_ROOT_NUMBER','tuple':['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FAIL'],
       'scope_flags':{k:False for k in ('claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number',
          'claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation','claims_target_zero_match',
          'claims_hilbert_polya_operator','invokes_route_b')},
       'field_encoding':{'2':'prime field','3':'prime field','4':'F2[w]/(w^2+w+1); 0,1,w,1+w','5':'prime field'},
       'ring_cases':rings,'tower_cases':towers,'controls':{'rank_zero_nonzero_torsion':False,
       'composite_conductor_is_single_prime':False,'all_nonunit_maps_are_permutations':False,
       'geometric_twist_conjugacy_implies_K_conjugacy':False,'finite_tests_prove_all_levels':False,
       'mandatory_a1_controls_completed':0,'target_prime_clock_constructed':False}}

def check(path):
    data=load(path); need(type(data) is dict and set(data)=={'schema','payload_sha256','payload'},'envelope')
    need(data['schema']=='c389-carlitz-evidence-v1','schema')
    raw=json.dumps(data['payload'],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    need(type(data['payload_sha256']) is str and hashlib.sha256(raw).hexdigest()==data['payload_sha256'],'payload hash')
    same(data['payload'],reconstruct())
    return {'status':'PASS','assertions':COUNT,'ring_cases':len(data['payload']['ring_cases']),
            'tower_cases':len(data['payload']['tower_cases']),'payload_sha256':data['payload_sha256']}

def main():
    if not __debug__: raise SystemExit('optimized mode forbidden')
    p=argparse.ArgumentParser(); p.add_argument('--evidence',type=Path,default=ROOT/'results/c389_carlitz_evidence.json'); args=p.parse_args()
    print(json.dumps(check(args.evidence),sort_keys=True))
if __name__=='__main__': main()
