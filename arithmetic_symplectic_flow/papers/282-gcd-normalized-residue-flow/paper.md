# Gcd-normalized residue feedback: an owned clock with only one log-two packet

**Candidate ID:** `ANG-20260920-GNR01`  
**Paper ID:** `282-gcd-normalized-residue-flow`  
**Date:** 2026-09-20; exact full-state owner and return classification.  
**Status:** `OWNED GCD-RESIDUE CLOCK; ONLY ONE LOG-TWO PACKET — STOP / FORK`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

Two evolving positive integers determine their current gcd, which
sets both a normalization and the residue extracted from a complete
profinite seed. The residue changes the next integer pair. This gives
a full arithmetic local-homeomorphism groupoid and its own Haar image
clock, without a fixed input label, scan stage or prescribed prime
roof. The exact full-seed return equation reduces every possible
periodic state to seed zero or minus one. Elementary cyclic arguments
then leave only (2,2,0), whose least time is log 2. It has no other
finite preimages, so no other state has nontrivial tail isotropy.
One actual cyclic-return packet survives, but the ordinary-prime
family does not. The full owner is retained and target promotion stops.

## 1. Frozen identity and lineage

The [version-1 card](candidate-card.md) freezes one action and its
measure/clock convention before proof. Its [prior-work interface](../../docs/prior_work/README.md)
is evolving integer divisibility -> current common-factor normalization
-> actual residue feedback into a second-order arithmetic update ->
that update's full measured groupoid. No Logistic/Hénon conjugacy or
finite-dimensional conservative realization is claimed.

Let K=Z_hat with normalized additive Haar h and its full residue
topology. The source is Y=coproduct_(a,b>=1){(a,b)}×K, with measure
mu equal to h on every root. For d=gcd(a,b) and j=x mod d in
{0,...,d−1}, define

    T(a,b,x)=(b,(a+b)/d+j,(x−j)/d).

For d=1 use j=0. Every root and every seed, including zero, minus
one and all nonintegers, remains. The arithmetic rule, Haar measure,
retained-lag arrows and real extension are the same throughout.
The two comparators in section 6 are separate owners.

Unlike [078](../078-gpf-fibonacci-a0-a1-control/candidate-card.md), this
uses no greatest-prime-factor readout. That card's withdrawn historical
cycle statement is not used. Unlike [273](../273-factor-branching-index-flow/candidate-card.md),
this is a full seed, not an independently marked path. Unlike
[278](../278-haar-seeded-witness-flow/candidate-card.md), there are no
hub/scan/escape registers. Their theorems are not dependencies here.

## 2. Full arithmetic owner and inverse branches

### Lemma 1 — division and Borel scaling

For every positive integer d, multiplication by d is injective on K,
with image the mod-d kernel. Each j+dK is compact open, and for
every Borel B subset K,

    h(j+dB)=h(B)/d.

**Proof.** Reducing dx=0 modulo dm forces x=0 modulo m for every m.
For a seed divisible by d, divide its compatible residues modulo dm
by d to obtain the compatible quotient modulo m. Compactness makes
K->dK a homeomorphism. Haar invariance gives each residue class
modulo m mass 1/m. Applying this to cylinders proves the scaling
identity there; uniqueness of finite Borel measures extends it to
all Borel subsets. Cylinders give full support, and singleton masses
are bounded by 1/m for every m, hence zero. K is not assumed to be
an integral domain. QED.

### Proposition 2 — all states retained, exact non-onto image

T is a local homeomorphism. Its image is exactly the union of roots
with second coordinate at least 2. Y is locally compact Hausdorff
and second countable; mu is non-atomic, full-support, Radon and
sigma-finite, with infinite total mass.

For a finite admissible branch word alpha, from root v to root w,
the entire inverse seed map is

    theta_alpha(t)=b_alpha+D_alpha t,
    D_alpha=product of the successive current gcd values,
    0<=b_alpha<=D_alpha−1.

