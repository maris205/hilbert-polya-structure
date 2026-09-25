# Fermat congruence scan: exact prime selection with infinite register packets

**Paper ID:** `231-fermat-congruence-register`  
**Candidate ID:** `ANG-20260918-FCR01`  
**Date:** `2026-09-18`  
**Status:** `STOP — PRIME SEPARATION, INFINITE REGISTER MULTIPLICITY AND NON-LOG CLOCK`  
**Evidence:** exact proofs; no numerical experiment.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The full discrete carrier consists of all integer triples (n,a,k) with
n>=2, 1<=a<n and k in Z. A cyclic scan of a performs the local test
a^(n-1)=1 modulo n and adds each failure to k. This defines a bijective
skew action and a complete groupoid suspension with the fixed roof
tau(n,a,k)=1+1/(n+a). The accumulated defect vanishes exactly on prime
fibres: Fermat's elementary permutation argument gives the prime
direction, while any proper divisor supplies a nonunit failure in every
composite fibre. The full periodic set is therefore prime-only, but for
each prime p every integer k labels a distinct primitive cycle. Its
actual suspension period is p-1+H_(2p-1)-H_p, rather than log p; repeats
multiply that same time. Infinite multiplicity and the non-logarithmic
clock stop the target dictionary. A nonunit-indicator control gives the
same prime periodic sector without Fermat tests on units, identifying
the precise scope of the arithmetic result. This is a predicate/roof
fork of the monotone defect-cocycle architecture, not a new independent
geometric architecture or a naturalness proof.

## 1. Frozen identity and exact lineage

The [version-1 candidate card](candidate-card.md) was written before
this audit. The complete state space is discrete:

\[
X=\{(n,a,k):n\ge2,\ 1\le a<n,\ k\in\mathbb Z\}.
\tag{1}
\]

Let a^+ be cyclic successor on {1,...,n-1} and a^- its predecessor;
for n=2 both fix 1. Define

\[
\Delta_n(a)=\mathbf1_{\{a^{n-1}\not\equiv1\ ({\rm mod}\ n)\}},
\qquad
\sigma(n,a,k)=(n,a^+,k+\Delta_n(a)),
\tag{2}
\]
\[
\tau(n,a,k)=1+\frac1{n+a}.
\tag{3}
\]

The source lineage is
[prime/composite observables -> symbolic admissibility](../../docs/prior_work/README.md),
followed by a defined autonomous reversible-register replacement. The
symbol is the congruence success/failure at a phase; admissibility for
a closed phase scan will mean all symbols are successes. The mechanism
is stated before that implication is proved. It does not claim a
conjugacy to a previous Logistic or Hénon system, a chronological-sieve
intertwining, or a non-autonomous fitting schedule. The integer n is
conserved: this system tests all integer-labelled fibres, but does not
generate the integer labels dynamically.

The nearest architectural parent is
[228, the gcd-defect cocycle](../228-gcd-defect-cocycle/paper.md).
The common architecture is a complete cyclic phase scan with a
nonnegative defect accumulated in an unrestricted integer register.
Here the arithmetic predicate and roof are different and no symplectic
plane is present. Thus this paper is a fresh candidate fork, not a
claim of independent architectural breadth or a transfer of 228's
geometric proof.

| Same-object field | Exact owner / limitation |
| --- | --- |
| Carrier | All of (1), countable discrete, with no prime or register crop |
| Evolution | The single map (2) |
| Groupoid | G = X crossed with Z under sigma, with source x and range sigma^m x for arrow (x,m) |
| Arithmetic | Modular exponentiation with the uniform exponent n-1 and all nonzero residue representatives |
| Clock / flow | Roof (3), endpoint-glued suspension and ordinary elapsed-time translation |
| Primitive convention | Least sigma cycles, modulo cyclic phase only; distinct k are not identified |
| Repetitions | Repeated traversal of one primitive oriented flow circle |
| Analytic owner | No transfer operator, trace, zeta or determinant supplied |
| Classical/later owner | Positive-dimensional symplectic, Hamiltonian, contact and quantum owners NOT SUPPLIED |

Only integer arithmetic enters (1)--(3). No prime table, prescribed
prime-log length, von Mangoldt weight, Riemann-zero datum or per-prime
parameter appears. This absence is not by itself evidence that the
declared predicate, carrier or clock is canonical. Naturalness and
endogenous generation of the static n label remain OPEN.

## 2. Question and strongest claim

