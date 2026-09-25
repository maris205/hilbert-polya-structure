# Arithmetic quotient feedback: an owned reciprocal clock with unwanted fixed packets

Candidate ID: `ANG-20260920-QRF01`.
Paper ID: `299-quotient-remainder-reciprocal-flow`. Date: 2026-09-20.
Status: `OWNED RECIPROCAL IMAGE CLOCK; UNIT PACKET AND WRONG PRIME TIMES — STOP / FORK`.
Evidence: exact Borel-owner and all-fixed-point audit; no numerical experiment.

## Abstract

The current integer quotient's greatest divisibility atom changes a
reciprocal update on the full quotient/remainder source. All endpoints,
composites and terminal states remain. Its counting–Lebesgue measure
owns an IMAGE density; the explicitly frozen analytic branch completion
gives a consistent all-point clock on its entire partial-tail groupoid.
The fixed points are exactly one unit-labelled core and one core per
prime p. Their least times are 2 log alpha_q, where
alpha_q=(q+sqrt(q^2+4))/2 and q is 1 or prime. Every alpha_q^2
is irrational, so these are not even logarithms of integers. The
unit packet alone defeats the target. The two frozen changed-source
controls distinguish arithmetic selection from the reciprocal clock.
We stop without classifying other main returns or constructing T3.

## 1. Frozen object, question and lineage

The original 154-line [card](candidate-card.md) has SHA-256

    30b59f86e36d599376d6c96cc0969eadedc4ec3c695bed60a74c2007d5b49577

Write X=N_0 x [0,1), v(q,r)=q+r, d(0)=0, d(1)=1,
and d(q)=the greatest divisibility atom dividing q for q>=2.
The partial autonomous map is

    u=q+r-d(q),
    T(q,r)=(floor(1/u), 1/u-floor(1/u)) when u>0.

There is no step when u=0, and those objects are not removed.
Let mu be counting(q) times Lebesgue(r). The question is whether
the same source's measured clock has the required primitive packets.

| Same-object field | Owner | Boundary |
|---|---|---|
| Carrier and arithmetic | ALL X, current d(q) and reciprocal remainder | No prime-digit or irrational-only subspace |
| Measure | Full counting–Lebesgue mu | Sigma-finite, not invariant or uniquely natural |
| Arrows | Entire partial retained-lag tail groupoid of T | Not arbitrary fractional-linear transformations |
| Clock | Actual IMAGE law, with frozen analytic branch completion | A.e. data alone do not determine null restrictions |
| Packets | Complete time groups and actual tail/time equivalence | No identification by length or factor labels |
| Classical / analytic owner | NOT APPLICABLE / NOT SUPPLIED | No symplectic suspension, operator, trace or quantum claim |

The [prior-work](../../docs/prior_work/README.md) arrow is divisor
observables -> active quotient/remainder deformation -> arithmetic
subtraction and reciprocal update -> same-source measured Borel time.
This stated symbolic replacement does not assert a Logistic/Henon
conjugacy or a positive-dimensional conservative lift. Greatest-factor
choice, reciprocal rule, measure and endpoint version are designs;
their stronger naturalness stays OPEN.

[127](../127-prime-continued-fraction-digit-boundary/candidate-card.md)
observes prime digits of an unchanged Gauss map on irrationals and
does not supply this transition or a time owner. [284](../284-least-divisor-borel-flow/candidate-card.md)
and [295](../295-canonical-residue-generated-flow/candidate-card.md)
have profinite affine owners with different arrows and clocks.
The [definition record](evidence/scout-record.md) distinguishes
provenance from validation. No old theorem, source lock or Route
credit transfers. No prime table, prime-time roof, fitted parameter,
Mangoldt weight or zero data enters; factoring cost is not real time.

## 2. Full Borel source, exact branches and terminals

**Proposition 1.** X is a standard Borel source; mu is sigma-finite,
full-support and nonatomic. The frozen rule is a countable-to-one
Borel partial map with the exact branches and inverses in its card.
Its terminal set is

    {(0,0),(1,0)} union {(p,0):p prime}.

It is not onto X. All its actual finite branch pairs generate the
stated countable standard Borel retained-lag groupoid.

