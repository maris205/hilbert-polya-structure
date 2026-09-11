# P198 bounded independent contribution gate

2026-09-05 UTC. Decision:
**KILL_CONTRIBUTION_ROOT_REWIRED_LAP_ERASURE / REOPEN_NUMBERED_SEAT**.
Mathematics of the frozen CMM manuscript survives. Independent-paper
admission does not: after an exact full-carrier encoding, its proposed
second engine is filtered least-pair insertion, and its new recurrent
behavior is a generic root rewiring of two already documented LAP forests.

This is a bounded mechanism adjudication for the root's ongoing Review A,
not another full manuscript review, not Review B, and not an author edit.
The frozen P198 package remains a rejected/held research artifact unless
the root adopts a different evidence-backed disposition. Author agreement
in `author_responses/P198_CONSTRAINED_ERASURE_RESPONSE.md` corroborates the
reduction but is not the evidence on which this decision depends.

## 1. Exact admissible-subset conjugacy

Let n=2m+1>=3. A matching has a nonempty monomer set S. Every clockwise
gap between consecutive monomers has odd length, since its interior
vertices are perfectly matched. Conversely each nonempty odd-gap S
determines exactly one matching: on every gap, the even interior path
has its unique dimer tiling. This includes singleton S, whose gap is n.
Thus the monomer map is a bijection, not a quotient.

If S={s_0<...<s_(2k)} with k>=1, the least monomer followed clockwise by
the next is exactly s_0,s_1. The alternating flip removes those two and
leaves all other monomers unchanged. If k=0, the monomer advances by two.
Writing e(S)=S minus its least element gives the full conjugate rule

$$F_S(S)=e^2(S)\ (|S|>=3),\qquad
F_S(\{a\})=\{a+2\pmod n\}.$$

Admissibility persists under deletion because the merged wrap gap is a
sum of three odd gaps. This is a restriction of e^2 off the singleton
boundary plus a separately specified recurrent boundary rule. **It is not
a conjugacy to unrestricted P100:** the carrier and recurrent periods
are different. No such false global claim is needed for the decision.

## 2. Complete inverse is the old insertion source set, parity-filtered

Let u=min U for an admissible nonempty target. A transient predecessor
must be U union {a,b}, with 0<=a<b<u. The first and last labels of U have
the same parity, since its cardinality is odd and its successive ordinary
gaps are odd. Replacing the wrap gap by three gaps shows admissibility is
equivalent to

$$a\equiv u\pmod2,\qquad b\not\equiv u\pmod2.$$

Write u=2r+epsilon with epsilon in {0,1}. All and only the choices are

$$a=2i+epsilon,\quad b=2j+1+epsilon,\quad 0<=i<=j<r.$$

There are r(r+1)/2. A singleton target additionally receives one singleton
rotor predecessor. This reconstructs every source set and every fibre,
including zero fibres, and immediately yields the support and unique
maximum 1+m(m+1)/2 at singleton n-1. The target dimer-interval proof is
exactly the same source choices in matching notation, not a second
nontransferring mechanism.

P100's binary map is exactly e under subset encoding; the old HF1 scout
explicitly gives the every-time element source set for delete-maximum.
Order reversal gives e, and at time two the source set of a nonempty
target is precisely arbitrary two-label insertion below its minimum.
HF1's binomial count is filtered by the displayed parity condition here.
The parity filter is not falsely said to appear verbatim in HF1; its
entire extra calculation is the two-line triangular sum above. HF1's
powerset lift is likewise not identified with CMM.

## 3. Stronger exact decomposition: two LAP forests, then root rewiring

Let H be the map that holds maximum cycle matchings and otherwise performs
the same flip as CMM. Before the maximum shell, the selected arc lies
between the two least numeric monomers and never crosses e_(n-1).
Therefore the wrap-edge bit is invariant under H on the entire carrier.

- If the wrap edge is absent, delete that absent cycle edge. The carrier
  and update are exactly LAP on P_n, with original labels 0,...,n-1.
- If the wrap edge is present, its endpoints 0,n-1 are matched forever
  under H. Remove that dimer and relabel vertices 1,...,n-2 by subtracting
  one. The remaining carrier and update are exactly LAP on P_(n-2).

