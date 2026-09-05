#!/usr/bin/env python3
"""Independent symbolic identities and high-precision Green/Stone regression."""
if not __debug__: raise RuntimeError("c391 symbolic refuses optimized Python")
import json
import sympy as sp
import mpmath as mp
def run():
    x,p,g,t=sp.symbols("x p g t",real=True,nonzero=True)
    h=p*p-g/x**2;y=x*x+4*x*p*t+4*h*t*t
    identities=[sp.diff(y,t,2)-8*h,(4*x*p)**2-16*x*x*h-16*g,
                2*p*sp.diff(h,x)-2*g/x**3*sp.diff(h,p),
                sp.expand(sp.diff(y,t)**2-16*(h*y+g))]
    a,b,u,v=sp.symbols("a b u v",real=True)
    T=u+sp.I*v;num=a-T*b;den=b-T*a
    identities.append(sp.expand(num*sp.conjugate(num)-den*sp.conjugate(den)-(a*a-b*b)*(1-u*u-v*v)))
    z=sp.symbols("z");identities.append(sp.factor(sp.diff((a-z*b)/(b-z*a),z)-(a*a-b*b)/(b-z*a)**2))
    s=sp.symbols("s",positive=True);j,theta=sp.symbols("j theta",real=True)
    loge=sp.log(4)-(theta+2*sp.pi*j)/s
    identities.append(sp.simplify(loge.subs(j,j+1)-loge+2*sp.pi/s))
    aa,bb=sp.symbols("aa bb",positive=True)
    norm=sp.pi*sp.sin(s*sp.log(aa/bb))/((aa**2-bb**2)*sp.sinh(sp.pi*s))
    identities.append(sp.simplify(sp.limit(norm,bb,aa)-sp.pi*s/(2*aa**2*sp.sinh(sp.pi*s))))
    for value in identities:assert sp.simplify(value)==0,value
    mp.mp.dps=100;stone=0;wronskians=0;odes=0;boundary=0;norms=0;periods=0
    def near(a,b,tol="1e-85"):assert abs(a-b)<mp.mpf(tol)*max(1,abs(b)),(a,b)
    for sigma in (mp.mpf("0.5"),mp.mpf(1),mp.mpf(2)):
      integ=mp.quad(lambda r:r*mp.besselk(1j*sigma,r)**2,[0,1,mp.inf])
      near(integ,mp.pi*sigma/(2*mp.sinh(mp.pi*sigma)),"1e-75");norms+=1
      for phase in (mp.mpf(0),mp.mpf(1)/3,mp.mpf(1),mp.mpf(5)/3):
        vs=mp.exp(1j*mp.pi*phase);kappa=vs*mp.gamma(1j*sigma)/mp.gamma(-1j*sigma)
        a=mp.exp(mp.pi*sigma/2);b=1/a
        def phi(k,x):
            T=vs*mp.exp(2j*sigma*mp.log(k/2))
            return mp.exp(-1j*mp.pi/4)*mp.sqrt(k*x)*(mp.besselj(1j*sigma,k*x)-T*mp.besselj(-1j*sigma,k*x))/(b-T*a)
        def green(rho,x,y):
            T=vs*mp.exp(2j*sigma*mp.log(rho/2))
            small=min(x,y);large=max(x,y)
            return mp.sqrt(small)*(mp.besseli(1j*sigma,rho*small)-T*mp.besseli(-1j*sigma,rho*small))*mp.sqrt(large)*mp.besselk(1j*sigma,rho*large)/(1-T)
        for k in (mp.mpf(1)/3,mp.mpf(1),mp.mpf(3)):
          for xx,yy in ((mp.mpf("0.7"),mp.mpf("1.3")),(mp.mpf("1.3"),mp.mpf("0.7")),(mp.mpf("0.7"),mp.mpf("0.7"))):
            density=k/(mp.pi*1j)*(green(-1j*k,xx,yy)-green(1j*k,xx,yy))
            near(density,phi(k,xx)*mp.conj(phi(k,yy)));stone+=1
          def refl(k):
            T=vs*mp.exp(2j*sigma*mp.log(k/2));return -1j*(a-T*b)/(b-T*a)
          near(refl(k),refl(k*mp.exp(mp.pi/sigma)));periods+=1
        rho=mp.mpc("1.3","0.2");T=vs*mp.exp(2j*sigma*mp.log(rho/2));xx=mp.mpf("0.7")
        U=lambda r:mp.sqrt(r)*(mp.besseli(1j*sigma,rho*r)-T*mp.besseli(-1j*sigma,rho*r))
        V=lambda r:mp.sqrt(r)*mp.besselk(1j*sigma,rho*r)
        near(U(xx)*mp.diff(V,xx)-mp.diff(U,xx)*V(xx),T-1);wronskians+=1
        near(-mp.diff(V,xx,2)-(sigma*sigma+mp.mpf(1)/4)/xx**2*V(xx),-rho*rho*V(xx));odes+=1
        tiny=mp.mpf("1e-30")
        expected=(kappa*tiny**(-1j*sigma)+tiny**(1j*sigma))*(rho/2)**(1j*sigma)/mp.gamma(1+1j*sigma)
        near(U(tiny)/mp.sqrt(tiny),expected,"1e-55");boundary+=1
    report=dict(symbolic_identities=len(identities),stone_jump_cells=stone,green_wronskians=wronskians,
                bessel_ode_cells=odes,boundary_matching_cells=boundary,normalization_integrals=norms,log_period_cells=periods,
                working_digits=100,interval_certified=False)
    print("C391 symbolic/high-precision PASS",json.dumps(report,sort_keys=True));return report
if __name__=="__main__":run()
