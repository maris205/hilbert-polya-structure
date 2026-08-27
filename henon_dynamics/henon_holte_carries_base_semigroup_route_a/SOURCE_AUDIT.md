# C194 source and scope audit

## Verified classical sources

1. John M. Holte, “Carries, Combinatorics, and an Amazing Matrix,” *American
   Mathematical Monthly* 104(2) (1997), 138--149.
   DOI: `10.1080/00029890.1997.11990612`; stable JSTOR DOI:
   `10.2307/2974981`.
   Theorem 1 is the transition coefficient, Theorem 3 is the common
   diagonalization and base semigroup, and Theorem 4 supplies the inverse/right
   eigenvector matrix.
2. Persi Diaconis and Jason Fulman, “Carries, shuffling, and symmetric
   functions,” *Advances in Applied Mathematics* 43(2) (2009), 176--196.
   DOI: `10.1016/j.aam.2009.02.002`.
   Theorem 1.1 gives the carries/descent marginal relation; Theorems 3.1 and
   3.3 give quantitative convergence statements.

The citation registry and manuscript bibliography each contain exactly these
two records.  Both DOI strings and theorem locators are hash-locked in the
evidence and exact-matched by the checker.

## Ownership boundary

The all-parameter transition, spectrum, eigenvectors, Eulerian stationary law
and semigroup are classical Holte results.  The shuffle relation and
convergence analysis are attributed to Diaconis--Fulman.  This package derives
only elementary finite-dimensional trace/determinant/projector corollaries and
adds an executable release certificate.  It makes no novelty or priority
claim.

## Data and scope boundary

The only data are exact digit counts, carry matrices, Eulerian numbers and
prime/composite base tags.  No target zero table, target prime table, modular
local dataset, Euler factor, root number or automorphy input is present.  Prime
bases are controls, not local arithmetic places.  The scope literal is exactly
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Seven-mode integrity audit

| risk | disposition |
|---|---|
| citation fabrication | CLEAR: two DOI records and precise theorem locators |
| experimental hallucination | CLEAR: every released count is regenerated |
| shortcut reliance | CLEAR: finite rows are regression; sources own all quantifiers |
| bug reported as insight | CLEAR: independent inclusion--exclusion and SymPy |
| methodology fabrication | CLEAR: producer/checker algorithms are explicit |
| frame drift | CLEAR: exact rejected Route-A tuple is retained |
| scope leakage | CLEAR: all forbidden flags are false and mutation-tested |

No external peer review, acceptance score or global literature priority is
claimed.
