# Successor–gcd–carry dynamics: an owned clock and a second prime-two packet

**Candidate ID:** `ANG-20260920-SGC01`  
**Paper ID:** `279-successor-gcd-carry-flow`  
**Date:** 2026-09-20; exact full-state audit.  
**Status:** `OWNED ARITHMETIC CARRY CLOCK; EXTRA PRIME-TWO PACKET — STOP / FORK`.  
**Route state:** broadened T0–T2 audit only; formal `UNASSIGNED`; B `NOT INVOKED`.

## Abstract

A deterministic arithmetic seed now performs successor, carry division
or gcd descent itself, without an independent divisor-scan register.
The full profinite source and its rootwise Haar measure yield a
surjective local homeomorphism, a complete retained-lag groupoid and
its actual continuous image-index clock. Every periodic full state
is an integer seed. The complete ledger has one log-p packet for
every prime p>=3, but TWO distinct least-log-2 packets: the seed-1
fixed point and the seed-2/3 two-cycle. Equal time is not repetition
of the same orbit. Both must remain, so the prime-single-packet
target stops. All noninteger seeds are retained and have no actual
time return, even when their branch itinerary is periodic. The
coarse extension quotient is not T1. Source normalization and local
arithmetic feedback are established only within the declared design;
naturalness remains OPEN and no T3 or formal Route claim follows.

## 1. Frozen question, lineage and ownership

The [version-1 card](candidate-card.md) fixes all inputs before proof.
The [prior-work arrow](../../docs/prior_work/README.md) is prime/composite
gcd observables -> compatible congruence state -> current-residue
successor/carry -> Euclidean feedback -> its arithmetic groupoid.
This changes the source evolution, not merely its interpretation.
It is not a Logistic/Henon conjugacy or classical geometric lift.

| Component | Exact SGC01 owner |
| --- | --- |
| Source | Y is the coproduct of full K=Z_hat over every integer n>=2 |
| Update | The same seed executes x+1, (x+1)/n, or x/d with modulus descent |
| Measure | Normalized additive Haar h on every root, root masses one |
| Arrows | ALL retained-lag T-tail arrows with full arithmetic topology |
| Clock | c=−log of the same measure's Borel IMAGE derivative |
| Time | Full real extension and translation, not algorithmic step counting |
| Packets | Actual full-state isotropy images and actual arrow/time equivalence |
| Absent fields | Classical symplectic map/suspension N/A; analytic, Hamiltonian, contact and quantum owners NOT SUPPLIED |

[278](../278-haar-seeded-witness-flow/candidate-card.md) has hub/scan/escape
roots and a different seed update. [274](../274-euclidean-residue-index-flow/candidate-card.md)
has independently marked paths. [238](../238-nonconfining-source-frontier/candidate-card.md)
and [228](../228-gcd-defect-cocycle/candidate-card.md) retain explicit finite
scan phases with other carriers and clocks. Their results do not
supply the clock, state returns or multiplicities proved here.

## 2. Complete arithmetic update and measure

For x in K, let j be its residue modulo n in {0,...,n−1}. Set

```text
j=n−1:                  T(n,x)=(n,(x+1)/n)             [CARRY]
j=0, or gcd(n,j)=1,
  excluding j=n−1:      T(n,x)=(n,x+1)                 [SUCCESSOR]
1<=j<=n−2, d=gcd(n,j)>1: T(n,x)=(d,x/d)               [GCD]
```

This branch priority is part of the design. Every root and seed,
including negative integers and zero, stays in the carrier. For
example T(6,2)=(2,1) changes both the source modulus and the seed.
The rule uses no primality predicate or prime-dependent constant.

### Lemma 1 — integer division and Haar scaling

For a positive integer a, multiplication by a on K is injective,
with image the kernel of reduction modulo a. For Borel B subset K
and integer b,

    h(b+aB)=h(B)/a.

Also, if ax=b in K with a positive integer and b an integer, then
a divides b in Z and x is that ordinary integer b/a.

**Proof.** Reducing ax=0 modulo am implies x=0 modulo m for every
m. Conversely, if x=0 modulo a, compatible residues obtained by
dividing x modulo am by a, modulo m, define its unique quotient.
Translation-invariant normalized measure gives every coset modulo
m mass 1/m. These cylinders generate the Borel sigma-algebra and
construct and uniquely determine h. On B=t+mK the scaling formula
is the equality 1/(am)=(1/m)/a; uniqueness of finite measures extends
it to Borel sets. Finally ax=b implies b=0 modulo a, and injectivity
identifies x with b/a. No assertion that K is an integral domain
is used. The same cylinders prove full support and h({x})=0. QED.

