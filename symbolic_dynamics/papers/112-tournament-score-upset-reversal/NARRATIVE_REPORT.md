# Narrative report — P112

Status: **anonymous working manuscript / external HOLD**.

## Technical story

The system starts from a labelled tournament and recomputes every contest in
parallel from the old outdegree scores.  A contest between unequal scores is
oriented from the higher score to the lower score; a tied contest is retained.
The natural first guess is that this is a score-sorting projection.  Exact
enumeration kills that guess at six vertices: mask `148` follows
`148 -> 4 -> 0`, so two score-refinement rounds can be necessary.  This mask
is called least only for the documented scan by increasing order and then
increasing numerical mask; no global extremal inference is attached to it.

The replacement story is fully proved.  The update is defined on every finite
label set, and every decision uses the unchanged old score vector before all
reversals occur simultaneously.  A signed incidence formula for the aggregate
score change makes the global energy `sum_v s(v)^2` strictly grow whenever an
upset edge is reversed and gives the local criterion `Phi(T)=T` iff no such arc
exists.  At the same time, one update changes only edges between old
equal-score classes and makes them an ordinal sum.  The induced tournaments
inside the classes remain literal copies of the old ones.  Their new global
score intervals are disjoint, so later updates cannot mix old classes and
factor into smaller independent copies of the same rule.

This recursive factorization explains the nonidempotent state.  Before the
tree is defined, a one-score-class tournament is shown fixed; hence each
nonfixed node has at least two strictly smaller children and the recursion is
well-founded.  Restricting two consecutive global iterates to each frozen
block proves that the parent is stable iff every factor is stable.  This gives
the exact `tau` recursion in both directions, identifies depth with tree
height, and yields `tau(T) <= n-1` for `n >= 1`.  The bound is universal, not
claimed sharp.  The energy and recursive routes are independent termination
proofs: one is numerical and global; the other is structural and inductive.

At a fixed point, all edges between score classes already point downward.
Uniform external wins then force each score-class subtournament to be regular.
Conversely, an ordered sum of regular tournaments has strictly decreasing
block scores and is fixed.  The score classes make the decomposition unique.
Choosing the unique top block yields the labelled recurrence, sequence
composition yields the EGF, and absence of nontrivial cycles gives the zeta
function.

## Boundary cases

The empty and one-vertex tournament spaces are singletons.  Both maps are the
identity, both depths are zero, `f_0=f_1=1`, and both zeta functions equal
`(1-z)^(-1)`.  The universal `n-1` depth bound is stated only for `n>=1`.

## Owner subtraction and collision firewall

Every mature component is itemized at zero credit: Landau score sequences;
Moon tournament, regular, and ordinal-sum background; Rubinstein/Henriet
static score ranking and Copeland choice; Bouyssou successive choice;
Linares Lejarraga--Bodanza's current iterative-Copeland procedure; Monsuur
upset statistics; Ryser/Thomassen arc and cycle reversals; the verified ESA
2026 score-sequence neighbor; McKay regular-tournament enumeration; generic
labelled-EGF bookkeeping; and Artin--Mazur zeta.  The recurrence, EGF, regular
counts, and zeta specialization are therefore low-credit corollaries.

After subtraction, only the exact finite-map conjunction for this synchronous
orientation update remains in scope: incidence/energy, permanent blocks,
recursive depth and bound, and the map-specific fixed-set identification.
The bounded search located no exact temporal owner, but that absence is not a
novelty, priority, or owner-clearance certificate.

P106 evolves vertex subsets of one fixed undirected graph under an antitone
MIS neighborhood polarity.  P112 evolves all edges of a complete orientation
using current outdegrees.  Its controls are a quadratic energy and recursive
ordinal sums, not Galois closure.  Regular cyclic tournaments can be fixed in
P112, whereas the recurrent objects in P106 are subset configurations.  The
shared words “synchronous,” “fixed,” and “zeta” carry no contribution credit.

## Deliberate nonclaims

The manuscript does not determine the sharp maximum depth, enumerate every
transient layer, or make a novelty/priority claim.  The `n=6` statement is an
exact scan-qualified finite computation, not an extrapolated theorem.
External circulation, submission, and specialist contact remain HOLD.
