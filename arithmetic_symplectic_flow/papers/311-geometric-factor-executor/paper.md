# Geometric factor execution: owned clock, impossible finite nonzero multiplicity

Paper ID: `311-geometric-factor-executor`.
Candidate ID: `ANG-20260920-GFE01`. Date: 2026-09-20.
Status: `OWNED EXECUTION CLOCK; FINITE NONZERO MULTIPLICITY IMPOSSIBLE — STOP / FORK`.
Evidence class: exact owner and conditional full-packet multiplicity theorem;
complete fixed/two-step exclusion. Classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A real geometric probe executes divisor splits and failed-probe merges
of finite positive-integer words. The updated first letter controls
the next quadratic plane map. All words, units, real
planes, cuts and terminal states remain. We derive every
inverse branch, the exact image and the actual plane IMAGE
clock of the partial Borel owner. Every hypothetical positive
periodic core admits infinitely many suffix copies with the SAME
least period and clock. Even unit suffixes, which preserve
the integer product, give distinct full-tail packets: their minimum
cyclic word lengths differ. Eventual isotropy reduces to periodic
cores, so positive primitive multiplicity is zero or infinite,
never finite nonzero. Separately, all fixed and two-step returns
are excluded using complete real-plane branch inequalities. Positive
higher-period existence remains OPEN. Three controls own their changed
domains and clocks. The full finite-multiplicity target stops without
a higher-period census or a suffix quotient repair.

## 1. Identity, lineage and question

The original [card](candidate-card.md) freezes the entire object, sourced
from the final finite-word definition in the [310 frontier](../310-binomial-bernstein-divisor-flow/evidence/scout-record.md).
All initial locks and review boundaries are recorded in [evidence](evidence/README.md).

| Item | Same-object construction | Boundary |
| --- | --- | --- |
| Carrier | ALL finite positive-integer words x R^2 | Units, empty word, repeats and order retained |
| Measure | Counting words x plane Lebesgue | Same density at every root |
| Arithmetic/execution | q=1+floor(abs(x)); divisor split, failed-probe merge | Real geometry chooses the actual next word |
| Geometry | Phi_a(x,y)=(y,y^2-a*x), a=current first letter | Designed quadratic generator, not a proved conservative lift |
| Clock/time | Actual inverse IMAGE and retained-lag real extension | No roof, runtime or inserted log-prime data |
| Packets | Full source isotropy time image and actual tail equivalence | No word-product or suffix quotient |
| Classical geometry | Symplectic base, positive roof, mapping torus | NOT APPLICABLE |
| Analytic owner | No trace, zeta, determinant or operator | T3 NOT SUPPLIED / NOT PURSUED |
| Controls | GEOMETRY-OFF, UNIT-JACOBIAN, SPLIT-ONLY | Each has its own source, inverse and clock |

The [prior-work lineage](../../docs/prior_work/README.md) realized here is divisor
admissibility d|n -> n=d*(n/d) -> actual finite-word
execution -> quadratic geometric feedback. On singleton (n),
every proper-divisor symbol is an actual branch when 1<q<n
and q|n; units and all composite words remain. The
absence of a proper divisor never grants closing permission.

This is an autonomous geometric replacement for passive symbolic
transport, not a conjugacy theorem with a prior Logistic or
Henon system. The probe, branch priority, failed-probe merge,
generator, coefficient placement, measure and null-cut version remain
declared designs. Stronger arithmetic naturalness is OPEN. No prime
predicate, table, zero data, per-prime parameter or fit is used.

Question: can this full executor own a clock and a
finite nonzero positive primitive packet multiplicity? The strongest result
below is a structural negative answer to the multiplicity part,
not an assertion that positive higher-period returns do not exist.

## 2. Exact executor, every inverse and full image

### 2.1 Full partial action

Let W contain all finite positive-integer words, including empty,
and Y=coproduct_(w in W) {w} x R^2 with its
standard Borel structure and mu=counting x Lebesgue. For
w=(a,eta), put q=1+floor(abs(x)). If q|a,
replace w by (q,a/q,eta). If q does not divide
a and w=(a,b,eta), replace it by (a*b,eta).
A failed singleton and the whole empty-word plane are terminal.
Every defined step simultaneously applies Phi_a(x,y)=(y,y^2-a*x).

The digit cells are E_1=(-1,1), and E_q={x:
q-1<=abs(x)<q} for q>=2. At x=+/-m use
q=m+1. All cuts and both signs remain. Inserting
or merging units uses the same rule; a=q=1 is
one split, not duplicate branches. A terminal retains T^0
and incoming arrows, never an invented identity successor.

