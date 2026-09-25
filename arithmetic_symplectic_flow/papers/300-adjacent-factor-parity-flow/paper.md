# Adjacent-factor parity exchange: an owned clock with no positive return packets

Candidate ID: `ANG-20260920-AFP01`.
Paper ID: `300-adjacent-factor-parity-flow`. Date: 2026-09-20.
Status: `OWNED PARITY IMAGE CLOCK; ALL POSITIVE RETURN PACKETS ABSENT — STOP / FORK`.
Evidence: exact all-state owner and all-period obstruction; no scientific numerics.

## Abstract

Current profinite seed parity chooses the positive or negative
adjacent factor in ac=b(b+epsilon). The full partial two-root source
owns its joint-Haar IMAGE clock and continuous complete real time.
Nevertheless it has no periodic full state at any period. A uniform
seed lemma first forces any periodic residue/shear seed to be a
constant nonnegative integer; its parity is then constant, and the
cyclic product of adjacent-factor equations is impossible. In
particular an explicit mixed-sign four-cycle of integer roots has
no full-seed periodic lift, including repeated root traversals.
All time-return groups are trivial. PARITY-OFF still has no returns;
ADJACENCY-OFF instead has n distinct primitives of least log n for
every n>=2, under its own clock. We preserve the complete owner and
stop target promotion, without retiming or downstream analytic work.

## 1. Identity, lineage and exact question

The original 158-line [card](candidate-card.md) has SHA-256

    fe1dc06ce89644078e422659e0b99cf48b45bbd97dd6ae3baa74faaa2a6553d5

For K=Z_hat with normalized additive Haar h, retain
Y=coproduct_(a,b>=1) {(a,b)} x K^2 and rootwise mu=h x h.
At z=(a,b,x,y) let j=x mod a, delta=y mod 2, epsilon=1-2delta.
The map is defined exactly when b+epsilon>0 and a|b(b+epsilon):

    c=b(b+epsilon)/a,
    T(a,b,x,y)=(b,c,y,(x-j)/a+y).

All other points are terminal objects, not deleted states.

| Same-object item | Frozen owner | Limit |
|---|---|---|
| Arithmetic source | All positive root pairs and all K^2 seeds | Current parity chooses the actual integrality domain |
| Measure | Counting roots, joint normalized Haar at each root | No invariant or uniquely natural law asserted |
| Arrows | Entire partial retained-lag tail groupoid of T | No free-word, germ or arbitrary affine enlargement |
| Clock | Negative log of this owner's Borel IMAGE derivative | Zero a=1 steps retained, no assigned positive roof |
| Primitive ledger | Entire time groups and actual tail/time equivalence | Root-only cycles do not constitute full returns |
| Classical / analytic fields | NOT APPLICABLE / NOT SUPPLIED | No symplectic map, mapping torus, trace or quantum claim |

The [prior-work](../../docs/prior_work/README.md) arrow is divisor-based
prime/composite admissibility -> the current constraint a|b(b+epsilon)
-> seed-controlled adjacent-factor exchange -> this same measured
groupoid. This is a defined source replacement, not a claimed
Logistic/Henon conjugacy or conservative dimensional lift. Naturalness
of the arithmetic rule, seed form and uniform measure remains OPEN.

