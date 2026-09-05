#!/usr/bin/env python3
"""Independent series division, renewal inversion and q-difference checks."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 checker refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CHECKS=0
def check(ok,message="check failed"):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(message)
def unique(pairs):
    result={}
    for key,val in pairs:
        if key in result:raise ValueError("duplicate JSON key")
        result[key]=val
    return result
def read(path):
    return json.loads(path.read_text(),object_pairs_hook=unique,
      parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def rational(x):
    check(type(x) is list and len(x)==2 and all(type(t) is int for t in x))
    check(x[1]>0)
    f=F(*x);check([f.numerator,f.denominator]==x)
    return f
def conv(a,b,N):
    out=[F(0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:out[i+j]+=x*y
    return out

def audit(x):
    check(type(x) is dict)
    def reject_bool_substitution(value, path=()):
        if type(value) is bool:
            check((path and path[0]=="scope_flags") or path==("route_a","route_b_invocation_allowed"))
        elif type(value) is dict:
            for k,v in value.items():reject_bool_substitution(v,path+(k,))
        elif type(value) is list:
            for i,v in enumerate(value):reject_bool_substitution(v,path+(i,))
        elif type(value) is float:
            raise ValueError("floating-point values are outside the exact evidence schema")
    reject_bool_substitution(x)
    check(set(x)==set("schema candidate_id obstruction_id source_commit fixed_epoch evaluation_date scope_literal evaluator_sha256 convention census parameter_rows boundary controls route_a scope_flags finite_evidence_role payload_sha256".split()))
    payload=dict(x);claimed=payload.pop("payload_sha256")
    check(claimed==hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest())
    for key,val in {"schema":"c380-blaschke-evidence-v1","candidate_id":"HCS-C380",
      "obstruction_id":"HEN-O364","source_commit":"0596f9d680277288225062a6fdd7ad7ce116e01d",
      "fixed_epoch":1788566400,"evaluation_date":"2026-09-05",
      "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}.items():
        check(type(x[key]) is type(val) and x[key]==val,key)
    expected_convention={"map":"z*(z-a)/(1-a*z)","parameter":"0<=a<1",
      "operator":"sum(w*f(z)/(z*Bprime(z))) over B(z)=w",
      "branches":"local only; their sum is globally single valued",
      "time":"integer iteration","multiplier":"positive angular derivative product",
      "spectrum":"1 once; (-a)^k twice for k>=1; 0",
      "determinant":"(1-u)*product_{k>=1}(1-(-a)^k*u)^2",
      "primitive_product_domain":"abs(u)<1","phase":"zero"}
    check(x["convention"]==expected_convention)
    check(x["route_a"]=={"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],
      "overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False})
    check(x["route_a"]["route_b_invocation_allowed"] is False)
    flags="claims_target_arithmetic_local_data claims_target_euler_factors claims_root_number claims_automorphy claims_target_divisor_or_counting_law claims_target_functional_equation claims_target_zero_match claims_hilbert_polya_operator invokes_route_b".split()
    check(set(x["scope_flags"])==set(flags) and all(v is False for v in x["scope_flags"].values()))
    check(x["boundary"]=={"a_zero":"P(z^(2m))=z^m; determinant=1-u; not rank one",
      "a_one":"cancelled map=-z; even iterates identity; no compact Perron operator"})
    check(x["controls"]==["same census for neighboring rational parameters",
      "prime and composite iterate labels use identical formulas","simpler parent a=0 retains circle census",
      "positive a instead of -a changes all odd traces",
      "omitting the reflected Hardy channel halves nonconstant spectral multiplicity"])
    check(x["finite_evidence_role"]=="exact rational regression; all-parameter conclusions use analytic proof")
    check(len(x["census"])==24)
    cycles={}
    for n,row in enumerate(x["census"],1):
        proper=sum(d*v for d,v in cycles.items() if n%d==0)
        new=(2**n-1-proper)//n;cycles[n]=new
        check(row=={"n":n,"fixed":2**n-1,"least_period_points":n*new,"primitive_cycles":new})
    expected_a=[F(0),F(1,7),F(1,3),F(1,2),F(3,4)]
    check(len(x["parameter_rows"])==len(expected_a))
    for row,a in zip(x["parameter_rows"],expected_a):
        check(set(row)==set("a q r q_of_r t expansion_min expansion_max angular_rows positive_section_0_to_10 trace_n_1_to_16 det_coefficients_0_to_16 spectral_sections tail_bounds zero_census".split()))
        check(rational(row["a"])==a);q=rational(row["q"]);check(q==-a)
        r=rational(row["r"]);t=rational(row["t"]);qr=rational(row["q_of_r"])
        check(r==(1+a)/2 and qr*(1+a*r)==r*(r+a) and 2*t==r+qr and qr<t<r<1)
        lower=rational(row["expansion_min"]);upper=rational(row["expansion_max"])
        check(lower*(1+a)==2 and upper*(1-a)==2 and lower>1)
        check(len(row["angular_rows"])==5)
        for d,c in zip(row["angular_rows"],[F(-1),F(-1,2),F(0),F(1,2),F(1)]):
            check(set(d)=={"cos_theta","angular_derivative"} and rational(d["cos_theta"])==c)
            v=rational(d["angular_derivative"])
            check((v-1)*(1-2*a*c+a*a)==1-a*a and lower<=v<=upper)
        # Independent coefficient computation: solve (1-a*z)B=z^2-a*z
        # recursively and form truncated powers by convolution; no binomial formula.
        N=10;b=[F(0)]*(N+1)
        for j in range(1,N+1):b[j]=a*b[j-1]+(F(-a) if j==1 else F(1) if j==2 else F(0))
        power=[F(1)]+[F(0)]*N
        check(len(row["positive_section_0_to_10"])==N+1)
        for k,matrix_row in enumerate(row["positive_section_0_to_10"]):
            check(len(matrix_row)==N+1)
            check([rational(v) for v in matrix_row]==power)
            power=conv(power,b,N)
        traces=[rational(v) for v in row["trace_n_1_to_16"]]
        coeff=[rational(v) for v in row["det_coefficients_0_to_16"]]
        check(len(traces)==16 and len(coeff)==17 and coeff[0]==1)
        for n in range(1,17):
            # Fixed-point index sum gives trace, independently of spectrum summation.
            check(traces[n-1]==2/(1-q**n)-1)
            previous=coeff[n-2] if n>=2 else F(0)
            check((q**n-1)*coeff[n]==q**(n-1)*((1+q)*coeff[n-1]-previous))
        check(len(row["spectral_sections"])==4)
        for section,N in zip(row["spectral_sections"],(2,4,8,16)):
            check(set(section)=={"N","polynomial","trace_power4","trace_power4_tail"} and section["N"]==N)
            # Newton identity from the finite eigenvalue power sums, independent
            # of the producer's multiplication of linear factors.
            c=[F(1)]
            lam=[F(1)]+[q**k for k in range(1,N+1) for _ in range(2)]
            for m in range(1,2*N+2):
                c.append(-sum(sum(v**j for v in lam)*c[m-j] for j in range(1,m+1))/m)
            check([rational(v) for v in section["polynomial"]]==c)
            finite=rational(section["trace_power4"]);tail=rational(section["trace_power4_tail"])
            check(finite==sum(v**4 for v in lam) and finite+tail==traces[3])
        check(len(row["tail_bounds"])==9)
        for d,(N,R) in zip(row["tail_bounds"],[(N,R) for N in (4,8,16) for R in (F(1,2),F(1),F(2))]):
            check(set(d)=={"N","radius","eta","log_tail_bound"} and d["N"]==N and rational(d["radius"])==R)
            eta=rational(d["eta"]);E=rational(d["log_tail_bound"])
            check(eta==R*a**(N+1) and eta<1 and E*(1-a)*(1-eta)==2*eta)
        check(len(row["zero_census"])==5)
        for d,R in zip(row["zero_census"],[F(1,2),F(1),F(2),F(4),F(16)]):
            check(set(d)=={"radius","nonconstant_exponents","zero_count_with_boundary"})
            check(rational(d["radius"])==R)
            ks=[k for k in range(1,100) if a and a**k*R>=1]
            check(d["nonconstant_exponents"]==ks and d["zero_count_with_boundary"]==int(R>=1)+2*len(ks))

def main():
    p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=ROOT/"results/c380_blaschke_evidence.json")
    args=p.parse_args();audit(read(args.input));print(f"C380 independent checker PASS: checks={CHECKS}")
if __name__=="__main__":main()
