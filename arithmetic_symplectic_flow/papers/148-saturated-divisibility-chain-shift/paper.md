# Saturated divisibility chains retain mixed primitive words

**Paper ID:** 148-saturated-divisibility-chain-shift  
**Candidate ID:** ANG-20260915-SDC01  
**Date:** 2026-09-15  
**Status:** STOP — EXACT MULTIPLICATIVE REPETITIONS; MIXED PRIMITIVES AND INFINITE UNIT PACKETS.  
**Evidence:** exact elementary proofs; no numerical extrapolation.  
**Route:** broadened T0--T3 owner audit; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

We replace sieve exclusion by multiplicative indecomposability in the
divisibility order on positive rationals, then study all two-sided
saturated chains modulo common rational scaling. The explicitly normalized
shift is a homeomorphism conjugate to the full shift on its intrinsically
derived prime cover ratios. Every primitive periodic word is retained.
Prime-power multiplicative observations occur on repetitions of constant
prime packets, but mixed words also give primitive composite-product
packets. There are infinitely many primitive unit packets, so the full
unweighted unit-roof zeta has no half-plane of absolute logarithmic
convergence. The carrier is not locally compact. These are scoped
obstructions for this frozen object, not a no-go theorem for other
arithmetic carriers or clocks.

## 1. Identity and same-object ledger

The [version-1 card](candidate-card.md) was frozen before these claims.
All positive rationals and all allowed chains are retained. Put

\[
x\preceq_D y\quad\Longleftrightarrow\quad y/x\in\mathbb N_{\ge1}.
\]

A strict cover \(x\prec_{\mathrm{cov}}y\) means \(x\ne y\), \(x\preceq_D y\),
and there is no \(z\) with \(x\prec_D z\prec_D y\). The full carrier and
action are

\[
X=\{y\in(\mathbb Q_{>0})^{\mathbb Z}:y_0=1,\
y_t\prec_{\mathrm{cov}}y_{t+1}\ \hbox{for every }t\},
\qquad
F(y)_t=\frac{y_{t+1}}{y_1}.
\tag{1}
\]

Positive rationals have the discrete topology, and X has the indicated
product-subspace topology. The frozen observable is \(C_m(y)=y_m\) for
positive integers m. It is not a time or a roof.

| Item | Frozen owner | Result or boundary |
| --- | --- | --- |
| Arithmetic source | All rational divisibility covers | Ratios derived as prime multiplicative atoms |
| Carrier and action | Full X and F in (1) | Homeomorphism; nowhere locally compact |
| Symbolic coding | Consecutive ratios of the same chain | Exact conjugacy proved below |
| Clock and flow | Unit roof and its suspension under F | Complete; one shift takes one time unit |
| Packets | All least-period F-orbits modulo cyclic phase | All primitive finite ratio words retained |
| Multiplicative observation | C_m from the same chain | Cocycle and repetition law, distinct from elapsed time |
| Zeta convention | Ordinary unweighted product over all primitive packets | Absolute logarithmic convergence fails in every right half-plane |
| Operator, domain and trace | Not supplied | No determinant or locally compact convolution construction |
| Classical geometry | No finite-dimensional symplectic base | NOT APPLICABLE |
| Later Hamiltonian/contact/quantum owner | Not constructed | DEFERRED; Route B NOT INVOKED |

The ANG label records the authorized nonclassical chain/action track. The
action can be recorded by its transformation groupoid, but no locally
compact groupoid hypothesis, measure normalization or operator algebra is
inferred from that bookkeeping.

## 2. Question and lineage

The specific prior-work arrow is

~~~text
divisor-exclusion prime/composite constraint
    -> multiplicative indecomposability
    -> saturated-chain admissibility
    -> cyclic words and multiplicative repetition.
~~~

This replaces the original chronological sieve by an explicitly stated
arithmetic-symbolic relation. It is not a conjugacy to the earlier sieve
trajectory and does not claim the later Hénon/symplectic arrow. Unlike a
selected prime alphabet, the initial inputs in (1) are all positive
rationals, integer divisibility and the cover relation.

The arithmetic admission is therefore owned by the frozen carrier
definition. F shifts already admissible chains; it does not execute an
evolving trial-division algorithm or generate an initially absent sieve
table. The positive source result is scoped to this intrinsic
order/admissibility mechanism.

The question is whether prime multiplicative atoms become the full
primitive packet ledger, with prime powers as repetitions. The answer
splits: prime atoms and their power observations are genuinely recovered,
but they do not exhaust primitive packets.

[136](../136-factorization-nonbacktracking-flow/paper.md) instead moves
among ordered factorizations of one fixed total product using split/merge
edges. Its prime components are isolated. Here irreducibility defines an
allowed cover step in a growing chain, whose overall scale is quotiented
from the outset. Neither its missing-prime result nor its product-8
packets are transferred to (1).

## 3. Definitions, permitted data and normalization

The normalization y_0=1 specifies the quotient without an implicit
topological choice. Every unnormalized cover chain x has the unique
representative y_t=x_t/x_0 under common rational scaling. Shifting the
chain and normalizing again gives exactly (1).

