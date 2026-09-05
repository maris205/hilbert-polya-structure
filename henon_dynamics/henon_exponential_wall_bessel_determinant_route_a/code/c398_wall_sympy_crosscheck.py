#!/usr/bin/env python3
"""Independent Bessel quadrature, ODE, spectral roots and trace normalization."""
if not __debug__:
    raise RuntimeError("c398 symbolic refuses optimized Python")
import sympy as s
import mpmath as mp
mp.mp.dps=70
E,a=s.symbols('E a',positive=True)
J=2*(s.sqrt(E)*s.acosh(s.sqrt(E)/a)-s.sqrt(E-a*a))
assert s.simplify(s.diff(J,E)-s.acosh(s.sqrt(E)/a)/s.sqrt(E))==0
constant=s.simplify((s.polygamma(0,s.Rational(3,2))+2*(s.log(2/a)-1))/4)
assert s.simplify(constant-(-s.EulerGamma-2*s.log(a))/4)==0
assert s.gamma(s.Rational(3,2))==s.sqrt(s.pi)/2
cases=0
for av in (mp.mpf('.5'),mp.mpf(1),mp.mpf(2)):
    for k in (mp.mpf(2),mp.mpf(8),mp.mpf(16)):
        K=mp.besselk(1j*k,av);I=mp.besseli(-1j*k,av)
        assert abs(K-mp.pi*mp.im(I)/mp.sinh(mp.pi*k))<mp.mpf('1e-60')
        S=mp.hyp0f1(1-1j*k,av*av/4)
        assert abs(I-(av/2)**(-1j*k)/mp.gamma(1-1j*k)*S)<mp.mpf('1e-55')
        b=av*av/4
        assert abs(S-1)<=mp.exp(b/k)-1
        assert abs(mp.diff(lambda t:mp.hyp0f1(1-1j*t,b),k))<=b*mp.exp(b/k)/(k*k)
        x=mp.mpf('.3');fun=lambda xx:mp.besselk(1j*k,av*mp.exp(xx))
        assert abs(-mp.diff(fun,x,2)+(av*av*mp.exp(2*x)-k*k)*fun(x))<mp.mpf('1e-55')
        cases+=1
    # Direct K integral is an independent representation, not a second call to hyp0f1.
    k=mp.mpf(3);upper=mp.acosh(180/av)
    integral=mp.quad(lambda t:mp.exp(-av*mp.cosh(t))*mp.cos(k*t),[0,1,2,upper])
    assert abs(integral-mp.besselk(1j*k,av))<mp.mpf('1e-55')
    # Find four bracketed source roots; completeness is supplied by the analytic theorem, not this scan.
    f=lambda k:mp.re(mp.exp(mp.pi*k/2)*mp.besselk(1j*k,av))
    roots=[];left=av;fl=f(left)
    for step in range(1,321):
        right=av+mp.mpf(step)/8;fr=f(right)
        if fl*fr<0:
            lo,hi=left,right;flo=fl
            for j in range(190):
                mid=(lo+hi)/2;fm=f(mid)
                if flo*fm<=0:hi=mid
                else:lo=mid;flo=fm
            root=(lo+hi)/2;roots.append(root)
            assert abs(f(root))<mp.mpf('1e-50')
            if len(roots)==4:break
        left,fl=right,fr
    assert len(roots)==4 and all(roots[j+1]>roots[j] for j in range(3))
    k=roots[0];en=k*k
    boundary_derivative=mp.diff(lambda ee:mp.besselk(mp.sqrt(-ee),av),en)
    argument_derivative=mp.diff(lambda zz:mp.besselk(1j*k,zz),av)
    norm=-av*argument_derivative*boundary_derivative
    xmax=mp.log(180/av)
    direct=mp.quad(lambda xx:mp.re(mp.besselk(1j*k,av*mp.exp(xx)))**2,[0,1,xmax])
    assert mp.re(norm)>0 and abs(norm-direct)<mp.mpf('1e-48')
    print('C398 finite source root regression: a='+str(av)+' roots='+','.join(mp.nstr(v,16) for v in roots),flush=True)
# Check logarithmic determinant derivative against the full resolvent diagonal integral.
av=mp.mpf(1);en=mp.mpf(-1)/4
# Half-integer Bessel formulas simplify the SAME full resolvent diagonal,
# avoiding very expensive I*K evaluation at quadrature nodes near infinity.
trace=mp.quad(lambda zz:(1-mp.exp(-2*(zz-av)))/(2*zz*zz),[av,2,10,mp.inf])
assert abs(trace-mp.exp(2*av)*mp.e1(2*av))<mp.mpf('1e-60')
log_derivative=-mp.diff(lambda ee:mp.log(mp.besselk(mp.sqrt(-ee),av)),en)
assert abs(trace-log_derivative)<mp.mpf('1e-50')
print('C398 symbolic/high-precision PASS: 3 symbolic identities; 9 series/ODE cases; 3 direct integrals; 12 bracketed roots; 3 norm identities; 1 full resolvent trace; dps=70; numerical regression not interval certification')
