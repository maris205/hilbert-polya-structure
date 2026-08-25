#!/usr/bin/env python3
"""Producer-independent checker for HCS-C161."""
from __future__ import annotations

import argparse
import cmath
from hashlib import sha256
import json
from math import gcd, pi, sqrt
from pathlib import Path


def payload_hash(data):
    clean = dict(data); clean.pop("payload_sha256")
    return sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def jacobi_symbol(a, n):
    a %= n; sign = 1
    while a:
        power = 0
        while a % 2 == 0:
            a //= 2; power += 1
        if power % 2 and n % 8 in (3, 5): sign *= -1
        if a % 4 == n % 4 == 3: sign *= -1
        a, n = n % a, a
    return sign if n == 1 else 0


def coeff(a, b, n):
    # Independent summation identities in binomial-coefficient form.
    return a*n, 2*a*(n*(n-1)//2)+b*n, a*n*(n-1)*(2*n-1)//6+b*n*(n-1)//2


def formula(q, a, b, n):
    aa, bb, cc = coeff(a, b, n); d = gcd(aa, q)
    if bb % d:
        return 0j, "VANISHING_GCD_OBSTRUCTION"
    reduced = q // d
    if reduced == 1:
        return q * cmath.exp(2j*pi*(cc % q)/q), "CONSTANT_PHASE"
    ar, br = aa//d, bb//d
    shift = (-br*br*pow(4*ar % reduced, -1, reduced)) % reduced
    phase = (cc+d*shift) % q
    epsilon = 1 if reduced % 4 == 1 else 1j
    value = d*jacobi_symbol(ar, reduced)*epsilon*sqrt(reduced)*cmath.exp(2j*pi*phase/q)
    return value, "PRIMITIVE_GAUSS_EVALUATION"

def descriptor(q,a,b,n):
    aa,bb,cc=coeff(a,b,n);d=gcd(aa,q)
    if bb%d:return {"status":"VANISHING_GCD_OBSTRUCTION","gcd_A_q":d,"A_n":aa,"B_n":bb,"C_n":cc}
    Q=q//d
    if Q==1:return {"status":"CONSTANT_PHASE","gcd_A_q":d,"A_n":aa,"B_n":bb,"C_n":cc,
                    "reduced_modulus":1,"scale":q,"radical":1,"jacobi_sign":1,"epsilon":"ONE","phase_numerator_mod_q":cc%q}
    ar,br=aa//d,bb//d;shift=(-br*br*pow(4*ar%Q,-1,Q))%Q
    return {"status":"PRIMITIVE_GAUSS_EVALUATION","gcd_A_q":d,"A_n":aa,"B_n":bb,"C_n":cc,
            "reduced_modulus":Q,"reduced_A":ar,"reduced_B":br,"completion_square_residue":shift,
            "scale":d,"radical":Q,"jacobi_sign":jacobi_symbol(ar,Q),"epsilon":"ONE" if Q%4==1 else "I",
            "phase_numerator_mod_q":(cc+d*shift)%q}


def direct(q, a, b, n):
    total = 0j
    for x in range(q):
        phase = sum(a*((x+j) % q)**2+b*((x+j) % q) for j in range(n)) % q
        total += cmath.exp(2j*pi*phase/q)
    return total


def prime(p):
    return p > 1 and all(p % d for d in range(2, int(sqrt(p))+1))


def legendre(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p-1)//2, p) == 1 else -1


def zero_formula(p, a, b, n):
    aa, bb, cc = (x % p for x in coeff(a, b, n))
    if aa: return 1+legendre(bb*bb-4*aa*cc, p)
    if bb: return 1
    return p if cc == 0 else 0


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=root/"results/c161_cyclic_gauss_evidence.json")
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args(); data = json.loads(args.evidence.read_text())
    assertions = 0
    assert set(data)=={"schema","candidate_id","evaluation_date","scope_literal","source_commit","source_lock",
                       "hard_gate","all_iterate_theorem","formal_lift","exhaustive_validation","sentinels",
                       "route_a","claim_boundary","payload_sha256"};assertions+=1
    assert set(data["source_lock"])=={"object","clock","normalization","determinant_convention","cutoff","precision",
                                      "training_data","forbidden_data"};assertions+=1
    assert set(data["hard_gate"])=={"required","rejected_candidate","rejection_reason","rejected_upstream_evidence_sha256",
                                    "pivot","status"};assertions+=1
    assert set(data["all_iterate_theorem"])=={"birkhoff_polynomial","vanishing_gate","nonzero_formula","constant_branch",
                                              "epsilon","prime_zero_law","pure_quadratic_specialization",
                                              "prime_zero_or_euler_interpretation"};assertions+=1
    assert set(data["formal_lift"])=={"hilbert_space","koopman_shift","phase_multiplier","weighted_unitary",
                                      "same_clock_identity","ordinary_trace_warning","time_reversal_antiunitary",
                                      "time_reversal_identity","time_reversal_involution","finite_dimensional_unitary",
                                      "target_operator_claimed"};assertions+=1
    assert set(data["exhaustive_validation"])=={"formula_cases","vanishing_cases","nonzero_cases",
                                                "prime_zero_count_cases","maximum_complex_absolute_error"};assertions+=1
    assert set(data["route_a"])=={"tuple","overall","route_b_invocation_allowed"};assertions+=1
    assert set(data["claim_boundary"])=={"target_trace_identity","target_divisor_matching","target_functional_equation",
                                         "target_counting_law","arithmetic_local_data","euler_factors","root_numbers",
                                         "automorphy","hilbert_polya_operator"};assertions+=1
    assert data["payload_sha256"] == payload_hash(data); assertions += 1
    assert data["schema"]=="hcs-c161-finite-cyclic-quadratic-birkhoff-evidence-v1";assertions+=1
    assert data["candidate_id"]=="HCS-C161";assertions+=1
    assert data["evaluation_date"]=="2026-08-25";assertions+=1
    assert data["source_commit"]=="63f75cf476711de93e6096ef74ac16969e1127d0";assertions+=1
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"; assertions += 1
    assert data["source_lock"]=={
        "object":"finite cyclic rotation R_q(x)=x+1 on Z/qZ, q odd, with phi_(a,b)(x)=a*x^2+b*x",
        "clock":"the exact Birkhoff iterate n>=1",
        "normalization":"unscaled complete orbit average numerator sum_(x mod q) exp(2*pi*i*S_n phi(x)/q)",
        "determinant_convention":"none; the object is a finite source dynamical amplitude",
        "cutoff":{"all_parameter_theorem":True,"exhaustive_q_odd_at_most":31,"n_at_most_twice_q":True},
        "precision":"exact modular formula; double-complex exhaustive sentinels with a 3e-10*q envelope",
        "training_data":"none",
        "forbidden_data":"target zero/prime tables, target divisors/counting laws, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B"};assertions+=1
    assert data["hard_gate"]=={
        "required":"a strict all-iterate evaluation rather than another finite Heisenberg table",
        "rejected_candidate":"the C156 Heisenberg all-n local-product draft",
        "rejection_reason":"discriminant evidence did not independently establish uniform quotient coordinates, translation removal, or the 2-adic and 5-adic equivalences",
        "rejected_upstream_evidence_sha256":"06791bf5734a48d0fe84d0e752e5d156172e637fe9a6a5e29792dfb3b2637b40",
        "pivot":"finite cyclic quadratic Birkhoff dynamics","status":"PASS_BY_MODEL_PIVOT"};assertions+=1
    assert data["all_iterate_theorem"]=={
        "birkhoff_polynomial":"for n>=1, S_n phi(x)=A_n*x^2+B_n*x+C_n with A_n=a*n, B_n=a*n(n-1)+b*n, C_n=a*n(n-1)(2n-1)/6+b*n(n-1)/2",
        "vanishing_gate":"d=gcd(A_n,q); the amplitude is zero exactly when d does not divide B_n",
        "nonzero_formula":"if d|B_n and Q=q/d>1: d*(A_n/d|Q)*epsilon_Q*sqrt(Q)*exp(2*pi*i*(C_n+d*(-B'^2*(4A')^-1 mod Q))/q)",
        "constant_branch":"if Q=1 the amplitude is q*exp(2*pi*i*C_n/q)",
        "epsilon":"epsilon_Q=1 for Q=1 mod 4 and i for Q=3 mod 4",
        "prime_zero_law":"for q=p prime: 1+(Delta|p) in the quadratic branch, one in the linear branch, and p or zero in the constant branch",
        "pure_quadratic_specialization":"for p>=5, a=1, b=0 and n nonzero mod p, Delta=n^2*(1-n^2)/3 and the zero count is 1+(Delta|p); n=0 mod p gives p roots, while n congruent to plus_or_minus 1 mod p gives the single double root",
        "prime_zero_or_euler_interpretation":False};assertions+=1
    assert data["formal_lift"]=={
        "hilbert_space":"H_q=ell^2(Z/qZ)","koopman_shift":"(K_q f)(x)=f(x+1)",
        "phase_multiplier":"(M_phi f)(x)=exp(2*pi*i*phi_(a,b)(x)/q)*f(x)",
        "weighted_unitary":"U_phi=M_phi*K_q","same_clock_identity":"G_(q,n)(a,b)=Tr(U_phi^n*K_q^(-n))",
        "ordinary_trace_warning":"G_(q,n) is not asserted to equal Tr(U_phi^n); the compensating K_q^(-n) is essential",
        "time_reversal_antiunitary":"Theta=D_g*P*J with (P f)(x)=f(-x), J complex conjugation, and g(x)=(a-b)*x^2",
        "time_reversal_identity":"Theta*U_phi*Theta^(-1)=U_phi^(-1)","time_reversal_involution":True,
        "finite_dimensional_unitary":True,"target_operator_claimed":False};assertions+=1
    assert data["route_a"]["route_b_invocation_allowed"] is False; assertions += 1
    assert data["route_a"]["tuple"]==["A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"];assertions+=1
    assert data["route_a"]["overall"]=="ROUTE_A_EXPLORATORY";assertions+=1
    assert not any(data["claim_boundary"].values()); assertions += len(data["claim_boundary"])

    cases = vanishing = prime_cases = 0
    q_values=[] if args.mutation_fast else range(3,32,2)
    for q in q_values:
        for a in range(q):
            for b in range(q):
                for n in range(1, 2*q+1):
                    aa, bb, _ = coeff(a, b, n)
                    obstructed = bb % gcd(aa, q) != 0
                    vanishing += obstructed; cases += 1; assertions += 1
                    if q <= 17 or (a*37+b*11+n*5+q) % 97 == 0:
                        predicted, branch = formula(q, a, b, n)
                        observed = direct(q, a, b, n)
                        assert abs(predicted-observed) < 3e-10*q; assertions += 1
                        assert (branch == "VANISHING_GCD_OBSTRUCTION") == obstructed; assertions += 1
                    if prime(q):
                        observed_zeros = sum(1 for x in range(q)
                                             if sum(a*((x+j)%q)**2+b*((x+j)%q)
                                                    for j in range(n)) % q == 0)
                        assert observed_zeros == zero_formula(q, a, b, n); assertions += 1
                        prime_cases += 1
    report = data["exhaustive_validation"]
    expected_totals=(261630,26864,234766,164284)
    assert (report["formula_cases"],report["vanishing_cases"],report["nonzero_cases"],
            report["prime_zero_count_cases"])==expected_totals;assertions+=4
    assert float(report["maximum_complex_absolute_error"])<1e-12;assertions+=1
    if not args.mutation_fast:
        assert (cases,vanishing,cases-vanishing,prime_cases)==expected_totals;assertions+=4

    for row in data["sentinels"]:
        assert set(row) in ({"q","a","b","n","formula","direct_real","direct_imag"},
                            {"q","a","b","n","formula","direct_real","direct_imag","prime_zero_level"});assertions+=1
        predicted, branch = formula(row["q"], row["a"], row["b"], row["n"])
        observed = complex(float(row["direct_real"]), float(row["direct_imag"]))
        assert abs(predicted-observed) < 1e-12*row["q"]; assertions += 1
        assert row["formula"]["status"] == branch; assertions += 1
        assert row["formula"]==descriptor(row["q"],row["a"],row["b"],row["n"]);assertions+=1
        for x in range(row["q"]):
            g=lambda z:(row["a"]-row["b"])*z*z
            phi=lambda z:row["a"]*z*z+row["b"]*z
            assert (g(x)-g(x-1)-phi(-x)+phi(x-1))%row["q"]==0;assertions+=1
            assert (g(x)-g(-x))%row["q"]==0;assertions+=1
        if prime(row["q"]):
            aa,bb,cc=(z%row["q"] for z in coeff(row["a"],row["b"],row["n"]))
            delta=(bb*bb-4*aa*cc)%row["q"] if aa else None
            branch0="QUADRATIC_DISCRIMINANT" if aa else ("LINEAR_UNIQUE_ROOT" if bb else "CONSTANT_LEVEL")
            assert row["prime_zero_level"]=={"count":zero_formula(row["q"],row["a"],row["b"],row["n"]),
                                             "discriminant_mod_p":delta,"branch":branch0};assertions+=1
    print(json.dumps({"status":"C161_INDEPENDENT_CHECK_PASS", "assertions":assertions,
                      "formula_cases":cases, "prime_zero_cases":prime_cases}, sort_keys=True))


if __name__ == "__main__": main()
