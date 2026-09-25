# Evidence — ANG-20260915-CDC01

**Date:** 2026-09-15.  
**Status:** ADVANCE — EXACT MARKED RETURN SELECTOR, COMPLETE PACKETS, LOCAL ORDINARY ZETA.

## Proof and input scope

The [paper](../paper.md) proves the inverse, arithmetic scan return, complete
primitive ledger and ordinary-product convergence for all n>=2 directly from
the [frozen version-1 card](../candidate-card.md). The proofs do not depend
on finite checks or a cited external theorem. Antecedents are the local
050 divisor-sieve construction and the scoped 031/052 ownership controls
linked in the paper; no historical Route credits are inherited.

No external prime table, logarithm table, zeros, numerical fitting, private
input or network lookup was used. This run checks the actual integer
divisibility test, not imported primality answers.

## Exact finite cross-check

Executed from the arithmetic_symplectic_flow workspace on 2026-09-15:

~~~sh
node - <<'JS'
function gcd(a,b){while(b){[a,b]=[b,a%b];}return a;}
let total=0;
for(let n=2;n<=20;n++){
 const L=Math.max(1,n-2), h=j=>j+2<n&&n%(j+2)===0?1:0;
 const a=Array.from({length:L},(_,j)=>h(j)).reduce((x,y)=>x+y,0);
 const F=([j,c])=>[(j+1)%L,(c+h(j))%n];
 const inv=([j,c])=>{const k=(j+L-1)%L;return[k,(c-h(k)+n)%n];};
 const seen=new Set(), periods=[];
 for(let j=0;j<L;j++)for(let c=0;c<n;c++){
  const state=[j,c], key=state.join(',');
  if(inv(F(state)).join(',')!==key)throw Error('inverse');
  let scan=state;
  for(let t=0;t<L;t++)scan=F(scan);
  if(scan.join(',')!==[j,(c+a)%n].join(','))throw Error('scan');
  if(seen.has(key))continue;
  let z=state,p=0;
  do{const k=z.join(',');if(seen.has(k))throw Error('orbit collision');seen.add(k);z=F(z);p++;}while(z.join(',')!==key);
  periods.push(p);
 }
 const g=gcd(n,a), T=L*n/g;
 if(periods.length!==g||periods.some(p=>p!==T)||seen.size!==L*n)throw Error('ledger');
 const prime=Array.from({length:Math.max(0,n-2)},(_,i)=>i+2).every(d=>n%d!==0);
 if((a===0)!==prime)throw Error('selector');
 total+=seen.size;
 console.log([n,L,a,g,T,seen.size].join(' '));
}
console.log('PASS all n=2..20; states='+total);
JS
~~~

Exit code: 0. Columns are n, L, a, g, T, visited states:

~~~text
2 1 0 2 1 2
3 1 0 3 1 3
4 2 1 1 8 8
5 3 0 5 3 15
6 4 2 2 12 24
7 5 0 7 5 35
8 6 2 2 24 48
9 7 1 1 63 63
10 8 2 2 40 80
11 9 0 11 9 99
12 10 4 4 30 120
13 11 0 13 11 143
14 12 2 2 84 168
15 13 2 1 195 195
16 14 3 1 224 224
17 15 0 17 15 255
18 16 4 2 144 288
19 17 0 19 17 323
20 18 4 4 90 360
PASS all n=2..20; states=2453
~~~

All integer values in this range are exactly representable in JavaScript
Number. Enumeration visits every scan phase and counter, not just one
seed. The arithmetic predicate cross-check uses the same elementary
divisibility characterization, so it is not independent evidence for
primality theory. The inverse, scanned update and exhaustive orbit census
are independent implementation comparisons with the derived formulas.
Nothing in this finite test certifies the infinite product or an
unbounded statement; those rely on the proofs.

## Independent bounded model audit

A separately dispatched agent, given the frozen card and formula questions,
independently confirmed the inverse, n=2 and n=3 edge cases, complete
gcd multiplicity and period formula, right-half-plane product estimate,
and the three distinct controls. It did not edit the paper and was not
given a draft to rationalize. This is same-family model review, not peer
review, a calibrated scientific assessment or a proof substitute.

The strongest qualification it identified was retained: prime recognition
is a marked first-scan return statement, not a one-prime-per-unmarked-length
dictionary. The global carrier is all integer instances of one fixed rule,
not one chronological orbit enumerating primes. Algorithmic naturalness
therefore remains qualified even though source and return owners agree.

The ARS argument-builder claim/evidence/counterargument checklist was used
to keep this exact positive result separate from the clock, operator and
naturalness limitations. No full ARS publication pipeline, external model
transport, journal assessment or submission-readiness gate was run.

The separate [carrier-scope audit](carrier-scope-audit.md) checks why the
uniform all-integer carrier is not automatically a supplied-prime carrier.
It is a scope assessment, not an independent proof of the arithmetic theorem.

See also the [claim ledger](../claim-ledger.md) and [summary](../README.md).
