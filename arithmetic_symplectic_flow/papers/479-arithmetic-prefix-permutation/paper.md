# Arithmetic first-hit prefix transport with a globally zero clock

Candidate ID: ANG-20260925-APP01.
Paper: 479-arithmetic-prefix-permutation; batch PRE-P0-STRUCTURE-20260925-Z, round 5/5.
Date label: 2026-09-25. Type: ANG partial measured-history owner.
Outcome: OWNED PREFIX-PERMUTATION IMAGE; GLOBAL ZERO CLOCK — STOP / FORK

## Abstract

The first adjacent proper-divisor witness selects an unbounded finite prefix
of an entire positive-integer sequence, and MAIN rotates that actual prefix.
For the frozen iid measure, we establish the full source, all actual inverses
and every-Borel IMAGE for MAIN and three independently owned controls.
Their prescribed pointwise inverse densities are identically one, including
all null histories. Every legal clock and the complete retained-lag cocycle
therefore vanish. The ENTIRE period group of every source object is zero,
and real translation on the extension has no positive primitive packets.
This global clock obstruction decides the frozen gate before a periodic census.
The sole authorized forward test distinguishes all four actions, but does not
rescue their clocks. Source periodic locations are not classified.

## 1. Frozen carrier, probability and actual arithmetic

The [frozen card](candidate-card.md), original lines 1–103, is the contract.
Let \(A=\mathbb Z_{\ge1}\), \(X=A^{\mathbb N_0}\), with discrete-coordinate
product topology and its Borel sigma-algebra. For a finite word \(w\), write
\([w]=\{w\xi:\xi\in X\}\). Freeze
\[
\rho(a)=\frac1{a(a+1)},\qquad
p(w)=\prod_{0\le i<|w|}\rho(w_i),\qquad \mu=\rho^{\mathbb N_0}.
\]
Normalization follows from
\(\sum_{a=1}^m\rho(a)=1-1/(m+1)\to1\).
The consistent cylinder values \(\mu([w])=p(w)\) define the countable product
probability. Every nonempty basic cylinder has positive measure, so support is
all \(X\). Every singleton has measure at most \(2^{-r}\) for every prefix
length \(r\), hence zero. No point is deleted because of this atomlessness.
The insertion map \(\iota_w:\xi\mapsto w\xi\) is a homeomorphism onto \([w]\),
and product factorization, first on cylinders and then on their Borel
sigma-algebra, gives
\[
\mu(\iota_w E)=p(w)\mu(E)\quad\hbox{for every Borel }E\subset X. \tag{1}
\]

Use the exact predicates
\[
D(a,b)\iff1<a<b,\ a\mid b,\qquad
N(a,b)\iff1<a<b,\ a\nmid b.
\]
N is not the full complement of D: unit and reversed pairs satisfy neither.
For a predicate \(P\), let \(k_P(x)\) be the FIRST adjacent hit, if one exists,
and \(L_P(x)=k_P(x)+2\). Its no-hit set is the intersection of all adjacent
non-hit conditions, hence a closed Borel subset of the full product.
The hit domain is its open complement. The law is a mathematical partial
action; no finite-time algorithm deciding every no-hit history is assumed.

| Owner | Own parser | Own actual prefix operation |
| --- | --- | --- |
| M MAIN | first D hit | left-rotate the entire first \(L_D\) letters |
| A arithmetic-OFF | every pair hits; \(L=2\) | swap the first two letters |
| N nondivisor-first | first N hit | left-rotate the entire first \(L_N\) letters |
| R rotation-OFF | first D hit | reverse the entire first \(L_D\) letters |

Every suffix beyond the selected prefix is unchanged at that step.
Subsequent parsing uses the changed full sequence, not a retained external
integer or an independent acceptance register. A is total; each other map
is genuinely undefined on its no-hit set. Those points retain identities and
ALL incoming, not absorbing self-loops. All units, constant/mixed/null tails
and possible infinite histories remain in \(X\), with no resampling or padding.

For a first pair \((d,n)\) and any tail, MAIN's length is two exactly when
\(1<d<n,\ d\mid n\). This is the prior proper-divisor symbolic interface.
Its autonomous deformation changes actual adjacent relations by moving the
whole selected prefix, rather than merely reporting a static prime/composite
label. The original measure and permutation rule are declared designs.
No conservative/symplectic lift or natural prime clock follows from this interface.

