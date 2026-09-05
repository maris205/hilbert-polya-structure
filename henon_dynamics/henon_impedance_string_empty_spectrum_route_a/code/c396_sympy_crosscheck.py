#!/usr/bin/env python3
"""Separate symbolic derivations and high-precision operator-action checks."""
if not __debug__: raise RuntimeError("c396 symbolic refuses optimized Python")
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
def run():
    e,p,v,s,z,T,h,theta=sp.symbols("e p v s z T h theta",real=True)
    q=(e-1)/(e+1);identities=[]
    identities.append(sp.expand((p-v)**2+(p+v)**2-2*(p*p+v*v)))
    identities.append(sp.factor((q*q-1)/2+2*e/(e+1)**2))
    identities.append(sp.factor((p+v-q*(p-v)).subs(p,-e*v)))
    identities.append(sp.factor(q+q.subs(e,1/e)))
    P=(s*s+1)/z+2*s/z**2+2/z**3
    identities.append(sp.simplify(z*P-sp.diff(P,s)-(s*s+1)))
    ut=sp.sin(theta*(1-s/T));xt=-theta*sp.cot(theta)/T
    uh=sp.sinh(h*(1-s/T));xh=-h*sp.coth(h)/T
    for u,x,mu in ((ut,xt,theta**2/(T*sp.sin(theta))**2),(uh,xh,h**2/(T*sp.sinh(h))**2),(T-s,-1/T,1/T**2)):
        identities.append(sp.simplify(sp.diff(u,s).subs(s,0)-x*u.subs(s,0)))
        identities.append(sp.trigsimp(-sp.diff(u,s,2)+x*x*u-mu*u))
    assert all(sp.simplify(y)==0 for y in identities)
    mp.mp.dps=100;d=json.loads((ROOT/"results/c396_evidence.json").read_text());actions=0;rayleigh=0;gauge=0;maxres=mp.mpf(0)
    for row in d["pseudospectrum_rows"]:
      tau=mp.mpf(row["tau"][0])/row["tau"][1];param=mp.mpf(row["parameter"][0])/row["parameter"][1]
      x=mp.mpf(row["real_part"])
      if row["branch"]=="trigonometric":u=lambda s:mp.sin(mp.pi*param*(1-s/tau))
      elif row["branch"]=="hyperbolic":u=lambda s:mp.sinh(param*(1-s/tau))
      else:u=lambda s:tau-s
      f=lambda s:x*u(s)-mp.diff(u,s)
      ratio=mp.sqrt(mp.quad(lambda s:u(s)**2,[0,tau])/mp.quad(lambda s:f(s)**2,[0,tau]))
      err=abs(ratio-mp.mpf(row["resolvent_norm"]));maxres=max(maxres,err);assert err<mp.mpf("1e-55");rayleigh+=1
      for sratio in (mp.mpf(1)/5,mp.mpf(1)/2,mp.mpf(4)/5):
        s=tau*sratio;value=mp.quad(lambda r:mp.exp(x*(s-r))*f(r),[s,tau]);err=abs(value-u(s));maxres=max(maxres,err);assert err<mp.mpf("1e-55");actions+=1
        y=mp.mpf(3)/2
        val=mp.quad(lambda r:mp.exp((x+1j*y)*(s-r))*mp.exp(1j*y*r)*f(r),[s,tau])
        err=abs(val-mp.exp(1j*y*s)*u(s));maxres=max(maxres,err);assert err<mp.mpf("1e-55");gauge+=1
    # Complete half-integer singular sequence is analytic; this is a 12-mode regression.
    singular=0
    for n in range(12):
        tau=mp.mpf(2);w=(n+mp.mpf("0.5"))*mp.pi/tau
        f=lambda s:mp.sin(w*s)
        for s in (mp.mpf(1)/3,mp.mpf(4)/3):
            val=mp.quad(f,[s,tau]);assert abs(val-mp.cos(w*s)/w)<mp.mpf("1e-90")
        singular+=1
    out=dict(symbolic_identities=len(identities),rayleigh_rows=rayleigh,volterra_actions=actions,complex_gauge_actions=gauge,singular_modes=singular,max_residual=mp.nstr(maxres,8),working_digits=100,interval_certified=False)
    print("C396 symbolic/high-precision PASS",json.dumps(out,sort_keys=True));return out
if __name__=="__main__":run()
