# Independent internal review — FBI01

**Candidate:** `ANG-20260919-FBI01`. **Date:** 2026-09-19.
**Reviewed status:** `OWNED NON-ATOMIC PRIME CLOCK; MIXED PRIMITIVE COLLISIONS — STOP / FORK`.
**Verdict:** PASS for the scoped exact proof and stop record.
No blocking mathematical error or required manuscript change was found.
This is not a pass of the full prime-only primitive-ledger target.

## Inputs, procedure and independence limits

| Input | SHA256 |
| --- | --- |
| Frozen version-1 card read before the manuscript | `afd7787de56c4fa3e0fb298266aef3d6fcc038ec85eb46776a29705b4f03775c` |
| Manuscript reviewed | `4ca2c45d45f5addecb4905406cf6d81a268d06ee6d65e55a7347a1eceac5419c` |

The reviewer first derived the source/measure/groupoid, clock sign,
eventual-period return rule and precommitted controls from the raw card,
and sent those findings before reading the manuscript. Checkpoint 2
is a subsequent comparison, not a claim that every stage was blind.
A bounded auxiliary model check received the graph/control definitions
but no files or manuscript, and confirmed the control algebra and
eventual-period rule after the reviewer's own derivation.

ARS academic-research-suite's deep-research devil's-advocate procedure
organized the three checkpoints. No numerical census, additional cycle
search, new owner, operator, T3 construction or formal Route evaluation
was undertaken. Hash checks bind documents, not scientific experiments.
Agents share model lineage and context: this is internal model review,
not external peer review, human certification, formal proof checking or
evidence that their errors are independent.

## Checkpoint 1 — independent raw-card derivation: PASS

**All paths and roots.** Every vertex has finite outdegree d>=2. At
each depth a rooted tree has finitely many prefixes and every prefix
extends. The finite-prefix inverse limit is nonempty compact metrizable
and zero-dimensional. The countable disjoint union of all root spaces
is locally compact Hausdorff and second countable; root spaces and
finite cylinders are compact open. No recurrent-core reduction occurs.

On each first-edge cylinder sigma is a homeomorphism onto the full
target root space. Its image is exactly the union of roots (x,p) with
p prime: necessity follows from the target formula, and sufficiency
uses predecessor (p^k−x,x), j=0, with p^k>x. Thus sigma is not onto.
This is a local-homeomorphism tail groupoid, not a global Z-action
obtained by inventing missing predecessors.

**Measure.** Equal child probabilities sum to their parent probability,
giving a unique rooted Borel probability. Their sum over every root
has full support and is sigma-finite. A compact set meets only finitely
many open root components, so local finiteness and componentwise Radon
regularity give the claimed Radon measure. Each singleton is contained
in cylinders of mass at most 2^(-m), hence has measure zero. In particular,
periodic paths are retained null states, not positive-weight atoms.

**Groupoid owner.** Every triple has a prefix-pair neighborhood. Equal
lags force intersecting prefix pairs to differ by appending the same
word on both sides. These refinements form the intersection basis.
Inversion exchanges prefixes; matching/refining the middle prefixes
gives composition and continuity. Each bisection has tail parameter
X_v and is compact open. Different triples are separated by lag, source
or range coordinates, proving Hausdorffness. Source/range maps are local
homeomorphisms. Distinct marks and distinct lags remain distinct data.

**Image clock with the frozen orientation.** For alpha and beta ending
at v and any Borel B in X_v, the cylinder prescription extends to
mu(alpha B)=mu_v(B)/D_alpha and mu(beta B)=mu_v(B)/D_beta.
Thus the arrow beta zeta -> alpha zeta has image Jacobian
J=D_beta/D_alpha and clock c=log D_alpha−log D_beta. Prefixing an edge
has clock +log d; deletion has clock −log d. The sign agrees with
SOURCE eta and RANGE xi, rather than the reverse shorthand.

If two representations have the same lag, their length changes agree.
Enlarging the shorter pair appends a common tail segment, whose D-factor
cancels. Refinements and units obey the same rule; aligning the middle
path in a product proves additivity. The resulting c is constant on each
prefix bisection and therefore continuous and representation-independent.

Full support on every source cylinder fixes its continuous Jacobian
version even at periodic null paths: a different continuous value would
persist on a positive-measure relatively open set. This is not a ratio
of singleton weights, nor an arbitrary null-set prescription. The
positive-atom argument in 272 is inapplicable to this owner.

The real extension on G×R has local source/range homeomorphisms on
bisection charts, with the target coordinate translated by c. It is
locally compact Hausdorff and étale; physical translation is jointly
continuous, commutes with the arrows and exists for every real time.
None of these facts establishes a Hausdorff coarse space or an embedded
circle in that coarse space.

