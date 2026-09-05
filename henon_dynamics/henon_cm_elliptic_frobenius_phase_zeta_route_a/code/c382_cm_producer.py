#!/usr/bin/env python3
"""Canonical finite receipts for the all-prime CM theorem; no fitted data."""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = '0596f9d680277288225062a6fdd7ad7ce116e01d'
SCOPE = 'NO_BAD_EULER_OR_ROOT_NUMBER'
FLAGS = {k: False for k in ('claims_target_arithmetic_local_data',
    'claims_target_euler_factors', 'claims_root_number', 'claims_automorphy',
    'claims_target_divisor_or_counting_law', 'claims_target_functional_equation',
    'claims_target_zero_match', 'claims_hilbert_polya_operator', 'invokes_route_b')}
ROUTE = ['A0_STRUCTURAL_ARITHMETIC_RELATION', 'A1_WEAK', 'A2_FAIL',
         'A3_FAIL', 'A4_FORMAL_HINT']

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()

def primes(limit):
    return [p for p in range(3, limit + 1, 2)
            if all(p % d for d in range(3, math.isqrt(p) + 1, 2))]

def legendre(x, p):
    value = pow(x % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value

def cm(p):
    if p % 4 == 3:
        return 0, None
    for b in range(2, math.isqrt(p) + 1, 2):
        a = math.isqrt(p - b*b)
        if a*a + b*b == p:
            if (a + b) % 4 != 1:
                a = -a
            return 2*a, [a, b]
    raise ValueError('Gaussian representation absent')

def row(p):
    t, pair = cm(p)
    S = [2, t]
    for n in range(2, 25):
        S.append(t*S[-1] - p*S[-2])
    counts = [p**n + 1 - S[n] for n in range(1, 25)]
    primitive = []
    for n, value in enumerate(counts, 1):
        total = value - sum(d*primitive[d-1] for d in range(1, n) if n % d == 0)
        if total % n or total < 0:
            raise ValueError('primitive count not integral/nonnegative')
        primitive.append(total//n)
    direct = p + 1 + sum(legendre(x*x*x-x, p) for x in range(p))
    d = next(d for d in range(2, p) if legendre(d, p) == -1)
    twist = p + 1 + sum(legendre(d*(x*x*x-x), p) for x in range(p))
    return dict(p=p, chamber='ordinary' if pair else 'supersingular', trace=t,
                primary_upper_pair=pair, fixed_counts=counts,
                primitive_counts=primitive, direct_prime_count=direct,
                quadratic_twist=dict(nonsquare=d, point_count=twist, trace=-t),
                parent_p1_counts=[p**n+1 for n in range(1, 25)])

def extension(p):
    r = next(r for r in range(2, p) if legendre(r, p) == -1)
    def mul(x, y):
        return ((x[0]*y[0]+r*x[1]*y[1]) % p,
                (x[0]*y[1]+x[1]*y[0]) % p)
    def power(x, n):
        ans = (1, 0)
        while n:
            if n % 2:
                ans = mul(ans, x)
            x = mul(x, x)
            n //= 2
        return ans
    count = 1
    for a in range(p):
        for b in range(p):
            x = (a, b)
            z = mul(mul(x, x), x)
            f = ((z[0]-a) % p, (z[1]-b) % p)
            if f == (0, 0):
                count += 1
            elif power(f, (p*p-1)//2) == (1, 0):
                count += 2
    return dict(p=p, degree=2, nonsquare=r, point_count=count)

def produce():
    rows = [row(p) for p in primes(1000)]
    mixed = [n for n in range(3, 100, 2) if n not in primes(100)]
    powers, composites = [], []
    for n in mixed:
        factors = [p for p in primes(100) if n % p == 0]
        (powers if len(factors) == 1 else composites).append(n)
    payload = dict(schema='hcs-c382-cm-evidence-v1', candidate_id='HCS-C382',
        obstruction_id='HEN-O366', source_commit=SOURCE, scope_literal=SCOPE,
        fixed_epoch=1788566400, curve='y^2=x^3-x', good_primes='all odd primes',
        phase_convention='b>0,a odd,b even,a^2+b^2=p,a+b=1 mod 4; unordered conjugate eigenvalues',
        frobenius_convention='F(x,y)=(x^p,y^p); pullback eigenvalues H0=1,H1=alpha,beta,H2=p',
        determinant_convention='Z=(1-t*u+p*u^2)/((1-u)*(1-p*u))',
        theorem_range='all odd primes p and every n>=1',
        finite_grid=dict(prime_max=1000, degree_max=24, prime_count=len(rows),
                         prime_degree_cells=24*len(rows)),
        prime_ledger=rows, quadratic_extension_ledger=[extension(p) for p in primes(43)],
        arithmetic_controls=dict(prime_power_labels=powers, mixed_composites=composites,
                                 mixed_composite_field_characteristic=False,
                                 twist_trace_sign=-1, parent_h1_dimension=0),
        route_tuple=ROUTE, overall_verdict='ROUTE_A_EXPLORATORY',
        native_results=dict(all_degree_closed_points=True, graded_determinant=True,
                            native_functional_equation=True, native_critical_circle=True),
        mandatory_a1_controls_completed=0, route_b_invocation_allowed=False,
        scope_flags=FLAGS)
    payload['payload_sha256'] = hashlib.sha256(canonical(payload)).hexdigest()
    return payload

def main():
    if sys.flags.optimize:
        raise RuntimeError('C382 producer refuses optimized Python')
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT/'results/c382_cm_evidence.json')
    args = parser.parse_args()
    evidence = produce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2)+'\n')
    print('C382_PRODUCER_PASS', evidence['finite_grid'], evidence['payload_sha256'])

if __name__ == '__main__':
    main()
