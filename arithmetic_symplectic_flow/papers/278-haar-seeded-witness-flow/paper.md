# Haar-seeded witness dynamics: actual arithmetic returns versus periodic itineraries

**Paper ID:** `278-haar-seeded-witness-flow`  
**Candidate ID:** `ANG-20260919-HWS01`  
**Date:** 2026-09-19; exact construction and adverse controls.  
**Status:** `OWNED HAAR-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.  
**Route state:** broadened owner-level T0–T2 only; formal `UNASSIGNED`; B `NOT INVOKED`.

## Abstract

We replace independent graph paths by a deterministic arithmetic source:
every hub consumes the current residue of a full profinite integer seed,
divides off that residue, and passes the remaining seed to its successor.
The whole source is retained. Normalized additive Haar measure determines
the finite residue probabilities and yields a continuous image-index
clock for the full local-homeomorphism groupoid. Its complete cyclic-return
ledger has exactly one packet per prime p, least time log p and repeats
r log p. This is not inferred from symbolic periodicity: an entire
uncountable seed fibre follows each prime periodic itinerary, but only
its zero seed actually returns. The extra additive source condition
excludes the earlier nonuniform branch law, conditionally; it neither
makes translations commute with the dynamics nor proves naturalness
of the scan architecture. Generic-predicate controls remain effective.
No classical geometric lift, coarse-circle embedding, T3 or formal Route
claim is made.

## 1. Frozen identity, provenance and question

The [version-1 card](candidate-card.md) freezes the entire tuple before
this proof. The [prior-work lineage](../../docs/prior_work/README.md) is
prime/composite congruence observables -> compatible residue source ->
residue extraction/division -> witnessed update of the next source
modulus -> full arithmetic groupoid. It is a broadened realization of
these arrows, not a proved Logistic/Hénon conjugacy or symplectic lift.

| Item | HWS01 owner and boundary |
| --- | --- |
| Source | Y is the countable coproduct of full K=Z_hat fibres over all graph vertices |
| Update | Deterministic T reads the actual seed residue, divides it off at hubs, and executes scan/escape rules |
| Measure | Normalized additive Haar h on each root K; total measure mu is their sum |
| Arrows | ALL retained-lag T-tail arrows, not all rational-affine maps and not a quotient by itinerary |
| Clock/time | Negative logarithm of the same measure's Borel IMAGE derivative; full real extension |
| Packets | Actual full-state isotropy images and arrow/time equivalence, with all seeds kept |
| Classical/later fields | (M,omega,F,tau), mapping torus and classical A0/A1/A2 N/A; analytic, contact and quantum owners NOT SUPPLIED |

[276](../276-witness-scan-index-flow/candidate-card.md) owns graph paths,
not this larger arithmetic source. [277](../277-symmetry-clock-admission-screen/candidate-card.md)
showed that graph automorphisms alone do not force its uniform weights.
HWS01 adds an explicitly declared compact additive source and its Haar
condition; it does not retroactively infer that structure from 276.
[270](../270-profinite-index-return/candidate-card.md) and
[275](../275-rational-affine-residue-flow/candidate-card.md) retain full
rational scaling or affine arrows on a different owner. None supplies
HWS01's clock, stabilizers or packet theorem. No novelty claim is made
for Haar measure or local-homeomorphism groupoids.

## 2. Source arithmetic and conditional Haar normalization

Let K=lim_inverse Z/mZ over divisibility of all positive moduli. It is
a compact metrizable additive group with its full residue topology.
Integers embed diagonally; a residue class modulo any m is represented
by an integer, so the embedded integers are dense. Write mK for the
image of multiplication by m.

### Lemma 1 — division and finite residue measure

For every integer n>0, multiplication by n is injective on K, and
nK is precisely the kernel of reduction modulo n. Each coset j+nK
is compact open. For its unique representative 0<=j<n, every seed
x in this coset has a unique y in K with x=j+ny. For any Borel B,

    h(j+nB)=h(B)/n.

Normalized translation-invariant probability on the declared additive
group K is unique, has h(j+mK)=1/m, is full-support and non-atomic.

**Proof.** If nx=0, reduce modulo nm for arbitrary m. The equation
n x_(nm)=0 mod nm forces x_(nm)=0 mod m, so every x_m=0. This proves
injectivity. Conversely, if x=0 mod n, define y_m by dividing its
residue modulo nm by n, modulo m. These residues are compatible and
give ny=x. Multiplication is a continuous bijection from compact K
to nK, hence a homeomorphism. Translation handles each other coset.
This argument does NOT assume K is an integral domain.

Translation invariance makes the m residue cosets equiprobable, so
normalization gives 1/m. The compatible finite uniform laws construct
the Borel probability, and the residue cylinders generate the Borel
sigma-algebra, proving uniqueness. For a cylinder B=t+mK, its image
is j+nt+nmK, of mass 1/(nm). Uniqueness of finite measures extends
the displayed scaling identity to all Borel B. Cylinders have positive
mass, whereas h({x})<=1/m for every m; this proves the last assertions.
QED.

Thus the WEIGHT demand that the zero-residue branch at n=3 have mass
1/2 is incompatible with normalized additive translation invariance
on this root. This is a CONDITIONAL uniqueness statement: choosing
K, its additive homogeneity and root masses one is additional structure.
It does not establish natural A0 for the full source/update/time tuple.

## 3. Full deterministic update and inverse branches

Vertices are H_n (n>=2), S_(n,d) (n>=3, 2<=d<=n−1), E_k (k>=0).
At (H_n,x), extract j=x mod n in {0,...,n−1} and put y=(x−j)/n.
Port j=0 sends the state to (S_(n,2),y) for n>=3, and to (H_2,y)
for n=2. If j>=1, the target is (H_gcd(n,j),y) for gcd>=2 and
(E_0,y) otherwise. Scan steps keep the seed: S_(n,d) goes to H_d
if d|n; otherwise to S_(n,d+1) until the final test, then to H_n.
Escape steps send (E_k,x) to (E_(k+1),x).

This defines T on every state, with every late scan root retained.
The seed is not a table of prime answers: its current residue is
actually consumed, and changing the hub changes which residue is
consumed next. The finite-observable interface is exactly

    y=t mod m  iff  x=j+nt mod nm

on branch j at H_n. Scan/escape steps leave all seed residues unchanged.

### Proposition 2 — full topology and local inverses

Y is locally compact Hausdorff and second countable, but not compact.
The rootwise measure mu is Radon, sigma-finite, full-support and
non-atomic. T is a local homeomorphism but not onto. For every finite
admissible branch word alpha from root v to root w, the inverse of
that branch of T^(|alpha|) is

    theta_alpha: {w}×K -> {v}×(b_alpha+D_alpha K),
    theta_alpha(t)=b_alpha+D_alpha t,
    D_alpha=product of the consumed hub moduli,   0<=b_alpha<D_alpha.

Here roots in the formula are understood and empty words have D=1,b=0.
For every Borel terminal set B, mu(theta_alpha B)=h(B)/D_alpha.

**Proof.** Each root is a compact open copy of K; infinitely many
disjoint roots give the stated coproduct properties. Every compact
subset meets only finitely many roots, proving local finiteness of
mu; the remaining measure assertions follow from Lemma 1. At a
hub the clopen j+nK branch maps homeomorphically onto its entire
target K by division. At a deterministic step the seed map is the
identity. Thus T is locally homeomorphic. S_(6,3) has no incoming
graph edge because S_(6,2) exits to H_2, so its whole nonempty fibre
has no preimage. No state is removed to make T onto.

An inverse hub branch is t->j+nt, and a deterministic inverse branch
preserves t. Compose these formulas along alpha. If a following
word beta is appended, b_(alpha beta)=b_alpha+D_alpha b_beta and
D_(alpha beta)=D_alpha D_beta. The bounds on b and Borel scaling
follow by induction and Lemma 1. QED.

The source translations A_a(v,x)=(v,x+a) are NOT asserted to commute
with T. For example, at (H_2,0), T A_1 reaches E_0 whereas A_1 T
stays at H_2. Haar source homogeneity is not dynamical equivariance.

## 4. Entire arithmetic groupoid and derived index time

Freeze G_T={(z,m−k,w):T^m z=T^k w}, with source w and target z.
For inverse words alpha,beta ending at the same root and an arbitrary
clopen residue set C in that terminal K, use the bisection

    B(alpha,beta;C) = {(theta_alpha(t), |alpha|−|beta|,
                       theta_beta(t)): t in C}.

Taking C=K alone would not give the full topology: different seeds
may have the same complete itinerary. Arbitrary terminal residue
cylinders, including empty-word unit bisections, are retained.

### Proposition 3 — full-owner clock

G_T is a second-countable locally compact Hausdorff étale groupoid.
On each displayed bisection, its Borel IMAGE derivative and clock are

    J = D_beta/D_alpha,       c = log D_alpha−log D_beta.

They are presentation-independent, continuous, and satisfy the
multiplicative/additive composition laws on ALL arrows.

**Proof.** The bisection's source and range are homeomorphic to C.
Its restrictions by finer residue cylinders form a countable basis.
Common refinements of presentations follow the same finite T-branch
from their shared terminal state, locally restricting to that branch's
clopen domain. Both inverse words then acquire the same continuation.
This proves the bisection intersection, inverse and composition laws.
It also proves local compactness and the étale property. Endpoint
coordinates and the discrete lag separate different arrows, giving
Hausdorffness. These constructions use the full arithmetic topology.

Proposition 2 gives source mass h(B)/D_beta and image mass
h(B)/D_alpha for every Borel B subset C; their ratio proves J.
For another representation of the SAME arrow, both deletion lengths
change by the same integer. Extending the shorter representation
along the common terminal branch multiplies both D's by the same
factor, so their ratio is unchanged. Matched-prefix composition
makes the ratios multiply. They are constant on each bisection and
hence continuous. Full support makes this continuous version unique
among image-density versions, even at null points. QED.

The terminology follows the local-homeomorphism construction in
[Sims, Examples 2.3.7 and 2.4.6](https://www.aidansims.com/papers/Sims2017.pdf).
The argument here establishes its concrete branch topology and
arithmetic index directly; no graph-only state space or operator
result is imported from that source.

The real extension has arrows (g,u):(w,u)->(z,u+c(g)). Its topology
is G_T×R, and its units are Y×R. Bisections give local source/range
homeomorphisms, so it too is locally compact Hausdorff and étale.
Translation of u by any t is a complete jointly continuous action
commuting with arrows. Positive c uses the insertion-lag orientation;
the reverse branch has negative clock. Deterministic steps have clock
zero. This time is not the elapsed runtime of the forward divisor scan
and is not a positive-roof edge suspension.

## 5. Symbolic coding is a factor, not the full arithmetic state

Let pi record the successive vertices and residue-branch marks of T,
as a path in the complete graph used by 276. Deterministic steps
have their unique edge. The map pi is continuous and intertwines
T with deletion of the first edge. For a finite word alpha, its
preimage is precisely the congruence cylinder b_alpha+D_alpha K
in its initial root, with mass 1/D_alpha.

Every finite admissible word has such a nonempty cylinder. For an
infinite graph path these cylinders are nested compact sets in its
initial K, so their intersection is nonempty. Thus pi is onto.
Its pushforward measure is exactly the rooted uniform path law,
by its finite-cylinder probabilities. This identity of statistics
does NOT identify the source spaces, their topology or their returns.

### Proposition 4 — the retained nonreturning fibre of a periodic word

At H_p, for prime p, the fibre of the indefinitely repeated zero-port
scan word is

    D_p = intersection_(r>=0) p^r K.

This is an uncountable, nonzero, Haar-null subgroup. After each full
scan cycle the actual seed changes by x->x/p. No nonzero x in D_p
ever returns to the same full state, despite the periodic itinerary.

**Proof.** Staying on the word requires a zero residue at each visit
to H_p, hence divisibility by every p^r; scan steps do not change the
seed. Conversely these conditions suffice. The finite Chinese
remainder isomorphisms are compatible under reduction, so passage
to inverse limits identifies K with the product of its prime-power
coordinate groups. D_p has zero p-coordinate and all other coordinates
free. It is uncountable, since a single other prime-power coordinate
already has all infinite digit sequences. For an explicit nonzero
seed, choose residues 0 on the p-power part of each modulus and 1
on its coprime part; Chinese remaindering gives compatible residues.
Also h(D_p)<=h(p^rK)=p^(−r), hence h(D_p)=0.

A return after r complete scans would imply x/p^r=x, hence
(p^r−1)x=0. Lemma 1 forces x=0, as p^r−1 is a nonzero integer.
This uses integer-multiplication injectivity, not a false claim
that K has no zero divisors. QED.

Even an escape itinerary has a whole affine K fibre: after the
finite prefix alpha first reaches E_k, all future graph steps are
fixed, independently of the remaining seed. Its preimage is
b_alpha+D_alpha K. Thus itinerary cylinders alone cannot separate
all arithmetic states, on a positive-measure stratum as well as on
the null periodic-word stratum. No fibre is collapsed in HWS01.

## 6. Full-state periods, stabilizers and primitive packets

### Theorem 5 — exhaustive actual return classification

The periodic states of T are exactly the zero-seed states at every
phase of

    C_2: H_2 -> H_2;
    C_p: H_p -> S_(p,2) -> ... -> S_(p,p−1) -> H_p,  p>=3 prime.

Their least T-periods are ell_p=p−1. Write B_p for ALL full states
whose future reaches one of these zero-seed C_p states. Then

    z in B_p:    G_z^z has lags ell_p Z,
                  c(z,r ell_p,z)=r log p,
                  H_z=(log p)Z;
    z outside union_p B_p: G_z^z trivial and H_z={0}.

Every fixed-object isotropy group in the real extension is trivial.
There is exactly one cyclic-return time packet per prime, of least
time log p, and its rth positive repetition has time r log p.
There are no other primitive cyclic-return packets.

**Proof.** Along a graph itinerary, any nonzero hub mark either escapes
or changes n to gcd(n,j)<n. Any divisor witness also changes n to
a strictly smaller integer. Scans have finitely many steps. A path
starting late in a composite scan may miss an earlier witness and
return to H_n once, but the next zero-port full scan restarts at 2
and finds a proper divisor. Thus every infinite nonescaping graph
itinerary eventually repeats one C_p; escape indices strictly increase.
These statements apply to all T itineraries, without a selected seed.

Consequently any periodic full state must lie on one of the listed
prime scan cycles. On each complete turn its seed is divided by p,
so the actual return equation from Proposition 4 forces that seed
to zero, at every phase. Conversely zero survives every zero-residue
test and is unchanged by division, giving these periodic states.
The graph cycle visits H_p once and has distinct scan vertices,
so its least full-state period is ell_p, including p=2.

Nonzero-lag isotropy means T^m z=T^k z for m!=k, which is equivalent
to entering an actual periodic full-state tail. The classification
above shows this is precisely membership in one B_p. Its isotropy
lags are all multiples of ell_p, since these are exactly the tail's
periods. A complete C_p turn consumes one modulus p and otherwise
has deterministic steps. Proposition 3 therefore assigns log p to
the positive insertion-lag generator. Transient prefix factors cancel,
giving the displayed formula for every r in Z. The clock is injective
on each nontrivial source isotropy group; its zero kernel proves
trivial fixed-object isotropy in the extension everywhere.

All phases and finite preimages of the same zero-seed C_p have
actual T-tail arrows to each other. Combining these arrows with
real time translation gives one packet, abstractly R/(log p)Z.
Zero-seed tails for different primes never have equal full roots,
so their packets are different. Outside all B_p the time stabilizer
is zero. No nonzero seed is removed or identified with zero to obtain
this classification. QED.

Each B_p is countable: there are countably many finite branch words,
and an inverse branch takes the terminal zero seed to the single
seed b_alpha. Thus all cyclic-return states form a countable null
subset of the full non-atomic source. More strongly, all states with
a nonescaping itinerary form a null set: there are only countably
many finite prefixes followed by a prime cycle phase, and each such
fibre is an affine image of some D_p. The escaping locus is conull,
but its points are NOT positive atoms. No almost-everywhere reduction
is used to replace the full-state packet theorem.

For example (H_p,x) with a nonzero x in D_p is NOT in B_p: division
by p can never make that nonzero seed zero. Its repeating symbolic
word therefore contributes no actual time return. Conversely all
zero-seed cycle phases are included because the equation selects them,
not because a representative was chosen by hand.

The theorem gives abstract groupoid/time packets. We do not infer a
Hausdorff coarse quotient or embedded classical circles from the
Hausdorff topology of the groupoid. Those questions remain OPEN.

## 7. Controls and remaining naturalness gap

**Haar versus graph-only weights.** Lemma 1 proves uniqueness only
under the explicitly added additive-source condition and the frozen
root normalization. At n=3 it excludes zero-port mass 1/2, so the
276/277 WEIGHT comparator cannot simultaneously satisfy that condition.
It is not a claim that graph automorphisms select Haar, that T preserves
mu, or that additive translations are T-equivariant. Source translations
are also not silently added as arrows: distinct seeds at E_0 can never
have equal future full states along the unchanged escape ray.

**Arrow-set control.** The zero seed at H_p has only the lag-return
group in Theorem 5. Adding all rational-affine maps would change this
owner and its stabilizers. A locally affine inverse branch is not
permission to complete the arrows to 275's full affine action.

**SOURCE-OFF comparator.** Replace scan witnesses by false and keep
the full K source, residue consumption, Haar and groupoid conventions.
The same hub-descent argument then allows a zero-port cycle C_n at
every n>=2, and no other graph cycles. The full-state return equation
is (n^r−1)x=0, so each cycle again has only zero-seed periodic phases.
Its least lag is n−1 and least time log n, one packet per integer.
The composite 4-packet is a different packet from the 2-packet's
second traversal, despite equal time. Thus witnesses do actual work
in producing prime specificity in HWS01.

**PREDICATE / PROVES_TOO_MUCH comparator.** For any set A of integers
>=2 containing 2, use h_A(n,2)=1_(n not in A), all other scan tests
false, with the same full arithmetic seed and Haar prescription.
A rejected zero-port scan goes to H_2; accepted scans close at H_n.
All nonzero hub ports still descend or escape. Therefore the complete
periodic ledger is precisely the zero-seed C_n for n in A, with
one least-log-n packet per accepted n. Late scan roots add transients,
not cycles. This is a theoretical encoding control, not input to the
main object; a noncomputable A defines no claimed finite algorithm.

Thus the Haar source resolves a particular normalization ambiguity
UNDER a declared stronger structure, while leaving the source-program
design question unresolved. Neither the prime-ledger match nor Haar's
conditional uniqueness proves arithmetic necessity of the witness,
reset, escape routing, source completion or real extension. Naturalness
is OPEN, not established and not universally refuted by this audit.

There is no finite census, precision choice, parameter fit or numerical
extrapolation. Classical geometric controls are unavailable because no
classical lift is supplied. No extra analytic object is used to rescue
the remaining naturalness gap.

## 8. Gates, decision and reproducibility

| Gate | Evidence for this exact candidate | Scoped state |
| --- | --- | --- |
| T0 | Full arithmetic T, topology, measure, lag groupoid and complete real extension | ESTABLISHED; no state or seed fibre deleted |
| T1 | Actual residue consumption/divisibility feedback; image clock; conditional Haar uniqueness | SCOPED SOURCE/INDEX ADVANCE; naturalness OPEN |
| T2 | Full-state periodic equation and exhaustive isotropy/packet classification | ESTABLISHED for abstract groupoid/time packets; no classical-circle assertion |
| T3 | No trace, zeta, determinant or operator supplied | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension | NOT APPLICABLE; no natural-A0 promotion |
| Formal Route A / B | No evaluation | UNASSIGNED / NOT INVOKED |

Portfolio: **advance the full arithmetic-source/clock/packet construction;
stop natural-A0 promotion; fork for the remaining source-architecture
justification**. This is a substantive change of source relative to
276, not a reinterpretation of its path measure. Any new action,
measure, quotient, clock or geometric lift requires a fresh card;
no retiming or T3 rescue follows this bounded audit. The original
research goal remains open and active; 241/242 remain paused.

The inputs are exactly the frozen all-moduli residue group, all graph
states, integer division/gcd/divisibility rules, rootwise Haar and
full T-tail convention. The reproducible method is compatible finite
congruences, inverse affine branch composition, strict hub descent
and the exact full-state return equation. No numerical artifact is
needed or produced. Same-object ownership remains intact throughout.
AI assistance and three-checkpoint internal model review are disclosed;
they are not external peer review or formal proof verification.

- [Candidate card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence, source check and verification](evidence/README.md)
- [Bounded architecture and collision record](evidence/scout-record.md)
- [Raw-card, manuscript and adverse review](evidence/independent-review.md)
