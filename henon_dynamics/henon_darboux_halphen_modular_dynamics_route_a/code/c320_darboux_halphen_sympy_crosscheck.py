#!/usr/bin/env python3
"""Algebraic differential-identity cross-checks for HCS-C320."""
import sys
import sympy as s
if sys.flags.optimize: raise RuntimeError("C320 SymPy lane refuses optimized Python")
x,y,z,c,u=s.symbols("x y z c u")
f=[y*z-x*(y+z),z*x-y*(z+x),x*y-z*(x+y)]
vars=(x,y,z)
def L(expr): return s.expand(sum(s.diff(expr,v)*fv for v,fv in zip(vars,f)))
S=x+y+z; S1=L(S);S2=L(S1);S3=L(S2)
D=(x-y)*(y-z)*(z-x)
checks=[s.factor(S3+4*S*S2-6*S1**2),s.factor(L(D)+2*S*D)]
# Common affine shift/weight-two covariance, u'=c and (gamma*tau)'=u^-2.
X=[s.symbols(f"X{i}") for i in range(3)]
a=s.symbols("a")
for i,(j,k) in enumerate(((1,2),(2,0),(0,1))):
    transformed=s.expand((X[j]/u**2+c/u)*(X[k]/u**2+c/u)-(X[i]/u**2+c/u)*((X[j]+X[k])/u**2+2*c/u))
    derivative=s.expand(f[i].subs({x:X[0],y:X[1],z:X[2]})/u**4-2*c*X[i]/u**3-c**2/u**2)
    checks.append(s.factor(transformed-derivative))
t,C=s.symbols("t C"); aa=1/t;bb=1/t+C/t**2
checks += [s.factor(s.diff(aa,t)+aa**2),s.factor(s.diff(bb,t)-(aa**2-2*aa*bb))]
for axis_point in ((0,0,C),(C,0,0),(0,C,0)):
    checks.extend(s.factor(expr.subs({x:axis_point[0],y:axis_point[1],z:axis_point[2]})) for expr in f)
if any(v!=0 for v in checks):raise AssertionError(checks)
count=len(checks)
def product_coeff(component,k):
    value=s.Rational(-1,2) if component==0 and k==0 else s.Integer(0)
    if k==0:return value
    for n in range(1,k//2+1):
        if k%(2*n)==0:
            r=k//(2*n)
            value += (4*n-8*n*(-1)**(r-1)) if component==0 else 4*n
        odd=2*n-1
        if component>0 and k%odd==0:
            r=k//odd
            value += -4*odd*(-1)**(r-1) if component==1 else 4*odd
    return s.Integer(value)
for k in range(129):
    expected=-s.Rational(1,2) if k==0 else 12*s.divisor_sigma(k//2) if k%2==0 else 0
    if s.simplify(sum(product_coeff(j,k) for j in range(3))-expected)!=0:raise AssertionError(f"E2 bridge {k}")
    count+=1
for k in range(1,101):
    subs={x:s.Rational(k,7),y:s.Rational(k+1,11),z:s.Rational(2*k-1,13)}
    if s.factor((S3+4*S*S2-6*S1**2).subs(subs))!=0 or s.factor((L(D)+2*S*D).subs(subs))!=0:raise AssertionError("specialization")
    count+=2
print(f"C320 SymPy cross-check: PASS ({count} exact identities)")
