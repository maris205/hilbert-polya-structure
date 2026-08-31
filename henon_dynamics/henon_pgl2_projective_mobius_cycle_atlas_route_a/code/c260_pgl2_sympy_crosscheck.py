#!/usr/bin/env python3
"""Independent symbolic identities for the PGL2 cycle atlas."""
import math
import sympy as sp
a,b,c,d,t,x=sp.symbols("a b c d t x"); A=sp.Matrix([[a,b],[c,d]]);tr=a+d;det=a*d-b*c;checks=0
assert (A**2-tr*A+det*sp.eye(2)).applyfunc(sp.expand)==sp.zeros(2);checks+=1
C=sp.Matrix([[0,-det],[1,tr]]);H=sp.Matrix([[0,det],[1,0]])
assert (H*C*H.inv()-det*C.inv()).applyfunc(sp.simplify)==sp.zeros(2);checks+=1
assert (H**2-det*sp.eye(2)).applyfunc(sp.simplify)==sp.zeros(2);checks+=1
for L in range(1,17):
 P=sp.zeros(L)
 for j in range(L):P[(j+1)%L,j]=1
 assert sp.simplify((sp.eye(L)-t*P).det()-(1-t**L))==0
 assert P.T*P==sp.eye(L)
 checks+=2
for q in [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32]:
 split=sum(q*(q+1)*sp.totient(e)//2 for e in sp.divisors(q-1) if e>1)
 nonsplit=sum(q*(q-1)*sp.totient(e)//2 for e in sp.divisors(q+1) if e>1)
 assert sp.simplify(1+(q*q-1)+split+nonsplit-q*(q*q-1))==0
 assert sum(sp.totient(e) for e in sp.divisors(q-1))==q-1
 assert sum(sp.totient(e) for e in sp.divisors(q+1))==q+1
 checks+=3
for q,p,d0,kind in [(9,3,4,"split"),(9,3,5,"nonsplit"),(16,2,5,"split"),(16,2,17,"nonsplit"),(25,5,8,"split"),(25,5,13,"nonsplit")]:
 if kind=="split": cyc=[1,1]+[d0]*((q-1)//d0)
 else:cyc=[d0]*((q+1)//d0)
 for n in range(1,2*d0+1):
  fixed=sum(L for L in cyc if n%L==0)
  expected=(2+(q-1)*(n%d0==0)) if kind=="split" else (q+1)*(n%d0==0)
  assert fixed==expected;checks+=1
print(f"C260_SYMPY_PASS ({checks} symbolic/algebraic identities; Cayley--Hamilton, reversor, cycle determinants, census closure, and fixed ledgers)")
