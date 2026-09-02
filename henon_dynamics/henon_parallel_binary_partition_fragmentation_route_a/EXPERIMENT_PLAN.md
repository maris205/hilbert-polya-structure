# Exact-evidence plan

## Analytic target

Couple `t` successive updates by assigning each label an independent uniform
binary word of length `t`.  Equal-word fibres inside each initial block should
give the full semigroup kernel.  From a one-block start this becomes classical
finite occupancy, while absorption is the event that all words are distinct.

For the spectrum, order labelled partitions by rank.  The transition matrix is
triangular with scalar rank blocks, but diagonalizability must be closed by an
invariant-flag lowering argument and a squarefree annihilating polynomial.

For the critical window, expand

`log((q)_n/q^n) = sum_{j=0}^{n-1} log(1-j/q)`

under `n^2/q -> lambda`, and retain the integer-time/dyadic subsequence phase.

## Finite certificate

- Enumerate every labelled set partition for `1 <= n <= 6` using canonical
  restricted-growth strings.
- Store every nonzero one-step transition probability exactly.
- Store block-count, expectation, absorption, trace, and multiplicity rows for
  `1 <= n <= 9`, `0 <= t <= 8`.
- Store absorption masses through `t=12` for `1 <= n <= 8`.
- Independently reconstruct the kernel by the refinement predicate rather than
  importing the producer.
- Use SymPy to check characteristic polynomials, source determinants,
  annihilators, eigenspace dimensions, and semigroup entries through `n=5`.
- Replay the producer twice byte-for-byte and run semantic/parser mutations.

## Paper and release gates

Round 0 states the coupled kernel and distribution proof.  Round 1 adds the
spectral gap closure and lattice-safe limit.  Round 2 adds exact evidence,
source collision, hostile Route-A evaluation, model-mutation boundaries, and
AI disclosure.  Each round is built twice under epoch `1788307200`.  Release
requires embedded fonts, no LaTeX layout/reference warnings, exact YAML-tree
equality, and a closed 27-file payload ledger.
