#!/usr/bin/env python3
"""Independent residue-square, binomial, orbit-product and extension checker.

This module deliberately imports neither the producer nor its CM routine.
"""
import argparse
from collections import Counter
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0

def need(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise ValueError(message)

def strict(path):
    def unique(pairs):
        obj = {}
        for k, v in pairs:
            if k in obj:
                raise ValueError('duplicate JSON key')
            obj[k] = v
        return obj
    return json.loads(Path(path).read_text(), object_pairs_hook=unique,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))

def prime(p):
    return p > 1 and all(p % d for d in range(2, math.isqrt(p)+1))

def validate(path):
    data = strict(path)
    need(type(data) is dict, 'root mapping')
    keys = {'schema','candidate_id','obstruction_id','source_commit','scope_literal',
            'fixed_epoch','curve','good_primes','phase_convention','frobenius_convention',
            'determinant_convention','theorem_range','finite_grid','prime_ledger',
            'quadratic_extension_ledger','arithmetic_controls','route_tuple',
            'overall_verdict','native_results','mandatory_a1_controls_completed',
            'route_b_invocation_allowed','scope_flags','payload_sha256'}
    need(set(data) == keys, 'schema exact keys')
    payload = {k:v for k,v in data.items() if k != 'payload_sha256'}
    digest = hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    need(data['payload_sha256'] == digest, 'payload SHA')
    literals = dict(schema='hcs-c382-cm-evidence-v1',candidate_id='HCS-C382',
        obstruction_id='HEN-O366',source_commit='0596f9d680277288225062a6fdd7ad7ce116e01d',
        scope_literal='NO_BAD_EULER_OR_ROOT_NUMBER',fixed_epoch=1788566400,
        curve='y^2=x^3-x',good_primes='all odd primes',
        phase_convention='b>0,a odd,b even,a^2+b^2=p,a+b=1 mod 4; unordered conjugate eigenvalues',
        frobenius_convention='F(x,y)=(x^p,y^p); pullback eigenvalues H0=1,H1=alpha,beta,H2=p',
        determinant_convention='Z=(1-t*u+p*u^2)/((1-u)*(1-p*u))',
        theorem_range='all odd primes p and every n>=1',overall_verdict='ROUTE_A_EXPLORATORY')
    for k, v in literals.items():
        need(type(data[k]) is type(v) and data[k] == v, 'literal '+k)
    flags = {'claims_target_arithmetic_local_data','claims_target_euler_factors',
             'claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law',
             'claims_target_functional_equation','claims_target_zero_match',
             'claims_hilbert_polya_operator','invokes_route_b'}
    need(set(data['scope_flags']) == flags and all(v is False for v in data['scope_flags'].values()),'scope flags')
    need(data['route_tuple'] == ['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FORMAL_HINT'],'strict route')
    need(data['route_b_invocation_allowed'] is False,'Route B')
    need(type(data['mandatory_a1_controls_completed']) is int and data['mandatory_a1_controls_completed']==0,'A1 control claim')
    need(data['native_results'] == dict(all_degree_closed_points=True,graded_determinant=True,native_functional_equation=True,native_critical_circle=True)
         and all(v is True for v in data['native_results'].values()),'native claim lock')
    ps = [p for p in range(3,1001) if prime(p)]
    need(data['finite_grid']==dict(prime_max=1000,degree_max=24,prime_count=len(ps),prime_degree_cells=24*len(ps)),'grid')
    need(all(type(v) is int for v in data['finite_grid'].values()),'integer grid types')
    need([r['p'] for r in data['prime_ledger']]==ps,'complete prime ledger')
    for r in data['prime_ledger']:
        need(set(r)=={'p','chamber','trace','primary_upper_pair','fixed_counts','primitive_counts','direct_prime_count','quadratic_twist','parent_p1_counts'},'row schema')
        p = r['p']
        need(type(p) is int and type(r['direct_prime_count']) is int,'integer prime/count types')
        sq = Counter(y*y % p for y in range(p))
        N1 = 1 + sum(sq[(x*x*x-x)%p] for x in range(p))
        t = p+1-N1
        need(type(r['trace']) is int and r['trace']==t and r['direct_prime_count']==N1,'direct square count')
        need(len(r['fixed_counts'])==len(r['primitive_counts'])==24,'degree ledger length')
        if p%4==1:
            a,b = r['primary_upper_pair']
            need(all(type(x) is int for x in (a,b)) and b>0 and a%2==1 and b%2==0,'Gaussian parity')
            need(a*a+b*b==p and (a+b)%4==1 and 2*a==t,'primary sign and norm')
            need(N1%8==0 and r['chamber']=='ordinary','ordinary torsion')
            j = next(x for x in range(p) if x*x%p==p-1)
            slope = (3*j*j-1)*pow(2*(j-1),-1,p)%p
            need((slope*slope-2*j)%p==0 and (slope*j-(j-1))%p==0,'explicit 4-torsion')
        else:
            need(r['primary_upper_pair'] is None and t==0 and r['chamber']=='supersingular','inert zero trace')
        for n in range(1,25):
            if p%4==1:
                trace = 2*sum(math.comb(n,2*k)*a**(n-2*k)*(-b*b)**k for k in range(n//2+1))
            else:
                trace = 0 if n%2 else 2*(-p)**(n//2)
            expected = p**n+1-trace
            need(type(r['fixed_counts'][n-1]) is int and r['fixed_counts'][n-1]==expected,'extension binomial count')
            need(type(r['primitive_counts'][n-1]) is int and r['primitive_counts'][n-1]>=0,'primitive nonnegative integer')
            need(sum(d*r['primitive_counts'][d-1] for d in range(1,n+1) if n%d==0)==expected,'orbit decomposition')
            need(r['parent_p1_counts'][n-1]==p**n+1,'P1 control')
        # Multiply (1-u^d)^(-B_d) directly and compare Riemann--Roch coefficients.
        product = [1]+[0]*24
        for d, B in enumerate(r['primitive_counts'],1):
            factor = [math.comb(B+k-1,k) if B else int(k==0) for k in range(24//d+1)]
            product = [sum(product[n-k*d]*factor[k] for k in range(n//d+1)) for n in range(25)]
        need(product==[1]+[N1*(p**n-1)//(p-1) for n in range(1,25)],'primitive Euler product / Riemann-Roch')
        tw = r['quadratic_twist']
        need(all(type(v) is int for v in tw.values()),'integer twist types')
        d = next(v for v in range(2,p) if v not in sq)
        inv = pow(d,-1,p)
        twist_N = 1+sum(sq[(x*x*x-x)*inv%p] for x in range(p))
        need(tw==dict(nonsquare=d,point_count=twist_N,trace=-t),'direct quadratic twist')
    need([r['p'] for r in data['quadratic_extension_ledger']]==[p for p in ps if p<=43],'quadratic ledger complete')
    for r in data['quadratic_extension_ledger']:
        p,d = r['p'],r['nonsquare']
        need(all(type(v) is int for v in r.values()),'integer extension types')
        sq = Counter(((a*a+d*b*b)%p,(2*a*b)%p) for a in range(p) for b in range(p))
        total = 1
        for a in range(p):
            for b in range(p):
                cub = ((a*a*a+3*d*a*b*b-a)%p,(3*a*a*b+d*b*b*b-b)%p)
                total += sq[cub]
        parent = data['prime_ledger'][ps.index(p)]
        need(set(r)=={'p','degree','nonsquare','point_count'} and r['degree']==2,'extension schema')
        need(total==r['point_count']==parent['fixed_counts'][1],'quadratic field direct count')
    pp,mixed = [],[]
    for n in range(3,100,2):
        if not prime(n):
            factors = [p for p in range(2,n) if prime(p) and n%p==0]
            (pp if len(factors)==1 else mixed).append(n)
    need(data['arithmetic_controls']==dict(prime_power_labels=pp,mixed_composites=mixed,mixed_composite_field_characteristic=False,twist_trace_sign=-1,parent_h1_dimension=0),'arithmetic controls')
    need(data['arithmetic_controls']['mixed_composite_field_characteristic'] is False,'typed field characteristic flag')
    return CHECKS

if __name__=='__main__':
    if sys.flags.optimize:
        raise RuntimeError('C382 checker refuses optimized Python')
    parser=argparse.ArgumentParser()
    parser.add_argument('path',nargs='?',type=Path,default=ROOT/'results/c382_cm_evidence.json')
    print('C382 independent checker: PASS (%d assertions)'%validate(parser.parse_args().path))
