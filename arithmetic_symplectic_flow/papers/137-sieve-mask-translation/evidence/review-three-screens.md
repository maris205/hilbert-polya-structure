# Bounded mathematical review of screens 135–137

**Date:** 2026-09-14.  
**Reviewer context:** separate AI subagent /root/review_cycle_three.  
**Scope:** exact proofs, frozen ownership, clock and multiplicity, and the
strength of positive and negative conclusions in the three cards and papers.
This is model-assisted checking, not human peer review, a calibrated review
panel, independent error-process evidence, a novelty determination, or a
formal Route evaluation. The reviewer received the integration task and its
requested risk areas; the review was not blinded to the intended gate decisions.
No manuscript was edited and no new candidate was constructed.

## Outcome

No blocking mathematical defect was found in the scoped claims reviewed.
All three stop/fork decisions are supported on their frozen definitions.
This clearance is limited to the arguments below; it does not turn these
screens into classical A0/A1/A2 results. Route B remains NOT INVOKED.

| Candidate and reviewed paper | Retained positive result | Decisive scoped stop |
| --- | --- | --- |
| ASFS-SCOUT-20260914-98, [135 parity toggles](../../135-divisibility-parity-toggles/paper.md) | Both infinite simultaneous half-steps are involutions; the prime-support state is retained at the correct half-step | F and its inverse are discontinuous in the frozen product topology; the rank-initial source orbit is nonperiodic |
| ANG-20260914-FAC01, [136 factorization paths](../../136-factorization-nonbacktracking-flow/paper.md) | Locally compact shift/groupoid, complete clock, and genuine composite-product periodic packets | The entire prime-product fibre X_p is empty |
| ANG-20260914-SBT01, [137 sieve-mask translation](../paper.md) | Exact full prime displacement and genuine closed orbits coexist on one owner | Uniform length-two packets have continuum multiplicity; the ordinary unweighted product fails |

## 135: simultaneous toggles and source timing

The rank convention is now explicit: number of vertices in a strict chain,
so primes have rank one. Its identification with Omega is proved from
integer factorization rather than supplied as a prime table. Cover neighbors
have opposite parity, which is exactly the fact needed by Proposition 1.

The eligibility condition depends on cover neighbors, not on the toggled
vertex's current membership. Since those neighbors all have the opposite
parity, none changes during a half-step. Thus eligibility is invariant under
that half-step and toggling twice restores every coordinate. Preservation
of every cover inequality also preserves every divisibility inequality,
because every divisibility interval is finite. This justifies the infinite
simultaneous operation directly; no unjustified infinite-composition limit
is needed.

For Proposition 2, downarrow(2q_j) converges coordinatewise to {2}, but the
present upper cover 2q_j blocks removal of 2. The following even half-step
cannot change coordinate 2. The inverse counterexample at coordinate 4 works
for the same reason with downarrow(4q_j). These are genuine counterexamples
on the frozen carrier, not artifacts of a finite boundary.

Proposition 3's boundary cases also check: F(I_0)=I_2, F(I_1)=I_0, and
F(I_3)=I_1. The displayed two-sided chain of rank-initial ideals is consistent
with the proved bijection. The paper correctly refuses to call F(empty)
itself the prime indicator and correctly retains P as a fixed-point control.
No inference from source escape to absence of all periodic states is made.

## 136: topology, arithmetic fibres, and packet counting

For each fixed n, the word-length bound and bounded entries give a finite
graph. The allowed bi-infinite paths form a closed subset of a finite-alphabet
product, hence a compact fibre X_n. In the full countable alphabet, the
coordinate-zero component condition is open and closed; all paths stay in
that component. Therefore the claimed topological disjoint union and local
compactness follow. The shift and its inverse preserve the defining local
constraints. No global finite-alphabet assumption was used incorrectly.

