# Prime-source rescreen: correcting the omitted GPF diagonal packets

**Paper ID:** `266-prime-source-return-rescreen`  
**Scope ID:** `ASFS-SCOUT-20260919-PSR01`  
**Date / status:** 2026-09-19; `SOURCE CORRECTION COMPLETE; NO NEW OWNER ADMITTED`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

A three-lane source/return rescreen uncovered a consequential domain error
in the existing GPF-Fibonacci control. Its frozen map acts on every positive
integer pair, but the record omitted the prime diagonal fixed points by
applying a nonconstant-cycle theorem without its initial-prime and inequality
conditions. We correct the periodic ledger without changing any carrier,
map or roof. The full map has one fixed point for each prime and one
nonconstant four-cycle. The unchanged unit suspension has infinitely many
unit-time primitives, invalidating its claimed finite ordinary zeta. The
unchanged log-output suspension has one primitive of time log p per prime
PLUS a primitive of time log 210. Its complete ordinary product on Re s>1
is the prime Euler product multiplied by (1−210^(−s))^(−1). This correction
does not establish natural timing, remove the mixed packet, provide a
symplectic lift, or confer Route credit. One reversible source proposal is
deferred at definition level; the geometry lane has no new admission.

## 1. Scope and unchanged owners

The [scope card](candidate-card.md) preceded new audits. During its collision
check, a source-integrity problem took priority over further admissions.
This paper corrects already frozen objects; PSR01 itself is not a flow.

| Existing ID / package | Carrier and action | Frozen clock |
| --- | --- | --- |
| ASFS-SCOUT-20260914-53 / 078 | S=N_{>0}², G(x,y)=(y,gpf(x+y)) | Discrete iterates only |
| ANG-20260914-GPF01 / 079 | Full two-sided G-path space X_G, shift sigma, its suspension | tau=1 |
| ANG-20260914-GPF02 / 081 | The same stated full path space and shift, separately roofed suspension | tau(z)=log gpf(x_0+y_0) |

Here gpf(m) is the greatest prime factor of m≥2. Give S the discrete
topology, X_G its product-subspace topology, and each suspension the quotient
topology. Both roofs are continuous and bounded below by a positive constant.
No diagonal, transient history, or mixed periodic path is removed. Their
exact arithmetic rule is still evaluated at the current pair; no prime list
or new parameter is inserted by this correction.

The prior-work arrow remains prime/composite factor observable -> autonomous
second-order arithmetic recurrence -> its reversible path extension. This is
not a positive-dimensional Hénon/symplectic realization. Classical geometric
fields remain NOT APPLICABLE to these discrete/path owners. A generator,
Fredholm determinant, trace formula and quantum owner are NOT SUPPLIED.

## 2. Source condition and claim boundary

Back and Caragiu's Theorem 3, printed pages 359–360, treats unequal initial
prime values. Its conclusion about the nonconstant four-cycle can be applied
to a periodic prime-pair trajectory; it cannot justify discarding equal
prime pairs from S. The [primary-source audit](evidence/source-audit.md)
records the exact source, retrieval and old-text preservation hashes.

The abstract's broader prose is not a replacement for the theorem's
hypotheses. Nor is replacing the old claim with “all unequal positive
integer seeds” adequate: the displayed map sends (2,6) to (6,2), then
to (2,2), which stays fixed. The audit therefore classifies periodic points
directly and uses the external theorem only in its applicable domain.

The old source is not being revised, and this is not a new literature
novelty claim. Every following result concerns the existing displayed
formulas, not an intended but unfrozen off-diagonal restriction.

## 3. Correct full periodic ledger of G

**Proposition 1.** The primitive periodic G-orbits on S are exactly

1. the singleton (p,p), one for every prime p;
2. the four-cycle C=((7,3),(3,5),(5,2),(2,7)).

**Proof.** After two applications of G both coordinates are prime. Every
point on a periodic orbit is an image of some other orbit point under
G², so both coordinates of every periodic point are prime. For every
prime p, gpf(2p)=p, including p=2. Thus G(p,p)=(p,p).

If a periodic orbit contains an equal pair, it is that fixed orbit: a
deterministic periodic trajectory cannot leave an absorbing fixed point.
Otherwise it has distinct prime coordinates. Apply the cited Theorem 3
to a point on this orbit: its forward trajectory eventually enters C.
An already periodic trajectory entering C must be C itself. The four
displayed states are distinct, and their updates use gpf(10)=5,
gpf(8)=2, gpf(7)=7 and gpf(9)=3. Its least period is therefore 4. QED.

