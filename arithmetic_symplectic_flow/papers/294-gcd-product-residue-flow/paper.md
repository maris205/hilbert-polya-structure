# Gcd-product residue dynamics: owned time and composite primitives

Candidate ID: `ANG-20260920-GPR01`.
Paper ID: `294-gcd-product-residue-flow`. Date: 2026-09-20.
Status: `OWNED GCD-PRODUCT CLOCK; COMPOSITE PRIMITIVES — STOP / FORK`.
Result type: exact full-source ownership and decisive primitive-packet audit.

## Abstract

We freeze a two-root arithmetic update that cancels the current gcd,
multiplies the remaining coprime factors and adds a consumed profinite
digit. The coupled two-seed action is a surjective local homeomorphism
on the complete source. Its own joint-Haar IMAGE law defines a continuous
lag-groupoid clock and complete real time action. However, every integer
n>=2 already has a zero-seed three-cycle with least time log n, and
different n give different packets. Hence n=4 contributes an independent
primitive, not the second traversal of the n=2 packet. The target fails
at the first frozen boundary test. We retain all states and the legitimate
clock, but stop prime-family promotion without classifying other seeds
or constructing an analytic object. GCD-OFF and FEEDBACK-OFF controls
separate index time from digit feedback. Strong naturalness remains OPEN.

## 1. Identity, lineage and question

The original [version-1 card](candidate-card.md) has SHA-256

    7c7371535c13100961f68fe6981af44494a13493745f87381979288e037c92cb

It freezes the definition proposed in the preceding
[breadth record](../293-active-pair-full-source-transfer/evidence/scout-record.md),
not an alteration of APR01 or its transfer owner. Put K=Z_hat and

    Y=coproduct_(a,b>=1) {(a,b)} x K²,
    mu|_(a,b)=h x h,
    g=gcd(a,b), j=x mod g in {0,...,g-1},
    T(a,b,x,y)=(b,ab/g²+j,y,(x-j)/g+y).

The lineage arrow is divisibility-symbolic observables -> current gcd
factor cancellation -> quotient-product/digit feedback -> this source's
own measured time. The gcd and residue symbols are recomputed on evolving
states. This is not a proved old-sieve conjugacy, Logistic/Hénon lift,
classical symplectic flow or prime-return mechanism merely by declaration.

| Same-object item | Frozen owner | Scope |
|---|---|---|
| Carrier, rule, measure | All Y, displayed T, uniform joint root-Haar | No prime subset, seed restriction or finite-modulus replacement |
| Arithmetic input | Positive integers, gcd, residues, fixed integer operations | No prime tables, log-prime roof, Mangoldt or zero data |
| Time | Full retained-lag groupoid, c=-log IMAGE factor, Y x R extension | No unit-time replacement at g=1 |
| Packets/repeats | Entire time stabilizer H_z and actual tail equivalence | Equal lengths do not identify different packets |
| Classical geometry and analytic owner | NOT APPLICABLE / NOT SUPPLIED | No imported symplectic, determinant or quantum object |

Nearest design ancestry is [282](../282-gcd-normalized-residue-flow/candidate-card.md),
whose normalized sum and one seed are replaced here by a product and
two coupled seeds. The gcd-consumption idea is not new. The discrete
parity action of [272](../272-power-divisibility-index-clock/candidate-card.md)
and the three-root partial law of [292](../292-integral-braid-residue-flow/candidate-card.md)
are different owners. Their theorems are not dependencies of the proofs below.

The narrow question is whether the new law's own time and full packet
convention survive the precommitted all-n zero-seed discriminator.
One composite primitive suffices to stop target promotion; success on
that test would not alone establish a complete prime ledger.

## 2. Exact local owner on the entire source

**Proposition 1.** T is a well-defined surjective local homeomorphism.
For fixed roots a,b and digit j, write g=gcd(a,b), q=ab/g².
The branch with x in j+gK maps homeomorphically onto the entire seed
fibre at root (b,q+j), with inverse

    I_(a,b,j)(xi,eta)=(a,b,j+g(eta-xi),xi).

Its Borel IMAGE factor relative to the joint root-Haar measures is 1/g.

*Proof.* Multiplication by a nonzero integer g is injective on K and
has image gK; division on that image is its continuous inverse.
Thus x-j is divisible by g in K. Both a/g and b/g are positive
integers, so q+j>=1. Substitution proves the two-sided branch formula;
its domain and image are clopen root/seed sets, covering all Y.

For completeness, inverse branches over target roots (u,v) are exactly

    g|u, a=gA, gcd(A,u/g)=1,
    j=v-A(u/g), 0<=j<g.