## 2. Exact source words and the entire inverse atlas

For \(P=D,N\), let
\[
W_L^P=\{w\in A^L:P(w_{L-2},w_{L-1}),\quad
\neg P(w_i,w_{i+1})\text{ for }0\le i<L-2\},\quad L\ge2.
\tag{2}
\]
The earlier-hit condition is empty when \(L=2\).
The cylinders \([w]\) for all these words partition the hit domain:
every hit has a first index; two different lengths cannot describe the same
source because the shorter witness would be earlier than the longer one.
Words of the same length give disjoint cylinders.
A instead uses all words of length two, a partition of all \(X\).
These are countable families since all finite integer-word sets are countable.
The domain lengths really are unbounded: for every \(L\ge2\), the word
\(1^{L-2}24\) belongs to \(W_L^D\), and \(1^{L-2}23\) belongs to \(W_L^N\).
These are source-domain witnesses, not additional forward or periodic tests.

For each owner take its words and its permutation \(\pi_L\) from the table.
Write \(v=\pi_Lw\). The full branch and inverse are
\[
U_w:w\xi\mapsto v\xi,\qquad
\theta_w:v\xi\mapsto w\xi,\qquad
\operatorname{dom}\theta_w=[v]. \tag{3}
\]
Every tail is allowed: the first hit is already fixed inside \(w\).
Both identities follow from the inverse finite permutation. These are actual
homeomorphisms between the displayed Borel cylinders.
Conversely every legal source has its unique first-hit length and source
word, so (3) lists all actual inverse branches. Its full image is the union
of these output cylinders; surjectivity is not presumed.

Operationally, at a target \(y\), enumerate EVERY \(L\ge2\). M/N propose
\[
(y_{L-1},y_0,\ldots,y_{L-2},y_L,y_{L+1},\ldots),
\]
and retain it exactly when its own first hit is \(L-2\).
R proposes
\[
(y_{L-1},y_{L-2},\ldots,y_0,y_L,y_{L+1},\ldots)
\]
and checks that source's first D hit. A has only its length-two swap.
No target-outgoing check or length cutoff occurs.
If two accepted labels produced one source, its unique parser would force
the same length and then the same prefix word. Thus labels do not duplicate
an actual predecessor. Distinct predecessors of the same target all remain;
uniqueness of the source label does not assert injectivity of the whole map.
Reversal inverts its fixed prefix permutation; this does not presume that
reparsing on the next R step chooses the same length.

## 3. Every-Borel IMAGE and the first global clock gate

For an arbitrary Borel \(B\subset[v]\), put \(E=\iota_v^{-1}B\).
Equation (1) gives the exact, not only cylinder-level, identity
\[
\mu(\theta_w B)=p(w)\mu(E)
=\int_B\frac{p(w)}{p(v)}\,d\mu. \tag{4}
\]
For every one of the four owners, \(v\) is a permutation of the letters of
\(w\); multiplication of their common marginal weights gives \(p(v)=p(w)\).
Consequently the FROZEN every-point prescription is
\[
J_{\theta_w}(v\xi)=\frac{p(w)}{p(v)}=1
\quad\hbox{for every }\xi\in X. \tag{5}
\]
All weights are positive, so no zero denominator or exceptional history occurs.
Equation (4) proves IMAGE on every Borel subset, including null subsets;
(5) fixes the stated version at every point, not by an a.e. uniqueness claim.
Nothing has been changed after looking at a return or null-set obstruction.

Thus for each owner, on every LEGAL step,
\[
\kappa_U(z)=-\log J_{I_z}(Uz)=0. \tag{6}
\]
There is no outgoing clock assigned at a terminal point; its zero-step sum
remains defined. These are four own IMAGE proofs, not a clock borrowed from M.
Branchwise (4) does not assert stationarity or global measure preservation
of a potentially many-to-one partial U. Multiple predecessors do not supply
an additional branch-count clock; that would change the frozen owner.

## 4. Complete histories, kernels, isotropy and real phases

