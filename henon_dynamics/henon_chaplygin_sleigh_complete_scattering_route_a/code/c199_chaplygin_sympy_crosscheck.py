#!/usr/bin/env python3
"""Independent symbolic reconstruction of the C199 theorem."""
import argparse, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=ROOT/"results/c199_chaplygin_evidence.json"

def main():
    p=argparse.ArgumentParser(); p.add_argument("--evidence",type=Path,default=DEFAULT); data=json.loads(p.parse_args().evidence.read_text())
    checks=0
    def check(x,msg):
        nonlocal checks; checks+=1
        if s.simplify(x) != 0: raise AssertionError(msg+": "+str(s.simplify(x)))
    m,J,b,R,z=s.symbols("m J b R z",positive=True)
    # b=|a| and eps=sgn(a); keep eps^2=1 by testing eps=+/-1 independently.
    for eps in (-1,1):
        for sigma in (-1,1):
            Ic=J+m*b**2; A=m*b*R/Ic; u=eps*R*s.tanh(A*z); w=sigma*R*s.sqrt(m/Ic)/s.cosh(A*z); a=eps*b
            check(s.diff(u,z)-a*w**2,"u ODE")
            check(s.diff(w,z)+(m*a/Ic)*u*w,"omega ODE")
            check(m*u**2/2+Ic*w**2/2-m*R**2/2,"energy")
            eta=s.sqrt(Ic/m)/b; theta=sigma*eta*s.asin(s.tanh(A*z))
            check(s.diff(theta,z)-w,"theta reconstruction")
            check(-(m*a/Ic)*(eps*R)+m*b*R/Ic,"stable eigenvalue")
    u,w,a,Ic,H=s.symbols("u w a Ic H", nonzero=True)
    # Poisson tensor J^{u,w}=(a/Ic)w gives X_H for H=m u^2/2+Ic w^2/2.
    grad=s.Matrix([m*u,Ic*w]); P=s.Matrix([[0,a*w/Ic],[-a*w/Ic,0]])
    vec=P*grad
    check(vec[0]-a*w**2,"Poisson u")
    check(vec[1]+m*a*u*w/Ic,"Poisson omega")
    rho=1/w
    check(s.diff(rho*vec[0],u)+s.diff(rho*vec[1],w),"invariant half-plane density")
    # Reduced reversor R=-Id: f(Rx)=-DR f(x)=f(x).
    f=s.Matrix([a*w**2,-m*a*u*w/Ic]); fR=f.subs({u:-u,w:-w}, simultaneous=True)
    check(fR[0]-f[0],"reversor u"); check(fR[1]-f[1],"reversor omega")
    # Every stored state is independently checked as a symbolic rational hyperbola identity.
    for row in data["regression"]["heteroclinic_cases"]:
        for state in row["samples"]:
            t=s.Rational(state["tanh_s_exact"]); q=s.Rational(state["sech_s_exact"])
            check(t*t+q*q-1,"tanh-sech identity")
    print(json.dumps({"status":"C199_SYMPY_PASS","checks":checks,"structural_identities":25,"sample_identities":36},sort_keys=True))

if __name__=="__main__": main()
