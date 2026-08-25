#!/usr/bin/env python3
"""Produce exact full-cycle secular-scaling evidence for HCS-C158."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
K_BINOMIAL_MAX = 24
K_POLYNOMIAL_MAX = 5
DIRECT_K_MAX = 3
TRACE_POWER_MAX = 32
CONCENTRATION_K = (8, 16, 32, 64)


class QSI:
    """Exact a+b*sqrt(3)+c*i+d*sqrt(3)*i arithmetic."""
    __slots__ = ("v",)

    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(Fraction(x) for x in (a, b, c, d))

    def __add__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return QSI(*(x + y for x, y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return QSI(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, QSI) else QSI(other)))

    def __mul__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        a, b, c, d = self.v; e, f, g, h = other.v
        return QSI(a*e+3*b*f-c*g-3*d*h,
                   a*f+b*e-c*h-d*g,
                   a*g+3*b*h+c*e+3*d*f,
                   a*h+b*g+c*f+d*e)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        value = Fraction(scalar)
        return QSI(*(x/value for x in self.v))

    def __pow__(self, exponent):
        answer, base = QSI(1), self
        while exponent:
            if exponent & 1: answer = answer * base
            base = base * base; exponent //= 2
        return answer

    def __eq__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return self.v == other.v

    def __bool__(self): return any(self.v)

    @staticmethod
    def text(value):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

    def receipt(self): return [self.text(x) for x in self.v]


ZERO, ONE = QSI(), QSI(1)
R = QSI(0, Fraction(1, 3))
TAU = QSI(0, Fraction(1, 6), Fraction(-1, 2))
Q0 = QSI(Fraction(-1, 2), 0, 0, Fraction(-1, 6))
A = (
    (R, ZERO, R),
    (R, ZERO, QSI(0, Fraction(-1, 6), Fraction(1, 2))),
    (R, ZERO, QSI(0, Fraction(-1, 6), Fraction(-1, 2))),
)


def trace_powers(limit):
    values = [QSI(2), TAU]
    for _ in range(2, limit + 1):
        values.append(TAU * values[-1] - Q0 * values[-2])
    return values


def secular_coefficients(k, traces):
    degree = 2**k
    coefficients = [ONE]
    for n in range(1, degree + 1):
        # Newton needs all earlier power traces, not just the current one.
        value = ZERO
        for j in range(1, n + 1):
            value = value + coefficients[n-j] * (traces[j] ** k)
        coefficients.append(-value / n)
    assert coefficients[-1] == (Q0 ** (k * 2 ** (k-1)))
    return coefficients


def kron(left, right):
    return tuple(tuple(left[i//len(right)][j//len(right[0])] * right[i%len(right)][j%len(right[0])]
                       for j in range(len(left[0])*len(right[0])))
                 for i in range(len(left)*len(right)))


def matmul(left, right):
    rows, inner, cols = len(left), len(right), len(right[0])
    return tuple(tuple(sum((left[i][h]*right[h][j] for h in range(inner)), ZERO) for j in range(cols)) for i in range(rows))


def direct_kronecker_coefficients(k):
    matrix = ((ONE,),)
    for _ in range(k): matrix = kron(matrix, A)
    power = tuple(tuple(ONE if i == j else ZERO for j in range(len(matrix))) for i in range(len(matrix)))
    traces = []
    for _ in range(1, 2**k + 1):
        power = matmul(power, matrix)
        traces.append(sum((power[i][i] for i in range(len(matrix))), ZERO))
    coefficients = [ONE]
    for n in range(1, 2**k + 1):
        coefficients.append(-sum((coefficients[n-j]*traces[j-1] for j in range(1,n+1)), ZERO)/n)
    return traces, coefficients


def decimal_receipts():
    getcontext().prec = 70
    root37 = Decimal(37).sqrt()
    psum = (Decimal(1)+root37)/Decimal(6)
    pdiff = ((root37-Decimal(5))/Decimal(18)).sqrt()
    pplus, pminus = (psum+pdiff)/2, (psum-pdiff)/2
    rplus, rminus = pplus.sqrt(), pminus.sqrt()
    a, b = rplus.ln(), rminus.ln()
    mu = -Decimal(3).ln()/4
    sigma2 = (a-b)*(a-b)/4
    moved_sigma2 = Decimal(3).ln()**2/16
    fmt = lambda x: format(x, ".50f")
    return {"p_plus":fmt(pplus),"p_minus":fmt(pminus),"abs_lambda_plus":fmt(rplus),"abs_lambda_minus":fmt(rminus),
            "log_abs_plus":fmt(a),"log_abs_minus":fmt(b),"mu":fmt(mu),"sigma_squared":fmt(sigma2),
            "moved_hole_sigma_squared":fmt(moved_sigma2)}


def binomial_ledgers():
    ledgers=[]
    for k in range(1,K_BINOMIAL_MAX+1):
        rows=[{"j":j,"multiplicity":comb(k,j),"plus_weight":QSI.text(Fraction(j,k)),"minus_weight":QSI.text(Fraction(k-j,k))} for j in range(k+1)]
        total=sum(row["multiplicity"] for row in rows)
        first=sum(row["j"]*row["multiplicity"] for row in rows)
        centered=sum((2*row["j"]-k)**2*row["multiplicity"] for row in rows)
        ledgers.append({"k":k,"ambient_dimension":3**k,"surviving_degree":2**k,"zero_generalized_eigenspace_dimension":3**k-2**k,
                        "rows":rows,"multiplicity_sum":total,"j_first_moment_sum":first,"centered_2j_minus_k_square_sum":centered,
                        "mean_identity":"mu=(log|lambda_+|+log|lambda_-|)/2=-log(3)/4",
                        "variance_identity":"Var(X_k)=sigma^2/k"})
    return ledgers


def concentration_ledgers():
    getcontext().prec=70
    rows=[]
    for k in CONCENTRATION_K:
        tail=sum(comb(k,j) for j in range(k+1) if abs(4*j-2*k)>=k)
        bound=Decimal(2)*(-Decimal(k)/Decimal(8)).exp()
        rows.append({"k":k,"event":"abs(X_k-mu)>=abs(log|lambda_+/lambda_-|)/4",
                     "exact_tail_numerator":tail,"exact_tail_denominator":2**k,
                     "hoeffding_bound":"2*exp(-k/8)","hoeffding_bound_decimal":format(bound,".50f")})
    return rows


def canonical_hash(payload):
    return sha256(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def build_evidence():
    traces=trace_powers(max(TRACE_POWER_MAX,2**K_POLYNOMIAL_MAX))
    polynomials={}
    direct={}
    for k in range(1,K_POLYNOMIAL_MAX+1):
        coeff=secular_coefficients(k,traces)
        polynomials[str(k)]={"degree":2**k,"zero_generalized_eigenspace_dimension":3**k-2**k,
                             "coefficient_basis":"1,sqrt(3),i,sqrt(3)*i","coefficients_ascending":[x.receipt() for x in coeff],
                             "trace_Ck_power_n":[{"n":n,"value":(traces[n]**k).receipt()} for n in range(1,min(12,2**k)+1)]}
        if k<=DIRECT_K_MAX:
            dtr,dco=direct_kronecker_coefficients(k)
            assert dco==coeff
            direct[str(k)]={"matrix_dimension":3**k,"determinant_degree":2**k,
                            "direct_matrix_power_traces":[x.receipt() for x in dtr],
                            "direct_newton_determinant_coefficients":[x.receipt() for x in dco],"matches_factor_theorem":True}
    decimals=decimal_receipts()
    payload={
      "schema":"hcs-c158-open-walsh-full-cycle-secular-scaling-v1","candidate_id":"HCS-C158","evaluation_date":"2026-08-25",
      "scope_literal":SCOPE,"source_commit":"506dead810d67fa58fa7c42b2d9a09bfae161059",
      "source_lock":{"object":"frozen C148/C153 Walsh gate B_k on (C^3)^tensor k with one-site A=F3^*diag(1,0,1)",
                     "gate":"B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0",
                     "full_cycle":"C_k=B_k^k","clock":"one B_k tick; one full cycle is exactly k ticks",
                     "secular_convention":"E_k(z)=det(I_(3^k)-z*C_k)",
                     "scaling_convention":"X_k=(1/k)log|rho| for a uniformly multiplicity-weighted nonzero eigenvalue rho of C_k",
                     "cutoffs":{"binomial_k_max":K_BINOMIAL_MAX,"field_polynomial_k_max":K_POLYNOMIAL_MAX,"direct_kronecker_k_max":DIRECT_K_MAX,"concentration_k":list(CONCENTRATION_K)},
                     "precision":"exact integers and Q(sqrt(3),i) coefficients; 50-place Decimal only for log-modulus sentinels",
                     "forbidden_data":"target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B"},
      "one_site_spectrum":{"characteristic_polynomial":"lambda*(lambda^2-tau*lambda+q0)","tau_q_sqrt3_i_sqrt3i":TAU.receipt(),
                           "q0_q_sqrt3_i_sqrt3i":Q0.receipt(),"discriminant_q_sqrt3_i_sqrt3i":(TAU**2-QSI(4)*Q0).receipt(),
                           "zero_simple":True,"nonzero_roots_distinct":True,"lambda_label":"|lambda_+|>|lambda_-|>0",
                           "squared_modulus_sum":"p_++p_-=(1+sqrt(37))/6","squared_modulus_product":"p_+*p_-=1/3",
                           "squared_modulus_discriminant":"(p_+-p_-)^2=(sqrt(37)-5)/18>0",
                           "squared_moduli":"p_+/-=(1+sqrt(37))/12 +/- sqrt((sqrt(37)-5)/72)",
                           "decimal_sentinels":decimals},
      "full_cycle_secular_theorem":{"identity":"C_k=B_k^k=A^(tensor k)",
                                     "factorization":"E_k(z)=product_(j=0)^k (1-z*lambda_+^j*lambda_-^(k-j))^binom(k,j)",
                                     "degree":"deg E_k=2^k","zero_generalized_eigenspace_dimension":"3^k-2^k",
                                     "trace_identity":"Tr(C_k^n)=Tr(A^n)^k",
                                     "proof_basis":"triangularize A, tensor the three diagonal entries 0,lambda_+,lambda_- and count words by plus-symbol count"},
      "field_trace_and_polynomial_ledgers":polynomials,"direct_kronecker_determinant_checks":direct,
      "surviving_log_modulus_theorem":{"measure":"nu_k=2^(-k) sum_(j=0)^k binom(k,j) delta_((j log|lambda_+|+(k-j)log|lambda_-|)/k)",
                                        "binomial_model":"J_k~Binomial(k,1/2), X_k=log|lambda_-|+(J_k/k)log(|lambda_+|/|lambda_-|)",
                                        "mean":"mu=-log(3)/4","variance":"Var(X_k)=sigma^2/k, sigma^2=(log(|lambda_+|/|lambda_-|))^2/4",
                                        "hoeffding":"nu_k(|X-mu|>=epsilon)<=2*exp(-k*epsilon^2/(2*sigma^2))",
                                        "weak_limit":"nu_k converges weakly to delta_mu",
                                        "central_limit":"sqrt(k)*(X_k-mu) converges in law to Normal(0,sigma^2)",
                                        "phase_limit_claimed":False,"secular_zero_inverse_radius_scaling_claimed":False,
                                        "binomial_ledgers":binomial_ledgers(),"concentration_sentinels":concentration_ledgers()},
      "controls":{"closed_parent":{"projector":"I_3","result":"A_closed=F3^* is unitary; full-cycle degree is 3^k and its normalized log-modulus measure is delta_0"},
                  "projector_order":{"gate":"A_right=diag(1,0,1)F3^*=F3*A*F3^*","result":"unitary similarity preserves lambda_+/- and hence every full-cycle factor, measure, mean, variance, and limit"},
                  "moved_hole":{"projector":"diag(0,1,1)","nonzero_eigenvalues":"-i and -1/sqrt(3)","rank_and_degree":"rank powers remain 2 and full-cycle degree remains 2^k",
                                "mean":"mu remains -log(3)/4 because the nonzero product modulus remains 1/sqrt(3)",
                                "variance":"sigma_0^2=(log 3)^2/16, different from the frozen sigma^2","variance_changes":True,"mean_changes":False}},
      "route_a":{"tuple":["A1_WEAK","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"],"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},
      "claim_boundary":{"finite_and_growing_k_source_gate_only":True,"phase_limit":False,"self_adjoint_limit":False,"target_divisor_matching":False,
                        "target_functional_equation":False,"target_counting_law":False,"prime_like_correspondence":False,"arithmetic_local_data":False,
                        "euler_factors":False,"root_numbers":False,"automorphy":False,"hilbert_polya_operator":False}}
    payload["payload_sha256"]=canonical_hash(payload)
    return payload


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parents[1]/"results/c158_full_cycle_evidence.json")
    args=parser.parse_args();payload=build_evidence();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"C158_PRODUCER_PASS","payload_sha256":payload["payload_sha256"],"binomial_k_max":K_BINOMIAL_MAX,"polynomial_k_max":K_POLYNOMIAL_MAX},sort_keys=True))

if __name__=="__main__":main()