This is a complete PERIODIC classification, not a classification of every
two-sided history. It does not assert that the entire natural extension
consists of periodic paths or discard histories with a nonperiodic past.
For the same reason no finite state search is used to infer completeness.

The original noninjectivity example G(1,1)=G(3,1)=(1,2) is unaffected.
The source mechanism is present; the earlier uniqueness statement was false.

## 4. Full path owner and unit-roof correction

Let X_G={z in S^Z : z_(j+1)=G(z_j) for every integer j}. This is a
closed subspace of the product of discrete copies of S. The left shift
sigma and right shift are inverse continuous maps on X_G.

For m≥1, evaluation z -> z_0 gives a bijection

    Fix(sigma^m)  <->  Fix(G^m).

Indeed a periodic path gives a periodic zeroth state. Conversely a periodic
G-state supplies exactly one m-periodic two-sided path by repetition of
its G-cycle; extra nonperiodic backward choices cannot produce an m-periodic
path with that zeroth state. Thus the periodic paths are exactly one
constant path z^(p) per prime, and four phase paths of C.

For any positive continuous roof bounded below, the suspension has a
complete two-sided translation flow: infinitely many section crossings
take infinite absolute time. A return meets the same section after an
integer number of shifts, and its time is the corresponding sum of roof
values. A primitive shift cycle therefore gives exactly one oriented
primitive circle with the least cycle sum as its period. No phase is
silently divided out except actual time translation along this circle.

For 079's ORIGINAL unit roof the complete primitive times are

    T_p=1 for every prime p;  T_C=4.

Repeats have times r and 4r respectively. Every Fix(sigma^m) is countably
infinite, so the earlier finite Artin–Mazur coefficient formula is invalid.
The ordinary unweighted full repetition series is not absolutely convergent
at any finite s: its r=1 terms already contain infinitely many identical
nonzero absolute values |exp(−s)|. Thus it has no ordinary absolute-
convergence half-plane. The old (1−exp(−4s))^(−1) is the C factor alone,
not the full owner's zeta. No regularization is proposed.

## 5. Existing log-output roof: prime circles AND the mixed circle

For 081's ORIGINAL roof tau(z)=log gpf(x_0+y_0), tau≥log2. On z^(p)
the roof is log p, so its least physical period is log p. On C the
four roof values are log5, log2, log7, log3, giving log210. Therefore

    T_p=log p for every prime p;  T_C=log210;
    repeat times: r log p and r log210.

Each prime gives exactly one primitive circle. C is one additional
primitive circle, not four packets and not a repetition of a prime circle.
For example, 210 has several different prime factors and cannot equal p^r.

**Proposition 2.** The full ordinary primitive product of the unchanged
081 flow is, in the absolute-convergence region Re s>1,

    Z_081(s) = [product_p (1−p^(−s))^(−1)] (1−210^(−s))^(−1)
             = zeta(s)/(1−210^(−s)).

**Proof.** Insert the complete ledger just proved into the unweighted
primitive/repetition convention. For sigma=Re s>1,

    sum_p sum_{r≥1} p^(−r sigma)/r
      ≤ [1/(1−2^(−sigma))] sum_{n≥2} n^(−sigma) < infinity.

The extra 210 repetition series also converges absolutely there. Unique
factorization expands each finite prime product into the integers supported
on those primes. Absolute convergence permits exhaustion by finite prime
sets, giving sum_{n≥1} n^(−s)=zeta(s) in that region. This is a product
calculation for the fixed flow, not a spectral or divisor identification. QED.

No claim is made here about continuation outside this half-plane, a
Fredholm realization, or a prime-power trace. The surplus C factor is
nontrivial even at real s>1. Deleting C, dividing out its factor as if it
were absent, restricting to the prime diagonals or changing the roof
would change the question/owner and is not part of this correction.

## 6. Clock and lineage controls

The correction reverses a specific false negative: 081 DOES have actual
per-prime log-time circles. It does NOT establish that this clock is
endogenous in the stronger research sense. The frozen roof explicitly
applies log to the prime-valued output; on a constant diagonal it is
exactly a prime-label-to-log readout. That is the [082 control](../082-gpf-fixed-point-euler-control/paper.md)
problem, not a reason to promote 081 after noticing its Euler factors.
The previous distinction “081 only aggregates one packet, so it avoids
the fixed-label issue” must be withdrawn.

