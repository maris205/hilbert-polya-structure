# Paper 28 initial proposal

## Working question

Can one construct an autonomous polynomial symplectomorphism whose iterated
weighted degrees follow a prescribed primitive Newton-selector word, and can
the exact selector itinerary be recovered from its period cocycle?

The intended contrast is with externally switched max-plus schedules,
special cluster patterns, stationary degree matrices, and untwisted
positive-support Hamiltonian shears.  The proposal seeks a proof-first realization theorem,
not an empirical example or a general entropy theory.

## Initial construction

For a rooted primitive pair word of length \(\ell\ge3\), use
\(r=\ell+1\) symplectic coordinate pairs.  A permutation cycles the \(\ell\)
moving coordinates and fixes a star coordinate.  Equal-total positive
exponent supports are assembled from the occurrence sets of the two label
components.  A spike weight moves under the permutation and makes the desired
V exponent the unique maximizer and the desired W exponent the unique
minimizer at every phase.

The autonomous map has the form

\[
 F_{\mathsf w}=\Pi_P\circ T_W\circ S_V,
\]

where \(S_V(q,p)=(q,p+\nabla V(q))\) and
\(T_W(q,p)=(q+\nabla W(p),p)\).  Equal exponent totals remove diagonal drift
from selector comparisons.  The selected weighted-degree matrices are a
permutation plus a rank-one update, so their ordered period product has an
explicit monodromy.

## Initial claim package

The first proposal aimed to establish:

1. a rational-polyhedral normal-fan iff for strict selector words;
2. one autonomous symplectomorphism per arbitrary rooted primitive pair word;
3. strict actual-degree carry and leading-form noncancellation;
4. an exact rank-one ordered monodromy;
5. base-\(\lambda\) recovery of the rooted word;
6. least selector and quotient periods \(\ell\); and
7. exact annihilating recurrences for phase-resolved degrees.

The proposal explicitly did not seek a universal map, fixed dimension,
ordinary total-degree universality, entropy, integrability, a periodic
polynomial state, or scalar-sequence word decoding.

## Risks registered before refinement

The initial design exposed seven proof risks:

- the automatic strict-carry inequality might fail in dimension one;
- a convenient momentum subcone might be mistaken for the exact admissible
  chamber;
- monodromy may recover algebraic support data but not arbitrary human labels;
- position and complete-state scalar degrees may have different initial
  recurrence ranges;
- the fixed star coordinate may be accidentally included in a moving-index
  congruence;
- a singleton selector alphabet has no finite best-competitor gap; and
- adjacent literature on weighted-degree chambers and affine-triangular
  automorphisms may narrow the novelty statement.

Each risk is theorem-critical.  The proposal therefore required adversarial
review before any paper number or project could be opened.

## Initial public value estimate

If all risks closed, the conjunction would support a 22--30 page proof-first
article: an explicit arbitrary-word realization, an exact normal-fan
classification, coefficient-uniform actual-degree survival, and a lossless
phase-resolved monodromy code.  If any quantifier or recurrence range failed,
the claim would be narrowed or stopped rather than patched by computation.

## Evidence boundary

No numerical experiment, code, CAS output, broad finite search, or private
dataset was proposed.  Literature misses were to be described only as a
bounded search gap.  Exact fixtures could refute formulas but could never
establish the universal theorem.

BATCH07_PAPER28_INITIAL_PROPOSAL_FROZEN