### Proposition 2 — full local-homeomorphism owner

Y is noncompact, locally compact Hausdorff and second countable;
mu is Radon, sigma-finite, full-support and non-atomic. T is an
onto local homeomorphism. On each branch the full domains, images
and forward IMAGE derivatives are:

| Branch at root n | Domain in K | Image and root | Forward J |
| --- | --- | --- | --- |
| SUCCESSOR residue j | j+nK | j+1+nK at n | 1 |
| CARRY | −1+nK | all K at n | n |
| GCD residue j, d=gcd(n,j)>1 | j+nK | j/d+(n/d)K at d | d |

**Proof.** Each listed clopen domain maps homeomorphically to its
listed clopen image by Lemma 1 or translation. In particular GCD
does NOT in general map onto its entire target root. Its inverse
y->dy is restricted to j/d+(n/d)K. Carry alone gives every (n,y)
the preimage (n,ny−1), so T is onto without deleting anything.
The Borel derivatives follow from Lemma 1: division by a multiplies
measure by a, whereas successor preserves it. A compact subset of
the countable coproduct meets finitely many roots; the stated
topological and measure properties follow. QED.

Every finite inverse branch is theta_alpha(t)=a_alpha t−b_alpha
on its actual clopen terminal domain, with a_alpha a positive
integer and b_alpha a nonnegative integer. The elementary inverses
are t−1, nt−1, dt. Composition gives

    a_(alpha beta)=a_alpha a_beta,
    b_(alpha beta)=b_alpha+a_alpha b_beta,
    mu(theta_alpha B)=h(B)/a_alpha

for Borel B in the terminal domain. Domain restrictions remain in
force under composition; no unrestricted affine action is inferred.

## 3. Full-arrow clock and real time

Let G_T={(z,m−k,w):T^m z=T^k w}, with source w, target z and
integer lag retained. For inverse branches alpha,beta ending in
the same root and any clopen arithmetic C in the intersection of
their terminal domains, use bisections

    B(alpha,beta;C)={(theta_alpha(t),|alpha|−|beta|,
                     theta_beta(t)):t in C}.

Empty words and arbitrary residue cylinders are included, so this
topology separates all arithmetic seeds, not just their itineraries.

### Proposition 3 — owned image clock

This is a second-countable locally compact Hausdorff étale groupoid.
Its continuous IMAGE derivative and clock on each bisection are

    J=a_beta/a_alpha,       c=log a_alpha−log a_beta.

**Proof.** The source and image of a Borel subset parameterized by
B subset C have masses h(B)/a_beta and h(B)/a_alpha. Their ratio
proves J. A different presentation of the same retained-lag arrow
extends both branches by the same local terminal continuation;
the two a factors acquire the same multiplier. This proves
presentation independence. Common terminal restrictions and
matched-branch composition prove the cocycle laws. The formulas
are constant on each bisection and hence continuous. Full support
makes this continuous version unique, including at null seeds.

The bisections and their residue restrictions form a countable
compact-open basis. Common refinements follow actual finite T
branches, establishing the topological groupoid operations. Source
and range are locally homeomorphisms. Endpoints and discrete lag
separate different arrows, proving Hausdorffness. QED.