*Proof.* An atom above 1 in divisibility is precisely an integer
with no proper nontrivial divisor, hence a prime. Every q>=2 has
such a divisor: its least divisor greater than 1 is an atom.
The finite nonempty divisor set has a greatest atom. For prime q
we have d(q)=q. For composite q, any prime divisor p is proper,
so q/p>=2 and p<=q/2; consequently h_q=q-d(q)>=2.
For q=0,1, or prime q, h_q=0. Thus u>=0, and u=0 exactly
on the displayed terminal set. There is no h_q=1 case.

Each source fibre is the standard Borel interval [0,1), and the
countable coproduct is standard Borel. The Borel bijection v to
[0,infinity), inverse x->(floor x,x-floor x), transports mu to
ordinary Lebesgue measure. Each fibre has measure 1; hence mu is
sigma-finite and nonatomic. Every nonempty open subset in the
product topology contains a positive-length relative interval in
one fibre, so mu has full support. No topology-preservation claim
is made for v across integer boundaries.

For k=0, floor(1/u)=0 means u>1. For k>=1 it means

    1/(k+1)<u<=1/k.

Intersecting with u=h_q+r and 0<=r<1 gives precisely B_(q,k)
in the card, with the strict left and closed right endpoints.
On that branch the map is injective. Solving for its inverse gives
r=d(q)+1/w-q, w=k+rho>0. The requirement 0<=r<1 gives exactly
E_(q,k), and substitution proves both inverse identities. These
are Borel sets and Borel inverses. The countably many branches
partition the nonterminal domain, proving the asserted measurability
and countable fibres. No floor discontinuity is discarded.

The value 1 has no preimage: it would require h_q+r=1, impossible
when h_q is 0 or at least 2 and r is in [0,1). Thus T is not onto.
The question does not require a classification of its entire image.

Let D_m be the Borel domain of the mth iterate, D_0=X. For m,k>=0
the set of pairs in D_m x D_k with T^m x=T^k y is Borel by the
diagonal test. Their countable union with lag m-k gives a Borel
subset G_T of X x Z x X. Its source and range fibres are countable
because every finite iterate is countable-to-one. Units include all
terminals. Inversion swaps endpoints and negates lag. To compose
two arrows, align their two iterate counts at the middle point to
their maximum. The needed extra iterates exist because the longer
middle presentation exists; equality propagates those iterates to
the other endpoint. This proves closure and addition of lags even
for a partial map; associativity follows from the triple law.

Choosing the finite branch itinerary at each endpoint makes T^m
and T^k injective on the corresponding Borel cells. Intersect
their terminal images and take one strict inverse followed by the
other forward map. These countably many Borel branch-pair charts
cover exactly G_T. No extra fractional-linear arrow is generated.
All structure maps are Borel restrictions of the explicit laws. QED.

Only this Borel category is claimed. In particular floor jumps do
not justify a topological local-homeomorphism or an etale flow claim.

## 3. IMAGE density, analytic version and complete real time

For a nonterminal x=(q,r) put

    a(x)=1/(q+r-d(q))^2 = v(Tx)^2,
    A_m(x)=product_(0<=i<m) a(T^i x), A_0=1,
    L_m(x)=log A_m(x).

**Proposition 2.** On an actual inverse branch theta with source
value w, its Borel IMAGE density is J_theta(w)=1/w^2. On the
whole retained-lag owner the frozen analytic version is

    J(x,m-k,y)=A_k(y)/A_m(x),
    c(x,m-k,y)=L_m(x)-L_k(y).

It is a finite Borel additive cocycle, including all retained
endpoints. The real extension owns a complete jointly Borel
time action. A.e. IMAGE data alone do not force this version on
arbitrary null restrictions.

*Proof.* In value coordinates the inverse branch is w->d(q)+1/w;
its absolute derivative is 1/w^2. Therefore, for every Borel
E subset E_(q,k),

    mu(theta(E))=integral_E (1/v(z)^2) dmu(z).

One may first integrate the derivative over intervals in the branch
and then extend by uniqueness of Borel measures; endpoints have
zero Lebesgue mass. The forward branch's absolute derivative is
a(x), not 1/v(Tx)^2. Finite branch itineraries are restrictions
of compositions of these analytic one-variable formulas. The
ordinary chain rule gives forward derivative A_m. Thus a chart
from y to x has derivative A_k(y)/A_m(x). Change of variable
proves the IMAGE identity on all its Borel subsets, including
null restrictions where that identity alone is vacuous.

