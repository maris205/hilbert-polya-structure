# Executable evidence plan

## Frozen regression domain

- `b=1,...,8`;
- `a/b=j/8`, `j=0,...,7`;
- `nu in {0,1/3,1,2,5}`;
- stationary moments through order ten;
- window-variance Maclaurin coefficients through order ten;
- Borel rows through cluster size twenty for eight branching ratios;
- six explicit boundary cases.

This gives 320 stable parameter cases, 3,520 moment cells, 3,200 window
coefficients, 160 cluster rows, and six boundary rows.  These rows are
regression oracles, not a replacement for the all-parameter proof.

## Independent validation

1. The producer evaluates the generator recurrence and closed covariance
   formulas with exact rational arithmetic.
2. The checker imports no producer implementation.  It reconstructs every
   coefficient of `G(x^n)`, recomputes all three covariance receipts, and
   verifies Borel coefficients from rooted-tree counts.
3. SymPy independently checks the affine generator coefficients, stationary
   cumulants, Fourier transform, window ODE, and stored rows.
4. Replay runs the producer in two fresh temporary directories and requires
   fresh/fresh/release byte equality.
5. Mutation testing repairs the payload hash after semantic changes and also
   contains a stale-hash control.

## Release gates

- source/evaluator/epoch/scope lock;
- every scope flag false and Route B disabled;
- three substantively different deterministic PDFs;
- final PDF byte-equal to round 2;
- extractable text, embedded/subset fonts, no settled warnings;
- 27 payloads plus one self-excluded manifest.