It maps the terminal K onto the corresponding initial congruence
cylinder, and mu(theta_alpha B)=h(B)/D_alpha for all Borel B.

**Proof.** The (a,b,j) branch has domain {(a,b)}×(j+dK), image
{(b,(a+b)/d+j)}×K, and inverse t->j+dt. Lemma 1 proves the full
branch homeomorphism and scaling. The next second coordinate is
at least 2 because a/d,b/d>=1. Conversely, for any target (b,c),
c>=2, choose the source pair (b(c−1),b) and branch j=0. Its gcd
is b and its whole image is {(b,c)}×K. Thus roots with second
coordinate 1 remain in Y but have no preimage.

Each root is compact open, and every compact subset of the countable
coproduct meets finitely many roots. This proves the topology and
measure assertions. Composing inverse branches gives
b_(alpha beta)=b_alpha+D_alpha b_beta and
D_(alpha beta)=D_alpha D_beta. The bound and Borel identity follow
by induction, including d=1 branches. QED.

For example, T(2,2,0)=(2,2,0), whereas T(2,2,1)=(2,3,0).
The seed genuinely changes the next arithmetic root and subsequent
gcd. Source homogeneity is a declared measure condition, not a claim
that all translations commute with T or that mu is T-invariant.

## 3. Full groupoid and image clock

Let G_T={(z,m−k,w):T^m z=T^k w}, with source w, target z and
integer lag retained. If inverse words alpha,beta end at the same
root, and C is any clopen terminal residue set, use the bisection

    B(alpha,beta;C)=
      {(theta_alpha(t),|alpha|−|beta|,theta_beta(t)):t in C}.

### Proposition 3 — exact same-owner time

G_T is a second-countable locally compact Hausdorff étale groupoid.
Its continuous Borel IMAGE derivative and additive clock are

    J(g)=D_beta/D_alpha,
    c(g)=log D_alpha−log D_beta.

They hold on every arrow, including null seeds and nonzero lag
isotropy. The real extension, with arrows
(w,u)->(z,u+c(g)), has complete jointly continuous real translation.

**Proof.** Proposition 2 gives source mass h(B)/D_beta and target
mass h(B)/D_alpha for any Borel terminal B. Their ratio proves
the actual image derivative on every bisection, not merely on
an itinerary cylinder. Finite words and all terminal residue sets
give a countable compact-open basis. On intersections, extend the
shorter presentations along the actual common T tail and restrict
to its clopen branch. This supplies common refinements and proves
the inverse/composition laws. Source and range are locally
homeomorphic; endpoints and the discrete lag separate arrows.

Changing a presentation of the same arrow adds the same continuation
to both words, multiplying both D values by the same factor. The
ratio is unchanged and ratios multiply under composition. The
displayed functions are locally constant and continuous. Full
support on bisection sources makes this continuous density version
unique, so null states cannot be assigned different times.

Give the extension arrow space G_T×R its product topology. Bisections
give local source/range homeomorphisms; translation by every real
t respects the groupoid operations and is jointly continuous and
two-sided complete. QED.

The positive orientation is inverse-branch insertion. A forward
deletion has the opposite sign. Gcd-one steps have zero increment;
this is neither a positive-roof edge suspension nor elapsed runtime.
No geometric roof, prime logarithm or symbolic clock is inserted.

## 4. Exhaustive full-state periodic classification

### Lemma 4 — the coprime sector cannot return

Once gcd(a,b)=1, every later pair is coprime, the seed is unchanged,
and the sum of the pair strictly increases.

**Proof.** Here j=0 and the next pair is (b,a+b), with gcd equal
to gcd(a,b)=1. Its sum a+2b exceeds a+b. QED.

Thus every gcd on a periodic full orbit must be at least 2.

### Lemma 5 — a periodic full seed is zero or minus one