If two presentations have the same endpoints and lag, their m,k
counts differ by a common integer. Extend the shorter presentation
to the longer one, which is possible by its existence. The added
forward derivatives at their common terminal point cancel. This
proves presentation independence at EVERY point, not merely a.e.
Aligning middle iterate counts as in Proposition 1 and using the
chain rule proves multiplicativity of J and additivity of c.
Units have c=0 and inverses have opposite c. Positivity and
finiteness follow from u>0 at each finite forward step.

The analytic formulas are also the card's explicit all-point
completion on half-closed and singleton restrictions. We do not
infer its uniqueness from IMAGE identities on measure-zero sets.
The fixed points used below, however, lie in open interiors of
single source/target branches: there the positive continuous density
is uniquely fixed by the IMAGE law and full-support Lebesgue measure.
Their periods are not a separately adjustable endpoint convention.

The extension arrows (g,s):(y,s)->(x,s+c(g)) and their structure
maps are Borel. Translation Phi_t(x,s)=(x,s+t), and likewise on
arrows, is jointly Borel, commutes with every extension arrow and
has inverse Phi_(-t) for every real t. It is complete. Equivalently
the derived partial step (x,s)->(Tx,s-log a(x)) has the same full
retained-lag extension. No additional roof or flow owner enters. QED.

The induced action on the orbit set is understood through this
groupoid. No standard Borel coarse quotient, Hausdorff topology or
embedded circle is asserted. At (x,s), its full time stabilizer is
H_x=c(G_x^x), independently of s. Negative one-step clocks can occur;
a positive-roof interpretation is neither assumed nor needed.

## 4. ALL fixed points and the decisive packet failure

**Theorem 3.** The fixed source points are precisely

    x_q=(q,alpha_q-q), alpha_q=(q+sqrt(q^2+4))/2,
    q in {1} union {primes}.

Each is a distinct primitive cyclic-time packet, with source lag
isotropy Z, trivial fixed-object extension isotropy and

    H_(x_q)=(2 log alpha_q) Z.

In particular the unit packet has least time
log((3+sqrt(5))/2). Every displayed time is NOT the logarithm of
an integer; at prime p it is strictly greater than 2 log p.

*Proof.* At a fixed point the positive value x=q+r satisfies
x=1/(x-d(q)), or x(x-d(q))=1. If q=0 then d=0 and the positive
solution x=1 is outside that fibre. For d>=1 the unique positive
solution alpha_d satisfies d<alpha_d<d+1. Thus its integer quotient
must be q=d. This holds exactly for q=1 or prime q, proving both
exhaustion and existence. The remainder lies strictly inside (0,1),
so no terminal or integer endpoint is a fixed point.

At x_q all iterates exist and equal x_q, so the entire source
lag isotropy is Z. Here a(x_q)=alpha_q^2, hence every isotropy
lag l has c=l*2 log alpha_q. Since alpha_q>1 the map from Z is
injective: the extension's fixed-object isotropy is trivial and
the least positive time is exactly 2 log alpha_q. Positive repeats
are its integer multiples in that same packet, not new primitives.

Two fixed points admit a tail arrow only if their constant forward
tails are equal, that is, only if the points themselves coincide.
Excursions through arbitrary finite preimages cannot change this,
since compositions already belong to the full tail groupoid.
All real phases at a fixed core belong to its one time packet.
Thus no uncounted identification or extra phase multiplicity changes
the displayed primitive convention.

The number alpha_q is an irrational root of X^2-qX-1: a rational
root of this monic integer polynomial would be an integer, whereas
q<alpha_q<q+1. Since alpha_q^2=q*alpha_q+1 and q>=1, its square
is also irrational. Therefore 2 log alpha_q=log(alpha_q^2) is not
log N for any positive integer N. The inequality at prime p follows
from alpha_p>p. Taking q=1 gives the explicit unit time. QED.

This proves failure of the prime-time target without claiming that
no other main periodic point could have time log p. Other periods,
eventual returns and the complete returning locus are NOT PURSUED.
Deleting q=1 would change the source and would not fix the proven
wrong times of the retained prime fixed cores.

