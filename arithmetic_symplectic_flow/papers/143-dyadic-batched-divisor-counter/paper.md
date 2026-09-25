# A logarithmic macroperiod from dyadic divisor batching

**Paper ID:** 143-dyadic-batched-divisor-counter.  
**Candidate ID:** ANG-20260915-DDC01.  
**Date:** 2026-09-15.  
**Status:** STOP PROMOTION — EXACT MARKED RETURNS; BATCH CLOCK NOT GEOMETRICALLY JUSTIFIED.  
**Route state:** broadened T0--T3 owner audit; classical A0/A1/A2 NOT
APPLICABLE; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The frozen action processes one dyadic block of proper-divisor candidates per
step and retains every integer, batch phase and modular counter. It is a
new reversible action, not a roof change on a serial-scan comparator.
The counter displacement at first batch-phase return recognizes primes
exactly. If a(n) is the proper-divisor count and g(n)=gcd(n,a(n)), the full
n-fibre has g(n) primitive cycles of length K_n n/g(n). In particular prime
p has p cycles of length K_p=log_2 p+O(1). Its complete ordinary unit-roof
product converges on Re(s)>2 log 2. This is a mathematically genuine
macroclock of the frozen batched action. However, a complete batch cycle
still entails n-2 individual divisor tests. No geometry or physical timing
principle establishes the binary batching convention as a canonical
prime-log clock. Promotion stops at that interpretation boundary, preserving
the exact arithmetic return, complete multiplicities and local product.

## 1. Identity, source and ownership

The [version-1 card](candidate-card.md) was frozen before theorem claims or
computations. Its entire carrier and action are

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
Y=\coprod_{n\geq2}\{n\}\times\{1,\ldots,K_n\}\times\mathbb Z/n\mathbb Z,
\]
\[
B(n,k)=\{d:2^k\leq d<2^{k+1},\ d<n\},\qquad
b(n,k)=\sum_{d\in B(n,k)}\mathbf1_{\{d\mid n\}},
\]
\[
F(n,k,c)=(n,k^+,c+b(n,k)\bmod n).
\]

Here k^+=k+1 except that K_n^+=1. The expression for K_n can be computed
from the binary length of n-1; no supplied logarithmic prime table is used.
The n=2 fibre has one empty block and two counter states.

| Item | Same frozen owner | Status |
| --- | --- | --- |
| Carrier and category | Full countable discrete Y; transformation groupoid Y crossed with Z | Defined and audited below |
| Action | One complete dyadic block per F step | Uniform autonomous local-block rule |
| Arithmetic source | Divisor witnesses computed during F | No precompleted mask or prime-selected fibre |
| Marked observable | n, phase k and complete modular counter | First-phase-return displacement |
| Clock and flow | Unit roof for this macro-action; its suspension | Not the serial-action clock |
| Primitive ledger | All full F-cycles, modulo cyclic phase | Every counter and composite fibre retained |
| Analytic object | Complete ordinary unweighted packet product | Sufficient convergence half-plane proved |
| Geometry and operator | Classical symplectic/contact/Hamiltonian/quantum owner; operator/domain/trace | NOT APPLICABLE / NOT SUPPLIED |

The precise [prior-work](../../docs/prior_work/README.md) arrow retained is
prime/composite divisor exclusion, followed by sequential witness
accumulation, followed by a reversible dyadic-block deformation retaining
the entire phase and counter. This is a replacement of the chronological
source mechanism of
[050](../050-causal-binary-sieve-fixed-point-screen/paper.md), not a claimed
conjugacy or an already completed Hénon/symplectic lift.

[140](../140-cyclic-divisor-counter/paper.md) is a separate serial-scan
comparator. Its roof, cycles, zeta and theorems are not transferred here.
The present map has fewer phase states and a different complete state
transition. In particular its unit roof does not retime the unchanged
140 action.

## 2. Exact batch coverage and return

### Proposition 1 — Every proper-divisor candidate occurs once

For n>=3 the blocks k=1,...,K_n partition {2,...,n-1}. For n=2 the only
block is empty. Consequently

\[
\sum_{k=1}^{K_n}|B(n,k)|=n-2,\qquad
\sum_{k=1}^{K_n}b(n,k)=
a(n):=\#\{d:2\leq d<n,\ d\mid n\}.
\]

**Proof.** For n>=3, K_n=floor(log_2(n-1)) and hence
2^{K_n}<=n-1<2^{K_n+1}. The dyadic intervals
[2^k,2^{k+1}), k=1,...,K_n, are disjoint and cover every integer from
2 through n-1 after intersection with d<n. For n=2, the condition
2<=d<2 is empty. Summing the cardinalities and witness indicators proves
both identities. QED.

### Proposition 2 — Full inverse and prime-return selector

F is a homeomorphism of Y, and for all complete states