The question is whether this reversible all-residue scan owns a
prime-only full periodic ledger with useful multiplicity and clock.
The exact answer splits into two parts. It does select prime fibres
without an external primality list. It does not produce a singleton
prime packet or a logarithmic prime clock on the same owner.

The strongest claim is the complete classification in Proposition 3
below and its same-object flow translation in Proposition 4. This is
a bounded construction/obstruction result. It is not a natural A0
result, a finite-dimensional symplectic realization, a formal Route
result, an analytic continuation, or a spectral statement.

## 3. Invertibility, groupoid clock and completeness

### Proposition 1 — Full reversible owner and complete suspension

The map sigma is a homeomorphism of X with inverse

\[
\sigma^{-1}(n,a,k)=(n,a^-,k-\Delta_n(a^-)).
\tag{4}
\]

Its transformation groupoid and the roof (3) define one complete flow
on

\[
Y_\tau=\{(x,t):x\in X,\ 0\le t\le\tau(x)\}/
((x,\tau(x))\sim(\sigma x,0)).
\tag{5}
\]

**Proof.** The predecessor in (4) is unique and the register subtraction
undoes the increment at that predecessor. Both compositions of (2)
and (4) give the identity on every full state, including the singleton
phase for n=2. Continuity follows from the discrete topology.

The groupoid G has arrows (x,m), m in Z, with range sigma^m x and
composition given by successive iteration. Its actual elapsed clock
c(x,m) is the sum of tau along m forward steps if m>0, zero if m=0,
and minus the backward sum if m<0. It satisfies

\[
c(x,m+\ell)=c(x,m)+c(\sigma^m x,\ell).
\tag{6}
\]

Equivalently (5) is the quotient of X times R by the integer action
(x,u) mapped to (sigma x,u-tau(x)); ordinary translation of u commutes
with this action and gives the same flow. The roof is continuous and

\[
1<\tau(n,a,k)\le\frac43,\qquad \inf_X\tau=1.
\tag{7}
\]

The upper bound is attained at (n,a)=(2,1), while the infimum is
approached as n+a grows. Thus every crossing consumes at least one
unit of time, and a bounded time interval contains only finitely many
crossings. Equation (4) supplies the unique backward continuation.
This proves completeness in both directions. On each sigma orbit,
the suspension is the usual gluing of intervals into a circle or a
line; different base orbits remain disjoint open components. QED.

The discrete base is not relabelled as the required positive-dimensional
symplectic realization. The groupoid and its suspension are the
broadened owner, with classical A0/A1/A2 NOT APPLICABLE here.

## 4. Exact arithmetic classification

Write L_n=n-1 and

\[
D_n=\sum_{a=1}^{n-1}\Delta_n(a).
\tag{8}
\]

### Proposition 2 — Zero accumulated defect exactly detects primes

For n>=2, D_n=0 if and only if n is prime. Every composite n has
D_n>=1.

**Proof.** Suppose n=p is prime. For any 1<=a<p, multiplication by a
permutes the p-1 nonzero residue classes modulo p: cancellation follows
because p does not divide a. Multiplying all the residues before and
after this permutation gives

\[
a^{p-1}(p-1)!\equiv(p-1)!\pmod p.
\]

The factorial is invertible modulo p, so a^(p-1)=1 modulo p. This is
the elementary proof of the Fermat congruence needed here, and it
applies to every phase. Hence all defects vanish. For p=2, the only
phase is a=1 and the same conclusion is immediate.

If n is composite, choose a proper divisor d with 1<d<n and use phase
a=d. Modulo d, the integer a^(n-1) is zero, while 1 is nonzero.
Consequently a^(n-1) cannot be congruent to 1 modulo n, since that
would imply congruence modulo d. Thus Delta_n(d)=1, and all other
summands in (8) are nonnegative. Therefore D_n>=1. QED.

This proof uses the complete residue scan, including nonunits. It
does not assert that testing only units distinguishes all composites;
the nonunit witness is precisely what proves the composite direction.

### Proposition 3 — Full periodic set and infinite primitive multiplicity

The full periodic set is

\[
\operatorname{Per}(\sigma)
=\{(p,a,k):p\text{ prime},\ 1\le a<p,\ k\in\mathbb Z\}.
\tag{9}
\]

For each pair (p,k) these p-1 phase states form one primitive base
cycle of least period p-1. No composite state is periodic.

**Proof.** Every complete phase scan visits all a exactly once, so

