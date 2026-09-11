# Fresh67: relation closure and Ferrers transpose-erasure

2026-09-11 UTC. Author: current_round_independent_scout.
**ZERO NOMINATIONS / NO PILOT / NO RESERVE.** Two materially different
finite carriers were considered. The exact adapters below stop both before
SCI source preparation or execution. No old-factor exception is assumed.
No extra agents, imports, central/live-paper edits, numbering or Git actions.

## A. Complement of reflexive-transitive closure

Fix n>=0, V=[n], and the carrier of every relation R subset V×V, loops
allowed. Let c(R) be reflexive-transitive closure and C complement relative
to V×V. Define T=Cc. This is the full closure, not one Boolean square and
not a silently acyclic restriction.

### Complete temporal deduction and why it does not qualify

For any monotone extensive idempotent closure c on a power set, put i=CcC.
Then i is monotone, contractive and idempotent. Pointwise operator order gives

    icic <= icc = ic,       icic >= iic = ic.

For the first inequality insert i<=id in the middle; for the second insert
c>=id between the two i's. Thus (ic)^2=ic and, since T²=ic, T⁴=T².
Every orbit has entrance time at most two and period dividing two.
This proof does not use reachability, vertex labels or even finiteness.
The entire temporal identity is a generic closure/interior mechanism.

For this literal, n=0 or 1 has one recurrent point, the empty relation,
and maximum entrance time respectively 0 or 1. For n>=2 there are no fixed
points: T(R)=R and extensivity would force R disjoint from itself, hence
R empty, but T(empty) is the nonempty off-diagonal relation. Every recurrent
orbit therefore has period two. At n=2 all T-images are already recurrent:
the possible closures are the diagonal, the two reflexive total orders and
the full relation; their complements form two two-cycles. Maximum entrance
time is 1, attained by the diagonal relation. At n>=3 maximum entrance time
is 2: take R={(1,2)}. The complement of its closure has every off-diagonal
edge except (1,2), is strongly connected via vertex 3, and is neither empty
nor the complete off-diagonal relation. Its next image is empty, after which
empty and the complete off-diagonal relation alternate. R is not on that
two-cycle, so the entrance time is exactly two. No computation was used.

### Evaluated inverse, with standard mechanisms explicitly deducted

For target Y put Q=C(Y). The fibre is empty unless Q is a preorder. If Q
is a preorder, partition V into its equivalence classes under mutual
Q-reachability, and let P be the strict quotient poset. Write b_A=|A|.
Then the full fibre cardinality is

    product_A s(b_A)
      * product_{A covered by B in P} (2^(b_A*b_B)-1)
      * product_{A<B in P, not a cover} 2^(b_A*b_B).

An empty product is one, so this includes n=0. Here s(b), including free
loops, is given explicitly for b>=1 as follows. Let H_b be the family of
all nonempty proper subsets of [b], and U(F) be the union of A×([b]\A)
over A in F. Then

    s(b) = 2^b * sum_{F subset H_b} (-1)^|F|
                          2^(b*(b-1)-|U(F)|).

In particular H_1 is empty and s(1)=2. This is a finite inclusion–exclusion
formula, not an unevaluated strongly-connected graph count or transfer matrix.

Proof: inside each equivalence class the chosen directed edges must induce
a strongly connected graph; no path can leave and return to a quotient
class. A finite directed graph is strongly connected exactly when every
nonempty proper vertex subset has an outgoing edge. Inclusion–exclusion for
the events that all edges in such a cut are absent gives the formula for s.
Loops are independent. Between classes, edges may point only along P.
Every quotient cover needs at least one cross edge, because no intermediate
class can realize that reachability; these conditions also suffice, by
concatenating a saturated cover chain and using internal strong connectivity.
Noncover comparable pairs are free. All edge groups are disjoint, proving
the product and its nonredundant predecessor parametrization.

This separate inverse is fully evaluated, but consists entirely of ordinary
strong-component decomposition, cover generators and cut inclusion–exclusion.
It does not make the generic two-step temporal identity a substantive new
time mechanism. No fibre extremum or special graph enumeration advance is
claimed; the formula is not presented as globally novel.

## B. Ferrers transpose followed by column erasure

The finite carrier is all partitions in an m×m box. Let J be conjugation
(diagram transposition), E delete the first column, and T=EJ. Coordinates
are T(lambda)_i=max(lambda'_i-1,0), with zero parts removed. Both operations
preserve the box. Write D for first-row deletion. Since JEJ=D,

    T²=EJEJ=ED,
    (T²(lambda))_i=max(lambda_{i+1}-1,0).

The latter is exactly fresh45's diagonal-deletion Q on the same carrier,
not merely an analogy. The relevant original section B in
`../finite_residual_fresh45/DESK.md` was reread: it already supplies Q's
Durfee clock and all-target free-border inverse. Odd iterates here only add
the known transpose/one-column operation. This is a square-root wrapper of
that old map, not a candidate with an authorized old-factor exception.
No new time theorem, pilot, or extra parameter variant is pursued.

## Evidence and subtraction limits

Project skill/workflow and latest stream/batch context remain controlling;
the current last seat is not filled by either calculation. Searches were
narrow semantic navigation, not whole-history reading or archive clearance.
Actual original reads in this desk: fresh45 section B and
`docs/papers204_208_sequence/scouting/set_partition_sixth/PROOF_BOUNDARIES.md`
sections 1, steps 1–4. The latter's UPC is the distinct unique-path map on
order-respecting DAGs. Its closure strata and cover/free-shortcut inversion
are deducted; UPC is not falsely identified with A. Its N(S)=Q\up(S)
adapter is another already-recorded complement-of-closure mechanism.

Primary paper actually opened:
[Gardner and Jackson, The Kuratowski closure-complement theorem](https://www.theoremoftheday.org/Topology/Kuratowski14/Gardner-Jackson-The_Kuratowski_closure-complement_theorem.pdf).
The opening definitions and operator proof on printed pages 1–2 were read.
They establish the classical closure/complement reduction mechanism. Our
displayed inequalities explicitly show why the needed identity requires
only Moore closure axioms; reflexive-transitive closure is not asserted to
be a topological closure. The 35-page paper was not read in full, and two
later text-find requests returned no match, not evidence of absence.
General web discovery of transitive closure or partition conjugation is not
attributed an unread theorem or used as novelty clearance.

## Handoff

All displayed mathematics is author desk work, not independent review.
Two separate inverse ingredients in A do not cure its fully generic time
mechanism; B has an exact old-square adapter. Therefore no SCI source,
fixed tinybox, import, execution or gate request is prepared. Only this desk
was written; all old evidence remains unchanged. Root owns integration.
HOLD_EXTERNAL remains in force.
