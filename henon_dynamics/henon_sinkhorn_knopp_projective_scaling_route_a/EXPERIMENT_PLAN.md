# C191 exact-regression plan

The experiment is an executable theorem sentinel, not empirical evidence for
the all-matrix claim.

## Producer path

1. Enumerate every order-two and order-three binary zero pattern with no zero
   row or column.
2. Classify support by positive permutations, total support by edge coverage,
   and full indecomposability by the strict Hall condition.
3. Construct four positive rational matrices from known doubly stochastic
   targets and declared positive diagonal factors, including a nonsymmetric
   target that distinguishes $S^TS$ from $S^2$.
4. Store exact Fraction iterates, marginal errors, target distances,
   cross-ratios, projective diameters, Birkhoff bounds and `S^T S` spectra.
5. Add four hostile boundary matrices: support-not-total,
   total-not-fully-indecomposable, fully indecomposable with zeros, and no
   support despite nonzero rows and columns.

## Independent checker path

The checker does not import producer code.  It uses augmenting-path matching,
forced-edge matchings and bipartite connectivity, then independently rebuilds
every scaling identity and iteration.  This differs from the producer's
permutation and strict-Hall implementation.

## Symbolic path

SymPy reconstructs the two-by-two closed form, the logarithmic Jacobian,
Ryser permanents, every positive scaling identity, every local characteristic
polynomial and every stored exact iterate.

## Integrity gates

- byte-for-byte isolated replay;
- repaired-payload-hash mutations of metadata, sources, theorems, Route
  labels, patterns, factors, spectra, iterates and boundaries;
- one stale-hash attack;
- two content-changing manuscript revisions after the original draft;
- two fresh fixed-epoch PDF builds, font embedding, clean logs and rendered
  page inspection.

The kill condition is any attempt to infer an all-matrix theorem from the
finite pattern census or to turn convergence into primitive-orbit arithmetic.
