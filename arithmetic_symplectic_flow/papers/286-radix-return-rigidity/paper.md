# Positive radix-clock packets are determined by two endpoint root graphs

Screen ID: `ASFS-SCREEN-20260920-RRR01`.
Paper ID: `286-radix-return-rigidity`. Date: 2026-09-20.
Main candidate: `NONE — SEPARATE-OWNER FAMILY SCREEN`.
Status: `EXACT ENDPOINT PACKET REDUCTION — STOP BLIND ROUTING SEARCH / FORK`.
Result type: exact architecture-class theorem and bounded admission rule.

## Abstract

Consider any fixed countable root system in which a complete profinite
integer seed supplies its standard residue modulo the current integer
index, is divided after removing that residue, and selects the next root
by an arbitrary fixed total routing function. The full tail groupoid owns
a Haar IMAGE clock. We prove that its positive cyclic-time packets are
in bijection with the index-expanding cycles of two root maps: the routes
at seed zero and seed minus one. The least packet time is the logarithm
of the product of the indices around the least root cycle. Unit-index
cycles and all other seeds remain in the owner. Thus richer nonendpoint
digit feedback alone supplies no additional positive periodic core.
This is not a universal prime-selection obstruction: the endpoint root
graphs can still contain arithmetic. It is a precise early admission
filter for further routing proposals, not a new main candidate or a
claim that the full groupoid reduces to those graphs.

## 1. Scope, prior dependency and frozen owner

The [version-1 card](candidate-card.md) was frozen before this paper's
claims, SHA-256:

    e69f918ca2b2fe13759cd85ea20ebffe6945bcd089611aaeb8a6c3ee946fd345

[282, Lemma 5](../282-gcd-normalized-residue-flow/paper.md) already gives
the elementary endpoint argument for its specific gcd-pair recurrence.
We explicitly reuse that argument, and do not claim it is new. The task
here is to prove the arbitrary-routing, full-clock, full-packet reduction,
including unit-only cycles, basins, primitive multiplicity and the prime
index-product constraint. The results apply separately to every fixed
owner; no theorems or Route credits are pooled across candidates.

Fix a nonempty countable discrete set R, integers n(r)>=1, and a total
function f(r,j) in R for every 0<=j<n(r). Put K=Z_hat, with its full
topology and normalized additive Haar h, and let Y be the coproduct of
root copies {r} x K. Give every root mass one. Define

    j = x mod n(r),   0<=j<n(r),
    T(r,x) = (f(r,j), (x-j)/n(r)).

The class excludes extra translations, additional seed coordinates,
nonstandard digit systems and arbitrary affine arrows. It includes
n(r)=1 steps, for which j=0 and the seed stays unchanged. No missing
incoming roots, nonintegers, null states or nonreturning states are removed.

The full retained-lag arrow owner is

    G={(z,m-k,w): T^m z=T^k w, m,k>=0},

from w to z. Its topology uses all finite inverse-branch pairs on clopen
terminal arithmetic subsets. On an alpha/beta branch pair the clock to
be proved is c=log D_alpha-log D_beta. Extension arrows identify
(w,u) with (z,u+c(g)); real translation in u defines time. It is not a
positive-roof mapping torus or a finite-dimensional symplectic flow.

This class abstracts the project's prime/composite residue-symbolic
source deformation. It does not make an arbitrary routing function a
lineage-admitted arithmetic candidate. Such admission would need its own
precise prior-work arrow and arithmetic-naturalness argument.

## 2. The complete measured arrow owner

**Lemma 1 (division and mixed radix).** Each branch of T is a
homeomorphism from a clopen source coset onto its entire target root.
A finite inverse prefix has seed formula

    theta_alpha(t)=b_alpha+D_alpha t,
    D_alpha=product_i n(r_i),   0<=b_alpha<=D_alpha-1.

For every Borel terminal set B, its source measure is h(B)/D_alpha.
For an empty or all-unit prefix, D=1 and b=0.