\[
F^{K_n}(n,k,c)=(n,k,c+a(n)\bmod n).
\]

Furthermore 0<=a(n)<=n-2<n, so

\[
F^{K_n}(n,k,c)=(n,k,c)
\quad\Longleftrightarrow\quad n\text{ is prime}.
\]

**Proof.** Let k^- be the preceding cyclic phase. The inverse image of
(n,k,c) is uniquely (n,k^-,c-b(n,k^-) modulo n). Both maps are continuous
because Y is discrete. Over K_n steps every block is processed once.
Proposition 1 gives the displayed return formula, independent of starting
phase and counter.

The witness count lies between zero and n-2, so reduction modulo n cannot
turn a nonzero witness count into zero. A prime has no proper divisor;
if n is composite, n=uv with u,v>=2 supplies a divisor 2<=u<n. This
proves the equivalence, including the empty-test prime n=2. QED.

This is an exact marked return selector inside one uniform action, not a
single orbit enumerating the primes. All n and all counters are present
before and after the audit. The source equivalence with the square-root
sieve follows because every composite has a proper divisor no greater
than its square root; the temporal evolution itself is different.

The groupoid uses arrows (y,m) from y to F^m y. It is countable discrete,
locally compact Hausdorff and étale. No positive-dimensional symplectic
interpretation is assigned to a discrete carrier.

## 3. Full primitive ledger and the actual macroclock

### Proposition 3 — Complete periods and multiplicity

Let g(n)=gcd(n,a(n)), with gcd(n,0)=n. Every state over n has least
F-period

\[
T(n)=K_n n/g(n),
\]

and the n-fibre contains exactly g(n) distinct primitive cycles.

**Proof.** Full-state return requires phase return, so its time is a
multiple mK_n. By Proposition 2 it is a return exactly when
ma(n)=0 modulo n. The least positive m is the additive order n/g(n).
There are K_n n states in the whole fibre, all having that period, hence
K_n n/T(n)=g(n) cycles. This counts every counter coset and makes no
zero-seed selection. QED.

Define the unit-roof suspension by

\[
S=(Y\times[0,1])/((y,1)\sim(Fy,0)).
\]

It is complete: at time t from representative (y,u), use
m=floor(u+t), state F^m y and height u+t-m. Only finitely many unit-roof
crossings occur in any bounded time interval. Returning to the same
suspension point requires integer elapsed time and a full base-state
return. Thus its primitive lengths are exactly T(n), and r traversals
have length rT(n). Orientation is not further quotiented. There is no
differential monodromy on the discrete base to infer or import.

### Proposition 4 — Prime macroperiod and test count

A prime p contributes p distinct primitive cycles, each with macroperiod
K_p. For p>2,

\[
0<\log_2 p-K_p<1,\qquad
\frac{K_p}{\log p}\longrightarrow\frac1{\log2}
\quad(p\longrightarrow\infty\text{ through primes}).
\]

However, executing the displayed update by evaluating each indicator once
uses p-2 elementary divisibility tests along one such primitive cycle.
For general n the corresponding complete primitive traversal uses
(n-2)n/g(n) individual tests.

**Proof.** Prime p has a(p)=0 and g(p)=p, so Proposition 3 gives the
period and multiplicity. For p>2,
2^{K_p}<p<=2^{K_p+1}; the upper equality would make p an even power
of two greater than two and is impossible. Taking base-two logarithms
gives the strict inequalities. Dividing the bounded error by log p
gives the limit. No prime-distribution estimate is used.

Proposition 1 counts exactly n-2 candidate tests per complete batch
cycle, and a primitive traversal uses n/g(n) such cycles. This counts
the operations of the displayed direct implementation, not a lower bound
for every possible primality algorithm or a constant-time arithmetic
model. The n=2 primitive cycles have one macrostep and zero tested
divisors. QED.

Thus the logarithmic macroperiod is true for this mathematical action.
What is not proved is that one increasingly large finite block should
consume a fixed unit of geometric or physical time. Binary batching is a
public architectural choice on all integers, not a hidden prime-specific
fit; that fact alone does not make its time units canonical.

## 4. Same-object ordinary product

### Proposition 5 — A sufficient convergence half-plane

The full frozen ordinary product is

\[
Z_{\rm DDC}(s)=
\prod_{n\geq2}
\left(1-e^{-sK_n n/g(n)}\right)^{-g(n)}.
\]

It is holomorphic and nonzero on Re(s)>2 log2, with locally absolutely
convergent repetition logarithm

\[
\log Z_{\rm DDC}(s)
=\sum_{n\geq2}g(n)\sum_{r\geq1}\frac{e^{-srT(n)}}r .
\]

Here 2 log2 means twice the natural logarithm of 2.

