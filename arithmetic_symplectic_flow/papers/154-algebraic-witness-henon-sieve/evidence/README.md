# Evidence — ASFS-20260915-AWH01

Status: **PRIME-ONLY HYPERBOLIC SYMPLECTIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.**

## Exact proof coverage

The [paper](../paper.md) proves the map and inverse on every real plane,
the sign obstruction for every composite and every period, all prime
periodic states, primitive multiplicity, suspension completeness,
monodromy, repetitions and the ordinary product's exact logarithmic-series
absolute-convergence boundary. No orbit cutoff or finite numerical sample
is used to establish an infinite claim.

The convergence proof includes an elementary proof of divergence of
\(\sum_p1/p\), so it does not depend on a recalled prime-number theorem
or an unverified external analytic result.

The [independent model review](review.md) is a separate delegated model
audit, not human peer review or a mathematical certification.

## Finite arithmetic regression method

The following reproducible Node command evaluates all divisor witnesses
for \(2\leq n\leq20\), checks against a differently bounded trial-division
predicate, checks shifted-test outcomes, and prints the phase ledger
predicted by the exact theorem. It does not enumerate real periodic
states and is not evidence of all-period completeness.

~~~sh
node <<'JS'
const rows=[];
const prime=n=>{
  if(n<2)return false;
  for(let d=2;d*d<=n;d++)if(n%d===0)return false;
  return true;
};
let directTests=0, failures=0;
for(let n=2;n<=20;n++){
  const K=Math.max(1,Math.floor(Math.log2(n-1)));
  let a=0,shift=0;
  for(let d=2;d<n;d++){
    directTests++;
    a+=Number(n%d===0);
    shift+=Number((n+1)%d===0);
  }
  if((a===0)!==prime(n))failures++;
  if((shift===0)!==prime(n+1))failures++;
  rows.push([n,K,a,Number(a===0),K*(n-2)].join(','));
}
console.log('n,K,a,primitive_packets,direct_tests_per_phase_cycle');
console.log(rows.join('\n'));
console.log(JSON.stringify({directTests,failures}));
if(failures)process.exit(1);
JS
~~~

Execution on 2026-09-15 returned exit code 0 and the following output:

~~~text
n,K,a,primitive_packets,direct_tests_per_phase_cycle
2,1,0,1,0
3,1,0,1,1
4,1,1,0,2
5,2,0,1,6
6,2,2,0,8
7,2,0,1,10
8,2,2,0,12
9,3,1,0,21
10,3,2,0,24
11,3,0,1,27
12,3,4,0,30
13,3,0,1,33
14,3,2,0,36
15,3,2,0,39
16,3,3,0,42
17,4,0,1,60
18,4,4,0,64
19,4,0,1,68
20,4,4,0,72
{"directTests":171,"failures":0}
~~~

Integer
inputs and divisibility operations in this range are exact in JavaScript;
the integer powers near which the binary floor is taken are exactly
representable. No floating-point force iteration, interval certification
or symbolic software package is used.

## Limits and ownership

No prime table, per-prime parameter, zero data, changed roof, selected
periodic centre, discarded composite state, or imported determinant occurs.
The full aggregation is still an explicit computational arithmetic
construction; the ordinary zeta is not declared to be an operator trace.
The approved Markdown-only scope is preserved.

## Package verification

On 2026-09-15, a filesystem-based recursive Markdown link check covered
all six package files and 26 local links: zero missing targets. The
four core documents carried the same ASFS-20260915-AWH01 identifier.
The checker found no unintended trailing whitespace, and the scoped
git diff whitespace check returned no errors. These are artifact checks,
not mathematical gate evidence. The independent review identified no
required mathematical revision.