For each U let \(D_r\) be its \(r\)-legal-step domain, \(D_0=X\), and
\(S_r(z)=\sum_{i=0}^{r-1}\kappa_U(U^iz)\), \(S_0=0\).
Every legal \(S_r\) is zero by (6). Retain exactly
\[
\mathcal G_U=\{(z,r-s,w):U^rz=U^sw\text{ legally},\ r,s\ge0\},\qquad
c(z,r-s,w)=S_r(z)-S_s(w)=0. \tag{7}
\]
Source is w, range z. Units, inversion and multiplication are the usual
equal-triple operations; no free word labels add arrows.
Composition follows by advancing the two intermediate histories to their
later common intermediate time. That legal iterate supplies every required
extra step even for a partial map. The relation is a countable union of
Borel equalizer sets, and inverse fibres are countable by (3).
Equal-lag presentations differ by equal advancement on both sides;
their equal future sums cancel. This proves descent and additivity of c
pointwise; its zero value also follows directly from (6).

Finite actual branch itineraries are countable. Restrict both legs of (7)
to their injective itineraries and compose inverse-first-leg with forward-
second-leg on their matching Borel images. The empty itinerary is the identity
on all X, including terminals. These branch pairs cover every arrow.
Repeated (4) proves their own every-Borel IMAGE is 1, precisely
\(\exp(-c)\). The actual forward arrow \((Uz,-1,z)\) has clock
\(-\kappa_U(z)=0\), with the same orientation as the frozen contract.

The complete kernels are
\[
K_c=\mathcal G_U,\qquad
K_{\rm lag}=\{(z,0,w):\exists r\ge0,\ U^rz=U^rw\text{ legally}\},\qquad
K_{\rm joint}=K_{\rm lag}. \tag{8}
\]
These formulas keep every actual arrow rather than identifying a kernel
with units merely from its name.
For source isotropy, a nonzero self-lag is equality of two different forward
iterates, hence exists exactly at an eventually periodic source.
If its eventual cycle has least period \(\ell\), equality of positions on
that cycle and arbitrary legal advancement show
\[
\operatorname{Iso}_{\mathcal G_U}(z)=\ell\mathbb Z.
\tag{9}
\]
Otherwise the isotropy is trivial. This is a conditional structural theorem,
not a location/classification of periodic sources. Terminal sources cannot
have such a nonzero self-lag; all their incoming arrows still remain.

Retain all \(X\times\mathbb R_h\) with \((w,h)\mapsto(z,h+c)\).
Since c is zero, extension isotropy is the FULL source isotropy (9), and
\[
H_z=c(\operatorname{Iso}_{\mathcal G_U}(z))=\{0\}
\quad\hbox{at EVERY source object}. \tag{10}
\]
Two extension points are related exactly when their source points belong to
the same source orbit and their real heights are equal.
Thus the quotient SET is \((X/\mathcal G_U)\times\mathbb R\), with no smooth,
Hausdorff or global measurable-section assertion. Real translation moves h
to \(h+t\) and stabilizes an orbit class only when \(t=0\).
There are no positive primitive translation packets or their repetitions.
Every real phase survives; distinct source orbits with the same zero clock
are not collapsed. Source repetitions encoded by (9) remain as zero-clock
isotropy and must not be misreported as positive closed-flow periods.

For completeness, apply every accepted inverse (3) to define
\(\operatorname{Pre}_U(A)\), then iterate from \(\operatorname{Pre}^0_U(A)=A\)
without an index or depth bound. Induction on depth proves this is exactly
every finite incoming history, including those of terminal targets.
Compatible infinite histories are exactly sequences whose every successive
pair passes (3); every finite-prefix condition is retained.
No assertion that every finite history extends infinitely is needed.
An explicit full orbit test is
\[
\mathcal O_U(z)=
\bigcup_{\substack{r\ge0\\z\in D_r}}\ \bigcup_{s\ge0}
\operatorname{Pre}_U^s(\{U^rz\}). \tag{11}
\]
Each membership is precisely an actual equal-future arrow, and conversely
every arrow has such indices. This covers all source packets, not only
eventually periodic ones. All-zero sums make an arrival phase
\(h-S_a(z)=h\); any other arrow to the same base also preserves h.
Equations (8)–(11) give the whole incoming/kernel/H/phase ledger without a census.

## 5. The sole concrete forward-control test