### 2.2 Complete branch enumeration

Write a target plane point as (u,v) and t=u^2-v.
The entire-plane inverse of Phi_a is (t/a,u).
At target word (r,s,eta), the split inverse is

    ((r*s,eta), t/(r*s), u), domain q(t/(r*s))=r.

At target word (c,eta), every ordered factorization a*b=c
gives a merge inverse

    ((a,b,eta), t/a, u), domain q(t/a) does not divide a.

There are no inverses at the empty word. Substitution proves
each formula, including its actual branch permission. Conversely every
forward split/merge has exactly that word relation and inverse
plane point; hence the enumeration is exhaustive. Distinct predecessors
and overlapping targets remain, with no selection of a factorization.
Each fibre has finitely many predecessors: at most one split
and the finite number of ordered factorizations of its first letter.

The full image also has a simple exact description. For
every nonempty target, the union of all MERGE images is

    abs(u^2-v)>=1.

Indeed the factorization a=1, b=c supplies every such point.
If abs(t)<1, then abs(t/a)<1 for every a>=1,
so q=1 divides a and no merge inverse exists.

For a target (r,s,eta), its split image requires
rs*(r-1)<=abs(t)<r^2*s when r>=2; these points
already lie in the merge image. When r=1, its
split image is abs(t)<s. Since s>=1, this fills
the entire missing region. Consequently the full rootwise image is:

| Target word | Exact plane image |
| --- | --- |
| Empty | Empty |
| Length at least two, first letter 1 | Entire R^2 |
| Every other nonempty word | abs(u^2-v)>=1 |

This description includes equality on the parabolic boundaries and is
not a finite cutoff argument. The source is partial Borel
and finite-to-one, not onto: ((2),0,0) has no predecessor.
It is not ordinary continuous on its domain: at singleton
(2), x approaches 1 from below through the split word
(1,2), whereas at x=1 the permitted split word is
(2,1). No etale/local-homeomorphism structure is asserted.

## 3. Own IMAGE, all-point clock and complete time

The plane derivatives are

    D Phi_a = [[0,1],[-a,2*y]], det=a,
    D Phi_a^(-1) = [[2*u/a,-1/a],[1,0]], det=1/a.

Thus a split inverse has J=1/(r*s); a merge
inverse from head a has J=1/a. Each inverse is
a restriction of a global polynomial diffeomorphism. Change of
variables proves mu(theta(E))=integral_E J dmu for EVERY
Borel subset of its actual target, not merely a whole-
branch ratio. The same positive finite formula is prescribed on
cut curves, including null points; a.e. uniqueness alone would
not select these values. No atomic measure was added.

On every defined forward step, rho(z)=a and kappa=log(a).
These values are derived from the frozen Lebesgue IMAGE, not
inserted as a word roof. The coefficient also shows why
the plane maps are not generally area preserving: Phi_a pulls
back dx wedge dy to a*(dx wedge dy). At a=1
the plane generator is area preserving, but this does not
turn the whole discontinuous word executor into a classical symplectomorphism.

Use only actual retained-lag triples G={(z,m-k,w):T^m z=T^k w},
source w and range z, with all iterates defined. Finite
iterate equalities are Borel and finite-iterate predecessor fibres are
countable, giving a countable Borel groupoid. Composition aligns the
already existing longer middle history; it does not continue a terminal.

For A_m(z)=product_(i<m) a(T^i z), A_0=1, actual
branch-pair IMAGE and clock are

    J(z,m-k,w)=A_k(w)/A_m(z),
    c(z,m-k,w)=log A_m(z)-log A_k(w).

On each legal history cell, the inverse polynomial chain rule
gives this IMAGE. Common legal future factors cancel between
presentations of a triple, also on cuts. The same alignment
proves composition and the all-Borel law. This does not assert
global invariance of mu under a many-to-one partial action.

The extension keeps ALL Y x R with arrows (w,h)->(z,h+c).
Translation h->h+t for every real t is jointly Borel,
complete and commutes with arrows. Only set-level quotient time
is claimed. Source isotropy, H_z=c(G_z^z), and extension
kernel remain separate. No coarse quotient topology or embedded
circle/suspension assertion is required for the packet statements below.

## 4. All-return structure and the suffix multiplicity obstruction

### 4.1 Word invariants and eventual cores

