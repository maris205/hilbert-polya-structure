# Independent internal review — ERI01

**Candidate:** `ANG-20260919-ERI01`. **Date:** 2026-09-19.
**Reviewed status:** `OWNED RESIDUE CLOCK; ALL-INTEGER NULL-STRATUM PACKETS — STOP / FORK`.
**Verdict:** PASS for the bounded exact proof and stop record.
No blocking error or required manuscript change was found. The prime-only
target fails; this verdict does not admit a promising main candidate.

## Inputs, procedure and review limits

| Input | SHA256 |
| --- | --- |
| Version-1 raw card, read before the manuscript | `e0e694646b266857f6e3f4e72c93f7add69bd4e7cf0b6fe97cfb442a581d21b6` |
| Manuscript reviewed | `bc69cf70413c8e4a9114a71a56ca4b1b6b4a788b012d9d87498fcc8ba6385afc` |

The reviewer derived the path descent, atomic/null decomposition, full
image clock, isotropy and packet controls from the raw card, and sent
those results before reading the manuscript. Checkpoint 2 compares the
manuscript against that earlier derivation; it is not claimed to be blind.
A bounded auxiliary model check received only the graph/measure/clock
definitions and controls, not files or manuscript, and confirmed the
reviewer's atomic-boundary and return conclusions.

ARS academic-research-suite's deep-research devil's-advocate procedure
organized the three checkpoints. No numerical census, extra cycle search,
new candidate, T3 construction, operator or formal Route evaluation was
performed. Hash checks are document binding, not scientific experiments.
Shared model lineage and context limit this internal review: it is not
external peer review, human certification, formal proof verification or
a guarantee of independent errors.

## Checkpoint 1 — independent raw-card derivation: PASS

**Complete path classification within scope.** Successive vertices divide
their predecessors. Every nonzero allowed mark strictly lowers n because
gcd(n,j)=n in 0<=j<n is equivalent to j=0. There are only finitely many
strict decreases. Hence every path is a finite marked prefix followed
by the unique zero-mark loop at a terminal d dividing its initial root.
This proves countability of the entire path space: finite marked words
form a countable set and each terminal constant tail is determined by d.
It is an exact descent argument, not an orbit census or a selected core.

Finite nonempty branching gives compact metrizable zero-dimensional
root spaces with compact-open cylinders. Their countable coproduct is
locally compact Hausdorff and second countable. Sigma restricted to a
first-edge cylinder is a homeomorphism onto the target root space. It
is onto: prefix (n,0) to any path rooted at n. This does not make sigma
globally injective or permit replacing the groupoid by a Z-action.

**The measure's precise atomic boundary.** Compatible equal child masses
give a unique rooted probability; summing over all roots gives full
support and sigma-finiteness. Compact sets meet finitely many open root
components, so componentwise regularity gives a locally finite Radon
measure. The degree-one root is included throughout.

Let A be paths eventually reaching 1. If alpha reaches 1, its cylinder
is a singleton with mass 1/D_alpha. If a path eventually stays at d>=2,
its cylinder masses are D_alpha^(-1)d^(-r), tending to zero. These are
all cases by descent. Since X is countable, the zero-mass complement
X\A is null. Thus the measure is purely atomic, although not every
point has positive singleton mass. Every finite prefix can be extended
to 1, using j=1 when its terminal vertex exceeds 1. A is therefore
dense, open and conull, consisting of isolated positive-mass points.

As an independent check on conullity, from root n>1 and before hitting
1 the current modulus is at most n, so the conditional chance of j=1
is at least 1/n. Avoiding 1 for m steps has probability at most
(1−1/n)^m. No independence of successive moduli is needed. This check
does not authorize removing the null complement from the frozen owner.

**Full groupoid and actual image sign.** Prefix pairs with a common
terminal vertex parameterize compact-open bisections. Equal-lag
intersections refine both prefixes by the same word; matching middle
prefixes gives composition and inversion exchanges prefixes. Source,
range and lag separate distinct triples, giving a locally compact
Hausdorff, second-countable étale groupoid with all lag labels retained.

For any Borel B in the terminal root space, cylinder consistency extends
to mu(alpha B)=mu_terminal(B)/D_alpha. Therefore beta zeta -> alpha zeta
has image Jacobian D_beta/D_alpha and clock log D_alpha−log D_beta,
with the frozen eta-to-xi orientation. Equal-lag representations have
equal changes in their two lengths; their common-tail factors cancel.
The same cancellation proves refinement independence, units and the
cocycle law. Factors from n=1 are exactly 1 and create no exception.