**Proof.** Compose one putative period's inverse branches. Its seed
equation is x=b+D x, where D>=2 and 0<=b<=D−1. Hence
(D−1)x=−b in K. Reduction modulo D−1 implies that D−1 divides
the ordinary integer b, so b=0 or b=D−1. Integer-multiplication
injectivity then gives x=0 or x=−1. This argument also includes
D=2; reduction modulo 1 places no extra restriction but the
same two endpoint values exhaust the bound.

For x=0 every actual digit is 0 and the seed remains 0. For
x=−1 every actual digit is d−1 and division leaves −1. These
sectors are consequences of the full return equation, not a
restriction of Y or a selection of periodic representatives. QED.

### Proposition 6 — only the state (2,2,0) is periodic

**Proof, seed zero.** Along a period write the positive integer
coordinates cyclically as a_i, and d_i=gcd(a_i,a_(i+1)). The
recurrence is d_i a_(i+2)=a_i+a_(i+1), with all d_i>=2. Summing
over one period gives

    sum_i (d_i−2)a_(i+2)=0.

Every summand is nonnegative and a_(i+2)>0, so all d_i=2.
The remaining recurrence is averaging. Its differences satisfy
a_(i+2)−a_(i+1)=−(a_(i+1)−a_i)/2. A periodic difference sequence
must therefore vanish. All a_i equal n, whose gcd with itself is
n=2. Conversely (2,2,0) is fixed.

**Proof, seed minus one.** The recurrence is

    (a,b) -> (b,(a+b)/d+d−1).

A periodic pair cannot have d=1 by Lemma 4. It cannot have a=b=n,
because its next pair would be (n,n+1), which is coprime. For an
unequal pair write its smaller and larger entries as du,dv, with
1<=u<v and d>=2. Its new entry c=u+v+d−1 satisfies

    dv−c=(d−1)(v−1)−u>=0,

with equality exactly when d=2 and v=u+1. Thus c never exceeds
the preceding maximum, except in the already excluded equal case.

Choose an occurrence of the global maximum M in a hypothetical
periodic coordinate sequence. To produce it from the preceding
unequal pair, equality is necessary: that pair must be {M−2,M}.
If the pair is (M−2,M), the output creates adjacent (M,M). If
it is (M,M−2), the next pair is (M−2,M), and one more step
creates (M,M). Both contradict exclusion of adjacent equality.
No minus-one periodic state exists. Lemma 5 exhausts all other
seeds, proving the proposition. QED.

This is an all-root, all-seed classification, not a finite cycle
census or an assertion about eventual convergence of every orbit.
Nonperiodic dynamics beyond what is needed here remain unclassified.

## 5. Full isotropy and the unique actual packet

### Theorem 7 — one log-two packet, no other returning states

Put z_star=(2,2,0). Then

    G_(z_star)^(z_star) has lags Z,
    c(z_star,r,z_star)=r log 2,
    H_(z_star)=(log 2)Z.

Every other state has trivial source isotropy and H_z={0}. Fixed-object
isotropy in the real extension is trivial everywhere. Exactly one
cyclic-return time packet exists, of least time log 2 and repetitions
r log 2. In particular every odd-prime packet is missing.

**Proof.** Nonzero-lag tail isotropy is equivalent to eventual
full-state periodicity. Proposition 6 leaves only z_star. It has
no distinct immediate preimage: a preimage must have second entry
2, so d=gcd(a,2) is 1 or 2. For d=1 the next second entry a+2
exceeds 2. For d=2 write a=2u; the required equation u+1+j=2
forces u=1,j=0, and terminal seed 0 forces input seed 0. Induction
therefore leaves no additional eventual preimages.

At z_star each turn has one inverse branch of modulus 2, so
Proposition 3 gives the stated clock and its least positive value.
Its kernel is zero; at all other states source isotropy is already
trivial. This proves the extension-isotropy assertion. All real
phases over z_star form one packet under time translation, with
precisely the displayed cyclic return group. QED.

