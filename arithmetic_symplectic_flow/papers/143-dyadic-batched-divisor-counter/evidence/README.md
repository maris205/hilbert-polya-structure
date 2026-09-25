# Evidence — ANG-20260915-DDC01

**Date:** 2026-09-15.  
**Status:** STOP PROMOTION — EXACT MARKED RETURNS; BATCH CLOCK NOT GEOMETRICALLY JUSTIFIED.

## All-integer proof versus bounded execution

The [paper](../paper.md) derives every theorem from the
[version-1 card](../candidate-card.md). Its dyadic coverage, counter return,
complete primitive ledger and sufficient product half-plane are proved for
all n>=2. The finite execution below corroborates the displayed formula
and catches implementation/edge errors; it cannot prove infinite claims.

No prime table, numerical prime logarithm, Riemann zeros, random sampling,
external source download or statistical fitting was used. The logarithmic
macroperiod follows from the frozen binary partition, not a prime-data fit.

## Exact command

Executed from arithmetic_symplectic_flow on 2026-09-15:

~~~sh
node - <<'JS'
function gcd(a,b){while(b){[a,b]=[b,a%b];}return a;}
let total=0;
for(let n=2;n<=20;n++){
 const K=Math.max(1,Math.floor(Math.log2(n-1)));
 const blocks=Array.from({length:K},(_,j)=>{const ds=[];for(let d=2**(j+1);d<2**(j+2)&&d<n;d++)ds.push(d);return ds;});
 const flat=blocks.flat(), target=Array.from({length:n-2},(_,j)=>j+2);
 if(flat.join(',')!==target.join(','))throw Error('coverage');
 const b=blocks.map(ds=>ds.reduce((s,d)=>s+(n%d===0?1:0),0));
 const a=b.reduce((s,t)=>s+t,0), g=gcd(n,a), T=K*n/g;
 const F=([k,c])=>[(k+1)%K,(c+b[k])%n];
 const inv=([k,c])=>{const j=(k+K-1)%K;return[j,(c-b[j]+n)%n];};
 const seen=new Set(), periods=[];
 for(let k=0;k<K;k++)for(let c=0;c<n;c++){
  const z0=[k,c], key=z0.join(',');
  if(inv(F(z0)).join(',')!==key)throw Error('inverse');
  let w=z0;for(let i=0;i<K;i++)w=F(w);
  if(w.join(',')!==[k,(c+a)%n].join(','))throw Error('scan');
  if(seen.has(key))continue;
  let z=z0,p=0;
  do{const q=z.join(',');if(seen.has(q))throw Error('collision');seen.add(q);p++;z=F(z);}while(z.join(',')!==key);
  periods.push(p);
 }
 if(periods.length!==g||periods.some(p=>p!==T)||seen.size!==K*n)throw Error('ledger');
 total+=seen.size;
 console.log([n,K,a,g,T,n-2].join(' '));
}
console.log('PASS all n=2..20; states='+total);
JS
~~~

Exit code: 0. Columns are n, K, a, g, T, and the number n-2 of elementary
candidate-divisor tests per complete scan:

~~~text
2 1 0 2 1 0
3 1 0 3 1 1
4 1 1 1 4 2
5 2 0 5 2 3
6 2 2 2 6 4
7 2 0 7 2 5
8 2 2 2 8 6
9 3 1 1 27 7
10 3 2 2 15 8
11 3 0 11 3 9
12 3 4 4 9 10
13 3 0 13 3 11
14 3 2 2 21 12
15 3 2 1 45 13
16 3 3 1 48 14
17 4 0 17 4 15
18 4 4 2 36 16
19 4 0 19 4 17
20 4 4 4 20 18
PASS all n=2..20; states=657
~~~

The code uses zero-based phase indices, equivalent to subtracting one from
the frozen phases 1,...,K. Every phase/counter state is enumerated. All
integer arithmetic is exactly representable in JavaScript Number in this
range. Math.log2 is used only for the displayed finite inputs 1,...,19;
the resulting blocks are exhaustively checked against the full candidate
interval. No numerical precision assertion for unbounded n is made.

## Independent bounded model audit

A separately dispatched reviewer read the frozen card and independently
derived the partition, inverse, return increment, gcd periods/multiplicity
and geometric-series product bound. It confirmed the n=2 exception to the
dyadic grouping inequality, the two n=2 fixed orbits, and the empty-block
behaviour of the block-cardinality control. It did not edit this package.
This is same-family model review, not peer review or a proof substitute.

The reviewer agreed that the exact macroperiod is not invalid: it belongs
to an explicitly defined autonomous action. The unsupported promotion is
from a chosen one-block unit of time to a canonical geometric or physical
prime-log clock. Both points are retained instead of declaring the
arithmetic mechanism external merely because its phase schedule is chosen.

The ARS argument/evidence checklist was used only to separate the exact
macroclock theorem from its stronger interpretation. No full publication
pipeline, external model transport, calibrated review or Route evaluation
was run.

The separate [clock-scope review](clock-scope-review.md) distinguishes a
valid autonomous macroclock from the unproved stronger timing claim and
supports a separately frozen geometric test, without credit transfer.
Its reading also identified a missing addition sign in Proposition 5's
displayed majorant; root corrected that typographical omission. The
correct estimate is 2 exp(-sigma) plus 2 sum_K (4 exp(-sigma))^K,
as required by the existing argument. No map, roof or theorem changed.

See [claim ledger](../claim-ledger.md) and [summary](../README.md).
