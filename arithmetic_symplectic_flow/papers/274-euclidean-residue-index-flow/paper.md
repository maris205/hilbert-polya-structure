# Euclidean residue feedback: full integer returns on a null stratum

**Paper ID:** `274-euclidean-residue-index-flow`  
**Candidate ID:** `ANG-20260919-ERI01`  
**Date:** 2026-09-19.  
**Status:** `OWNED RESIDUE CLOCK; ALL-INTEGER NULL-STRATUM PACKETS — STOP / FORK`.  
**Type:** exact bounded source, measure and first-return screen.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The complete residue graph has one vertex for each positive integer n
and one marked edge n -> gcd(n,j) for every residue 0<=j<n. Uniform
rooted cylinder measures produce a continuous prefix-image clock on
its full path groupoid. Every path eventually repeats the zero-mark
edge at some divisor d of its initial root. This yields exactly one
primitive packet of least time log d for EVERY integer d>=2, not only
primes. In particular the log 4 packet is not a repeat of the log 2
packet. The full-support measure is purely atomic but assigns zero
mass to every returning path; its conull unit-tail stratum has no
positive time returns. This is not a contradiction of the earlier
every-point positive-atom obstruction. The full-state prime target
fails, and no measure restriction, branch deletion or analytic rescue
is performed.

## 1. Question, frozen owner and lineage

The [version-1 card](candidate-card.md) fixes all vertices n>=1 and
all distinct marked edges e=(n,j), 0<=j<n, with target gcd(n,j),
including gcd(n,0)=n. X_n contains ALL infinite paths from n; X is
their countable topological coproduct. The left shift sigma deletes
the first edge. For each finite prefix alpha define

    D_alpha=product of the source integers along alpha,
    mu([alpha])=1/D_alpha,          mu(X_n)=1.

The full groupoid consists of triples (xi,m−k,eta) with equal forward
tails sigma^m xi=sigma^k eta. The arrow direction is eta to xi;
integer lag is retained. Prefix replacements beta zeta -> alpha zeta
are allowed whenever the two prefixes end at the same vertex. Time
will be the real extension by minus the log IMAGE Jacobian.

| Field | This candidate's definition / boundary |
| --- | --- |
| Arithmetic source | Complete current residue choices and Euclidean gcd update |
| State space | All rooted infinite marked paths, including degree-one/unit paths |
| Source evolution | n changes to gcd(n,j); no invariant external root label is retained after shift |
| Measure | Uniform rooted cylinder rule above; its atomic structure is a result, not an assumption |
| Clock | Actual continuous Borel prefix-image cocycle, Section 3 |
| Packets | Actual time orbits of extension isomorphism classes; equal length does not merge packets |
| Classical symplectic, mapping-torus and Hamiltonian fields | NOT APPLICABLE / NOT SUPPLIED |
| Operator, trace, zeta, determinant and quantum fields | NOT SUPPLIED; no T3 pursuit after stop |

The [lineage](../../docs/prior_work/README.md) is current prime/composite
divisibility observables -> complete residue-word choices -> Euclidean
feedback -> measured groupoid replacement. This is not a Logistic or
Hénon conjugacy. A prime table, prime predicate, per-prime parameter,
zero data or prescribed log-prime roof is not an input. The graph and
uniform branch rule are still designed choices; naturalness is OPEN.

The question is whether this complete residue mechanism gives prime
primitives, rather than merely logarithmic time for every integer.
This is a bounded mechanism screen, not an admission as a promising
main architecture. It is distinct from 273's factor-sum feedback on
integer pairs and 225's reversible geometric word/port owner.

## 2. All paths and the exact measure boundary

### Proposition 1 — full source and eventual terminal integer

X is countable, locally compact Hausdorff, zero-dimensional and second
countable; each X_n is compact metrizable. Sigma is an ONTO local
homeomorphism. Every path is eventually the constant zero-mark path
at a uniquely determined integer d dividing its initial vertex.

**Proof.** Along any path the next integer divides the current one.
For 0<=j<n, gcd(n,j)=n if and only if j=0. Every nonzero mark
therefore strictly decreases the positive integer; there can be only
finitely many such decreases. After the last one all marks are zero
and the vertex is a constant divisor d. Finite prefixes over a
countable edge alphabet form a countable set; every path is a finite
prefix followed by one of the countably many constant tails. Hence
X is countable without discarding any infinite path.

Each vertex has a finite nonempty outgoing set. The finite-prefix
inverse limit at a root is nonempty compact metrizable, with clopen
cylinders. Countably many roots give the asserted coproduct topology
and compact-open countable basis. Deleting the first edge on [e]
is a homeomorphism onto the full target root space, inverse to
prefixing e. Finally the edge (n,0) can be prefixed to every path
starting at n, so sigma is onto. It is not a globally invertible
map: distinct allowed prefixes can have the same image. ∎

Write d(xi) for that terminal integer and A={xi:d(xi)=1}.