The entire time-return locus in Y is the SINGLE Haar-null point
z_star, not a selected conull or recurrent reduction. No coarse
Hausdorffness or embedded-circle statement is inferred from this
abstract groupoid/time packet. Those topological questions are not
needed to stop prime-family promotion.

## 6. Controls and interpretation

**Diagonal prime/composite test.** For every n>=2 the integer-root
branch (n,n)->(n,n) would require j=n−2. A full fixed state would
also satisfy (n−1)x=−(n−2). For n>2, reduction modulo n−1 makes
this impossible in K. Thus a formally closing root branch, prime
or composite, is not a returning full arithmetic state. No exception
for n=2 is tuned: it is an outcome of the frozen recurrence.

**GCD-OFF.** Setting d=1 throughout yields (a,b,x)->(b,a+b,x).
Lemma 4's strict increase now holds everywhere, and each image
branch has derivative 1. This distinct control has no periodic
state, source isotropy or positive time-return packet.

**FEEDBACK-OFF.** Omit j only from the integer update, retaining
the full seed extraction. Every periodic integer pair satisfies
the zero-seed recurrence of Proposition 6, hence must be (2,2).
On that root the complete seed map is x->(x−(x mod 2))/2.
Lemma 5 leaves only 0 and −1; both are fixed. They have no common
T-tail, so this control has TWO distinct least-log-2 packets, not
two phases of one packet. No other periodic tail contributes a
new packet. This tests the specific feedback's effect without
changing the candidate after observing its result.

**Arithmetic meaning and naturalness.** Current gcd and current
residue both genuinely affect the action. The owned clock and
surviving packet are positive construction results. However, one
prime-two packet is not an endogenous ordinary-prime dictionary.
The scan-free architecture therefore does not solve the target
source/return problem. Naturalness of the chosen recurrence,
completion and extension remains OPEN. No arbitrary-predicate
encoding theorem is proved; possible PROVES_TOO_MUCH concerns are
not used as a substitute for the exact missing-prime result.

## 7. Gates, stop and reproducibility

| Gate | Same-object evidence | Scoped status |
|---|---|---|
| T0 | Full non-onto arithmetic local homeomorphism, measure, lag groupoid and complete real extension | ESTABLISHED |
| T1 | Current gcd normalization and actual seed feedback; full Haar image clock | OWNED ARITHMETIC MECHANISM; ordinary-prime family not generated; naturalness OPEN |
| T2 | Exhaustive periodic/isotropy classification; one least-log-2 packet and exact repeats | ESTABLISHED LEDGER; prime-family coverage FAIL |
| T3 | No trace, zeta, determinant or operator | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No classical symplectic base or positive-roof suspension | NOT APPLICABLE |
| Formal Route / B | No evaluation | UNASSIGNED / NOT INVOKED |

Portfolio: **STOP prime-family promotion / FORK**. Keep the full
gcd/residue owner and its one correctly timed packet as an exact
control. Do not alter the normalization, residue injection, seed
domain or clock to populate the missing primes. No T3 rescue follows.

Inputs are precisely the frozen integer gcd recurrence, complete K,
rootwise Haar, full T-tail relation and real extension. Methods are
compatible congruences, Borel scaling, inverse-branch composition,
the extremal affine return equation and elementary cyclic inequalities.
There is no scientific code, numerical precision, finite cutoff,
cycle enumeration, prime table or zero fitting. Coarse topology and
general nonperiodic asymptotics remain OPEN / NOT CLASSIFIED.

Same-object ownership is intact. ARS staged internal review and AI
assistance are disclosed; they are not external peer review, formal
verification or independent-error certification. Other packages are
unchanged, 241/242 remain paused and the programme goal stays active.

- [Frozen candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence, review bindings and document verification](evidence/README.md)
- [Admission and parallel scouting record](evidence/scout-record.md)
- [Three-checkpoint internal review](evidence/independent-review.md)
