# Evidence — ANG-20260914-FAC01

**Date:** 2026-09-14.  
**Status:** STOP — PRIME-PRODUCT COMPONENTS HAVE NO PATHS.

## Inputs and provenance

The sole mathematical input is the [version-1 frozen card](../candidate-card.md):
all ordered factorization words for every integer n>=2; simple undirected
split/merge graphs; two-sided nonbacktracking oriented-edge paths; the shift;
and unit roof. The direct source lineage is the prime/composite symbolic
recognition and admissibility theme recorded in the
[prior-work guide](../../../docs/prior_work/README.md).

No external theorem, graph-zeta identity, prime table, selected prime modulus,
Riemann-zero data, fitted roof, or numerical precision choice is used.

## Reproduction method and output

All outputs are exact derivations in [paper.md](../paper.md), Propositions 1--4.
No mathematical script or numerical experiment was run.

1. For arbitrary n, bound factor-word length by floor(log_2 n), then merge
   adjacent factors to the root word (n). This proves finite connected graph
   components. Use the finite directed-edge alphabet in each component to
   verify the local compactness and action assertions.
2. Apply the unit-roof formula using k=floor(u+t). A return has integer
   elapsed time and occurs precisely when the corresponding shift fixes the
   full path. This proves the stated primitive and repetition law.
3. For a prime p, a factor word of length at least two contradicts the
   definition of primality. The remaining isolated vertex has no edge and
   supplies no path under the frozen convention. This is an all-prime proof,
   not extrapolation from a prime cutoff.
4. As a complete finite control, list the only words with product 8:
   (8), (2,4), (4,2), (2,2,2). The only edges form C4. Choose any one of its
   eight oriented edges; nonbacktracking forces all other coordinates. The
   eight states divide into two shift orbits of length 4. The reverse orbit
   remains distinct as required by the card.
5. For the negative composite control n=4, the only words are (4) and (2,2).
   The only possible next edge after their connecting edge is its reversal,
   so no bi-infinite nonbacktracking path exists.

The general topological and prime-empty-fibre arguments cover every n where
stated. The exact count of primitive paths covers n=8 alone. There is no
claimed enumeration cutoff for the full graph, global zeta product,
determinant, or trace. T3 is deliberately unassessed after the first
prime-packet stop.

## Ownership and verification limits

All times and packet conventions use the same shift and roof. The simple
graph rule and reverse-orientation convention are essential inputs. Adding
loops, retaining isolated vertices as constant paths, allowing backtracking,
or changing the roof would change the frozen object.

The writing and symbolic proofs are locally auditable; no external peer
review is claimed. Package-link and identity checks are editorial checks,
not proofs. Route B remains NOT INVOKED.

The [separate-context 135--137 check](../../137-sieve-mask-translation/evidence/review-three-screens.md)
found no blocking defect in this carrier, clock, and prime-product-fibre
argument. It is model checking, not external peer review.