There are finitely many such pairs g,A. In particular g=u, A=v,
j=0 is always allowed, giving source roots (uv,u), so T is onto.
No target seed is omitted, since each inverse branch accepts all K².

The inverse seed map decomposes into the unimodular change
(xi,eta)->(eta-xi,xi), multiplication by g in its first coordinate,
and translation by (j,0). The first and last preserve additive Haar.
Multiplication identifies Haar on K with normalized Haar on the
index-g subgroup gK, whose ambient mass is 1/g. Therefore for EVERY
Borel set E in the target seed fibre,

    mu(I_(a,b,j) E)=mu(E)/g.

This is a joint two-seed calculation, not a product of marginal
Jacobian guesses. It holds for all branches, including g=1. QED.

## 3. Full lag clock and complete real time

Let G_T consist of all triples (z,m-k,w) with T^m z=T^k w,
m,k>=0. Retain lag and all actual inverse-branch refinements. Define

    D_m(z)=product_(0<=i<m) gcd(a_i,b_i), D_0=1,
    c(z,m-k,w)=log D_m(z)-log D_k(w).

**Proposition 2.** This is a presentation-independent continuous
additive cocycle. On each actual local branch-pair bisection its
Borel IMAGE factor is J=D_k(w)/D_m(z), so c=-log J. The full
cocycle extension carries a continuous complete R-action.

*Proof.* Restrict a finite itinerary to a clopen domain on which its
root/digit word is fixed. Proposition 1 composes to IMAGE factor
1/D_m for its inverse branch. Pair two such branches over their
common terminal domain: from w to z the IMAGE factor is D_k/D_m.
Every further clopen seed refinement has the same law. These domains
cover all arrows and all points, including Haar-null ones.

Two presentations with the same endpoints and lag differ by adding
the same integer to both iterate counts. Extending the shorter pair
adds equal products along the common terminal trajectory to numerator
and denominator. The ratio is unchanged. For composition, extend
presentations until their counts at the middle state agree; its
products cancel, giving additivity. Inversion changes the sign.
On each branch-pair chart the clock is constant, hence continuous.
This full-point version is derived from actual branches, not chosen
arbitrarily on an almost-everywhere exceptional set.

Extension arrows are (gamma,t):(w,t)->(z,t+c(gamma)). On every
bisection this is a homeomorphism of open subsets of Y x R. Thus
orbit saturation is open, and the orbit quotient map is open. Time
translation (z,t)->(z,t+s) commutes with every extension arrow and
descends to the quotient. The product with an open quotient map is
again a quotient map, so the descended action is jointly continuous.
It exists for every s in R, proving two-sided completeness. No
positive-roof or non-Zeno substitution is needed for this explicitly
defined R-action. QED.

The quotient's separation properties and embedded-circle topology are
not established. These are packet/time-stabilizer statements below,
not a claim that the full coarse carrier is a Hausdorff flow manifold.

## 4. The first boundary already decides the target

Let z_n=(n,n,0,0). Zero seeds have digit zero and remain zero.

**Theorem 3.** For every n>=2, z_n has least source period three,
full time stabilizer (log n)Z, and therefore a primitive time packet
of least time log n. Different n give different packets. For n=1,
the source point is fixed but its time stabilizer is {0}.

*Proof.* Direct application of the exact rule gives

    (n,n,0,0) -> (n,1,0,0) -> (1,n,0,0) -> (n,n,0,0),
    current gcds: n, 1, 1.

For n>1 the three root pairs are distinct, proving least period three.
For any m,k>=0, T^m z_n=T^k z_n holds precisely when m-k is
a multiple of three. Hence its ENTIRE lag isotropy is 3Z. The
product of current gcds over one full cycle is n, so Proposition 2
gives, for every integer r,

    c(z_n,3r,z_n)=r log n, H_(z_n)=(log n)Z.

This includes all presentations with arbitrary common extra prefixes;
there is no untested smaller positive clock from a different lag.

The zero-seed root cycles for distinct n are disjoint. Since the
forward map is deterministic, equality of any two forward tails of
cycle points would require the same cycle. Therefore no actual arrow
connects cycles for different n. Adding real time coordinates or
translating time does not create an arrow with new source endpoints.
All finite preimages of an exhibited cycle remain in its same packet;
they cannot identify it with a distinct cycle.

For n=1, z_1 is fixed with g=1 at every iterate. Source isotropy
is Z but every clock is zero, so H_(z_1)={0}. QED.

