#!/usr/bin/env python3
"""Canonical exact-rational evidence for the C380 source theorem."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 producer refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "0596f9d680277288225062a6fdd7ad7ce116e01d"
PARAMETERS = [F(0), F(1, 7), F(1, 3), F(1, 2), F(3, 4)]

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def frac(x):
    return [x.numerator, x.denominator]

def mobius(n):
    answer, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            answer = -answer
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -answer if n > 1 else answer

def entry(a, k, m):
    if k == 0:
        return F(int(m == 0))
    if m < k:
        return F(0)
    total = F(0)
    for j in range(min(k, m-k) + 1):
        ell = m-k-j
        total += comb(k, j) * (-a)**(k-j) * comb(k+ell-1, ell) * a**ell
    return total

def produce():
    census = []
    for n in range(1, 25):
        fixed = 2**n - 1
        exact = sum(mobius(n//d) * (2**d-1) for d in range(1, n+1) if n%d == 0)
        assert exact % n == 0
        census.append({"n": n, "fixed": fixed, "least_period_points": exact,
                       "primitive_cycles": exact//n})
    rows = []
    for a in PARAMETERS:
        q = -a
        r = (1+a)/2
        qr = r*(r+a)/(1+a*r)
        t = (r+qr)/2
        matrix = [[entry(a, k, m) for m in range(11)] for k in range(11)]
        traces = [(1+q**n)/(1-q**n) for n in range(1, 17)]
        coefficients = [F(1)]
        for n in range(1, 17):
            coefficients.append(-sum(traces[k-1]*coefficients[n-k]
                                     for k in range(1, n+1))/n)
        sections = []
        for N in (2, 4, 8, 16):
            polynomial = [F(1), F(-1)]
            for k in range(1, N+1):
                for _ in range(2):
                    new = polynomial + [F(0)]
                    for j, val in enumerate(polynomial):
                        new[j+1] -= q**k*val
                    polynomial = new
            trace4 = 1+2*sum(q**(4*k) for k in range(1,N+1))
            trace4_tail = 2*q**(4*(N+1))/(1-q**4)
            sections.append({"N":N, "polynomial":list(map(frac,polynomial)),
                             "trace_power4":frac(trace4),
                             "trace_power4_tail":frac(trace4_tail)})
        tail_bounds=[]
        for N in (4, 8, 16):
            for radius in (F(1,2), F(1), F(2)):
                eta=radius*a**(N+1)
                assert eta < 1
                bound=2*radius*a**(N+1)/((1-a)*(1-eta))
                tail_bounds.append({"N":N,"radius":frac(radius),"eta":frac(eta),
                                    "log_tail_bound":frac(bound)})
        angular=[]
        for c in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
            v=1+(1-a*a)/(1-2*a*c+a*a)
            angular.append({"cos_theta":frac(c),"angular_derivative":frac(v)})
        roots=[]
        for radius in (F(1,2),F(1),F(2),F(4),F(16)):
            ks=[]
            if a:
                k=1
                while a**k * radius >= 1:
                    ks.append(k);k+=1
            roots.append({"radius":frac(radius),"nonconstant_exponents":ks,
                          "zero_count_with_boundary":int(radius>=1)+2*len(ks)})
        rows.append({"a":frac(a),"q":frac(q),"r":frac(r),"q_of_r":frac(qr),
                     "t":frac(t),"expansion_min":frac(2/(1+a)),
                     "expansion_max":frac(2/(1-a)),"angular_rows":angular,
                     "positive_section_0_to_10":[list(map(frac,row)) for row in matrix],
                     "trace_n_1_to_16":list(map(frac,traces)),
                     "det_coefficients_0_to_16":list(map(frac,coefficients)),
                     "spectral_sections":sections,"tail_bounds":tail_bounds,
                     "zero_census":roots})
    flags={key:False for key in ("claims_target_arithmetic_local_data",
      "claims_target_euler_factors","claims_root_number","claims_automorphy",
      "claims_target_divisor_or_counting_law","claims_target_functional_equation",
      "claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")}
    value={"schema":"c380-blaschke-evidence-v1","candidate_id":"HCS-C380",
      "obstruction_id":"HEN-O364","source_commit":SOURCE,"fixed_epoch":1788566400,
      "evaluation_date":"2026-09-05","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
      "convention":{"map":"z*(z-a)/(1-a*z)","parameter":"0<=a<1",
        "operator":"sum(w*f(z)/(z*Bprime(z))) over B(z)=w",
        "branches":"local only; their sum is globally single valued",
        "time":"integer iteration","multiplier":"positive angular derivative product",
        "spectrum":"1 once; (-a)^k twice for k>=1; 0",
        "determinant":"(1-u)*product_{k>=1}(1-(-a)^k*u)^2",
        "primitive_product_domain":"abs(u)<1","phase":"zero"},
      "census":census,"parameter_rows":rows,
      "boundary":{"a_zero":"P(z^(2m))=z^m; determinant=1-u; not rank one",
                  "a_one":"cancelled map=-z; even iterates identity; no compact Perron operator"},
      "controls":["same census for neighboring rational parameters",
        "prime and composite iterate labels use identical formulas",
        "simpler parent a=0 retains circle census",
        "positive a instead of -a changes all odd traces",
        "omitting the reflected Hardy channel halves nonconstant spectral multiplicity"],
      "route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],
                 "overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},
      "scope_flags":flags,
      "finite_evidence_role":"exact rational regression; all-parameter conclusions use analytic proof"}
    value["payload_sha256"]=hashlib.sha256(canonical(value)).hexdigest()
    return value

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=ROOT/"results/c380_blaschke_evidence.json")
    args=parser.parse_args()
    value=produce();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n")
    print("C380 producer PASS: parameters=5 census=24 exact trace and coefficient orders=16 payload="+value["payload_sha256"])
if __name__=="__main__":main()