This locally constant clock is continuous. Full support on each branch
domain makes its continuous Jacobian version unique even on zero-mass
paths: a discrepancy would persist on a positive-measure open subset.
No singleton ratio is used at those null points. The extension charts
on G×R give Hausdorff locally compact étale source/range maps, and real
translation is jointly continuous and complete. These claims do not
identify a Hausdorff coarse quotient or an embedded flow circle.

**Actual returns, including the unit.** Beyond a finite prefix, every
path repeats (d,0), so its base isotropy lags are all of Z. The lag-one
clock is log d, and the clock on lag l is l log d. Thus:

| Terminal integer | Base isotropy | Extension fixed-object isotropy | Actual time-return group |
| --- | --- | --- | --- |
| d=1 | Z | Z | {0} |
| d>=2 | Z | trivial | (log d)Z, least positive time log d |

Time returns refer to extension isomorphism classes, not fixed points of
translation on the raw product X×R. In particular unit isotropy does not
make time stationary, and trivial extension isotropy does not prevent
a nonzero isomorphism-class time return at d>=2.

Two paths have equal forward tails exactly when their terminal d agrees.
Finite transients connect by actual prefix arrows to the constant tail,
and time translation aligns the real coordinates. Consequently every
d>=2 gives exactly one cyclic packet; d=1 gives one noncyclic time orbit.
This classification uses terminal d, not the initial root. Constant
4 and constant 2 have different tails, so the primitive time log4 is
not a second traversal of the 2-packet, despite log4=2log2. A path
starting with (4,2) and then staying at 2 is a different path already
in the 2-packet. The 6-packet is likewise primitive, with time log6,
not a prime packet or any integer traversal of one. The composite
control triggers the stop without any additional cycle enumeration.

## Checkpoint 2 — manuscript comparison and scope checks: PASS

Propositions 1–4 match the raw derivation, including countability,
surjectivity of sigma, all roots and marks, degree-one behavior and
the unit extension-isotropy exception. The distinction between an
integer-graph edge and a tail-groupoid arrow is correctly used to
prevent merging the constant 4 and constant 2 paths by divisibility.
The full packet ledger follows directly from the card's descent test.

The full-state/almost-everywhere distinction in Section 5 is correct.
A is invariant under the groupoid because terminal d is invariant under
tail equality. Its points are isolated and have finite positive masses,
so the atomic singleton argument applies to the restricted groupoid:
L(xi)=−log mu({xi}) is finite and c=L(xi)−L(eta) on its arrows.
Every time stabilizer there is {0}. This restriction is conull but is
not the frozen full owner. On the latter, a d=2 isotropy arrow has
c=log2, whereas every everywhere-defined endpoint difference vanishes
on same-point arrows. Thus the restricted potential and the full
non-coboundary conclusion are compatible. No ergodic type is inferred.

The cited [Sims Examples 2.4.6–2.4.7](https://www.aidansims.com/papers/Sims2017.pdf)
were directly read in the preceding source check and serve only the
same terminology role here. Their reversed graph source/range naming
is correctly noted; the current outward-path and image-sign formulas
are proved from this card. No graph C*-algebra result, prior-candidate
clock, arithmetic completeness theorem or operator claim is imported.

## Checkpoint 3 — final adverse checks and disposition: PASS

| Strongest objection | Resolution |
| --- | --- |
| Full support plus pure atomicity might activate 272 on all X | False: the retained terminal-d>=2 points have zero mass. EVERY-point positivity holds only on A. |
| Every point null in 273 might carry over to this graph | It does not: the degree-one tail produces positive isolated atoms and a conull atomic set. |
| Null periodic clocks might be freely reassigned | Full support fixes the continuous branch Jacobian version at those points. |
| A 4-to-2 graph transition might identify their constant paths | A fixed infinite future cannot be changed by a finite-prefix replacement. Their terminal labels differ. |
| A composite period equal to a prime repetition might cease to be primitive | Packet identity and least lag/time decide primitivity; equal numerical length alone does not. |
| Unit isotropy Z might give a period-one physical clock | Its clock is identically zero, so H={0}; the isotropy remains retained. |
| A conull nonreturning restriction might remove the target failure | It changes the full-state owner and discards every positive-return packet. It is not performed. |

Required changes: **none**. Retain the bounded source, clock and measure
boundary results; **stop target promotion / fork** because every integer
d>=2, including composites, supplies a primitive packet. The same-object
ledger remains intact. Naturalness stays OPEN; T3 is NOT SUPPLIED /
NOT PURSUED. Classical fields are NOT APPLICABLE, formal coordinates
UNASSIGNED and Route B NOT INVOKED. This is internal review of a scoped
negative screen, not a no-go theorem for all Euclidean or measured clocks.