## 5. Frozen controls, each with its own clock

### FACTOR-OFF: complete reciprocal involution

With d(q)=0 for all q, the value map is T_0(x)=1/x on x>0;
0 is its only terminal. The same change-of-variable argument gives
its OWN forward derivative a_0(x)=x^(-2) and inverse density 1/w^2.
Since T_0^2 x=x and a_0(x)a_0(1/x)=1, every two-step clock is zero.
At x=1 the source isotropy is Z and every clock is zero; at other
x>0 it is 2Z, again with zero clock. At 0 it is trivial. Therefore
H_x={0} at EVERY point, and no positive cyclic-time packet exists.
The extension retains these source isotropy groups: zero clock
does not delete arrows or turn isotropy into positive periods.

The branch q=1,k=1 is the singleton x=1, so its pointwise density
1 comes from the frozen analytic completion, not the zero-measure
IMAGE identity on that singleton alone. This control preserves the
endpoint precisely where an unqualified full-support argument fails.

### QUOTIENT-READOUT: all integer fixed labels

With d(q)=q for all q, u=r, so every integer endpoint is terminal.
The actual inverse branch again has derivative 1/w^2; forward
a_Q(x)=r^(-2) where r>0. Deriving this from this changed rule and
measure, rather than transferring the main cocycle, gives its own
complete branch-pair owner by the proof of Proposition 2.
Its fixed points are exactly x_q with EVERY integer q>=1. Each
has full source isotropy Z, trivial extension fixed-object isotropy,
H=(2 log alpha_q)Z and a distinct packet. In particular q=4 is
now an additional fixed core. No higher-return claim is made.
The main arithmetic readout really restricts the fixed labels;
that fact does not repair the reciprocal times or prove naturalness.

### Main endpoint and terminal ownership

The original endpoint (4,0), value 4, satisfies d(4)=2 and follows

    (4,0) -> (0,1/2) -> (2,0), then no forward step.

The forward derivatives are 1/4 and 4, with product 1. This is an
actual finite path and zero two-step clock, NOT a periodic orbit.
The endpoint (0,0) has no step. A path that reaches a terminal
cannot have nonzero tail lag isotropy, since equality of two unequal
forward iterates would create a repeatable cycle. Thus these tested
terminal/preterminal points have trivial source and extension
isotropy and H={0}. Their null status never authorizes removal.
The main (1,0) is terminal, while FACTOR-OFF keeps it as a fixed
point with zero time group; the two owners are not conflated.

## 6. Gate assessment, decision and reproducibility

| Gate | Exact result for QRF01 | Limit |
|---|---|---|
| T0 | ESTABLISHED: full partial Borel source, arrows and complete real extension | No topological/classical lift claim |
| T1 | ESTABLISHED: divisibility readout and actual IMAGE law with analytic completion | Naturalness OPEN; null-version boundary explicit |
| T2 | ESTABLISHED for ALL fixed cores; target FAIL | Unit packet and wrong prime-core times; other returns OPEN |
| T3 | NOT SUPPLIED / NOT PURSUED | No zeta, trace, operator or analytic rescue |
| Classical A0/A1/A2 | NOT APPLICABLE | Formal coordinates UNASSIGNED |
| Route B | NOT INVOKED | No Route readiness or B evaluation |

Portfolio: **stop target promotion / fork**. The same-object ledger
remained intact: no endpoints, terminals, quotients, inverse domains
or packets were dropped. The strongest result is an owned measured
Borel construction with a decisive fixed-point obstruction, not a
global no-go theorem or a complete periodic classification.

Inputs and proofs are exact at arbitrary indices; no finite cutoff,
precision, numerical trajectory, external literature campaign or
target fitting is used. The [claim ledger](claim-ledger.md),
[evidence](evidence/README.md), [native review](evidence/independent-review.md)
and [scout record](evidence/scout-record.md) preserve provenance,
controls and limitations. Review is inherited-model/shared-context
internal scrutiny, not external peer review or formal verification.
All old packages and mirrors remain unchanged; 241/242 stay paused;
the programme goal remains active. No PDF/LaTeX, staging, commit,
upload, publication or formal Route-B action occurred.