The unit-roof return argument in Proposition 2 compares the same suspended
point: returning to its height forces integer elapsed time, and returning to
its base state imposes exactly the shift period. This proves the stated
primitive/repeated clock law, with orientation and cyclic phase left intact.

For a prime p the sole word (p) has no edge, so no coordinate of an edge path
can be filled. X_p is therefore empty. Proposition 4's complete graph at n=8
has exactly the four listed vertices and four listed edges. Each directed
edge forces a unique two-sided nonbacktracking traversal; the eight paths
split into two length-four shift orbits. No phase or orientation factor is
missing from the count.

The negative conclusion is properly restricted to prime PRODUCT fibres.
It does not exclude prime factors as observables on composite fibres, nor
prove that every conceivable prime-to-packet construction on a different
rule is impossible. No determinant is inferred after the frozen stop.

## 137: positivity, conjugacy, and the complete product

The divisor test proves c_n equals the prime indicator at every integer
coordinate. This is a valid full arithmetic readout without a supplied prime
table. It is nonetheless a fixed forcing word; the proof does not establish
state-dependent generation or an endogenous prime-selective clock. Keeping
T1 PARTIAL preserves this distinction without erasing the positive result.

Since c_2=1 and T squared is the identity, every point has exact period two.
The coordinate-2-zero section is used only to count all orbits, not to select
a preferred subfamily. Every orbit meets it once, so the continuum packet
count and the same-suspension lengths 2 and 2r are correct. The full 2Z
isotropy is explicitly retained in the transformation groupoid.

The conjugacy H is invertible and continuous in both directions. Its
calculation gives a two-point flip times the identity, but H contains c.
Transporting the distinguished displacement observable through H leaves
the same constant prime word. The manuscript correctly limits its genericity
claim to unlabelled dynamics and period data, rather than asserting that a
conjugacy destroys labelled arithmetic information.

The ordinary product is unambiguous as a net over finite subsets of the full
packet set. For real s>0 every factor equals one fixed number greater than
one, and subsets of arbitrarily large finite cardinality make the products
unbounded. This proves the stated failure of the usual right-half-plane
product construction without pretending to classify every possible measured,
weighted, regularized, or operator-valued alternative.

## Integration cautions, not additional defects

- Preserve the source-level arithmetic and algebraic positives when shortening
  the portfolio summary. None of the three papers proves that its arithmetic
  content is entirely absent or externally fabricated.
- Do not combine 135's prime half-step, 136's finite composite packets, and
  137's continuous action into one candidate. Their mutually different maps,
  carriers and packet ledgers have remained separate in the reviewed text.
- Other periodic ideals in 135 and alternative analytic constructions in 137
  remain outside the proved negative scope. Their unresolved status is not a
  reason to prolong these already stopped screens.

## Reviewed input identity

The following SHA-256 values bind this check to the cards and papers read.
They were obtained using sha256sum on the six explicit files. Later edits
should be compared for whether they alter a checked claim; metadata changes
alone do not require a new mathematical audit.

| Input | SHA-256 |
| --- | --- |
| 135 candidate-card.md | 4e55ace599b66186b76850b01d3ab6272c3f3146ce08c96da058d8a29f03d20a |
| 135 paper.md | 16305b62c1aa1f721370331e3d8ce26a06a3d139814565c784d03bb90fd33556 |
| 136 candidate-card.md | 46b23fb661ed1fba1cc4999cdd965326db53c336693c30c2946227dfe180e169 |
| 136 paper.md | d975f57329eeea4966541081b380ad41ddfde6938ae6b65b647278882b3f0c71 |
| 137 candidate-card.md | fda61b499a62ab1e855d5ac826613ecb71238bdff5ff39d9b461270c25e6d0c1 |
| 137 paper.md | f86329e333c9d22b61e59f30c2537c0203c182c50955abd28455cce9769d5c0a |

This audit uses elementary local proofs and asserts no external theorem or
literature-wide novelty claim. No numerical experiment, external upload,
or formal Route evaluation was performed.