**All actual return groups.** Nonzero isotropy lag is equivalent to
eventual periodicity of the marked edge sequence. Its lag subgroup is
hZ, where h is the least eventual edge period. Past the transient,
let B be the product of d over one such minimal word. Then B>=2^h>1
and c on lag rh equals r log B. Transients cancel and rotation does
not change B. Therefore H=(log B)Z with least time log B; a path
that is not eventually periodic has H={0}. Extension fixed-object
isotropy is trivial in both cases, unlike base isotropy hZ. A shorter
period of the degree word does not shorten the marked-edge return.

**Precommitted exact controls.**

| Control | Least marked period and actual time | Ownership check |
| --- | --- | --- |
| Constant vertex | Only (p,p), j=0 for a prime p; h=1, T=log p | A self-loop forces x=y=n=gpf(2n+j), hence n prime; 0<=j<n then forces j=0. Units/composites give none. |
| (2,3), j=3; (3,2), j=1 | gpf(8)=2, gpf(6)=3; both degrees 5; h=2, T=log25 | The two distinct vertices force edge primitivity; no tail equals the constant (5,5) loop. |
| (7,3),(3,5),(5,2),(2,7), all j=0 | Degrees 5,2,7,3 from sums 10,8,7,9; h=4, T=log210 | Four distinct vertices force edge primitivity; no tail equals a constant loop or the two-cycle. |

The mixed two-cycle is a primitive packet, not a second traversal of
the prime-5 packet, despite equal times at log25. The four-cycle has
time log210, which is not r log p for any prime p and positive integer r.
The first mixed control already triggers the frozen stop; checking the
second predeclared word is not an expanded cycle census.

## Checkpoint 2 — manuscript comparison and exact added corollaries: PASS

Propositions 1–4 and both mixed controls agree with the raw derivations.
The manuscript preserves all roots, parallel marks, transient prefixes,
inverse arrows and isotropy lags; it does not confuse source observables
with invariants or a local homeomorphism with an onto shift.

The stated packet bijection was checked at manuscript comparison:
every eventual periodic path has a real groupoid arrow to its pure
periodic tail; two pure periodic tails have equal forward shifts exactly
when their minimal marked closed words differ by cyclic phase. Actual
time translation aligns real coordinates, and commuting translation
past arrows introduces no further identification. Here primitive means
not a proper power as a marked closed word, not vertex-simple. Finite
transient prefixes and cyclic starting points are retained representatives
of the same packet, not additional multiplicities or deleted states.

The strengthened Proposition 5 is also correct. A primitive word of
length h>=2 has B equal to a product of at least two integers >=2,
so B cannot be prime. Thus a packet of least time log p must have h=1;
the exact self-loop calculation then makes it unique. This classifies
the log-prime stratum, not all longer cycles or all coincident lengths.

The non-coboundary statement is valid pointwise on the full groupoid:
a globally defined endpoint potential vanishes on isotropy, but the
prime-loop isotropy arrow has c=log p. This does not classify measurable
almost-everywhere cohomology or ergodic type, and the manuscript makes
no such claim. Nonzero owned clocks do not remove the mixed-packet stop.

The narrow source citation was checked directly against Aidan Sims,
[Hausdorff étale groupoids and their C*-algebras, Examples 2.4.6–2.4.7](https://www.aidansims.com/papers/Sims2017.pdf).
Those examples provide the local-homeomorphism and graph-groupoid
terminology. The graph source/range naming is reversed relative to
this manuscript's outward convention, as the manuscript explicitly
notes. No onto-shift assumption, C*-algebra theorem, trace construction
or old GPF completeness result is needed or imported into these proofs.

## Checkpoint 3 — final adverse checks and disposition: PASS

| Strongest objection | Resolution |
| --- | --- |
| Null periodic paths might have arbitrarily assigned prime clocks | The full-support continuous branch Jacobian, not a singleton derivative, fixes these values. |
| A root or parallel edge might have been silently removed | All root components and marked cylinders remain; groupoid equivalence, not deletion, relates eventual tails. |
| Degree-period one might shorten the alternating return | Returns require identical marked tails. Its lag subgroup is 2Z, not Z. |
| Equal time might identify the mixed word with a prime repetition | Actual forward tails differ, hence no groupoid/time equivalence exists. |
| Unique log-prime packets might imply a prime-only ledger | It does not: the independent primitive log25 and log210 packets remain. |
| Non-coboundary or Hausdorff arrow spaces might justify geometric/Route promotion | Neither gives naturalness, embedded coarse circles, a trace owner or any formal Route result. |

Required changes: **none**. The same-object ledger is intact. Retain
the scoped non-atomic source/clock result, but **stop target promotion
and fork** on the first mixed primitive. Naturalness is OPEN; T3 is
NOT SUPPLIED / NOT PURSUED. Classical fields are NOT APPLICABLE,
formal coordinates UNASSIGNED and Route B NOT INVOKED. This is a bounded
negative target audit, not a no-go theorem for all non-atomic arithmetic
dynamics or a full enumeration of this graph's cycles.
