# Source and collision audit — HCS-C302

## Verified literature owners

1. C. A. R. Hoare, “Quicksort,” *The Computer Journal* 5 (1962),
   10--16, DOI
   [10.1093/comjnl/5.1.10](https://doi.org/10.1093/comjnl/5.1.10).
   The Oxford Academic record verifies the algorithm, author, issue, date and
   pages.  This is the algorithmic owner token.
2. M. Regnier, “A limiting distribution for quicksort,” *RAIRO --
   Theoretical Informatics and Applications* 23 (1989), 335--343,
   [NUMDAM record](https://www.numdam.org/item/ITA_1989__23_3_335_0/).
   The journal archive verifies the author, title, year, volume and pages and
   owns the early centered limiting-distribution result.
3. U. Rosler, “A limit theorem for Quicksort,” *RAIRO -- Theoretical
   Informatics and Applications* 25 (1991), 85--100,
   [NUMDAM paper](https://numdam.org/item/ITA_1991__25_1_85_0.pdf).
   This primary paper proves convergence to a recursively characterized
   contraction fixed point and gives moment recurrences.

ASCII spellings are used in machine-readable artifacts; the manuscript uses
the authors' accented names where the LaTeX encoding is stable.  C302 claims
no priority for Quicksort, its finite cost recurrence or the contraction
method.  It exposes a self-contained derivation for the frozen cost model.

## Workspace collision scan

The C289 idea ledger explicitly recorded Quicksort as surviving collision
screening.  A full C1--C298 title/registry scan found no Quicksort package.
C291 is the nearest formal neighbor because its first-event decomposition
also gives a polynomial convolution.  Its state is a jammed random dimer
configuration on a finite path or cycle; C302 recursively splits a random
permutation into independent subproblems and takes a non-Gaussian
distributional fixed point.  Neither theorem implies the other.

## Claim/source separation

- Input size `n`, pivot ranks, comparison counts, PGFs and the fixed-point law
  are source algorithmic/probabilistic data.
- The finite polynomial table checks the recurrence only through a declared
  cutoff; the all-`n` formulas and limit require analytic induction and the
  quadratic-Wasserstein contraction.
- The limit is not called Gaussian: the exact third centered moment is
  nonzero.  The normalization and comparison-only cost convention are frozen.
- A finite PGF is not a target determinant, `n` is not an arithmetic clock,
  and the contraction operator is not a Hilbert--Polya operator.
- No target arithmetic local datum, Euler factor, root number, automorphy,
  target divisor/counting law, functional equation or target zero match is
  asserted.  Route B is not authorized.

Verified on 2026-09-02 under scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