Definition provenance is [299's untested proposal](../299-quotient-remainder-reciprocal-flow/evidence/scout-record.md),
SHA-256 `1b7d92d27032ec555d6afc1041bc29246089143e51abde864128470d2b647423`.
[292](../292-integral-braid-residue-flow/candidate-card.md) and
[294](../294-gcd-product-residue-flow/candidate-card.md) already use
related residue/shear and IMAGE designs; their root rules differ.
Here j controls seed consumption but not c directly, while delta
controls the factor sign and domain. [104](../104-qrt-factorization-lineage-boundary/candidate-card.md)
is only a generic QRT external control. No old theorem, clock or
Route result transfers; the arguments below establish this owner.
No prime table, primality acceptor, log-prime roof, target zeros,
Mangoldt weight or fitted parameter enters.

## 2. Full profinite source and actual partial branches

**Proposition 1.** Y is locally compact, Hausdorff and second countable;
mu is sigma-finite, locally finite, full-support and nonatomic. T
is a partial local homeomorphism on a clopen domain. The branch U
and complete image V specified in the card have the stated strict
inverse I. T is not onto, and the entire partial tail owner exists
without removing missing-image or terminal states.

*Proof.* View K as the inverse limit of all Z/NZ. Multiplication
by any integer a>=1 is injective: if ax=0, reduction modulo aN
implies x=0 modulo N, for every N. Its image is precisely aK,
the kernel of reduction modulo a. Indeed, for x=0 modulo a,
the compatible coordinates x_(aN)/a modulo N define its unique
quotient. Multiplication is a homeomorphism K->aK; aK is clopen
of index a. Each residue coset has Haar mass 1/a. K is compact
metrizable (factorial moduli suffice), with a countable clopen basis.

The countable disjoint union of compact K^2 fibres has the stated
topological properties. Rootwise Haar gives the stated measure;
compact subsets meet finitely many root fibres. Every nonempty
open cylinder has positive mass. Haar is nonatomic, since refining
residue partitions makes every cell mass arbitrarily small; the
same holds on each K^2 fibre and its countable coproduct.

The root tests are discrete and parity is clopen, so the forward
domain and its complement are clopen. On a valid U with fixed
a,b,j,delta, the proposed image is

    V={roots (b,c), u mod 2=delta, v in K},
    I(b,c,u,v)=(a,b,j+a(v-u),u).

Substitution shows I lands exactly in U and both compositions are
identities. The maps are continuous by the division result above.
Both U and V are compact open. They cover every actual forward
step and no terminal point acquires an outgoing branch.

At any target (b,c,u,v), parity fixes epsilon and hence forces
a=b(b+epsilon)/c. A preimage exists exactly when this numerator
is positive and a a positive integer; then every j=0,...,a-1
gives the displayed inverse, with no others. In particular a target
with roots (1,1) and odd u has no preimage. Its existence as a
source object is unaffected by this failure of surjectivity. QED.

The clopen-domain iterates give G_T={(z,m-k,w):T^m z=T^k w}.
Actual finite inverse-branch pairs over common open terminal domains
form its bisections. Equal-lag charts agree after extending both
counts to a common presentation. Partial composition aligns the
two middle counts to their maximum; the longer already-defined
middle itinerary supplies all needed extra steps. No iteration
past a terminal or surjectivity assumption is used. These charts
give an etale groupoid. Range, source and discrete lag separate
different triples, so it is Hausdorff; compact-open terminal
refinements give local compactness and a countable basis. Every
terminal retains its identity and all actual finite preimage arrows.

## 3. Actual joint-Haar IMAGE clock and complete time

**Proposition 2.** For every Borel E subset V, mu(I(E))=mu(E)/a.
For A_m(z)=product_(0<=i<m) a(T^i z), A_0=1, the full owner has

    J(z,m-k,w)=A_k(w)/A_m(z),
    c_G(z,m-k,w)=log A_m(z)-log A_k(w).

This is the unique continuous all-point IMAGE version, including
null seeds. Its real extension owns a jointly continuous complete
time action. A=1 steps have zero clock, not a unit-time substitute.

*Proof.* The map (u,v)->(v-u,u) is a continuous group automorphism
of K^2, with an integer inverse, hence preserves normalized Haar.
Scaling its first coordinate by a maps onto the subgroup aK x K
of index a; its pushforward normalized Haar is that subgroup's
normalized Haar. Thus its IMAGE factor relative to ambient joint
Haar is 1/a. Translation by j preserves Haar. Restricting this
composition to V proves the same factor on arbitrary Borel subsets.
The parity condition occurs in BOTH source and target; it does
not insert another factor of 1/2.

Compose these actual inverse branches and their forward inverses.
On a branch pair from w to z the factor is A_k(w)/A_m(z).
When two presentations have the same endpoints and lag, their
counts differ by a common integer. The extra product along their
equal terminal state cancels, proving pointwise independence.
Aligning middle counts as above proves multiplicativity, hence
additivity of c_G. The factor is locally constant on the charts.
Since mu has full support on every open source chart, a different
continuous density satisfying all Borel IMAGE identities cannot
differ at any point: a nonzero difference persists on an open set
of positive measure. Null seed values are therefore owned by this
continuous version, not a separate assignment to returning points.

The extension arrows (w,s)->(z,s+c_G) are homeomorphisms on the
corresponding open object charts. Translation by every real t
commutes with them and their compositions, is jointly continuous,
and has inverse translation by -t. The action is complete. If
one uses the coarse orbit set, its quotient map is open because
saturation is a union of these local homeomorphism images; real
translation therefore descends continuously. No Hausdorff coarse
quotient, embedded circle or classical suspension is inferred. QED.

## 4. A uniform seed restriction at EVERY period

**Lemma 3.** Suppose a finite positive index word a_0,...,a_(h-1)
and its canonical digits define a periodic K^2 seed trajectory
under (x,y)->(y,(x-j)/a_i+y). Then ALL its coordinates equal one
ordinary integer k with 0<=k<a_i for every i. Conversely such
constant seeds satisfy the seed equations for that index word.

*Proof.* First localize K at the positive integers to B=S^(-1)K.
The preceding injectivity embeds K in B; rational scalars act there.
Moreover Q intersect K=Z: if a reduced rational p/q belongs to K,
then p=qz in K, and reducing modulo q forces q|p in Z, so q=1.

On the fixed actual digit itinerary the seed update is affine,
with rational linear matrix and integer-digit offset

    P_a=[[0,1],[1/a,1]], offset=(0,-j/a).

Let M=P_(a_(h-1))...P_(a_0). We show det(I-M)!=0 for EVERY
positive index word, not just for small h or sampled moduli.
For h=1 the positive eigenvalue of P_a is
(1+sqrt(1+4/a))/2>1, and the other has absolute value <1.
For h>=2 the product is strictly positive entrywise. Its row sums
are both >1: already P_b P_a(1,1)=(1+1/a,1+1/a+1/b), and
each further P preserves the strict inequality in both coordinates.
For a positive 2x2 matrix the larger eigenvalue lambda_+ has a
positive eigenvector by the explicit quadratic formula; evaluating
the eigenvector equation at its smallest component gives
lambda_+>=minimum row sum>1. The other eigenvalue satisfies

    abs(lambda_-)=abs(det M)/lambda_+<1,
    abs(det M)=1/product_i a_i<=1.

Thus neither eigenvalue is 1. This is an elementary finite-matrix
argument for arbitrary length, not a spectral approximation.

The periodic equation in B^2 is (I-M)z=b for a rational vector b.
The invertible rational matrix gives a rational solution; since
z belongs to K^2, both coordinates are ordinary integers. Every
subsequent coordinate is then also an integer, and the canonical
remainder makes (x-j)/a exactly floor(x/a), even for negative x.
Writing the cyclic scalar seed sequence s_i, we have

    s_(i+2)=s_(i+1)+floor(s_i/a_i).

If two adjacent terms are nonnegative, all later terms stay so
and, from the second term onward, are nondecreasing. Periodicity
forces a constant k>=0. If two adjacent terms are negative, all
later terms remain negative and strictly decrease, impossible.
Otherwise the signs alternate between nonnegative and negative.
At a nonnegative term s_i, its next nonnegative term satisfies
s_(i+2)<=s_(i+1)+s_i<s_i, again impossible around a finite cycle.
Only the constant nonnegative case remains. Its equation is
floor(k/a_i)=0, precisely 0<=k<a_i. Direct substitution proves
the converse. QED.

This lemma does not assume zero digits, zero seeds, constant roots
or prime indices. It is limited to the EXACT displayed seed law;
it is not a theorem about arbitrary profinite arithmetic dynamics.

## 5. Root cycles do not lift: all-state nonreturn

**Theorem 4.** AFP01 has no periodic full states of ANY positive
source period. Every G_T isotropy group is trivial, every H_z={0},
and every extension fixed-object isotropy group is trivial. There
are no positive primitive cyclic-time packets anywhere in the owner.

*Proof.* Suppose a full h-periodic state existed. Lemma 3 makes
every seed coordinate the same integer k. Hence epsilon has one
constant value, +1 for even k or -1 for odd k. Writing a_i for
the cyclic first-root sequence, the root equations are

    a_i*a_(i+2)=a_(i+1)*(a_(i+1)+epsilon).

Multiplying them around the entire cycle and cancelling positive
factors gives product_i a_i=product_i(a_i+epsilon). For epsilon=+1
the right side is strictly larger. For epsilon=-1 the valid domain
requires every a_i>1, and the right side is strictly smaller.
Both contradict equality. This excludes every full source period.

If any z had equal defined iterates T^m z=T^k z with m>k,
the point T^k z would be periodic of period m-k. Thus no nonzero
lag isotropy is possible, including at preterminal or nonperiodic
points. Lag zero with identical endpoints is the identity triple.
Consequently both its clock image H_z and extension isotropy are
trivial at EVERY state. There is no least positive return time. QED.

The card's four-root diagnostic genuinely illustrates the issue.
For every n>=1 the root pairs

    (n,n) -> (n,n+1) -> (n+1,n+1) -> (n+1,n) -> (n,n)

satisfy the adjacent-factor equations with signs +,-,-,+ and
positive integer quotients. The four pairs are distinct. This is
also a realizable finite seed itinerary: start with (n(2n+1),0).
The digits are (0,0,n,n), and successive seed pairs are

    (0,2n+1), (2n+1,2n+1),
    (2n+1,2n+2), (2n+2,2n+3).

The initial seed and first three updated seeds have second-coordinate
parities 0,1,1,0, giving exactly +,-,-,+ for these four steps.
The final seed is not the initial seed. The raw reviewer supplied
this finite-path witness; root checked all four updates directly.
It strengthens the ownership control, not the nonreturn theorem.
However,
a full-state return after one or any number of these traversals
would invoke Lemma 3 and force constant parity, contradicting the
required sign changes. Not even a higher seed-period lift repairs
this projected cycle. The formal index product n^2(n+1)^2 is
therefore NOT a period or evidence of a primitive packet.

The all-period proof is decisive and stops promotion. This is an
exact obstruction for the frozen owner, not a finite-search failure.

## 6. Two controls with their OWN measured owners

### PARITY-OFF

With epsilon=+1 everywhere, the clopen domain is a|b(b+1).
The fixed-j inverse is the same formula on its full K^2 target
fibre, without a parity restriction. Its own Haar calculation gives
J=1/a, so the full cocycle follows by actual branch composition.
Periodic roots alone would require product a_i=product(a_i+1),
which is impossible. Thus this control also has no periodic full
states, no nonzero isotropy and H={0} everywhere. Main parity
feedback changes actual domains, but does not create a return ledger.

### ADJACENCY-OFF

Here domain is a|b^2 and the root rule is (a,b)->(b,b^2/a).
Again the full-K^2 inverse branches, with all j, have their OWN
IMAGE factor 1/a. A periodic root word satisfies
a_i*a_(i+2)=a_(i+1)^2; successive positive ratios
a_(i+1)/a_i are equal, and their product around the cycle is one.
Every root is therefore a single n>=1. Lemma 3 then proves that
ALL periodic full states are the fixed cores

    z_(n,k)=(n,n,k,k), n>=1, 0<=k<n.

Conversely each is fixed with j=k. At n>=2 its entire source
isotropy Z has clock image (log n)Z and zero kernel; the least
time is log n and extension fixed-object isotropy is trivial.
Different (n,k) cores have no common tail and remain different
packets even through arbitrary finite preimages. Every eventually
periodic state reaches one such core, and the same cancelled-prefix
clock gives the same time group throughout its basin. Thus there
are exactly n distinct positive primitive packets of least log n
at each n>=2. Their repetitions have times ell log n within each
packet. In particular the four log-4 primitives are not repetitions
of either log-2 primitive.

At n=1,k=0 the full source and extension isotropy are Z but H={0};
its basin has no positive cyclic-time packet. Other points are not
eventually periodic, so their source isotropy and H are trivial.
All states and this zero-clock stratum remain in the comparator.

The controls expose source selectivity and multiplicity limits, not
a newly adopted action. Main AFP01 is not replaced by either one.

## 7. Decision, gates and evidence limits

| Gate | Exact AFP01 result | Limit |
|---|---|---|
| T0 | ESTABLISHED: full partial local action and topological groupoid | All terminals and missing-image objects retained |
| T1 | ESTABLISHED: active arithmetic domain and joint-Haar IMAGE clock | Source/measure naturalness OPEN |
| T2 | ESTABLISHED: ALL time groups zero; target FAIL | No primitive positive packets at any state |
| T3 | NOT SUPPLIED / NOT PURSUED | No trace, zeta, operator or quantum rescue |
| Classical A0/A1/A2 | NOT APPLICABLE | No finite-dimensional symplectic owner |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | Broadened labels are not Route coordinates |

Portfolio: **stop target promotion / fork**. The same-object ledger
remained intact; the failure is absence of full returns, not clock
borrowing or a numerical cutoff. The full returning locus is settled
as empty for positive time. Other nonreturning orbit equivalences,
coarse Hausdorffness and stronger arithmetic naturalness remain OPEN.

The exact inputs and methods are sufficient at arbitrary period and
index, with no scientific numerical run, external-source expansion
or parameter search. See the [claim ledger](claim-ledger.md),
[evidence](evidence/README.md), [internal review](evidence/independent-review.md)
and [scout record](evidence/scout-record.md). Model-assisted proofs
and review are disclosed as inherited-model/shared-context internal
work, not external peer review or formal verification. Old packages
and mirrors remain unchanged; 241/242 paused; programme goal active.
No PDF/LaTeX, staging, commit, upload or publication occurred.