*Proof.* Multiplication by a nonzero integer a is injective on K: if
a x=0, reduction modulo |a|m for each positive integer m forces x=0
modulo m. Multiplication by n maps K homeomorphically onto nK, the
kernel of reduction modulo n. The coset j+nK therefore has inverse
t->j+nt onto the entire target root prescribed by f(r,j).

For n_0,...,n_(l-1) and digits j_i in their standard ranges,

    b = j_0+n_0 j_1+...+(n_0 ... n_(l-2))j_(l-1).

The upper bound follows by substituting j_i<=n_i-1 and telescoping;
it gives b<=D-1 even when some n_i=1. Composing inverse branches gives
the displayed formula. The subgroup nK has Haar mass 1/n, and the
transported normalized Haar on that subgroup is unique. Consequently
h(j+nB)=h(B)/n for every Borel B. Iteration proves the measure formula.
QED.

**Proposition 2 (full clock).** G has a Hausdorff, locally compact,
second-countable étale topology of actual branch pairs, with continuous
Borel IMAGE derivative and additive clock

    J(g)=D_beta/D_alpha,
    c(g)=log D_alpha-log D_beta.

These identities hold on all arrows, not just almost everywhere. The
real extension owns complete continuous real translation.

*Proof.* Each prefix-pair bisection takes beta(t) to alpha(t). Lemma 1
gives source mass h(B)/D_beta and target mass h(B)/D_alpha, proving
the IMAGE ratio for all Borel restrictions. Finite branches and clopen
terminal congruence sets give a countable compact-open basis. Intersecting
presentations of an arrow have the same retained lag; the longer pair
extends both prefixes by the same actual forward tail. Restricting its
finite branches gives a common refinement. The same refinement rule
handles composition and inverse; source and range are local homeomorphisms.
Endpoints and the integer lag separate different arrows, proving the
Hausdorff property. Surjectivity of T is not required.

Extending both prefixes multiplies both D values by the same tail
product, so their ratio is representation-independent. Ratios multiply
under composition and invert under inverse. The formulas are locally
constant on bisections. Source measure has full support on every such
bisection, so a continuous density agreeing almost everywhere cannot
differ at a null source point: a continuous difference there would
persist on a nonempty open set of positive measure.

Give extension arrows G x R the product topology, with source (w,u)
and target (z,u+c(g)). These are locally homeomorphisms. Real translation
commutes with all arrows and is jointly continuous and two-sided complete.
This does not assert Hausdorffness of its coarse orbit quotient. QED.

The chosen sign is inverse-prefix insertion. Forward deletion has the
opposite clock sign. A zero-index-clock step need not have zero discrete
lag, and a null state is not assigned a new clock version.

## 3. Endpoint rigidity, including its exact exception

Define the two root maps

    f_0(r)=f(r,0),     f_-(r)=f(r,n(r)-1).

Seeds 0 and -1 are invariant under their respective seed updates. For
-1, its standard residue is n-1 and (-1-(n-1))/n=-1, also for n=1.

**Lemma 3 (periodic seed).** If a full-state period consumes a product
D>1, its seed is exactly 0 or -1. If D=1, the period contains only unit
steps, and this conclusion does not follow: every seed in K is compatible
with the same closed unit-root word.

*Proof.* Compose the actual inverse branches around the period. The
return equation is x=b+D x with 0<=b<=D-1. If D>1, reduction of
(D-1)x=-b modulo D-1 forces the ordinary integer b to be divisible by
D-1. Thus b=0 or D-1. Injectivity of nonzero-integer multiplication on
K gives x=0 or -1 respectively. D=2 causes no gap: modulo 1 adds no
restriction, but the two endpoints already exhaust the integer bound.
If D=1, every index is one and every digit is zero. The return equation
is x=x and leaves all seeds free. QED.

