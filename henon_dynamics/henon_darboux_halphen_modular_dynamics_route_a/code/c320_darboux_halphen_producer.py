#!/usr/bin/env python3
"""Produce exact and high-precision receipts for HCS-C320."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c320_darboux_halphen_evidence.json"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
ORDER = 128
EVAL_RAW = "ec086cb94fd2131f75bf138675e4fa2ca1ad2b8331f01f03b9159c069541b220"
EVAL_SEMANTIC = "843b788e9bbfcbbfbd0e6c926921dba4efe05ef35c6e1464c6f085478fa9b25f"
mp.mp.dps = 90

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}

def fs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def cs(z) -> dict:
    return {"re": mp.nstr(mp.re(z), 72, strip_zeros=False), "im": mp.nstr(mp.im(z), 72, strip_zeros=False)}

def theta_polynomials(order: int):
    a2 = [Fraction(0) for _ in range(order + 1)]
    a3 = [Fraction(0) for _ in range(order + 1)]
    a4 = [Fraction(0) for _ in range(order + 1)]
    for k in range(order + 1):
        n = 0
        while n * (n + 1) <= k:
            if n * (n + 1) == k: a2[k] += 1
            n += 1
        n = 1
        while n * n <= k:
            if n * n == k:
                a3[k] += 2
                a4[k] += 2 * ((-1) ** n)
            n += 1
    a2[0] = 1; a3[0] = 1; a4[0] = 1
    return a2, a3, a4

def qlog(a):
    order = len(a) - 1
    numerator = [Fraction(k) * a[k] for k in range(order + 1)]
    out = [Fraction(0) for _ in range(order + 1)]
    for k in range(order + 1):
        out[k] = numerator[k] - sum(a[j] * out[k-j] for j in range(1, k+1))
    return out

def convolution(a, b, k): return sum(a[j] * b[k-j] for j in range(k+1))

def sigma1(n): return sum(d for d in range(1,n+1) if n%d==0)

def exact_rows():
    a2, a3, a4 = theta_polynomials(ORDER)
    x1 = [-2*v for v in qlog(a2)]; x1[0] -= Fraction(1,2)
    x2 = [-2*v for v in qlog(a3)]
    x3 = [-2*v for v in qlog(a4)]
    rows = []
    for k in range(ORDER + 1):
        r1 = Fraction(k)*x1[k] - convolution(x2,x3,k) + convolution(x1,x2,k) + convolution(x1,x3,k)
        r2 = Fraction(k)*x2[k] - convolution(x3,x1,k) + convolution(x2,x3,k) + convolution(x2,x1,k)
        r3 = Fraction(k)*x3[k] - convolution(x1,x2,k) + convolution(x3,x1,k) + convolution(x3,x2,k)
        if r1 or r2 or r3: raise AssertionError(f"formal-series residual at {k}")
        e2half = Fraction(-1,2) if k==0 else Fraction(12*sigma1(k//2)) if k%2==0 else Fraction(0)
        bridge=x1[k]+x2[k]+x3[k]-e2half
        if bridge: raise AssertionError(f"E2 bridge residual at {k}")
        rows.append({"power": k, "X1": fs(x1[k]), "X2": fs(x2[k]), "X3": fs(x3[k]), "minus_half_E2":fs(e2half), "sum_bridge_residual":fs(bridge), "residuals": [fs(r1),fs(r2),fs(r3)]})
    return rows

def theta(index, tau): return mp.jtheta(index, 0, mp.e ** (mp.pi * 1j * tau))

def xvalue(index, tau): return -2 * mp.diff(lambda t: theta(index,t), tau) / theta(index,tau)

def numeric_rows():
    points = [(1,7,4,5),(2,9,11,10),(-1,5,3,2),(3,13,7,10),(-2,11,6,5),(1,3,9,5)]
    rows=[]
    for ar,ad,br,bd in points:
        tau=mp.mpf(ar)/ad + 1j*mp.mpf(br)/bd
        xs=[xvalue(j,tau) for j in (2,3,4)]
        dx=[mp.diff(lambda t, j=j: xvalue(j,t),tau) for j in (2,3,4)]
        rhs=[xs[1]*xs[2]-xs[0]*(xs[1]+xs[2]), xs[2]*xs[0]-xs[1]*(xs[2]+xs[0]), xs[0]*xs[1]-xs[2]*(xs[0]+xs[1])]
        residual=[dx[i]-rhs[i] for i in range(3)]
        tvals=[xvalue(j,tau+1) for j in (2,3,4)]
        t_res=[tvals[0]-xs[0],tvals[1]-xs[2],tvals[2]-xs[1]]
        stau=-1/tau
        transformed=[tau**(-2)*xvalue(j,stau)+1/tau for j in (2,3,4)]
        s_res=[transformed[0]-xs[2],transformed[1]-xs[1],transformed[2]-xs[0]]
        if max(map(abs,residual+t_res+s_res)) > mp.mpf("2e-70"): raise AssertionError("theta/modular numerical lock")
        rows.append({"tau":{"re":f"{ar}/{ad}","im":f"{br}/{bd}"}, "x":[cs(v) for v in xs], "ode_residual":[cs(v) for v in residual], "T_residual":[cs(v) for v in t_res], "S_residual":[cs(v) for v in s_res]})
    return rows

def collision_rows():
    rows=[]
    for c in (-3,-1,2):
        for C in (-2,0,3):
            for t in (4,7):
                u=Fraction(t-c); a=1/u; b=1/u+Fraction(C,u*u)
                ap=-1/(u*u); bp=-1/(u*u)-2*Fraction(C,u*u*u)
                rows.append({"c":c,"C":C,"t":t,"a":fs(a),"b":fs(b),"a_prime":fs(ap),"b_prime":fs(bp),"residual_a":fs(ap+a*a),"residual_b":fs(bp-(a*a-2*a*b))})
    return rows

def axis_rows():
    rows=[]
    for zero_pair,axis in (((1,2),3),((2,3),1),((3,1),2)):
        for value in (-3,-1,0,2,5):
            point=[0,0,0];point[axis-1]=value
            x,y,z=point
            rhs=[y*z-x*(y+z),z*x-y*(z+x),x*y-z*(x+y)]
            if rhs != [0,0,0]:raise AssertionError("axis equilibrium")
            rows.append({"zero_pair":list(zero_pair),"free_axis":axis,"value":value,"point":point,"vector_field":rhs})
    return rows

def leaves(value):
    if type(value) is dict: return sum(leaves(v) for v in value.values())
    if type(value) is list: return sum(leaves(v) for v in value)
    return 1

def payload_hash(data):
    body=dict(data); body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    if sys.flags.optimize: raise RuntimeError("C320 producer refuses optimized Python")
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,default=OUTPUT); args=parser.parse_args()
    qrows=exact_rows(); nrows=numeric_rows(); crows=collision_rows(); arows=axis_rows()
    data={
      "schema":"hcs-c320-darboux-halphen-v1","candidate_id":"HCS-C320","obstruction_id":"HEN-O304",
      "evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,
      "evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR},
      "route_a_yaml":{"path":"evaluations/route_a/HCS-C320/2026-09-03.yaml","raw_sha256":EVAL_RAW,"semantic_sha256":EVAL_SEMANTIC},
      "model":{"time":"tau in the upper half-plane","polynomial_system":"x1'=x2*x3-x1*(x2+x3), cyclically","nome":"Q=exp(pi*i*tau)","scaled_variables":"Xi=xi/(pi*i)=-2*Q*d_Q log(theta_i), i=2,3,4 mapped to 1,2,3"},
      "theorem_contract":{"theta_seed":"x1=-2*d_tau log theta2, x2=-2*d_tau log theta3, x3=-2*d_tau log theta4","eisenstein_bridge":"X1+X2+X3=-E2/2=-1/2+12*sum_(n>=1)sigma1(n)*Q^(2n)","modular_covariance":"x tilde_i(tau)=(c*tau+d)^(-2)x_i(gamma tau)+c/(c*tau+d)","chazy":"S'''=-4*S*S''+6*(S')^2 for S=x1+x2+x3","discriminant":"Delta'=-2*S*Delta","collisions":"each pair-collision stratum has a reciprocal family and a coordinate-axis equilibrium family; the three axes meet at the origin","collision_parameters":"c,C,B are complex; reciprocal charts require tau!=c; one zero of a forces the axis branch by uniqueness"},
      "q_series":{"order":ORDER,"convention":"theta2=2*Q^(1/4)*sum_(m>=0)Q^(m(m+1)); theta3=1+2*sum_(m>=1)Q^(m^2); theta4=1+2*sum_(m>=1)(-1)^m Q^(m^2)","rows":qrows},
      "theta_numeric_rows":nrows,"collision_rows_x1_eq_x2":crows,"axis_equilibrium_rows":arows,
      "boundary_atlas":[
        {"face":"Im(tau)>0 and theta constants nonzero","status":"main analytic theta chart"},
        {"face":"Q=0 cusp","status":"boundary limit X=(-1/2,0,0), not an interior time"},
        {"face":"c*tau+d=0","status":"excluded modular pole of the transformed chart"},
        {"face":"Delta=0","status":"invariant union of pair-collision strata"},
        {"face":"C=0 in the reciprocal collision family","status":"nonzero fully diagonal Riccati solution for c in C and tau!=c"},
        {"face":"a=0 on a pair-collision stratum","status":"coordinate-axis equilibrium family with B in C; all three axes meet at the origin"},
        {"face":"theta zero under continuation","status":"logarithmic-derivative pole; outside the regular chart"}],
      "collision_boundary":{"C186":"Euler-top Jacobi action-angle flow, not a modular theta-constant polynomial flow","C244":"spherical-pendulum elliptic monodromy, not PSL2 covariance of Darboux--Halphen time","C17-C18":"modular scattering clocks and open traces, not the three-component theta ODE","C35":"adelic Henon--theta scattering quantization, not the classical complex-time Halphen phase portrait"},
      "route_a":{"tuple":["A0_WEAK_ARITHMETIC_RELATION","A1_FAIL","A2_FAIL","A3_PARTIAL_ANALYTIC_STRUCTURE","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},
      "scope_flags":FLAGS,
      "nonclaims":["No priority is claimed for the Darboux--Halphen system, theta solution, modular covariance, or Chazy reduction.","No exhaustive meromorphic-solution classification beyond the stated transformations and strata is claimed.","Modular-form coefficients are not target arithmetic local data and no target Euler product is asserted.","No Hilbert--Polya operator, automorphy transfer, root number, functional equation, or target-zero match is claimed."],
      "references":[{"url":"https://ocu-omu.repo.nii.ac.jp/record/2009467/files/111F0000002-03202-12.pdf","role":"primary historical and theta-function account"},{"doi":"10.3842/SIGMA.2018.003","arxiv":"1709.09682","role":"modern Darboux--Halphen geometry and generalizations"},{"arxiv":"solv-int/9902012","role":"modular solutions and triangle-function lineage"}],
      "enumeration":{"q_series_rows":len(qrows),"theta_numeric_rows":len(nrows),"collision_rows":len(crows),"axis_equilibrium_rows":len(arows)} }
    data["enumeration"]["audited_leaf_count"]=leaves(data)+1
    data["payload_sha256"]=payload_hash(data)
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(f"C320_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")

if __name__=="__main__": main()