Every defined step preserves the positive integer word product D,
and changes word length by exactly +1 or -1. There
are no fixed states, and every periodic source orbit has
even least period. Empty-word states are terminal, not exceptions.

For any deterministic partial action here, nonzero source isotropy
means T^m z=T^k z for some m>k with legal
histories. The state T^k z then lies on an actual
periodic core, with all subsequent iterates defined. Conversely a
state reaching a periodic core of least period r has
source isotropy the literal subgroup r Z. For that core put

    Q=product_(i=0)^(r-1) a(T^i z_core), a positive integer.

Conjugating by its finite incoming tail cancels the transient factors.
Thus its entire eventual basin has H=log(Q) Z. If
Q>1, log Q is the least positive time and the
extension kernel is zero; if Q=1, H=0 and the
extension kernel is r Z. A state with no eventual
core has source/H/extension isotropy zero. In particular there
is no hidden nondiscrete positive time group supplied by transient histories.

These facts classify the FORM of all possible time groups,
not which higher-period cores exist. They do not prove prime
selection, finite multiplicity or absence of composite clocks.

### 4.2 Exact suffix replication of every periodic core

For a fixed suffix eta define R_eta(w,x,y)=(w*eta,x,y),
where * means concatenation. Whenever Tz is defined,

    T(R_eta z)=R_eta(Tz), with the same first-letter factor rho.

A split inspects only the head and geometry; a legal
merge already has its required two letters, and appending a
suffix changes neither rule. This identity is deliberately only
for previously DEFINED steps. An originally failed singleton can
gain a merge after extension, so R_eta is not claimed
to preserve every terminal or to conjugate the entire partial system.

Let z lie on ANY periodic core of least period r.
Every step on that core is legal, so its suffix copy
has the same periodic geometry, first-letter sequence and clock Q.
If the copy had a shorter period s, injectivity of
word concatenation on the right would imply T^s z=z.
Thus least source period r, full time image log(Q) Z
and its least positive generator (when Q>1) all survive.

Now use the suffix of k units, eta=1^k, k>=0.
These copies have the SAME conserved word product D as
the original. If ell is the minimum word length over
its periodic orbit, the kth copy has minimum ell+k.
Two periodic cores are full-source tail equivalent exactly when
their periodic orbits meet. Meeting would make them the same
cyclic orbit, with the same minimum length. The copies for
different k therefore cannot merge under ANY actual tail arrow.
Finite inverse excursions compose to actual tail arrows and do
not alter this conclusion. Physical time shifts only height and
cannot cross distinct source-tail classes.

Hence each existing positive primitive packet produces at least
countably infinitely many distinct packets at its SAME least time,
even inside a single conserved-product sector. All real heights
and finite predecessors attach to their own packet; they do
not identify the different suffix copies or shorten their primitive.

### 4.3 Global multiplicity verdict, with existence left open

For EVERY L>0, positive primitive multiplicity in the full
owner is either zero or infinite. If a packet exists,
Section 4.1 gives a periodic core and Section 4.2 gives
infinitely many same-L copies; if none exists, multiplicity is zero.
No finite positive count, in particular one packet per prime,
is possible. This conditional exhaustive dichotomy does not require
exhibiting a positive core and does NOT assert that one exists.

The finite-nonzero multiplicity target therefore decides STOP / FORK.
Quotienting words by unused suffixes, erasing units, fixing a
word length or selecting a centre would change the frozen
carrier and owner. There is no such repair in this paper.
Positive higher-period existence remains OPEN / NOT PURSUED.

## 5. Complete one- and two-step checks

No one-step fixed state exists because word length changes.
Any two-step return must use one split and one merge;
rotate its phase to begin with a split at (a,eta).
Let d=q(x)|a. The intermediate word is (d,a/d,eta),
and the next step must be the failed-probe merge, requiring
q(y) not to divide d. The real two-step equations are

    Phi_d(Phi_a(x,y))=(x,y),
    y^2=(a+1)*x, x^2=(d+1)*y.

They force x,y>=0. At the zero solution, q(0)=1
forces d=1; the second probe is again 1 and
divides d, so the required merge fails. At every nonzero
solution, eliminating y gives

    x^3=(a+1)*(d+1)^2.

Since d|a implies a>=d, one has x>=d+1.
But the first actual digit q(x)=d requires x<d,
including the d=1 case. This is impossible. The argument
covers ALL integer factors, signs, cuts, full real planes and
arbitrary suffixes, not a numerical search or a chosen centre.
Thus T^2 z=z has no solution anywhere. Nor can an
eventual core have period one or two. Any eventual periodic
core, if it exists, has even least period at least four.