The non-domain nature of K is harmless because only integer injectivity
was used. The conclusion concerns full states, not merely periodic root
words. This is the exact extension of the previously recorded 282 argument.

## 4. Uniform full-packet classification

Let C be a finite directed cycle of f_0 or f_-, counted modulo cyclic
rotation with its least root period ell_C. Keep its endpoint tag even
if the same root list appears in both graphs. Write

    D_C=product_(r visited once around C) n(r).

Call C expanding when D_C>1; this is index expansion, not a smooth
hyperbolicity assertion. Let B_C contain ALL full source states eventually
reaching the tagged endpoint cycle, including all finite preimages.

**Theorem 4 (exact positive-packet reduction).** For every separately
fixed R,n,f:

1. Positive cyclic-time packets are in bijection with the expanding
   tagged cycles of f_0 and f_-, modulo cyclic rotation.
2. Each such C owns exactly one packet. At every z in B_C, source
   isotropy has lags ell_C Z and the time-return group is

       H_z=(log D_C)Z.

   Its least positive time is log D_C and its repetitions are k log D_C.
3. Different tagged cycles remain different packets, even when their
   times are equal or integer multiples of one another.
4. Outside the union of these B_C, H_z={0}. This does not say that
   source isotropy is trivial there: unit-only cycles retain discrete
   isotropy with zero clock.

*Proof.* Nonzero-lag source isotropy means T^m z=T^k z for some m>k.
It is equivalent to eventual full-state periodicity. At a periodic
core, an isotropy generator traverses its least full period once; its
clock is the logarithm of the product of the indices on that period.

If that product exceeds one, Lemma 3 forces the seed to 0 or -1. The
seed then remains at that endpoint at every step. Consequently the
least full period is exactly the least period of its tagged root cycle,
and the clock generator is log D_C. Conversely every expanding tagged
root cycle gives an actual full-state cycle at its endpoint seed.

For any eventual preimage, conjugation by its actual finite-prefix arrow
transports isotropy from the cycle. The prefix clock and its negative
cancel. All lags are therefore ell_C Z and their clock values are
k log D_C, with every integer k actually realized. In particular this
is the least positive generator, not merely one positive return value.
The fixed-object isotropy in the real extension is trivial on B_C,
since the clock is injective on that source isotropy group.

All B_C states have actual common tails with the cycle, so form one G
orbit. Together with all real coordinates they give one time packet.
Two different periodic cycles of a function cannot have a common tail.
Nor can the two endpoint sectors meet: seed 0 remains 0 and seed -1
remains -1. Thus neither equal periods nor equal root lists merge the
distinct tagged packets.

Finally, any positive clock isotropy elsewhere would give an eventual
periodic core with an index product >1, already covered. A unit-only
core instead has product one and every isotropy clock value zero; a
non-eventually-periodic state has no nonzero-lag isotropy at all. QED.

**Corollary 5 (where the basins can lie).** Every source state with
positive clock returns has an ordinary integer seed. In a zero-endpoint
basin it is nonnegative; in a minus-one-endpoint basin it is negative.
No converse is asserted.

*Proof.* An actual finite inverse prefix to seed 0 gives b in
{0,...,D-1}; one to seed -1 gives b-D in {-D,...,-1}. These include
the empty prefix. Noninteger seeds cannot reach either endpoint.
They can still have unit-only periodic source dynamics with clock zero.
Integer-seed states can also escape forever or reach a unit-only cycle. QED.

The theorem is NOT a reduction of the full groupoid or its topology to
two discrete graphs. Nonendpoint digits still affect transients,
basins, measure, topology and individual nonclosed arrow clocks. The
claim reduces only the positive primitive packet ledger and its times.

## 5. Prime-product constraint and fixed controls

**Corollary 6.** A positive primitive packet has least time log p for
a prime p if and only if its least tagged root cycle contains exactly
one step of index p and every other step has index one.

