# Experiment plan

## Exact claims under audit

1. The pair average uses unordered pairs, uniform angle measure, and generator `N(I-Q_N)`.
2. Sphere even moments agree with the exact Dirichlet/gamma formula.
3. The conditional operator `K_N` has the predicted degree-0 through degree-8 triangular matrices and eigenvalues.
4. Exact Gram and `Q` quadratic-form matrices on a degree-eight polynomial test space are symmetric and preserve constants.
5. The centered quartic has the predicted `Q_N` eigenvalue.
6. `kappa_N`, `mu_N`, the induction factor, and the telescoping gap agree exactly.

## Frozen grid

- `K_N` rows for `N=3,...,12` and even degrees `0,2,4,6,8`.
- Gap and quartic rows for `N=2,...,12`.
- Exact Gram/`Q` forms for `N=2,...,7` on all even monomials in the first at most three coordinates of total ordinary degree at most eight.
- A disjoint symbolic check of the pair-angle average, sphere moments, conditional spectrum, product, and centering.

## Acceptance gates

The producer and checker use independently written polynomial actions.  JSON and YAML reject duplicates, nonfinite values, aliases, merge keys, non-string keys, timestamps, unknown/missing fields, and typed-invariant changes.  Repaired-hash theorem, normalization, matrix, provenance, and Route-A mutations must fail, as must `python -O`.  Three substantively different manuscript rounds must build twice identically under LuaLaTeX with no warning, overfull box, undefined reference, control character, or missing glyph; fonts must be embedded and subset.