\[
\sigma^{L_n}(n,a,k)=(n,a,k+D_n).
\tag{10}
\]

A return after m>0 steps must return the phase and therefore requires
m=rL_n for an integer r>=1. Its register value is then k+rD_n.
For composite n, Proposition 2 makes this different from k, so no
return is possible. This argument includes every integer-register
value, rather than imposing a bounded k window.

For prime p all individual defects vanish. The register is constant
and the phase advances in one cycle of length p-1. This gives exactly
one cycle at each k with the asserted least period, including period
one for p=2. Different k cannot be cyclic phases of the same orbit,
because k is constant on every prime orbit. All states in X have
already been covered by these two alternatives. QED.

For composite n, (10) also makes clear that backward drift is to
negative k and forward drift to positive k after successive complete
scans. Reversibility therefore introduces no hidden periodic history.

## 5. Actual clock and the decisive target stop

### Proposition 4 — Complete primitive flow ledger and repetitions

The primitive closed flow orbits of (5) are exactly gamma_(p,k),
indexed by primes p and all k in Z. Their least periods are

\[
T_{p,k}=T_p
=\sum_{a=1}^{p-1}\left(1+\frac1{p+a}\right)
=p-1+H_{2p-1}-H_p,
\tag{11}
\]

where H_m=sum_(j=1)^m 1/j. Their r-fold traversals have periods rT_p.
For every prime p,

\[
p-1<T_p<p-1+\log2,
\qquad T_p>\log p.
\tag{12}
\]

**Proof.** A closed suspended trajectory meets the section in a
periodic point of sigma. Conversely the suspension of one primitive
base cycle is one circle whose length is the sum of the same roof
over that cycle. Proposition 3 exhausts the base cycles, so it also
exhausts the flow circles. No shorter return can skip a required phase
or change k. Equation (11) is just the full phase sum of (3), and
repeated traversal adds the same total time r times.

The correction in (11) is positive. Since 1/x is strictly decreasing,

\[
0<\sum_{j=p+1}^{2p-1}\frac1j
<\int_p^{2p-1}\frac{dx}{x}<\log2.
\]

Also log p<p-1 for p>1, proving (12). At the boundary prime p=2 the
formula gives T_2=1+1/3=4/3. QED.

The failure has two independent parts. There are countably infinitely
many intrinsic primitive circles at each prime length. Even if that
multiplicity were ignored, the actual frozen clock grows as p-1 with
a bounded correction; it is not a logarithmic clock and no fixed
global time scale converts all these periods to log p. Equal lengths
among different k do not identify their distinct full-state orbits.

No orbit zeta or trace is built after this stop. The complete periodic
ledger already has infinitely many primitives at T_2=4/3, so an
ordinary positive orbit-counting measure is not locally finite at that
time. This is an immediate ledger obstruction, not a universal claim
against regularized objects. A regularization, weighting or quotient
would require its own explicit owner and cannot be silently credited
to the unmodified counting convention.

## 6. Controls, counterarguments and PROVES_TOO_MUCH

### 6.1 Nonunit/gcd indicator

Replace the defect in a control only by

\[
\eta_n(a)=\mathbf1_{\{\gcd(a,n)>1\}}.
\tag{13}
\]

The same register construction then has zero total defect exactly on
prime fibres. A prime has no nonunits among 1,...,p-1; every composite
has a proper divisor phase. It consequently has exactly the same
prime periodic sector, register multiplicity and periods as (9)--(11)
with the unchanged control roof. No Fermat test on units is needed
for this theorem. This is not a conjugacy of the entire dynamics:
the defects and therefore composite drift can change. For example,
n=9 and a=2 is a unit but 2^8=256=4 modulo 9, so Delta_9(2)=1 while
eta_9(2)=0. The comparator restricts the novelty and naturalness claim
to an alternative prime/composite predicate in the same architecture.

### 6.2 Phase-order shuffle

Any replacement successor that is one cycle through all n-1 phases
visits every defect and every roof term once. Equations (10)--(12)
and the primitive multiplicity remain unchanged, although composite
within-scan paths change. This is not true of an arbitrary permutation
with several cycles: fixing phase a=1 would give a zero-defect fixed
phase even for composite n. The test therefore confirms dependence
on exhaustive admissibility, not independence of the scan structure.

### 6.3 Altered exponent

