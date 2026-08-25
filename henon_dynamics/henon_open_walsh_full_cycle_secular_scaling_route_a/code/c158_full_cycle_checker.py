#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C158."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


class E:
    __slots__=("x",)
    def __init__(self,a=0,b=0,c=0,d=0):self.x=tuple(Fraction(v) for v in (a,b,c,d))
    def __add__(self,o):
        o=o if isinstance(o,E) else E(o);return E(*(a+b for a,b in zip(self.x,o.x)))
    __radd__=__add__
    def __neg__(self):return E(*(-a for a in self.x))
    def __sub__(self,o):return self+(-(o if isinstance(o,E) else E(o)))
    def __mul__(self,o):
        o=o if isinstance(o,E) else E(o);a,b,c,d=self.x;e,f,g,h=o.x
        return E(a*e+3*b*f-c*g-3*d*h,a*f+b*e-c*h-d*g,a*g+3*b*h+c*e+3*d*f,a*h+b*g+c*f+d*e)
    __rmul__=__mul__
    def __truediv__(self,n):return E(*(v/Fraction(n) for v in self.x))
    def __pow__(self,n):
        out,base=E(1),self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def __eq__(self,o):return self.x==(o if isinstance(o,E) else E(o)).x
    def __bool__(self):return any(self.x)
    @classmethod
    def read(cls,row):return cls(*(Fraction(v) for v in row))
    def receipt(self):return [str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}" for v in self.x]


Z,O=E(),E(1);R=E(0,Fraction(1,3));TAU=E(0,Fraction(1,6),Fraction(-1,2));Q0=E(Fraction(-1,2),0,0,Fraction(-1,6))
A=((R,Z,R),(R,Z,E(0,Fraction(-1,6),Fraction(1,2))),(R,Z,E(0,Fraction(-1,6),Fraction(-1,2))))