For n>=2 the cocycle is injective on 3Z, so fixed-object extension
isotropy at (z_n,t) is trivial, even though time has the stabilizer
(log n)Z. At z_1 the extension retains source isotropy Z while time
has no nonzero stabilizer. These are different notions of return.

**Decisive stop.** The n=4 packet has its OWN least time log 4.
Although log 4=2 log 2, this is not the n=2 packet traversed twice:
their actual core cycles have no common tail. More generally every
composite n>=2 supplies such an extra primitive. Thus the mechanism
produces an all-integer primitive family, not only prime primitives
and their repetitions. This disproves the intended exact prime-ledger
identification without any nonzero-seed census.

The theorem exhibits this family inside the complete retained source;
it does NOT replace the source by the family or claim that the family
exhausts all returns. Other seed cycles, packet multiplicities at a
given time, and the complete returning locus remain OPEN / NOT PURSUED.

## 5. Precommitted controls and arithmetic scope

| Control | Exact bounded result | What it distinguishes |
|---|---|---|
| All n, including composite n=4 | Distinct primitive packet of least log n for each n>=2 | A numerical prime-power time is not necessarily a repetition |
| g=1 steps and n=1 | Zero clock increments; H_(z_1)={0} | Runtime/iterate count is not physical time |
| GCD-OFF, all Y | Owned clock identically zero, no positive time stabilizer | Actual gcd index consumption supplies the nonzero time |
| FEEDBACK-OFF, all Y | Same exhibited all-n primitive family | Adding the digit does not remove this obstruction |

For GCD-OFF the separate frozen rule is

    T_off(a,b,x,y)=(b,ab,y,x+y).

Each root fibre maps homeomorphically onto (b,ab) x K²; its seed
matrix has determinant -1, so every branch IMAGE factor is one.
The full image consists exactly of roots (u,v) with u dividing v.
Every prefix and branch-pair clock is zero, hence H_z={0} for ALL
states, irrespective of their discrete periodicity. This uses the
control's own measure, not the main clock attached to a changed rule.

For FEEDBACK-OFF the separate rule is

    T_fb(a,b,x,y)=(b,ab/g²,y,(x-j)/g+y).

Fixing roots and digit again gives the exact inverse seed formula of
Proposition 1, now onto root (b,ab/g²). Each branch has IMAGE 1/g;
all digits remain in the carrier. Targets (u,v) again have a branch
from (uv,u), so the map is onto. The branch-pair construction proves
its own prefix-g clock. On zero seeds its full state evolution equals
the main three-cycle, so the proof of Theorem 3 applies to the exhibited
family with the SAME scope. No classification of its other seeds or
complete control packet ledger is asserted.

This is a concrete PROVES_TOO_MUCH failure: actual arithmetic and
owned logarithmic index time occur, but the first family accepts
composites too. It is not a theorem that arbitrary data can be encoded,
nor a no-go for all gcd-based or measured arithmetic actions. The
declared completion, measure and feedback design remain naturalness
questions; the result does not upgrade them to a strong A0 mechanism.

## 6. Gate decision and evidence boundary

| Layer | Result for THIS candidate | Limit / next decision |
|---|---|---|
| T0 | ESTABLISHED: complete source, exact local map and full groupoid owner | Coarse separation / circle embedding unaudited |
| Scoped T1 | ESTABLISHED: actual gcd/residue action and owned IMAGE clock | Prime-selectivity FAIL; strong naturalness OPEN |
| T2 | ESTABLISHED exhibited all-n family, least times and packet distinction | Composite primitive refutes target; complete ledger OPEN / NOT PURSUED |
| T3 | NOT SUPPLIED / NOT PURSUED | No analytic rescue after the decisive first test |
| Classical A0/A1/A2 | NOT APPLICABLE | This is not a symplectic mapping torus |
| Formal Route coordinates / B | UNASSIGNED / NOT INVOKED | No spectral, quantum, completed-Xi or zero claim |

Portfolio: **stop prime-family promotion / fork search**. The same-object
ledger stayed intact: no composite was deleted, no time rescaled, and
no independent primitive relabelled as a repeat. This is a rapid gate
decision, not a reason to tune this rule or finish an unnecessary orbit
classification. Any genuinely different next architecture needs its
own freeze; no old positive or negative credit transfers.

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md),
[internal review](evidence/independent-review.md) and
[breadth/provenance record](evidence/scout-record.md) distinguish proofs,
definition authorship and unresolved scope. ARS's three internal adverse
checkpoints are not external peer review, formal verification or
independent-error evidence. This is AI-assisted exact research; no
scientific numerical run or external theorem is used. Old packages and
mirrors remain unchanged; 241/242 paused; programme goal active.