Replacing n-1 by n gives a negative arithmetic control. On a prime p,
the proven Fermat identity implies a^p=a modulo p. Thus only phase
a=1 passes the altered congruence a^p=1 modulo p. Its accumulated
defect is p-2, which is positive for every prime p>2; their primitive
cycles disappear. The p=2 singleton survives. The exponent matters to
prime closure, but this sensitivity does not prove it determines a
natural clock or remove the register multiplicity.

### 6.4 Forgetting or selecting the register

The projection (n,a,k) mapped to (n,a) forgets all accumulated defects
and intertwines sigma with the cyclic phase successor. That quotient
has a primitive cycle for every integer n, including composites, with
period n-1+H_(2n-1)-H_n under the projected roof. It removes prime
multiplicity only by also destroying the prime-only exclusion. The
k=0 slice is not invariant on composite fibres with a defect; taking
only its already-classified prime cycles deletes other genuine full
orbits. Neither operation repairs this owner.

### 6.5 Zero-defect and clock controls

With Delta set to zero everywhere, every integer and every k gives a
primitive cycle. With unit roof but the original Delta, the original
prime-only periodic sector survives with periods p-1 and the same
infinite k multiplicity. These controls distinguish arithmetic
exclusion from the declared timing perturbation. Neither modified
map nor modified roof is installed in the candidate.

### 6.6 PROVES_TOO_MUCH and static labels

For any nonnegative integer-valued phase predicate h_n(a), the skew
map k mapped to k+h_n(a) has periodic points precisely on those full
phase cycles for which every h value is zero. Thus the register can
encode any property presented as an exhaustive zero-defect scan. The
arithmetic input here is exact, but reversible accumulation does not
by itself derive prime structure from a privileged dynamics. The
static n label, engineered scan and chosen roof retain their
naturalness gap. No source-generation result, Logistic/Hénon lift or
operator geometry follows from the positive prime-selection lemma.

## 7. Gate assessment and portfolio decision

| Gate | Evidence for ANG-20260918-FCR01 | Status / boundary |
| --- | --- | --- |
| T0 | Full countable state, two-sided inverse, transformation groupoid, actual roof cocycle and complete suspension | ESTABLISHED for this broadened owner |
| T1 | Congruence defect is executed inside sigma; all-residue scan separates primes; n is static and roof is declared | SCOPED SOURCE RESULT; SOURCE NATURALNESS OPEN; TARGET CLOCK FAILS |
| T2 | Complete prime-only periodic set, one primitive per (p,k), actual T_p and repetitions rT_p | FULL LEDGER ESTABLISHED; TARGET MULTIPLICITY/CLOCK FAIL |
| T3 | No trace, transfer space, zeta or determinant developed after the stop | NOT ADVANCED |
| Classical A0/A1/A2 | No positive-dimensional symplectic realization in this card | NOT APPLICABLE; no classical credit transferred from 228 |
| Formal Route / B | No formal evaluation invoked | UNASSIGNED / NOT INVOKED |

**Decision: STOP this candidate; FORK the search.** The decisive gate
reason is the full intrinsic ledger: infinitely many register circles
per prime with linear-scale actual periods. The same-object ledger
remains intact because no k quotient, prime-selected slice, new roof
or analytic owner is installed. The source-selection theorem is
retained as a reusable exact control, not accumulated Route credit.

A future candidate must address register multiplicity and the source
of its actual clock before deeper analytic investment. Any change to
the register, predicate, carrier or roof requires a fresh frozen card;
no successor is authorized or claimed by this paper alone.

## Reproducibility, limitations and disclosure

The complete inputs are (1)--(3), without cutoffs or numerical
precision parameters. The proofs above are exact infinite-family
arguments, not finite checks extrapolated to all n. The
[claim ledger](claim-ledger.md) and [evidence record](evidence/README.md)
separate theorem statements, controls and unbuilt obligations. The
bounded model check of the displayed definitions is shared-family
mathematical checking, not human peer review or an independent
certificate. No literature novelty claim or journal-readiness claim
is made.

**Data availability:** all mathematical inputs and proofs are in this
Markdown package; no numerical data set was produced.
**Ethics:** no human subjects, personal data or external experimental
intervention. **Author contributions:** the assistant prepared the
frozen construction, proofs and documentation under the user's
research direction; the user has not been assigned an attested CRediT
role. **Conflicts of interest:** no declaration was supplied; none is
inferred. **Funding:** no information was supplied. **AI use:** this is
an AI-assisted internal research record, including bounded model
checking; it is not a published or peer-reviewed paper.