**Proof.** Write sigma=Re(s). Because T(n)>=K_n and g(n)<=n,
it suffices to sum n exp(-sigma K_n). Isolate n=2. For n>=3 and K_n=K,
the integers satisfy 2^K<n<=2^{K+1}; there are 2^K of them and each is
at most 2^{K+1}. Consequently

\[
\sum_{n\geq2}g(n)e^{-\sigma T(n)}
\leq2e^{-\sigma}
+2\sum_{K\geq1}\left(4e^{-\sigma}\right)^K<\infty
\]

when sigma>log4=2 log2. Since T(n)>=1, the repetition sum is bounded
by this quantity divided by 1-e^{-sigma}. These bounds are uniform
when sigma has any fixed lower bound greater than log4. The logarithm
therefore converges locally uniformly to a holomorphic function; its
exponential gives the claimed nonzero product with the complete packet
multiplicities. QED.

This is only a sufficient half-plane. The exact abscissa, boundary
behaviour, analytic continuation, operator/trace owner and target divisor
are OPEN. The formula is not an Euler product over primes only:
composite packets and p-fold prime multiplicities are still present.
No normalization converts its repetitions into a prime-power trace
formula in this record.

## 5. Controls and the clock-promotion boundary

All controls below are separate comparison objects.

| Control | Exact result | Boundary |
| --- | --- | --- |
| Set every block increment b to zero | Every integer passes phase return; n cycles of length K_n | Binary phase geometry alone does not recognize primes |
| Replace b(n,k) by cardinality of B(n,k) | Complete increment n-2; only n=2 passes phase return | n>=3 primes lose the zero-witness return; n=2 empty-block edge retained |
| Serial scan 140 | Complete increment still a(n), but period L_n n/g(n) | Arithmetic return can survive a different true action while its clock changes |
| Count the tests inside each displayed block | n-2 tests per full scan, not K_n constant-work tests | Logarithmic schedule depth is not established geometric elapsed time |
| Retain all counter states | Prime p has p cycles; composites also close | No representative selection may create a one-prime/one-packet ledger |

For example primes 5 and 7 both have macroperiod 2, with respectively
five and seven primitive packets. The unmarked period does not uniquely
identify a prime even within the prime sector. Their serial comparator
periods are 3 and 5; substituting those serial lengths into this product
would violate ownership.

The carrier is not external merely because n is conserved or the binary
partition is chosen. The actual fixed F computes all divisor witnesses
and its marked return is genuinely arithmetic. The narrower adverse
finding is that the tested source/clock relationship does not justify a
geometric meaning for a unit-cost batch of unbounded cardinality.
Replacing the binary blocks or roof to rescue that interpretation would
require another frozen candidate. No such rescue is performed.

## 6. Gate assessment and decision

| Gate | Evidence for ANG-20260915-DDC01 | Status | Limitation |
| --- | --- | --- | --- |
| T0 | Exact uniform action, inverse, groupoid and suspension | ESTABLISHED | Broadened discrete category only |
| T1 arithmetic | Complete marked phase return iff prime, mechanism controls | ESTABLISHED FOR MARKED RETURN | Engineered bounded-witness scan |
| T1 clock | Exact K_p=log_2 p+O(1) macroperiod | ESTABLISHED AS MACROCLOCK; GEOMETRIC INTERPRETATION OPEN | Increasing block work is hidden inside each unit step |
| T2 | Every cycle, counter multiplicity and repetition | ESTABLISHED | p cycles per prime; composite packets retained |
| T3 | Same complete ordinary product on Re(s)>2 log2 | ESTABLISHED FOR LOCAL PRODUCT ONLY | Sufficient, not exact half-plane; operator and continuation OPEN |
| Classical A0/A1/A2 | No positive-dimensional symplectic owner | NOT APPLICABLE | No geometric lift credit |
| Formal Route A / Route B | No formal evaluation or readiness | UNASSIGNED / NOT INVOKED | No target/prime-power trace conclusion |

**Decision: stop promotion; portfolio fork.** Preserve the exact marked
arithmetic return, logarithmic macroperiod, complete packet ledger and
same-object ordinary product. Do not promote a chosen batching convention
to a canonical geometric prime-log clock. The planned discriminator has
been applied; no further tuning, new blocking schedule or operator
construction is undertaken under this ID.

## Evidence and reproducibility

The proofs cover all integers. A finite exact check independently
enumerates all 657 states for 2<=n<=20 and verifies block coverage,
inverse, complete return and the full period/multiplicity formulas.
It is corroboration, not a proof of the infinite conclusions.

- [Frozen card and audit addendum](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Package summary](README.md)
- [Commands, output and bounded model review](evidence/README.md)

No prime table, Riemann-zero data, fitted weights, external upload or
publication artifact is used. This is a model-assisted internal note,
not externally peer reviewed or venue calibrated. No human/animal study
is involved; human authorship, funding and conflict declarations have
not been supplied or inferred.