For the frozen input \(z_*=(3,2,4,5,1,1,\ldots)\), the first pair (3,2)
satisfies neither D nor N because it is reversed; (2,4) satisfies D but not N;
(4,5) satisfies N. Apply just the one specified step:

| Owner | First-hit k; length L | Actual one-step image |
| --- | --- | --- |
| M | \(1;\ 3\) | \((2,4,3,5,1,1,\ldots)\) |
| A | \(0;\ 2\) | \((2,3,4,5,1,1,\ldots)\) |
| N | \(2;\ 4\) | \((2,4,5,3,1,1,\ldots)\) |
| R | \(1;\ 3\) | \((4,2,3,5,1,1,\ldots)\) |

The four outputs are distinct. Arithmetic parsing and prefix operation thus
change an actual image in this test. No second iterate, fixed-point test,
cycle word, selected core or periodic census was performed.
This one-step difference does not distinguish their clocks: all four own
global clocks are already zero by (5)–(7).

## 6. Scope, target failure and decision

The whole source, original measure, pointwise IMAGE version and actual
histories remain intact. The decisive obstruction is global clock value,
not a source-period computation: the required NONEMPTY positive prime-packet
ledger is impossible for every frozen owner by (10).
An empty positive ledger is not a prime-purity success. We do not claim
that there are no periodic symbolic sources; their locations remain OPEN.

| Obligation | Scoped status |
| --- | --- |
| T0 full source/normalization/inverse/IMAGE | ESTABLISHED |
| Exact proper-divisor lineage and active one-step discrimination | ESTABLISHED |
| T1 useful positive prime-return clock | NOT PASSED: global zero-clock obstruction |
| Full-history kernels/H/isotropy/phases | ESTABLISHED structurally on the whole source |
| Positive primitive/repetition ledger | EMPTY globally; required nonemptiness fails |
| Source periodic locations / periodic census | OPEN / NOT AUDITED |
| Strong naturalness / PROVES_TOO_MUCH beyond this obstruction | OPEN; not rescued by active syntax |
| T3 / operator / trace | NOT AUDITED |
| Classical conservative/symplectic/positive-roof fields | NOT APPLICABLE |
| Formal coordinates / Route B | UNASSIGNED / NOT INVOKED |

STOP / FORK at the frozen clock-first gate. No new density, manual roof,
aggregate-predecessor clock, selected recurrent subset or extra orbit search
is introduced. This is a statement about the four frozen owners, not a
universal no-go for all arithmetic symbolic dynamics or other clock owners.

## 7. Inputs, exposure and author assistance

Author fully read original card 1–103 through EOF, SHA-256
dee878be33686a7a14383adefb27c0228aea00ff05f9da1d894e20a11dd7086d.
Root separately released mathematical authorship after its CP1 read.
This author read no CP1 report, raw proof, peer manuscript or final review.
The method is exact finite-prefix/product-measure and history algebra.
No scientific code, approximate experiment, network or external dataset was used.

The root supplied this seed after a SEPARATE no-ID precursor was rejected
for exact identity with 455's N owner. That precursor is not this candidate
and contributes no mathematical result here.
Current definition comparisons were
papers/381-coprime-exchange-heap/candidate-card.md, 1–43/93, prefix SHA
e6e69e4808cf86eea1f45ee1892f879a1d0cd700851916589b0592cf39ea453e,
and same-author helper's
papers/415-divisor-word-sweep/candidate-card.md, 1–47/109, prefix SHA
d4f9264168569d5fcc7818164c7047235b871c736579fd7658bbafa6a71c919d.
Only appended-outcome headings were exposed in those comparisons; no old
proof/outcome body was read or transferred. The author previously authored
381 and retains that shared history. Root informally considered permutation
IMAGE feasibility before freeze; this was not a blind or outcome-sealed trial.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author read
only the original 103-line APP01 card for its released task, independently
measured the same hash, and checked the sole forward test and source-label
uniqueness. It read no other science and performed no second iterate,
periodic test, file write or extra delegation. It is not a reviewer seat.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Shared-model/history work is
NOT_CALIBRATED, with no novelty, nonconjugacy or independent-human-review claim.
Root's subsequent comparison/review is separate, not an input to these proofs.

Navigation: [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[package README](README.md), [separate final review](evidence/review.md).