This short-return exclusion is distinct from the global multiplicity
theorem. It does not become an all-period nonreturn theorem.

## 6. Three separately owned controls

### 6.1 GEOMETRY-OFF

Keep the main word rule/domain but real output (x,y).
The split inverse at (r,s,eta,x,y) is (rs,eta,x,y)
exactly when q(x)=r. The merge inverses at (c,eta,x,y)
are ALL (a,b,eta,x,y), a*b=c, with q(x) not
dividing a. These are OWN domains, not parabolic main images.
All IMAGE factors are 1, so the full cocycle is zero.

The digit d=q(x) is now constant along every trajectory.
Before the first split, all steps are merges and strictly
decrease finite word length, until a terminal or a split.
After a split the new head is d, and d|d
forces every subsequent step to split, increasing length forever.
Thus no state is eventually periodic; ALL source/H/extension
isotropy are zero. An initially empty or failed singleton is
already terminal. This is a global control result, not just
failure to find a short return.

### 6.2 UNIT-JACOBIAN

Keep main word permissions but use Phi_1 at every step.
With t=u^2-v, split inverse plane is (t,u) on
q(t)=r at target (r,s,eta). Merge inverse plane is
(t,u) for EVERY a*b=c with q(t) not dividing
a at target (c,eta). Unit factorizations and overlaps remain.
The actual inverse determinant is 1 for every branch, hence
the entire cocycle and ALL time groups H vanish. No
main inverse scaling or main real itinerary was borrowed.

There are no fixed states because word length still changes.
For any state its extension isotropy equals its source isotropy;
the latter's complete higher-period classification is NOT PURSUED.
Zero clock is not, by itself, absence of source recurrence.

### 6.3 SPLIT-ONLY

Retain Phi_a and divisor splits; every failed probe is terminal.
Only the split inverse from Section 2.2 remains, with its
own domain q(t/(r*s))=r and IMAGE 1/(r*s).
No merge predecessor survives. This is a separately derived
restricted owner, still retaining all objects and incoming terminal arrows.
Every defined step strictly increases word length; no eventual
periodic state exists. ALL source/H/extension isotropy are zero,
even though local clocks log(a) need not vanish.

The controls isolate real feedback, coefficient-dependent clock and
return execution. They do not force the chosen generator or
measure. The suffix theorem proves only its stated replication
property; no arbitrary-data realization or universal geometric no-go
is inferred as a PROVES_TOO_MUCH slogan.

## 7. Gate assessment and portfolio decision

| Gate | Exact GFE01 result | Boundary |
| --- | --- | --- |
| T0 | Full partial Borel owner, every inverse, exact image, all-Borel IMAGE and complete real extension | Not onto or ordinary continuous; no etale/classical lift |
| T1 | Actual divisor execution and plane transport own kappa=log(current head) | Stronger naturalness OPEN; generator and measure are designed |
| T2 | All possible positive times are log(Q); EVERY existing positive primitive has infinite suffix multiplicity | Finite nonzero target impossible; positive existence OPEN |
| Short returns | ALL fixed and two-step returns absent | Higher periods NOT PURSUED, not proved absent |
| T3 | NOT SUPPLIED / NOT PURSUED | No analytic owner borrowed |
| Classical/formal | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED | No Route credit |

Portfolio: **stop finite-multiplicity prime-time promotion; retain the owned
execution clock and full-suffix obstruction; fork a different architecture**.
The same-object ledger is intact. Negative records are search
constraints, not accumulated route credit. Positive 304 remains separate.

## Reproduction and AI-assisted review disclosure

Inputs are exactly the frozen finite-word rule, full real planes,
measure and all-point inverse version. Methods are explicit polynomial
inversion, change of variables, legal-history cancellation, word invariants,
right cancellation, full-tail equivalence and exact two-step inequalities.
No scientific numerical command, precision/period cutoff, external literature
lemma or prime/zero data is used. See [claim ledger](claim-ledger.md),
[evidence/locks](evidence/README.md), [internal review](evidence/independent-review.md),
[source/frontier record](evidence/scout-record.md) and [package index](README.md).
ARS three checkpoints are inherited-model/shared-context AI-assisted scrutiny,
not external peer review, independent-error evidence or formal verification.
No venue calibration; no claim that separate roles remove shared context.
Old packages, mirrors and Phase-I sources unchanged; 241/242 paused;
goal active. Markdown only; no publication, upload, staging or commit.