The arithmetic recurrence and its complete returning packets remain useful
source controls. Their existence and a chosen arithmetic roof are distinct
from a source-derived physical-time mechanism. The unit-roof comparison
demonstrates the dependence on the chosen roof without changing either
candidate. No quotient or relabelling turns the mixed C packet into a prime.

Applicable controls: prime diagonals (including p=2), the mixed four-cycle,
the unequal composite seed (2,6), unchanged noninjectivity, every marked
cyclic phase, roof ownership and ordinary-product convergence. Shuffled
labels, numerical cutoffs and precision checks are not used: the results
are exact formulas with a source-backed nonconstant-cycle classification.
An arbitrary recognizer followed by a prescribed label roof remains a
PROVES_TOO_MUCH warning. No new geometric or operator claim is evaluated.

## 7. Three-lane screening outcome and dependency scope

The reversible-source scout supplied a provisional all-integer law:
g(0)=0, g(1)=1, g(m)=gpf(m) for m≥2; H(y)=g(|y|);
F(x,y)=(y,2H(y)−x), with proposed inverse
(u,v)->(2H(u)−v,u). It retains all integer pairs. This is DEFERRED,
NOT ADMITTED: no orbit theorem, clock result or symplectic claim for it
is made here. Its signed variant is a different unfrozen proposal.
The Hénon memory shell overlaps 133, and the GPF source has the corrected
078 comparison; neither result transfers to this proposed action.

The source-feedback scout uncovered the present error during collision
checking and stopped its new design work to audit the direct dependencies.
The geometry scout supplied no sufficiently new joint source/action/clock
mechanism beyond the examined witness-kick and cover-lift controls. That
is NO ADMISSION, not a proof that conservative geometry is impossible.
The [scout record](evidence/scout-record.md) distinguishes these outcomes.

The correction is propagated by explicit notices to 078, 079 and 081
papers/cards/ledgers/summaries/evidence. Narrow dependency notices clarify:
080's noninjectivity obstruction survives; 082's own readout control
survives but its comparison was false; 240 must no longer describe
078/081 as a single-small-packet source. The other affine-GPF owners
087/094 are different formulas and are not re-scored here.

This is not an exhaustive audit of every historical mention. Older
uncorrected summaries must not override the exact formulas and this
corrigendum. All original text remains recoverable beneath dated notices.

## 8. Gate assessment and portfolio decision

| Owner | Corrected evidence | Boundary / decision |
| --- | --- | --- |
| 078 | Internal arithmetic update; complete diagonal-prime plus C ledger | Retain source control; stop unique-cycle assertion; geometry absent |
| 079 | Full invertible path action; complete unit-time ledger | Stop finite ordinary-zeta claim; infinite unit primitives |
| 081 | Full log-time ledger and ordinary product on Re s>1 | Retain exact calculation; stop missing-prime claim AND pure-Euler/natural-clock promotion |
| PSR01 | Bounded source correction and proposal dispositions | No dynamical coordinates; fork search from corrected comparator |

Broadened T0 ownership remains valid for 079/081; T2 is corrected as above.
The old unconditional T1 clock-naturalness language is not retained.
079's ordinary T3 claim is withdrawn; 081's ordinary product calculation
is replaced on the smaller established half-plane, without an operator.
Classical A0/A1/A2 are NOT APPLICABLE to these path owners. Formal Route
coordinates remain UNASSIGNED; Route B remains NOT INVOKED.

**Portfolio: advance the corrected arithmetic/packet control; stop the
invalid uniqueness and finite-unit-zeta claims; fork subsequent search.**
The decisive new information is that the prime family was already present
in the full old owner, together with an unavoidable extra primitive packet.
A next admitted mechanism must address physical clock ownership and the
full mixed-packet ledger without erasing states, and must supply its own
positive-dimensional geometry if it claims the classical lineage arrow.
The deferred reversible proposal is eligible only for a separately frozen
first-gate audit, not automatic development or assumed geometric success.

## Reproducibility and limitations

This work used direct symbolic reasoning, one verified primary paper,
bounded local collision checks and separately executed model review.
There was no numerical census, fitting, GPU job, new target data, PDF/LaTeX
generation, external circulation or formal Route invocation. 241/242
remain paused. The external classification theorem is explicitly attributed;
new deductions and invalid old claims are separated in the [claim ledger](claim-ledger.md).
AI assistance was used for scouting, derivation, writing and review; this is
not external peer review or a claim of independent human verification.

[Candidate/scope record](candidate-card.md) · [Evidence index](evidence/README.md) ·
[Package summary](README.md).
