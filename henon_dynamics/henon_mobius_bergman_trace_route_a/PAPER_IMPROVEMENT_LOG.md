# Paper improvement log

No external reviewer score or model-family independence is claimed.  The two
rounds below are internal evidence-anchored hostile reviews.

## Round 0

The baseline contained the disk geometry, trace-class bound, all-word matrix
formula, Fredholm product, order-sensitive control, and strict scope.  It
compiled to three clean pages and was preserved as
`paper/main_round0_original.pdf`.

## Round 1 — convention and nuclearity audit

- Made the rank-one functional and output norms explicit in the Bergman
  nuclear decomposition.
- Distinguished the function-word matrix convention from the reversed
  composition-operator product convention.
- Explained that the all-word trace sum uses a reversal bijection rather than
  a false termwise equality.
- Wrote the primitive logarithmic contribution before exponentiation.

The rebuilt three-page version was preserved as `paper/main_round1.pdf`.

## Round 2 — trace and convergence boundary audit

- Stated why every word composition operator remains trace class and why its
  trace survives bounded disk-automorphism similarity.
- Added the explicit majorant proving raw product convergence for
  `|z|<1/2`, extended the near-zero identity across that disk by analyticity,
  and separated this from entire Fredholm continuation.
- Verified that the multiplier is well-defined on a primitive cyclic class
  by cyclic invariance of matrix trace and determinant.
- Listed every cyclic rotation of `33366` and supplied an exact injectivity
  argument showing that traces `1344` and `1317` force different weights and
  multipliers.
- Bound the paper to the final `2,561` symbolic checks, 36 repaired-hash
  semantic mutations, and one stale-hash mutation.

The final three-page version is preserved as `paper/main_round2.pdf` and is
byte-identical to `paper/main.pdf`.