def canon(data):
    work=dict(data);work.pop("payload_sha256",None)
    return sha256(json.dumps(work,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def traces(limit):
    values=[E(2),TAU]
    for _ in range(2,limit+1):values.append(TAU*values[-1]-Q0*values[-2])
    return values


def coefficients(k,t):
    out=[O]
    for n in range(1,2**k+1):out.append(-sum((out[n-j]*(t[j]**k) for j in range(1,n+1)),Z)/n)
    return out


def kron(left,right):
    lr,lc,rr,rc=len(left),len(left[0]),len(right),len(right[0])
    return tuple(tuple(left[i//rr][j//rc]*right[i%rr][j%rc] for j in range(lc*rc)) for i in range(lr*rr))


def mm(left,right):
    return tuple(tuple(sum((left[i][h]*right[h][j] for h in range(len(right))),Z) for j in range(len(right[0]))) for i in range(len(left)))


def direct(k):
    matrix=((O,),)
    for _ in range(k):matrix=kron(matrix,A)
    power=tuple(tuple(O if i==j else Z for j in range(len(matrix))) for i in range(len(matrix)))
    pt=[]
    for _ in range(2**k):
        power=mm(power,matrix);pt.append(sum((power[i][i] for i in range(len(matrix))),Z))
    out=[O]
    for n in range(1,2**k+1):out.append(-sum((out[n-j]*pt[j-1] for j in range(1,n+1)),Z)/n)
    return pt,out


def decimal_values():
    getcontext().prec=70;r37=Decimal(37).sqrt();s=(1+r37)/Decimal(6);d=((r37-5)/Decimal(18)).sqrt()
    pp,pm=(s+d)/2,(s-d)/2;rp,rm=pp.sqrt(),pm.sqrt();a,b=rp.ln(),rm.ln();fmt=lambda x:format(x,".50f")
    return {"p_plus":fmt(pp),"p_minus":fmt(pm),"abs_lambda_plus":fmt(rp),"abs_lambda_minus":fmt(rm),"log_abs_plus":fmt(a),"log_abs_minus":fmt(b),
            "mu":fmt(-Decimal(3).ln()/4),"sigma_squared":fmt((a-b)**2/4),"moved_hole_sigma_squared":fmt(Decimal(3).ln()**2/16)}


def main():
    parser=argparse.ArgumentParser();parser.add_argument("evidence",nargs="?",type=Path,default=Path(__file__).resolve().parents[1]/"results/c158_full_cycle_evidence.json");parser.add_argument("--mutation-fast",action="store_true")
    args=parser.parse_args();data=json.loads(args.evidence.read_text());checks=0
    def check(condition,message):
        nonlocal checks;checks+=1
        if not condition:raise AssertionError(message)
    def check_keys(mapping,expected,message):
        check(isinstance(mapping,dict) and set(mapping)==set(expected),message)
    def check_receipts(rows,expected_length,message):
        check(isinstance(rows,list) and len(rows)==expected_length,message+" length")
        check(all(isinstance(row,list) and len(row)==4 for row in rows),message+" shape")
    top={"schema","candidate_id","evaluation_date","scope_literal","source_commit","source_lock","one_site_spectrum","full_cycle_secular_theorem","field_trace_and_polynomial_ledgers","direct_kronecker_determinant_checks","surviving_log_modulus_theorem","controls","route_a","claim_boundary","payload_sha256"}
    check_keys(data,top,"top closure");check(data["schema"]=="hcs-c158-open-walsh-full-cycle-secular-scaling-v1","schema")
    check(data["candidate_id"]=="HCS-C158","candidate");check(data["evaluation_date"]=="2026-08-25","date");check(data["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER","scope")
    check(data["source_commit"]=="506dead810d67fa58fa7c42b2d9a09bfae161059","commit");check(data["payload_sha256"]==canon(data),"hash")
    lock=data["source_lock"]
    check_keys(lock,{"object","gate","full_cycle","clock","secular_convention","scaling_convention","cutoffs","precision","forbidden_data"},"source-lock closure")
    check(lock["object"]=="frozen C148/C153 Walsh gate B_k on (C^3)^tensor k with one-site A=F3^*diag(1,0,1)","source object")
    check(lock["gate"]=="B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0","source gate")
    check(lock["full_cycle"]=="C_k=B_k^k" and lock["clock"]=="one B_k tick; one full cycle is exactly k ticks","clock")
    check(lock["secular_convention"]=="E_k(z)=det(I_(3^k)-z*C_k)","secular")
    check(lock["scaling_convention"]=="X_k=(1/k)log|rho| for a uniformly multiplicity-weighted nonzero eigenvalue rho of C_k","scaling")
    check(lock["cutoffs"]=={"binomial_k_max":24,"field_polynomial_k_max":5,"direct_kronecker_k_max":3,"concentration_k":[8,16,32,64]},"cutoffs")
    check(lock["precision"]=="exact integers and Q(sqrt(3),i) coefficients; 50-place Decimal only for log-modulus sentinels","precision")
    check(lock["forbidden_data"]=="target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B","forbidden data")
    one=data["one_site_spectrum"]
    check_keys(one,{"characteristic_polynomial","tau_q_sqrt3_i_sqrt3i","q0_q_sqrt3_i_sqrt3i","discriminant_q_sqrt3_i_sqrt3i","zero_simple","nonzero_roots_distinct","lambda_label","squared_modulus_sum","squared_modulus_product","squared_modulus_discriminant","squared_moduli","decimal_sentinels"},"one-site closure")
    check(one["characteristic_polynomial"]=="lambda*(lambda^2-tau*lambda+q0)","characteristic polynomial")
    check(one["tau_q_sqrt3_i_sqrt3i"]==TAU.receipt(),"tau");check(one["q0_q_sqrt3_i_sqrt3i"]==Q0.receipt(),"q")
    disc=TAU**2-E(4)*Q0;check(one["discriminant_q_sqrt3_i_sqrt3i"]==disc.receipt()==["11/6","0","0","1/2"],"discriminant")
    check(one["zero_simple"] is True and one["nonzero_roots_distinct"] is True,"simple roots")
    check(one["lambda_label"]=="|lambda_+|>|lambda_-|>0","root labels")
    check(one["squared_modulus_sum"]=="p_++p_-=(1+sqrt(37))/6","p sum");check(one["squared_modulus_product"]=="p_+*p_-=1/3","p product")
    check(one["squared_modulus_discriminant"]=="(p_+-p_-)^2=(sqrt(37)-5)/18>0","p discrimination")
    check(one["squared_moduli"]=="p_+/-=(1+sqrt(37))/12 +/- sqrt((sqrt(37)-5)/72)","squared moduli")
    check(one["decimal_sentinels"]==decimal_values(),"decimal sentinels")
    theorem=data["full_cycle_secular_theorem"]
    check_keys(theorem,{"identity","factorization","degree","zero_generalized_eigenspace_dimension","trace_identity","proof_basis"},"theorem closure")
    check(theorem["identity"]=="C_k=B_k^k=A^(tensor k)","full cycle")
    check(theorem["factorization"]=="E_k(z)=product_(j=0)^k (1-z*lambda_+^j*lambda_-^(k-j))^binom(k,j)","factorization")
    check(theorem["degree"]=="deg E_k=2^k" and theorem["zero_generalized_eigenspace_dimension"]=="3^k-2^k","dimensions")
    check(theorem["trace_identity"]=="Tr(C_k^n)=Tr(A^n)^k","trace identity")
    check(theorem["proof_basis"]=="triangularize A, tensor the three diagonal entries 0,lambda_+,lambda_- and count words by plus-symbol count","proof basis")
    t=traces(32)
    ledgers=data["field_trace_and_polynomial_ledgers"]
    check_keys(ledgers,set(map(str,range(1,6))),"field keys")
    for k in range(1,6):
        coeff=coefficients(k,t);row=ledgers[str(k)]
        check_keys(row,{"degree","zero_generalized_eigenspace_dimension","coefficient_basis","coefficients_ascending","trace_Ck_power_n"},f"field row closure {k}")
        check(row["coefficient_basis"]=="1,sqrt(3),i,sqrt(3)*i",f"coefficient basis {k}")
        check(row["degree"]==2**k and row["zero_generalized_eigenspace_dimension"]==3**k-2**k,f"dimensions {k}")
        check_receipts(row["coefficients_ascending"],2**k+1,f"coefficient receipts {k}")
        check([E.read(x) for x in row["coefficients_ascending"]]==coeff,f"coefficients {k}")
        check(coeff[-1]==Q0**(k*2**(k-1)),f"endpoint {k}")
        expected=[{"n":n,"value":(t[n]**k).receipt()} for n in range(1,min(12,2**k)+1)]
        check(isinstance(row["trace_Ck_power_n"],list) and len(row["trace_Ck_power_n"])==len(expected),f"trace ledger length {k}")
        check(all(isinstance(item,dict) and set(item)=={"n","value"} for item in row["trace_Ck_power_n"]),f"trace row closure {k}")
        check(all(isinstance(item["value"],list) and len(item["value"])==4 for item in row["trace_Ck_power_n"]),f"trace receipt shape {k}")
        check(row["trace_Ck_power_n"]==expected,f"traces {k}")
    direct_rows=data["direct_kronecker_determinant_checks"]
    check_keys(direct_rows,{"1","2","3"},"direct keys")
    for k in range(1,4):
        row=direct_rows[str(k)];coeff=coefficients(k,t)
        check_keys(row,{"matrix_dimension","determinant_degree","direct_matrix_power_traces","direct_newton_determinant_coefficients","matches_factor_theorem"},f"direct row closure {k}")
        check(row["matrix_dimension"]==3**k and row["determinant_degree"]==2**k,f"direct dimensions {k}")
        check_receipts(row["direct_matrix_power_traces"],2**k,f"direct trace receipts {k}")
        check([E.read(x) for x in row["direct_matrix_power_traces"]]==[t[n]**k for n in range(1,2**k+1)],f"direct trace receipt {k}")
        check_receipts(row["direct_newton_determinant_coefficients"],2**k+1,f"direct determinant receipts {k}")
        check([E.read(x) for x in row["direct_newton_determinant_coefficients"]]==coeff,f"direct coefficient receipt {k}")
        check(row["matches_factor_theorem"] is True,f"direct match {k}")
        if not args.mutation_fast:
            dt,dc=direct(k);check(dt==[t[n]**k for n in range(1,2**k+1)],f"literal trace {k}");check(dc==coeff,f"literal determinant {k}")
    scaling=data["surviving_log_modulus_theorem"]
    check_keys(scaling,{"measure","binomial_model","mean","variance","hoeffding","weak_limit","central_limit","phase_limit_claimed","secular_zero_inverse_radius_scaling_claimed","binomial_ledgers","concentration_sentinels"},"scaling closure")
    check(scaling["measure"]=="nu_k=2^(-k) sum_(j=0)^k binom(k,j) delta_((j log|lambda_+|+(k-j)log|lambda_-|)/k)","measure")
    check(scaling["binomial_model"]=="J_k~Binomial(k,1/2), X_k=log|lambda_-|+(J_k/k)log(|lambda_+|/|lambda_-|)","binomial model")
    check(scaling["mean"]=="mu=-log(3)/4","mean");check(scaling["variance"]=="Var(X_k)=sigma^2/k, sigma^2=(log(|lambda_+|/|lambda_-|))^2/4","variance")
    check(scaling["hoeffding"]=="nu_k(|X-mu|>=epsilon)<=2*exp(-k*epsilon^2/(2*sigma^2))","Hoeffding")
    check(scaling["weak_limit"]=="nu_k converges weakly to delta_mu","weak");check(scaling["central_limit"]=="sqrt(k)*(X_k-mu) converges in law to Normal(0,sigma^2)","CLT")
    check(scaling["phase_limit_claimed"] is False and scaling["secular_zero_inverse_radius_scaling_claimed"] is False,"convention boundary")
    bins=scaling["binomial_ledgers"];check(isinstance(bins,list) and len(bins)==24,"binomial count")
    for k,row in enumerate(bins,1):
        frozen=[{"j":j,"multiplicity":comb(k,j),"plus_weight":str(Fraction(j,k)),"minus_weight":str(Fraction(k-j,k))} for j in range(k+1)]
        check_keys(row,{"k","ambient_dimension","surviving_degree","zero_generalized_eigenspace_dimension","rows","multiplicity_sum","j_first_moment_sum","centered_2j_minus_k_square_sum","mean_identity","variance_identity"},f"binomial ledger closure {k}")
        check(row["k"]==k and row["ambient_dimension"]==3**k and row["surviving_degree"]==2**k,f"bin dimensions {k}")
        check(row["zero_generalized_eigenspace_dimension"]==3**k-2**k,f"zero space {k}")
        check(isinstance(row["rows"],list) and len(row["rows"])==k+1,f"bin row length {k}")
        check(all(isinstance(item,dict) and set(item)=={"j","multiplicity","plus_weight","minus_weight"} for item in row["rows"]),f"bin row closure {k}")
        check(row["rows"]==frozen,f"bin rows {k}")
        check(row["multiplicity_sum"]==2**k,f"mass {k}");check(row["j_first_moment_sum"]==k*2**(k-1),f"first {k}")
        check(row["centered_2j_minus_k_square_sum"]==k*2**k,f"variance combinatorics {k}")
        check(row["mean_identity"]=="mu=(log|lambda_+|+log|lambda_-|)/2=-log(3)/4",f"mean identity {k}")
        check(row["variance_identity"]=="Var(X_k)=sigma^2/k",f"variance identity {k}")
    con=scaling["concentration_sentinels"]
    check(isinstance(con,list) and len(con)==4,"concentration count")
    getcontext().prec=70
    for row,k in zip(con,(8,16,32,64)):
        tail=sum(comb(k,j) for j in range(k+1) if abs(4*j-2*k)>=k);bound=format(Decimal(2)*(-Decimal(k)/8).exp(),".50f")
        check_keys(row,{"k","event","exact_tail_numerator","exact_tail_denominator","hoeffding_bound","hoeffding_bound_decimal"},f"concentration row closure {k}")
        check(row["event"]=="abs(X_k-mu)>=abs(log|lambda_+/lambda_-|)/4",f"concentration event {k}")
        check(row["hoeffding_bound"]=="2*exp(-k/8)",f"concentration bound text {k}")
        check(row["k"]==k and row["exact_tail_numerator"]==tail and row["exact_tail_denominator"]==2**k,f"tail {k}")
        check(row["hoeffding_bound_decimal"]==bound,f"bound {k}")
        check(Decimal(tail)/Decimal(2**k)<=Decimal(bound),f"inequality {k}")
    controls=data["controls"]
    check_keys(controls,{"closed_parent","projector_order","moved_hole"},"controls closure")
    closed=controls["closed_parent"]
    check_keys(closed,{"projector","result"},"closed control closure")
    check(closed["projector"]=="I_3","closed projector")
    check(closed["result"]=="A_closed=F3^* is unitary; full-cycle degree is 3^k and its normalized log-modulus measure is delta_0","closed result")
    order=controls["projector_order"]
    check_keys(order,{"gate","result"},"projector-order closure")
    check(order["gate"]=="A_right=diag(1,0,1)F3^*=F3*A*F3^*","projector-order gate")
    check(order["result"]=="unitary similarity preserves lambda_+/- and hence every full-cycle factor, measure, mean, variance, and limit","projector-order result")
    moved=controls["moved_hole"]
    check_keys(moved,{"projector","nonzero_eigenvalues","rank_and_degree","mean","variance","variance_changes","mean_changes"},"moved-hole closure")
    check(moved["projector"]=="diag(0,1,1)","moved projector")
    check(moved["nonzero_eigenvalues"]=="-i and -1/sqrt(3)","moved spectrum")
    check(moved["rank_and_degree"]=="rank powers remain 2 and full-cycle degree remains 2^k","moved rank and degree")
    check(moved["variance_changes"] is True and moved["mean_changes"] is False,"moved moments")
    check(moved["mean"]=="mu remains -log(3)/4 because the nonzero product modulus remains 1/sqrt(3)","moved mean")
    check(moved["variance"]=="sigma_0^2=(log 3)^2/16, different from the frozen sigma^2","moved variance")
    check(data["route_a"]=={"tuple":["A1_WEAK","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"],"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},"route")
    boundary={"finite_and_growing_k_source_gate_only":True,"phase_limit":False,"self_adjoint_limit":False,"target_divisor_matching":False,"target_functional_equation":False,"target_counting_law":False,"prime_like_correspondence":False,"arithmetic_local_data":False,"euler_factors":False,"root_numbers":False,"automorphy":False,"hilbert_polya_operator":False}
    check(data["claim_boundary"]==boundary,"claim-boundary closure and values")
    print(json.dumps({"status":"C158_CHECKER_PASS","assertions":checks},sort_keys=True))

if __name__=="__main__":main()