This is the local-homeomorphism construction described in
[Sims, Examples 2.3.7 and 2.4.6](https://www.aidansims.com/papers/Sims2017.pdf);
the concrete branch domains and arithmetic clock above are proved
here, without importing a graph-only state space or operator.

The extension has units Y×R and arrows
(g,u):(w,u)->(z,u+c(g)). With topology G_T×R it is locally compact
Hausdorff and étale; branch bisections give the local source/range
homeomorphisms. Translation by every real time is jointly continuous,
complete and respects arrows. Forward carry has clock −log n;
positive insertion-lag has clock +log n. Successor has clock zero.
This is not the runtime of the algorithm or a positive-roof suspension.

## 4. Full periodic states: a decisive second packet at two

The earliest decisive check is already an exact full-state cycle:

    (2,1) --CARRY--> (2,1),
    (2,2) --SUCCESSOR--> (2,3) --CARRY--> (2,2).

These two cycles have disjoint forward tails. Both traverse exactly
one factor-2 carry per primitive cycle. Thus the second packet is
not a repetition of the first. The following bounded classification
finishes the precommitted all-state tests, without a numerical census
or any modification intended to remove this counterexample.

### Lemma 4 — every periodic full seed is an integer

**Proof.** The modulus decreases strictly on every GCD step, so a
periodic orbit has constant modulus n and no GCD step. A nonempty
period word contains r carries and otherwise successors. Its inverse
formula is n^r x−b, with integer b>0: every elementary inverse in
that word has intercept −1, and positive slopes preserve positivity
of the accumulated b. A full return requires

    (n^r−1)x=b.

If r=0 this is impossible. If r>=1, Lemma 1 forces x to be a positive
ordinary integer. Equality of branch itineraries alone is insufficient
to obtain this equation. QED.

### Lemma 5 — all integer seeds eventually reach the listed cycles

At a constant modulus n>=3, the unfiltered successor/carry algorithm
has exactly the cycle 1->2->...->n−1->1. At n=2 it instead has
two cycles: {1} and {2,3}.

**Proof.** On integers x<=0 every permitted step increases x
strictly until it is positive. GCD division of a negative seed,
when it occurs, also increases it, and positive seeds remain positive.
The modulus can decrease only finitely many times. After its last
decrease the orbit follows the unfiltered successor/carry rule.

For a positive x, advance to the next carry. Its output is
floor(x/n)+1. For n>=3 and x>=n this is strictly smaller than x;
repeated carries therefore reach {1,...,n−1}, which is the displayed
cycle. If n is composite, this cycle contains a nonunit residue
1<j<n−1 and the actual GCD rule forces another modulus decrease.
Consequently the final modulus cannot be composite.

For n=2, seed 1 is fixed. The positive set {2,3,...} is invariant,
and the next-carry output floor(x/2)+1 decreases x when x>2 and
equals 2 when x=2. Its orbit therefore reaches the two-cycle {2,3}.
Nonpositive seeds reach 1. There is no GCD branch at n=2. QED.

### Theorem 6 — complete full-state return ledger

The periodic full states are exactly the following cycles. Write
B_P for all states eventually entering the indicated cycle P.

| Primitive cycle P | Least T-lag ell | Isotropy clock on r ell | Least positive time |
| --- | --- | --- | --- |
| C_p={(p,1),...,(p,p−1)}, prime p>=3 | p−1 | r log p | log p |
| C_2^a={(2,1)} | 1 | r log 2 | log 2 |
| C_2^b={(2,2),(2,3)} | 2 | r log 2 | log 2 |

For z in B_P, source isotropy has lags ell Z and clock image as in
the table. For every other state source isotropy and the time-return
group are trivial. Every fixed-object extension isotropy group is
trivial. There is one abstract cyclic-return packet for each table
row, and its positive repeats have time r times that row's least time.

**Proof.** Lemmas 4–5 prove the exhaustive periodic classification.
Nonzero-lag isotropy T^m z=T^k z is equivalent to an actual eventually
periodic tail, and its lag group is the multiples of that tail's
least period. Each primitive listed cycle has precisely one carry;
all other steps are successors. Proposition 3 gives the clock in
the table, with transient prefix factors cancelling. The clock is
injective on every nontrivial source isotropy group, so the extension's
fixed-object isotropy, its kernel, is trivial everywhere.

All phases and preimages entering the same cycle share actual tails
and hence form one arrow/time packet. Distinct cycles never share
a tail. In particular C_2^a and C_2^b are distinct despite their
equal least time. The second positive repetition of C_2^a has time
2 log 2, not log 2. QED.

The union of all B_P is exactly the integer-seed locus, every root
times Z. Lemma 5 proves one inclusion. For the converse, every
inverse branch takes an integer terminal seed to an integer, so a
noninteger can never acquire an integer periodic tail. The complete
returning locus is countable, dense and mu-null. Its noninteger
complement is retained and conull; no almost-everywhere quotient
is used as the owner.

There are also noninteger seeds with periodic itineraries. At root 2
the fibre of the all-CARRY itinerary is 1+D_2, where
D_2=intersection_r 2^r K. Compatible Chinese remainder coordinates
give D_2 zero 2-adic coordinate and arbitrary other prime-power
coordinates, so it is uncountable and nonzero. Iteration sends
1+z to 1+z/2^r. A full return forces (2^r−1)z=0, hence z=0.
The entire nonzero fibre remains; it contributes no extra return.

## 5. Coarse topology and adverse controls

### Proposition 7 — the coarse extension quotient is not T1

Fix a prime p>=3 and u in R. Every integer seed at root p eventually
enters C_p, so it has a T-tail arrow to that cycle. All such arrows
have clock in (log p)Z, since only successor and p-carry occur.
Composing with cycle isotropy cancels that clock. Thus one extension
orbit contains every (p,k,u), k in Z. Integers are dense in K, but
any noninteger limit (p,x,u) is outside that orbit by Theorem 6.
The extension orbit is not closed. The preimage of its singleton
in the coarse quotient is therefore not closed; the quotient is
not T1. This proves no claim about embeddings of individual circles.

**Haar/source control.** Additive homogeneity conditionally fixes
the measure by Lemma 1, but the source translations are not claimed
T symmetries. At (2,1), applying translation by 1 before T gives
(2,3), while applying it after T gives (2,2). Nor are arbitrary
source translations adjoined as arrows: the distinct cycles at 2
are already a counterexample to that expansion. Full architecture
naturalness is OPEN, not resolved by conditional Haar uniqueness.

**SOURCE-OFF.** Replacing GCD by SUCCESSOR keeps the entire arithmetic
source and the same branch-measure recipe. The full-period equation
still forces integer seeds. Lemma 5 now gives one cycle and one
least-log-n packet for every n>=3, plus both packets at 2. In
particular the 4-packet is distinct from every repetition of a
2-packet: different root labels never share a future in this control.
GCD feedback does remove composite primitives in the main object,
but does not remove its duplicate prime-two packet.

**PREDICATE / PROVES_TOO_MUCH.** Keep CARRY; at residue 1 of a root
n>=3 outside A reset to (2,x); make all other non-carry branches
SUCCESSOR. Root 2 remains unchanged. Constant-root periodic words
still force integer seeds. For an accepted root n>=3 its cycle is
{1,...,n−1}; an excluded root's integer trajectories eventually hit
residue 1 and reset, so no such cycle survives. The full ledger is
one log-n packet for every n in A with n>=3 and the same TWO log-2
packets. All integer seeds eventually reach these cycles; nonintegers
cannot become integer because inverse reset preserves the seed.
This is a distinct theoretical encoding control, not input to SGC01;
noncomputable A supplies no claimed finite algorithm. It preserves
both the naturalness gap and the decisive multiplicity defect.

**Lag/ownership controls.** The two prime-two cycles have different
least algorithmic lags and equal least physical groupoid time. A
unit-step count is not this clock. Onto does not mean invertible:
(2,3) has both (2,2) and (2,5) as preimages. No classical unit-roof
suspension is supplied for T. Keeping the lag, all branch domains
and all states is necessary; selecting a cycle or adjoining affine
arrows changes the candidate and is not a repair of this result.

## 6. Decision, gates and reproducibility

| Gate | Evidence for this candidate | State |
| --- | --- | --- |
| T0 | Full arithmetic source, onto local homeomorphism, all arrows and complete time | ESTABLISHED; no seed deletion or itinerary quotient |
| T1 | Actual successor/carry/gcd feedback and Borel image clock | SCOPED SOURCE/INDEX RESULT; architecture naturalness OPEN |
| T2 | Theorem 6 classifies every packet and repeat | PRIME-SINGLE-PACKET TARGET FAILS: two least-log-2 primitives |
| Coarse topology | Proposition 7 | NOT T1; no classical-circle claim |
| T3 | No analytic owner provided | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 and formal Route | No classical symplectic suspension or evaluation | NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED |

Portfolio: **stop target promotion / fork the source search**. Retain
the owned arithmetic feedback and clock as a scoped result, but do
not call this a prime-single-packet construction. No special-case
change at 2, seed deletion, retiming or T3 rescue follows the stop.
The same-object ledger remains intact. 278 and all older candidates
remain unchanged; 241/242 stay paused and the programme goal active.

Exact inputs are the three frozen rules, all integers/congruences,
rootwise Haar, retained-lag groupoid and image-time convention.
The reproducible method is residue division, Borel image scaling,
affine word composition and integer descent. There is no numerical
cutoff, precision setting, prime table, zero data or empirical
extrapolation. AI assistance and three-checkpoint native review
are disclosed; neither is external peer review or formal verification.

- [Frozen candidate and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and document checks](evidence/README.md)
- [Architecture admission and two non-admitted lanes](evidence/scout-record.md)
- [Raw-card, comparison and adverse review](evidence/independent-review.md)
