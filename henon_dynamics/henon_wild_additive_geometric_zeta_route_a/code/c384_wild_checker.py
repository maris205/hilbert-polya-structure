#!/usr/bin/env python3
"""Independent modular sparse-polynomial and finite-field matrix validator."""
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
TOTAL=0

def require(x,message):
    global TOTAL
    TOTAL+=1
    if not x:raise ValueError(message)

def unique(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate JSON key');out[k]=v
    return out

def load(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=unique,
      parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite '+x)))

def mu(n):
    primes=[];d=2
    while d*d<=n:
        if n%d==0:
            n//=d;primes.append(d)
            if n%d==0:return 0
        d+=1
    if n>1:primes.append(n)
    return (-1)**len(primes)

def ds(n):return [d for d in range(1,n+1) if n%d==0]

def ppart(n,p):
    ans=1
    while n%p==0:n//=p;ans*=p
    return ans

def sparse_remainder(a,b,p):
    a=dict(a)
    while a and max(a)>=max(b):
        shift=max(a)-max(b);factor=a[max(a)]*pow(b[max(b)],p-2,p)%p
        for j,v in b.items():
            k=j+shift;a[k]=(a.get(k,0)-factor*v)%p
            if a[k]==0:a.pop(k)
    return a

def sparse_gcd(a,b,p):
    while b:a,b=b,sparse_remainder(a,b,p)
    fac=pow(a[max(a)],p-2,p)
    return [a.get(k,0)*fac%p for k in range(max(a)+1)]

def rank(a,p):
    a=[list(r) for r in a];h=0
    for j in range(len(a[0])):
        pivot=next((k for k in range(h,len(a)) if a[k][j]%p),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h];inv=pow(a[h][j],p-2,p)
        a[h]=[x*inv%p for x in a[h]]
        for k in range(len(a)):
            if k!=h:
                c=a[k][j];a[k]=[(x-c*y)%p for x,y in zip(a[k],a[h])]
        h+=1
    return h

def matrix_recount(p,r,mod):
    cols=[]
    b={i:v for i,v in enumerate(mod) if v}
    for j in range(r):
        rem=sparse_remainder({j*p:1},b,p)
        cols.append([(rem.get(i,0)+(i==j))%p for i in range(r)])
    a=[[cols[j][i] for j in range(r)] for i in range(r)]
    it=[[int(i==j) for j in range(r)] for i in range(r)];out=[]
    for _ in range(12):
        it=[[sum(it[i][k]*a[k][j] for k in range(r))%p for j in range(r)] for i in range(r)]
        delta=[[(it[i][j]-(i==j))%p for j in range(r)] for i in range(r)]
        out.append(p**(r-rank(delta,p)))
    return out

def same(actual,expected,message):
    require(type(actual) is type(expected),message+' type')
    if isinstance(expected,dict):
        require(set(actual)==set(expected),message+' keys')
        for k,v in expected.items():same(actual[k],v,message+'.'+k)
    elif isinstance(expected,list):
        require(len(actual)==len(expected),message+' length')
        for a,b in zip(actual,expected):same(a,b,message+' item')
    else:require(actual==expected,message)

def check(path):
    data=load(path);require(set(data)=={'payload','payload_sha256'},'outer schema')
    x=data['payload'];require(type(x) is dict,'payload type')
    require(hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()==data['payload_sha256'],'payload hash')
    require(set(x)=={'schema','candidate_id','source_commit','scope_literal','route_tuple','scope_flags',
      'route_b_invocation_allowed','source','grid','period_rows','extension_rows','neighbor_controls',
      'direct_field_recounts','residue_intervals','interior_tail_bounds','composite_characteristic_controls','proof_scope'},'payload schema')
    same(x['schema'],'hcs-c384-wild-v1','schema');same(x['candidate_id'],'HCS-C384','candidate')
    same(x['source_commit'],'3e692da6fa94362225c7534e9b66c83c15c7f284','baseline')
    same(x['scope_literal'],'NO_BAD_EULER_OR_ROOT_NUMBER','firewall')
    same(x['route_tuple'],['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FAIL'],'tuple')
    flags={'claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number',
      'claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation',
      'claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b'}
    require(set(x['scope_flags'])==flags and all(v is False for v in x['scope_flags'].values()),'scope flags')
    require(x['route_b_invocation_allowed'] is False,'Route B')
    same(x['source'],dict(map='x+x^p',space='A1(Fbar_p)',clock='iterate n',arithmetic_clock='extension r',
      geometric_zeta='exp(sum N_n z^n/n)',length_zeta='1/(1-p*z)',boundary='abs(z)=1/p'),'source')
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
    same(x['grid'],dict(primes=primes,period_n_max=96,extension_primes=primes[:5],extension_n_max=48,
      extension_r_max=24,period_rows=1344,extension_rows=5760,control_rows=896),'grid')
    require(len(x['period_rows'])==1344,'period coverage')
    for row,(p,n) in zip(x['period_rows'],((p,n) for p in primes for n in range(1,97))):
        e=ppart(n,p);count=p**(n-e);primitive=sum(mu(n//d)*p**(d-ppart(d,p)) for d in ds(n))
        require(primitive>=0 and primitive%n==0,'primitive integrality')
        same(row,dict(p=p,n=n,valuation_power=e,geometric=count,multiplicity=p**e,
          scheme_length=p**n,primitive_cycles=primitive//n),'period row')
        require(row['geometric']*row['multiplicity']==row['scheme_length'],'scheme reconstruction')
        require(all(type(v) is int for v in row.values()),'period integer types')
    require(len(x['extension_rows'])==5760,'extension coverage');lookup={}
    for row,(p,n,r) in zip(x['extension_rows'],((p,n,r) for p in primes[:5] for n in range(1,49) for r in range(1,25))):
        a={j:comb(n,j)%p for j in range(1,n+1) if comb(n,j)%p};b={0:p-1,r:1}
        g=sparse_gcd(a,b,p);count=p**(len(g)-1);lookup[p,n,r]=count
        exact=sum(mu(n//i)*mu(r//j)*lookup[p,i,j] for i in ds(n) for j in ds(r))
        require(exact>=0 and exact%n==0,'joint Möbius integrality')
        same(row,dict(p=p,n=n,r=r,gcd=g,count=count,exact_period_degree_points=exact,exact_degree_cycles=exact//n),'extension row')
        require(all(type(row[k]) is int for k in row if k!='gcd') and all(type(v) is int for v in g),'extension integer types')
    require(len(x['neighbor_controls'])==896,'neighbor coverage')
    for row,(p,a,n) in zip(x['neighbor_controls'],((p,a,n) for p in primes[:5] for a in range(p) for n in range(1,33))):
        d=next((k for k in range(1,p) if pow(a,k,p)==1),0)
        poly=[(comb(n,j)*pow(a,n-j,p)-(j==0))%p for j in range(n+1)]
        j=next(k for k,c in enumerate(poly) if c)
        same(row,dict(p=p,a=a,n=n,unit_order=d,geometric=p**(n-j)),'neighbor polynomial')
    require(len(x['direct_field_recounts'])==9,'recount coverage')
    for row,(p,r) in zip(x['direct_field_recounts'],((p,r) for p in [2,3,5] for r in [1,2,3])):
        require(type(row) is dict and set(row)=={'p','r','modulus','counts'},'recount schema')
        same(row['p'],p,'recount prime exact type')
        same(row['r'],r,'recount extension exact type')
        mod=row['modulus'];require(len(mod)==r+1 and mod[-1]==1 and all(type(a) is int and 0<=a<p for a in mod),'modulus shape')
        if r>1:require(all(sum(a*pow(t,j,p) for j,a in enumerate(mod))%p for t in range(p)),'irreducible small modulus')
        same(row['counts'],matrix_recount(p,r,mod),'matrix vs direct recount')
        same(row['counts'],[lookup[p,n,r] for n in range(1,13)],'recount vs gcd')
    require(len(x['residue_intervals'])==9,'residue coverage')
    for row,(p,k) in zip(x['residue_intervals'],((p,k) for p in [2,3,5] for k in [1,2,3])):
        lower=sum((Fraction(1,p**(p**(j-1)))-Fraction(1,p**(p**j)))/p**j for j in range(k,5))
        upper=lower+Fraction(1,p**(5+p**4));bound=Fraction(1,p**(k+p**(k-1)))
        expected=dict(p=p,K=k,J=4,residue_lower=[lower.numerator,lower.denominator],
          residue_upper=[upper.numerator,upper.denominator],universal_upper=[bound.numerator,bound.denominator])
        same(row,expected,'residue bounds');require(0<lower<upper<=bound<1,'noninteger residue')
    require(len(x['interior_tail_bounds'])==18,'tail coverage')
    for row,(p,k,rho) in zip(x['interior_tail_bounds'],((p,k,rho) for p in [2,3,5] for k in range(3) for rho in [Fraction(1,2),Fraction(3,4)])):
        h=p**(k+1);bound=rho**h/(p**(p**k)*(1-rho**h))
        same(row,dict(p=p,K=k,rho=[rho.numerator,rho.denominator],bound=[bound.numerator,bound.denominator]),'tail bound')
    same(x['composite_characteristic_controls'],[dict(label=c,admissible=False) for c in [6,10,12,14,15,18,20,21,22,24]],'composite controls')
    same(x['proof_scope'],'all primes p, n>=1 and r>=1; finite grid is regression only','proof scope')
    return TOTAL

def main():
    if sys.flags.optimize:raise RuntimeError('C384 checker refuses optimized Python')
    path=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'results/c384_wild_evidence.json'
    total=check(path);print('C384_CHECKER_PASS assertions='+str(total))

if __name__=='__main__':main()
