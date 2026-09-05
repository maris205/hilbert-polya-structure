#!/usr/bin/env python3
"""Independent symbolic identities, ODE integration, and all-mode geometric sums."""
if not __debug__:raise RuntimeError("c386 sympy refuses optimized Python")
import argparse, json
import sympy as S
import mpmath as mp

def symbolic():
    d,M,Q,a=S.symbols("d M Q alpha",positive=True);T=a-Q-M;B=Q-M*d
    C=M*d*d;P=1-d;F=-T-4*M*d
    G=-M*M*d*d*P-B*C+2*B*M*d*P
    k2=4*Q*M-T*T;Xr=d*T/2+M*d*d
    tests=[
      4*(B*M*d*d*(1-d)-Xr**2)-d*d*(k2-4*a*M*d),
      2*(F*Xr+G)-(k2*d-6*a*M*d*d),
      k2-4*a*M+(Q-M-a)**2]
    b,c,p=S.symbols("b c p",real=True)
    dd=1-p*p;mass=b*b+c*c/dd;moment=c*c/dd**2
    energy=(b**4+4*b*b*c*c/dd+c**4*(1+p*p)/dd**3+4*c**3*b*p/dd**2)/4+a*b*b/2
    tests.append(energy-mass**2/4-a*mass/2-moment*dd*((b+c*p/dd)**2-a)/2)
    t,k,ds=S.symbols("t k ds",real=True)
    radial=ds/S.cosh(k*t/2)**2
    tests.extend([S.diff(radial,t)**2-k*k*radial**2*(1-radial/ds),
                  S.diff(radial,t,2)-k*k*radial+S.Rational(3,2)*k*k*radial**2/ds])
    tests.append((k2*(k2/(4*a*M))-6*a*M*(k2/(4*a*M))**2)+k2*k2/(8*a*M))
    r,w=S.symbols("r w",real=True)
    tests.extend([c*c/dd**2-moment,(1-w*moment)-(1-w*c*c/dd**2),
                  (Q-M*d)+M*d+M-(Q+M)])
    # Direct six-real-variable invariant derivatives.
    br,bi,cr,ci,pr,pi,aa=S.symbols("br bi cr ci pr pi aa",real=True)
    bb=br+S.I*bi;cc=cr+S.I*ci;pp=pr+S.I*pi
    B=br*br+bi*bi;C=cr*cr+ci*ci;D=1-pr*pr-pi*pi
    vb=-S.I*((B+2*C/D+aa)*bb+C*cc*S.conjugate(pp)/D**2)
    vc=-S.I*((2*B+C/D**2)*cc+2*bb*C*pp/D)
    vp=-S.I*(cc*S.conjugate(bb)+C*pp/D)
    variables=(br,bi,cr,ci,pr,pi)
    field=[S.re(vb),S.im(vb),S.re(vc),S.im(vc),S.re(vp),S.im(vp)]
    invQ=B+C/D;invM=C/D**2
    invE=(B*B+4*B*C/D+C*C*(1+pr*pr+pi*pi)/D**3+
          4*C*S.re(bb*pp*S.conjugate(cc))/D**2)/4+aa*B/2
    for inv in (invQ,invM,invE):
        tests.append(sum(S.diff(inv,x)*v for x,v in zip(variables,field)))
    for n,expr in enumerate(tests):
        assert S.simplify(S.expand_trig(expr))==0,("symbolic identity",n)
    return len(tests)

def numerical():
    mp.mp.dps=100;ode_rows=0;sum_rows=0;max_error=mp.mpf(0)
    for a in (mp.mpf(1)/4,mp.mpf(1),mp.mpf(4)):
      for direction in (-1,1):
        def rhs(t,state):
            b,c,p=state;B=abs(b)**2;C=abs(c)**2;d=1-abs(p)**2
            return [direction*(-1j)*((B+2*C/d+a)*b+C*c*mp.conj(p)/d**2),
                    direction*(-1j)*((2*B+C/d**2)*c+2*b*C*p/d),
                    direction*(-1j)*(c*mp.conj(b)+C*p/d)]
        solution=mp.odefun(rhs,0,[mp.sqrt(a),mp.mpf(1),mp.mpf(0)],tol=mp.mpf("1e-48"),degree=30)
        for t in (mp.mpf(1)/4,mp.mpf(1)/2):
            b,c,p=solution(t);d=1-abs(p)**2;exact=1/mp.cosh(mp.sqrt(a)*t)**2
            err=abs(d-exact);max_error=max(max_error,err)
            assert err<mp.mpf("1e-42")
            assert abs(abs(c)-d)<mp.mpf("1e-42")
            assert abs(abs(b)**2+abs(c)**2/d-(1+a))<mp.mpf("1e-42")
            assert abs(abs(c)**2/d**2-1)<mp.mpf("1e-42")
            ode_rows+=1
    q=S.symbols("q")
    for exponent in (1,2,4,6):
        expression=1/(1-q)
        for _ in range(exponent):expression=S.factor(q*S.diff(expression,q)+expression)
        closed=S.lambdify(q,expression,"mpmath")
        for denominator in (4,8,16):
            d=mp.mpf(1)/denominator;qq=1-d;N=2048
            direct=mp.fsum((n+1)**exponent*qq**n for n in range(N+1))
            ratio=qq*(mp.mpf(N+3)/(N+2))**exponent
            bound=(N+2)**exponent*qq**(N+1)/(1-ratio)
            difference=abs(closed(qq)-direct)
            assert difference<=bound+mp.mpf("1e-80")
            sum_rows+=1
    return dict(precision_digits=100,independent_ode_rows=ode_rows,geometric_sum_rows=sum_rows,
                max_ode_error=mp.nstr(max_error,8),ode_tolerance="1e-42",interval_certification=False)
def main():
    argparse.ArgumentParser().parse_args()
    count=symbolic();numbers=numerical()
    print("C386 symbolic and numerical PASS",json.dumps(dict(symbolic_identities=count,**numbers),sort_keys=True))
if __name__=="__main__":main()