Only integer multiplication and divisibility determine admissibility.
There is no supplied prime table, zero data, per-prime parameter, fitted
length, logarithmic roof or von Mangoldt weight. No finite alphabet is
silently substituted for the complete carrier. The prime set appearing
in the proof below is an output of the cover test.

## 4. Exact proofs

### Proposition 1 — Source-derived alphabet and global conjugacy

The cover \(x\prec_{\mathrm{cov}}y\) holds exactly when y/x is prime.
Consequently the ratio map

\[
R:X\longrightarrow\mathcal P^{\mathbb Z},\qquad
R(y)_t=y_{t+1}/y_t
\tag{2}
\]

is a homeomorphism, where \(\mathcal P\) is the set of primes with discrete
topology. It conjugates F to the left shift \(\sigma\).

**Proof.** A strict divisibility ratio is an integer n>=2. If n=ab with
a,b>=2, the rational z=ax is strictly between x and y. Conversely any
strict intermediate z supplies a factorization
n=(z/x)(y/z) with both factors integers at least 2. Absence of such z is
therefore exactly primality, without selecting any alphabet in advance.

For every ratio sequence a in \(\mathcal P^{\mathbb Z}\), the unique
normalized chain with those ratios is

\[
y_0=1,\qquad
y_t=\prod_{j=0}^{t-1}a_j\ (t>0),\qquad
y_t=\left(\prod_{j=t}^{-1}a_j\right)^{-1}\ (t<0).
\tag{3}
\]

All coordinates are positive rationals; the prime-ratio criterion proves
the cover condition. Equations (2)--(3) are inverse maps. Each output
coordinate uses finitely many discrete input coordinates, proving their
continuity for the product topologies. Direct cancellation gives
R(Fy)_t=R(y)_{t+1}. Thus F is a homeomorphism, with explicit inverse

\[
F^{-1}(y)_t=\frac{y_{t-1}}{y_{-1}}.
\tag{4}
\]

No selected subset of X is used. QED.

### Proposition 2 — Topological boundary

X is Hausdorff, second countable and zero dimensional, but has no compact
neighborhood at any point.

**Proof.** The full countable discrete-alphabet product in Proposition 1
is Hausdorff and has a countable basis of finite-coordinate cylinders.
These cylinders are clopen, giving the first assertions.

There are infinitely many primes: from any finite list their product plus
one has a prime divisor outside the list. Suppose a compact set K were
a neighborhood of some sequence. It would contain a nonempty basic
cylinder U fixing only finitely many coordinates. Choose a coordinate j
outside that finite set. Its projection satisfies
\(\pi_j(K)\supseteq\pi_j(U)=\mathcal P\).
But the continuous image of K must be compact, and a compact subset of a
discrete space is finite. This contradicts the infinitude of
\(\mathcal P\). Proposition 1 transfers the result to X. QED.

Closedness of a constraint set in a product would not, by itself, give
local compactness. The obstruction above is explicit and does not rely
on such an inference.

### Proposition 3 — Full packet ledger and two distinct repetition laws

The complete primitive F-orbit ledger is the set of all finite prime
words which are not proper word powers, modulo cyclic rotation.
For a least-period word \(w=(a_0,\ldots,a_{m-1})\), define
\(N_w=\prod_{j=0}^{m-1}a_j\).
The unit-roof suspension has one primitive oriented packet for each such
word class, with time m. For every positive integer r, its r-fold
repetition has time rm and multiplicative observation \(N_w^r\).

**Proof.** Under Proposition 1, F-periodicity is exactly shift
periodicity. Every period-m sequence is obtained by repeating its length-m
word. Its least period is m precisely when that word is not a proper
power; changing the sequence's phase cyclically rotates the word. This
classifies all periodic states and their multiplicities.

Induction in (1) gives
\[
F^m(y)_t=\frac{y_{t+m}}{y_m},\qquad
C_{m+n}(y)=C_m(y)\,C_n(F^m y).
\tag{5}
\]
When F^m y=y, the cocycle identity gives
\[
C_{rm}(y)=C_m(y)^r=N_w^r.
\tag{6}
\]
The product N_w is cyclic-phase invariant because integer multiplication
is commutative.

The frozen suspension is
\[
S=(X\times[0,1])/((y,1)\sim(Fy,0)).
\tag{7}
\]
The map and its inverse exist globally, and each roof crossing consumes
one unit of time, so translation defines the flow for all real times.
Returning to the same height requires an integer elapsed time; returning
to the same state requires the corresponding iterate of F to fix y.
Thus its primitive time is m, and r traversals have time rm. This proves
the time law separately from (6). QED.

No reverse-time packet is added by convention. A reversed ratio word is
another allowed word, but is another packet only if it is not already a
cyclic rotation of the original word.

### Proposition 4 — Prime powers do not exhaust the full ledger

For each prime p, the chain y_t=p^t is a fixed point of F and gives one
primitive unit packet. Its return after r steps has observation p^r.
Conversely, if F^m y=y and C_m(y)=p^r for a positive integer m, its ratio
sequence is constant p, m=r, and its least period is 1. The hypothesis
that m is a return time is essential.