In binary edge coordinates, the second embedding is
`p -> (1 << (n-1)) | (p << 1)`. The odd paths have respectively m+1 and
m singleton-monomer fixed roots, totalling n. Thus **H is exactly the
disjoint union LAP(P_n) plus LAP(P_(n-2))**, and CMM differs from H only
by replacing those n self-loops with the permutation a->a+2 mod n.

Here is the generic root-rewiring lemma. Suppose every orbit of h enters
its fixed set R, and sigma is any permutation of R. Define g=h off R and
g=sigma on R. Every first-entry time into R is unchanged. For a target
outside R its predecessor set is unchanged. For r in R, the predecessor
r itself is replaced by sigma^(-1)(r), while every predecessor outside R
is unchanged. Hence **every labelled indegree, image set, maximal fibre,
equality target and depth layer remains unchanged**. Only the cycles among
roots are replaced by the freely chosen permutation sigma.

This applies literally to H and CMM. Every claimed inverse/extremal/image
quantity is inherited unchanged from the two LAP pieces. The only changed
temporal datum is the inserted n-cycle, already assigned zero standalone
credit by the CMM contract. No independent dynamical interaction with the
transient forest remains after this decomposition.

## 4. Historical boundary and exact level of the kill

Pinned evidence:

- `papers/100-least-valuation-digit-erasure/main.tex`, Sections 1–3:
  least-element clearing, exact digit-sum clock; binary endpoint credited
  to Wegner rather than claimed as new.
- `docs/papers132_136_sequence/replacement_scout/combinatorial/SCOUT.md`,
  Section 5.1: e's order-reversed every-time source sets and binomial
  counts; Section 6 explicitly links the killed erasure engine to P100.
- `docs/papers197_201_sequence/scouting/graph_matching_lane/BREADTH_AND_KILL_LEDGER.md`,
  LAP row: exact deficiency, triangular fibres and image claim; disposition
  KILL_BEHIND_CMM_AP1_GCM.
- That lane's `verify_graph_matching_lane.py`, `lap_step` and `audit_lap`:
  the literal odd/even path map and target formula
  T_floor(min_monomer/2)+1_maximum are explicitly present and checked.

LAP is a **current-batch precursor**, not a falsely asserted pre-P197 paper.
Its old kill says CMM is stronger because of the rotor; this new exact
root-rewiring argument shows why that claimed strengthening gives no new
inverse engine or tail theorem. The decision does not reason circularly
that LAP is killed merely because it is labelled killed. It uses the
explicit e^2 reduction and a generic root-rewiring theorem to show that
all apparent extra CMM structure has already been subtracted.

A bounded search for older least-pair/odd-gap literals found no prior
manuscript with exactly the same whole rule. This is **not** a
KILL_EXACT_EXTERNAL_LITERAL_OWNER verdict. It is a contribution-threshold
kill under the central anchor: stopped restrictions, elementary parity
filtering and generic recurrent rewiring do not restore a materially
independent second axis. Correct mathematics, an existing paper number,
larger boxes and the Stage-1 SELECT cannot waive this criterion.

## 5. Independent verification and findings

The independent verifier imports no author code. It generates cycle
matchings from the two path components, reconstructs the full monomer
bijection, tests literal CMM against subset e^2/rotor, tests H against the
two LAP components, checks every labelled indegree is unchanged, and
enumerates the complete parity-filtered predecessor set for each target.
All odd n=3,...,25 are covered: 271,440 sources and targets in total.
Two fresh processes reproduce 3,257,004 assertions per run.

Finding census for admission: **Critical 1, Major 0, Minor 0**.
Critical C1: the proposed distinct-paper residual collapses under the
exact stopped-erasure / two-LAP / root-rewiring reduction. It is fatal to
the current admission, not a counterexample to its formulas. Confidence:
5/5 within this bounded algebraic claim, based on the explicit bijections,
all-parameter lemma and independent full-box source/target checks.

Required disposition: preserve Round0, reject current CMM seat, reopen
the slot for a genuinely separated map. No author edits are requested to
disguise the reduction, and adding a source disclaimer alone would not
restore the missing contribution. Parent Review A should decide its exact
bookkeeping disposition; this package counts as zero additional paper
reviews. **HOLD_EXTERNAL** persists.