### Proposition 2 — purely atomic full support, with null periodic tails

The cylinder rule defines a sigma-finite locally finite Radon measure
mu of full support. Its positive-mass points are exactly A, and
mu(X\A)=0. Every point with d(xi)>=2 has mass zero. Thus the
measure is purely atomic, but NOT positive at every state of X.

**Proof.** The n equal child weights sum to each parent weight. This
defines compatible finite-prefix probabilities and a unique Borel
probability on each compact X_n. Sum over all roots. Every cylinder
has positive mass, giving full support. Root mass one gives local
finiteness and sigma-finiteness. Compact sets meet only finitely many
open root components; componentwise compact-metric regularity gives
the Radon property.

If a prefix alpha reaches 1, its only continuation repeats (1,0).
Its cylinder is the singleton xi, so mu({xi})=1/D_alpha>0.
If xi has terminal d>=2, a prefix alpha followed by r of its final
zero edges has measure D_alpha^(-1)d^(-r), tending to zero.
Continuity from above gives mu({xi})=0. By Proposition 1, X\A is
countable, so its measure is zero. The positive-mass set A is conull
and supports the entire measure. It is also dense: any prefix ending
at n>1 can be extended by j=1 to vertex 1. None of this removes the
null complement from X. ∎

Thus branching, full support and a countable state space do not
justify either a non-atomic measure or positive mass at every state.
The latter is the explicit hypothesis of
[272's atomic control](../272-power-divisibility-index-clock/paper.md).
It is unavailable on this entire X, but will hold on A.

## 3. Complete groupoid and image-derived time

### Proposition 3 — topology and continuous clock on all states

The full prefix groupoid G is locally compact Hausdorff, second
countable and étale. On theta:beta zeta -> alpha zeta, its Borel
image derivative and continuous clock are

    J_theta=D_beta/D_alpha,
    c(xi,m−k,eta)=log D_m(xi)−log D_k(eta).

These formulas include every null path. The cocycle extension on
X×R and its real translation time are complete and continuous.

**Proof.** The sets

    Z(alpha,beta)={(alpha zeta, |alpha|−|beta|, beta zeta)}

with common terminal vertex v have tail parameter X_v. They form
compact-open bisections. At an intersection, equal lags mean that
the longer prefix pair simultaneously appends the same word to both
members of the shorter pair. These refinements form the intersection
basis. Inversion exchanges prefixes; aligning middle prefixes makes
composition another prefix replacement. Distinct triples are separated
by their lag, source or range cylinders. This proves Hausdorffness,
local compactness and the topological groupoid laws; the countable
bisection basis and local source/range homeomorphisms give the rest.

For any Borel B in X_v, cylinder consistency and uniqueness of finite
measures give mu(alpha B)=mu_v(B)/D_alpha. Applying this identity
to alpha and beta proves the image ratio for every Borel subset of
the branch domain. Its negative logarithm gives the displayed c.
Two representations of a triple have the same change in both forward
lengths; the extra factors lie on a common tail and cancel. Aligning
the middle tail also proves additivity under composition. On a
prefix bisection c is constant, hence continuous. Full support on
its source cylinder makes this continuous version unique: continuous
versions agreeing almost everywhere cannot differ on a nonempty open
set. Null periodic values are not assigned independently.

An extension arrow (g,u) goes from (eta,u) to (xi,u+c(g)). On
G×R its bisection charts have source/range local homeomorphisms,
so the extension is locally compact Hausdorff and étale. Translation
u->u+t is a jointly continuous automorphism for every real t, with
inverse translation by −t. There is no added roof or finite-time
termination. ∎

The graph/local-homeomorphism terminology is standard; see
[Aidan Sims, Hausdorff étale groupoids and their C*-algebras, Examples 2.4.6–2.4.7](https://www.aidansims.com/papers/Sims2017.pdf).
That source's graph source/range names use the opposite convention.
The outward-path formulas above fix ours explicitly. No operator
theorem or graph-specific arithmetic conclusion is imported.

## 4. Complete first-return classification and the composite stop

### Proposition 4 — one cyclic packet per integer d>=2

Every path has base isotropy lags Z. If d=d(xi), its time-return
group is H_xi=(log d)Z. For d>=2 there is exactly one primitive
packet with that terminal integer, of least time log d and repetition
times r log d. For d=1 there is one noncyclic real time orbit, with
H_xi={0}. Extension fixed-object isotropy is trivial for d>=2 and
is Z for d=1.

**Proof.** After a prefix of length N, xi repeats the single marked
edge (d,0). Every integer lag occurs in isotropy. Its positive lag-one
arrow has representation (N+1,N), hence clock

    log D_(N+1)(xi)−log D_N(xi)=log d.

Additivity gives l log d on lag l. This determines H and its least
positive generator for d>=2. For d=1 every such value is zero.
Fixed-object extension isotropy consists of the lags with c=0,
proving the two isotropy statements. Zero clock on base loops does
not make the real time action stationary: on this d=1 time orbit
only time zero returns to the same extension isomorphism class.

Two paths have equal shifted tails if and only if their terminal
integers coincide. Each finite transient is connected by an actual
groupoid arrow to the appropriate constant tail. Time translation
aligns the remaining real coordinate. Consequently there is one
time packet for each d>=2 and one noncyclic time orbit for d=1.
Different d cannot be connected by any such arrow. These are
abstract homogeneous R-sets R/((log d)Z) or R; no embedded-circle
or Hausdorff coarse-topology theorem is asserted. ∎

The fixed controls now decide the target without a cycle search:

| Terminal tail | Full minimal time | Distinction |
| --- | --- | --- |
| d=1, edge (1,0) | No positive time return | Base and extension isotropy Z do not supply positive clock |
| d=p prime | log p, one packet | Local prime part works, without excluding composites |
| d=4 | log 4=2 log 2, one NEW primitive | Not the second traversal of d=2: shifted tails never agree |
| d=6 | log 6, one NEW primitive | Not any prime packet or traversal of one |

There are arrows in the underlying INTEGER GRAPH that decrease 4 to
2, but that does not connect the constant 4 PATH to the constant 2
PATH in G. A prefix (4,2) attached to the constant 2 tail is another
path, already in the d=2 packet. Replacing the future of the constant
4 path is not a prefix-replacement arrow. This ownership distinction
prevents merging packets by divisibility of their terminal labels.

The prime-only target already fails at d=4. All-integer completeness
here is a direct consequence of the precommitted monotone-source
check, not an expanded numerical or combinatorial census after stop.

## 5. Full-state versus almost-everywhere evidence

Every positive-return path is in the null complement X\A. On A,
let L(xi)=−log mu({xi}), a finite value given by the finite prefix
product to the unit. Image measures on singletons give exactly

    c(xi,l,eta)=L(xi)−L(eta)             for arrows within A.

All such time stabilizers vanish, as Proposition 4 already proves.
Thus the conull atomic restriction has a pointwise endpoint potential,
while the FULL groupoid has no everywhere-defined endpoint potential:
the constant d=2 isotropy has c=log 2!=0, and any endpoint difference
vanishes on a same-point arrow. Both statements can hold because the
every-state positive-atom hypothesis fails precisely on the retained
return stratum. There is no claim of an ergodic-type classification.

Restricting to A would change the frozen full-state owner and lose
every positive-return packet. Conversely, treating full support as
if every periodic singleton had positive mass is false. Neither
shortcut is used to promote or eliminate the actual full ledger.

## 6. Gates, decision and scope

| Gate / control | Result | Boundary |
| --- | --- | --- |
| T0 | Full groupoid, measure and complete real time established | Nonclassical owner; coarse flow geometry not established |
| T1 | Current gcd feedback and image-derived logarithmic clock | Entire residue rule and uniform probabilities are designed; naturalness OPEN |
| T2 | Exactly one primitive per integer d>=2, with correct repetitions | Prime-only target FAILS; prime powers remain new primitives |
| T3 | NOT SUPPLIED / NOT PURSUED | No operator, trace, product, determinant or correction |
| Unit / atom control | Conull dense positive-atom class, no positive time return | Not the whole topological source |
| Composite / equal-length control | d=4 is primitive despite time collision with d=2 repeat | Packet equality requires actual arrows, not label factorization |
| PROVES_TOO_MUCH | Complete residue degree supplies log d for every d | Logarithmic clock alone is not prime selectivity |

Portfolio: **stop target promotion / fork**. Retain the bounded source,
clock and measure-boundary results; this was not a promising-main-owner
admission. The same-object ledger stayed intact. No edge, zero residue,
unit, null path, lag or packet was removed. Classical A0/A1/A2 NOT
APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.
241/242 remain paused and the programme goal stays active.

Next proposals need arithmetic admissibility that distinguishes
composite primitive returns in the full action. Relabelling an integer
as a factor product, or using only a conull nonreturning stratum, does
not supply that mechanism. This screen is not a no-go theorem for
Euclidean arithmetic or all countable/measured groupoid clocks.

## 7. Evidence, reproducibility and disclosure

The exact inputs are the frozen graph, all paths, uniform root masses,
image convention and time/packet definitions. Methods are integer
descent, compatible cylinder probabilities, prefix bisections, Borel
measure uniqueness and exact lag clocks. There was no numerical run,
approximation, cutoff, fit or period enumeration. The controls 1,
prime, 4 and 6 were declared in the card before their audit.

See [claim scopes](claim-ledger.md), [evidence and source provenance](evidence/README.md),
[bounded scouting](evidence/scout-record.md) and the
[separate internal review](evidence/independent-review.md).
AI-assisted research and native same-family/shared-context model
review were used; this is not external peer review or formal proof
verification. No old candidate, external source, PDF, LaTeX or
publication artifact was changed.