*Proof.* By Theorem 4 its least time is log D_C. Since all indices are
positive integers, D_C=p is equivalent to exactly that factor pattern.
The logarithm is injective on positive real numbers. QED.

A least root cycle with D_C=p^a, a>1, instead has its own primitive
time a log p. It is not the a-th traversal of a different packet with
time log p: its OWN least full period generated its isotropy group.
An admissible prime-only, multiplicity-one target therefore requires
exactly one expanding tagged cycle with D_C=p per prime and no other
expanding tagged cycles. This states a necessary-and-sufficient ledger
condition within this class, not an arithmetic-naturalness proof.

Two exact precommitted controls show the boundaries without enumeration:

- One root with n=2 and both digits returning to it has two distinct
  positive packets, at seeds 0 and -1. Each has least time log 2.
  Equal times and equal root names do not identify them.
- One root with n=1 fixes every seed in K. Source isotropy is Z at
  every seed, but its clock image is {0}; there is no positive-time
  cyclic packet. This forbids upgrading source periodicity to time
  periodicity or applying the endpoint lemma when D=1.

No numerical cutoff, finite modulus sample, precision parameter or
prime table enters these results. They are all-root, all-seed arguments.

## 6. Admission consequence, scope controls and decision

The architecture test is now cheap and precise: for a routing-only
proposal of this type, first inspect f_0, f_- and n. Prove or refute its
expanding-cycle ledger THERE before investing in nonendpoint orbit
tables or claiming richer seed feedback generates new prime packets.
An unproved or merely relabelled endpoint mechanism stays OPEN.

This does not exclude arithmetic endpoint mechanisms. In particular
[278](../278-haar-seeded-witness-flow/README.md) remains a positive
fixed-object prime-packet control with its own proofs and naturalness
OPEN. Its [285 topology audit](../285-haar-seeded-packet-topology/README.md)
is unchanged. We neither borrow those results into this theorem nor
invalidate them by pretending that endpoint rigidity means no packets.

| Control / risk | Disposition |
|---|---|
| Arbitrary fixed root routing | Included uniformly; different choices remain different owners |
| Unit-index cycles | Full seed continuum retained; zero clock distinguished |
| Periodic symbolic word versus full state | Affine return equation is mandatory |
| All finite preimages | Kept via actual prefix arrows; no centre or representative selection |
| Composite product versus repetition | Distinct primitive root cycle remains primitive |
| Naturalness / PROVES_TOO_MUCH | Not resolved by freedom to program f; arbitrary predicate encoding is no achievement |
| Existing 282 endpoint lemma | Explicitly credited; no basic-lemma novelty claim |
| Successor, nonlinear, multiseed or physical-clock architectures | Outside hypotheses; no no-go transferred to them |

Portfolio: **stop blind routing-only search / fork**. Reject the claim
that nonendpoint standard-radix seed richness by itself yields a new
positive closed-orbit source. Continue with a genuinely new arithmetic
mechanism in the endpoint graphs or a freshly frozen source/action outside
this class. Do not delete the full seed space to obtain an apparent repair.

No main candidate is admitted. Main-candidate T0-T3 and A0/A1/A2
coordinates are NOT ASSIGNED; classical fields NOT APPLICABLE, formal
Route coordinates UNASSIGNED, Route B NOT INVOKED. The screen supplies
uniform owned-clock/packet facts under explicit hypotheses, not a formal
Route result. No operator, determinant, trace or T3 construction is
supplied or pursued. 241/242 remain paused; programme goal active.

## Evidence and disclosure

The [claim ledger](claim-ledger.md), [evidence](evidence/README.md) and
[internal review](evidence/independent-review.md) bind scope and versions.
The [parallel scouts](evidence/scout-record.md) remain definition-level
nonadmissions, not new no-go theorems. AI-assisted authorship followed
the ARS freeze/adverse-check workflow. Internal same-model checking
does not establish external peer review, independent errors or formal
verification. No scientific computation or external publication occurred.