Nevertheless there are primitive mixed packets. The repeating word
(2,3) has least period 2 and multiplicative observation 6.

**Proof.** Formula (3) gives y_t=p^t for the constant ratio sequence.
It is fixed by F, and its displayed observation is immediate. Conversely
C_m is a product of the m prime ratios in a return word. Unique
factorization forces every factor to equal p and their number to be r.
Since the chain is periodic with that word, its entire ratio sequence is
constant p. Its least period is therefore 1.

The two ratios in (2,3) are distinct, so this word is not a square of a
length-1 word and has least period 2. Its product is 6. The phase (3,2)
is the same packet, not an additional one. More generally every primitive
word of length greater than 1 contains at least two distinct prime ratios
and hence has a product that is not a prime power. QED.

The prime-power observation at return times is therefore exact and endogenous, but
discarding all mixed packets to obtain a prime-only primitive ledger
would change the frozen carrier. Multiplicative observation is not
the clock: a prime packet has time 1, not log p.

### Proposition 5 — Full ordinary zeta fails its first convergence test

The proposed full ordinary product has no right half-plane of absolute
logarithmic convergence. Its positive finite subproducts diverge for
every positive real s.

**Proof.** The convention would require
\[
\log Z(s)=
\sum_{[w]\ \mathrm{primitive}}\ \sum_{r\ge1}
\frac{e^{-sr|w|}}r.
\tag{8}
\]
Already the r=1 contributions of the distinct constant prime packets
are
\[
\sum_{p\in\mathcal P}e^{-s}.
\tag{9}
\]
For any s with positive real part the absolute value of each summand is
the same strictly positive number. Infinitely many primes make (9)
diverge absolutely. For real s>0, keeping L distinct constant packets
alone gives the subproduct \((1-e^{-s})^{-L}\), which tends to infinity.
All other factors in a positive finite subproduct are at least 1.
Thus no omission-free ordinary product is supplied by (8). QED.

This does not rule out every independently defined regularization or
operator. None is defined or assigned credit here.

## 5. Controls and adverse findings

| Control | Exact result | Interpretation |
| --- | --- | --- |
| Composite proposed step | Ratio 4 has intermediate 2x | Source covers reject reducible arithmetic increments |
| Genuine atom | Every constant prime ratio gives a unit packet | The source does retain all prime atoms |
| Mixed admissible word | (2,3) gives one primitive length-2 packet, product 6 | Prime atoms do not imply a prime-only primitive ledger |
| Repeated mixed word | (2,3,2,3) is a second traversal, not a new primitive packet | Word, orbit and repetition multiplicities remain separate |
| Finite-alphabet comparator | Restricting the ratios deletes states of X | Finite cutoff convergence cannot repair the full object |
| Constant-word restriction | Deletes mixed packets although they are intrinsic | An immediate new-owner/fork event |
| Generic alphabet relabelling | Any bijection of the countable ratio alphabet conjugates the unweighted shift | Arithmetic labels alone do not select a logarithmic clock or distinguish its unweighted dynamics |
| Full topology | Every finite cylinder leaves an infinite free coordinate | No locally compact carrier is inferred from finite approximations |

The generic-alphabet observation is a PROVES_TOO_MUCH limit on arithmetic
specialness, not a denial of Proposition 1's exact source derivation.
No cutoff, floating-point precision, Riemann-zero comparison or parameter
fit enters the proofs.

## 6. Gate assessment and decision

| Audit | Result for this same candidate | Boundary |
| --- | --- | --- |
| T0 | Full X, homeomorphism, normalized quotient and complete unit suspension ESTABLISHED | Carrier is nowhere locally compact; no classical symplectic realization |
| T1 | Endogenous prime cover ratios and multiplicative cocycle ESTABLISHED | Clock is unit time, not prime-log time; arithmetic does not make the unweighted shift prime-specific |
| T2 | Complete word/packet classification and both repetition laws ESTABLISHED | Prime-only primitive target FAILS because mixed primitive packets remain |
| T3 | Full ordinary logarithmic zeta convergence scoped FAIL | Infinite unit packets; no operator, trace or regularization supplied |
| Classical A0/A1/A2 | NOT APPLICABLE | No classical candidate is claimed |
| Formal Route coordinates | UNASSIGNED | No target/divisor evaluation |
| Route B | NOT INVOKED | No formal readiness or separate evaluation |

**Decision: stop; portfolio fork.** The exact multiplicative prime-power
observation is retained as a positive control, but it does not allow
selection of only those packets. The full ledger has mixed primitives and
infinitely many shortest packets. Both failures follow without extended
local investigation. A restricted carrier, changed clock or regularized
analytic convention would need a new frozen identity.

## Evidence and reproducibility

The [evidence index](evidence/README.md) records the method and verification.
The [independent model review](evidence/review.md) found no mathematical
blocker and required explicit return-time wording in the short claim ledger;
that clarification is incorporated.
The [card](candidate-card.md), [claim ledger](claim-ledger.md) and
[summary](README.md) preserve the same ID and stop status. Every global
mathematical claim is proved above; no external theorem beyond elementary
integer factorization, nor any finite computation, is used as a substitute
for proof.
